from pathlib import Path
import hashlib, json, sys
import pandas as pd
import nbformat

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_HASHES = {
    "data/final_results.csv": "405a5017589b4722fbcad13a5c43a555d3e5afc6498fe46cf5a16a63baaf91f4",
    "data/benchmark/frozen_alignsec_v4_benchmark.csv": "d0bba7ade1d3801cdab983c277303c35c4200985abd48cf4001b71fa555b3d46",
}
MODELS = {"mistral_7b_instruct_v0_2", "qwen2_5_3b_instruct", "zephyr_7b_beta", "llama2_7b_chat_failed_diagnostic"}
LANGS = {"English", "French", "Arabic", "Bengali", "Sindhi"}

def sha256(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024), b""):
            h.update(chunk)
    return h.hexdigest()

def norm(s):
    return str(s).replace("\\_", "_")

errors=[]
def ok(msg): print("[OK]",msg)
def fail(msg): errors.append(msg)

# Frozen hashes
for rel,exp in EXPECTED_HASHES.items():
    p=ROOT/rel
    if not p.exists(): fail(f"Missing frozen input: {rel}"); continue
    act=sha256(p)
    if act!=exp: fail(f"SHA-256 mismatch for {rel}: expected {exp}, got {act}")
    else: ok(f"SHA-256 {rel}")

if not errors:
    final=pd.read_csv(ROOT/"data/final_results.csv")
    bench=pd.read_csv(ROOT/"data/benchmark/frozen_alignsec_v4_benchmark.csv")
    if len(final)!=3200: fail(f"Expected 3200 final rows, found {len(final)}")
    else: ok("final_results.csv rows = 3200")
    if len(bench)!=800: fail(f"Expected 800 benchmark rows, found {len(bench)}")
    else: ok("frozen benchmark rows = 800")
    if set(final.model_canonical.unique())!=MODELS: fail("Unexpected canonical model set")
    else: ok("canonical model set = 4 expected models")
    if set(bench.language.unique())!=LANGS: fail("Unexpected benchmark language-condition set")
    else: ok("language conditions = 5 expected conditions")
    vc=final.model_canonical.value_counts()
    if not (vc==800).all(): fail(f"Expected 800 rows/model, got {vc.to_dict()}")
    else: ok("800 rows per model")
    for m,g in final.groupby('model_canonical'):
        pt=g.prompt_type.value_counts().to_dict()
        if pt.get('attack')!=400 or pt.get('benign')!=400: fail(f"{m}: expected 400 attack/400 benign, got {pt}")
        for lang,lg in g.groupby('language'):
            lpt=lg.prompt_type.value_counts().to_dict()
            if lpt.get('attack')!=80 or lpt.get('benign')!=80: fail(f"{m}/{lang}: expected 80 attack/80 benign, got {lpt}")
    if not any(x.startswith('Expected 400') for x in errors): ok("400 attack + 400 benign/model; 80 + 80/language")
    dups=int(final.duplicated(['model_canonical','prompt_id']).sum())
    if dups: fail(f"Expected 0 duplicate model/prompt rows, found {dups}")
    else: ok("duplicate model/prompt rows = 0")
    if bench.prompt_id.nunique()!=800: fail(f"Expected 800 unique prompt IDs, found {bench.prompt_id.nunique()}")
    else: ok("unique prompt IDs = 800")
    if bench.canary_value.nunique()!=800: fail(f"Expected 800 unique canaries, found {bench.canary_value.nunique()}")
    else: ok("unique canaries = 800")

    # benchmark identity across models
    keys=['prompt_id','language','resource_tier','prompt_type','attack_category','source_group','source_dataset','canary_value','base_text','localized_task','final_prompt']
    ref=bench[keys].sort_values('prompt_id').reset_index(drop=True).fillna('')
    for m,g in final.groupby('model_canonical'):
        cur=g[keys].sort_values('prompt_id').reset_index(drop=True).fillna('')
        if not cur.equals(ref): fail(f"Benchmark identity mismatch for {m}")
    if not any('Benchmark identity mismatch' in e for e in errors): ok("benchmark identity across models")

    # exact canary recomputation
    recomputed=[norm(c) in norm(r) for c,r in zip(final.canary_value, final.response.fillna(''))]
    stored=final.exact_canary_in_response.astype(bool).tolist()
    mism=sum(a!=b for a,b in zip(recomputed,stored))
    if mism: fail(f"Exact-canary recomputation mismatches = {mism}")
    else: ok("exact-canary recomputation matches 3200/3200")

# Frozen statistical output counts
pdfs=list((ROOT/'outputs/figures').glob('*.pdf')); csvs=list((ROOT/'outputs/tables').glob('*.csv'))
if len(pdfs)!=15: fail(f"Expected 15 frozen PDF figures, found {len(pdfs)}")
else: ok("frozen PDF figures = 15")
if len(csvs)!=44: fail(f"Expected 44 frozen CSV tables, found {len(csvs)}")
else: ok("frozen CSV tables = 44")

# Required artifacts
required=[
'analysis/AlignSec_Final_Analysis.ipynb','analysis/AlignSec_Final_Analysis_EXECUTED.ipynb',
'inference/mistral/mistral_inference.ipynb','inference/zephyr_llama2/zephyr_llama2_inference.ipynb',
'inference/qwen/qwen_historical_run_reconstruction.py','inference/provenance/QWEN_PROVENANCE_RESOLUTION.md',
'inference/provenance/Qwen2_5_3B_historical_execution_record.txt','metadata/model_provenance.csv',
'data/DATA_DICTIONARY.md','docs/ATTACK_TAXONOMY.md','docs/ARTIFACT_MAP.md','THIRD_PARTY_NOTICES.md',
'docs/figures/benchmark_schema.pdf','docs/figures/evaluation_workflow.pdf','docs/figures/system_architecture.pdf']
for rel in required:
    if not (ROOT/rel).exists(): fail(f"Missing required artifact: {rel}")
if not any('Missing required artifact' in e for e in errors): ok("required repository artifacts present")

# Model-provenance paths/hashes
try:
    p=pd.read_csv(ROOT/'metadata/model_provenance.csv')
    for _,r in p.iterrows():
        for fcol,hcol in [('raw_response_file','raw_response_sha256'),('inference_code_file','inference_code_sha256'),('benchmark','benchmark_sha256')]:
            fp=ROOT/str(r[fcol])
            if not fp.exists(): fail(f"model_provenance missing path: {r[fcol]}")
            elif sha256(fp)!=str(r[hcol]): fail(f"model_provenance hash mismatch: {r[fcol]}")
    if not any('model_provenance' in e for e in errors): ok("model provenance paths and hashes")
except Exception as e: fail(f"Could not validate model_provenance.csv: {e}")

# Executed notebook errors
try:
    nb=nbformat.read(ROOT/'analysis/AlignSec_Final_Analysis_EXECUTED.ipynb',as_version=4)
    errs=[]; code=0; executed=0
    for cell in nb.cells:
        if cell.cell_type=='code':
            code+=1
            if cell.get('execution_count') is not None: executed+=1
            for out in cell.get('outputs',[]):
                if out.get('output_type')=='error': errs.append(out.get('ename','error'))
    if errs: fail(f"Executed notebook contains error outputs: {errs}")
    else: ok(f"executed notebook error outputs = 0 ({executed}/{code} code cells executed)")
except Exception as e: fail(f"Could not inspect executed notebook: {e}")

# Current repository manifest + checksum list (generated after final files)
manifest=ROOT/'metadata/repository_manifest.csv'
checks=ROOT/'metadata/repository_SHA256SUMS.txt'
if not manifest.exists(): fail('Missing metadata/repository_manifest.csv')
if not checks.exists(): fail('Missing metadata/repository_SHA256SUMS.txt')
if manifest.exists():
    try:
        mf=pd.read_csv(manifest)
        missing=[x for x in mf.path if not (ROOT/x).exists()]
        if missing: fail(f"Repository manifest has missing paths: {missing[:5]}")
        else: ok(f"repository manifest paths = {len(mf)} present")
    except Exception as e: fail(f"Could not validate repository manifest: {e}")
if checks.exists():
    bad=[]; n=0
    for line in checks.read_text(encoding='utf-8').splitlines():
        if not line.strip(): continue
        hx,rel=line.split('  ',1); n+=1; fp=ROOT/rel
        if not fp.exists() or sha256(fp)!=hx: bad.append(rel)
    if bad: fail(f"Repository checksum mismatches: {bad[:5]}")
    else: ok(f"repository SHA-256 entries = {n} verified")

if errors:
    print("\nRepository verification FAILED:")
    for e in errors: print(" -",e)
    sys.exit(1)
print("\nRepository verification PASSED.")
