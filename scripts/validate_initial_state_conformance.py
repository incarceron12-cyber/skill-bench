#!/usr/bin/env python3
"""Validate and replay task-initial-state bypass conformance cases."""
import argparse, hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUTCOMES={"pass","fail_pre_satisfied","fail_stale_residual","fail_copied_witness","fail_missing_transition","invalid_environment"}
NONCLAIMS={"agent capability","occupational validity","professional quality","failure prevalence","cross-domain generalization","expert validity","deployment readiness"}

def classify(case, task):
    initial, final = case["initial_state"], case["final"]
    if not initial.get("environment_valid"):
        return "invalid_environment"
    if initial.get("output_present") or task["final_artifact"] in initial.get("inventory",{}):
        return "fail_stale_residual" if final.get("origin")=="stale_residual" else "fail_pre_satisfied"
    if final.get("origin")=="copied_reference" or "copy_reference" in case.get("events",[]):
        return "fail_copied_witness"
    if not final.get("artifact_present") or final.get("origin")!="task_created":
        return "fail_missing_transition"
    events=case.get("events",[])
    if not any(events==path for path in task["admissible_paths"]):
        return "fail_missing_transition"
    return "pass"

def semantic_errors(p, check_paths=False):
    e=[]; task=p.get("public_task",{}); cases=p.get("cases",[])
    required={"clean_start","task_created_output","verified_before_export","no_reference_copy"}
    if not required <= set(task.get("public_requirements",[])): e.append("transition and provenance checks require a fair public basis")
    paths=task.get("admissible_paths",[])
    if len(paths)<2 or not all(path and path[-1]=="export" and any("verify" in x for x in path) for path in paths): e.append("standard and verified alternative paths required")
    ids=[c.get("case_id") for c in cases]
    expected_ids={"valid-completion","pre-satisfied-outcome","stale-residual-artifact","copied-reference-witness","omitted-required-transition","legitimate-alternate-path","invalid-environment"}
    if set(ids)!=expected_ids or len(ids)!=len(set(ids)): e.append("exact seven unique planted cases required")
    for c in cases:
        if c.get("expected") not in OUTCOMES: e.append(f"unknown expected outcome: {c.get('case_id')}")
        if c.get("expected") != classify(c,task): e.append(f"replay mismatch: {c.get('case_id')}")
        init=c.get("initial_state",{})
        if not init.get("environment_valid") and not init.get("invalid_reason"): e.append(f"invalid environment lacks reason: {c.get('case_id')}")
        for path,digest in init.get("inventory",{}).items():
            if len(digest)!=64: e.append(f"unhashed initial inventory: {c.get('case_id')}:{path}")
    if not NONCLAIMS <= set(p.get("validity_record",{}).get("unsupported",[])): e.append("required non-claims missing")
    if task.get("invalid_environment_policy")!="exclude_not_fail": e.append("invalid environment must abstain, not become task failure")
    if check_paths:
        for r in p.get("provenance",{}).values():
            path=ROOT/r.get("path","")
            if not path.is_file(): e.append(f"missing provenance path: {r.get('path')}")
            elif r.get("sha256") and hashlib.sha256(path.read_bytes()).hexdigest()!=r["sha256"]: e.append(f"hash mismatch: {r['path']}")
    return e

def validate_file(path,check_paths=False):
    p=json.loads(Path(path).read_text()); e=semantic_errors(p,check_paths)
    if e: raise ValueError("\n".join(e))
    return p

def replay(p):
    return [{"case_id":c["case_id"],"observed":classify(c,p["public_task"]),"expected":c["expected"],"matched":classify(c,p["public_task"])==c["expected"]} for c in p["cases"]]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("path"); ap.add_argument("--check-paths",action="store_true"); ap.add_argument("--report"); a=ap.parse_args()
    p=validate_file(a.path,a.check_paths); report={"package_id":p["package_id"],"cases":replay(p),"summary":{"matched":len(p["cases"]),"total":len(p["cases"]),"claims":p["validity_record"]}}
    text=json.dumps(report,indent=2)+"\n"
    if a.report: Path(a.report).write_text(text)
    print("VALID"); print(text,end="")
if __name__=="__main__": main()
