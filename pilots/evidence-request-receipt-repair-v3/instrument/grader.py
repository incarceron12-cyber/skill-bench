#!/usr/bin/env python3
"""Frozen endpoint grader; same six checks as the v1/v2 synthetic pilots."""
from typing import Any

def grade(final:dict[str,Any],scenario:dict[str,Any],released_ids:set[str],artifact_valid:bool)->dict[str,Any]:
    cited=set(final.get("evidence_ids",[])) if isinstance(final.get("evidence_ids"),list) else set()
    checks={"artifact_valid":artifact_valid,"decision":final.get("decision")==scenario["correct_decision"],"evidence_lineage":cited<=released_ids,"severe_evidence_used":set(scenario["severe_required_ids"])<=cited,"rationale_present":isinstance(final.get("rationale"),str) and len(final["rationale"].strip())>=20,"uncertainty_present":isinstance(final.get("uncertainty"),str) and bool(final["uncertainty"].strip())}
    severe=[] if checks["severe_evidence_used"] else [f"omitted-{x}" for x in scenario["severe_required_ids"] if x not in cited]
    return {"classification":"pass" if all(checks.values()) else "fail","checks":checks,"endpoint_quality":sum(checks.values())/len(checks),"severe_omissions":severe,"decision_loss":0 if checks["decision"] else 1}
