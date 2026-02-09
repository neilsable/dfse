cat > README.md << 'EOF'
# DFSE — Decision-Driven Forecasting & Segmentation Engine

A production-minded **traditional data science** project: demand forecasting + customer segmentation, built to simulate ambiguous consulting requirements and produce decision-grade outputs.

**What this demonstrates:**
- End-to-end delivery (data → modelling → evaluation → stakeholder-ready narrative)
- Rigorous classical modelling (time series + segmentation)
- Clean, maintainable Python + SQL-style transformations
- Clear communication: outputs are actionable, not just “model scores”

---

## Outputs (at a glance)

**Forecast vs Actual (60-day holdout)**  
![Forecast Plot](assets/forecast_plot.png)

Key artefacts:
- `data/processed/forecast_metrics.csv` — MAE / RMSE / MAPE
- `data/processed/segment_summary.csv` — cluster characteristics
- `reports/executive_summary.md` — stakeholder narrative

---

## Project structure

- `src/` — pipelines + modelling + evaluation
- `data/processed/` — generated datasets + outputs
- `reports/` — executive summary + plots
- `sql/` — Snowflake-style query examples (illustrative)

---

## Quickstart (local)

### 1) Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

