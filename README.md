# DFSE — Decision-Driven Forecasting & Segmentation Engine

<p align="center">
  <img src="assets/forecast_plot.png" width="880" alt="Forecast vs Actual">
</p>

<p align="center">
  <strong>A practical, decision-first data science project.</strong>
</p>

---

## What is this?

DFSE is a small, self-contained Python project that demonstrates how I approach
a real-world analytics problem from start to finish.

It focuses on:
- realistic data and assumptions  
- robust, explainable modelling  
- outputs that support real decisions  

You do not need prior knowledge of the codebase to use this project.

---

## What happens when I run it?

When you run DFSE, it:

1. Generates a realistic sample dataset (no external or private data)
2. Builds a demand forecast using classical time-series modelling
3. Segments customers using standard RFM techniques
4. Writes reports and data outputs to disk

---

## What outputs will I see?

After a successful run, you will find:

**Reports**
- `reports/executive_summary.md` — plain-English summary
- `reports/forecast_plot.png` — actual vs forecast visual

**Data**
- `data/processed/forecast_metrics.csv`
- `data/processed/forecast_60d.csv`
- `data/processed/rfm_segments.csv`
- `data/processed/segment_summary.csv`

---

## How to run

If you are new to Python projects, start here.

```bash
make run

# If make is not available:
./run.sh

# Manual execution (optional):
python3 -m venv .venv
source .venv/bin/activate        # macOS / Linux
# .\.venv\Scripts\Activate.ps1   # Windows (PowerShell)
python3 -m pip install -r requirements.txt
python3 -m src.pipeline
python3 -m src.evaluation
That single workflow:

sets up the environment

installs dependencies

runs the full pipeline

generates all outputs

Viewing the results
macOS:
open reports/forecast_plot.png
open reports/executive_summary.md

Linux:
xdg-open reports/forecast_plot.png
xdg-open reports/executive_summary.md

Windows (PowerShell):
Start-Process reports\forecast_plot.png
Start-Process reports\executive_summary.md

How the modelling works (high level)
Forecasting
SARIMAX with weekly seasonality and promotional effects, chosen for stability
and interpretability rather than black-box accuracy.

Segmentation
Standard RFM features combined with K-Means clustering to create actionable
customer groups.

Why this project exists
This project reflects how I would deliver a real analytics task:

start from ambiguity

choose robust, explainable methods

keep execution reproducible

focus on outputs stakeholders can act on
