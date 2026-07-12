#!/usr/bin/env python3
"""Replay a frozen, oracle-separated evaluator audit over two work shapes."""
from __future__ import annotations
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent

def load(name): return json.loads((HERE/name).read_text())
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def native(case):
    if case["observer_view"] == "missing": return "fail"
    return "pass" if case["observed_target"] == case["native_target"] and case["communication"] == "complete" else "fail"

def hybrid(case):
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
            "sensitivity":tp/(tp+fn) if tp+fn else None,"specificity":tn/(tn+fp) if tn+fp else None,
            "tp":tp,"fn":fn,"tn":tn,"fp":fp}

def model_records():
    manifest=load("model-runs/manifest.json"); records=[]
    for name in manifest["records"]:
        record=load("model-runs/"+name)
        if not record["valid"]: raise ValueError(f"invalid model record: {name}")
        usage=load("model-runs/"+name.removesuffix(".json")+"-usage.json")
        records.append({"name":name,"condition_id":record["condition_id"],"repeat":record["repeat"],
          "verdicts":{x["case_id"]:x["verdict"] for x in record["result"]["verdicts"]},
          "rubric":record["result"]["rubric"],"raw_sha256":record["raw_sha256"],
          "usage":{"total_tokens":usage["total_tokens"],"api_calls":usage["api_calls"],"estimated_cost_usd":usage["estimated_cost_usd"]}})
    return manifest,records

def replay(write=True):
    protocol=load("protocol.json"); cases=load("evaluator-inputs.json")["cases"]
    oracle={x["case_id"]:x for x in load("oracle-private.json")["adjudications"]}
    model_manifest,model_runs=model_records(); rows=[]
    for c in cases:
        ref=oracle[c["case_id"]]
        row={"case_id":c["case_id"],"work_shape":c["work_shape"],"failure_type":c["failure_type"],
             "reference":ref["verdict"],"native_deterministic":native(c),"hybrid_restricted":hybrid(c),
             "model_judge_runs":{r["name"]:r["verdicts"][c["case_id"]] for r in model_runs}}
        row["disagreement_loci"]=[k for k in ("native_deterministic","hybrid_restricted") if row[k]!=row["reference"]]
        row["disagreement_loci"] += [name for name,v in row["model_judge_runs"].items() if v!=row["reference"]]
        rows.append(row)
    model_metrics={r["name"]:metrics([{**row,r["name"]:row["model_judge_runs"][r["name"]]} for row in rows],r["name"]) for r in model_runs}
    signatures=[[r["verdicts"][c["case_id"]] for c in cases] for r in model_runs]
    total_tokens=sum(r["usage"]["total_tokens"] for r in model_runs)
    report={"schema_version":"0.2.0","status":"fixed_trace_crossed_evaluator_audit",
      "frozen_hashes":{"protocol":sha(HERE/"protocol.json"),"evaluator_inputs":sha(HERE/"evaluator-inputs.json"),"reference_adjudication":sha(HERE/"oracle-private.json"),"audit_code":sha(HERE/"audit.py")},
      "model_condition":{"status":"executed","manifest_sha256":sha(HERE/"model-runs/manifest.json"),"protocol_sha256":model_manifest["protocol_sha256"],
        "runs":[{"name":r["name"],"condition_id":r["condition_id"],"repeat":r["repeat"],"rubric":r["rubric"],"raw_sha256":r["raw_sha256"],"usage":r["usage"]} for r in model_runs],
        "total_tokens":total_tokens,"predeclared_observation_ceiling":50000,"budget_violation":total_tokens>50000,
        "all_verdict_signatures_identical":len({tuple(v) for v in signatures})==1},
      "rows":rows,"metrics":{"native_deterministic":metrics(rows,"native_deterministic"),"hybrid_restricted":metrics(rows,"hybrid_restricted"),"model_runs":model_metrics},
      "variance_source_limits":["Fixed synthetic traces only","Two fixed-rubric and two regenerated-rubric model executions; four identical verdict vectors are an observation, not zero population variance","Rubric prose differed but criterion equivalence was not independently established","No trajectory, expert-reference, or environment variance estimated","Predeclared 50000-token observation ceiling was exceeded; retained as a protocol deviation"],
      "claim_ceiling":["exact_behavior_of_two_deterministic_evaluators_and_four_pinned_model_judge_calls_on_frozen_builder_authored_cases"],"excluded_claims":protocol["excluded_claims"]}
    if write: (HERE/"report.json").write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
    return report
if __name__=="__main__":
    r=replay(); print(json.dumps({"status":r["status"],"metrics":r["metrics"],"model":r["model_condition"]},indent=2))
