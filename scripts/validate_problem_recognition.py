#!/usr/bin/env python3
"""Validate and replay the internal problem-recognition intervention slice."""
import argparse, hashlib, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
STAGES = ["cue_extraction","problem_framing","targeted_inquiry","action_selection","artifact_state"]
REQUIRED_NONCLAIMS = {"expert validity","prevalence","agent capability","treatment effect","cross-domain generalization","professional competence","deployment readiness"}

def semantic_errors(p, check_paths=False):
    e=[]
    cond={x["id"]:x for x in p.get("conditions",[])}; scen={x["id"]:x for x in p.get("scenarios",[])}
    if set(cond)!={"situation_only","minimal_frame","fully_specified"}: e.append("exact matched condition set required")
    if p.get("stages") != STAGES: e.append("stages must remain separate and ordered")
    if not any(x.get("polarity")=="positive" for x in scen.values()) or not any(x.get("polarity")=="negative" for x in scen.values()): e.append("positive and negative near neighbors required")
    sets={x.get("neighbor_set") for x in scen.values()};
    for s in sets:
        if {x.get("polarity") for x in scen.values() if x.get("neighbor_set")==s}!={"positive","negative"}: e.append(f"near-neighbor set {s} lacks contrast")
    for c in cond.values():
        if set(c.get("disclosure",[])) & set(c.get("forbidden_disclosure",[])): e.append(f"condition {c['id']} leaks forbidden labels")
        if "expected_label" not in c.get("forbidden_disclosure",[]) or "rubric_terms" not in c.get("forbidden_disclosure",[]): e.append(f"condition {c['id']} permits label/template leakage")
    expected={(s,c) for s in scen for c in cond}; seen=set()
    for o in p.get("observations",[]):
        key=(o.get("scenario_id"),o.get("condition_id")); seen.add(key)
        if key[0] not in scen or key[1] not in cond: e.append(f"unknown observation key {key}"); continue
        vals=[o.get(x) for x in STAGES]
        if o.get("environment")=="invalid_environment":
            if any(v is not None for v in vals) or not o.get("invalid_reason"): e.append(f"invalid environment {key} must abstain with reason")
        elif any(type(v) is not bool for v in vals): e.append(f"valid observation {key} requires boolean stages")
        if o.get("artifact_state") and not (o.get("action_selection") and o.get("problem_framing")): e.append(f"action/artifact success without supported framing in {key}")
    if seen != expected: e.append("framed-condition drift: every scenario must have all matched conditions")
    policy=p.get("scoring_policy",{})
    if not policy.get("stage_scores_are_separate") or policy.get("recognition_gate")!=STAGES[:2] or policy.get("execution_gate")!=STAGES[2:]: e.append("cue/framing and execution stages must not be collapsed")
    unsupported=set(p.get("validity_record",{}).get("unsupported",[]))
    if not REQUIRED_NONCLAIMS <= unsupported: e.append("unsupported professional/cross-domain claims must remain explicit non-claims")
    if check_paths:
        for k in ("paper_pdf","release_manifest"):
            r=p.get("provenance",{}).get(k,{}); path=ROOT/r.get("path","")
            if not path.is_file(): e.append(f"missing provenance path: {r.get('path')}")
            if r.get("sha256") and path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest()!=r["sha256"]: e.append(f"hash mismatch: {r['path']}")
    return e

def replay(p):
    out=[]
    for o in p["observations"]:
        invalid=o["environment"]!="valid"
        out.append({"scenario_id":o["scenario_id"],"condition_id":o["condition_id"],"disposition":"invalid_environment" if invalid else "scored","recognition":None if invalid else all(o[x] for x in STAGES[:2]),"execution":None if invalid else all(o[x] for x in STAGES[2:]),"stage_scores":{x:o[x] for x in STAGES}})
    return out

def validate_file(path, check_paths=False):
    p=json.loads(Path(path).read_text()); errors=semantic_errors(p,check_paths)
    if errors: raise ValueError("\n".join(errors))
    return p

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("path"); ap.add_argument("--check-paths",action="store_true"); ap.add_argument("--report"); a=ap.parse_args()
    p=validate_file(a.path,a.check_paths); report={"package_id":p["package_id"],"cells":replay(p),"claim_scope":p["validity_record"]}
    text=json.dumps(report,indent=2)+"\n"
    if a.report: Path(a.report).write_text(text)
    print("VALID"); print(text,end="")
if __name__=="__main__": main()
