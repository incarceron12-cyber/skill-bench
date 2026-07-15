#!/usr/bin/env python3
"""Hash-pinned root/surface audit of immutable v1 active attempts; never rescores v1."""
from __future__ import annotations
import hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
V1=ROOT/"pilots/evidence-acquisition-matched-agent-v1"
OUT=Path(__file__).resolve().parent/"v1-root-surface-audit.json"
def load(p): return json.loads(p.read_text())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,v): p.write_text(json.dumps(v,indent=2,sort_keys=True)+"\n")

def main():
    protocol=load(V1/"protocol.json"); rows=[]
    for scheduled in protocol["schedule"]["rows"]:
        if scheduled["condition_id"]!="active": continue
        aid=scheduled["attempt_id"]; base=V1/"execution/attempts"/aid; report=load(base/"trial-report.json")
        requests=[]
        for req in report["requests"]:
            linked=[e for e in report["access_events"] if e.get("request_id")==req["request_id"]]
            requests.append({
                "request_id":req["request_id"],"raw_request":req["raw_request"],"intent":req["intent"],
                "requested_scope":req["requested_scope"],"parser_interpretation":req["parser_interpretation"],
                "access_transitions":linked,
                "surface_failure": "parser_realization" if req["parser_interpretation"]["status"]!="matched" else ("access" if not any(e["status"]=="released" for e in linked) else "none")
            })
        cited=report["final"].get("evidence_ids",[])
        rows.append({
            "attempt_id":aid,"scenario_id":report["scenario_id"],"repeat":report["repeat"],
            "hashes":{"trial_report_sha256":sha(base/"trial-report.json"),"grade_sha256":sha(base/"grade.json"),
                      "turn_output_sha256":[{"path":p.relative_to(ROOT).as_posix(),"sha256":sha(p)} for p in sorted((base/"trial/outputs").glob("turn-*.json"))]},
            "requests":requests,"released_ids":report["released_ids"],
            "adoption_record":{"kind":"terminal_citation_proxy_only","cited_released_ids":sorted(set(cited)&set(report["released_ids"])),"not_identified":"belief uptake or counterfactual artifact change"},
            "stop":{"reason":report["final"].get("stop_reason"),"decision":report["final"].get("decision"),"uncertainty":report["final"].get("uncertainty")},
            "grade":report["grade"],
            "root_attribution":"unidentified: selected evidence need, free-text expression, and deterministic alias parser are not independently randomized"
        })
    out={"audit_id":"v1-active-root-surface-audit","immutable_source":{"protocol_path":V1.joinpath("protocol.json").relative_to(ROOT).as_posix(),"protocol_sha256":sha(V1/"protocol.json"),"study_report_sha256":sha(V1/"execution/study-report.json")},
         "active_attempts":rows,
         "unidentified_causal_attributions":["evidence-need selection versus request expression","request expression versus parser realization","released-content adoption versus terminal citation","interface effect versus repeat stochasticity","endpoint effect of inquiry versus supplied information","cross-shape or professional generality"],
         "claim_limits":["No v1 artifact was modified or rescored.","Surface parser failures do not establish an agent inquiry-selection failure.","Terminal evidence IDs are a citation proxy, not direct evidence of belief adoption."]}
    dump(OUT,out); print(json.dumps({"path":OUT.relative_to(ROOT).as_posix(),"active_attempts":len(rows),"requests":sum(len(x["requests"]) for x in rows),"sha256":sha(OUT)},indent=2))
if __name__=="__main__": main()
