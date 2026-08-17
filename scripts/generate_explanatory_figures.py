from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "figures"
OUT.mkdir(parents=True, exist_ok=True)

def box(ax, xy, w, h, text, fs=9):
    p=FancyBboxPatch(xy,w,h,boxstyle="round,pad=0.02",linewidth=1.2,facecolor="white",edgecolor="black")
    ax.add_patch(p)
    ax.text(xy[0]+w/2,xy[1]+h/2,text,ha="center",va="center",fontsize=fs,wrap=True)
    return p

def arrow(ax,a,b):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle="->",mutation_scale=12,linewidth=1.1))

def save(fig,name):
    fig.savefig(OUT/f"{name}.pdf",bbox_inches="tight")
    fig.savefig(OUT/f"{name}.svg",bbox_inches="tight")
    plt.close(fig)

# 1 Benchmark schema
fig,ax=plt.subplots(figsize=(12,6.8)); ax.set_xlim(0,12); ax.set_ylim(0,7); ax.axis('off')
ax.text(6,6.65,'AlignSec Benchmark Schema and Example Evaluation Paths',ha='center',va='center',fontsize=14,weight='bold')
ax.text(0.35,5.35,'Attack',fontsize=11,weight='bold'); ax.text(0.35,2.25,'Benign',fontsize=11,weight='bold')
xs=[1.1,3.15,5.25,7.25,9.2,10.8]; w=[1.45,1.55,1.4,1.3,1.35,1.0]
attack_labels=['Prompt ID','Protected context\n+ unique canary','Localized attack\nobjective','LLM response','Exact-canary\ndetector','Attack success\n/ no leak']
benign_labels=['Prompt ID','Protected context\n+ unique canary','Benign request','LLM response','Exact-canary\ndetector','Benign leak\n/ no leak']
for y,labels in [(4.7,attack_labels),(1.6,benign_labels)]:
    centers=[]
    for x,ww,t in zip(xs,w,labels):
        box(ax,(x,y),ww,0.9,t); centers.append((x,ww))
    for (x1,w1),(x2,w2) in zip(centers,centers[1:]): arrow(ax,(x1+w1,y+0.45),(x2,y+0.45))
ax.text(6,0.35,'English is the anchor condition. Non-English conditions retain the shared English protected-context scaffold while localizing the task/objective.',ha='center',fontsize=9)
ax.text(6,0.05,'Resource-tier labels are descriptive metadata, not causal experimental factors.',ha='center',fontsize=9)
save(fig,'benchmark_schema')

# 2 Workflow
fig,ax=plt.subplots(figsize=(13,5.6)); ax.set_xlim(0,13); ax.set_ylim(0,5.6); ax.axis('off')
ax.text(6.5,5.25,'AlignSec End-to-End Evaluation Workflow',ha='center',fontsize=14,weight='bold')
labels=['Frozen\nbenchmark','Verify\ninputs','Construct\nprompt','LLM\ninference','Store raw\nresponse','Exact-canary\ndetection','Attack / benign\nsplit','Benign-clean\nscreen','Metrics + paired /\ncluster-aware statistics','Figures, tables,\nmetadata']
xs=[0.25,1.55,2.75,4.05,5.25,6.55,7.85,9.15,10.35,11.75]
ws=[1.0,0.95,1.0,1.0,1.0,1.05,1.05,1.0,1.15,1.0]
y=2.75
for x,wid,t in zip(xs,ws,labels): box(ax,(x,y),wid,1.0,t,fs=8.5)
for i in range(len(xs)-1): arrow(ax,(xs[i]+ws[i],y+0.5),(xs[i+1],y+0.5))
ax.text(6.5,1.55,'Mistral, Qwen and Zephyr → primary clean comparison',ha='center',fontsize=9.5)
ax.text(6.5,1.15,'Llama-2 → diagnostic branch after three observed benign canary leaks',ha='center',fontsize=9.5)
ax.text(6.5,0.55,'No training or fine-tuning occurs; the frozen benchmark remains unchanged throughout evaluation.',ha='center',fontsize=9)
save(fig,'evaluation_workflow')

# 3 Architecture
fig,ax=plt.subplots(figsize=(9.5,9)); ax.set_xlim(0,10); ax.set_ylim(0,10); ax.axis('off')
ax.text(5,9.6,'AlignSec Security-Evaluation System Architecture',ha='center',fontsize=14,weight='bold')
components=[
(8.45,'Benchmark Manager','Frozen IDs, schema, canaries,\nlanguage conditions, integrity'),
(7.25,'Prompt Constructor','System instruction + protected context\n+ canary + localized attack/benign task'),
(6.05,'Model Interface','Mistral | Qwen | Zephyr | Llama-2\nDeterministic standardized inference'),
(4.85,'Response Logger','Prompt/model/language/canary/response\nlatency and run metadata'),
(3.65,'Leakage Detector','Minimal normalization + exact-canary containment\nAttack / benign disclosure indicators'),
(2.45,'Eligibility / Diagnostic Layer','0 benign leaks + 0 invalid outputs → clean comparison\notherwise → diagnostic analysis'),
(1.25,'Statistical Analyzer','ASR, BLR, CLIRS, Wilson CI, McNemar, BH-FDR,\ncluster bootstrap, sign-flip tests, category analysis'),
(0.05,'Artifact Exporter','CSVs, PDFs, manifests, provenance, checksums,\nreproducibility files')]
for y,title,sub in components:
    box(ax,(1.35,y),7.3,0.85,f'{title}\n{sub}',fs=8.8)
for i in range(len(components)-1):
    y1=components[i][0]; y2=components[i+1][0]
    arrow(ax,(5,y1),(5,y2+0.85))
ax.text(9.35,5.0,'Data → Prompting → Model → Detection → Statistics → Reproducibility',rotation=90,ha='center',va='center',fontsize=9)
save(fig,'system_architecture')

print(f"Wrote explanatory figures to {OUT}")
