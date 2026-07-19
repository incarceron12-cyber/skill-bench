#!/usr/bin/env python3
"""Validate commit-bound, append-only custody for benchmark freezes.

The validator reads only immutable Git objects. A live path is never allowed to
re-identify an audited freeze. Repairs become separately identified successors,
and execution closure must resolve the exact manifest and bindings of the freeze
that authorized execution.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas/freeze-custody.schema.json"


def _git(*args: str) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True)


def _git_text(*args: str) -> str | None:
    proc = _git(*args)
    return proc.stdout.decode().strip() if proc.returncode == 0 else None


def _object(commit: str, path: str) -> tuple[str, str, bytes | None] | None:
    oid = _git_text("rev-parse", f"{commit}:{path}")
    if oid is None:
        return None
    kind = _git_text("cat-file", "-t", oid)
    if kind is None:
        return None
    data = None
    if kind == "blob":
        proc = _git("show", f"{commit}:{path}")
        if proc.returncode:
            return None
        data = proc.stdout
    return oid, kind, data


def _is_ancestor(older: str, newer: str) -> bool:
    return _git("merge-base", "--is-ancestor", older, newer).returncode == 0


def _pointer(document: Any, pointer: str) -> Any:
    value = document
    for token in pointer.lstrip("/").split("/"):
        token = token.replace("~1", "/").replace("~0", "~")
        if isinstance(value, list):
            value = value[int(token)]
        elif isinstance(value, dict):
            value = value[token]
        else:
            raise KeyError(pointer)
    return value


def _binding_map(freeze: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {row["path"]: row for row in freeze.get("bindings", [])}


def validate_record(record: dict[str, Any]) -> dict[str, Any]:
    """Return a fail-closed semantic validation report."""
    errors: list[str] = []
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    for error in Draft202012Validator(schema).iter_errors(record):
        location = "/".join(str(piece) for piece in error.absolute_path) or "<root>"
        errors.append(f"schema {location}: {error.message}")
    if errors:
        return {"valid": False, "errors": errors, "freeze_count": 0, "closure_count": 0}

    freezes = record["freezes"]
    freeze_by_id = {freeze["freeze_id"]: freeze for freeze in freezes}
    if len(freeze_by_id) != len(freezes):
        errors.append("freeze ids must be unique")
    versions = [freeze["instrument_version"] for freeze in freezes]
    if len(set(versions)) != len(versions):
        errors.append("instrument versions must be unique; repair requires a new version")

    adjudications = record["adjudications"]
    adjudication_by_id = {row["adjudication_id"]: row for row in adjudications}
    if len(adjudication_by_id) != len(adjudications):
        errors.append("adjudication ids must be unique")

    for freeze in freezes:
        freeze_id = freeze["freeze_id"]
        snapshot = freeze["snapshot"]
        commit = snapshot["git_commit"]
        commit_exists = _git("cat-file", "-e", f"{commit}^{{commit}}").returncode == 0
        if not commit_exists:
            errors.append(f"{freeze_id}: absent snapshot commit {commit}")
            continue

        root = _object(commit, snapshot["root_path"])
        if root is None or root[1] != "tree":
            errors.append(f"{freeze_id}: snapshot root is absent or not a tree")
        elif root[0] != snapshot["git_tree"]:
            errors.append(f"{freeze_id}: snapshot tree identity mismatch")

        paths = [row["path"] for row in freeze["bindings"]]
        if len(paths) != len(set(paths)):
            errors.append(f"{freeze_id}: binding paths must be unique")
        manifests = [row for row in freeze["bindings"] if row["role"] == "manifest"]
        if len(manifests) != 1:
            errors.append(f"{freeze_id}: exactly one manifest binding is required")

        for binding in freeze["bindings"]:
            path = binding["path"]
            observed = _object(commit, path)
            if observed is None:
                errors.append(f"{freeze_id}: absent frozen object {path}")
                continue
            oid, kind, data = observed
            if oid != binding["git_oid"]:
                errors.append(f"{freeze_id}: frozen Git object drift: {path}")
            if kind != binding["object_type"]:
                errors.append(f"{freeze_id}: frozen object type mismatch: {path}")
            if data is not None:
                if len(data) != binding.get("bytes"):
                    errors.append(f"{freeze_id}: frozen byte-size drift: {path}")
                if hashlib.sha256(data).hexdigest() != binding.get("sha256"):
                    errors.append(f"{freeze_id}: frozen SHA-256 drift: {path}")

        binding_paths = set(paths)
        gate_ids: set[str] = set()
        for gate in freeze["observed_gate_states"]:
            gate_id = gate["gate_id"]
            if gate_id in gate_ids:
                errors.append(f"{freeze_id}: duplicate gate id {gate_id}")
            gate_ids.add(gate_id)
            evidence_path = gate["evidence_path"]
            if evidence_path not in binding_paths:
                errors.append(f"{freeze_id}: gate evidence is not a frozen binding: {evidence_path}")
                continue
            observed = _object(commit, evidence_path)
            if observed is None or observed[2] is None:
                errors.append(f"{freeze_id}: gate evidence is not an available blob: {evidence_path}")
                continue
            try:
                evidence = json.loads(observed[2])
                historical_outcome = _pointer(evidence, gate["json_pointer"])
            except (json.JSONDecodeError, KeyError, IndexError, ValueError, TypeError):
                errors.append(f"{freeze_id}: gate evidence locator does not resolve: {gate_id}")
                continue
            normalized = str(historical_outcome).upper()
            if normalized != gate["outcome"]:
                errors.append(
                    f"{freeze_id}: gate-state replacement: {gate_id} declares "
                    f"{gate['outcome']} but historical evidence says {normalized}"
                )

    for freeze in freezes:
        predecessor_id = freeze.get("predecessor_freeze_id")
        if not predecessor_id:
            continue
        freeze_id = freeze["freeze_id"]
        predecessor = freeze_by_id.get(predecessor_id)
        if predecessor is None:
            errors.append(f"{freeze_id}: missing predecessor freeze {predecessor_id}")
            continue
        if predecessor_id == freeze_id:
            errors.append(f"{freeze_id}: a freeze cannot supersede itself")
        old_commit = predecessor["snapshot"]["git_commit"]
        new_commit = freeze["snapshot"]["git_commit"]
        if not _is_ancestor(old_commit, new_commit) or old_commit == new_commit:
            errors.append(f"{freeze_id}: successor snapshot must descend from a distinct parent snapshot")

        adjudication_id = freeze["supersession_adjudication_id"]
        adjudication = adjudication_by_id.get(adjudication_id)
        if adjudication is None:
            errors.append(f"{freeze_id}: missing supersession adjudication {adjudication_id}")
            continue
        if adjudication["subject_freeze_id"] != predecessor_id:
            errors.append(f"{freeze_id}: adjudication subject is not its predecessor")
        if adjudication["successor_freeze_id"] != freeze_id:
            errors.append(f"{freeze_id}: adjudication does not point to this successor")
        if adjudication["event_commit"] != new_commit:
            errors.append(f"{freeze_id}: adjudication event is not bound to successor commit")

        old_bindings = _binding_map(predecessor)
        changed: list[str] = []
        for path, old_binding in old_bindings.items():
            observed = _object(new_commit, path)
            if observed is None or observed[0] != old_binding["git_oid"]:
                changed.append(path)
        if sorted(adjudication["changed_bound_paths"]) != sorted(changed):
            errors.append(
                f"{freeze_id}: omitted or extra changed bindings; expected {sorted(changed)}"
            )
        successor_bindings = _binding_map(freeze)
        if set(successor_bindings) != set(old_bindings):
            errors.append(f"{freeze_id}: compact successor must preserve the predecessor binding inventory")
        for path in changed:
            if path in successor_bindings and successor_bindings[path]["git_oid"] == old_bindings[path]["git_oid"]:
                errors.append(f"{freeze_id}: changed binding was not re-identified in successor: {path}")

    for adjudication in adjudications:
        subject = freeze_by_id.get(adjudication["subject_freeze_id"])
        if subject is None:
            errors.append(f"{adjudication['adjudication_id']}: unknown subject freeze")
            continue
        if not _is_ancestor(subject["snapshot"]["git_commit"], adjudication["event_commit"]):
            errors.append(f"{adjudication['adjudication_id']}: event predates subject snapshot")
        successor_id = adjudication["successor_freeze_id"]
        if successor_id is not None and successor_id not in freeze_by_id:
            errors.append(f"{adjudication['adjudication_id']}: unknown successor freeze")

    closure_ids: set[str] = set()
    for closure in record["execution_closures"]:
        closure_id = closure["execution_id"]
        if closure_id in closure_ids:
            errors.append(f"duplicate execution closure id {closure_id}")
        closure_ids.add(closure_id)
        freeze = freeze_by_id.get(closure["freeze_id"])
        if freeze is None:
            errors.append(f"{closure_id}: unknown freeze")
            continue
        freeze_commit = freeze["snapshot"]["git_commit"]
        source_commit = closure["source_commit"]
        if not _is_ancestor(freeze_commit, source_commit):
            errors.append(f"{closure_id}: execution source does not descend from freeze snapshot")
        manifest = next((row for row in freeze["bindings"] if row["role"] == "manifest"), None)
        if manifest is None:
            continue
        if closure["manifest_path"] != manifest["path"] or closure["manifest_git_blob"] != manifest["git_oid"]:
            errors.append(f"{closure_id}: execution closure uses a post-hoc or different manifest")
        observed_manifest = _object(source_commit, closure["manifest_path"])
        if observed_manifest is None or observed_manifest[0] != manifest["git_oid"]:
            errors.append(f"{closure_id}: frozen manifest did not survive to execution source")
        for path, binding in _binding_map(freeze).items():
            observed = _object(source_commit, path)
            if observed is None or observed[0] != binding["git_oid"]:
                errors.append(f"{closure_id}: frozen binding changed before execution: {path}")
        execution_root = _object(source_commit, closure["execution_root_path"])
        if execution_root is None or execution_root[1] != "tree":
            errors.append(f"{closure_id}: execution root is absent or not a tree")
        elif execution_root[0] != closure["execution_git_tree"]:
            errors.append(f"{closure_id}: execution tree identity mismatch")

    return {
        "valid": not errors,
        "errors": errors,
        "freeze_count": len(freezes),
        "adjudication_count": len(adjudications),
        "closure_count": len(record["execution_closures"]),
    }


def validate_file(path: Path) -> dict[str, Any]:
    try:
        record = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {"valid": False, "errors": [f"cannot load custody record: {exc}"]}
    return validate_record(record)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", type=Path)
    args = parser.parse_args()
    report = validate_file(args.record)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
