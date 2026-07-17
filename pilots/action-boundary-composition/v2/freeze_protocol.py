#!/usr/bin/env python3
"""Freeze the prospective v2 service-recovery replication without task tuning."""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
V1 = ROOT / "pilots/action-boundary-composition/v1"


def module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


v1_builder = module("action_boundary_v1_builder_for_v2", V1 / "freeze_protocol.py")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def authority_record(form: str, condition: str) -> dict[str, Any]:
    """Exact v1 authority semantics; exposed for the reused v1 runner."""
    return v1_builder.authority_record(form, condition)


def public_task(form: str) -> str:
    """Exact v1 public task; exposed for the reused v1 runner."""
    return v1_builder.public_task(form)


def build() -> dict[str, Any]:
    protocol = copy.deepcopy(v1_builder.build())
    protocol.update(
        {
            "version": "2.0.0",
            "status": "prospectively_frozen_service_recovery_replication",
            "useful_completion": "All six unchanged intended cells pass zero-call gates and execute once after a pushed freeze, yielding interpretable artifact/state evidence or an exact fail-closed service/environment diagnosis.",
            "replication_provenance": {
                "design_source": "pilots/action-boundary-composition/v1/protocol.json",
                "design_source_sha256": sha(V1 / "protocol.json"),
                "prior_campaign": "pilots/action-boundary-composition/v1/execution/study-report.json",
                "prior_campaign_sha256": sha(V1 / "execution/study-report.json"),
                "prior_service_valid": 0,
                "later_service_evidence": "pilots/analytical-hypothesis-lifecycle-v2/execution/summary.json",
                "later_service_evidence_sha256": sha(ROOT / "pilots/analytical-hypothesis-lifecycle-v2/execution/summary.json"),
                "later_service_valid": 8,
                "outcome_tuning": False,
                "task_rubric_expected_outcome_changes": [],
                "transport_change": "A v2 path wrapper reuses the frozen v1 builder, runner, grader, and launcher; only replication paths, pushed-protocol lookup, and report identity differ.",
            },
            "implementation_components": [
                {"path": path, "sha256": sha(ROOT / path)}
                for path in [
                    "pilots/action-boundary-composition/v1/freeze_protocol.py",
                    "pilots/action-boundary-composition/v1/grade.py",
                    "pilots/action-boundary-composition/v1/run.py",
                    "pilots/configured-artifact-revision/launcher.py",
                    "pilots/action-boundary-composition/v2/freeze_protocol.py",
                    "pilots/action-boundary-composition/v2/run.py",
                ]
            ],
        }
    )
    return protocol


if __name__ == "__main__":
    path = HERE / "protocol.json"
    path.write_text(json.dumps(build(), indent=2, sort_keys=True) + "\n")
    print(sha(path))
