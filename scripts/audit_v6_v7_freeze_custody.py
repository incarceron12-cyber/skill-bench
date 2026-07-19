#!/usr/bin/env python3
"""Reconstruct and adjudicate the v6/v7 freeze-custody history from Git.

This audit is deliberately read-only with respect to every pilot and execution file.
It distinguishes the commit-bound audited snapshots from the retrospective repair at
0cb5bea and fails closed if a changed frozen binding is omitted from the report.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports/validation/2026-07-19-pretask-procedure-v6-v7-custody-adjudication.json"

FREEZE_AUDIT_COMMIT = "0b7f9306ec6c3a18d4f5bba98af3eabd2ea7f200"
EXECUTION_SOURCE_COMMIT = "a6d06f988dcdd56e6e3cb46845c652b9f1ace3e3"
EXECUTION_AUDIT_COMMIT = "b025bf2c0ae6ce00312c3740a4cca5435e829574"
PRE_REPAIR_COMMIT = "79bb86a1b0bacede1209695ab565234fc1a64277"
REPAIR_COMMIT = "0cb5bea98ca3f1cbb698a04bc4b285a7fe5d69d1"
V6_PREFIX = "pilots/pretask-procedure-transfer-v6/"
V7_MANIFEST = "pilots/pretask-procedure-transfer-v7/freeze-manifest.json"
EXECUTION_PREFIX = "pilots/pretask-procedure-transfer-v7-execution/"
CLAIM_CEILING = {
    "agent_capability": False,
    "expert_provenance": False,
    "production_fitness": False,
    "professional_validity": False,
    "readiness": False,
    "transfer": False,
    "utility": False,
}


def git(*args: str, text: bool = False) -> bytes | str:
    result = subprocess.run(
        ["git", *args], cwd=ROOT, check=True, capture_output=True, text=text
    )
    return result.stdout


def blob(commit: str, path: str) -> bytes:
    return git("show", f"{commit}:{path}")  # type: ignore[return-value]


def identity(commit: str, path: str) -> dict[str, Any]:
    data = blob(commit, path)
    return {
        "bytes": len(data),
        "git_blob": str(git("rev-parse", f"{commit}:{path}", text=True)).strip(),
        "sha256": hashlib.sha256(data).hexdigest(),
    }


def changed_paths(old: str, new: str, prefix: str | None = None) -> list[str]:
    args = ["diff", "--name-only", old, new]
    if prefix:
        args.extend(["--", prefix])
    output = str(git(*args, text=True))
    return sorted(line for line in output.splitlines() if line)


def manifest_at(commit: str) -> dict[str, Any]:
    return json.loads(blob(commit, V7_MANIFEST))


def audit_manifest_bindings(commit: str) -> dict[str, Any]:
    manifest = manifest_at(commit)
    rows: list[dict[str, Any]] = []
    for kind, key in (("component", "components"), ("external", "external_immutable_bindings")):
        for binding in manifest[key]:
            observed = identity(commit, binding["path"])
            rows.append(
                {
                    "kind": kind,
                    "path": binding["path"],
                    "declared_bytes": binding["bytes"],
                    "declared_sha256": binding["sha256"],
                    "observed_bytes": observed["bytes"],
                    "observed_sha256": observed["sha256"],
                    "match": binding["bytes"] == observed["bytes"]
                    and binding["sha256"] == observed["sha256"],
                }
            )
    mismatches = [row["path"] for row in rows if not row["match"]]
    return {
        "commit": commit,
        "component_bindings_checked": sum(row["kind"] == "component" for row in rows),
        "external_bindings_checked": sum(row["kind"] == "external" for row in rows),
        "mismatches": mismatches,
        "all_bindings_match": not mismatches,
    }


def tree_identity(commit: str, path: str) -> str:
    return str(git("rev-parse", f"{commit}:{path}", text=True)).strip()


def build_report() -> dict[str, Any]:
    if str(git("rev-parse", f"{REPAIR_COMMIT}^", text=True)).strip() != PRE_REPAIR_COMMIT:
        raise AssertionError("declared pre-repair commit is not the repair parent")

    all_repair_paths = changed_paths(PRE_REPAIR_COMMIT, REPAIR_COMMIT)
    changed_v6 = changed_paths(PRE_REPAIR_COMMIT, REPAIR_COMMIT, V6_PREFIX)
    audited_manifest = manifest_at(FREEZE_AUDIT_COMMIT)
    execution_manifest = manifest_at(EXECUTION_SOURCE_COMMIT)
    post_manifest = manifest_at(REPAIR_COMMIT)

    audited_external = {row["path"]: row for row in audited_manifest["external_immutable_bindings"]}
    execution_external = {row["path"]: row for row in execution_manifest["external_immutable_bindings"]}
    post_external = {row["path"]: row for row in post_manifest["external_immutable_bindings"]}
    bound_changed_v6 = sorted(path for path in changed_v6 if path in audited_external)
    unbound_changed_v6 = sorted(path for path in changed_v6 if path not in audited_external)

    mutations = []
    for path in changed_v6:
        before = identity(PRE_REPAIR_COMMIT, path)
        after = identity(REPAIR_COMMIT, path)
        mutations.append(
            {
                "path": path,
                "was_v7_external_binding": path in audited_external,
                "pre_repair": before,
                "post_repair": after,
                "audited_v7_declared": {
                    "bytes": audited_external[path]["bytes"],
                    "sha256": audited_external[path]["sha256"],
                }
                if path in audited_external
                else None,
                "post_repair_v7_declared": {
                    "bytes": post_external[path]["bytes"],
                    "sha256": post_external[path]["sha256"],
                }
                if path in post_external
                else None,
            }
        )

    manifest_binding_changes = []
    for path in sorted(set(audited_external) | set(post_external)):
        old = audited_external.get(path)
        new = post_external.get(path)
        if old != new:
            manifest_binding_changes.append(
                {
                    "path": path,
                    "audited": old,
                    "post_repair": new,
                }
            )

    freeze_binding_audit = audit_manifest_bindings(FREEZE_AUDIT_COMMIT)
    execution_binding_audit = audit_manifest_bindings(EXECUTION_SOURCE_COMMIT)

    execution_changed_by_repair = changed_paths(
        PRE_REPAIR_COMMIT, REPAIR_COMMIT, EXECUTION_PREFIX
    )
    v7_changes_by_repair = changed_paths(
        PRE_REPAIR_COMMIT, REPAIR_COMMIT, "pilots/pretask-procedure-transfer-v7/"
    )

    expected_repair_paths = sorted(
        changed_v6
        + [V7_MANIFEST, "data/work_queue.json", "tests/test_pretask_procedure_transfer_v6.py"]
    )
    if all_repair_paths != expected_repair_paths:
        raise AssertionError(
            f"repair path inventory drift: expected {expected_repair_paths}, got {all_repair_paths}"
        )
    if set(bound_changed_v6) != set(changed_v6):
        raise AssertionError(f"changed v6 files omitted from v7 bindings: {unbound_changed_v6}")
    if sorted(row["path"] for row in manifest_binding_changes) != bound_changed_v6:
        raise AssertionError("refreshed v7 manifest changes do not exactly cover changed v6 bindings")
    if not freeze_binding_audit["all_bindings_match"] or not execution_binding_audit["all_bindings_match"]:
        raise AssertionError("historical v7 manifest does not close at an audited source commit")
    if v7_changes_by_repair != [V7_MANIFEST]:
        raise AssertionError(f"repair changed unexpected v7 files: {v7_changes_by_repair}")
    if execution_changed_by_repair:
        raise AssertionError(f"repair changed execution evidence: {execution_changed_by_repair}")

    original_manifest_same_at_execution = blob(FREEZE_AUDIT_COMMIT, V7_MANIFEST) == blob(
        EXECUTION_SOURCE_COMMIT, V7_MANIFEST
    )
    execution_tree_same_through_repair = tree_identity(
        EXECUTION_SOURCE_COMMIT, EXECUTION_PREFIX.rstrip("/")
    ) == tree_identity(REPAIR_COMMIT, EXECUTION_PREFIX.rstrip("/"))

    return {
        "adjudication_id": "pretask-procedure-transfer-v6-v7-freeze-custody-after-retrospective-repair",
        "audit_kind": "append_only_commit_reconstruction_and_custody_adjudication",
        "status": "PASS_WITH_HISTORICAL_CUSTODY_BREACH",
        "scope": "Git-only reconstruction; no model, provider, executor, oracle, checker, canary, preflight, pilot, or execution row was run or modified.",
        "commits": {
            "independent_freeze_audit_source": FREEZE_AUDIT_COMMIT,
            "execution_source": EXECUTION_SOURCE_COMMIT,
            "execution_independent_audit_record": EXECUTION_AUDIT_COMMIT,
            "pre_repair_parent": PRE_REPAIR_COMMIT,
            "retrospective_repair": REPAIR_COMMIT,
        },
        "attempt_ledger": {
            "canary": 0,
            "checker": 0,
            "executor": 0,
            "model": 0,
            "oracle": 0,
            "provider": 0,
            "repair_or_retry_row": 0,
        },
        "claim_ceiling": CLAIM_CEILING,
        "historical_binding_recomputation": {
            "independent_freeze_audit_source": freeze_binding_audit,
            "execution_source": execution_binding_audit,
            "original_manifest_byte_identical_at_freeze_and_execution_sources": original_manifest_same_at_execution,
        },
        "retrospective_mutation": {
            "all_paths_changed_by_repair_commit": all_repair_paths,
            "changed_v6_frozen_paths": changed_v6,
            "changed_v6_binding_count": len(bound_changed_v6),
            "unbound_changed_v6_paths": unbound_changed_v6,
            "v6_binding_mutations": mutations,
            "v7_manifest": {
                "path": V7_MANIFEST,
                "pre_repair": identity(PRE_REPAIR_COMMIT, V7_MANIFEST),
                "post_repair": identity(REPAIR_COMMIT, V7_MANIFEST),
                "refreshed_external_bindings": manifest_binding_changes,
            },
            "v7_non_manifest_paths_changed": [
                path for path in v7_changes_by_repair if path != V7_MANIFEST
            ],
            "execution_paths_changed": execution_changed_by_repair,
        },
        "state_adjudication": {
            "pre_repair_v6": {
                "commit": PRE_REPAIR_COMMIT,
                "classification": "frozen_failed_preexecution_state",
                "canary": "FAIL",
                "preflight": "FAIL",
                "interpretation": "The exact state bound by the v7 freeze and execution source commits; it remains recoverable and hash-verifiable in Git.",
            },
            "post_repair_v6": {
                "commit": REPAIR_COMMIT,
                "classification": "post_hoc_infrastructure_repair_not_a_new_prospective_instrument",
                "canary": "PASS",
                "preflight": "PASS",
                "interpretation": "A later repaired HEAD state. It must not replace, rescore, or be described as the frozen v6 state used by v7.",
            },
            "head_worktree_preserves_exact_failed_v6_bytes": False,
            "git_history_preserves_exact_failed_v6_bytes": True,
            "audited_v7_manifest_was_rewritten_after_execution": True,
        },
        "execution_closure": {
            "decision": "REMAINS_HASH_VERIFIABLE_AT_COMMIT_BOUND_SNAPSHOTS",
            "historical_manifest_closes_at_freeze_source": freeze_binding_audit["all_bindings_match"],
            "historical_manifest_closes_at_execution_source": execution_binding_audit["all_bindings_match"],
            "original_manifest_same_at_freeze_and_execution_sources": original_manifest_same_at_execution,
            "v7_task_treatment_files_changed_by_repair": False,
            "v7_execution_package_changed_by_repair": bool(execution_changed_by_repair),
            "execution_tree_same_from_source_through_repair": execution_tree_same_through_repair,
            "qualification": "Closure is licensed only by the immutable Git snapshots and retained execution evidence, not by treating the refreshed HEAD manifest as the manifest independently audited or used at execution.",
        },
        "preservation_claim_adjudication": {
            "licensed": [
                "At commits 0b7f930 and a6d06f9, v7 bound and verified the exact failed v6 state then present.",
                "The original failed v6 bytes and original v7 manifest remain recoverable and hash-verifiable from Git history.",
                "The 32-row v7 task/treatment/execution closure remains commit-bound and hash-verifiable because the repair changed no v7 task/treatment byte or execution-package byte.",
            ],
            "not_licensed": [
                "Current HEAD preserves the exact failed v6 bytes in the pilot directory.",
                "Current HEAD's v7 manifest is byte-identical to the independently audited or execution-time manifest.",
                "The v6 repair was prospective v7 evidence or retroactively converted frozen v6 failure into a pass.",
                "The lifecycle completed without any later rewrite of prior frozen evidence.",
            ],
        },
        "required_claim_limits": "No transfer, capability, utility, expert, professional, production, or readiness claim follows from either the repair or this custody audit.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="compare reconstruction with committed report")
    args = parser.parse_args()
    report = build_report()
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.check:
        if not REPORT.exists() or REPORT.read_text(encoding="utf-8") != rendered:
            raise SystemExit("custody report is missing or differs from Git reconstruction")
        print("PASS: custody report exactly matches Git reconstruction")
    else:
        REPORT.parent.mkdir(parents=True, exist_ok=True)
        REPORT.write_text(rendered, encoding="utf-8")
        print(f"wrote {REPORT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
