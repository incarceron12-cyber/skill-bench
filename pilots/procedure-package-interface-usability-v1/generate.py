#!/usr/bin/env python3
"""Run the frozen three-case interface conformance study exactly once."""
from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
HERMES = Path("/home/sam/.hermes/hermes-agent")
PYTHON = Path("/home/sam/.local/share/uv/python/cpython-3.11-linux-x86_64-gnu")
MODEL = "gpt-5.6-sol"
PROVIDER = "openai-codex"
ORDER = ["case-alpha", "case-beta", "case-heldout"]

spec = importlib.util.spec_from_file_location("output_validator", ROOT / "scripts/validate_procedure_generation_output.py")
assert spec and spec.loader
output_validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(output_validator)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_bytes(revision: str, path: Path) -> bytes:
    return subprocess.run(["git", "show", f"{revision}:{path.relative_to(ROOT).as_posix()}"], cwd=ROOT, check=True, capture_output=True).stdout


def verify_pushed_freeze() -> dict[str, Any]:
    subprocess.run(["git", "fetch", "origin", "main"], cwd=ROOT, check=True, capture_output=True)
    origin = subprocess.run(["git", "rev-parse", "origin/main"], cwd=ROOT, check=True, text=True, capture_output=True).stdout.strip()
    manifest_path, protocol_path = HERE / "freeze-manifest.json", HERE / "protocol.json"
    for path in (manifest_path, protocol_path):
        if git_bytes("origin/main", path) != path.read_bytes():
            raise RuntimeError(f"local bytes differ from pushed origin/main: {path.name}")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for row in manifest["components"]:
        path = ROOT / row["path"]
        if sha(path) != row["sha256"] or hashlib.sha256(git_bytes("origin/main", path)).hexdigest() != row["sha256"]:
            raise RuntimeError(f"frozen component drift: {row['path']}")
    preflight = json.loads((HERE / "preflight-report.json").read_text(encoding="utf-8"))
    if preflight.get("status") != "PASS" or not preflight.get("generation_authorized"):
        raise RuntimeError("pre-call source/task and freeze preflight is not passing")
    protocol = json.loads(protocol_path.read_text(encoding="utf-8"))
    for usage_rel in protocol["prerequisite_gates"]["provider_cost_evidence"]:
        usage = json.loads((ROOT / usage_rel).read_text(encoding="utf-8"))
        if not (usage.get("completed") is True and usage.get("failed") is False and usage.get("cost_status") == "included" and usage.get("estimated_cost_usd") == 0.0 and usage.get("model") == MODEL and usage.get("provider") == PROVIDER):
            raise RuntimeError(f"included-USD-0.00 provider prerequisite failed: {usage_rel}")
    return {"origin_commit": origin, "manifest_sha256": sha(manifest_path), "protocol_sha256": sha(protocol_path)}


def make_profile(path: Path) -> None:
    path.mkdir(parents=True)
    hermes_home = Path(os.environ.get("HERMES_HOME", str(Path.home() / ".hermes")))
    for source in (Path.home() / ".hermes/auth.json", hermes_home / ".env"):
        if source.exists():
            shutil.copy2(source, path / source.name)
    (path / "config.yaml").write_text(f"model:\n  default: {MODEL}\n  provider: {PROVIDER}\nagent:\n  max_turns: 20\nplatform_toolsets:\n  cli:\n    - file\n", encoding="utf-8")


def sandbox(inputs: Path, outputs: Path, profile: Path, command: list[str]) -> list[str]:
    return [
        "bwrap", "--die-with-parent", "--new-session", "--unshare-pid", "--proc", "/proc", "--dev", "/dev", "--tmpfs", "/tmp",
        "--ro-bind", "/usr", "/usr", "--ro-bind", "/bin", "/bin", "--ro-bind", "/lib", "/lib", "--ro-bind", "/lib64", "/lib64", "--ro-bind", "/etc", "/etc",
        "--dir", "/run/systemd", "--ro-bind", "/run/systemd/resolve", "/run/systemd/resolve",
        "--dir", "/home", "--dir", "/home/sam", "--dir", "/home/sam/.local", "--dir", "/home/sam/.local/share", "--dir", "/home/sam/.local/share/uv", "--dir", "/home/sam/.local/share/uv/python", "--ro-bind", str(PYTHON), str(PYTHON),
        "--dir", "/opt/hermes", "--ro-bind", str(HERMES), "/opt/hermes", "--bind", str(profile), "/run/hermes-profile",
        "--ro-bind", str(inputs), "/trial", "--bind", str(outputs), "/trial/outputs", "--chdir", "/trial",
        "--setenv", "HOME", "/home/sam", "--setenv", "HERMES_REAL_HOME", "/home/sam", "--setenv", "HERMES_HOME", "/run/hermes-profile", "--setenv", "TERMINAL_CWD", "/trial", "--setenv", "PYTHONPATH", "/opt/hermes", "--setenv", "SSL_CERT_FILE", "/opt/hermes/venv/lib/python3.11/site-packages/certifi/cacert.pem",
        "--unsetenv", "HERMES_CRON_SESSION", "--unsetenv", "HERMES_SESSION_ID", "--unsetenv", "HERMES_SESSION_KEY", "--", *command,
    ]


def prompt(policy: dict[str, Any]) -> str:
    claims = json.dumps(policy["allowed_claim_ceiling"], sort_keys=True)
    return f"""Read corpus.json, interface-guide.md, example-source.json, and example-package.json. Produce one reusable source-only procedure package for corpus.json. The example demonstrates shape and typing only; do not copy its identifiers or content. Do not infer a downstream task, check, endpoint, answer, or claim. Follow interface-guide.md exactly, preserve or explicitly omit every source primitive, and ensure reciprocal proposition/clause bindings.

Use source family_id {policy['expected_family_id']}, family_version {policy['expected_family_version']}, and SHA-256 {policy['source_corpus_sha256']}. generation_context must be generator_kind model_corpus_only_once, source_only true, task_context_visible false, generation_attempt 1, and visible_inputs exactly {json.dumps(policy['allowed_visible_inputs'])}. claim_ceiling must be exactly {claims}.

Read only the four named files. Write only strict JSON to outputs/package.json. Produce no markdown fence, commentary, or other artifact."""


def field_validity(package: dict[str, Any] | None, structural: list[str]) -> dict[str, bool]:
    required = ["schema_version", "package_id", "package_version", "source_identity", "generation_context", "proposition_bindings", "clauses", "omissions", "contradictions", "thresholds", "artifact_conventions", "failure_signatures", "claim_ceiling"]
    if package is None:
        return {field: False for field in required}
    result: dict[str, bool] = {}
    for field in required:
        result[field] = field in package and not any(error.startswith(field + ".") or error.startswith(field + ":") or ("is a required property" in error and f"'{field}'" in error) for error in structural)
    return result


def run_case(case: dict[str, Any], freeze: dict[str, Any]) -> tuple[dict[str, Any], bool]:
    case_id = case["case_id"]
    attempt = HERE / "generation" / case_id
    if attempt.exists():
        raise RuntimeError(f"retry forbidden; attempt exists: {case_id}")
    inputs, outputs, profile = attempt / "inputs", attempt / "outputs", attempt / ".profile"
    inputs.mkdir(parents=True); outputs.mkdir(); (inputs / "outputs").mkdir()
    source_path, policy_path = ROOT / case["source_path"], ROOT / case["policy_path"]
    for source, name in ((source_path, "corpus.json"), (HERE / "interface/interface-guide.md", "interface-guide.md"), (HERE / "interface/example-source.json", "example-source.json"), (HERE / "interface/example-package.json", "example-package.json")):
        shutil.copy2(source, inputs / name)
    policy = json.loads(policy_path.read_text(encoding="utf-8"))
    prompt_path = attempt / "prompt.txt"; prompt_path.write_text(prompt(policy) + "\n", encoding="utf-8")
    make_profile(profile)
    command = ["/opt/hermes/venv/bin/python", "/opt/hermes/venv/bin/hermes", "-z", prompt_path.read_text(encoding="utf-8"), "--usage-file", "/trial/outputs/usage.json", "--model", MODEL, "--provider", PROVIDER, "--toolsets", "file", "--safe-mode"]
    started = datetime.now(timezone.utc).isoformat()
    try:
        proc = subprocess.run(sandbox(inputs, outputs, profile, command), text=True, capture_output=True, timeout=900)
    except subprocess.TimeoutExpired as exc:
        proc = subprocess.CompletedProcess(command, 124, exc.stdout or "", exc.stderr or "timeout")
    finished = datetime.now(timezone.utc).isoformat()
    (attempt / "stdout.log").write_text(proc.stdout if isinstance(proc.stdout, str) else proc.stdout.decode(errors="replace"), encoding="utf-8")
    (attempt / "stderr.log").write_text(proc.stderr if isinstance(proc.stderr, str) else proc.stderr.decode(errors="replace"), encoding="utf-8")
    shutil.rmtree(profile, ignore_errors=True)
    package_path, usage_path = outputs / "package.json", outputs / "usage.json"
    package = None; parse_error = None; structural: list[str] = []; semantic: list[str] = []
    if package_path.exists():
        try:
            package = json.loads(package_path.read_text(encoding="utf-8"))
            structural = output_validator.structural_errors(package)
            if not structural:
                semantic = output_validator.semantic_errors(package, json.loads(source_path.read_text(encoding="utf-8")), source_path.read_bytes(), policy)
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            parse_error = str(exc)
    else:
        parse_error = "outputs/package.json missing"
    usage = json.loads(usage_path.read_text(encoding="utf-8")) if usage_path.exists() else {}
    service_valid = proc.returncode == 0 and usage.get("completed") is True and usage.get("failed") is False and usage.get("cost_status") == "included" and usage.get("estimated_cost_usd") == 0.0
    schema_valid = service_valid and package is not None and parse_error is None and not structural and not semantic
    adjudication = {"case_id": case_id, "parse_error": parse_error, "structural_errors": structural, "semantic_errors": semantic, "field_validity": field_validity(package, structural), "whole_package_schema_valid": schema_valid}
    (attempt / "adjudication.json").write_text(json.dumps(adjudication, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    report = {"case_id": case_id, "role": case["role"], "started_at": started, "finished_at": finished, "model": MODEL, "provider": PROVIDER, "toolsets": ["file"], "attempted": True, "service_valid": service_valid, "schema_valid": schema_valid, "launcher_returncode": proc.returncode, "repair_attempts": 0, "retry_attempts": 0, "executor_attempts": 0, "prompt_sha256": sha(prompt_path), "package_sha256": sha(package_path) if package_path.exists() else None, "usage_sha256": sha(usage_path) if usage_path.exists() else None, "freeze_verification": freeze, "claim_ceiling": policy["allowed_claim_ceiling"]}
    (attempt / "report.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report, service_valid


def main() -> int:
    if (HERE / "generation").exists() or (HERE / "study-report.json").exists():
        raise RuntimeError("study output exists; every rerun is forbidden")
    freeze = verify_pushed_freeze()
    protocol = json.loads((HERE / "protocol.json").read_text(encoding="utf-8"))
    by_id = {row["case_id"]: row for row in protocol["cases"]}
    reports: list[dict[str, Any]] = []
    stop_reason = None
    for case_id in ORDER:
        report, service_valid = run_case(by_id[case_id], freeze)
        reports.append(report)
        if not service_valid:
            stop_reason = f"protocol-wide service/cost prerequisite failed after retained attempt: {case_id}"
            break
    summary = {"study_id": protocol["study_id"], "status": "complete" if len(reports) == 3 else "stopped_fail_closed", "stop_reason": stop_reason, "denominators": {"intended": 3, "attempted": len(reports), "service_valid": sum(row["service_valid"] for row in reports), "schema_valid": sum(row["schema_valid"] for row in reports)}, "cases": reports, "repair_attempts": 0, "retry_attempts": 0, "executor_attempts": 0, "claim_ceiling": protocol["claim_ceiling"], "interpretation": "Interface conformance only. No transfer, consumption, capability, utility, expert, professional, production, or readiness claim."}
    (HERE / "study-report.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0 if len(reports) == 3 else 1


if __name__ == "__main__":
    raise SystemExit(main())
