# Data

This directory contains the frozen benchmark and response data used by the final AlignSec analysis.

- `benchmark/frozen_alignsec_v4_benchmark.csv` — frozen 800-item benchmark.
- `final_results.csv` — frozen 3,200-row analysis dataset used by the final notebook.
- `canonical_responses/` — deduplicated per-model response files recovered from the frozen final dataset.
- `raw_responses/` — preserved historical raw-output artifacts where available, including the explicitly reconstructed Qwen historical-format artifact.
- `DATA_DICTIONARY.md` — definitions for benchmark and final-response fields.

## Frozen-path metadata

The `source_csv_path` column in `final_results.csv` and canonical response files contains historical local `/mnt/data/...` build paths. These strings are preserved to keep the frozen final dataset byte-identical to the analysis input. They are provenance metadata only and are **not** paths required for reproduction.

## Qwen provenance note

The original byte-identical standalone Qwen source cell and separate original raw CSV were not preserved. The file `raw_responses/qwen_raw_outputs_RECONSTRUCTED_FROM_FROZEN_FINAL_DATA.csv` reconstructs the historical 19-column raw schema losslessly from the frozen final data and is explicitly labelled as reconstructed. See `../inference/provenance/` for the preserved execution evidence and provenance resolution.

## Primary frozen-input hashes

- `data/final_results.csv`: `405a5017589b4722fbcad13a5c43a555d3e5afc6498fe46cf5a16a63baaf91f4`
- `data/benchmark/frozen_alignsec_v4_benchmark.csv`: `d0bba7ade1d3801cdab983c277303c35c4200985abd48cf4001b71fa555b3d46`
