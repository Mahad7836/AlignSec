# AlignSec Final Technical Freeze

## Decision
The technical analysis is frozen for the current manuscript. No additional LLM inference is required for the claims supported by this repository.

## Resolved publication-critical items
1. **Qwen fairness/provenance:** historical execution is tied to the preserved v5 runner by run-stage tag, 19-column schema, checkpoint cadence, and file naming. A transparent historical invocation reconstruction is supplied; the byte-identical standalone Qwen source cell was not preserved.
2. **Overall model clustering:** primary inference clusters the 400 language-expanded attack observations into 80 underlying base attack templates.
3. **CLIRS uncertainty:** primary 95% intervals resample paired base templates; the earlier category-level bootstrap is retained only as sensitivity analysis.
4. **Category uncertainty:** base-template cluster bootstrap is primary when estimable; singleton categories use a Wilson descriptive fallback.
5. **Category-by-language analysis:** denominator-aware ASR is used rather than raw successful-leak counts.
6. **Qwen raw data:** the 800-row, 19-column raw-format artifact is reconstructed losslessly from frozen final fields and explicitly labelled reconstructed.
7. **Environment/revisions:** recoverable values are recorded; missing exact historical package versions and model-repository commit SHAs are explicitly not invented.
8. **Input length:** character/UTF-8 length audit is included; exact historical tokenizer-level lengths are not claimed.
9. **Latency/secondary labels:** supplementary only; they are not used for primary security claims.
10. **Final artifact synchronization:** statistical wording and output counts are synchronized with the frozen analysis.

## Final generated artifacts
- 44 CSV tables
- 15 PDF figures
- 3,200-row final analysis dataset
- 800-item frozen benchmark

## Historical naming note
Some frozen notebook run tags, output filenames, and metadata retain the historical `EAAI` development label. They are intentionally preserved because they identify the exact frozen analysis artifact. The current public repository is journal-neutral and the scientific results do not depend on the journal target.

## Current repository metadata

Current live repository paths are tracked in `metadata/repository_manifest.csv`, `metadata/current_repository_figure_index.csv`, and `metadata/current_repository_supplementary_manifest.csv`. The preserved historical technical-package manifest is retained separately as `metadata/historical_technical_package_manifest.csv`.
