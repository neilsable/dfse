# DFSE — Decision-Driven Forecasting & Segmentation Engine

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Inter&weight=600&size=28&pause=800&color=111827&center=true&vCenter=true&width=900&lines=Decision-Driven+Forecasting+%26+Segmentation+Engine;Traditional+data+science+with+a+modern+delivery+mindset;Built+to+be+run%2C+read%2C+and+understood" />
</p>

<p align="center">
  <b>Forecasting and segmentation, delivered like a real analytics engagement.</b>
</p>

<p align="center">
  <img src="assets/forecast_plot.png" alt="Forecast vs Actual" width="880">
</p>

---

## What is this project?

DFSE is a self-contained data science project that demonstrates how I approach
real-world analytics problems end-to-end.

The focus is not on dashboards or black-box models, but on:
- working with unclear requirements,
- using robust and explainable methods,
- and producing outputs that support real decisions.

You do **not** need prior knowledge of the codebase to run this project.

---

## What happens when I run it?

When you execute DFSE, it:

1. Generates a realistic sample dataset (no external or private data)
2. Builds a demand forecast using classical time-series modelling
3. Segments customers using standard RFM techniques
4. Produces clear outputs you can immediately open and understand

---

## What outputs will I see?

After a successful run, the following files are created.

### Reports (human-readable)
- `reports/executive_summary.md`  
  A short, plain-English explanation of the approach, results, and recommendations.

- `reports/forecast_plot.png`  
  A visual comparison of actual demand vs forecasted demand.

### Data outputs
- `data/processed/forecast_metrics.csv`  
  Forecast accuracy metrics (MAE, RMSE, MAPE)

- `data/processed/forecast_60d.csv`  
  Actual vs forecast values for the evaluation period

- `data/processed/rfm_segments.csv`  
  Each customer with an assigned segment

- `data/processed/segment_summary.csv`  
  A summary of each customer segment

---

## How to run (start here)

If you are new to Python projects, **this is the only command you need**:

```bash
make run
That single command:

sets up the environment,

installs all required dependencies,

runs the full pipeline,

and generates all outputs.

Other ways to run (optional)

If make is not available on your machine:

./run.sh


If you want to run everything step-by-step:

python3 -m venv .venv

# macOS / Linux
source .venv/bin/activate

# Windows (PowerShell)
# .\.venv\Scripts\Activate.ps1

python3 -m pip install -r requirements.txt
python3 -m src.pipeline
python3 -m src.evaluation

Viewing the results

After running the project, you can open the outputs directly.

macOS
open reports/forecast_plot.png
open reports/executive_summary.md

Linux
xdg-open reports/forecast_plot.png
open reports/executive_summary.md

Windows (PowerShell)
Start-Process reports\forecast_plot.png
Start-Process reports\executive_summary.md

How the modelling works (high level)

You do not need to understand this to use the project, but for context:

Forecasting

Uses a SARIMAX model with weekly seasonality

Promotional effects are included as an external driver

Chosen for stability and interpretability rather than black-box accuracy

Segmentation

Uses standard RFM features (recency, frequency, monetary value)

K-Means clustering on scaled inputs

Segments are designed to map directly to business actions

Why this project exists

This is not a tutorial or a demo dashboard.

It reflects how I would deliver a real analytics task:

start from an ambiguous problem,

apply robust and explainable methods,

keep execution simple and reproducible,

and focus on outputs that stakeholders can act on.

If you are trying this for the first time and something does not work,
running make run again is usually sufficient.
