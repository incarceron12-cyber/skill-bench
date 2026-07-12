#!/usr/bin/env python3
"""Replay a frozen, oracle-separated evaluator audit over two work shapes."""
from __future__ import annotations
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent

def load(name): return json.loads((HERE/name).read_text())
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def native(case):
    # Deliberately narrow exact-target evaluator: a retained failure hypothesis.
    if case["observer_view"] == "missing": return "fail"
    return "pass" if case["observed_target"] == case["native_target"] and case["communication"] == "complete" else "fail"

def hybrid(case):
    # Factual gates cannot be overridden by qualitative communication judgment.
    if case["observer_view"] == "missing": return "abstain"
    if not case["state_safe"] or not case["consequence_complete"]: return "fail"
    if case["observed_target"] not in case["admissible_targets"]: return "fail"
    return "pass" if case["communication"] == "complete" else "fail"

def metrics(rows, evaluator):
    decided=[r for r in rows if r[evaluator] != "abstain"]
    tp=sum(r[evaluator]=="fail" and r["reference"]=="fail" for r in decided)
    fn=sum(r[evaluator]=="pass" and r["reference"]=="fail" for r in decided)
    tn=sum(r[evaluator]=="pass" and r["reference"]=="pass" for r in decided)
    fp=sum(r[evaluator]=="fail" and r["reference"]=="pass" for r in decided)
    return {"n":len(rows),"decided":len(decided),"abstentions":len(rows)-len(decided),
            "sensitivity": tp/(tp+fn) if tp+fn else None,
            "specificity": tn/(tn+fp) if tn+fp else None,"tp":tp,"fn":fn,"tn":tn,"fp":fp}

def replay(write=True):
    protocol=load("protocol.json"); cases=load("evaluator-inputs.json")["cases"]
    oracle={x["case_id"]:x for x in load("oracle-private.json")["adjudications"]}
    rows=[]
    for c in cases:
        ref=oracle[c["case_id"]]
        row={"case_id":c["case_id"],"work_shape":c["work_shape"],"failure_type":c["failure_type"],
             "reference":ref["verdict"],"native_deterministic":native(c),"hybrid_restricted":hybrid(c),
             "unrestricted_model_judge":"not_executed"}
        row["disagreement_loci"]=[k for k in ("native_deterministic","hybrid_restricted") if row[k]!=row["reference"]]
        rows.append(row)
    report={"schema_version":"0.1.0","status":"partial_prospective_audit",
      "frozen_hashes":{"protocol":sha(HERE/"protocol.json"),"evaluator_inputs":sha(HERE/"evaluator-inputs.json"),"reference_adjudication":sha(HERE/"oracle-private.json"),"audit_code":sha(HERE/"audit.py")},
      "model_condition":{"status":"not_executed","reason":"No pinned model-judge execution was performed in this bounded slice; abstaining prevents fabricated model evidence."},
      "rows":rows,"metrics":{"native_deterministic":metrics(rows,"native_deterministic"),"hybrid_restricted":metrics(rows,"hybrid_restricted")},
      "variance_source_limits":["Fixed synthetic traces only","Deterministic configurations have zero observed repeat variance by construction","No trajectory, model-judge, regenerated-rubric, expert-reference, or environment variance estimated"],
      "claim_ceiling":["exact_behavior_of_two_deterministic_evaluators_on_frozen_builder_authored_cases"],"excluded_claims":protocol["excluded_claims"]}
    if write: (HERE/"report.json").write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
    return report
if __name__=="__main__":
    r=replay(); print(json.dumps({"status":r["status"],"metrics":r["metrics"],"model":r["model_condition"]},indent=2))
