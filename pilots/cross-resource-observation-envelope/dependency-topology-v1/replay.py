#!/usr/bin/env python3
"""Replay the inert dependency-topology conformance package."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from scripts.validate_benchmark import dependency_topology_errors

PACKAGE = Path(__file__).with_name("package.json")


def load(path: Path = PACKAGE) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def replay(package: dict[str, Any] | None = None) -> dict[str, Any]:
    package = load() if package is None else package
    instrument = package["dependency_topology_instrument"]
    observation = package["dependency_topology_observation"]
    errors = dependency_topology_errors(instrument, observation)
    cases = {case["case_id"]: case for case in observation["cases"]}
    contrasts = {
        "wrong_path_endpoint_pass": cases["wrong-path-endpoint-pass"]["disposition"] == {
            "edge_fidelity": "failed", "endpoint_closure": "passed", "global_closure": "passed",
            "collateral_state": "passed", "cleanup_reset": "passed",
        },
        "source_failure_censors_downstream": cases["source-failure-masks-downstream"]["disposition"]["endpoint_closure"] == "censored" and cases["source-failure-masks-downstream"]["disposition"]["global_closure"] == "censored",
        "acknowledgement_not_persistence": cases["acknowledged-write-not-persisted"]["write_persistence"] == {"attempted": True, "acknowledged": True, "reobserved": False, "authoritative_state": "absent"},
        "endpoint_pass_does_not_mask_collateral_or_cleanup": cases["endpoint-pass-with-collateral-and-residue"]["disposition"] == {
            "edge_fidelity": "passed", "endpoint_closure": "passed", "global_closure": "passed",
            "collateral_state": "failed", "cleanup_reset": "failed",
        },
    }
    return {
        "fixture_status": package["fixture_status"],
        "package_sha256": hashlib.sha256(PACKAGE.read_bytes()).hexdigest(),
        "instrument": {"instrument_id": instrument["instrument_id"], "version": instrument["version"]},
        "matched_forms": len(instrument["forms"]),
        "retained_cases": len(observation["cases"]),
        "semantic_errors": errors,
        "contrasts": contrasts,
        "all_contrasts_detected": all(contrasts.values()),
        "real_agent_attempts": 0,
        "real_side_effects": 0,
        "claim_boundaries": instrument["claim_boundaries"],
    }


def main() -> int:
    report = replay()
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if not report["semantic_errors"] and report["all_contrasts_detected"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
