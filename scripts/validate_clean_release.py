#!/usr/bin/env python3
"""Fail-closed clean-release validation over retained, zero-call pilot packages."""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas/clean-release-manifest.schema.json"
CLAIMS = {
    "agent_capability", "professional_validity", "production_safety",
    "production_fitness", "public_release_readiness", "cross_domain_generalization",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def safe_path(root: Path, text: str) -> Path | None:
    candidate = (root / text).resolve()
    try:
        candidate.relative_to(root.resolve())
    except ValueError:
        return None
    return candidate


def pointer(document: Any, locator: str) -> Any:
    value = document
    for raw in locator[1:].split("/"):
        token = raw.replace("~1", "/").replace("~0", "~")
        value = value[int(token)] if isinstance(value, list) else value[token]
    return value


def file_errors(spec: dict[str, Any], label: str, root: Path) -> list[str]:
    path = safe_path(root, spec.get("path", ""))
    if path is None:
        return [f"{label}: path escapes release root"]
    if not path.is_file():
        return [f"{label}: missing file {spec.get('path')}"]
    actual = sha256(path)
    return [] if actual == spec.get("sha256") else [f"{label}: stale hash for {spec.get('path')}"]


def semantic_errors(manifest: dict[str, Any], *, root: Path = ROOT, check_paths: bool = True) -> list[str]:
    errors: list[str] = []
    try:
        jsonschema.Draft202012Validator(load(SCHEMA)).validate(manifest)
    except jsonschema.ValidationError as exc:
        errors.append(f"schema: {exc.json_path}: {exc.message}")
        return errors

    aggregation = dict(manifest["aggregation"])
    declared_hash = aggregation.pop("spec_sha256")
    actual_aggregation_hash = canonical_hash(aggregation)
    if declared_hash != actual_aggregation_hash:
        errors.append("aggregation specification hash mismatch")

    packages = manifest["packages"]
    work_shapes = {item["work_shape"] for item in packages}
    if len(work_shapes) < 2:
        errors.append("release must retain at least two materially different work shapes")

    identity_groups = {
        "release item": [item["release_item_id"] for item in packages],
        "package": [item["package_id"] for item in packages],
        "task": [task for item in packages for task in item["task_ids"]],
        "component": [component["component_id"] for item in packages for component in item["components"]],
        "control": [control["control_id"] for item in packages for control in item["controls"]],
    }
    for label, values in identity_groups.items():
        if len(values) != len(set(values)):
            errors.append(f"duplicate {label} identity")

    if check_paths:
        for index, evidence in enumerate(manifest["evidence_basis"]):
            errors.extend(file_errors(evidence, f"evidence_basis[{index}]", root))

    for package in packages:
        pid = package["package_id"]
        if package["aggregation_id"] != aggregation["aggregation_id"] or package["aggregation_spec_sha256"] != declared_hash:
            errors.append(f"{pid}: conflicting aggregation identity")
        if set(package["claim_ceiling"]) != CLAIMS or any(package["claim_ceiling"].values()):
            errors.append(f"{pid}: claim ceiling upgrade")
        if check_paths:
            errors.extend(file_errors(package["redistribution"]["evidence"], f"{pid}/rights", root))

        components = {item["component_id"]: item for item in package["components"]}
        component_paths = {item["path"]: item for item in package["components"]}
        for component in package["components"]:
            cid = component["component_id"]
            if check_paths:
                component_file_errors = file_errors(component, f"{pid}/{cid}", root)
                errors.extend(component_file_errors)
                if component_file_errors:
                    continue
                path = safe_path(root, component["path"])
                assert path is not None
                try:
                    if component["compile_check"] == "python_compile":
                        if component["language"] != "python":
                            raise ValueError("python_compile requires language=python")
                        compile(path.read_bytes(), component["path"], "exec")
                    elif component["compile_check"] == "json_parse":
                        if component["language"] != "json":
                            raise ValueError("json_parse requires language=json")
                        load(path)
                    elif component["language"] != "markdown":
                        raise ValueError("not_executable is reserved for markdown rights/design evidence")
                except (SyntaxError, UnicodeError, ValueError, json.JSONDecodeError) as exc:
                    errors.append(f"{pid}/{cid}: compile check failed: {exc}")

        containment = package.get("containment", {})
        if set(containment) != {"status", "untrusted_execution_allowed", "network", "filesystem", "process_resource_boundary"}:
            errors.append(f"{pid}: undeclared containment boundary")
        if containment.get("untrusted_execution_allowed") is not False:
            errors.append(f"{pid}: untrusted execution is forbidden")

        for control in package["controls"]:
            control_id = control["control_id"]
            runner = components.get(control["runner_component_id"])
            if runner is None or runner.get("compile_check") != "python_compile":
                errors.append(f"{pid}/{control_id}: runner is not a pinned executable component")
            argv = control["argv"]
            rendered = " ".join(argv).lower()
            if argv[0] != "python" or len(argv) != 2 or argv[1] not in component_paths:
                errors.append(f"{pid}/{control_id}: control argv must name one pinned Python script")
            if any(token in rendered for token in ("hermes", "--provider", "--model", "curl", "wget")):
                errors.append(f"{pid}/{control_id}: control may call a model or network")
            if control["result_evidence"]["path"] not in component_paths:
                errors.append(f"{pid}/{control_id}: result evidence is not a pinned component")
            if check_paths:
                errors.extend(file_errors(control["result_evidence"], f"{pid}/{control_id}/result", root))
                result_path = safe_path(root, control["result_evidence"]["path"])
                if result_path and result_path.is_file():
                    try:
                        evidence = load(result_path)
                        for expectation in control["expected_evidence"]:
                            if pointer(evidence, expectation["pointer"]) != expectation["equals"]:
                                errors.append(f"{pid}/{control_id}: result-evidence predicate mismatch at {expectation['pointer']}")
                    except (json.JSONDecodeError, KeyError, IndexError, ValueError, TypeError) as exc:
                        errors.append(f"{pid}/{control_id}: invalid result evidence: {exc}")
            expected = control["expected_stdout"]
            if "json_path" in expected:
                if expected["json_path"] not in component_paths:
                    errors.append(f"{pid}/{control_id}: expected stdout file is not a pinned component")
                elif check_paths:
                    expected_path = safe_path(root, expected["json_path"])
                    if expected_path:
                        try:
                            load(expected_path)
                        except (OSError, json.JSONDecodeError) as exc:
                            errors.append(f"{pid}/{control_id}: invalid expected stdout: {exc}")
    if set(manifest["claim_ceiling"]) != CLAIMS or any(manifest["claim_ceiling"].values()):
        errors.append("release claim ceiling upgrade")
    return errors


def run_control(package: dict[str, Any], control: dict[str, Any], root: Path) -> dict[str, Any]:
    argv = [sys.executable, control["argv"][1]]
    result = subprocess.run(argv, cwd=root, capture_output=True, text=True, timeout=control["timeout_seconds"])
    detail = []
    if result.returncode != control["expected_exit"]:
        detail.append(f"exit {result.returncode}, expected {control['expected_exit']}")
    try:
        observed = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        observed = None
        detail.append(f"stdout is not JSON: {exc}")
    expected_spec = control["expected_stdout"]
    expected = expected_spec.get("inline_json")
    if "json_path" in expected_spec:
        expected = load(root / expected_spec["json_path"])
    if observed != expected:
        detail.append("stdout JSON differs from the declared exact outcome")
    return {
        "package_id": package["package_id"], "control_id": control["control_id"],
        "argv": control["argv"], "exit_status": result.returncode,
        "stdout_sha256": hashlib.sha256(result.stdout.encode()).hexdigest(),
        "stderr": result.stderr, "passed": not detail, "errors": detail,
    }


def validate_release(manifest_path: Path, *, run_controls: bool = True, root: Path = ROOT) -> dict[str, Any]:
    manifest = load(manifest_path)
    errors = semantic_errors(manifest, root=root, check_paths=True)
    controls: list[dict[str, Any]] = []
    if not errors and run_controls:
        for package in manifest["packages"]:
            for control in package["controls"]:
                record = run_control(package, control, root)
                controls.append(record)
                errors.extend(f"{package['package_id']}/{control['control_id']}: {error}" for error in record["errors"])
    return {
        "report_version": "1.0.0", "release_id": manifest.get("release_id"),
        "manifest": {"path": manifest_path.relative_to(root).as_posix(), "sha256": sha256(manifest_path)},
        "status": "passed_internal_clean_release_conformance" if not errors else "failed_closed",
        "passed": not errors, "errors": errors, "package_count": len(manifest.get("packages", [])),
        "work_shapes": sorted({item.get("work_shape") for item in manifest.get("packages", [])}),
        "control_results": controls, "aggregation_id": manifest.get("aggregation", {}).get("aggregation_id"),
        "claim_ceiling": manifest.get("claim_ceiling"),
        "claim_boundary": "Internal retained-fixture release conformance only; no agent capability, professional validity, production safety/fitness, public-release readiness, or cross-domain generalization claim.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--no-controls", action="store_true")
    args = parser.parse_args()
    report = validate_release(args.manifest.resolve(), run_controls=not args.no_controls)
    payload = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
