#!/usr/bin/env python3
"""Replay the inert cross-resource envelope against the benchmark validator."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from scripts.validate_benchmark import resource_envelope_errors

PACKAGE = Path(__file__).with_name("package.json")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def replay(package: dict[str, Any] | None = None) -> dict[str, Any]:
    package = load(PACKAGE) if package is None else package
    contract = package["task_resource_envelope"]
    observed = package["trial_resource_envelope"]
    errors = resource_envelope_errors(contract, observed)
    mutations = observed["mutations"]
    planted = {
        "intentional_null_preserved": any(m["kind"] == "update" and m["before"] is not None and m["after"] is None and m["observation_status"] == "observed" for m in mutations),
        "untagged_background_write_detected": any(m["context_status"] == "untagged" and m["observation_status"] == "escaped" for m in mutations),
        "sequence_increment_recorded": any(m["kind"] == "increment" for m in mutations),
        "non_table_cache_effect_recorded": any(m["resource_id"] == "notification-cache" for m in mutations),
        "same_resource_matching_ambiguity_failed_closed": any(len(m["candidate_item_keys"]) > 1 and m["outcome"] == "insufficient_evidence" for m in observed["matches"]),
        "concurrent_parent_change_invalidated": observed["start_parent_root_sha256"] != observed["end_parent_root_sha256"] and observed["overall_disposition"] == "invalid_environment",
        "stale_dependency_incomplete_commit_rejected": observed["commit_assessment"]["stale_base"] and not observed["commit_assessment"]["dependency_closure"] and observed["commit_assessment"]["decision"] == "reject_commit",
        "failed_evaluation_retained_in_denominator": observed["attempt"] == {"status": "failed_evaluation", "disposition": "failed_attempt", "denominator_included": True},
    }
    return {
        "fixture_status": package["fixture_status"],
        "package_sha256": hashlib.sha256(PACKAGE.read_bytes()).hexdigest(),
        "observer_sha256": contract["observer"]["component"]["sha256"],
        "semantic_errors": errors,
        "planted_defects": planted,
        "all_planted_defects_detected": all(planted.values()),
        "overall_disposition": observed["overall_disposition"],
        "attempted": 1,
        "failed_attempts": 1,
        "invalid_environment_attempts": 1,
        "real_commits": 0,
        "network_side_effects": 0,
        "claim_boundaries": contract["claim_boundaries"],
    }


def main() -> int:
    report = replay()
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if not report["semantic_errors"] and report["all_planted_defects_detected"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
