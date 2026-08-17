# AlignSec FINAL repository-metadata cleanup

This cleanup changes repository metadata, reproducibility wording, and manuscript Monte Carlo notation only. It does **not** change the frozen benchmark, frozen 3,200-row model-response dataset, ASRs, CLIRS values, hypothesis-test results, cluster-bootstrap intervals, category results, or any LLM inference output.

## Changes made

1. **CLIRS metadata corrected**
   - `table_20_metric_and_CLIRS_definitions.csv` now states that the primary CLIRS 95% CI uses a paired **base-template bootstrap over 80 attack templates** with 10,000 iterations.
   - Category-cluster CLIRS bootstrap is explicitly marked as supporting sensitivity analysis only.

2. **Manuscript reminders synchronized to FINAL statistics**
   - `table_25_manuscript_writeup_reminders.csv` now distinguishes:
     - 12 language-vs-English exact paired McNemar tests + BH-FDR;
     - 3 overall model comparisons using base-template cluster bootstrap CIs + 100,000-draw paired sign-flip randomization + BH-FDR;
     - 15 language-specific model exact paired McNemar tests + BH-FDR.
   - Category uncertainty wording now matches the base-template cluster bootstrap with Wilson fallback for singleton categories.

3. **Supplementary artifact filename corrected**
   - `table_42_supplementary_artifact_role_and_claim_boundaries.csv` now references `figure_15_paired_category_bootstrap_language_gaps.pdf`.

4. **Supplementary manifest updated from v9 to FINAL**
   - Final executed notebook path is now `analysis/FINAL_AlignSec_EAAI_Journal_Ready_Analysis_EXECUTED.ipynb`.
   - Frozen analysis data are described as the primary FINAL input.

5. **Execution manifest expanded**
   - `table_15_execution_manifest.csv` now records the correct primary overall-model cluster inference, primary CLIRS base-template bootstrap, paired McNemar families, and supporting category-cluster sensitivity analysis.

6. **Reproducibility table synchronized**
   - `table_23_reproducibility_and_execution_details.csv` now separates primary proportion uncertainty, overall model inference, primary CLIRS uncertainty, three FDR families, and supporting category-composition sensitivity analysis.

7. **Portable figure paths**
   - `table_16_figure_index_and_captions.csv` now stores repository-relative paths rather than `/mnt/data/...` paths.

8. **FINAL environment naming**
   - Conda environment renamed to `alignsec-final-analysis`.
   - `requirements.txt` now points to the FINAL analysis notebook and contains no v9 naming.

9. **Portable README expanded**
   - Added exact Conda and pip reproduction commands.
   - Added expected output counts and integrity checks.
   - Added the FINAL statistical source-of-truth summary and Qwen provenance/claim boundaries.

10. **Environment provenance wording cleaned**
    - FINAL analysis rows are labeled `FINAL executed analysis` / `FINAL analysis code`.
    - Historical GPU/PyTorch evidence is labeled as historical v5 execution evidence rather than implying the released inference notebook itself is executed.
    - Qwen input-cap metadata is synchronized with the matched historical v5 runner provenance.

11. **Monte Carlo precision wording corrected in manuscript**
    - The three overall sign-flip comparisons are reported as approximately `1.0 × 10^-5`, with the plus-one-corrected minimum `1/100001`, rather than `p < 10^-5`.

12. **Release checksums and manifests regenerated**
    - `metadata/release_manifest.csv` and `metadata/SHA256SUMS.txt` were rebuilt after the cleanup.
    - The output ZIP and complete technical package were rebuilt and ZIP integrity-tested.

## Verification

- Executed FINAL notebook: **24/24 code cells executed**.
- Notebook execution errors: **0**.
- Generated outputs: **44 CSV tables + 15 PDF figures**.
- Frozen final-results SHA-256 remains `405a5017589b4722fbcad13a5c43a555d3e5afc6498fe46cf5a16a63baaf91f4`.
- Frozen benchmark SHA-256 remains `d0bba7ade1d3801cdab983c277303c35c4200985abd48cf4001b71fa555b3d46`.
- Output ZIP integrity: passed.
- Complete technical package ZIP integrity: passed.
- Key scientific result tables were byte-for-byte unchanged from the prior FINAL technical freeze.

**Status: repository-metadata cleanup complete. This is the submission-ready technical package.**
