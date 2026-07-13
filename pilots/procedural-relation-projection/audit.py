#!/usr/bin/env python3
"""Replay frozen procedural-relation projection contrast families.

This zero-call audit validates builder-authored synthetic conformance records. It
is not evidence of expert authority, professional validity, agent capability,
safety, production fitness, or readiness.
"""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def load() -> dict[str, Any]:
    return json.loads((HERE / "suite.json").read_text(encoding="utf-8"))


def load_oracle() -> dict[str, Any]:
    return json.loads((HERE / "oracle-private.json").read_text(encoding="utf-8"))


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def predicate_holds(predicate: dict[str, Any], facts: dict[str, Any], events: dict[str, Any]) -> bool:
    values = facts if "fact" in predicate else events
    key = predicate.get("fact", predicate.get("event"))
    return key in values and values[key] == predicate["equals"]


def expression_holds(expression: dict[str, Any], facts: dict[str, Any], events: dict[str, Any]) -> bool:
    return all(predicate_holds(item, facts, events) for item in expression["all"])


def structural_findings(suite: dict[str, Any]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []

    def add(code: str, locus: str, detail: str) -> None:
        findings.append({"code": code, "failure_locus": locus, "detail": detail})

    if suite.get("status") != "frozen_builder_authored_relation_conformance_only":
        add("suite_not_frozen", "instrument_identity", "suite status is not frozen")
    if len({world["work_shape"] for world in suite["worlds"]}) < 2:
        add("work_shape_coverage", "instrument_coverage", "fewer than two work shapes")

    for record in suite["source_evidence"].values():
        path = ROOT / record["path"]
        if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != record["sha256"]:
            add("source_evidence_hash_mismatch", "source_authority", record["path"])

    worlds = {world["world_id"]: world for world in suite["worlds"]}
    for world in suite["worlds"]:
        clauses = {item["clause_id"]: item for item in world["clauses"]}
        declared_views = {item["view_id"] for item in world["artifact_views"]}
        manifest = world["task_projection_manifest"]
        if set(manifest["projection_kinds"]) != {"instruction", "source_environment", "witness", "check"} or not manifest["reciprocal_coverage"] or manifest["checker_only_obligations"]:
            add("projection_coverage_defect", "public_basis", world["world_id"])
        if set(manifest["requirements"]) != set(clauses):
            add("projection_requirement_drift", "source_normalization", world["world_id"])
        for clause in clauses.values():
            if clause["span"] != {"start": 0, "end": len(clause["text"])} or clause["sha256"] != sha256_text(clause["text"]):
                add("source_clause_hash_or_span_drift", "source_normalization", clause["clause_id"])
        for relation in world["relations"]:
            if not set(relation["clause_ids"]) <= set(clauses) or relation["governing_clause_id"] not in clauses:
                add("relation_clause_drift", "source_normalization", relation["relation_id"])
            if not relation["accepted_paths"]:
                add("accepted_path_inventory_empty", "accepted_path_coverage", relation["relation_id"])
            if any(item.startswith("private:") for item in relation["public_basis"]):
                add("private_oracle_in_public_basis", "public_basis", relation["relation_id"])
            missing_views = set(relation["observer"]["required_views"]) - declared_views
            if missing_views:
                add("observer_references_undeclared_view", "observer_sufficiency", f"{relation['relation_id']}:{sorted(missing_views)}")
            if relation["consequence_claim"].get("safety_claim"):
                add("unsupported_safety_consequence", "consequence_interpretation", relation["relation_id"])

    for case in suite["cases"]:
        world = worlds.get(case["world_id"])
        if world is None:
            add("unknown_case_world", "case_projection", case["case_id"])
            continue
        needed = {predicate["fact"] for relation in world["relations"] for predicate in relation["trigger"]["all"]}
        missing = needed - set(case["facts"])
        if missing:
            add("trigger_fact_unobserved", "case_applicability", f"{case['case_id']}:{sorted(missing)}")
    return findings


def evaluate_case(world: dict[str, Any], case: dict[str, Any]) -> dict[str, Any]:
    facts = case["facts"]
    events = {item["event"]: item["value"] for item in case["events"]}
    applicable = [relation for relation in world["relations"] if expression_holds(relation["trigger"], facts, events)]
    evidence = [{"event": item["event"], "value": item["value"]} for item in case["events"]]
    if not applicable:
        return {"relation_id": None, "verdict": "not_applicable", "failure_locus": None, "evidence_events": evidence, "mixed_evidence": False}
    max_priority = max(relation["priority"] for relation in applicable)
    governing = [relation for relation in applicable if relation["priority"] == max_priority]
    if len(governing) != 1:
        return {"relation_id": None, "verdict": "inconclusive", "failure_locus": "relation_priority", "evidence_events": evidence, "mixed_evidence": False}
    relation = governing[0]
    missing_views = [view for view in relation["observer"]["required_views"] if case["views"].get(view) != "available"]
    if missing_views:
        return {"relation_id": relation["relation_id"], "verdict": "inconclusive", "failure_locus": "observer_sufficiency", "missing_views": missing_views, "evidence_events": evidence, "mixed_evidence": False}
    violated = expression_holds(relation["violation"], facts, events)
    satisfied_paths = [path["path_id"] for path in relation["accepted_paths"] if expression_holds(path, facts, events)]
    repair_events = {"recall_completed", "label_repaired"}
    mixed = violated and any(events.get(event) is True for event in repair_events)
    if violated:
        verdict, locus = "relation_violated", "execution"
    elif satisfied_paths:
        verdict, locus = "relation_satisfied", None
    else:
        verdict, locus = "relation_violated", "execution"
    return {
        "relation_id": relation["relation_id"], "verdict": verdict, "failure_locus": locus,
        "accepted_path_ids": satisfied_paths, "evidence_events": evidence, "mixed_evidence": mixed,
        "consequence_claim": relation["consequence_claim"],
    }


def replay(suite: dict[str, Any] | None = None, oracle: dict[str, Any] | None = None, write: bool = True) -> dict[str, Any]:
    suite = copy.deepcopy(suite or load())
    oracle = copy.deepcopy(oracle or load_oracle())
    findings = structural_findings(suite)
    worlds = {world["world_id"]: world for world in suite["worlds"]}
    expected = {item["case_id"]: item for item in oracle["cases"]}
    rows = []
    for case in suite["cases"]:
        observed = evaluate_case(worlds[case["world_id"]], case)
        wanted = expected[case["case_id"]]
        rows.append({
            "case_id": case["case_id"], "world_id": case["world_id"], "work_shape": worlds[case["world_id"]]["work_shape"],
            **observed,
            "relation_selection_correct": observed["relation_id"] == wanted["relation_id"],
            "final_verdict_correct": observed["verdict"] == wanted["verdict"],
            "failure_locus_correct": observed["failure_locus"] == wanted["failure_locus"],
        })
    report = {
        "schema_version": "0.1.0", "status": "frozen_procedural_relation_projection_replay",
        "structural_findings": findings, "rows": rows,
        "summary": {
            "cases": len(rows), "work_shapes": sorted({row["work_shape"] for row in rows}),
            "relation_selection_errors": sum(not row["relation_selection_correct"] for row in rows),
            "final_verdict_errors": sum(not row["final_verdict_correct"] for row in rows),
            "failure_locus_errors": sum(not row["failure_locus_correct"] for row in rows),
            "inconclusive": sum(row["verdict"] == "inconclusive" for row in rows),
            "not_applicable": sum(row["verdict"] == "not_applicable" for row in rows),
            "mixed_evidence_retained": sum(row["mixed_evidence"] for row in rows),
        },
        "claim_ceiling": suite["claim_ceiling"], "excluded_claims": suite["excluded_claims"],
    }
    if write:
        (HERE / "report.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report


def mutate(suite: dict[str, Any], kind: str) -> dict[str, Any]:
    candidate = copy.deepcopy(suite)
    procurement, research = candidate["worlds"]
    if kind == "source_hash_drift":
        procurement["clauses"][0]["sha256"] = "0" * 64
    elif kind == "trigger_fact_missing":
        candidate["cases"][0]["facts"].pop("release_requested")
    elif kind == "priority_tie":
        procurement["relations"][0]["priority"] = procurement["relations"][1]["priority"]
        procurement["relations"][0]["trigger"]["all"][1]["equals"] = True
    elif kind == "hidden_public_basis":
        procurement["relations"][0]["public_basis"].append("private:oracle-verdict")
    elif kind == "accepted_path_removed":
        research["relations"][0]["accepted_paths"] = []
    elif kind == "observer_view_removed":
        research["artifact_views"] = [view for view in research["artifact_views"] if view["view_id"] != "memo-bytes"]
    elif kind == "consequence_overclaim":
        procurement["relations"][0]["consequence_claim"]["safety_claim"] = True
    else:
        raise ValueError(f"unknown mutation: {kind}")
    return candidate


def mutation_report(suite: dict[str, Any] | None = None, oracle: dict[str, Any] | None = None) -> list[dict[str, Any]]:
    suite, oracle = suite or load(), oracle or load_oracle()
    rows = []
    for kind, expected_locus in oracle["mutation_expectations"].items():
        candidate = mutate(suite, kind)
        findings = structural_findings(candidate)
        loci = sorted({item["failure_locus"] for item in findings})
        if kind == "priority_tie":
            world = candidate["worlds"][0]
            case = next(item for item in candidate["cases"] if item["case_id"] == "proc-override-hold")
            result = evaluate_case(world, case)
            loci = [result["failure_locus"]] if result["failure_locus"] else []
        rows.append({"mutation": kind, "expected_locus": expected_locus, "observed_loci": loci, "localized_exactly": loci == [expected_locus]})
    return rows


if __name__ == "__main__":
    print(json.dumps(replay(), indent=2, sort_keys=True))
