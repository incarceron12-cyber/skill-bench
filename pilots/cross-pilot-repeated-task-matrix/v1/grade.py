#!/usr/bin/env python3
"""Deterministic exact-field grader for the frozen repeated-task matrix."""
from __future__ import annotations
import argparse, json, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FORMS = [
    ROOT / "evidence-reconciliation/adoption",
    ROOT / "evidence-reconciliation/renewal",
    ROOT / "incident-state/vendor",
    ROOT / "incident-state/pipeline",
]

def grade(form: Path, output: Path) -> dict:
    key = json.loads((form / "answer-key.json").read_text())
    try:
        observed = json.loads(output.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        return {"classification":"invalid_artifact","error":str(exc),"criteria":[]}
    criteria = []
    expected = key["expected"]
    mapping = {
        "decision": [k for k in expected if k in {"decision","threshold_result","action","new_state"}],
        "action": [k for k in expected if k in {"action","new_state"}],
        "trusted-set": ["trusted_evidence_ids"],
        "rejected-set": ["rejected_evidence_ids"],
        "effective-status": ["effective_status_id"],
        "reconciliation": ["trusted_evidence_ids","rejected_evidence_ids"],
    }
    for criterion in key["criteria"]:
        fields = mapping[criterion["id"]]
        passed = bool(fields) and all(observed.get(f) == expected[f] for f in fields)
        criteria.append({"id":criterion["id"],"severity":criterion["severity"],"passed":passed,"fields":fields})
    failed = [c for c in criteria if not c["passed"]]
    return {"classification":"pass" if not failed else "fail","criteria":criteria,
            "failed_severity_counts":{s:sum(c["severity"]==s for c in failed) for s in ("critical","major","minor")}}

def self_test() -> None:
    for form in FORMS:
        key = json.loads((form / "answer-key.json").read_text())
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "decision.json"
            p.write_text(json.dumps({**key["expected"], "rationale":"builder-authored calibration"}))
            assert grade(form,p)["classification"] == "pass"
            for field, value in key["expected"].items():
                bad = {**key["expected"], "rationale":"mutation"}
                bad[field] = [] if isinstance(value,list) else "MUTATED"
                p.write_text(json.dumps(bad))
                assert grade(form,p)["classification"] == "fail", (form,field)
    print(json.dumps({"status":"PASS","forms":4,"test":"positive_and_all_expected_field_mutations"}))

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("--self-test",action="store_true"); ap.add_argument("--form"); ap.add_argument("--output")
    a=ap.parse_args()
    if a.self_test: self_test(); return 0
    if not a.form or not a.output: ap.error("--form and --output required")
    print(json.dumps(grade(ROOT / a.form, Path(a.output)), indent=2, sort_keys=True)); return 0
if __name__ == "__main__": raise SystemExit(main())
