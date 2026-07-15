#!/usr/bin/env python3
"""Deterministic fail-closed grader for the frozen internal matrix."""
from __future__ import annotations
import json
from pathlib import Path

def grade(output: Path, expected: dict) -> dict:
    observations=[]
    try:
        value=json.loads(output.read_text(encoding="utf-8"))
        valid=isinstance(value,dict) and set(value)=={"decision","action","evidence_ids","rationale"} and isinstance(value.get("evidence_ids"),list) and isinstance(value.get("rationale"),str)
    except (OSError,json.JSONDecodeError):
        value={}; valid=False
    checks=[
      ("artifact_valid","critical",valid,"report parses with the exact disclosed keys"),
      ("decision","critical",valid and value.get("decision")==expected["decision"],"decision matches pinned authoritative consequence"),
      ("action",expected["severity"],valid and value.get("action")==expected["action"],"action matches pinned bounded response"),
      ("evidence","major",valid and value.get("evidence_ids")==expected["evidence_ids"],"evidence IDs contain only the current authoritative record"),
      ("conflict_rationale","minor",valid and any(w in value.get("rationale","").lower() for w in ("supersed","untrusted","authority","informal")),"rationale explains exclusion by authority or supersession"),
    ]
    for cid,severity,passed,reason in checks:
        observations.append({"criterion_id":cid,"severity":severity,"passed":bool(passed),"reason":reason})
    critical_fail=any(not x["passed"] and x["severity"]=="critical" for x in observations)
    return {"classification":"pass" if all(x["passed"] for x in observations) else "fail","critical_failure":critical_fail,"passed_criteria":sum(x["passed"] for x in observations),"total_criteria":len(observations),"observations":observations}

def main():
    import argparse
    p=argparse.ArgumentParser(); p.add_argument("output"); p.add_argument("expected"); a=p.parse_args()
    print(json.dumps(grade(Path(a.output),json.loads(Path(a.expected).read_text())),indent=2,sort_keys=True))
if __name__=="__main__": main()
