#!/usr/bin/env python3
"""Deterministic checker for frozen evidence-route packets.

The checker consumes cases and raw evidence only. Independent labels and their
rationales are loaded solely by replay() after every packet has been checked.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
FORBIDDEN_CHECKER_KEYS = {"expected", "oracle", "rationale", "planted_defect"}
RESULT_KEYS = (
    "structural_completeness",
    "route_coverage",
    "evidence_truth_sufficiency",
    "invalidity",
    "criterion_conclusion",
    "decision_eligibility",
)


def canonical_sha256(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def _contains_forbidden(value: Any) -> bool:
    if isinstance(value, dict):
        return bool(FORBIDDEN_CHECKER_KEYS & set(value)) or any(
            _contains_forbidden(item) for item in value.values()
        )
    if isinstance(value, list):
        return any(_contains_forbidden(item) for item in value)
    return False


def _structurally_complete(case: dict[str, Any]) -> bool:
    if not {"case_id", "shape_id", "environment", "actual_path", "interventions", "packet"} <= set(case):
        return False
    path = case["actual_path"]
    packet = case["packet"]
    if not {"attempts", "selected_route_id"} <= set(path) or not path["attempts"]:
        return False
    if not {"conclusion", "observations", "packet_check_results", "declared_contradictions", "declared_insufficiency"} <= set(packet):
        return False
    for attempt in path["attempts"]:
        if not {"route_id", "steps", "stop_reason"} <= set(attempt) or not attempt["steps"]:
            return False
        if any(not {"phase", "status"} <= set(step) for step in attempt["steps"]):
            return False
    required_observation = {"raw_locator", "raw_sha256", "transformed", "transformed_sha256"}
    return all(required_observation <= set(obs) for obs in packet["observations"])


def _safe_path(locator: str, root: Path) -> Path | None:
    try:
        candidate = (root / locator).resolve()
        candidate.relative_to(root.resolve())
    except (ValueError, OSError):
        return None
    return candidate


def _service_map(case: dict[str, Any]) -> dict[str, tuple[str, str]]:
    return {
        service["service_id"]: (service["version"], service["state"])
        for service in case["environment"]["services"]
    }


def _route_service(route: dict[str, Any]) -> tuple[str, str] | None:
    if len(route["prerequisites"]) != 1 or "@" not in route["prerequisites"][0]:
        return None
    return tuple(route["prerequisites"][0].rsplit("@", 1))  # type: ignore[return-value]


def check_case(case: dict[str, Any], contract: dict[str, Any], root: Path = REPO_ROOT) -> dict[str, Any]:
    """Check one packet without accepting labels, rationales, or oracle fields."""
    if _contains_forbidden(case) or _contains_forbidden(contract):
        raise ValueError("checker input contains forbidden oracle/rationale field")

    structural = _structurally_complete(case)
    base = {"case_id": case.get("case_id", "missing-id"), "structural_completeness": structural}
    if not structural:
        return {**base, "route_coverage": "incomplete", "evidence_truth_sufficiency": "invalid", "invalidity": "evidence_invalid", "criterion_conclusion": "invalid", "decision_eligibility": "abstain"}

    routes = {route["route_id"]: route for route in contract["routes"]}
    attempts = case["actual_path"]["attempts"]
    selected_id = case["actual_path"]["selected_route_id"]
    services = _service_map(case)

    all_unavailable = True
    for route in routes.values():
        identity = _route_service(route)
        if identity and services.get(identity[0]) == (identity[1], "available"):
            all_unavailable = False
    environment_invalid = all_unavailable and all(
        attempt["stop_reason"] == "service_unavailable" for attempt in attempts
    )

    route_complete = False
    selected_route = routes.get(selected_id) if selected_id is not None else None
    if selected_route is not None:
        selected_attempts = [a for a in attempts if a["route_id"] == selected_id]
        if len(selected_attempts) == 1:
            succeeded = {s["phase"] for s in selected_attempts[0]["steps"] if s["status"] == "succeeded"}
            route_complete = set(selected_route["required_phases"]) <= succeeded and selected_attempts[0]["stop_reason"] == "completed"
            identity = _route_service(selected_route)
            route_complete = bool(identity and services.get(identity[0]) == (identity[1], "available") and route_complete)
            if len(attempts) > 1:
                previous = routes.get(attempts[-2]["route_id"])
                route_complete = bool(
                    previous
                    and (selected_id in previous["backtracking_to"] or selected_route["bounded_substitute_for"] == previous["route_id"])
                    and route_complete
                )

    route_coverage = "invalid" if environment_invalid else "complete" if route_complete else "incomplete"

    intervention_invalid = False
    if selected_route is not None:
        permitted = set(selected_route["permitted_interventions"])
        intervention_invalid = any(
            item["route_id"] == selected_id and item["kind"] not in permitted
            for item in case["interventions"]
        )

    evidence_invalid = False
    values: list[str] = []
    route_identity = _route_service(selected_route) if selected_route else None
    for observation in case["packet"]["observations"]:
        path = _safe_path(observation["raw_locator"], root)
        if path is None or not path.is_file():
            evidence_invalid = True
            continue
        raw_bytes = path.read_bytes()
        if hashlib.sha256(raw_bytes).hexdigest() != observation["raw_sha256"]:
            evidence_invalid = True
            continue
        try:
            raw = json.loads(raw_bytes)
        except json.JSONDecodeError:
            evidence_invalid = True
            continue
        transformed = observation["transformed"]
        if canonical_sha256(transformed) != observation["transformed_sha256"]:
            evidence_invalid = True
        if transformed != {"claim_value": raw.get("claim_value")}:
            evidence_invalid = True
        if raw.get("artifact_id") != contract["artifact_id"] or raw.get("criterion_id") != contract["criterion_id"]:
            evidence_invalid = True
        if route_identity != (raw.get("service_id"), raw.get("service_version")):
            evidence_invalid = True
        values.append(str(raw.get("claim_value")))

    if intervention_invalid:
        truth = "invalid"
        invalidity = "intervention_invalid"
    elif evidence_invalid:
        truth = "invalid"
        invalidity = "evidence_invalid"
    elif not values:
        truth = "insufficient"
        invalidity = "environment_invalid" if environment_invalid else "none"
    elif len(set(values)) > 1 or case["packet"]["conclusion"] not in set(values):
        truth = "contradicted"
        invalidity = "none"
    elif values[0] != contract["expected_value"]:
        truth = "contradicted"
        invalidity = "none"
    else:
        truth = "supported"
        invalidity = "none"

    if environment_invalid:
        conclusion, decision = "invalid", "environment_invalid"
    elif truth == "supported" and route_coverage == "complete":
        conclusion, decision = "supported", "eligible"
    elif truth == "contradicted":
        conclusion, decision = "contradicted", "failed"
    elif truth == "insufficient" or route_coverage == "incomplete":
        conclusion, decision = "insufficient", "abstain"
    else:
        conclusion, decision = "invalid", "abstain"

    return {
        **base,
        "route_coverage": route_coverage,
        "evidence_truth_sufficiency": truth,
        "invalidity": invalidity,
        "criterion_conclusion": conclusion,
        "decision_eligibility": decision,
    }


def check_cases(data: dict[str, Any], root: Path = REPO_ROOT) -> list[dict[str, Any]]:
    if _contains_forbidden(data):
        raise ValueError("checker input contains forbidden oracle/rationale field")
    contracts = {item["shape_id"]: item for item in data["route_contracts"]}
    if len(contracts) < 2:
        raise ValueError("contrast set must span at least two retained work shapes")
    return [check_case(case, contracts[case["shape_id"]], root) for case in data["cases"]]


def replay(data: dict[str, Any], labels: dict[str, Any], root: Path = REPO_ROOT) -> dict[str, Any]:
    results = check_cases(data, root)
    expected = {item["case_id"]: item["expected"] for item in labels["labels"]}
    if set(expected) != {row["case_id"] for row in results}:
        raise ValueError("case/label identity mismatch")
    mismatches = []
    for row in results:
        observed = {key: row[key] for key in RESULT_KEYS}
        if observed != expected[row["case_id"]]:
            mismatches.append({"case_id": row["case_id"], "expected": expected[row["case_id"]], "observed": observed})
    if mismatches:
        raise ValueError(f"independent-label mismatch: {mismatches}")
    return {
        "version": data["version"],
        "status": "passed",
        "cases_replayed": len(results),
        "work_shapes": sorted({case["shape_id"] for case in data["cases"]}),
        "checker_oracle_access": false_value(),
        "claim_boundary": data["claim_boundary"],
        "results": results,
    }


def false_value() -> bool:
    """Named helper keeps the report assertion explicit and JSON-serializable."""
    return False


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("cases", type=Path)
    parser.add_argument("labels", type=Path)
    parser.add_argument("--root", type=Path, default=REPO_ROOT)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    report = replay(json.loads(args.cases.read_text()), json.loads(args.labels.read_text()), args.root)
    text = json.dumps(report, indent=2) + "\n"
    if args.report:
        args.report.write_text(text)
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
