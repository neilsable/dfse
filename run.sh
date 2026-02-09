#!/usr/bin/env bash
set -euo pipefail

# Create venv if missing
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

# Activate venv
source .venv/bin/activate

# Install dependencies
python3 -m pip install --upgrade pip >/dev/null
python3 -m pip install -r requirements.txt >/dev/null

# Run the application
python3 -m src.pipeline
python3 -m src.evaluation

echo ""
echo "✅ DFSE execution complete."
echo ""
echo "Outputs generated:"
echo " - reports/executive_summary.md"
echo " - reports/forecast_plot.png"
echo " - data/processed/forecast_metrics.csv"
echo " - data/processed/segment_summary.csv"
