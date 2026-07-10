#!/usr/bin/env python3
"""Validate expertise-to-evaluation authoring packets.

JSON Schema checks record shape. Semantic checks enforce the evidence crosswalk,
anti-surprise-check policy, reciprocal mappings, and ordered authoring gates.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Iterable

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = ROOT / "schemas" / "expertise-transfer.schema.json"
STAGES = [
    "elicitation",
    "primitive_mapping",
    "scenario_design",
    "source_pack",
    "rubric",
    "pilot_validation",
    "release_review",
]


class ValidationFailure(Exception):
    """Raised when an authoring packet fails structural or semantic validation."""


def _duplicates(values: Iterable[str]) -> set[str]:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for value in values:
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    return duplicates


def _check_unique(items: list[dict[str, Any]], key: str, location: str, errors: list[str]) -> None:
    for duplicate in sorted(_duplicates(item[key] for item in items)):
        errors.append(f"{location}: duplicate {key} {duplicate!r}")


def _check_refs(owner: str, values: Iterable[str], valid: set[str], label: str, errors: list[str]) -> None:
    for value in values:
        if value not in valid:
            errors.append(f"{owner}: unknown {label} {value!r}")


def semantic_errors(packet: dict[str, Any]) -> list[str]:
    """Return cross-reference, fairness, and stage-gate violations."""
    errors: list[str] = []
    collections = [
        (packet["contributors"], "contributor_id", "contributors"),
        (packet["claims"], "claim_id", "claims"),
        (packet["primitives"], "primitive_id", "primitives"),
        (packet["scenarios"], "scenario_id", "scenarios"),
        (packet["sources"], "source_id", "sources"),
        (packet["traps"], "trap_id", "traps"),
        (packet["artifact_contracts"], "artifact_id", "artifact_contracts"),
        (packet["checks"], "check_id", "checks"),
        (packet["quality_gates"], "stage", "quality_gates"),
    ]
    for items, key, location in collections:
        _check_unique(items, key, location, errors)

    contributor_ids = {item["contributor_id"] for item in packet["contributors"]}
    claim_ids = {item["claim_id"] for item in packet["claims"]}
    primitive_ids = {item["primitive_id"] for item in packet["primitives"]}
    scenario_ids = {item["scenario_id"] for item in packet["scenarios"]}
    source_ids = {item["source_id"] for item in packet["sources"]}
    trap_ids = {item["trap_id"] for item in packet["traps"]}
    artifact_ids = {item["artifact_id"] for item in packet["artifact_contracts"]}
    check_ids = {item["check_id"] for item in packet["checks"]}
    primitive_by_id = {item["primitive_id"]: item for item in packet["primitives"]}
    scenario_by_id = {item["scenario_id"]: item for item in packet["scenarios"]}
    check_by_id = {item["check_id"]: item for item in packet["checks"]}

    for claim in packet["claims"]:
        _check_refs(f"claim {claim['claim_id']}", [claim["contributor_id"]], contributor_ids, "contributor_id", errors)

    for primitive in packet["primitives"]:
        owner = f"primitive {primitive['primitive_id']}"
        _check_refs(owner, primitive["claim_ids"], claim_ids, "claim_id", errors)
        _check_refs(owner, primitive["scenario_ids"], scenario_ids, "scenario_id", errors)
        _check_refs(owner, primitive["check_ids"], check_ids, "check_id", errors)
        for scenario_id in primitive["scenario_ids"]:
            scenario = scenario_by_id.get(scenario_id)
            if scenario and primitive["primitive_id"] not in scenario["primitive_ids"]:
                errors.append(f"{owner}: scenario {scenario_id!r} does not map back to primitive")
        for check_id in primitive["check_ids"]:
            check = check_by_id.get(check_id)
            if check and primitive["primitive_id"] not in check["primitive_ids"]:
                errors.append(f"{owner}: check {check_id!r} does not map back to primitive")

    for scenario in packet["scenarios"]:
        owner = f"scenario {scenario['scenario_id']}"
        _check_refs(owner, scenario["primitive_ids"], primitive_ids, "primitive_id", errors)
        _check_refs(owner, scenario["source_ids"], source_ids, "source_id", errors)
        _check_refs(owner, scenario["trap_ids"], trap_ids, "trap_id", errors)
        _check_refs(owner, scenario["artifact_ids"], artifact_ids, "artifact_id", errors)

    for trap in packet["traps"]:
        owner = f"trap {trap['trap_id']}"
        _check_refs(owner, trap["primitive_ids"], primitive_ids, "primitive_id", errors)
        _check_refs(owner, trap["source_ids"], source_ids, "source_id", errors)

    for check in packet["checks"]:
        owner = f"check {check['check_id']}"
        _check_refs(owner, check["primitive_ids"], primitive_ids, "primitive_id", errors)
        _check_refs(owner, check["public_basis_primitive_ids"], primitive_ids, "public basis primitive_id", errors)
        _check_refs(owner, check["artifact_ids"], artifact_ids, "artifact_id", errors)
        if check["visibility"] in {"private", "hidden"}:
            if not check["public_basis_primitive_ids"]:
                errors.append(f"{owner}: private/hidden check must name a public basis; hidden obligations are forbidden")
            for basis_id in check["public_basis_primitive_ids"]:
                basis = primitive_by_id.get(basis_id)
                if basis and basis["visibility"] != "public":
                    errors.append(f"{owner}: public basis primitive {basis_id!r} is not public")
            if check["disclosure_basis"] not in {"public_principle_consequence", "safety_necessity", "internal_calibration_only"}:
                errors.append(f"{owner}: private/hidden check has invalid disclosure_basis")

    gates = {gate["stage"]: gate for gate in packet["quality_gates"]}
    missing_stages = set(STAGES) - set(gates)
    if missing_stages:
        errors.append(f"quality_gates: missing stages {sorted(missing_stages)}")
    current_index = STAGES.index(packet["current_stage"])
    for stage in STAGES[:current_index]:
        gate = gates.get(stage)
        if gate and gate["status"] != "passed":
            errors.append(f"quality_gates: stage {stage!r} must pass before current_stage {packet['current_stage']!r}")
    for stage, gate in gates.items():
        if gate["status"] == "passed" and not gate["evidence_paths"]:
            errors.append(f"quality_gates: passed stage {stage!r} requires evidence_paths")

    release = packet["release"]
    if release["status"] == "releasable":
        if any(gates.get(stage, {}).get("status") != "passed" for stage in STAGES):
            errors.append("release: releasable packet requires every quality gate to pass")
        if release["leakage_review"] != "passed" or release["expert_validity_review"] != "passed":
            errors.append("release: releasable packet requires passed leakage and expert-validity reviews")

    return errors


def _declared_paths(packet: dict[str, Any]) -> Iterable[str]:
    for source in packet["sources"]:
        yield source["path"]
    for gate in packet["quality_gates"]:
        yield from gate["evidence_paths"]

    def provenance_paths(value: Any) -> Iterable[str]:
        if isinstance(value, dict):
            if "locator" in value and "description" in value and "local_path" in value:
                yield value["local_path"]
            for child in value.values():
                yield from provenance_paths(child)
        elif isinstance(value, list):
            for child in value:
                yield from provenance_paths(child)

    yield from provenance_paths(packet)


def validate_file(packet_path: Path, schema_path: Path = DEFAULT_SCHEMA, check_paths: bool = False) -> None:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    packet = json.loads(packet_path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = [
        f"{'.'.join(str(part) for part in error.absolute_path) or '<root>'}: {error.message}"
        for error in sorted(validator.iter_errors(packet), key=lambda item: list(item.absolute_path))
    ]
    if not errors:
        errors.extend(semantic_errors(packet))
    if check_paths:
        for path in sorted(set(_declared_paths(packet))):
            if not (ROOT / path).is_file():
                errors.append(f"declared repository path does not exist: {path}")
    if errors:
        raise ValidationFailure("\n".join(f"- {error}" for error in errors))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packets", nargs="+", type=Path)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--check-paths", action="store_true")
    args = parser.parse_args()
    failed = False
    for packet_path in args.packets:
        try:
            validate_file(packet_path, args.schema, args.check_paths)
            print(f"VALID {packet_path}")
        except (OSError, json.JSONDecodeError, ValidationFailure) as exc:
            failed = True
            print(f"INVALID {packet_path}\n{exc}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
