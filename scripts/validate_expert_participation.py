#!/usr/bin/env python3
"""Validate expert participation, consent, and transformation-authority packages."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Iterable

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = ROOT / "schemas" / "expert-participation.schema.json"


class ValidationFailure(Exception):
    """Raised when a participation package fails structural or semantic checks."""


def _duplicates(values: Iterable[str]) -> set[str]:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for value in values:
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    return duplicates


def _refs(owner: str, values: Iterable[str], valid: set[str], label: str, errors: list[str]) -> None:
    for value in values:
        if value not in valid:
            errors.append(f"{owner}: unknown {label} {value!r}")


def semantic_errors(package: dict[str, Any]) -> list[str]:
    """Return authority, consent-purpose, transformation, and delegation violations."""
    errors: list[str] = []
    keyed = (
        ("linked_artifacts", "artifact_id"), ("participants", "participant_id"),
        ("consent_records", "consent_id"), ("contribution_units", "contribution_id"),
        ("derived_artifacts", "artifact_id"), ("transformations", "transformation_id"),
        ("reviews", "review_id"), ("authority_delegations", "delegation_id"),
        ("decision_rights", "right_id"), ("reconsent_events", "event_id"),
    )
    for collection, key in keyed:
        for duplicate in sorted(_duplicates(item[key] for item in package[collection])):
            errors.append(f"{collection}: duplicate {key} {duplicate!r}")

    participants = {x["participant_id"]: x for x in package["participants"]}
    consents = {x["consent_id"]: x for x in package["consent_records"]}
    contributions = {x["contribution_id"]: x for x in package["contribution_units"]}
    artifacts = {x["artifact_id"]: x for x in package["derived_artifacts"]}
    transformations = {x["transformation_id"]: x for x in package["transformations"]}
    reviews = {x["review_id"]: x for x in package["reviews"]}
    participant_ids, consent_ids = set(participants), set(consents)
    contribution_ids, artifact_ids = set(contributions), set(artifacts)
    transformation_ids, review_ids = set(transformations), set(reviews)

    linked_contributors = {p["linked_contributor_id"] for p in package["participants"]}
    if len(linked_contributors) != len(package["participants"]):
        errors.append("participants: linked_contributor_id must be unique within one lifecycle")

    for consent in package["consent_records"]:
        owner = f"consent {consent['consent_id']}"
        _refs(owner, [consent["participant_id"]], participant_ids, "participant_id", errors)
        overlap = set(consent["allowed_purposes"]) & set(consent["prohibited_purposes"])
        if overlap:
            errors.append(f"{owner}: purposes cannot be both allowed and prohibited: {sorted(overlap)}")

    for unit in package["contribution_units"]:
        owner = f"contribution {unit['contribution_id']}"
        _refs(owner, [unit["participant_id"]], participant_ids, "participant_id", errors)
        _refs(owner, [unit["consent_id"]], consent_ids, "consent_id", errors)
        _refs(owner, unit["artifact_ids"], artifact_ids, "artifact_id", errors)
        consent = consents.get(unit["consent_id"])
        if consent:
            if consent["participant_id"] != unit["participant_id"]:
                errors.append(f"{owner}: consent belongs to a different participant")
            if unit["purpose"] not in consent["allowed_purposes"] or unit["purpose"] in consent["prohibited_purposes"]:
                errors.append(f"{owner}: purpose {unit['purpose']!r} is not authorized by consent")
            if consent["status"] in {"withdrawn", "superseded"}:
                errors.append(f"{owner}: cannot use withdrawn or superseded consent")

    for artifact in package["derived_artifacts"]:
        _refs(f"artifact {artifact['artifact_id']}", artifact["source_contribution_ids"], contribution_ids, "contribution_id", errors)

    for review in package["reviews"]:
        owner = f"review {review['review_id']}"
        _refs(owner, [review["artifact_id"], review["evidence_artifact_id"]], artifact_ids, "artifact_id", errors)
        _refs(owner, [review["reviewer_participant_id"]], participant_ids, "participant_id", errors)
        if review["transformation_id"] is not None:
            _refs(owner, [review["transformation_id"]], transformation_ids, "transformation_id", errors)

    for transform in package["transformations"]:
        owner = f"transformation {transform['transformation_id']}"
        _refs(owner, transform["input_artifact_ids"] + [transform["output_artifact_id"]], artifact_ids, "artifact_id", errors)
        _refs(owner, transform["consent_ids"], consent_ids, "consent_id", errors)
        _refs(owner, transform["review_ids"], review_ids, "review_id", errors)
        output = artifacts.get(transform["output_artifact_id"])
        for consent_id in transform["consent_ids"]:
            consent = consents.get(consent_id)
            if consent and (transform["purpose"] not in consent["allowed_purposes"] or transform["purpose"] in consent["prohibited_purposes"]):
                errors.append(f"{owner}: purpose drift without reconsent; {transform['purpose']!r} is not authorized by {consent_id!r}")
            if consent and transform["operation"] not in consent["allowed_transformations"]:
                errors.append(f"{owner}: operation {transform['operation']!r} is not authorized by {consent_id!r}")
        valid_approval = any(
            (review := reviews.get(review_id))
            and review["review_type"] == "transformation_fidelity"
            and review["transformation_id"] == transform["transformation_id"]
            and review["artifact_id"] == transform["output_artifact_id"]
            and review["disposition"] == "approved"
            and participants.get(review["reviewer_participant_id"], {}).get("actor_type") == "domain_expert"
            for review_id in transform["review_ids"]
        )
        if output and transform["material"] and output["authority_state"] in {"expert_approved", "expert_edited"} and not valid_approval:
            errors.append(f"{owner}: transformed artifact cannot inherit expert approval without post-transformation expert review")
        if output and transform["actor_type"] in {"model", "script", "benchmark_builder"} and output["authority_state"] == "expert_authored":
            errors.append(f"{owner}: non-expert output cannot be labeled expert_authored")

    for delegation in package["authority_delegations"]:
        owner = f"delegation {delegation['delegation_id']}"
        _refs(owner, [delegation["standard_artifact_id"]], artifact_ids, "artifact_id", errors)
        review_id = delegation["fidelity_review_id"]
        if review_id is not None:
            _refs(owner, [review_id], review_ids, "review_id", errors)
        review = reviews.get(review_id) if review_id else None
        valid_fidelity = bool(
            review and review["review_type"] == "held_out_application_fidelity"
            and review["held_out"] and review["disposition"] == "approved"
            and participants.get(review["reviewer_participant_id"], {}).get("actor_type") == "domain_expert"
        )
        if delegation["status"] == "approved" and not valid_fidelity:
            errors.append(f"{owner}: developer/model substitution requires approved held-out expert-fidelity evidence")

    for right in package["decision_rights"]:
        _refs(f"decision right {right['right_id']}", [right["participant_id"]], participant_ids, "participant_id", errors)

    for event in package["reconsent_events"]:
        owner = f"reconsent {event['event_id']}"
        _refs(owner, [event["old_consent_id"], event["new_consent_id"]], consent_ids, "consent_id", errors)
        _refs(owner, event["affected_artifact_ids"], artifact_ids, "artifact_id", errors)
        if event["old_consent_id"] == event["new_consent_id"]:
            errors.append(f"{owner}: reconsent must create a new consent version")

    release = package["release"]
    _refs("release", release["approved_artifact_ids"], artifact_ids, "artifact_id", errors)
    _refs("release", release["claim_review_ids"], review_ids, "review_id", errors)
    if release["expert_grounding_claim"] != "none":
        for artifact_id in release["approved_artifact_ids"]:
            artifact = artifacts.get(artifact_id)
            if artifact and artifact["authority_state"] not in {"expert_authored", "expert_edited", "expert_approved"}:
                errors.append(f"release: artifact {artifact_id!r} lacks current expert authority for an expert-grounding claim")
    if release["status"] == "releasable" and release["expert_grounding_claim"] == "none":
        errors.append("release: releasable expert-participation package must state a bounded or validated grounding claim")
    return errors


def validate_file(package_path: Path, schema_path: Path = DEFAULT_SCHEMA, check_paths: bool = False) -> None:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    package = json.loads(package_path.read_text(encoding="utf-8"))
    errors = [f"{'.'.join(map(str, e.absolute_path)) or '<root>'}: {e.message}" for e in sorted(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(package), key=lambda e: list(e.absolute_path))]
    if not errors:
        errors.extend(semantic_errors(package))
    if check_paths:
        for item in package["linked_artifacts"] + package["derived_artifacts"]:
            path = ROOT / item["path"]
            if not path.is_file():
                errors.append(f"artifact {item['artifact_id']}: path does not exist: {item['path']}")
            elif hashlib.sha256(path.read_bytes()).hexdigest() != item["sha256"]:
                errors.append(f"artifact {item['artifact_id']}: sha256 does not match {item['path']}")
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
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
