#!/usr/bin/env python3
"""Fail-closed validator for the prospective repeated-task matrix protocol."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def sha(p:Path)->str: return hashlib.sha256(p.read_bytes()).hexdigest()
def validate(check_paths:bool=True)->list[str]:
    p=json.loads((ROOT/"protocol.json").read_text()); errors=[]
    forms=p.get("forms",[]); schedule=p.get("attempt_schedule",[])
    if len(forms)!=4 or len({x["family_id"] for x in forms})!=2: errors.append("need two families and four forms")
    if len(schedule)!=8 or len({x["attempt_id"] for x in schedule})!=8: errors.append("need eight unique attempts")
    for f in forms:
        rows=[x for x in schedule if x["form_id"]==f["form_id"]]
        if len(rows)!=2 or len({x["repeat_seed"] for x in rows})!=2: errors.append(f"{f['form_id']}: need two unique repeats")
        if f.get("provenance_status")!="builder_authored_hypothesis": errors.append(f"{f['form_id']}: provenance ceiling")
        if {c["severity"] for c in f.get("criteria",[])} != {"critical","major","minor"}: errors.append(f"{f['form_id']}: severity coverage")
        if f.get("task_health",{}).get("operational_role")!="calibration_only": errors.append(f"{f['form_id']}: task health role")
    if any(p.get("claim_boundaries",{}).values()): errors.append("claim upgrade")
    if p.get("confidence_channel",{}).get("absent_outcome")!="insufficient_evidence": errors.append("confidence must fail closed")
    if p.get("retry_policy")!="none; retain failures and unstarted rows; never replace or tune": errors.append("retry policy drift")
    if check_paths:
        for c in p.get("frozen_components",[]):
            path=ROOT/c["path"]
            if not path.is_file(): errors.append(f"missing {c['path']}")
            elif sha(path)!=c["sha256"]: errors.append(f"hash mismatch {c['path']}")
    return errors

def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument("--check-paths",action="store_true"); a=ap.parse_args(); e=validate(a.check_paths)
    print(json.dumps({"status":"PASS" if not e else "FAIL","errors":e},indent=2)); return 1 if e else 0
if __name__=="__main__": raise SystemExit(main())
