# DFSE  
### Decision-Driven Forecasting & Segmentation Engine

<p align="center">
  <img src="assets/forecast_plot.png" alt="Forecast vs Actual" width="880">
</p>

<p align="center">
  <b>Traditional data science, delivered with a modern, decision-first mindset.</b>
</p>

---

## 👋 What is this?

DFSE is a self-contained data science project that demonstrates how I approach
real-world analytics problems end-to-end:

- ambiguous requirements  
- realistic data patterns  
- explainable modelling choices  
- clear, decision-ready outputs  

It is designed to be **easy to run**, **easy to understand**, and **useful on first contact**.

---

## 🚀 Start here (30 seconds)

If you do nothing else, run this:

```bash
make run
That single command:

sets up the environment

installs dependencies

runs the full pipeline

generates all outputs

No prior setup required.

📦 What you get after running it
Outputs you can read
Executive summary
reports/executive_summary.md
A plain-English explanation of the approach, results, and recommendations.

Forecast visual
reports/forecast_plot.png
Actual vs forecasted demand, designed for clarity rather than dashboards.

Outputs you can analyse
data/processed/forecast_metrics.csv — forecast accuracy (MAE / RMSE / MAPE)

data/processed/forecast_60d.csv — actual vs forecast values

data/processed/rfm_segments.csv — customer-level segmentation

data/processed/segment_summary.csv — segment-level characteristics

🧠 What’s happening under the hood (high level)
You don’t need to know this to run the project, but for context:

Forecasting
Classical SARIMAX time-series model

Weekly seasonality modelled explicitly

Promotional effects treated as exogenous signals

Chosen for stability and interpretability, not black-box accuracy

Segmentation
Standard RFM features (recency, frequency, monetary value)

K-Means clustering on scaled inputs

Segments designed to map directly to commercial actions

🛠 How else can I run it?
If make isn’t available, you have two alternatives.

One-command script
./run.sh
Manual (step-by-step)
python3 -m venv .venv

# macOS / Linux
source .venv/bin/activate

# Windows (PowerShell)
# .\.venv\Scripts\Activate.ps1

python3 -m pip install -r requirements.txt
python3 -m src.pipeline
python3 -m src.evaluation
👀 Viewing the results
macOS
open reports/forecast_plot.png
open reports/executive_summary.md
Linux
xdg-open reports/forecast_plot.png
xdg-open reports/executive_summary.md
Windows
Start-Process reports\forecast_plot.png
Start-Process reports\executive_summary.md
🧩 Why this project exists
This is not a tutorial, dashboard, or GenAI demo.

It reflects how I would deliver a real analytics engagement:

focus on decisions, not novelty

choose robust, explainable methods

keep execution reproducible

make outputs understandable to non-technical stakeholders

<p align="center"> <i>Built to be run, read, and understood — not just skimmed.</i> </p> ```
