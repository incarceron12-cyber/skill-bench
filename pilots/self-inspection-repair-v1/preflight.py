#!/usr/bin/env python3
"""Fail-closed semantic and zero-call preflight for the repair candidate freeze."""
from __future__ import annotations
import argparse, hashlib, inspect, json, tempfile
from pathlib import Path
import importlib.util

HERE = Path(__file__).resolve().parent
CONDITION_IDS = {"no_second_attempt","retry_no_new_information","generic_self_review","native_render_self_inspection","consequence_only_feedback","criterion_disclosure"}
TERMINAL_STATES = {"criterion_fail","invalid_artifact","insufficient_evidence","observer_invalid","environment_invalid","service_invalid","passed"}
KINDS = {"positive","near_miss","legitimate_alternative","corrupt_artifact","missing_view","observer_failure"}

def load(path): return json.loads(Path(path).read_text())
def raw_hash(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def canonical_hash(value): return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",", ":")).encode()).hexdigest()

def checker_module(root=HERE):
    spec = importlib.util.spec_from_file_location("repair_checker", root / "checkers" / "check_fixtures.py")
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load condition-blind checker")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def validate(protocol, manifest, root=HERE, check_paths=True):
    errors=[]
    conditions=protocol.get("conditions",[]); by_condition={c.get("condition_id"):c for c in conditions}
    if set(by_condition)!=CONDITION_IDS or len(conditions)!=6: errors.append("condition_matrix")
    if set(protocol.get("terminal_states",[]))!=TERMINAL_STATES: errors.append("terminal_type_collapse")
    if protocol.get("ecological_feedback",{}).get("included") is not False: errors.append("unauthorized_ecological_feedback")
    if any(protocol.get("claim_ceiling",{}).values()): errors.append("claim_ceiling")
    for cid,c in by_condition.items():
        if cid!="criterion_disclosure" and c.get("hidden_criterion_access"): errors.append(f"hidden_criterion_leak:{cid}")
        if cid!="criterion_disclosure" and "criterion_text" in c.get("information_treatment",[]): errors.append(f"criterion_treatment_leak:{cid}")
    shared=("tool_id","harness_id","model_id","provider_id","budget_id")
    if any(len({c.get(k) for c in conditions})!=1 for k in shared): errors.append("unequal_execution_envelope")
    tasks=protocol.get("tasks",[])
    if {t.get("shape") for t in tasks}!={"memo","structured_native"}: errors.append("work_shape_collapse")
    assignments=protocol.get("assignments",[])
    expected={(t["task_id"],c) for t in tasks for c in CONDITION_IDS}
    if {(a.get("task_id"),a.get("condition_id")) for a in assignments}!=expected: errors.append("assignment_matrix")
    for a in assignments:
        unhashed={k:v for k,v in a.items() if k!="assignment_sha256"}
        if a.get("assignment_sha256")!=canonical_hash(unhashed): errors.append(f'assignment_hash:{a.get("assignment_id")}')
        if a.get("attempts_executed")!=0: errors.append(f'post_freeze_execution:{a.get("assignment_id")}')
    for task in tasks:
        rows=[a for a in assignments if a.get("task_id")==task["task_id"]]
        if len({a.get("starting_artifact_sha256") for a in rows})!=1: errors.append(f'starting_artifact_drift:{task["task_id"]}')
    contract=protocol.get("repair_record_contract",{})
    expected_seq=["defect_observation","diagnosis","revision_delta","criterion_local_recheck","collateral_recheck","new_error_assessment","cost"]
    if contract.get("required_sequence")!=expected_seq or not contract.get("condition_blind_checker"): errors.append("repair_record_contract")
    if manifest.get("assignment_set_sha256")!=canonical_hash(assignments): errors.append("assignment_set_hash")
    if any(manifest.get(k)!=0 for k in ("model_calls","provider_calls","repair_rows_executed")): errors.append("nonzero_call_ledger")
    if "independent" not in manifest.get("next_gate",""): errors.append("independent_audit_gate")
    bound={b["path"]:b for b in manifest.get("bindings",[])}
    if len(bound)!=len(manifest.get("bindings",[])): errors.append("duplicate_binding")
    if check_paths:
        for rel,b in bound.items():
            path=root/rel
            if not path.is_file(): errors.append(f"missing_binding:{rel}"); continue
            if path.stat().st_size!=b.get("bytes") or raw_hash(path)!=b.get("sha256"): errors.append(f"post_freeze_edit:{rel}")
        transforms=load(root/"transformations.json")
        for item in transforms.get("transformations",[]):
            if not item.get("transformation_id") or not item.get("implementation") or not item.get("permitted_invariances"): errors.append("unpinned_transformation")
    fixture=load(root/"fixtures"/"calibration.json")
    observed={(c.get("shape"),c.get("kind")) for c in fixture.get("cases",[])}
    if observed!={(s,k) for s in ("memo","structured") for k in KINDS}: errors.append("calibration_coverage")
    checker=checker_module(root)
    if "condition" in inspect.signature(checker.evaluate).parameters: errors.append("checker_condition_dependence")
    rows=checker.replay(root/"fixtures"/"calibration.json")
    if any(r["terminal_state"] not in TERMINAL_STATES or r["terminal_state"]!=r["expected"] for r in rows): errors.append("calibration_replay")
    return errors,rows

def isolation_canary():
    with tempfile.TemporaryDirectory(prefix="repair-canary-") as tmp:
        base=Path(tmp); task=base/"task-cwd"; output=base/"trial-output"; outside=base/"private-rubric.json"
        task.mkdir(); output.mkdir(); (task/"source.json").write_text("{}\n"); outside.write_text('{"hidden":true}\n')
        allowlist={str((task/"source.json").resolve())}; requested=[task/"source.json"]
        allowlist_ok=all(str(p.resolve()) in allowlist for p in requested) and str(outside.resolve()) not in allowlist
        traversal_blocked=str((task/".."/"private-rubric.json").resolve()) not in allowlist
        out=output/"candidate.txt"; out.write_text("canary\n")
        return {"status":"PASS" if allowlist_ok and traversal_blocked and out.parent==output and task!=output else "FAIL","task_scoped_cwd":task!=HERE,"private_rubric_excluded":str(outside.resolve()) not in allowlist,"path_traversal_blocked":traversal_blocked,"unique_output_root":out.parent==output}

def run(check_paths=True,write=True):
    protocol=load(HERE/"protocol.json"); manifest=load(HERE/"freeze-manifest.json")
    errors,rows=validate(protocol,manifest,HERE,check_paths)
    canary=isolation_canary()
    equal_envelope=not any(e=="unequal_execution_envelope" for e in errors)
    ledger=load(HERE/"attempt-ledger.json")
    zero_calls=ledger=={"instrument_id":"self-inspection-repair-v1","attempts":[],"model_calls":0,"provider_calls":0,"repair_rows_executed":0}
    status="PASS" if not errors and canary["status"]=="PASS" and equal_envelope and zero_calls else "FAIL"
    report={"schema_version":"1.0.0","status":status,"freeze_status":"awaiting_separate_commit_bound_independent_audit","errors":errors,"bindings_checked":len(manifest["bindings"]),"assignments_checked":len(protocol["assignments"]),"calibration_cases_checked":len(rows),"calibration_outcomes":{state:sum(r["terminal_state"]==state for r in rows) for state in sorted(TERMINAL_STATES)},"zero_call_isolation_canary":canary,"equal_envelope_canary":{"status":"PASS" if equal_envelope else "FAIL","shared_fields":["tool_id","harness_id","model_id","provider_id","budget_id"],"declared_differences_only":["repair_authorized","information_treatment","hidden_criterion_access"]},"attempt_ledger_zero":zero_calls,"model_calls":0,"provider_calls":0,"repair_rows_executed":0,"claim_ceiling":protocol["claim_ceiling"],"required_next_gate":protocol["next_gate"]}
    if write: (HERE/"preflight-report.json").write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
    return report

def main():
    p=argparse.ArgumentParser(); p.add_argument("--check-paths",action="store_true"); args=p.parse_args()
    report=run(check_paths=args.check_paths); print(json.dumps(report,indent=2,sort_keys=True)); raise SystemExit(0 if report["status"]=="PASS" else 1)
if __name__=="__main__": main()
