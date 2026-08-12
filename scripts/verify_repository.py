from pathlib import Path
import hashlib
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    ROOT / "data" / "final_results.csv": "405a5017589b4722fbcad13a5c43a555d3e5afc6498fe46cf5a16a63baaf91f4",
    ROOT / "data" / "benchmark" / "frozen_alignsec_v4_benchmark.csv": "d0bba7ade1d3801cdab983c277303c35c4200985abd48cf4001b71fa555b3d46",
}

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

errors = []
for path, expected in EXPECTED.items():
    if not path.exists():
        errors.append(f"Missing frozen input: {path.relative_to(ROOT)}")
        continue
    actual = sha256(path)
    if actual != expected:
        errors.append(
            f"SHA-256 mismatch for {path.relative_to(ROOT)}: expected {expected}, got {actual}"
        )
    else:
        print(f"[OK] SHA-256 {path.relative_to(ROOT)}")

if not errors:
    final_df = pd.read_csv(ROOT / "data" / "final_results.csv")
    bench_df = pd.read_csv(ROOT / "data" / "benchmark" / "frozen_alignsec_v4_benchmark.csv")
    if len(final_df) != 3200:
        errors.append(f"Expected 3200 final rows, found {len(final_df)}")
    else:
        print("[OK] final_results.csv rows = 3200")
    if len(bench_df) != 800:
        errors.append(f"Expected 800 benchmark rows, found {len(bench_df)}")
    else:
        print("[OK] frozen benchmark rows = 800")
    if {"model_canonical", "prompt_id"}.issubset(final_df.columns):
        dups = int(final_df.duplicated(["model_canonical", "prompt_id"]).sum())
        if dups != 0:
            errors.append(f"Expected 0 duplicate model/prompt rows, found {dups}")
        else:
            print("[OK] duplicate model/prompt rows = 0")

pdf_count = len(list((ROOT / "outputs" / "figures").glob("*.pdf")))
csv_count = len(list((ROOT / "outputs" / "tables").glob("*.csv")))
print(f"[INFO] PDF figures = {pdf_count}")
print(f"[INFO] CSV tables = {csv_count}")
if pdf_count != 15:
    errors.append(f"Expected 15 PDF figures, found {pdf_count}")
if csv_count != 44:
    errors.append(f"Expected 44 CSV tables, found {csv_count}")

required = [
    ROOT / "analysis" / "AlignSec_Final_Analysis.ipynb",
    ROOT / "analysis" / "AlignSec_Final_Analysis_EXECUTED.ipynb",
    ROOT / "inference" / "mistral" / "mistral_inference.ipynb",
    ROOT / "inference" / "zephyr_llama2" / "zephyr_llama2_inference.ipynb",
    ROOT / "inference" / "qwen" / "qwen_historical_run_reconstruction.py",
    ROOT / "inference" / "provenance" / "QWEN_PROVENANCE_RESOLUTION.md",
]
for path in required:
    if not path.exists():
        errors.append(f"Missing required artifact: {path.relative_to(ROOT)}")
    else:
        print(f"[OK] {path.relative_to(ROOT)}")

if errors:
    print("\nRepository verification FAILED:")
    for error in errors:
        print(" -", error)
    sys.exit(1)

print("\nRepository verification PASSED.")
