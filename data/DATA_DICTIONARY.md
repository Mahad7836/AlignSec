# AlignSec data dictionary

This document defines the fields used in the frozen benchmark and final response dataset. The frozen CSV files themselves are not modified by this documentation.

## Frozen benchmark: `data/benchmark/frozen_alignsec_v4_benchmark.csv`

| Field | Meaning |
|---|---|
| `prompt_id` | Stable identifier for one frozen benchmark item. |
| `language` | Evaluated language condition: English, French, Arabic, Bengali, or Sindhi. |
| `resource_tier` | Descriptive language-resource label used as metadata only; not treated as a causal variable. |
| `prompt_type` | Whether the benchmark item is an adversarial `attack` prompt or a `benign` control. |
| `attack_category` | Attack-family label for adversarial items; not applicable to benign controls. |
| `base_text` | Underlying base task/attack text used to preserve pairing across language conditions. |
| `base_text_sanitized` | Sanitized representation of the base text used during benchmark construction/auditing. |
| `localized_task` | Language-retargeted task or adversarial objective for the selected condition. |
| `protected_context` | Shared protected-context scaffold containing the assigned synthetic canary. |
| `final_prompt` | Final user-facing benchmark prompt after controlled construction. |
| `prompt` | Stored prompt field retained from the frozen benchmark build. |
| `canary_value` | Unique synthetic protected value assigned to the benchmark item. |
| `source_group` | Construction/source grouping such as built-in safe attack templates, benign bank, or public attack source. |
| `source_dataset` | External dataset identifier when applicable; otherwise records the benchmark source provenance. |
| `is_attack` | Boolean indicator for whether the row is adversarial. |
| `stage` | Frozen benchmark construction/evaluation-stage metadata. |

## Final response dataset: `data/final_results.csv`

| Field | Meaning |
|---|---|
| `model_id` | Upstream model repository identifier used for inference. |
| `model_short_name` | Short display name recorded by the historical runner. |
| `model_family` | Model-family metadata recorded during inference. |
| `model_run_stage` | Historical inference-stage/run tag. |
| `stage` | Historical benchmark/evaluation stage retained in the response record. |
| `prompt_id` | Stable identifier linking the response to one frozen benchmark item. |
| `language` | Evaluated language condition. |
| `resource_tier` | Descriptive language-resource metadata; not causal. |
| `prompt_type` | Attack or benign control. |
| `attack_category` | Attack-family label when applicable. |
| `source_group` | Benchmark construction/source grouping. |
| `source_dataset` | External source identifier when applicable. |
| `canary_value` | Synthetic protected value assigned to the benchmark item. |
| `label` | Historical qualitative response label retained for provenance; not the primary leakage endpoint. |
| `latency_seconds` | Historical inference latency for the response; descriptive only and not a controlled efficiency benchmark. |
| `base_text` | Underlying base attack/task text. |
| `localized_task` | Language-retargeted task or adversarial objective. |
| `final_prompt` | Final prompt sent to the model. |
| `response` | Generated model response. |
| `model_canonical` | Canonical model key used by the final analysis. |
| `source_csv_path` | Historical local build-path metadata retained to preserve the byte-identical frozen dataset; not required for reproduction. |
| `source_priority` | Historical source-selection/deduplication priority metadata from the final dataset build. |
| `exact_canary_in_response` | Mechanically recomputed indicator that the assigned normalized canary occurs in the response. |
| `label_implies_canary_leak` | Audit field indicating whether the historical qualitative label implied a canary leak; used for consistency checks, not as the primary endpoint. |

## Frozen-path note

`source_csv_path` contains historical `/mnt/data/...` build paths from the original analysis assembly environment. These strings are provenance metadata only. They are intentionally retained so that `data/final_results.csv` remains byte-identical to the frozen analysis input and are not external dependencies required to reproduce the analysis.
