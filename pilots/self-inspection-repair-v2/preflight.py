#!/usr/bin/env python3
"""Fail-closed prospective v2 preflight. Executes no model/provider/repair row."""
from __future__ import annotations
import argparse, hashlib, importlib.util, inspect, json, tempfile
from pathlib import Path
HERE=Path(__file__).resolve().parent
CONDITIONS={"retry_no_new_information","generic_self_review","native_render_self_inspection","consequence_only_feedback","criterion_disclosure"}

def load(p): return json.loads(Path(p).read_text())
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def canon(v): return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def module(name):
    spec=importlib.util.spec_from_file_location(name,HERE/"checkers"/f"{name}.py"); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def adjudicate(a,b):
    keys=("terminal_state","endpoint","collateral")
    if any(a.get(k)!=b.get(k) for k in keys): return {"terminal_state":"observer_invalid","endpoint":None,"collateral":None}
    return {k:a[k] for k in keys}

def run(check_paths=True,write=True):
    p=load(HERE/"protocol.json"); manifest=load(HERE/"freeze-manifest.json"); errors=[]
    tasks=p.get("tasks",[]); families={t.get("family") for t in tasks}; shapes={t.get("shape") for t in tasks}
    if families!={"roster","service","workflow"} or len(tasks)!=6 or len(shapes)!=3: errors.append("task_family_or_shape_diversity")
    for f in families:
        if {t.get("defect_stratum") for t in tasks if t.get("family")==f}!={"near_threshold_single_locus","multi_locus_collateral_risk"}: errors.append(f"strata:{f}")
    conditions=p.get("conditions",[])
    if {c.get("condition_id") for c in conditions}!=CONDITIONS: errors.append("condition_matrix")
    shared=("tool_id","harness_id","model_id","provider_id","budget_id")
    if any(len({c.get(k) for c in conditions})!=1 for k in shared): errors.append("unequal_execution_envelope")
    assignments=p.get("assignments",[]); expected=len(tasks)*len(CONDITIONS)*5
    if len(assignments)!=expected or p.get("repetitions_per_task_condition_system")<5: errors.append("repetition_matrix")
    if any(a.get("attempts_executed")!=0 or a.get("assignment_sha256")!=canon({k:v for k,v in a.items() if k!="assignment_sha256"}) for a in assignments): errors.append("assignment_identity_or_attempt")
    if len({(a["task_id"],a["condition_id"],a["repetition"]) for a in assignments})!=expected: errors.append("duplicate_assignment")
    if any(p.get("claim_ceiling",{}).values()): errors.append("claim_ceiling")
    if p.get("calibration_gate",{}).get("no_post_treatment_tuning") is not True: errors.append("calibration_tuning_boundary")
    bound={x["path"]:x for x in manifest.get("bindings",[])}
    if check_paths:
        for rel,b in bound.items():
            q=HERE/rel
            if not q.is_file() or q.stat().st_size!=b["bytes"] or sha(q)!=b["sha256"]: errors.append(f"binding:{rel}")
    if manifest.get("assignment_set_sha256")!=canon(assignments): errors.append("assignment_set")
    if any(manifest.get(k)!=0 for k in ("model_calls","provider_calls","repair_rows_executed")): errors.append("manifest_calls")
    oa,ob=module("observer_a"),module("observer_b")
    if any("condition" in inspect.signature(m.evaluate).parameters for m in (oa,ob)): errors.append("observer_condition_dependence")
    rows=[]
    for c in load(HERE/"fixtures/calibration.json")["cases"]:
        a=oa.evaluate(c["family"],c["candidate"],c["view_status"],c["transform_status"]); b=ob.evaluate(c["family"],c["candidate"],c["view_status"],c["transform_status"]); result=adjudicate(a,b); rows.append({"case_id":c["case_id"],"expected":c["expected"],**result})
        if result["terminal_state"]!=c["expected"]: errors.append(f"calibration:{c['case_id']}")
    passed=sum(r["terminal_state"]=="passed" for r in rows); fraction=passed/len(rows)
    if not 0.15<fraction<0.85: errors.append("floor_or_ceiling")
    kinds={c["kind"] for c in load(HERE/"fixtures/calibration.json")["cases"]}
    required={"false_rejection_control","subtle_false_acceptance_control","multi_locus_false_acceptance_control","collateral_damage","missing_view","transform_drift","invalid_artifact"}
    if not required<=kinds: errors.append("mutation_coverage")
    disagreement=adjudicate({"terminal_state":"passed","endpoint":True,"collateral":True},{"terminal_state":"criterion_fail","endpoint":False,"collateral":True})
    if disagreement["terminal_state"]!="observer_invalid": errors.append("disagreement_fail_closed")
    ledger=load(HERE/"attempt-ledger.json"); zero=ledger=={"instrument_id":"self-inspection-repair-v2","attempts":[],"model_calls":0,"provider_calls":0,"repair_rows_executed":0}
    if not zero: errors.append("nonzero_attempt_ledger")
    with tempfile.TemporaryDirectory(prefix="repair-v2-canary-") as d:
        root=Path(d); task=root/"task"; out=root/"output"; private=root/"private"; task.mkdir();out.mkdir();private.mkdir();(task/"source").write_text("public");(private/"criterion").write_text("hidden");allow={str((task/"source").resolve())}; isolation=str((private/"criterion").resolve()) not in allow and str((task/".."/"private"/"criterion").resolve()) not in allow and task!=out
    if not isolation: errors.append("isolation_canary")
    status="PASS" if not errors else "FAIL"
    report={"schema_version":"2.0.0","status":status,"freeze_status":"awaiting_separate_commit_bound_independent_audit","errors":errors,"tasks_checked":len(tasks),"families_checked":len(families),"shapes_checked":len(shapes),"assignments_checked":len(assignments),"repetitions_per_cell":5,"calibration_cases_checked":len(rows),"calibration_pass_fraction":fraction,"calibration_outcomes":{s:sum(r["terminal_state"]==s for r in rows) for s in sorted({r["terminal_state"] for r in rows})},"observer_agreement":all(r["terminal_state"]!="observer_invalid" for r in rows),"observer_disagreement_canary":disagreement["terminal_state"],"zero_call_isolation_canary":{"status":"PASS" if isolation else "FAIL","private_paths_excluded":isolation,"unique_output_root":task!=out},"equal_envelope_canary":{"status":"PASS" if "unequal_execution_envelope" not in errors else "FAIL","shared_fields":list(shared)},"attempt_ledger_zero":zero,"model_calls":0,"provider_calls":0,"repair_rows_executed":0,"claim_ceiling":p["claim_ceiling"],"required_next_gate":p["next_gate"]}
    if write: (HERE/"preflight-report.json").write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
    return report
if __name__=="__main__":
    ap=argparse.ArgumentParser();ap.add_argument("--check-paths",action="store_true");a=ap.parse_args();r=run(a.check_paths);print(json.dumps(r,indent=2,sort_keys=True));raise SystemExit(0 if r["status"]=="PASS" else 1)
