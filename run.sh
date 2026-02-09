#!/usr/bin/env bash
set -euo pipefail

if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

source .venv/bin/activate
python -m pip install --upgrade pip >/dev/null
pip install -r requirements.txt >/dev/null

python -m src.pipeline
python -m src.evaluation

echo "✅ Done. Review:"
echo " - reports/executive_summary.md"
echo " - reports/forecast_plot.png"
echo " - data/processed/forecast_metrics.csv"
echo " - data/processed/segment_summary.csv"
