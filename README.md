cat > README.md << 'EOF'
# DFSE — Decision-Driven Forecasting & Segmentation Engine
**Traditional data science, delivered like a lean consultancy project**  
Forecasting • Segmentation • Reproducible runs • Stakeholder-ready outputs

<p align="center">
  <img src="assets/forecast_plot.png" alt="Forecast vs Actual" width="900" />
</p>

<p align="center">
  <b>One-command run</b> • <b>Clean repo hygiene</b> • <b>Decision-grade artefacts</b>
</p>

---

## ✅ What this project demonstrates (Snap-aligned)

- **Traditional, rigorous data science** (time series + classical clustering)
- **End-to-end delivery** (data → modelling → evaluation → outputs)
- **Operating under ambiguity** (clear assumptions + tradeoffs documented)
- **Clean, production-minded workflow** (Makefile + CI)
- **Communication** (executive summary + actionable segment framing)

---

## 📦 Outputs you get

After a successful run, you’ll have:

### Reports
- `reports/executive_summary.md` — stakeholder-style narrative + recommendations
- `reports/forecast_plot.png` — clean, readable forecast visual

### Data artefacts
- `data/processed/forecast_metrics.csv` — MAE / RMSE / MAPE
- `data/processed/forecast_60d.csv` — forecast vs actual (holdout)
- `data/processed/rfm_segments.csv` — customer-level segment labels
- `data/processed/segment_summary.csv` — segment-level summary stats

---

## 🧠 Modelling approach (high signal, no fluff)

### 1) Forecasting — SARIMAX
- Weekly seasonality (s=7)
- Promo-day effect as an exogenous regressor
- Optimised for **stability + interpretability** (stakeholders can trust it)

### 2) Segmentation — RFM + K-Means
- Features: Recency, Frequency, Monetary value + Average order value
- Scaled features + K-Means clustering
- Segments designed to map to actions:
  - retention / loyalty
  - win-back
  - low-cost onboarding

---

## 🚀 How to run (pick one)

### Option A — One-command runner (recommended)
```bash
chmod +x run.sh
./run.sh
