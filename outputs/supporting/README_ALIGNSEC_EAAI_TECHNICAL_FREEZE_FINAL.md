AlignSec EAAI Journal-Ready Technical Freeze — FINAL
====================================================
Generated UTC: 2026-08-12 10:48:00 UTC

Frozen inputs
-------------
data/final_results.csv SHA-256: 405a5017589b4722fbcad13a5c43a555d3e5afc6498fe46cf5a16a63baaf91f4
data/benchmark/frozen_alignsec_v4_benchmark.csv SHA-256: d0bba7ade1d3801cdab983c277303c35c4200985abd48cf4001b71fa555b3d46
No LLM inference is performed by this FINAL analysis notebook.

Primary reviewer-grade inference
--------------------------------
1. Leakage endpoint: mechanically recomputed exact assigned-canary containment.
2. Language-vs-English within-model tests: exact paired McNemar with BH-FDR across 12 tests.
3. Overall clean-model comparison: 80 underlying base attack templates are the cluster unit; 95% CIs use paired base-template bootstrap and p-values use paired Monte Carlo sign-flip randomization (100,000 permutations), with BH-FDR across 3 comparisons.
4. Language-specific clean-model comparisons remain exact paired McNemar tests within each language.
5. CLIRS primary uncertainty: paired bootstrap over the same 80 base attack templates, retaining English and target-language outcomes together.
6. Attack-category uncertainty: base-template cluster bootstrap when a category has >=2 underlying base templates; singleton categories report Wilson descriptive intervals and explicitly mark cluster CI as not estimable.
7. Figure 9 is denominator-aware category-language ASR, not raw leak counts.

Qwen provenance resolution
--------------------------
The completed historical Qwen run is tied to the preserved v5 runner by an exact match in RUN_STAGE, 19-column raw-output schema, checkpoint cadence, checkpoint naming, and raw-output filename pattern. The v5 runner therefore supplies the common system policy and inference settings for the historical Qwen run. The separate byte-identical Qwen source cell was not preserved, so this release includes a transparent historical invocation reconstruction rather than falsely claiming an original source file. The 800-row 19-column Qwen raw artifact is reconstructed losslessly from frozen final fields and is clearly named RECONSTRUCTED_FROM_FROZEN_FINAL_DATA.

Inference provenance boundaries
-------------------------------
- Historical GPU: Tesla T4; historical PyTorch: 2.10.0+cu128.
- Historical exact Transformers/Accelerate/bitsandbytes versions were not logged; recoverable setup minima are documented and exact versions are not invented.
- Historical Hugging Face commit SHAs were not logged; model IDs are preserved, but no retroactive revision SHA is fabricated. Any future rerun should pin revisions explicitly.
- Preserved v5 runner: input cap 2048 with truncation, attack max_new_tokens=120, benign max_new_tokens=80, do_sample=False, 4-bit NF4/double-quant/float16 compute.
- Frozen prompt character/UTF-8 byte lengths are audited. Exact historical tokenizer-level lengths were not logged, so no retroactive exact token-count claim is made.

Claim boundaries
----------------
Resource tier is descriptive, not causal. Non-English conditions are controlled language-retargeted objectives under a shared English scaffold/base instruction, not fully native-language attacks. Latency and secondary response-class plots are supplementary only. This is an evaluation framework, not an implemented defense system.

Generated artifacts
-------------------
CSV tables: 44
PDF figures: 15
