from __future__ import annotations

from pathlib import Path
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def mae(y_true, y_pred) -> float:
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    return float(np.mean(np.abs(y_true - y_pred)))


def rmse(y_true, y_pred) -> float:
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    return float(np.sqrt(np.mean((y_true - y_pred) ** 2)))


def mape(y_true, y_pred) -> float:
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    y_true = np.clip(y_true, 1, None)
    return float(np.mean(np.abs((y_true - y_pred) / y_true)) * 100.0)


def plot_forecast(fc: pd.DataFrame, out_path: Path) -> None:
    fc = fc.copy()
    fc["date"] = pd.to_datetime(fc["date"])
    fc = fc.sort_values("date")

    # Larger, modern-readable canvas
    fig, ax = plt.subplots(figsize=(12, 6), constrained_layout=True)

    ax.plot(fc["date"], fc["demand"], label="Actual", linewidth=2.0)
    ax.plot(fc["date"], fc["forecast"], label="Forecast", linewidth=2.0, alpha=0.9)

    ax.set_title("60-Day Forecast vs Actual", pad=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Demand")

    # --- Fix the overlapping date labels properly ---
    locator = mdates.AutoDateLocator(minticks=6, maxticks=10)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(locator))
    fig.autofmt_xdate(rotation=30, ha="right")

    # Cleaner look
    ax.grid(True, which="major", linestyle="--", linewidth=0.7, alpha=0.35)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Legend that doesn't block the plot
    ax.legend(loc="upper left", frameon=True)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=220)
    plt.close(fig)


def main():
    root = Path(__file__).resolve().parents[1]
    processed = root / "data" / "processed"

    fc = pd.read_csv(processed / "forecast_60d.csv")
    rfm = pd.read_csv(processed / "rfm_segments.csv")

    # Forecast metrics
    y_true = fc["demand"]
    y_pred = fc["forecast"]

    metrics = {
        "MAE": mae(y_true, y_pred),
        "RMSE": rmse(y_true, y_pred),
        "MAPE_%": mape(y_true, y_pred),
    }
    metrics_df = pd.DataFrame([metrics])
    metrics_path = processed / "forecast_metrics.csv"
    metrics_df.to_csv(metrics_path, index=False)

    # Plot forecast vs actual (fixed formatting)
    fig_path = root / "reports" / "forecast_plot.png"
    plot_forecast(fc, fig_path)

    # Segment summary
    seg_summary = rfm.groupby("segment").agg(
        customers=("customer_id", "count"),
        avg_recency=("recency_days", "mean"),
        avg_frequency=("frequency", "mean"),
        avg_monetary=("monetary", "mean"),
        avg_order=("avg_order", "mean"),
    ).reset_index().sort_values("avg_monetary", ascending=False)

    seg_path = processed / "segment_summary.csv"
    seg_summary.to_csv(seg_path, index=False)

    print("✅ Evaluation outputs:")
    print(f"- {metrics_path}")
    print(f"- {fig_path}")
    print(f"- {seg_path}")


if __name__ == "__main__":
    main()
