#!/usr/bin/env python3
"""Freeze the v2 held-out protocol before any model calls."""
from __future__ import annotations
import hashlib,json,random
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
COMPONENTS=[HERE/"README.md",HERE/"instrument/scenarios.json",HERE/"instrument/prompt-template.md",HERE/"instrument/calibration-cases.json",HERE/"run_study.py",ROOT/"pilots/configured-artifact-revision/launcher.py",ROOT/"papers/agent-benchmarks/2026-07-16-pmbench-prospective-memory-validity.md",ROOT/"docs/benchmark-design-taxonomy.md"]
def sha(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def main()->None:
 scenarios=json.loads((HERE/"instrument/scenarios.json").read_text())["scenarios"];rows=[]
 for s in scenarios:
  for condition in ("neutral_interrupt","channel_hint","oracle_reminder"):
   token=hashlib.sha256(f"{s['scenario_id']}:{condition}:1:delayed-v2".encode()).hexdigest()[:10];rows.append({"attempt_id":f"dot2-{token}","scenario_id":s["scenario_id"],"work_shape":s["work_shape"],"condition_id":condition,"repeat":1})
 random.Random(716202602).shuffle(rows)
 for i,row in enumerate(rows,1):row["execution_order"]=i
 claims={x:False for x in ["general_prospective_memory","causal_treatment_effect","agent_capability","professional_capability","expert_validity","cross_domain_generality","safety","production_fitness","deployment_readiness","population_representativeness"]}
 protocol={
  "schema_version":"0.2.0","protocol_id":"delayed-obligation-heldout-v2","frozen_at":"2026-07-16T01:15:03Z",
  "charter_decision_filter":{"objectives":["B: expertise-to-evaluation methodology","C: executable infrastructure"],"artifact":"immutable four-form held-out matrix, discriminating primary graders, harness-observed channel flow, exact replay","uncertainty":"whether v1 obligation signatures and primary-work ceiling persist on unseen forms where primary subchecks can fail","mode":"building and validation","duplication":"v1 bytes are preserved; v2 is a prospectively versioned equivalent-form extension","scope_boundary":"two purposive synthetic work shapes test reusable machinery, not domain or cross-domain generality","useful_completion":"zero-call isolation/perfect/failure/mutation canaries pass; all twelve intended attempts are retained including invalid or service failures; exact replay succeeds"},
  "development_evidence":{"path":"pilots/delayed-obligation-dual-task/validity-record.json","role":"v1 development evidence only","immutable":True},
  "configured_system":{"model":"gpt-5.6-sol","provider":"openai-codex","toolsets":["file"],"safe_mode":True,"invocation":"fresh oneshot each of three turns","timeout_seconds_per_turn":900,"retries":0,"replacement":"none","launcher":"pilots/configured-artifact-revision/launcher.py"},
  "schedule":{"order_seed":716202602,"rows":rows,"outcome_based_retry":"forbidden","selective_replacement":"forbidden"},
  "held_fixed":{"turns":3,"attempts_per_cell":1,"forms_per_shape":2,"conditions_per_form":3,"obligation_form":"one original, one replacement/update, one obsolete lure, one public due cue","prompt_and_grader":"same except declared form and treatment","budget":"three calls per attempt; 36 calls intended"},
  "treatments":{"neutral_interrupt":"non-answer-bearing interruption; channel content requires prior query","channel_hint":"names obligation channel without contents; channel content requires prior query","oracle_reminder":"privileged evaluator-derived current update/action reminder"},
  "channel_instrumentation":{"query_issuance":"recorded from each submitted action artifact","availability":"set by harness from prior-turn query","returned_evidence":"exact harness-returned update recorded per turn","due_cue":"public harness event recorded","encoding":"unobserved","adoption":"unobserved","agent_state":"retained as self-report only"},
  "reporting":{"no_shape_pooling":True,"no_condition_pooling":True,"descriptive_only":True,"outcomes":["primary_subchecks_by_turn","update_exposure","update_reconciliation","due_status_timing","action_realization","obsolete_lure_commission","collateral_loss","calls_tokens_cost_latency","invalid_service_environment"]},
  "invalidity":{"service":"nonzero call or missing/failed usage record; retained in intended denominator","environment":"failed isolation canary or input mutation","artifact":"missing/malformed turn JSON or primary object","comparison":"cell-specific exact denominators; no effect estimate"},
  "claim_boundaries":claims,
  "frozen_components":[{"path":str(x.relative_to(ROOT)),"sha256":sha(x),"bytes":x.stat().st_size} for x in COMPONENTS]
 }
 out=HERE/"protocol.json";out.write_text(json.dumps(protocol,indent=2,sort_keys=True)+"\n");print(json.dumps({"path":str(out.relative_to(ROOT)),"sha256":sha(out),"attempts":len(rows)},indent=2))
if __name__=="__main__":main()
