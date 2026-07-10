#!/usr/bin/env python3
"""Validate claim-centered validity argument packages.

JSON Schema checks shape. Semantic checks prevent unbound evidence, scalar or
undifferentiated validity approval, unsupported claim upgrades, and decision
claims without an evidence-backed threshold/loss policy.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Iterable

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = ROOT / "schemas" / "validity-argument.schema.json"
FACETS = {"content", "criterion", "construct", "external", "consequential"}
INSTRUMENT_TYPES = {"task", "bundle", "rubric", "grader", "harness", "environment"}
MEASUREMENT_TYPES = {"trial", "measurement", "adjudication", "impact_record"}


class ValidationFailure(Exception):
    """Raised when a validity package fails structural or semantic checks."""


def _duplicates(values: Iterable[str]) -> set[str]:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for value in values:
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    return duplicates


def _check_refs(owner: str, values: Iterable[str], valid: set[str], label: str, errors: list[str]) -> None:
    for value in values:
        if value not in valid:
            errors.append(f"{owner}: unknown {label} {value!r}")


def semantic_errors(package: dict[str, Any]) -> list[str]:
    """Return reference, evidence-scope, facet, and claim-licensing violations."""
    errors: list[str] = []
    for items, key, label in (
        (package["artifacts"], "artifact_id", "artifacts"),
        (package["evidence"], "evidence_id", "evidence"),
        (package["arguments"], "argument_id", "arguments"),
    ):
        for duplicate in sorted(_duplicates(item[key] for item in items)):
            errors.append(f"{label}: duplicate {key} {duplicate!r}")

    artifacts = {item["artifact_id"]: item for item in package["artifacts"]}
    evidence = {item["evidence_id"]: item for item in package["evidence"]}
    arguments = {item["argument_id"]: item for item in package["arguments"]}
    artifact_ids, evidence_ids, argument_ids = set(artifacts), set(evidence), set(arguments)

    for item in package["evidence"]:
        owner = f"evidence {item['evidence_id']}"
        _check_refs(owner, [item["artifact_ref_id"]], artifact_ids, "artifact_ref_id", errors)
        _check_refs(owner, item["claim_scope"], argument_ids, "argument_id", errors)
        if item["evidence_type"] == "expert_review" and len(item["facet_scope"]) != 1:
            errors.append(f"{owner}: expert review must address exactly one validity facet; undifferentiated expert-validity approval is forbidden")

    for argument in package["arguments"]:
        argument_id = argument["argument_id"]
        owner = f"argument {argument_id}"
        _check_refs(owner, argument["instrument_ref_ids"], artifact_ids, "artifact_ref_id", errors)
        _check_refs(owner, argument["measurement_ref_ids"], artifact_ids, "artifact_ref_id", errors)
        for ref in argument["instrument_ref_ids"]:
            if ref in artifacts and artifacts[ref]["artifact_type"] not in INSTRUMENT_TYPES:
                errors.append(f"{owner}: instrument_ref_id {ref!r} has non-instrument type")
        for ref in argument["measurement_ref_ids"]:
            if ref in artifacts and artifacts[ref]["artifact_type"] not in MEASUREMENT_TYPES:
                errors.append(f"{owner}: measurement_ref_id {ref!r} has non-measurement type")

        inference = argument["inference"]
        referenced_evidence = set(inference["evidence_ids"])
        _check_refs(owner, referenced_evidence, evidence_ids, "evidence_id", errors)
        for item in inference["assumptions"]:
            _check_refs(f"{owner} assumption {item['assumption_id']}", item["evidence_ids"], evidence_ids, "evidence_id", errors)
        for item in inference["rebuttals"]:
            _check_refs(f"{owner} rebuttal {item['rebuttal_id']}", item["evidence_ids"], evidence_ids, "evidence_id", errors)
        for item in inference["nomological_links"]:
            _check_refs(f"{owner} nomological link", item["evidence_ids"], evidence_ids, "evidence_id", errors)

        facets = argument["validity_facets"]
        facet_names = [item["facet"] for item in facets]
        if set(facet_names) != FACETS or len(facet_names) != len(set(facet_names)):
            errors.append(f"{owner}: validity_facets must contain each of the five facets exactly once")
        facets_by_name = {item["facet"]: item for item in facets}
        for facet in facets:
            facet_owner = f"{owner} facet {facet['facet']}"
            _check_refs(facet_owner, facet["evidence_ids"], evidence_ids, "evidence_id", errors)
            for evidence_id in facet["evidence_ids"]:
                item = evidence.get(evidence_id)
                if item and facet["facet"] not in item["facet_scope"]:
                    errors.append(f"{facet_owner}: evidence {evidence_id!r} is not scoped to this facet")
                if item and item["claim_scope"] and argument_id not in item["claim_scope"]:
                    errors.append(f"{facet_owner}: evidence {evidence_id!r} is not scoped to this claim")
            if facet["requirement"] == "required" and facet["status"] == "supported" and not facet["evidence_ids"]:
                errors.append(f"{facet_owner}: supported required facet needs scoped evidence")
            if facet["requirement"] != "required" and not facet["rationale"]:
                errors.append(f"{facet_owner}: bypassed facet requires rationale")

        claim_type = argument["claim"]["object_type"]
        status = argument["status"]
        if claim_type == "construct":
            construct = facets_by_name.get("construct", {})
            if construct.get("requirement") != "required":
                errors.append(f"{owner}: construct claim cannot bypass construct validity")
            if status in {"supported", "provisional"} and (
                not inference["mediating_constructs"] or not inference["nomological_links"]
            ):
                errors.append(f"{owner}: supported/provisional construct claim requires mediating constructs and evidence-linked nomological links")
        if claim_type == "decision":
            if "decision_policy" not in argument:
                errors.append(f"{owner}: decision claim requires a decision_policy")
            consequential = facets_by_name.get("consequential", {})
            if consequential.get("requirement") != "required":
                errors.append(f"{owner}: decision claim cannot bypass consequential validity")
        elif "decision_policy" in argument and argument["decision_policy"]["threshold_basis"] != "none":
            errors.append(f"{owner}: non-decision claim cannot license an action threshold")

        if status == "supported":
            unsupported = [f["facet"] for f in facets if f["requirement"] == "required" and f["status"] != "supported"]
            if unsupported:
                errors.append(f"{owner}: supported claim has unsupported required facets {unsupported}")
            open_assumptions = [a["assumption_id"] for a in inference["assumptions"] if a["status"] in {"contested", "untested", "rejected"}]
            open_rebuttals = [r["rebuttal_id"] for r in inference["rebuttals"] if r["status"] == "open"]
            if open_assumptions or open_rebuttals:
                errors.append(f"{owner}: supported claim has unresolved assumptions/rebuttals {open_assumptions + open_rebuttals}")
            if claim_type == "decision":
                policy = argument.get("decision_policy", {})
                if policy.get("threshold_basis") in {"provisional_policy", "none"}:
                    errors.append(f"{owner}: supported decision claim requires empirical loss or expert standard-setting evidence")
        for evidence_id in referenced_evidence:
            item = evidence.get(evidence_id)
            if item and item["claim_scope"] and argument_id not in item["claim_scope"]:
                errors.append(f"{owner}: inference evidence {evidence_id!r} is not scoped to this claim")

        _check_refs(owner, argument["independent_review_evidence_ids"], evidence_ids, "evidence_id", errors)
        for evidence_id in argument["independent_review_evidence_ids"]:
            item = evidence.get(evidence_id)
            if item and item["evidence_type"] not in {"expert_review", "human_adjudication"}:
                errors.append(f"{owner}: independent review reference {evidence_id!r} is not review evidence")

    return errors


def validate_file(package_path: Path, schema_path: Path = DEFAULT_SCHEMA, check_paths: bool = False) -> None:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    package = json.loads(package_path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = [
        f"{'.'.join(str(part) for part in error.absolute_path) or '<root>'}: {error.message}"
        for error in sorted(validator.iter_errors(package), key=lambda item: list(item.absolute_path))
    ]
    if not errors:
        errors.extend(semantic_errors(package))
    if check_paths:
        for artifact in package["artifacts"]:
            path = ROOT / artifact["path"]
            if not path.is_file():
                errors.append(f"artifact {artifact['artifact_id']}: path does not exist: {artifact['path']}")
            elif hashlib.sha256(path.read_bytes()).hexdigest() != artifact["sha256"]:
                errors.append(f"artifact {artifact['artifact_id']}: sha256 does not match {artifact['path']}")
    if errors:
        raise ValidationFailure("\n".join(f"- {error}" for error in errors))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packages", nargs="+", type=Path)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--check-paths", action="store_true")
    args = parser.parse_args()
    failed = False
    for package_path in args.packages:
        try:
            validate_file(package_path, args.schema, args.check_paths)
            print(f"VALID {package_path}")
        except (OSError, json.JSONDecodeError, ValidationFailure) as exc:
            failed = True
            print(f"INVALID {package_path}\n{exc}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
