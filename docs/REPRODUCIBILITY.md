# Reproducibility guide

## Scope

The final statistical analysis can be reproduced from the frozen benchmark and response data in this repository without rerunning LLM inference. Full statistical reproduction may take several minutes depending on hardware because the notebook includes 10,000-iteration bootstrap procedures and 100,000-draw Monte Carlo randomization.

## Frozen primary inputs

- `data/final_results.csv`
- `data/benchmark/frozen_alignsec_v4_benchmark.csv`

Their fixed SHA-256 hashes are checked by `scripts/verify_repository.py`.

## Quick verification

```bash
python scripts/verify_repository.py
```

The verifier checks the frozen input hashes, dataset dimensions and pairing structure, unique prompt/canary counts, exact-canary recomputation, benchmark identity across models, required inference/provenance artifacts, statistical artifact counts, the current repository manifest/checksums, and the absence of notebook error outputs in the preserved executed analysis notebook.

## Analysis reproduction

Use `scripts/reproduce_analysis.sh` or `scripts/reproduce_analysis.bat`, or follow the commands in the root README. The analysis notebook consumes the frozen response data; it does not contact model APIs or download model weights.

## Historical inference boundary

The repository preserves available inference code/evidence but does not claim bit-for-bit reconstruction of every historical environment detail. Exact historical Transformers, Accelerate, and bitsandbytes versions and Hugging Face repository commit SHAs were not logged. Qwen provenance is documented separately under `inference/provenance/`.
