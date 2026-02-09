# DFSE — Decision-Driven Forecasting & Segmentation Engine

![Python](https://img.shields.io/badge/Python-3.x-111827?style=for-the-badge&logo=python&logoColor=white)
![Traditional DS](https://img.shields.io/badge/Traditional%20DS-Forecasting%20%26%20Segmentation-111827?style=for-the-badge)
![Reproducible](https://img.shields.io/badge/Reproducible-Makefile%20%2B%20run.sh-111827?style=for-the-badge)
![CI](https://github.com/neilsable/dfse/actions/workflows/ci.yml/badge.svg)

A self-directed, end-to-end data science project built to reflect how I deliver under ambiguity: **frame the problem, build robust classical models, and publish decision-ready outputs**.

---

## What this project produces

<p align="center">
  <img src="assets/forecast_plot.png" alt="Forecast vs Actual (holdout window)" width="900" />
</p>

After a successful run, DFSE generates:

### Reports
- `reports/executive_summary.md` — concise narrative + recommendations
- `reports/forecast_plot.png` — forecast vs actual visual

### Data outputs
- `data/processed/forecast_metrics.csv` — MAE / RMSE / MAPE
- `data/processed/forecast_60d.csv` — actual vs forecast (holdout window)
- `data/processed/rfm_segments.csv` — customer → segment assignment
- `data/processed/segment_summary.csv` — segment characteristics

---

## Approach (deliberately traditional + explainable)

### Forecasting (SARIMAX)
- Weekly seasonality modelled explicitly
- Promotions included as an exogenous driver
- Emphasis on **stability and interpretability** so decisions are explainable

### Segmentation (RFM + K-Means)
- Features: Recency, Frequency, Monetary value, Average order value
- Standardised inputs + K-Means clustering
- Segments designed to map to actions (retention / win-back / low-touch engagement)

---

## How to run

This project is intentionally simple to execute. Most users should only need the first command below.

```bash
# Recommended: run everything end-to-end
make run


# Alternative: explicit single entry point
./run.sh


# Manual execution (useful on fresh machines)

# Create a virtual environment
python3 -m venv .venv

# Activate it
# macOS / Linux:
source .venv/bin/activate

# Windows (PowerShell):
# .\.venv\Scripts\Activate.ps1

# Install dependencies
python3 -m pip install -r requirements.txt

# Run the pipeline and evaluation
python3 -m src.pipeline
python3 -m src.evaluation



I prioritised interpretability over maximal accuracy to reflect stakeholder needs.

Promotional effects are modelled explicitly to separate demand lift from seasonality.

The project is intentionally focused on traditional data science rather than GenAI.


