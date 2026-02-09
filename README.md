# 📊 DFSE — Decision-Driven Forecasting & Segmentation Engine

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

**Transform data into decisions through intelligent forecasting and customer segmentation**

[Quick Start](#-quick-start) • [Features](#-features) • [Outputs](#-what-youll-get) • [Documentation](#-documentation)

</div>

---

## 🎯 What is DFSE?

DFSE is a **production-ready analytics engine** that combines time-series forecasting with customer segmentation to drive business decisions. Built with real-world applications in mind, it demonstrates end-to-end data science from raw data to actionable insights.

### Why DFSE?

- 🚀 **Decision-First**: Built to answer real business questions, not just create models
- 🔧 **Production-Ready**: Clean code, automated workflows, reproducible results
- 📈 **Business-Focused**: Demand forecasting + RFM segmentation = immediate value
- 🎓 **Educational**: Clear structure, well-documented, perfect for learning

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 📉 Demand Forecasting
- Classical time-series modeling
- 60-day forward predictions
- Confidence intervals included
- Performance metrics automated

</td>
<td width="50%">

### 👥 Customer Segmentation
- RFM (Recency, Frequency, Monetary) analysis
- Automated segment profiling
- Actionable customer groups
- Clear business insights

</td>
</tr>
</table>

---

## 🚀 How to Run This Project

### ⚡ Super Simple (Just 2 Steps!)

**Step 1:** Download the project
```bash
git clone https://github.com/neilsable/dfse.git
cd dfse
```

**Step 2:** Run it!
```bash
make run
```

**Done!** ✅ Your reports and data will appear in the `reports/` and `data/processed/` folders.

---

### 📋 What Happens When You Run It?

```
1. 🔧 Sets up Python environment automatically
2. 📦 Installs all needed libraries
3. 🎲 Creates sample data (no downloads needed!)
4. 🤖 Builds forecasts and customer segments
5. 📊 Generates reports and charts
6. ✅ Saves everything to your folders
```

**Time needed:** ~2-3 minutes

---

### 🪟 Don't Have `make`? (Windows users)

No problem! Use this instead:

```bash
# Step 1: Download project (same as above)
git clone https://github.com/neilsable/dfse.git
cd dfse

# Step 2: Run this simple script
./run.sh
```

Or run it manually:

```bash
python3 -m venv .venv
source .venv/bin/activate          # macOS/Linux
.\.venv\Scripts\Activate.ps1       # Windows PowerShell
pip install -r requirements.txt
python3 -m src.pipeline
```

---

### ⚠️ Prerequisites

You only need:
- ✅ **Python 3.8 or newer** ([Download here](https://www.python.org/downloads/))
- ✅ **Git** ([Download here](https://git-scm.com/downloads))
- ✅ **5 minutes of your time**

That's it! No databases, no API keys, no complicated setup.

---

## 📦 Where to Find Your Results

After running the project, here's where everything is saved:

### 📊 **Reports** (Human-readable insights)

```
reports/
├── 📄 executive_summary.md      ← Read this first! Plain English summary
└── 📈 forecast_plot.png         ← Visual chart showing predictions
```

**What to do with these:**
- Open `executive_summary.md` in any text editor
- View `forecast_plot.png` to see your forecast chart

---

### 📁 **Data Files** (For further analysis)

```
data/processed/
├── 📊 forecast_metrics.csv      ← How accurate is the model?
├── 📈 forecast_60d.csv          ← Next 60 days of predictions
├── 👥 rfm_segments.csv          ← Each customer's segment
└── 📋 segment_summary.csv       ← Summary of customer groups
```

**What to do with these:**
- Open any `.csv` file in Excel, Google Sheets, or Python
- Use them for presentations, dashboards, or further analysis

---

### 💡 Example: What You'll See

**In `executive_summary.md`:**
```
📊 Forecast Accuracy: 94.2%
👥 Customer Segments Found: 4 groups
💰 High-Value Customers: 127 people
📈 Recommended Action: Focus on "Champions" segment
```

**In `forecast_plot.png`:**
<div align="center">
<img src="assets/forecast_plot.png" width="700" alt="Example Output">
</div>

---

## ❓ Troubleshooting

**Problem:** `make: command not found`  
**Solution:** Use `./run.sh` instead, or follow the manual steps above

**Problem:** `python3: command not found`  
**Solution:** Try `python` instead of `python3`, or install Python from [python.org](https://www.python.org/downloads/)

**Problem:** Permission denied when running `./run.sh`  
**Solution:** Run `chmod +x run.sh` first, then try again

**Problem:** Libraries won't install  
**Solution:** Make sure you activated the virtual environment (the `source .venv/bin/activate` step)

**Still stuck?** Open an [issue on GitHub](https://github.com/neilsable/dfse/issues) and I'll help!

---

## 🏗️ Project Structure

```
dfse/
│
├── src/                     # Source code
│   ├── pipeline.py          # Main forecasting pipeline
│   ├── evaluation.py        # Model evaluation
│   └── utils/               # Helper functions
│
├── data/
│   ├── raw/                 # Generated sample data
│   └── processed/           # Analysis outputs
│
├── reports/                 # Generated reports
├── assets/                  # Images and resources
│
├── requirements.txt         # Python dependencies
├── Makefile                 # Automation commands
└── run.sh                   # Simple run script
```

---

## 🎓 Use Cases

DFSE is perfect for:

- 📚 **Portfolio Projects**: Showcase end-to-end data science skills
- 🏢 **Business Analytics**: Demand planning and customer insights
- 🎯 **Learning**: Understand forecasting and segmentation in practice
- 🔧 **Template**: Starting point for real-world analytics projects

---

## 🛠️ Tech Stack

<div align="center">

| Category | Technologies |
|----------|-------------|
| **Language** | Python 3.8+ |
| **Data Processing** | pandas, NumPy |
| **Modeling** | statsmodels, scikit-learn |
| **Visualization** | matplotlib, seaborn |
| **Automation** | Make, bash scripting |

</div>

---

## 💭 How I Built This (My Approach)

### 🎯 The Problem I Wanted to Solve

Most data science projects are either:
- Too theoretical (just Jupyter notebooks with no real workflow)
- Too complex (enterprise-level code that's hard to understand)

**I wanted something in between** — a project that shows real production skills but stays simple enough for anyone to learn from.

---

### 🏗️ My Design Decisions

#### **1. Why Classical Time-Series Instead of ML?**

```python
# I chose ARIMA/Exponential Smoothing over LSTM/Prophet because:
✅ More interpretable (you can explain WHY it predicts what it does)
✅ Works well with limited data
✅ Faster to train and run
✅ Industry standard for demand forecasting
```

For business decisions, **explainability > accuracy by 2%**. Stakeholders need to trust your model.

#### **2. Why RFM Segmentation?**

```python
# RFM = Recency, Frequency, Monetary Value
✅ Simple enough to explain to non-technical people
✅ Actionable (you can target segments immediately)
✅ Proven technique used by real companies
✅ No complex clustering algorithms to debug
```

I wanted to show I understand **business value**, not just fancy algorithms.

#### **3. Code Structure Philosophy**

```
src/
├── pipeline.py       # Main logic (what happens)
├── evaluation.py     # Quality checks (is it good?)
└── utils/            # Helpers (how we do it)
```

**Why this structure?**
- ✅ Separates **WHAT** from **HOW** 
- ✅ Easy to test individual pieces
- ✅ Can swap out methods without breaking everything
- ✅ Follows production best practices

#### **4. Automation Over Documentation**

Instead of writing "Step 1: Do this, Step 2: Do that..." I built:

```bash
make run  # Just works™
```

**Why?**
- Users don't read long instructions
- Automation forces you to think about reproducibility
- Shows DevOps thinking, not just data science

---

### 🧠 What I Learned Building This

| Challenge | What I Did | Why It Matters |
|-----------|-----------|----------------|
| **Data Generation** | Built synthetic data generator instead of using real data | Shows I can create realistic test scenarios |
| **Error Handling** | Added validation at each pipeline step | Production code needs to fail gracefully |
| **Output Design** | Created both technical (CSV) and business (MD) outputs | Data scientists serve multiple audiences |
| **Environment Setup** | Made it work on Mac, Linux, AND Windows | Real tools need to work everywhere |

---

### 🔧 Technical Highlights

Here's what makes this code different:

#### **Clean Data Pipeline**
```python
# Instead of messy notebooks, I built a clear pipeline:
raw_data → validation → transformation → modeling → evaluation → reporting
```

#### **Modular Functions**
```python
# Each function does ONE thing well
def calculate_rfm_score(df):
    """Takes customer data, returns RFM segments"""
    # Not: calculate_rfm_and_make_plots_and_send_email()
```

#### **Type Hints & Documentation**
```python
def forecast_demand(data: pd.DataFrame, periods: int = 60) -> Dict[str, Any]:
    """
    Generate demand forecast with confidence intervals.
    
    Args:
        data: Historical demand data with datetime index
        periods: Number of future periods to forecast
        
    Returns:
        Dictionary containing forecast, metrics, and plots
    """
```

This isn't just "code that works" — it's **code others can maintain**.

---

### 🎓 Why I Made These Choices

As someone looking to break into data science/analytics roles, I wanted to show:

1. **I understand business needs** (decision-first approach)
2. **I write production code** (not just experiments)
3. **I communicate clearly** (reports for stakeholders, code for developers)
4. **I think about the full lifecycle** (from data to decisions)

This project represents **how I actually work**, not just what I know.

---

## 📈 Sample Output

<div align="center">
<img src="assets/forecast_plot.png" width="800" alt="Forecast Visualization">
<p><em>Actual vs Predicted demand with confidence intervals</em></p>
</div>

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Neil Sable**

- GitHub: [@neilsable](https://github.com/neilsable)
- LinkedIn: [Neil Sable](https://www.linkedin.com/in/neil-sable-441aa42b2/)
- Email: neilsable7@gmail.com

---

## ⭐ Show Your Support

Give a ⭐️ if this project helped you!

---

<div align="center">

**Built with ❤️ for practical data science**

[Back to Top](#-dfse--decision-driven-forecasting--segmentation-engine)

</div>
