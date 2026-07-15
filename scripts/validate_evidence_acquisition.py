#!/usr/bin/env python3
"""Validate cross-domain evidence-acquisition episode packages."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Iterable

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = ROOT / "schemas" / "evidence-acquisition-episode.schema.json"
REQUIRED_CONDITIONS = {"active", "full_information", "expert_minimal"}
REQUIRED_ACCESS_STATUSES = {"released", "delayed", "denied", "ambiguous"}
REQUIRED_UNSUPPORTED = {
    "professional capability", "clinical validity", "compliance validity",
    "agent capability", "causal inquiry benefit", "safety", "production fitness",
    "deployment readiness", "cross-domain generality",
}


class ValidationFailure(Exception):
    """Raised when structural or semantic episode validation fails."""


def _duplicates(values: Iterable[str]) -> set[str]:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for value in values:
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    return duplicates


def semantic_errors(package: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if package.get("status") != "internal_synthetic_conformance_only":
        errors.append("status must remain internal_synthetic_conformance_only")
    if not REQUIRED_UNSUPPORTED <= set(package.get("claim_limits", {}).get("unsupported", [])):
        errors.append("claim limits omit required unsupported upgrades")

    conditions = {item["condition_id"]: item for item in package["conditions"]}
    if set(conditions) != REQUIRED_CONDITIONS:
        errors.append("condition matrix must contain exactly active, full_information, and expert_minimal")
    expected = {
        "active": ("on_request", True),
        "full_information": ("all_admissible_at_start", False),
        "expert_minimal": ("frozen_minimal_set_at_start", False),
    }
    for condition_id, vector in expected.items():
        item = conditions.get(condition_id, {})
        if (item.get("delivery_mode"), item.get("agent_may_request")) != vector:
            errors.append(f"condition {condition_id}: treatment vector drift")

    scenarios = package["scenarios"]
    if len({item["work_shape"] for item in scenarios}) < 2:
        errors.append("at least two unlike knowledge-work shapes are required")
    for duplicate in sorted(_duplicates(item["scenario_id"] for item in scenarios)):
        errors.append(f"duplicate scenario_id {duplicate!r}")

    observed_statuses: set[str] = set()
    for scenario in scenarios:
        sid = scenario["scenario_id"]
        atoms = {item["evidence_id"]: item for item in scenario["evidence_atoms"]}
        atom_ids = set(atoms)
        if len(atoms) != len(scenario["evidence_atoms"]):
            errors.append(f"{sid}: evidence ids must be unique")
        for atom in atoms.values():
            unknown = (set(atom["dependency_ids"]) | set(atom["contradicts_ids"])) - atom_ids
            if unknown:
                errors.append(f"{sid}/{atom['evidence_id']}: unknown evidence links {sorted(unknown)}")
            if atom["evidence_id"] in atom["dependency_ids"] or atom["evidence_id"] in atom["contradicts_ids"]:
                errors.append(f"{sid}/{atom['evidence_id']}: evidence cannot depend on or contradict itself")

        episodes = {item["condition_id"]: item for item in scenario["episodes"]}
        if set(episodes) != REQUIRED_CONDITIONS:
            errors.append(f"{sid}: must contain exactly one episode per matched condition")
            continue
        for condition_id, episode in episodes.items():
            owner = f"{sid}/{condition_id}"
            requests = {item["request_id"]: item for item in episode["requests"]}
            events = {item["access_event_id"]: item for item in episode["access_events"]}
            if len(requests) != len(episode["requests"]):
                errors.append(f"{owner}: request ids must be unique")
            if len(events) != len(episode["access_events"]):
                errors.append(f"{owner}: access event ids must be unique")
            if condition_id == "active" and not requests:
                errors.append(f"{owner}: active condition requires observable inquiry requests")
            if condition_id != "active" and requests:
                errors.append(f"{owner}: supplied-information conditions cannot contain agent requests")

            for request in requests.values():
                parser = request["parser_interpretation"]
                mapped = set(parser["mapped_evidence_ids"])
                if not mapped <= atom_ids:
                    errors.append(f"{owner}/{request['request_id']}: parser maps unknown evidence ids")
                if parser["status"] == "matched" and len(mapped) != 1:
                    errors.append(f"{owner}/{request['request_id']}: matched parser result requires exactly one evidence id")
                if parser["status"] in {"unmatched", "parser_error"} and mapped:
                    errors.append(f"{owner}/{request['request_id']}: unmatched/parser_error cannot map evidence")

            released_ids: set[str] = set()
            for event in events.values():
                observed_statuses.add(event["status"])
                request_id, evidence_id = event["request_id"], event["evidence_id"]
                if condition_id == "active" and request_id not in requests:
                    errors.append(f"{owner}/{event['access_event_id']}: access transition lacks its request")
                if condition_id != "active" and request_id is not None:
                    errors.append(f"{owner}/{event['access_event_id']}: environment-supplied evidence cannot cite an agent request")
                if evidence_id is not None and evidence_id not in atom_ids:
                    errors.append(f"{owner}/{event['access_event_id']}: unknown evidence_id {evidence_id!r}")
                if event["status"] == "released":
                    if evidence_id is None or event["content_locator"] is None:
                        errors.append(f"{owner}/{event['access_event_id']}: released evidence needs identity and content locator")
                    else:
                        released_ids.add(evidence_id)
                elif event["content_locator"] is not None:
                    errors.append(f"{owner}/{event['access_event_id']}: non-release access status cannot expose evidence content")
                if request_id in requests:
                    parser = requests[request_id]["parser_interpretation"]
                    if event["status"] == "released" and (parser["status"] != "matched" or evidence_id not in parser["mapped_evidence_ids"]):
                        errors.append(f"{owner}/{event['access_event_id']}: parser interpretation and release are conflated or inconsistent")
                    if event["status"] == "ambiguous" and parser["status"] != "ambiguous":
                        errors.append(f"{owner}/{event['access_event_id']}: ambiguous access requires a separately recorded ambiguous parser result")

            admissible = {eid for eid, atom in atoms.items() if atom["availability"] in {"admissible", "delayed"}}
            minimal = {eid for eid, atom in atoms.items() if atom["minimal_set_member"]}
            if condition_id == "full_information" and released_ids != admissible:
                errors.append(f"{owner}: full-information condition must supply every admissible/delayed atom")
            if condition_id == "expert_minimal" and released_ids != minimal:
                errors.append(f"{owner}: expert-minimal condition must supply exactly the frozen minimal set")

            for adoption in episode["adoptions"]:
                if adoption["access_event_id"] not in events:
                    errors.append(f"{owner}: adoption references unknown access event")
                    continue
                event = events[adoption["access_event_id"]]
                if event["status"] != "released" or event["evidence_id"] != adoption["evidence_id"]:
                    errors.append(f"{owner}: adoption must map to a release of the same evidence atom")
                if not adoption["trace_evidence_locator"].strip():
                    errors.append(f"{owner}: endpoint-only adoption inference is prohibited")

            firewall = episode["feedback_firewall"]
            if firewall["evaluator_outputs_exposed_before_terminal"]:
                errors.append(f"{owner}: evaluator feedback must remain firewalled until terminal action")
            for feedback in firewall["feedback_events"]:
                if feedback["source"] in {"evaluator", "grader"} and feedback["phase"] != "post_terminal":
                    errors.append(f"{owner}: undeclared evaluator/grader feedback before terminal action")
                if feedback["phase"] == "preterminal" and feedback["content_kind"] not in firewall["allowed_preterminal_feedback"]:
                    errors.append(f"{owner}: preterminal feedback kind is not allowlisted")

            stopping = episode["stopping"]
            basis, unacquired = set(stopping["basis_evidence_ids"]), set(stopping["considered_unacquired_ids"])
            if not basis <= released_ids or not unacquired <= atom_ids - released_ids:
                errors.append(f"{owner}: stopping basis/unacquired ledger is inconsistent with access")
            required_reason = {"full_information": "all_supplied", "expert_minimal": "expert_minimal_set_supplied"}.get(condition_id)
            if required_reason and stopping["reason"] != required_reason:
                errors.append(f"{owner}: supplied condition has invalid stopping reason")
            if condition_id == "active" and stopping["reason"] in {"all_supplied", "expert_minimal_set_supplied"}:
                errors.append(f"{owner}: active inquiry cannot use a supplied-condition stopping reason")
            if stopping["reason"] in {"decision_sufficient", "marginal_value_below_cost"} and (not basis or not unacquired):
                errors.append(f"{owner}: substantive stopping requires acquired basis and considered unacquired evidence")
            max_step = max([item["step"] for item in episode["requests"] + episode["access_events"]], default=0)
            if stopping["step"] < max_step:
                errors.append(f"{owner}: stopping occurs before the final request/access transition")
            if not episode["terminal_consequence"]["endpoint_evidence_locators"]:
                errors.append(f"{owner}: terminal consequence lacks direct endpoint evidence")

    if not REQUIRED_ACCESS_STATUSES <= observed_statuses:
        errors.append(f"planted access-status coverage missing: {sorted(REQUIRED_ACCESS_STATUSES - observed_statuses)}")
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
        for item in package.get("provenance", []):
            path = ROOT / item["path"]
            if not path.is_file():
                errors.append(f"missing provenance path: {item['path']}")
            elif hashlib.sha256(path.read_bytes()).hexdigest() != item["sha256"]:
                errors.append(f"provenance hash mismatch: {item['path']}")
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
        except (OSError, ValueError, json.JSONDecodeError, ValidationFailure) as exc:
            failed = True
            print(f"INVALID {package_path}\n{exc}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
