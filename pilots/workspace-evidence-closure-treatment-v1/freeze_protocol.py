#!/usr/bin/env python3
"""Freeze matched workspace-closure protocol before provider calls."""
from __future__ import annotations
import hashlib,json,random
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
def sha(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def main()->None:
 components=[HERE/"README.md",HERE/"run_study.py",HERE/"instrument/public-guide.md",HERE/"instrument/calibration-cases.json",HERE/"instrument/record/task.md",HERE/"instrument/record/sources/brief.json",HERE/"instrument/record/sources/draft.json",HERE/"instrument/memo/task.md",HERE/"instrument/memo/sources/brief.md",HERE/"instrument/memo/sources/draft.md",ROOT/"pilots/configured-artifact-revision/launcher.py",ROOT/"papers/agent-benchmarks/2026-07-17-paper-replication-workspace-evidence-validity.md",ROOT/"data/sources/releases/2607.02134v2-paper-replication/release-audit.json",ROOT/"pilots/workspace-evidence-closure-conformance/report.json"]
 rows=[]
 for shape in ("record","memo"):
  for repeat in (1,2):
   nonce=hashlib.sha256(f"workspace-closure-v1:{shape}:{repeat}".encode()).hexdigest()[:12]
   for condition in ("no_workspace","workspace"):
    token=hashlib.sha256(f"{shape}:{condition}:{repeat}:{nonce}".encode()).hexdigest()[:10];rows.append({"attempt_id":f"wec-{token}","shape":shape,"condition":condition,"repeat":repeat,"pair_nonce":nonce})
 random.Random(17072026).shuffle(rows)
 for i,x in enumerate(rows,1):x["execution_order"]=i
 claims={x:False for x in ("expertise_transfer","universal_workflow_efficacy","configured_system_reliability","cross_domain_generality","professional_validity","safety","production_fitness","deployment_readiness")}
 p={"schema_version":"0.1.0","protocol_id":"workspace-evidence-closure-treatment-v1","frozen_at":"2026-07-16T21:10:00Z","charter_decision_filter":{"objectives":["B: expertise-to-evaluation methodology","C: executable infrastructure"],"artifact":"frozen two-shape matched treatment, isolated attempts, independent grades, and replayable report","uncertainty":"whether durable obligation/check closure changes independently checked outcomes under a fixed configured system","mode":"building and validation","duplication":"extends the completed deterministic conformance slice into a prospective treatment without changing its contracts","scope":"two structurally unlike synthetic shapes test reusable machinery; no profession or cross-domain claim","useful_completion":"preflight and mutations pass; eight intended attempts are retained or typed invalid; outcomes and paired differences stay separate"},"configured_system":{"model":"gpt-5.6-sol","provider":"openai-codex","toolsets":["file"],"safe_mode":True,"invocation":"fresh oneshot","calls_per_attempt":1,"timeout_seconds":900,"retries":0,"replacement":"none","seed_control":"provider unsupported","pair_nonce":"frozen opaque label shared within pair"},"held_fixed":{"within_pair":["model/provider/version","tools","task and source bytes","one-call budget","timeout","stopping rule","independent grader","severe-defect rule","invalid policy"],"treatment_difference":"workspace condition alone receives public-guide.md; no private checks, labels, expected values, or evaluator rationales","invalid_policy":"retain every intended attempt; substantive metrics require service, environment, artifact, and included-zero-cost validity; never replace invalids"},"schedule":rows,"stopping_rule":"one provider invocation; stop when outputs are written or provider terminates","outcomes":["artifact completion","independent correctness","obligation coverage","predicate satisfaction","source entailment","execution-to-byte lineage","report freshness","repair retention","new errors","severe defects","latency","tokens","cost","service invalids","paired effects"],"frozen_components":[{"path":str(x.relative_to(ROOT)),"sha256":sha(x)} for x in components],"claim_boundaries":claims}
 out=HERE/"protocol.json";out.write_text(json.dumps(p,indent=2,sort_keys=True)+"\n");print(json.dumps({"path":str(out.relative_to(ROOT)),"sha256":sha(out),"attempts":len(rows)},indent=2))
if __name__=="__main__":main()
