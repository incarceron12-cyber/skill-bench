#!/usr/bin/env python3
"""Independently validate source-only procedure-generation outputs."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas/procedure-generation-output.schema.json"


class ValidationFailure(Exception):
    pass


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def duplicates(values: Iterable[str]) -> set[str]:
    seen: set[str] = set()
    repeated: set[str] = set()
    for value in values:
        if value in seen:
            repeated.add(value)
        seen.add(value)
    return repeated


def structural_errors(package: dict[str, Any]) -> list[str]:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    return [
        f"{'.'.join(map(str, error.absolute_path)) or '<root>'}: {error.message}"
        for error in Draft202012Validator(schema).iter_errors(package)
    ]


def semantic_errors(
    package: dict[str, Any],
    source: dict[str, Any],
    source_bytes: bytes,
    policy: dict[str, Any],
) -> list[str]:
    errors: list[str] = []
    identity = package["source_identity"]
    actual_hash = sha256(source_bytes)
    if actual_hash != policy.get("source_corpus_sha256"):
        errors.append("source corpus bytes do not match the predeclared policy hash")
    if identity.get("source_corpus_sha256") != actual_hash:
        errors.append("package source hash does not match exact source bytes")
    for key in ("family_id", "family_version"):
        expected = policy.get(f"expected_{key}")
        if identity.get(key) != expected or source.get(key) != expected:
            errors.append(f"{key} does not match source and predeclared policy")

    context = package["generation_context"]
    if context.get("visible_inputs") != policy.get("allowed_visible_inputs"):
        errors.append("generation visible inputs differ from the exact source-only allowlist")
    serialized = json.dumps(package, sort_keys=True).casefold()
    for token in policy.get("forbidden_tokens", []):
        if token.casefold() in serialized:
            errors.append(f"forbidden downstream token leaked into package: {token}")
    for fragment in policy.get("forbidden_path_fragments", []):
        if any(fragment.casefold() in path.casefold() for path in context.get("visible_inputs", [])):
            errors.append(f"forbidden downstream path leaked into generation view: {fragment}")
    if package.get("claim_ceiling") != policy.get("allowed_claim_ceiling"):
        errors.append("claim ceiling differs from the predeclared all-false ceiling")

    propositions = source.get("propositions", [])
    proposition_ids = {row.get("id") for row in propositions}
    bindings = package["proposition_bindings"]
    binding_ids = [row["proposition_id"] for row in bindings]
    if duplicates(binding_ids):
        errors.append("duplicate proposition binding")
    if set(binding_ids) != proposition_ids:
        errors.append("proposition bindings must exhaust every and only source proposition")

    clauses = package["clauses"]
    clause_ids = [row["clause_id"] for row in clauses]
    if duplicates(clause_ids):
        errors.append("duplicate clause identity")
    clause_by_id = {row["clause_id"]: row for row in clauses}
    for clause in clauses:
        if not set(clause["proposition_basis"]) <= proposition_ids:
            errors.append(f"clause {clause['clause_id']} has unknown proposition basis")
    for binding in bindings:
        proposition_id = binding["proposition_id"]
        declared_clauses = set(binding["clause_ids"])
        if not declared_clauses <= set(clause_by_id):
            errors.append(f"binding {proposition_id} references unknown clause")
            continue
        reciprocal = {
            clause_id for clause_id, clause in clause_by_id.items()
            if proposition_id in clause["proposition_basis"]
        }
        if declared_clauses != reciprocal:
            errors.append(f"binding {proposition_id} is not reciprocal with clause bases")
    referenced_clauses = {clause_id for row in bindings for clause_id in row["clause_ids"]}
    if referenced_clauses != set(clause_by_id):
        errors.append("every clause must be proposition-bound")

    primitive_specs = (
        ("contradictions", "contradictions", "contradiction", "propositions"),
        ("decision_thresholds", "thresholds", "threshold", "basis"),
        ("artifact_conventions", "artifact_conventions", "artifact_convention", "basis"),
        ("failure_signatures", "failure_signatures", "failure_signature", "basis"),
    )
    omissions = package["omissions"]
    omission_pairs = [(row["source_kind"], row["source_object_id"]) for row in omissions]
    if duplicates(f"{kind}:{item_id}" for kind, item_id in omission_pairs):
        errors.append("duplicate typed omission")
    for source_key, output_key, omission_kind, basis_key in primitive_specs:
        source_rows = source.get(source_key, [])
        source_by_id = {row.get("id"): row for row in source_rows}
        output_rows = package[output_key]
        output_ids = [row["source_object_id"] for row in output_rows]
        omitted_ids = [item_id for kind, item_id in omission_pairs if kind == omission_kind]
        if duplicates(output_ids):
            errors.append(f"{output_key} has duplicate source projection")
        if set(output_ids) & set(omitted_ids):
            errors.append(f"{output_key} source object cannot be both projected and omitted")
        if set(output_ids) | set(omitted_ids) != set(source_by_id):
            errors.append(f"{output_key} must project or explicitly omit every and only source object")
        for row in output_rows:
            source_row = source_by_id.get(row["source_object_id"])
            if source_row is None:
                continue
            expected_basis = set(source_row.get(basis_key, []))
            if set(row["proposition_basis"]) != expected_basis or not expected_basis <= proposition_ids:
                errors.append(f"{output_key} {row['source_object_id']} has invalid proposition basis")
    return errors


def validate_documents(
    package: dict[str, Any],
    package_bytes: bytes,
    source: dict[str, Any],
    source_bytes: bytes,
    policy: dict[str, Any],
    launcher_report: dict[str, Any] | None = None,
) -> list[str]:
    errors = structural_errors(package)
    if not errors:
        errors.extend(semantic_errors(package, source, source_bytes, policy))
    if launcher_report is not None:
        if launcher_report.get("package_sha256") != sha256(package_bytes):
            errors.append("launcher report package hash does not match candidate bytes")
        if launcher_report.get("launcher_valid") is True and errors:
            errors.append("false launcher acceptance: independent validation rejects launcher-valid output")
    return errors


def validate_file(
    package_path: Path,
    source_path: Path,
    policy_path: Path,
    launcher_report_path: Path | None = None,
) -> None:
    package_bytes = package_path.read_bytes()
    source_bytes = source_path.read_bytes()
    package = json.loads(package_bytes)
    source = json.loads(source_bytes)
    policy = json.loads(policy_path.read_text(encoding="utf-8"))
    report = json.loads(launcher_report_path.read_text(encoding="utf-8")) if launcher_report_path else None
    errors = validate_documents(package, package_bytes, source, source_bytes, policy, report)
    if errors:
        raise ValidationFailure("\n".join(f"- {error}" for error in errors))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", type=Path)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--policy", type=Path, required=True)
    parser.add_argument("--launcher-report", type=Path)
    args = parser.parse_args()
    try:
        validate_file(args.package, args.source, args.policy, args.launcher_report)
        print(f"VALID {args.package}")
        return 0
    except (OSError, json.JSONDecodeError, ValidationFailure) as exc:
        print(f"INVALID {args.package}\n{exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
