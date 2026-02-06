# Decision-Driven Forecasting & Segmentation Engine (DFSE)

## Context
This project simulates a client engagement where documentation is limited and requirements evolve. The objective is to produce decision-grade outputs using traditional, rigorous data science—specifically demand forecasting and customer segmentation—then translate results into actionable recommendations.

## What I built (end-to-end)
- **Forecasting**: A SARIMAX time-series model with weekly seasonality and promo-day effects.
- **Segmentation**: RFM-based customer features (Recency, Frequency, Monetary) plus average order value, clustered via K-Means.
- **Production hygiene**: Reproducible pipelines, modular code, version-controlled repository structure, and evaluation artifacts.

## Key results
- **60-day forecast accuracy**: See `data/processed/forecast_metrics.csv` for MAE/RMSE/MAPE.
- **Operational visibility**: Forecast vs actual plot saved to `reports/forecast_plot.png`.
- **Customer segmentation**:
  - Segment summary: `data/processed/segment_summary.csv`
  - Output includes segment labels per customer: `data/processed/rfm_segments.csv`

## Recommendations (how a client would use this)
1. **Inventory / capacity planning**: Use the 60-day forecast to plan staffing and replenishment cycles; treat promo days as an explicit exogenous driver.
2. **Commercial strategy by segment**:
   - High monetary + high frequency: retention programs, VIP support, proactive cross-sell.
   - High monetary + low frequency: targeted win-back offers and lifecycle messaging.
   - Low monetary: low-cost engagement channels and product onboarding improvements.

## Assumptions and trade-offs
- Optimised for **stability and interpretability** to support stakeholder decision-making, rather than maximizing black-box accuracy.
- Promo effect modelled explicitly to avoid conflating demand seasonality with campaign lift.
- Synthetic dataset used to enable full reproducibility and fast iteration; design mirrors real enterprise patterns.

## Next steps (production hardening)
- Add backtesting across multiple rolling windows and compare models (Prophet, XGBoost with lag features).
- Add automated data quality checks (schema validation, missingness thresholds).
- Package as a CLI entrypoint and containerise with Docker for deployment.
