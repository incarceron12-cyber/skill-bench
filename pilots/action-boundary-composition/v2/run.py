#!/usr/bin/env python3
"""v2 path wrapper around the hash-pinned v1 preflight, runner, and grader."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
PROTOCOL = HERE / "protocol.json"
EXECUTION = HERE / "execution"
V1_RUN = ROOT / "pilots/action-boundary-composition/v1/run.py"


def module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


core = module("action_boundary_v1_runner_for_v2", V1_RUN)
# The only runtime change is the destination envelope. All task materialization,
# isolation, launcher, action observer, native grading, and replay logic is reused.
core.HERE = HERE
core.PROTOCOL = PROTOCOL
core.EXECUTION = EXECUTION


def verify(require_pushed: bool = False) -> dict[str, Any]:
    protocol = core.load(PROTOCOL)
    errors = core.semantic_errors(protocol)
    commit = None
    if require_pushed:
        subprocess.run(["git", "fetch", "origin", "main"], cwd=ROOT, capture_output=True)
        remote = subprocess.run(
            ["git", "show", "origin/main:pilots/action-boundary-composition/v2/protocol.json"],
            cwd=ROOT,
            capture_output=True,
        )
        if remote.returncode or hashlib.sha256(remote.stdout).hexdigest() != core.sha(PROTOCOL):
            errors.append("protocol_not_pushed")
        else:
            commit = subprocess.check_output(["git", "rev-parse", "origin/main"], cwd=ROOT, text=True).strip()
    return {
        "passed": not errors,
        "errors": sorted(set(errors)),
        "protocol_sha256": core.sha(PROTOCOL),
        "pushed_commit": commit,
    }


def report(protocol: dict[str, Any], attempts: list[dict[str, Any]]) -> dict[str, Any]:
    value = core._v1_report(protocol, attempts)
    value["kind"] = "realistic_artifact_action_boundary_composition_v2_service_recovery"
    value["replication_provenance"] = protocol["replication_provenance"]
    return value


# Install wrapper functions into the reused module globals used by execute/preflight.
core.verify = verify
core._v1_report = core.report
core.report = report

# Public aliases make equivalence/mutation tests explicit.
semantic_errors = core.semantic_errors
public_task = core.public_task
authority = core.authority
canonical_decision = core.canonical_decision
preflight = core.preflight
execute = core.execute
replay = core.replay
grader = core.grader


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("verify", "preflight", "execute", "replay"))
    parser.add_argument("--require-pushed", action="store_true")
    args = parser.parse_args()
    value = (
        verify(args.require_pushed)
        if args.mode == "verify"
        else preflight(args.require_pushed)
        if args.mode == "preflight"
        else execute()
        if args.mode == "execute"
        else replay()
    )
    passed = value.get("passed", value.get("status") != "blocked_before_model_calls")
    print(
        json.dumps(
            {
                "mode": args.mode,
                "passed": passed,
                "errors": value.get("errors", []),
                "status": value.get("status"),
                "denominators": value.get("strict_denominators"),
                "counts": value.get("classification_counts"),
            },
            indent=2,
        )
    )
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
