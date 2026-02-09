<<<<<<< HEAD
cat > README.md << 'EOF'
<!-- DFSE README — modern, GitHub-safe, first-person voice -->

<div align="center">

![DFSE — Decision-Driven Forecasting & Segmentation Engine](https://readme-typing-svg.demolab.com?font=Inter&weight=700&size=28&duration=2400&pause=650&color=111827&center=true&vCenter=true&width=980&lines=DFSE+—+Decision-Driven+Forecasting+%26+Segmentation+Engine;Traditional+data+science%2C+delivered+like+real+client+work;Forecasting+%7C+Segmentation+%7C+Reproducible+runs+%7C+Decision-ready+outputs)

<br/>

<img alt="Python" src="https://img.shields.io/badge/Python-3.x-111827?style=for-the-badge&logo=python&logoColor=white"/>
<img alt="Traditional DS" src="https://img.shields.io/badge/Traditional%20DS-Forecasting%20%26%20Segmentation-111827?style=for-the-badge"/>
<img alt="Reproducible" src="https://img.shields.io/badge/Reproducible-Makefile%20%2B%20run.sh-111827?style=for-the-badge"/>
<img alt="CI" src="https://github.com/neilsable/dfse/actions/workflows/ci.yml/badge.svg"/>

<br/><br/>

**I built DFSE as an end-to-end data science deliverable that mirrors how I work under ambiguity:**  
*frame the problem → build robust classical models → publish decision-grade outputs.*

</div>

---

## Why I built this

In real analytics work, the difficult part is rarely “training a model.” Requirements are incomplete, data is imperfect, and stakeholders need clarity.

DFSE demonstrates how I:
- independently scope an under-specified analytical problem,
- choose **interpretable classical methods** over black-box novelty,
- keep code clean and reproducible (Makefile + CI),
- deliver stakeholder-ready artefacts (executive summary, metrics, plots).

---

## Quick demo (what you get)

<div align="center">
  <img src="assets/forecast_plot.png" alt="Forecast vs Actual (holdout)" width="900" />
</div>

### Generated artefacts
**Reports**
- `reports/executive_summary.md` — narrative + recommendations
- `reports/forecast_plot.png` — forecast vs actual visual

**Data outputs**
- `data/processed/forecast_metrics.csv` — MAE / RMSE / MAPE
- `data/processed/forecast_60d.csv` — actual vs forecast (holdout window)
- `data/processed/rfm_segments.csv` — customer → segment assignment
- `data/processed/segment_summary.csv` — segment characteristics

---

## Modelling approach

### 1) Demand forecasting (SARIMAX)
- Weekly seasonality modelled explicitly
- Promotions included as an exogenous driver
- Optimised for **stability + interpretability** so decisions are explainable

### 2) Customer segmentation (RFM + K-Means)
- Features: Recency, Frequency, Monetary value, Average order value
- Standardised inputs + K-Means clustering
- Segments designed to map to actions (retention / win-back / low-touch engagement)

---

## System flow

```mermaid
flowchart LR
  A[Data generation / ingestion] --> B[Feature engineering]
  B --> C1[SARIMAX forecasting]
  B --> C2[RFM + K-Means segmentation]
  C1 --> D[Metrics + forecast plot]
  C2 --> E[Segment summaries]
  D --> F[Decision-ready outputs]
  E --> F
  F --> G[Executive summary]
How to run
Option A — Makefile (recommended)
make run
Option B — One-command script
./run.sh
Option C — Manual
python3 -m venv .venv

# macOS / Linux:
source .venv/bin/activate

# Windows (PowerShell):
# .\.venv\Scripts\Activate.ps1

python3 -m pip install -r requirements.txt
python3 -m src.pipeline
python3 -m src.evaluation
Open outputs (cross-platform)
macOS
open reports/forecast_plot.png
open reports/executive_summary.md
open data/processed/forecast_metrics.csv
open data/processed/segment_summary.csv
Linux
xdg-open reports/forecast_plot.png
xdg-open reports/executive_summary.md
xdg-open data/processed/forecast_metrics.csv
xdg-open data/processed/segment_summary.csv
Windows (PowerShell)
Start-Process reports\forecast_plot.png
Start-Process reports\executive_summary.md
Start-Process data\processed\forecast_metrics.csv
Start-Process data\processed\segment_summary.csv
Engineering & delivery hygiene
Dependencies pinned in requirements.txt

Makefile included for standardised execution

CI runs the pipeline on push/PR to prevent regressions

Synthetic data used for full reproducibility (no private data), while preserving enterprise-like patterns (seasonality, promotions, long-tail customers)

<details> <summary><b>Assumptions & trade-offs</b></summary>
I prioritised interpretability over maximal accuracy to reflect stakeholder needs.

Promotional effects are modelled explicitly to separate demand lift from seasonality.

The project is intentionally focused on traditional data science rather than GenAI.

</details> <details> <summary><b>Repository structure</b></summary>
dfse/
├── src/                 # pipeline + modelling + evaluation
├── data/processed/      # generated outputs
├── reports/             # executive summary + plots
├── assets/              # GitHub visuals
├── sql/                 # Snowflake-style query examples
├── .github/workflows/   # CI
├── Makefile             # make run
└── run.sh               # ./run.sh
</details>
<div align="center">
Built to reflect real analytics delivery — from framing to decision-ready outputs.

</div> EOF ```
=======
# DFSE — Decision-Driven Forecasting & Segmentation Engine

![Python](https://img.shields.io/badge/Python-3.x-111827?style=for-the-badge&logo=python&logoColor=white)
![Traditional DS](https://img.shields.io/badge/Traditional%20DS-Forecasting%20%26%20Segmentation-111827?style=for-the-badge)
![Reproducible](https://img.shields.io/badge/Reproducible-Makefile%20%2B%20run.sh-111827?style=for-the-badge)
![CI](https://github.com/neilsable/dfse/actions/workflows/ci.yml/badge.svg)

A self-directed, end-to-end data science project built to reflect how I deliver under ambiguity: frame the problem, build robust classical models, and publish decision-ready outputs.

---

## What you get

<p align="center">
  <img src="assets/forecast_plot.png" alt="Forecast vs Actual (holdout)" width="900" />
</p>

After running DFSE, you’ll have:

**Reports**
- `reports/executive_summary.md` — narrative + recommendations
- `reports/forecast_plot.png` — forecast vs actual visual

**Data outputs**
- `data/processed/forecast_metrics.csv` — MAE / RMSE / MAPE
- `data/processed/forecast_60d.csv` — actual vs forecast (holdout window)
- `data/processed/rfm_segments.csv` — customer → segment assignment
- `data/processed/segment_summary.csv` — segment characteristics

---

## Approach (high-level)

**Forecasting (SARIMAX)**
- Weekly seasonality modelled explicitly
- Promotions included as an exogenous driver
- Focus on stability and interpretability

**Segmentation (RFM + K-Means)**
- Features: Recency, Frequency, Monetary value, Average order value
- Standardised inputs + K-Means clustering
- Segments designed to map to actions (retention / win-back / low-touch)

---

## How to run

### Option A — Makefile (recommended)
```bash
make run
Option B — One-command script
./run.sh
Option C — Manual
python3 -m venv .venv

# macOS / Linux:
source .venv/bin/activate

# Windows (PowerShell):
# .\.venv\Scripts\Activate.ps1

python3 -m pip install -r requirements.txt
python3 -m src.pipeline
python3 -m src.evaluation
Open outputs (cross-platform)
macOS
open reports/forecast_plot.png
open reports/executive_summary.md
open data/processed/forecast_metrics.csv
open data/processed/segment_summary.csv
Linux
xdg-open reports/forecast_plot.png
xdg-open reports/executive_summary.md
xdg-open data/processed/forecast_metrics.csv
xdg-open data/processed/segment_summary.csv
Windows (PowerShell)
Start-Process reports\forecast_plot.png
Start-Process reports\executive_summary.md
Start-Process data\processed\forecast_metrics.csv
Start-Process data\processed\segment_summary.csv
Engineering hygiene
Dependencies pinned in requirements.txt

Makefile included for standardised execution

CI runs the pipeline on push/PR to ensure reproducibility

Synthetic data is used for full reproducibility (no private data), while preserving realistic patterns

>>>>>>> f3ffe63 (Fix README rendering (remove broken mermaid and stray terminal text))
