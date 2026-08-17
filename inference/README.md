# Inference artifacts

This directory preserves the available historical inference code and provenance evidence. Reproducing the **final statistical analysis** does not require rerunning model inference; use the frozen response data under `data/`.

## Mistral

`mistral/mistral_inference.ipynb` is the preserved historical Mistral runner associated with the frozen v4 benchmark baseline.

## Zephyr and Llama-2

`zephyr_llama2/zephyr_llama2_inference.ipynb` is the preserved shared historical runner used for the Zephyr and Llama-2 frozen-v4 stage. Llama-2 is retained as a diagnostic model because it produced three observed benign canary leaks.

## Qwen

The historical Qwen run completed all 800 frozen benchmark items, but the byte-identical standalone Qwen source cell and separately preserved original raw CSV were not retained. The repository therefore provides:

- `qwen/qwen_historical_run_reconstruction.py` — transparent reconstruction of the historical invocation logic;
- `provenance/QWEN_PROVENANCE_RESOLUTION.md` — provenance resolution and claim boundaries;
- `provenance/Qwen2_5_3B_historical_execution_record.txt` — preserved execution evidence;
- `../data/raw_responses/qwen_raw_outputs_RECONSTRUCTED_FROM_FROZEN_FINAL_DATA.csv` — explicitly labelled lossless reconstruction of the 19-column historical raw format from the frozen final dataset.

## Historical environment boundary

Preserved evidence records a Tesla T4 GPU and PyTorch `2.10.0+cu128`. The setup code specified minimum dependencies of Transformers `>=4.44.0`, Accelerate `>=0.33.0`, and bitsandbytes `>=0.43.0`, but the exact historical versions present during the final inference runs were not saved in executed output. Exact Hugging Face repository commit revisions were also not recorded. Therefore inference reruns are not claimed to reproduce historical outputs bit-for-bit.
