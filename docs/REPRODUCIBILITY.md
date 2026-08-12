# Reproducibility guide

## Scope
The final analysis can be reproduced from the frozen benchmark and response data in this repository without rerunning LLM inference.

## Frozen primary inputs
- `data/final_results.csv`
- `data/benchmark/frozen_alignsec_v4_benchmark.csv`

The clean final analysis notebook verifies both files against fixed SHA-256 hashes before proceeding.

## Quick verification

```bash
python scripts/verify_repository.py
```

Expected checks include 3,200 final rows, 800 benchmark rows, 0 duplicate model/prompt keys, 15 PDF figures, and 44 CSV tables.

## Analysis reproduction
Use either `scripts/reproduce_analysis.sh` or `scripts/reproduce_analysis.bat`, or follow the commands in the root README.

## Historical inference boundary
The repository preserves available inference code/evidence but does not claim bit-for-bit reconstruction of every historical environment detail. Exact historical Transformers, Accelerate, bitsandbytes versions and Hugging Face repository commit SHAs were not logged. Qwen provenance is documented separately under `inference/provenance/`.
