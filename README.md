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

This project is designed so that most users only need **one command**.

```bash
make run
./run.sh
python3 -m venv .venv
source .venv/bin/activate        # macOS / Linux
# .\.venv\Scripts\Activate.ps1   # Windows (PowerShell)
python3 -m pip install -r requirements.txt
python3 -m src.pipeline
python3 -m src.evaluation

## What this does Running the workflow above:

1. sets up the environment
2. installs all required dependencies
3. runs the full forecasting and segmentation pipeline
4. generates all reports and data outputs

You do not need to run every command above.
For most users, make run is sufficient.
