#!/usr/bin/env python3
"""Validate plural judgments, reducibility diagnoses, and policy aggregation."""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
from typing import Any
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas/plural-judgment.schema.json"
REDUCIBILITY_GATES = {"evidence_sufficiency", "rubric_comprehension", "within_rater_repeat", "prospective_framework", "multiple_observers_per_framework", "held_out_framework_interaction", "alternate_context_or_rubric", "outcome_or_stakeholder_evidence"}

class ValidationFailure(Exception): pass

def semantic_errors(p: dict[str, Any]) -> list[str]:
    e: list[str] = []
    def index(items, key, label):
        out = {}
        for x in items:
            if x[key] in out: e.append(f"{label}: duplicate {key} {x[key]!r}")
            out[x[key]] = x
        return out
    frameworks=index(p["frameworks"],"framework_id","frameworks"); observers=index(p["observers"],"observer_id","observers")
    views=index(p["evidence_views"],"view_id","evidence views"); obs=index(p["observations"],"observation_id","observations")
    cases=index(p["disagreement_cases"],"case_id","cases")
    for o in observers.values():
        if o["framework_id"] not in frameworks: e.append(f"observer {o['observer_id']}: unknown framework")
        for other in o["independent_of"]:
            if other not in observers: e.append(f"observer {o['observer_id']}: unknown independence reference {other!r}")
            elif o["observer_id"] not in observers[other]["independent_of"]: e.append(f"observer {o['observer_id']}: independence with {other!r} is not reciprocal")
    for o in obs.values():
        owner=f"observation {o['observation_id']}"
        if o["observer_id"] not in observers or o["framework_id"] not in frameworks or o["view_id"] not in views: e.append(f"{owner}: unknown observer, framework, or view")
        elif observers[o["observer_id"]]["framework_id"] != o["framework_id"]: e.append(f"{owner}: framework differs from observer declaration")
        if o["repeat_of"] is not None:
            prior=obs.get(o["repeat_of"])
            if prior is None or prior["observer_id"] != o["observer_id"] or prior["case_id"] != o["case_id"]: e.append(f"{owner}: repeat must link same observer and case")
    for c in cases.values():
        selected=[obs.get(i) for i in c["observation_ids"]]
        if any(x is None for x in selected) or any(x and x["case_id"] != c["case_id"] for x in selected): e.append(f"case {c['case_id']}: observation references must exist and match case")
        if c["disposition"] == "irreducible_disagreement" and set(c["tested_reducibility"]) != REDUCIBILITY_GATES: e.append(f"case {c['case_id']}: irreducible_disagreement requires every reducibility gate")
        if c["disposition"] == "framework_stratified":
            declared={x["framework_id"] for x in selected if x and frameworks[x["framework_id"]]["declaration_status"]=="declared" and frameworks[x["framework_id"]]["declared_before_observation"]}
            if len(declared)<2 or "within_rater_repeat" not in c["tested_reducibility"] or "prospective_framework" not in c["tested_reducibility"]: e.append(f"case {c['case_id']}: framework stratification requires stable prospective competing frameworks")
    for a in p["aggregations"]:
        selected=[obs.get(i) for i in a["observation_ids"]]
        if a["case_id"] not in cases or any(x is None for x in selected): e.append(f"aggregation {a['aggregation_id']}: unknown case or observation")
        if set(a["weights"]) != {x["observer_id"] for x in selected if x}: e.append(f"aggregation {a['aggregation_id']}: weights must cover exactly contributing observers")
        elif abs(sum(a["weights"].values())-1)>1e-12: e.append(f"aggregation {a['aggregation_id']}: weights must sum to one")
        expected=sum(a["weights"][x["observer_id"]]*x["value"] for x in selected if x)
        if abs(expected-a["output"])>1e-12: e.append(f"aggregation {a['aggregation_id']}: output does not equal declared weighted rule")
        actual_endorsers={x["observer_id"] for x in selected if x and x["endorsed"] and x["value"]==a["output"]}
        if set(a["endorsed_by"]) != actual_endorsers: e.append(f"aggregation {a['aggregation_id']}: endorsed_by does not match observations")
        if not actual_endorsers and set(a["dissent_observation_ids"]) != set(a["observation_ids"]): e.append(f"aggregation {a['aggregation_id']}: unendorsed policy output must preserve every contributing observation as dissent")
    unsupported=" ".join(p["claim_limits"]["unsupported"]).lower()
    for phrase in ("professional validity","expert consensus","cross-domain generality","prevalence"):
        if phrase not in unsupported: e.append(f"claim_limits: must explicitly deny {phrase}")
    return e

def validate_file(path: Path) -> None:
    schema=json.loads(SCHEMA.read_text()); package=json.loads(path.read_text())
    errors=[f"{'.'.join(map(str,x.absolute_path)) or '<root>'}: {x.message}" for x in Draft202012Validator(schema).iter_errors(package)]
    if not errors: errors=semantic_errors(package)
    if errors: raise ValidationFailure("\n".join(f"- {x}" for x in errors))

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("packages",nargs="+",type=Path); args=ap.parse_args(); failed=False
    for path in args.packages:
        try: validate_file(path); print(f"VALID {path}")
        except (OSError,json.JSONDecodeError,ValidationFailure) as ex: failed=True; print(f"INVALID {path}\n{ex}",file=sys.stderr)
    return int(failed)
if __name__=="__main__": raise SystemExit(main())
