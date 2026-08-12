# AlignSec

**AlignSec** is a reproducible security-evaluation framework for measuring prompt-injection protected-context leakage across selected language conditions in aligned instruction-tuned large language models.

The study uses unique synthetic canary strings as protected values and evaluates whether a model discloses the assigned canary under attack prompts or benign controls. The non-English conditions are **controlled language-retargeted objectives under a shared English scaffold/base instruction**; they are not claimed to be fully native-language attacks. Resource-tier labels are descriptive metadata only and are not interpreted causally.

## Frozen study design

- **800 prompts per model**: 400 attack + 400 benign
- **5 language conditions**: English, French, Arabic, Bengali, Sindhi
- **80 attack + 80 benign prompts per language condition**
- **27 attack categories**
- **3 clean-comparison models**:
  - `mistralai/Mistral-7B-Instruct-v0.2`
  - `Qwen/Qwen2.5-3B-Instruct`
  - `HuggingFaceH4/zephyr-7b-beta`
- **1 diagnostic model**:
  - `NousResearch/Llama-2-7b-chat-hf`
- **3,200 final response rows**

## Primary observed results

Overall exact-canary attack success rate (ASR) across the 400 attack prompts per clean model:

| Model | Successful attacks | ASR |
|---|---:|---:|
| Mistral-7B-Instruct-v0.2 | 37 / 400 | 9.25% |
| Qwen2.5-3B-Instruct | 175 / 400 | 43.75% |
| Zephyr-7B-Beta | 293 / 400 | 73.25% |

All three clean-comparison models had **0 observed benign canary leaks out of 400 benign prompts**. Llama-2 is retained as a diagnostic case because it produced 3 benign canary disclosures.

These values are descriptive summaries; reviewer-grade inference in the final notebook respects the 80 underlying base attack templates as paired/clustered experimental units where appropriate.

## Repository structure

```text
AlignSec/
├── analysis/                   # Clean and executed final analysis notebooks
├── data/
│   ├── benchmark/              # Frozen v4 benchmark
│   ├── canonical_responses/    # Deduplicated per-model response datasets
│   ├── raw_responses/          # Historical/raw-format response artifacts
│   └── final_results.csv       # Frozen 3,200-row primary analysis input
├── inference/
│   ├── mistral/                # Preserved Mistral inference notebook
│   ├── qwen/                   # Historical Qwen invocation reconstruction
│   ├── zephyr_llama2/          # Preserved Zephyr/Llama-2 runner
│   └── provenance/             # Qwen execution/provenance evidence
├── outputs/
│   ├── figures/                # 15 frozen PDF figures
│   ├── tables/                 # 44 frozen CSV tables
│   └── supporting/             # Execution manifest/supporting notes
├── metadata/                   # Environment, provenance, manifests, checksums
├── docs/                       # Technical-freeze and repository notes
├── scripts/                    # Verification and reproduction helpers
├── environment.yml
├── requirements.txt
└── requirements-inference.txt
```

## Reproduce the final analysis

The final analysis notebook does **not** rerun LLM inference. It consumes the frozen, hash-verified benchmark and response dataset included in this repository.

### Conda

```bash
conda env create -f environment.yml
conda activate alignsec-final-analysis
python scripts/verify_repository.py
jupyter nbconvert --to notebook --execute analysis/AlignSec_Final_Analysis.ipynb \
  --output AlignSec_Final_Analysis_REPRODUCED.ipynb \
  --ExecutePreprocessor.timeout=600
```

### pip

```bash
python -m pip install -r requirements.txt
python scripts/verify_repository.py
jupyter nbconvert --to notebook --execute analysis/AlignSec_Final_Analysis.ipynb \
  --output AlignSec_Final_Analysis_REPRODUCED.ipynb \
  --ExecutePreprocessor.timeout=600
```

If your notebook environment does not start from the repository root, set `ALIGNSEC_PROJECT_ROOT` to the repository root before execution.

## Primary endpoint

The primary leakage endpoint is mechanically recomputed exact-canary disclosure after minimal formatting normalization (`\\_` → `_`). The study does not use fuzzy, semantic, partial, or encoded matching as the primary endpoint.

## Statistical analysis

- Language-vs-English: exact paired McNemar tests with BH-FDR across 12 non-English comparisons.
- Overall clean-model comparison: base-template cluster bootstrap over 80 underlying attack templates plus paired sign-flip randomization (100,000 draws), with BH-FDR across 3 model comparisons.
- Language-specific model comparisons: exact paired McNemar tests.
- CLIRS uncertainty: paired base-template bootstrap, 10,000 iterations.
- Attack-category uncertainty: base-template cluster bootstrap where estimable; Wilson descriptive fallback for singleton-template categories.

## Reproducibility and provenance boundaries

Historical execution evidence records a Tesla T4 and PyTorch `2.10.0+cu128`. Exact historical Transformers, Accelerate, bitsandbytes versions and Hugging Face repository commit SHAs were not recorded and are not retroactively invented.

The historical Qwen run is supported by execution evidence and a preserved v5 runner with matching run stage, schema, checkpoint cadence, and naming conventions. The original byte-identical standalone Qwen source cell was not preserved, so the repository supplies a transparent reconstruction instead of claiming an original source artifact.

See:
- `docs/TECHNICAL_FREEZE.md`
- `inference/provenance/QWEN_PROVENANCE_RESOLUTION.md`
- `metadata/`

## Historical naming note

A small number of frozen analysis-internal run tags and generated artifact names retain the historical `EAAI` label from the development stage. These names are preserved so the public repository remains traceable to the exact frozen analysis. The current repository and manuscript work are journal-neutral from a technical perspective.

## Security and ethical scope

The benchmark uses synthetic canary values only. No real passwords, credentials, personal records, or confidential enterprise data are included. AlignSec is an evaluation framework; it does not implement or claim a prompt-injection defense.

## Citation

Citation metadata is provided in `CITATION.cff`. The repository author list/version should be synchronized with the final publication before creating the archival release/DOI.

## License

Software code in this repository is released under the MIT License. Model-generated outputs and associated response datasets are provided for research reproducibility and should also be used consistently with the licenses/terms of the respective source models.
