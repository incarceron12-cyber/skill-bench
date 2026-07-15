#!/usr/bin/env python3
"""Post-hoc replay of frozen evidence-access charges; does not alter grades."""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
SCENARIOS={p.stem:json.loads(p.read_text()) for p in (HERE/"instrument/scenarios").glob("*.json")}
BY_ID={value["scenario_id"]:value for value in SCENARIOS.values()}

def charge(attempt:dict)->float:
    costs={a["evidence_id"]:a["cost"] for a in BY_ID[attempt["scenario_id"]]["evidence_atoms"]}
    total=0.0
    for request in attempt["requests"]:
        parser=request["parser_interpretation"]
        total += costs[parser["mapped_evidence_ids"][0]] if parser["status"]=="matched" else 0.5
    return total

def build():
    protocol=json.loads((HERE/"protocol.json").read_text());rows=[]
    for declared in protocol["schedule"]["rows"]:
        path=HERE/"execution/attempts"/declared["attempt_id"]/"trial-report.json";attempt=json.loads(path.read_text())
        rows.append({"attempt_id":declared["attempt_id"],"scenario_id":declared["scenario_id"],"condition_id":declared["condition_id"],"repeat":declared["repeat"],"request_access_charge":charge(attempt),"remaining_budget":3-charge(attempt),"basis":"Frozen parser policy: matched atom cost; ambiguous/unmatched 0.5. Supplied conditions make no requests and charge zero."})
    return {"kind":"posthoc_frozen_charge_replay","changes_grades":False,"rows":rows}

if __name__=="__main__":
    value=build();out=HERE/"execution/posthoc-cost-audit.json";out.write_text(json.dumps(value,indent=2,sort_keys=True)+"\n");print(json.dumps({"rows":len(value["rows"]),"path":str(out.relative_to(ROOT))},indent=2))
