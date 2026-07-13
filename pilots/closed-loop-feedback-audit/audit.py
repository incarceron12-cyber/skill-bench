#!/usr/bin/env python3
"""Replay the frozen synthetic closed-loop feedback information-boundary audit."""
from __future__ import annotations
import copy, hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONDITIONS = ("no-feedback", "generic-nudge", "visible-only", "hidden-coarse")
CLASSIFICATIONS = {"public-entailed", "independently-visible", "private-signal-inferred", "hidden-equivalent", "new-authority-preference", "non-informative"}
REQUIRED_ROLES = ("executor", "supervisor", "simulator", "rewriter", "observer", "task", "environment")

def load(name: str): return json.loads((HERE / name).read_text())
def digest(value) -> str: return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
def proposition(case, condition):
    if condition == "no-feedback": return []
    if condition == "generic-nudge": return [{"text":"Please review the result and correct any issue you can independently identify.","source":"generic"}]
    if condition == "visible-only":
        return ([{"text":case["public_feedback"],"source":"public-observer"}] if case["defect_visibility"] == "public-visible" else
                [{"text":"Please verify the result against the public request.","source":"public-observer"}])
    return ([{"text":case["hidden_feedback"],"source":"private-derived-status"}] if case["defect_visibility"] == "hidden-only" else
            [{"text":"A private check reports a problem; inspect the visible result.","source":"private-derived-status"}])

def execute(case, condition, props):
    first = case["initial_outcome"]
    if first == "pass":
        changed = condition == "hidden-coarse" and bool(props)
        return {"repair_uptake":changed,"repair_correct":False,"new_error":changed,"final_outcome":"fail" if changed else "pass"}
    informative = condition == "visible-only" and case["defect_visibility"] == "public-visible"
    informative |= condition == "hidden-coarse" and case["defect_visibility"] == "hidden-only"
    return {"repair_uptake":bool(informative),"repair_correct":bool(informative),"new_error":False,"final_outcome":"pass" if informative else "fail"}

def validate(protocol):
    cases, configs = protocol["cases"], protocol["configurations"]
    if set(configs) != set(REQUIRED_ROLES): raise ValueError("all independently hashed roles are required")
    if any(configs[r]["sha256"] != digest(configs[r]["frozen_value"]) for r in REQUIRED_ROLES): raise ValueError("configuration hash mismatch")
    if len({c["work_shape"] for c in cases}) < 2: raise ValueError("two work shapes required")
    for shape in {c["work_shape"] for c in cases}:
        vis={c["defect_visibility"] for c in cases if c["work_shape"] == shape}
        if vis != {"public-visible", "hidden-only", "no-action-control"}: raise ValueError("each shape needs matched visible, hidden, and control cases")
    if any(c["observer_view"] != "complete-public-view" for c in cases): raise ValueError("missing observer view")
    if any(c["condition_inputs"] != protocol["frozen_executor_inputs"] for c in cases): raise ValueError("condition contamination")

def replay(protocol=None, write=True):
    protocol = copy.deepcopy(protocol or load("protocol.json")); validate(protocol)
    rows=[]
    for case in protocol["cases"]:
        for condition in CONDITIONS:
            props=proposition(case,condition); result=execute(case,condition,props)
            labels=[]
            for prop in props:
                expected = ("non-informative" if condition in {"generic-nudge","visible-only"} and case["defect_visibility"] != "public-visible" else
                            "independently-visible" if condition == "visible-only" else
                            "hidden-equivalent" if condition == "hidden-coarse" and case["defect_visibility"] == "hidden-only" else
                            "private-signal-inferred" if condition == "hidden-coarse" else "non-informative")
                coder_b = "private-signal-inferred" if expected == "hidden-equivalent" else expected
                labels.append({"proposition":prop["text"],"source":prop["source"],"coder_labels":[{"coder_id":"blind-coder-a","label":expected},{"coder_id":"blind-coder-b","label":coder_b}],"agreement":expected==coder_b})
            rows.append({"case_id":case["case_id"],"work_shape":case["work_shape"],"defect_visibility":case["defect_visibility"],"condition":condition,"first_attempt_outcome":case["initial_outcome"],"recoverable":case["recoverable"],"released_signal":{"condition":condition,"private_derived":condition=="hidden-coarse"},"feedback_propositions":labels,**result,"cost":{"calls":0,"usd":0.0}})
    leaked=sum(any(x["label"] in {"hidden-equivalent","private-signal-inferred"} for x in r["feedback_propositions"] for x in x["coder_labels"]) for r in rows)
    unsupported=sum(any(x["label"]=="new-authority-preference" for x in r["feedback_propositions"] for x in x["coder_labels"]) for r in rows)
    report={"schema_version":"0.1.0","status":"frozen_synthetic_feedback_boundary_audit","frozen_hashes":{"protocol":digest(protocol),**{r:protocol["configurations"][r]["sha256"] for r in REQUIRED_ROLES}},"rows":rows,"metrics":{"trials":len(rows),"repair_uptake":sum(r["repair_uptake"] for r in rows),"correct_repairs":sum(r["repair_correct"] for r in rows),"new_errors":sum(r["new_error"] for r in rows),"final_passes":sum(r["final_outcome"]=="pass" for r in rows),"leakage_rate":leaked/len(rows),"unsupported_authority_rate":unsupported/len(rows),"abstentions":0},"variance_limits":["Two builder-authored work shapes and six frozen cases","One deterministic replay per case-condition cell; no executor, simulator, coder, task, or environment variance estimated","Coder disagreement is retained and not adjudicated","Zero-call synthetic execution measures contract behavior only"],"claim_ceiling":["exact deterministic behavior of this frozen 24-cell synthetic audit"],"excluded_claims":protocol["excluded_claims"]}
    if write: (HERE/"report.json").write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
    return report
if __name__ == "__main__": print(json.dumps(replay(),indent=2))
