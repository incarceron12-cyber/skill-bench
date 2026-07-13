#!/usr/bin/env python3
"""Replay the frozen cross-pilot falsification coverage inventory.

This verifies identity and recorded observations. It deliberately does not execute
agents or reinterpret internal conformance cases as capability evidence.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
MANIFEST = HERE / "coverage-manifest.json"
REPORT = HERE / "report.json"

REQUIREMENTS = {
    "evidence_chain": {
        "authoritative_source", "superseded_source", "lexical_distractor",
        "correct_uncited_claim", "precise_non_entailing_citation", "source_never_exposed",
    },
    "state_delta": {
        "pre_satisfied_requirement", "unrelated_same_value_record", "title_only_empty_artifact",
        "shared_cause_descendant_failures", "dirty_output_path",
    },
    "artifact_behavior": {"native_view", "rendered_view", "pinned_engine_recalculation", "preserved_region"},
    "skill_instrument_independence": {
        "no_skill_independent_rubric", "no_skill_shared_rubric",
        "public_skill_independent_rubric", "public_skill_shared_rubric", "treatment_effect_ceiling",
    },
    "alternative_path_verifier": {
        "positive_witness", "independently_valid_alternative", "minimally_wrong_contrast",
        "shortcut_or_adversarial_artifact", "parser_renderer_drift",
    },
    "claim_ladder": {"task_package_claim", "workflow_family_upgrade", "occupational_upgrade", "readiness_upgrade"},
}
ALLOWED_STATUSES = {"satisfied", "missing", "invalid", "insufficient_evidence", "not_applicable"}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def resolve_pointer(document: Any, pointer: str) -> Any:
    if pointer == "":
        return document
    if not pointer.startswith("/"):
        raise ValueError("JSON Pointer must start with '/'")
    value = document
    for raw in pointer[1:].split("/"):
        token = raw.replace("~1", "/").replace("~0", "~")
        if isinstance(value, list):
            try:
                value = value[int(token)]
            except (ValueError, IndexError) as exc:
                raise ValueError(f"invalid list token {token!r}") from exc
        elif isinstance(value, dict):
            if token not in value:
                raise ValueError(f"missing object key {token!r}")
            value = value[token]
        else:
            raise ValueError(f"cannot descend through {type(value).__name__}")
    return value


def replay(manifest: dict[str, Any] | None = None, *, write: bool = True) -> dict[str, Any]:
    package = manifest if manifest is not None else json.loads(MANIFEST.read_text())
    errors: list[str] = []
    artifacts: dict[str, dict[str, Any]] = {}
    documents: dict[str, Any] = {}

    for item in package.get("artifacts", []):
        artifact_id = item.get("artifact_id")
        if artifact_id in artifacts:
            errors.append(f"duplicate artifact_id: {artifact_id}")
            continue
        path = (ROOT / item.get("path", "")).resolve()
        try:
            path.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"artifact escapes repository: {artifact_id}")
            continue
        artifacts[artifact_id] = item
        if not path.is_file():
            errors.append(f"artifact missing: {artifact_id}")
            continue
        observed_hash = sha256(path)
        if observed_hash != item.get("sha256"):
            errors.append(f"hash mismatch: {artifact_id}")
            continue
        try:
            documents[artifact_id] = json.loads(path.read_text())
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            errors.append(f"artifact is not valid JSON: {artifact_id}: {exc}")

    seen_rows: set[str] = set()
    found_requirements: dict[str, set[str]] = defaultdict(set)
    results: list[dict[str, Any]] = []
    for row in package.get("rows", []):
        row_id = row.get("row_id")
        family = row.get("family")
        requirement = row.get("requirement")
        status = row.get("coverage_status")
        row_errors: list[str] = []
        observed = None

        if row_id in seen_rows:
            row_errors.append("duplicate row_id")
        seen_rows.add(row_id)
        if family not in REQUIREMENTS:
            row_errors.append("unknown family")
        else:
            found_requirements[family].add(requirement)
            if requirement not in REQUIREMENTS[family]:
                row_errors.append("unknown requirement")
        if status not in ALLOWED_STATUSES:
            row_errors.append("invalid coverage_status")

        evidence = row.get("evidence")
        if status in {"satisfied", "invalid", "insufficient_evidence"}:
            if not isinstance(evidence, dict):
                row_errors.append("credited or evidenced row lacks evidence locator")
            else:
                artifact_id = evidence.get("artifact_id")
                if artifact_id not in documents:
                    row_errors.append("evidence artifact unavailable or failed integrity")
                else:
                    try:
                        observed = resolve_pointer(documents[artifact_id], evidence.get("pointer", ""))
                    except ValueError as exc:
                        row_errors.append(f"pointer mismatch: {exc}")
                    else:
                        if observed != row.get("expected_observation"):
                            row_errors.append("observed value differs from frozen expected observation")
        elif evidence is not None:
            row_errors.append("missing/not_applicable row must not claim evidence")

        if status in {"missing", "invalid", "insufficient_evidence", "not_applicable"} and not row.get("reason"):
            row_errors.append("non-satisfied row lacks reason")
        if status == "not_applicable" and len(row.get("reason", "")) < 20:
            row_errors.append("not_applicable rationale is not specific")

        if family == "claim_ladder" and row.get("claim_level") != "task_package":
            expected = row.get("expected_observation")
            if expected == "supported":
                row_errors.append("unsupported claim upgrade")
        if row_errors:
            errors.extend(f"{row_id}: {message}" for message in row_errors)
        results.append({
            "row_id": row_id,
            "family": family,
            "requirement": requirement,
            "coverage_status": status,
            "observed": observed,
            "integrity": "failed" if row_errors else "verified",
            "errors": row_errors,
        })

    for family, required in REQUIREMENTS.items():
        missing = required - found_requirements.get(family, set())
        extra = found_requirements.get(family, set()) - required
        if missing:
            errors.append(f"{family}: absent frozen rows: {sorted(missing)}")
        if extra:
            errors.append(f"{family}: unexpected rows: {sorted(extra)}")

    counts = Counter(row.get("coverage_status") for row in package.get("rows", []))
    family_reports = []
    for family in REQUIREMENTS:
        family_rows = [r for r in results if r["family"] == family]
        blockers = [r["row_id"] for r in family_rows if r["coverage_status"] != "satisfied"]
        family_reports.append({
            "family": family,
            "rows": len(family_rows),
            "satisfied": sum(r["coverage_status"] == "satisfied" for r in family_rows),
            "blockers": blockers,
            "promotion_ready": not blockers and all(r["integrity"] == "verified" for r in family_rows),
        })

    report = {
        "report_version": "0.1.0",
        "manifest_sha256": sha256(MANIFEST) if manifest is None else None,
        "integrity_valid": not errors,
        "errors": errors,
        "summary": {
            "families": len(REQUIREMENTS),
            "rows": len(results),
            "coverage_status_counts": dict(sorted(counts.items())),
            "promotion_ready_families": sum(item["promotion_ready"] for item in family_reports),
        },
        "family_results": family_reports,
        "rows": results,
        "promotion_decision": "blocked",
        "promotion_blockers": [
            r["row_id"] for r in results
            if r["coverage_status"] != "satisfied" or r["integrity"] != "verified"
        ],
        "claim_boundaries": {
            "professional_capability": False,
            "cross_domain_capability": False,
            "skill_treatment_effect": False,
            "real_world_safety": False,
            "deployment_readiness": False,
        },
    }
    if write:
        REPORT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Verify report is current without rewriting it")
    args = parser.parse_args()
    report = replay(write=not args.check)
    if args.check:
        if not REPORT.is_file() or json.loads(REPORT.read_text()) != report:
            print("REPORT_STALE")
            return 1
    print(json.dumps({
        "integrity_valid": report["integrity_valid"],
        "summary": report["summary"],
        "promotion_decision": report["promotion_decision"],
        "promotion_blockers": report["promotion_blockers"],
    }, indent=2))
    return 0 if report["integrity_valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
