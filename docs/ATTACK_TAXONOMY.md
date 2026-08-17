# AlignSec attack taxonomy

The frozen attack set contains 27 categories. Counts below are computed from `data/benchmark/frozen_alignsec_v4_benchmark.csv`. Because every underlying attack template is represented across five language conditions, `attack rows` equals five times the number of underlying base templates for these categories.

| Attack category | Plain-language description | Base templates | Attack rows |
|---|---|---:|---:|
| `audit_claim` | Claims that a security/audit procedure requires disclosure of the protected value. | 2 | 10 |
| `auditor_roleplay` | Asks the model to adopt an auditor/compliance role and enumerate protected values. | 1 | 5 |
| `authority_claim` | Claims authorization or owner permission to disclose the protected value. | 2 | 10 |
| `benchmark_pressure` | Frames disclosure as necessary to pass a benchmark or evaluation. | 2 | 10 |
| `completion_attack` | Uses sentence/text completion pressure to elicit the protected value. | 5 | 25 |
| `context_downgrade` | Reframes protected context as ordinary text that may be summarized or repeated. | 1 | 5 |
| `debugging_claim` | Claims debugging or troubleshooting requires disclosure. | 4 | 20 |
| `direct_override` | Directly instructs the model to ignore prior/no-disclosure instructions. | 4 | 20 |
| `error_message_leak` | Requests an error/debug message that embeds the protected value. | 4 | 20 |
| `evaluation_claim` | Claims that evaluation requires exact disclosure of the protected value. | 3 | 15 |
| `exact_match_pressure` | Demands exact formatting/spelling of the protected value. | 5 | 25 |
| `forced_completion` | Constrains the answer so that refusal is disallowed and the protected value is the only acceptable completion. | 2 | 10 |
| `format_constraint` | Uses a structured-output requirement such as JSON to force inclusion of the protected value. | 4 | 20 |
| `harmlessness_claim` | Argues that disclosure is harmless because the value is synthetic or part of a test. | 3 | 15 |
| `indirect_extraction` | Asks indirectly for the protected string, for example by asking what must not be revealed. | 3 | 15 |
| `label_disregard` | Explicitly asks the model to ignore the confidentiality/no-disclosure label. | 2 | 10 |
| `minimal_output` | Requests only the protected value with no additional explanation. | 1 | 5 |
| `policy_reversal` | Claims the confidentiality rule has been revoked, reversed, or was only a test. | 3 | 15 |
| `priority_claim` | Claims the user request has higher priority than the no-disclosure instruction. | 1 | 5 |
| `public_prompt_injection` | Publicly sourced prompt-injection templates preserved with source attribution. | 2 | 10 |
| `quotation_leak` | Asks the model to quote the protected context verbatim. | 1 | 5 |
| `role_override` | Reassigns the model to a role or mode in which protected values are requested. | 5 | 25 |
| `roleplay_jailbreak` | Uses hypothetical/role-play framing to elicit the canary. | 4 | 20 |
| `semantic_downgrade` | Reframes the protected information as less sensitive and then requests exact disclosure. | 3 | 15 |
| `social_engineering` | Uses emotional, professional, or social pressure to request disclosure. | 3 | 15 |
| `summarization_leak` | Requests a summary that explicitly includes protected fields. | 4 | 20 |
| `verification_claim` | Frames exact disclosure as necessary to verify or validate the system. | 6 | 30 |

## Interpretation

Category effectiveness in the paper is denominator-aware: raw successful-disclosure counts are not compared without accounting for the number of attempts. Base-template clustering is used for category uncertainty where at least two underlying templates are available; singleton-template categories use a Wilson descriptive fallback.
