cat > README.md << 'EOF'
<!-- =========================
DFSE — README
Modern GitHub-friendly layout
No AI-assistant voice; first-person project-owner tone
========================= -->

<div align="center">

<!-- Animated header (GitHub-friendly SVG). If it ever fails to render, the rest of the README still looks great. -->
<img src="https://readme-typing-svg.demolab.com?font=Inter&weight=700&size=28&duration=2400&pause=700&color=111827&center=true&vCenter=true&width=980&lines=DFSE+—+Decision-Driven+Forecasting+%26+Segmentation+Engine;Traditional+data+science%2C+delivered+like+real+client+work;Forecasting+%7C+Segmentation+%7C+Reproducible+runs+%7C+Stakeholder-ready+outputs" alt="DFSE animated title" />

<br/><br/>

<!-- Badges (visual proof points) -->
<img alt="Python" src="https://img.shields.io/badge/Python-3.x-111827?style=for-the-badge&logo=python&logoColor=white"/>
<img alt="Traditional DS" src="https://img.shields.io/badge/Traditional%20DS-Forecasting%20%26%20Segmentation-111827?style=for-the-badge"/>
<img alt="Makefile" src="https://img.shields.io/badge/One-Command%20Run-Makefile%20%2B%20run.sh-111827?style=for-the-badge"/>
<a href="https://github.com/neilsable/dfse/actions"><img alt="CI" src="https://img.shields.io/github/actions/workflow/status/neilsable/dfse/ci.yml?branch=main&style=for-the-badge&label=CI&color=111827"/></a>

<br/><br/>

<b>A self-directed, end-to-end data science project built to mirror how I deliver under ambiguity:</b><br/>
<i>frame the problem → build robust classical models → publish decision-grade outputs.</i>

</div>

---

## Why I built this

In real analytics work (especially consulting-style delivery), the hard part isn’t “training a model” — it’s translating unclear requirements and imperfect data into outputs stakeholders can act on.

I built DFSE to demonstrate how I:
- independently scope an under-specified analytical problem,
- choose **interpretable classical methods** over black-box novelty,
- keep code clean and reproducible (Makefile + CI),
- deliver stakeholder-ready artefacts (executive summary, metrics, plots).

---

## Quick demo (what you get)

<div align="center">
  <img src="assets/forecast_plot.png" alt="Forecast vs Actual (holdout window)" width="900" />
</div>

### Generated artefacts
**Reports**
- `reports/executive_summary.md` — concise narrative + recommendations
- `reports/forecast_plot.png` — readable forecast visual

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
- Segments designed to map directly to actions (retention / win-back / low-touch engagement)

---

## System flow (visual)

```mermaid
flowchart LR
  A[Data Generation / Ingestion] --> B[Feature Engineering]
  B --> C1[SARIMAX Forecasting]
  B --> C2[RFM + K-Means Segmentation]
  C1 --> D[Metrics + Plot]
  C2 --> E[Segment Summaries]
  D --> F[Stakeholder Outputs]
  E --> F
  F --> G[Executive Summary]
How to run
Option A — Makefile (recommended for reviewers)
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
Open the outputs (cross-platform)
macOS
open reports/forecast_plot.png
open reports/executive_summary.md
open data/processed/forecast_metrics.csv
open data/processed/segment_summary.csv
Linux
Most Linux desktops support xdg-open:

xdg-open reports/forecast_plot.png
xdg-open reports/executive_summary.md
xdg-open data/processed/forecast_metrics.csv
xdg-open data/processed/segment_summary.csv
Windows (PowerShell)
Start-Process opens files with default apps:

Start-Process reports\forecast_plot.png
Start-Process reports\executive_summary.md
Start-Process data\processed\forecast_metrics.csv
Start-Process data\processed\segment_summary.csv
Engineering & delivery hygiene
Dependencies pinned in requirements.txt for reproducibility

Makefile included for standardised execution

CI runs the pipeline on push/PR to prevent regressions

Synthetic data is used deliberately for full reproducibility (no private data), while preserving enterprise-like patterns (seasonality, promotions, long-tail customers)

<details> <summary><b>Assumptions & trade-offs</b></summary>
I prioritised interpretability over maximal accuracy to reflect stakeholder needs.

Promotional effects are modelled explicitly to avoid conflating lift with seasonality.

The project is intentionally focused on traditional data science rather than GenAI.

</details> <details> <summary><b>Repository structure</b></summary>
dfse/
├── src/                 # pipeline + modelling + evaluation
├── data/processed/      # generated outputs
├── reports/             # executive summary + plots
├── assets/              # GitHub visuals (README)
├── sql/                 # Snowflake-style query examples
├── .github/workflows/   # CI pipeline
├── Makefile             # make run
└── run.sh               # ./run.sh
</details>
<div align="center"> <b>Built to reflect real analytics delivery — from framing to decision-ready outputs.</b> </div> EOF ```
