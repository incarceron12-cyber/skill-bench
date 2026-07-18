#!/usr/bin/env python3
"""Validate and replay the v0.2 staged-lineage conformance fixture."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
REQUIRED_UNSUPPORTED = {"agent capability", "professional validity", "cross-domain generalization", "deployment readiness"}
REQUIRED_SIGNATURES = {
    "duplicate_reports_treated_as_independent",
    "verbatim_number_bound_to_wrong_group_or_time",
    "offsetting_extraction_errors",
}


def file_sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def diagnose(item: dict[str, Any], stage_order: list[str]) -> dict[str, Any]:
    chain = item["chain"]
    failed = [node["stage"] for node in chain if node["admissibility"] == "failed"]
    earliest = min(failed, key=stage_order.index) if failed else None
    protocol = item["protocol_difference"]
    authorized = protocol["present"] and protocol["authorized"] and bool(protocol["authority_locator"])
    if failed:
        disposition = "blocked_by_stage_failure"
        accepted = False
    elif protocol["present"]:
        disposition = "authorized_protocol_difference" if authorized else "unauthorized_protocol_difference"
        accepted = authorized
    else:
        disposition = "chain_valid"
        accepted = True
    endpoint = item["endpoint"]
    return {
        "case_id": item["case_id"],
        "shape_id": item["shape_id"],
        "earliest_consequential_break": earliest,
        "stage_chain_accepted": accepted,
        "disposition": disposition,
        "endpoint_within_tolerance": endpoint["within_tolerance"],
        "decision_agreement": endpoint["decision_agreement"],
        "endpoint_cannot_compensate": bool(failed and endpoint["within_tolerance"] and not accepted),
    }


def semantic_errors(data: dict[str, Any], root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    if data.get("version") != "2.0.0":
        errors.append("fixture version must remain 2.0.0")
    for key in ("immutable_parent", "design_basis"):
        record = data.get(key, {})
        path_key = "path" if key == "immutable_parent" else "review_path"
        candidate = root / record.get(path_key, "")
        if not candidate.is_file() or file_sha(candidate) != record.get("sha256" if key == "immutable_parent" else "review_sha256"):
            errors.append(f"{key} path/hash mismatch")
    stages = data.get("stage_order", [])
    if stages != ["protocol", "search", "screen", "study_map", "extract", "transform", "analyze", "report"]:
        errors.append("stage order drift")
    unsupported = set(data.get("claim_boundary", {}).get("unsupported", []))
    if not REQUIRED_UNSUPPORTED <= unsupported:
        errors.append("claim ceiling upgrade")
    cases = data.get("cases", [])
    if len({c.get("shape_id") for c in cases}) < 2:
        errors.append("at least two unlike synthesis shapes required")
    if len(cases) != 10:
        errors.append("frozen matrix must contain exactly ten cases")
    signatures: set[str] = set()
    compensating_count = 0
    authorized_count = 0
    seen_case_ids: set[str] = set()
    for item in cases:
        cid = item.get("case_id", "missing")
        if cid in seen_case_ids:
            errors.append(f"{cid}: duplicate case id")
        seen_case_ids.add(cid)
        chain = item.get("chain", [])
        if [node.get("stage") for node in chain] != stages:
            errors.append(f"{cid}: incomplete or reordered stage chain")
            continue
        artifact_stage: dict[str, str] = {}
        previous_id = None
        for index, node in enumerate(chain):
            artifact_id = node.get("artifact_id")
            if not artifact_id or artifact_id in artifact_stage:
                errors.append(f"{cid}: duplicate or absent artifact id")
            expected_inputs = [] if index == 0 else [previous_id]
            if node.get("input_artifact_ids") != expected_inputs:
                errors.append(f"{cid}/{node.get('stage')}: cross-stage conservation failure")
            if index and any(ref not in artifact_stage for ref in node.get("input_artifact_ids", [])):
                errors.append(f"{cid}/{node.get('stage')}: dangling lineage reference")
            if not node.get("evidence_locators"):
                errors.append(f"{cid}/{node.get('stage')}: missing evidence locator")
            state = node.get("admissibility")
            if state not in {"passed", "authorized_divergence", "failed"}:
                errors.append(f"{cid}/{node.get('stage')}: invalid admissibility state")
            signature = node.get("failure_signature")
            if state == "failed" and not signature:
                errors.append(f"{cid}/{node.get('stage')}: failed stage lacks failure signature")
            if state != "failed" and signature is not None:
                errors.append(f"{cid}/{node.get('stage')}: nonfailed stage carries failure signature")
            if signature:
                signatures.add(signature)
            artifact_stage[artifact_id] = node.get("stage")
            previous_id = artifact_id
        endpoint = item.get("endpoint", {})
        distance = round(abs(endpoint.get("candidate", 0) - endpoint.get("reference", 0)), 6)
        if endpoint.get("absolute_distance") != distance or endpoint.get("within_tolerance") != (distance <= endpoint.get("tolerance", -1)):
            errors.append(f"{cid}: endpoint arithmetic mismatch")
        if endpoint.get("decision_agreement") != (endpoint.get("candidate_decision") == endpoint.get("reference_decision")):
            errors.append(f"{cid}: decision agreement mismatch")
        protocol = item.get("protocol_difference", {})
        protocol_state = chain[0].get("admissibility")
        if protocol.get("present") != (protocol_state == "authorized_divergence"):
            errors.append(f"{cid}: protocol-difference state mismatch")
        if protocol_state == "authorized_divergence" and not (protocol.get("authorized") and protocol.get("authority_locator")):
            errors.append(f"{cid}: unauthorized protocol difference cannot be promoted")
        observed = diagnose(item, stages)
        expected = item.get("expected", {})
        for key in ("earliest_consequential_break", "stage_chain_accepted", "disposition"):
            if observed[key] != expected.get(key):
                errors.append(f"{cid}: expected {key} does not match replay")
        if observed["endpoint_cannot_compensate"]:
            compensating_count += 1
        if observed["disposition"] == "authorized_protocol_difference":
            authorized_count += 1
    if not REQUIRED_SIGNATURES <= signatures:
        errors.append("required planted failure signatures absent")
    if compensating_count < 4:
        errors.append("close endpoints do not exercise enough noncompensatory failures")
    if authorized_count != 2:
        errors.append("authorized protocol-difference controls incomplete")
    return errors


def replay(data: dict[str, Any], root: Path = ROOT) -> dict[str, Any]:
    errors = semantic_errors(data, root)
    if errors:
        raise ValueError("; ".join(errors))
    results = [diagnose(item, data["stage_order"]) for item in data["cases"]]
    return {
        "version": data["version"],
        "status": "passed",
        "case_count": len(results),
        "shape_count": len({row["shape_id"] for row in results}),
        "accepted_chains": sum(row["stage_chain_accepted"] for row in results),
        "blocked_chains": sum(not row["stage_chain_accepted"] for row in results),
        "close_endpoint_blocked_chains": sum(row["endpoint_cannot_compensate"] for row in results),
        "authorized_protocol_differences": sum(row["disposition"] == "authorized_protocol_difference" for row in results),
        "claim_boundary": data["claim_boundary"],
        "results": results,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("fixture", type=Path)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    report = replay(json.loads(args.fixture.read_text()), args.root)
    rendered = json.dumps(report, indent=2) + "\n"
    if args.report:
        args.report.write_text(rendered)
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
