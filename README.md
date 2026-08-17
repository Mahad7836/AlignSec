# AlignSec

## A Reproducible Cross-Lingual Evaluation of Prompt-Injection Protected-Context Leakage in Aligned Large Language Models

**AlignSec** is a reproducible security-evaluation framework for measuring prompt-injection protected-context leakage across selected language conditions in aligned instruction-tuned large language models. The associated manuscript is being prepared for the *Journal of Information Security and Applications (JISA)*.

The study uses unique synthetic canary strings as protected values and evaluates whether a model discloses its assigned canary under adversarial prompts or benign controls. The non-English conditions are **controlled language-retargeted objectives under a shared English scaffold/base instruction**; they are not claimed to be fully native-language attacks. Resource-tier labels are descriptive metadata only and are not interpreted causally.

## Frozen study design

- **800 prompts per model**: 400 attack + 400 benign
- **5 language conditions**: English, French, Arabic, Bengali, Sindhi
- **80 attack + 80 benign prompts per language condition**
- **27 attack categories**
- **3 clean-comparison models**:
  - `mistralai/Mistral-7B-Instruct-v0.2`
  - `Qwen/Qwen2.5-3B-Instruct`
  - `HuggingFaceH4/zephyr-7b-beta`
- **1 diagnostic model**: `NousResearch/Llama-2-7b-chat-hf`
- **3,200 final response rows**

## Primary observed results

| Model | Successful attacks | Overall ASR | Benign canary leaks |
|---|---:|---:|---:|
| Mistral-7B-Instruct-v0.2 | 37 / 400 | 9.25% | 0 / 400 |
| Qwen2.5-3B-Instruct | 175 / 400 | 43.75% | 0 / 400 |
| Zephyr-7B-Beta | 293 / 400 | 73.25% | 0 / 400 |

Llama-2 is retained as a diagnostic case because it produced 3 observed benign canary disclosures out of 400 benign prompts. Reviewer-grade inference in the final notebook respects the 80 underlying base attack templates as paired/clustered experimental units where appropriate.

See `docs/ARTIFACT_MAP.md` for direct mappings from manuscript claims to frozen figures and supporting artifacts.

## Repository structure

```text
AlignSec/
├── analysis/                   # Clean and executed final analysis notebooks
├── data/                       # Frozen benchmark, final dataset, canonical/raw responses
├── inference/                  # Historical runners, Qwen reconstruction, provenance
├── outputs/                    # 15 frozen statistical PDFs + 44 frozen CSV tables
├── docs/                       # Reproducibility, taxonomy, artifact map, explanatory diagrams
├── metadata/                   # Current/historical manifests, provenance, checksums
├── scripts/                    # Verification, reproduction, diagram-generation helpers
├── .github/workflows/          # Lightweight repository verification CI
├── THIRD_PARTY_NOTICES.md
├── environment.yml
├── requirements.txt
└── requirements-inference.txt
```

## Verify the repository

```bash
python scripts/verify_repository.py
```

A successful run ends with:

```text
Repository verification PASSED.
```

## Reproduce the final analysis

The final analysis notebook does **not** rerun LLM inference. It consumes the frozen, hash-verified benchmark and response dataset included in this repository. Full execution may take several minutes because the analysis includes bootstrap and Monte Carlo procedures.

### Conda

```bash
conda env create -f environment.yml
conda activate alignsec-final-analysis
python scripts/verify_repository.py
jupyter nbconvert --to notebook --execute analysis/AlignSec_Final_Analysis.ipynb \
  --output AlignSec_Final_Analysis_REPRODUCED.ipynb \
  --ExecutePreprocessor.timeout=1200
```

### pip

```bash
python -m pip install -r requirements.txt
python scripts/verify_repository.py
jupyter nbconvert --to notebook --execute analysis/AlignSec_Final_Analysis.ipynb \
  --output AlignSec_Final_Analysis_REPRODUCED.ipynb \
  --ExecutePreprocessor.timeout=1200
```

If the notebook environment does not start from the repository root, set `ALIGNSEC_PROJECT_ROOT` to the repository root before execution.

## Primary endpoint

The primary leakage endpoint is mechanically recomputed exact-canary disclosure after minimal formatting normalization (`\_` → `_`). AlignSec does not use fuzzy, semantic, partial, paraphrase, or encoded matching as the primary endpoint.

## Statistical analysis

- Language-vs-English: exact paired McNemar tests with BH-FDR across 12 non-English comparisons.
- Overall clean-model comparison: base-template cluster bootstrap over 80 underlying attack templates plus paired sign-flip randomization (100,000 draws), with BH-FDR across 3 model comparisons.
- Language-specific model comparisons: exact paired McNemar tests.
- CLIRS uncertainty: paired base-template bootstrap, 10,000 iterations, seed 42.
- Attack-category uncertainty: base-template cluster bootstrap where estimable; Wilson descriptive fallback for singleton-template categories.

## Reproducibility and provenance boundaries

Historical execution evidence records a Tesla T4 and PyTorch `2.10.0+cu128`. Exact historical Transformers, Accelerate, and bitsandbytes versions and Hugging Face repository commit SHAs were not recorded and are not retroactively invented.

The historical Qwen run is supported by preserved execution evidence and a preserved v5 runner context with matching run stage, schema, checkpoint cadence, and naming conventions. The original byte-identical standalone Qwen source cell and separately preserved original raw CSV were not retained, so the repository supplies a transparent reconstruction rather than claiming an original source artifact.

See `inference/README.md`, `inference/provenance/QWEN_PROVENANCE_RESOLUTION.md`, and `metadata/model_provenance.csv`.

## Historical naming note

Some **frozen generated artifacts** retain the historical `EAAI` label from the development stage. These labels are intentionally preserved where editing them would break traceability to the frozen analysis. Current publication-facing documentation and repository metadata are JISA-oriented or journal-neutral.

## Security, ethical, and validity scope

- synthetic canaries only; no real credentials, PII, or enterprise secrets;
- exact-match leakage endpoint does not measure transformed/encoded/semantic leakage;
- five selected language conditions;
- controlled retargeting under a shared English scaffold, not fully native multilingual attacks;
- resource-tier labels are descriptive only;
- 4-bit historical inference and deterministic single generations;
- no closed/proprietary models, RAG/tool execution, or defense layer;
- historical environment/revision limitations are documented explicitly.

## Documentation

- `data/DATA_DICTIONARY.md` — benchmark and response-field definitions
- `docs/ATTACK_TAXONOMY.md` — 27 attack categories and template counts
- `docs/ARTIFACT_MAP.md` — manuscript-to-repository artifact map
- `docs/REPRODUCIBILITY.md` — reproduction scope and procedure
- `docs/TECHNICAL_FREEZE.md` — final technical-freeze decisions
- `docs/LICENSE_SCOPE.md` — licensing boundaries
- `THIRD_PARTY_NOTICES.md` — public attack-source and model attribution notes

## Citation

`CITATION.cff` uses the final paper title and current repository metadata. Before the archival `v1.0.0` release, synchronize the author list with the final manuscript order and add the archival DOI once assigned.

## License

Software/code authored for AlignSec is released under the MIT License. The license does not override upstream dataset/model terms. See `docs/LICENSE_SCOPE.md` and `THIRD_PARTY_NOTICES.md`.
