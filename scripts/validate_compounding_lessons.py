#!/usr/bin/env python3
"""Validate provenance-gated compounding lesson stores.

JSON Schema checks record shape. Semantic checks enforce immutable content,
append-only lifecycle transitions, independent promotion, contradiction handling,
private-evidence firewalls, downstream lineage, and executable rollback.
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
DEFAULT_SCHEMA = ROOT / "schemas" / "compounding-lessons.schema.json"
REQUIRED_DIMENSIONS = {
    "declared_criterion",
    "safety_regression",
    "contradiction_handling",
    "distribution_shift",
}
ALLOWED_EVENT_TRANSITIONS = {
    "proposed": {(None, "candidate")},
    "validation_recorded": {
        ("candidate", "candidate"),
        ("candidate", "validated"),
        ("validated", "validated"),
        ("promoted", "promoted"),
        ("quarantined", "quarantined"),
    },
    "promoted": {("validated", "promoted")},
    "quarantined": {
        ("candidate", "quarantined"),
        ("validated", "quarantined"),
        ("promoted", "quarantined"),
    },
    "deprecated": {("promoted", "deprecated"), ("quarantined", "deprecated")},
    "superseded": {("promoted", "deprecated")},
    "rollback": {("promoted", "quarantined"), ("promoted", "deprecated")},
}


class ValidationFailure(Exception):
    """Raised when a lesson store fails structural or semantic validation."""


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


def _pair(a: str, b: str) -> frozenset[str]:
    return frozenset((a, b))


def _qualifying_validation(validation: dict[str, Any]) -> bool:
    dimensions = {item["dimension"]: item["status"] for item in validation["dimensions"]}
    return (
        validation["status"] == "passed"
        and all(validation["independence"].values())
        and set(dimensions) == REQUIRED_DIMENSIONS
        and all(status == "passed" for status in dimensions.values())
    )


def semantic_errors(store: dict[str, Any]) -> list[str]:
    """Return immutable-lineage, promotion, contradiction, firewall, and rollback violations."""
    errors: list[str] = []
    collections = [
        (store["observations"], "observation_id", "observations"),
        (store["lessons"], "lesson_id", "lessons"),
        (store["validations"], "validation_id", "validations"),
        (store["relations"], "relation_id", "relations"),
        (store["contradiction_resolutions"], "resolution_id", "contradiction_resolutions"),
        (store["lifecycle_events"], "event_id", "lifecycle_events"),
        (store["dependencies"], "dependency_id", "dependencies"),
        (store["rollbacks"], "rollback_id", "rollbacks"),
    ]
    for items, key, location in collections:
        _check_unique(items, key, location, errors)

    observations = {item["observation_id"]: item for item in store["observations"]}
    lessons = {item["lesson_id"]: item for item in store["lessons"]}
    validations = {item["validation_id"]: item for item in store["validations"]}
    events = {item["event_id"]: item for item in store["lifecycle_events"]}
    dependencies = {item["dependency_id"]: item for item in store["dependencies"]}
    rollbacks = {item["rollback_id"]: item for item in store["rollbacks"]}
    observation_ids = set(observations)
    lesson_ids = set(lessons)
    validation_ids = set(validations)
    event_ids = set(events)
    dependency_ids = set(dependencies)
    rollback_ids = set(rollbacks)

    for lesson in store["lessons"]:
        owner = f"lesson {lesson['lesson_id']}"
        expected_hash = hashlib.sha256(lesson["statement"].encode("utf-8")).hexdigest()
        if lesson["content_sha256"] != expected_hash:
            errors.append(f"{owner}: content_sha256 does not match the immutable statement")
        _check_refs(owner, lesson["source_observation_ids"], observation_ids, "observation_id", errors)

    for validation in store["validations"]:
        owner = f"validation {validation['validation_id']}"
        _check_refs(owner, [validation["lesson_id"]], lesson_ids, "lesson_id", errors)
        _check_refs(owner, validation["source_observation_ids"], observation_ids, "observation_id", errors)
        for dimension in validation["dimensions"]:
            _check_refs(owner, dimension["evidence_observation_ids"], observation_ids, "observation_id", errors)
        dimensions = [item["dimension"] for item in validation["dimensions"]]
        if set(dimensions) != REQUIRED_DIMENSIONS or len(dimensions) != len(set(dimensions)):
            errors.append(f"{owner}: dimensions must contain each required promotion dimension exactly once")
        lesson = lessons.get(validation["lesson_id"])
        if lesson:
            overlap = set(lesson["source_observation_ids"]) & set(validation["source_observation_ids"])
            if overlap:
                errors.append(f"{owner}: validation reuses proposal observations {sorted(overlap)}")
            proposal_clusters = {
                observations[item]["scenario_cluster"]
                for item in lesson["source_observation_ids"]
                if item in observations
            }
            validation_clusters = {
                observations[item]["scenario_cluster"]
                for item in validation["source_observation_ids"]
                if item in observations
            }
            if validation["independence"]["scenario_cluster_distinct"] and proposal_clusters & validation_clusters:
                errors.append(f"{owner}: claims distinct scenario clusters but overlaps {sorted(proposal_clusters & validation_clusters)}")
        if validation["status"] == "passed" and not _qualifying_validation(validation):
            errors.append(f"{owner}: passed status requires all independence controls and promotion dimensions to pass")

    events_by_lesson: dict[str, list[dict[str, Any]]] = {lesson_id: [] for lesson_id in lesson_ids}
    for event in store["lifecycle_events"]:
        owner = f"event {event['event_id']}"
        _check_refs(owner, [event["lesson_id"]], lesson_ids, "lesson_id", errors)
        _check_refs(owner, event["observation_ids"], observation_ids, "observation_id", errors)
        _check_refs(owner, event["validation_ids"], validation_ids, "validation_id", errors)
        if (event["from_state"], event["to_state"]) not in ALLOWED_EVENT_TRANSITIONS[event["event_type"]]:
            errors.append(
                f"{owner}: invalid {event['event_type']} transition "
                f"{event['from_state']!r}->{event['to_state']!r}"
            )
        if event["lesson_id"] in events_by_lesson:
            events_by_lesson[event["lesson_id"]].append(event)

    for lesson_id, lesson_events in events_by_lesson.items():
        owner = f"lesson {lesson_id} lifecycle"
        if not lesson_events:
            errors.append(f"{owner}: requires at least one event")
            continue
        current = None
        for event in lesson_events:
            if event["from_state"] != current:
                errors.append(
                    f"{owner}: event {event['event_id']!r} starts at {event['from_state']!r}, expected {current!r}; history must be append-only and contiguous"
                )
            current = event["to_state"]
        if current != lessons[lesson_id]["state"]:
            errors.append(f"{owner}: final event state {current!r} does not match lesson state {lessons[lesson_id]['state']!r}")

    qualifying_by_lesson: dict[str, set[str]] = {lesson_id: set() for lesson_id in lesson_ids}
    for validation in store["validations"]:
        if validation["lesson_id"] in qualifying_by_lesson and _qualifying_validation(validation):
            qualifying_by_lesson[validation["lesson_id"]].add(validation["validation_id"])
    for event in store["lifecycle_events"]:
        if event["event_type"] == "promoted":
            qualifying = qualifying_by_lesson.get(event["lesson_id"], set())
            if not qualifying or not (set(event["validation_ids"]) & qualifying):
                errors.append(f"event {event['event_id']}: promotion requires a referenced independent passed validation")

    relation_types: dict[frozenset[str], set[str]] = {}
    contradiction_pairs: set[frozenset[str]] = set()
    for relation in store["relations"]:
        owner = f"relation {relation['relation_id']}"
        _check_refs(owner, [relation["from_lesson_id"], relation["to_lesson_id"]], lesson_ids, "lesson_id", errors)
        _check_refs(owner, relation["evidence_observation_ids"], observation_ids, "observation_id", errors)
        if relation["from_lesson_id"] == relation["to_lesson_id"]:
            errors.append(f"{owner}: a lesson cannot relate to itself")
        pair = _pair(relation["from_lesson_id"], relation["to_lesson_id"])
        relation_types.setdefault(pair, set()).add(relation["type"])
        if relation["type"] == "contradicts":
            contradiction_pairs.add(pair)

    accepted_resolutions: dict[frozenset[str], dict[str, Any]] = {}
    for resolution in store["contradiction_resolutions"]:
        owner = f"resolution {resolution['resolution_id']}"
        _check_refs(owner, resolution["lesson_ids"], lesson_ids, "lesson_id", errors)
        _check_refs(owner, resolution["evidence_observation_ids"], observation_ids, "observation_id", errors)
        pair = frozenset(resolution["lesson_ids"])
        if resolution["status"] == "accepted" and resolution["decision"] != "unresolved":
            accepted_resolutions[pair] = resolution

    promoted = {lesson_id for lesson_id, lesson in lessons.items() if lesson["state"] == "promoted"}
    for pair, types in relation_types.items():
        if "contradicts" in types and ({"supersedes", "duplicates"} & types) and pair not in accepted_resolutions:
            errors.append(f"relations: contradictory merge for lessons {sorted(pair)} requires an accepted resolution")
        if pair <= promoted and "contradicts" in types and pair not in accepted_resolutions:
            errors.append(f"relations: contradictory promoted lessons {sorted(pair)} require an accepted resolution")

    private_visibilities = set(store["policy"]["private_feedback_visibilities"])
    outward_exposures = set(store["policy"]["agent_visible_exposures"])
    for dependency in store["dependencies"]:
        owner = f"dependency {dependency['dependency_id']}"
        _check_refs(owner, [dependency["lesson_id"]], lesson_ids, "lesson_id", errors)
        _check_refs(owner, [dependency["introduced_by_event_id"]], event_ids, "event_id", errors)
        introduced_by = events.get(dependency["introduced_by_event_id"])
        if introduced_by and (
            introduced_by["event_type"] != "promoted"
            or introduced_by["lesson_id"] != dependency["lesson_id"]
        ):
            errors.append(f"{owner}: introduced_by_event_id must reference this lesson's promotion event")
        if dependency.get("retired_by_rollback_id"):
            _check_refs(owner, [dependency["retired_by_rollback_id"]], rollback_ids, "rollback_id", errors)
        lesson = lessons.get(dependency["lesson_id"])
        if dependency["active"] and lesson and lesson["state"] != "promoted":
            errors.append(f"{owner}: active downstream dependency requires a promoted lesson")
        if lesson and dependency["active"] and dependency["exposure"] in outward_exposures:
            private_sources = [
                observations[item]
                for item in lesson["source_observation_ids"]
                if item in observations and observations[item]["visibility"] in private_visibilities
            ]
            if dependency["exposure"] == "public" and private_sources:
                errors.append(f"{owner}: public dependency leaks private/reference-derived lesson evidence")
            target_splits = set(dependency["evaluation_split_ids"])
            overlap = sorted({split for obs in private_sources for split in obs["evaluation_split_ids"]} & target_splits)
            if dependency["exposure"] == "agent_visible" and overlap:
                errors.append(f"{owner}: private-evidence firewall blocks agent-visible use on splits {overlap}")

    for rollback in store["rollbacks"]:
        owner = f"rollback {rollback['rollback_id']}"
        _check_refs(owner, [rollback["lesson_id"]], lesson_ids, "lesson_id", errors)
        _check_refs(owner, [rollback["event_id"]], event_ids, "event_id", errors)
        _check_refs(owner, rollback["cause_observation_ids"], observation_ids, "observation_id", errors)
        _check_refs(owner, rollback["reverted_dependency_ids"], dependency_ids, "dependency_id", errors)
        event = events.get(rollback["event_id"])
        if event and (event["event_type"] != "rollback" or event["lesson_id"] != rollback["lesson_id"]):
            errors.append(f"{owner}: event_id must reference this lesson's rollback lifecycle event")
        if rollback["status"] == "applied":
            for dependency_id in rollback["reverted_dependency_ids"]:
                dependency = dependencies.get(dependency_id)
                if dependency and (dependency["active"] or dependency.get("retired_by_rollback_id") != rollback["rollback_id"]):
                    errors.append(f"{owner}: applied rollback must retire dependency {dependency_id!r} with reciprocal linkage")

    return errors


def _declared_paths(store: dict[str, Any]) -> Iterable[str]:
    for observation in store["observations"]:
        if observation.get("local_path"):
            yield observation["local_path"]
    for validation in store["validations"]:
        yield from validation["evidence_paths"]
    for dependency in store["dependencies"]:
        yield dependency["target_path"]


def validate_file(store_path: Path, schema_path: Path = DEFAULT_SCHEMA, check_paths: bool = False) -> None:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    store = json.loads(store_path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = [
        f"{'.'.join(str(part) for part in error.absolute_path) or '<root>'}: {error.message}"
        for error in sorted(validator.iter_errors(store), key=lambda item: list(item.absolute_path))
    ]
    if not errors:
        errors.extend(semantic_errors(store))
    if check_paths:
        for path in sorted(set(_declared_paths(store))):
            if not (ROOT / path).is_file():
                errors.append(f"declared repository path does not exist: {path}")
        for dependency in store["dependencies"]:
            target = ROOT / dependency["target_path"]
            if target.is_file():
                actual = hashlib.sha256(target.read_bytes()).hexdigest()
                if actual != dependency["target_sha256"]:
                    errors.append(
                        f"dependency {dependency['dependency_id']}: target_sha256 does not match {dependency['target_path']}"
                    )
    if errors:
        raise ValidationFailure("\n".join(f"- {error}" for error in errors))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stores", nargs="+", type=Path)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--check-paths", action="store_true")
    args = parser.parse_args()
    failed = False
    for store_path in args.stores:
        try:
            validate_file(store_path, args.schema, args.check_paths)
            print(f"VALID {store_path}")
        except (OSError, json.JSONDecodeError, ValidationFailure) as exc:
            failed = True
            print(f"INVALID {store_path}\n{exc}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
