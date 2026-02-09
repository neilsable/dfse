cat > README.md << 'EOF'
# DFSE  
## Decision-Driven Forecasting & Segmentation Engine

<p align="center">
  <strong>Production-minded classical data science for ambiguous, real-world business problems</strong>
</p>

<p align="center">
  <em>Forecasting • Segmentation • Evaluation • Stakeholder-ready outputs</em>
</p>

---

## 🚀 Why this project exists

In real consulting engagements, problems are rarely clean or fully specified.

This project simulates that reality: limited documentation, evolving requirements, and a need to deliver **decision-grade insights**, not dashboards or academic models.

DFSE demonstrates how to:
- independently scope an unclear problem,
- apply **rigorous traditional data science**,
- build clean, reproducible pipelines,
- and communicate results in a way stakeholders can act on.

---

## 📊 What this delivers (at a glance)

### Demand Forecasting (60-day holdout)
![Forecast Plot](assets/forecast_plot.png)

**Key artefacts produced:**
- `forecast_metrics.csv` — MAE, RMSE, MAPE
- `segment_summary.csv` — interpretable customer clusters
- `executive_summary.md` — consultant-style narrative & recommendations

---

## 🧠 Modelling approach

### 1️⃣ Forecasting — Classical, interpretable, robust
- **Model:** SARIMAX
- **Seasonality:** Weekly (s = 7)
- **Exogenous driver:** Promotional activity
- **Design choice:** Optimised for *stability and explainability*, not black-box accuracy

Why this matters:
> Stakeholders must trust and understand forecasts before acting on them.

---

### 2️⃣ Segmentation — Commercially actionable clustering
- **Features:**  
  - Recency (days since last purchase)  
  - Frequency (number of transactions)  
  - Monetary value (total spend)  
  - Average order value  
- **Method:** Standard scaling + K-Means

Segments are designed to map directly to actions:
- retention & loyalty
- win-back campaigns
- low-cost onboarding strategies

---

## 🏗️ Project structure

```text
dfse/
├── src/                 # pipelines, models, evaluation
├── data/processed/      # generated datasets & outputs
├── reports/             # executive summary & plots
├── assets/              # visuals for GitHub
├── sql/                 # Snowflake-style analytical queries
├── run.sh               # one-command execution
└── README.md
