#!/usr/bin/env python3
"""Post-hoc, no-rescore flow audit for retained v3 attempts."""
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent;EXEC=HERE/"execution"
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 protocol=load(HERE/"protocol.json");flows=[]
 for row in protocol["schedule"]["rows"]:
  path=EXEC/"attempts"/row["attempt_id"]/"trial-report.json";trial=load(path)
  eligible=all(trial[k] for k in ("service_valid","cost_valid","environment_valid","artifact_valid"))
  flows.append({**row,"eligible":eligible,"request":{"count":len(trial["requests"]),"statuses":[x["parser"]["status"] for x in trial["requests"]]},"receipt":{"count":len(trial["receipts"]),"records":trial["receipts"]},"repair":{"count":len(trial["repairs"]),"records":trial["repairs"]},"access":{"statuses":[x["status"] for x in trial["access_events"]],"released_ids":trial["released_ids"]},"adoption":trial["adoption"],"stop":{"decision":trial["final"].get("decision"),"reason":trial["final"].get("stop_reason"),"uncertainty":trial["final"].get("uncertainty")},"endpoint":{"classification":trial["grade"]["classification"],"quality":trial["grade"]["endpoint_quality"],"decision_loss":trial["grade"]["decision_loss"],"severe_omissions":trial["grade"]["severe_omissions"]},"cost":{"reported_usd":sum(x.get("estimated_cost_usd",0) or 0 for x in trial["usage"]),"total_tokens":sum(x.get("total_tokens",0) or 0 for x in trial["usage"])},"trial_report_sha256":sha(path)})
 pairs=[]
 for sid in ("vendor-disposition","segment-release"):
  for repeat in (1,2):
   n=next(x for x in flows if x["scenario_id"]==sid and x["condition_id"]=="natural_request" and x["repeat"]==repeat);r=next(x for x in flows if x["scenario_id"]==sid and x["condition_id"]=="receipt_repair" and x["repeat"]==repeat)
   pairs.append({"scenario_id":sid,"repeat":repeat,"eligible":n["eligible"] and r["eligible"],"natural_attempt_id":n["attempt_id"],"receipt_repair_attempt_id":r["attempt_id"],"observed":{"natural":{"requests":n["request"]["count"],"repairs":n["repair"]["count"],"released":len(n["access"]["released_ids"]),"endpoint_quality":n["endpoint"]["quality"],"tokens":n["cost"]["total_tokens"]},"receipt_repair":{"requests":r["request"]["count"],"repairs":r["repair"]["count"],"released":len(r["access"]["released_ids"]),"endpoint_quality":r["endpoint"]["quality"],"tokens":r["cost"]["total_tokens"]}}})
 result={"analysis_id":"evidence-request-receipt-repair-v3-flow-audit","protocol_sha256":sha(HERE/"protocol.json"),"study_report_sha256":sha(EXEC/"study-report.json"),"denominators":{"intended":8,"retained":len(flows),"eligible":sum(x["eligible"] for x in flows)},"attempt_flows":flows,"shape_specific_pairs":pairs,"no_shape_pooling":True,"no_rescoring":True,"reported_cost_usd":sum(x["cost"]["reported_usd"] for x in flows),"total_tokens":sum(x["cost"]["total_tokens"] for x in flows),"interpretation":"All eight attempts were valid. In vendor-disposition, both conditions routed two requests and passed. In segment-release, natural requests directly routed one adjusted-audit topic; receipt/repair requests first combined metric semantics with adjusted audit, received an ambiguous receipt, repaired to the audit, and still omitted the metric-dictionary requirement. Receipt/repair therefore exercised the intended transition but did not improve the six-check endpoint in these two repeats. Exact purposive observations only; no causal, inquiry-quality, capability, expert-validity, cross-domain, safety, production, or readiness claim."}
 (EXEC/"flow-audit.json").write_text(json.dumps(result,indent=2,sort_keys=True)+"\n");print(json.dumps({"eligible":result["denominators"]["eligible"],"pairs":len(pairs),"tokens":result["total_tokens"],"reported_cost_usd":result["reported_cost_usd"]},indent=2))
if __name__=="__main__":main()
