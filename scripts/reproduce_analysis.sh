#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
export ALIGNSEC_PROJECT_ROOT="$ROOT"
python scripts/verify_repository.py
jupyter nbconvert --to notebook --execute analysis/AlignSec_Final_Analysis.ipynb \
  --output AlignSec_Final_Analysis_REPRODUCED.ipynb \
  --ExecutePreprocessor.timeout=600
