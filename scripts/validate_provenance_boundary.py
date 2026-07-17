#!/usr/bin/env python3
"""Validate frozen Git evidence plus a mutable canonical-document dependency.

This boundary is intentionally narrow: immutable task, source, grader, and runtime
artifacts still use ordinary byte hashes.  Only an explicitly declared live
canonical document may evolve, and its cited semantics must remain present both
in the historical Git object and in the working-tree document. Legacy records use
shared literal anchors. Versioned locators may name different historical/live text
(for example after section renumbering), but hash and uniquely resolve each bounded
locator in its respective document.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
OID = re.compile(r"^[0-9a-f]{40}$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")


def _git(*args: str) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True)


def _safe_repo_path(value: Any) -> str | None:
    if not isinstance(value, str) or not value:
        return None
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        return None
    return path.as_posix()


def validate_record(
    record: dict[str, Any], *, expected_path: str, expected_role: str
) -> dict[str, Any]:
    """Validate one typed historical/live dependency pair, fail closed."""
    errors: list[str] = []
    if record.get("boundary_type") != "historical_snapshot_with_live_canonical":
        errors.append("invalid provenance boundary type")

    historical = record.get("historical_snapshot", {})
    live = record.get("live_dependency", {})
    historical_path = _safe_repo_path(historical.get("path"))
    live_path = _safe_repo_path(live.get("path"))
    if historical_path != expected_path or live_path != expected_path:
        errors.append(f"path substitution: expected {expected_path}")
    if live.get("semantic_role") != expected_role:
        errors.append(f"semantic role change: expected {expected_role}")

    commit = historical.get("git_commit")
    expected_blob = historical.get("git_blob")
    expected_sha = historical.get("sha256")
    anchors = live.get("required_anchors")
    locators = live.get("semantic_locators")
    if locators is None:
        if not isinstance(anchors, list) or not anchors or any(not isinstance(a, str) or not a for a in anchors):
            errors.append("live dependency requires nonempty semantic anchors")
            anchors = []
        locators = []
    else:
        anchors = []
        if not isinstance(locators, list) or not locators:
            errors.append("live dependency requires nonempty semantic locators")
            locators = []
    if not isinstance(commit, str) or not OID.fullmatch(commit):
        errors.append("historical snapshot has invalid Git commit")
    if not isinstance(expected_blob, str) or not OID.fullmatch(expected_blob):
        errors.append("historical snapshot has invalid Git blob")
    if not isinstance(expected_sha, str) or not SHA256.fullmatch(expected_sha):
        errors.append("historical snapshot has invalid SHA-256")

    historical_bytes: bytes | None = None
    observed_blob: str | None = None
    if historical_path and isinstance(commit, str) and OID.fullmatch(commit):
        commit_check = _git("cat-file", "-e", f"{commit}^{{commit}}")
        if commit_check.returncode:
            errors.append(f"absent historical Git commit: {commit}")
        else:
            blob_proc = _git("rev-parse", f"{commit}:{historical_path}")
            show_proc = _git("show", f"{commit}:{historical_path}")
            if blob_proc.returncode or show_proc.returncode:
                errors.append(f"absent historical object: {commit}:{historical_path}")
            else:
                observed_blob = blob_proc.stdout.decode().strip()
                historical_bytes = show_proc.stdout
                if observed_blob != expected_blob:
                    errors.append(f"historical Git blob mismatch: {historical_path}")
                if hashlib.sha256(historical_bytes).hexdigest() != expected_sha:
                    errors.append(f"historical SHA-256 mismatch: {historical_path}")

    live_file = ROOT / live_path if live_path else None
    live_text: str | None = None
    if live_file is None or not live_file.is_file():
        errors.append(f"missing live dependency: {live_path or '<invalid-path>'}")
    else:
        try:
            live_text = live_file.read_text()
        except UnicodeDecodeError:
            errors.append(f"live dependency is not UTF-8 text: {live_path}")

    historical_text: str | None = None
    if historical_bytes is not None:
        try:
            historical_text = historical_bytes.decode("utf-8")
        except UnicodeDecodeError:
            errors.append(f"historical dependency is not UTF-8 text: {historical_path}")
    for anchor in anchors:
        if historical_text is not None and anchor not in historical_text:
            errors.append(f"missing historical semantic anchor: {anchor}")
        if live_text is not None and anchor not in live_text:
            errors.append(f"missing live semantic anchor: {anchor}")

    semantic_ids: set[str] = set()
    for locator in locators:
        if not isinstance(locator, dict):
            errors.append("semantic locator must be an object")
            continue
        semantic_id = locator.get("semantic_id")
        historical_locator = locator.get("historical_text")
        live_locator = locator.get("live_text")
        historical_locator_sha = locator.get("historical_text_sha256")
        live_locator_sha = locator.get("live_text_sha256")
        if not isinstance(semantic_id, str) or not semantic_id or semantic_id in semantic_ids:
            errors.append("semantic locator ids must be unique and nonempty")
        else:
            semantic_ids.add(semantic_id)
        for label, text, expected_text_sha, document in (
            ("historical", historical_locator, historical_locator_sha, historical_text),
            ("live", live_locator, live_locator_sha, live_text),
        ):
            if not isinstance(text, str) or not text:
                errors.append(f"{semantic_id or '<invalid>'}: missing {label} semantic locator text")
                continue
            if not isinstance(expected_text_sha, str) or not SHA256.fullmatch(expected_text_sha):
                errors.append(f"{semantic_id or '<invalid>'}: invalid {label} semantic locator hash")
            elif hashlib.sha256(text.encode("utf-8")).hexdigest() != expected_text_sha:
                errors.append(f"{semantic_id or '<invalid>'}: {label} semantic locator hash mismatch")
            if document is not None:
                count = document.count(text)
                if count == 0:
                    errors.append(f"{semantic_id or '<invalid>'}: missing {label} semantic locator")
                elif count != 1:
                    errors.append(f"{semantic_id or '<invalid>'}: ambiguous {label} semantic locator")

    return {
        "valid": not errors,
        "errors": errors,
        "path": expected_path,
        "semantic_role": expected_role,
        "historical_commit": commit,
        "historical_blob": observed_blob,
        "historical_sha256": expected_sha,
        "live_anchor_count": len(anchors) + len(locators),
    }


def load_and_validate(path: Path, *, expected_path: str, expected_role: str) -> dict[str, Any]:
    try:
        record = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        return {"valid": False, "errors": [f"cannot load provenance boundary: {exc}"]}
    return validate_record(record, expected_path=expected_path, expected_role=expected_role)


def validate_historical_contract_reference(
    reference: dict[str, Any],
    boundary_path: Path,
    *,
    expected_path: str,
    expected_role: str,
) -> dict[str, Any]:
    """Resolve one legacy path/hash pin through an immutable Git snapshot.

    Historical packages keep their original ``path`` and ``sha256`` bytes. The
    boundary supplies the matching commit/blob identity and narrowly bounded live
    semantics. Requiring the package hash to equal the historical snapshot hash
    prevents a mutable-current-file refresh from reidentifying an old dependency.
    """
    errors: list[str] = []
    try:
        boundary = json.loads(boundary_path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        return {"valid": False, "errors": [f"cannot load provenance boundary: {exc}"]}

    report = validate_record(
        boundary, expected_path=expected_path, expected_role=expected_role
    )
    errors.extend(report["errors"])
    historical = boundary.get("historical_snapshot", {})
    if reference.get("path") != expected_path:
        errors.append(f"historical contract path substitution: expected {expected_path}")
    if historical.get("path") != reference.get("path"):
        errors.append("historical contract reference path differs from boundary snapshot")
    if historical.get("sha256") != reference.get("sha256"):
        errors.append("historical contract reference hash differs from boundary snapshot")
    return {"valid": not errors, "errors": errors, "boundary": report}


def validate_frozen_component_set(
    protocol_path: Path,
    boundary_path: Path,
    *,
    expected_path: str,
    expected_role: str,
) -> dict[str, Any]:
    """Verify a legacy frozen component list without rewriting its historical bytes.

    The one declared canonical document is checked through ``validate_record``.
    Every other component remains pinned to its working-tree SHA-256, so this
    function cannot weaken task/source/grader/runtime integrity.
    """
    errors: list[str] = []
    try:
        protocol = json.loads(protocol_path.read_text())
        boundary = json.loads(boundary_path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        return {"valid": False, "errors": [f"cannot load frozen provenance inputs: {exc}"]}

    report = validate_record(boundary, expected_path=expected_path, expected_role=expected_role)
    errors.extend(report["errors"])
    components = protocol.get("frozen_components", [])
    matches = [item for item in components if item.get("path") == expected_path]
    if len(matches) != 1:
        errors.append("live dependency must match exactly one frozen component")
    elif matches[0].get("sha256") != boundary.get("historical_snapshot", {}).get("sha256"):
        errors.append("frozen component hash differs from historical snapshot hash")

    for item in components:
        item_path = _safe_repo_path(item.get("path"))
        if item_path == expected_path:
            continue
        candidate = ROOT / item_path if item_path else None
        if candidate is None or not candidate.is_file():
            errors.append(f"missing immutable frozen component: {item.get('path')}")
        elif hashlib.sha256(candidate.read_bytes()).hexdigest() != item.get("sha256"):
            errors.append(f"immutable frozen component drift: {item_path}")
    return {"valid": not errors, "errors": errors, "boundary": report}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("record", type=Path)
    parser.add_argument("--expected-path", required=True)
    parser.add_argument("--expected-role", required=True)
    args = parser.parse_args()
    report = load_and_validate(
        args.record, expected_path=args.expected_path, expected_role=args.expected_role
    )
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
