from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

import statsmodels.api as sm


@dataclass(frozen=True)
class Paths:
    root: Path = Path(__file__).resolve().parents[1]
    raw_dir: Path = root / "data" / "raw"
    processed_dir: Path = root / "data" / "processed"
    reports_dir: Path = root / "reports"

    def ensure(self) -> None:
        self.raw_dir.mkdir(parents=True, exist_ok=True)
        self.processed_dir.mkdir(parents=True, exist_ok=True)
        self.reports_dir.mkdir(parents=True, exist_ok=True)


def generate_synthetic_data(seed: int = 42) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Generates:
    1) daily_demand: daily demand with seasonality + promo effects
    2) transactions: customer-level transactions for RFM segmentation
    """
    rng = np.random.default_rng(seed)

    # --- Demand time series ---
    dates = pd.date_range("2022-01-01", "2025-12-31", freq="D")
    n = len(dates)

    day_of_week = dates.dayofweek.values  # 0=Mon
    month = dates.month.values

    weekly = 10 * np.sin(2 * np.pi * (day_of_week / 7))
    yearly = 20 * np.sin(2 * np.pi * (dates.dayofyear.values / 365.25))
    base = 200

    promo = (rng.random(n) < 0.06).astype(int)  # 6% of days are promo days
    promo_lift = promo * rng.normal(40, 10, size=n)

    noise = rng.normal(0, 15, size=n)

    demand = base + weekly + yearly + promo_lift + noise
    demand = np.clip(demand, 10, None)

    daily_demand = pd.DataFrame({
        "date": dates,
        "demand": demand.round(0).astype(int),
        "promo": promo,
        "dow": day_of_week,
        "month": month,
    })

    # --- Transactions for segmentation ---
    n_customers = 2500
    customer_ids = [f"C{str(i).zfill(5)}" for i in range(1, n_customers + 1)]

    # Each customer: number of transactions ~ Poisson, with a long tail
    tx_counts = rng.poisson(3, n_customers) + (rng.random(n_customers) < 0.10) * rng.poisson(10, n_customers)
    tx_counts = np.clip(tx_counts, 1, 60)

    start = pd.Timestamp("2023-01-01")
    end = pd.Timestamp("2025-12-31")
    days_range = (end - start).days

    rows = []
    for cid, k in zip(customer_ids, tx_counts):
        # customer spend profile
        avg_order = rng.lognormal(mean=3.2, sigma=0.55)  # ~£25-£60 typical
        for _ in range(int(k)):
            d = start + pd.Timedelta(days=int(rng.integers(0, days_range + 1)))
            amount = float(rng.lognormal(mean=np.log(avg_order), sigma=0.35))
            rows.append((cid, d, amount))

    transactions = pd.DataFrame(rows, columns=["customer_id", "date", "amount"])
    transactions["amount"] = transactions["amount"].round(2)

    return daily_demand, transactions


def build_rfm(transactions: pd.DataFrame, asof: pd.Timestamp) -> pd.DataFrame:
    tx = transactions.copy()
    tx["date"] = pd.to_datetime(tx["date"])

    grouped = tx.groupby("customer_id").agg(
        last_purchase=("date", "max"),
        frequency=("date", "count"),
        monetary=("amount", "sum"),
        avg_order=("amount", "mean"),
    ).reset_index()

    grouped["recency_days"] = (asof - grouped["last_purchase"]).dt.days
    grouped = grouped.drop(columns=["last_purchase"])

    return grouped


def fit_sarimax_forecast(daily: pd.DataFrame, horizon_days: int = 60):
    df = daily.copy()
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date").set_index("date")

    # Train-test split
    train = df.iloc[:-horizon_days]
    test = df.iloc[-horizon_days:]

    # Exogenous: promo flag
    exog_train = train[["promo"]]
    exog_test = test[["promo"]]

    # SARIMAX (seasonal weekly)
    model = sm.tsa.SARIMAX(
        train["demand"],
        exog=exog_train,
        order=(1, 1, 1),
        seasonal_order=(1, 1, 1, 7),
        enforce_stationarity=False,
        enforce_invertibility=False,
    )
    res = model.fit(disp=False)

    pred = res.get_forecast(steps=horizon_days, exog=exog_test).predicted_mean
    out = test.copy()
    out["forecast"] = pred.values.round(0).astype(int)
    return res, out.reset_index()


def kmeans_segmentation(rfm: pd.DataFrame, k: int = 5) -> pd.DataFrame:
    feats = rfm[["recency_days", "frequency", "monetary", "avg_order"]].copy()

    scaler = StandardScaler()
    X = scaler.fit_transform(feats)

    km = KMeans(n_clusters=k, n_init=20, random_state=42)
    labels = km.fit_predict(X)

    out = rfm.copy()
    out["segment"] = labels
    return out


def main():
    paths = Paths()
    paths.ensure()

    daily_demand, transactions = generate_synthetic_data(seed=42)

    # Save processed (we are not keeping raw folder in gitignore by default)
    daily_path = paths.processed_dir / "daily_demand.csv"
    tx_path = paths.processed_dir / "transactions.csv"

    daily_demand.to_csv(daily_path, index=False)
    transactions.to_csv(tx_path, index=False)

    # RFM + segmentation
    asof = pd.Timestamp("2026-01-01")
    rfm = build_rfm(transactions, asof=asof)
    segments = kmeans_segmentation(rfm, k=5)

    rfm_path = paths.processed_dir / "rfm_segments.csv"
    segments.to_csv(rfm_path, index=False)

    # Forecasting
    _, forecast_df = fit_sarimax_forecast(daily_demand, horizon_days=60)
    fc_path = paths.processed_dir / "forecast_60d.csv"
    forecast_df.to_csv(fc_path, index=False)

    print("✅ Generated datasets:")
    print(f"- {daily_path}")
    print(f"- {tx_path}")
    print(f"- {rfm_path}")
    print(f"- {fc_path}")


if __name__ == "__main__":
    main()
