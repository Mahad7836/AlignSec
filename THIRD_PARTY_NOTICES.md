# Third-party notices

AlignSec includes or references materials associated with third-party datasets and model repositories. The root MIT License applies only to AlignSec software/code authored by the project and does not override upstream licenses, model terms, acceptable-use policies, or dataset terms.

## Public attack source

Two underlying attack templates in the frozen benchmark were sourced from the public dataset identifier `deepset/prompt-injections` and retargeted across the five AlignSec language conditions, producing 10 benchmark rows under `source_group=PublicAttackSource`. The frozen benchmark preserves the source identifier in `source_dataset`. Users should consult the upstream dataset repository for its current license and attribution requirements.

Upstream source: `https://huggingface.co/datasets/deepset/prompt-injections`

## Evaluated model repositories

AlignSec does not redistribute model weights. The repository contains generated responses and inference/provenance artifacts associated with the following upstream model identifiers:

- `mistralai/Mistral-7B-Instruct-v0.2`
- `Qwen/Qwen2.5-3B-Instruct`
- `HuggingFaceH4/zephyr-7b-beta`
- `NousResearch/Llama-2-7b-chat-hf`

Use of model weights or other upstream materials remains subject to the terms published by their respective providers.
