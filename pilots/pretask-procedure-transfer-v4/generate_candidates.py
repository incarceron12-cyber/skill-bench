#!/usr/bin/env python3
"""Make exactly one frozen-order source-only v4 generation attempt per family.

This append-only launcher verifies the pushed zero-call freeze, imports the exact
successful upstream prompt function, exposes only the four predeclared files,
and retains candidate bytes without repair or retry. It never materializes a
hindsight package, assignment, endpoint canary, or executor trial.
"""
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
ORDER = ("family-epsilon", "family-zeta")
FAMILY_PATHS = {
    "family-epsilon": (HERE / "families/epsilon/corpus.json", HERE / "generation-policies/epsilon.json"),
    "family-zeta": (HERE / "families/zeta/corpus.json", HERE / "generation-policies/zeta.json"),
}
VISIBLE_INPUTS = ("corpus.json", "interface-guide.md", "example-source.json", "example-package.json")
UPSTREAM_PATH = ROOT / "pilots/procedure-package-interface-usability-v1/generate.py"

spec = importlib.util.spec_from_file_location("upstream_interface_launcher", UPSTREAM_PATH)
assert spec and spec.loader
upstream = importlib.util.module_from_spec(spec)
spec.loader.exec_module(upstream)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_bytes(revision: str, path: Path) -> bytes:
    return subprocess.run(
        ["git", "show", f"{revision}:{path.relative_to(ROOT).as_posix()}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    ).stdout


def inventory(path: Path) -> dict[str, dict[str, Any]]:
    return {
        item.relative_to(path).as_posix(): {"sha256": sha(item), "bytes": item.stat().st_size}
        for item in sorted(path.rglob("*"))
        if item.is_file()
    }


def verify_pushed_freeze() -> dict[str, Any]:
    subprocess.run(["git", "fetch", "origin", "main"], cwd=ROOT, check=True, capture_output=True)
    origin = subprocess.run(
        ["git", "rev-parse", "origin/main"], cwd=ROOT, check=True, capture_output=True, text=True
    ).stdout.strip()
    manifest_path = HERE / "freeze-manifest.json"
    preflight_path = HERE / "preflight-report.json"
    for path in (manifest_path, preflight_path):
        if git_bytes("origin/main", path) != path.read_bytes():
            raise RuntimeError(f"local bytes differ from pushed origin/main: {path.name}")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    checked: list[dict[str, str]] = []
    for row in manifest["components"]:
        path = ROOT / row["path"]
        actual = sha(path)
        origin_hash = hashlib.sha256(git_bytes("origin/main", path)).hexdigest()
        if actual != row["sha256"] or origin_hash != row["sha256"]:
            raise RuntimeError(f"frozen component drift: {row['path']}")
        checked.append({"path": row["path"], "sha256": actual})
    preflight = json.loads(preflight_path.read_text(encoding="utf-8"))
    if preflight.get("status") != "PASS" or preflight.get("errors") or not preflight.get("generation_authorized_after_pushed_commit"):
        raise RuntimeError("committed v4 zero-call preflight does not authorize generation")
    if preflight.get("executor_authorized") is not False:
        raise RuntimeError("zero-call preflight improperly authorizes execution")
    protocol = json.loads((HERE / "protocol.json").read_text(encoding="utf-8"))
    for usage_rel in protocol["provider_cost_gate"]["evidence"]:
        usage = json.loads((ROOT / usage_rel).read_text(encoding="utf-8"))
        if not (
            usage.get("completed") is True
            and usage.get("failed") is False
            and usage.get("cost_status") == "included"
            and usage.get("estimated_cost_usd") == 0.0
            and usage.get("model") == MODEL
            and usage.get("provider") == PROVIDER
        ):
            raise RuntimeError(f"included-USD-0.00 prerequisite failed: {usage_rel}")
    return {
        "origin_commit": origin,
        "manifest_sha256": sha(manifest_path),
        "preflight_report_sha256": sha(preflight_path),
        "component_count": len(checked),
        "component_hashes": checked,
    }


def prompt(policy: dict[str, Any]) -> str:
    """Import, rather than restate or tune, the successful prompt semantics."""
    return upstream.prompt(policy)


def make_profile(path: Path) -> None:
    path.mkdir(parents=True)
    hermes_home = Path(os.environ.get("HERMES_HOME", str(Path.home() / ".hermes")))
    for source in (Path.home() / ".hermes/auth.json", hermes_home / ".env"):
        if source.exists():
            shutil.copy2(source, path / source.name)
    (path / "config.yaml").write_text(
        f"model:\n  default: {MODEL}\n  provider: {PROVIDER}\n"
        "agent:\n  max_turns: 20\nplatform_toolsets:\n  cli:\n    - file\n",
        encoding="utf-8",
    )


def sandbox(inputs: Path, outputs: Path, profile: Path, command: list[str]) -> list[str]:
    return [
        "bwrap", "--die-with-parent", "--new-session", "--unshare-pid",
        "--proc", "/proc", "--dev", "/dev", "--tmpfs", "/tmp",
        "--ro-bind", "/usr", "/usr", "--ro-bind", "/bin", "/bin",
        "--ro-bind", "/lib", "/lib", "--ro-bind", "/lib64", "/lib64",
        "--ro-bind", "/etc", "/etc", "--dir", "/run/systemd",
        "--ro-bind", "/run/systemd/resolve", "/run/systemd/resolve",
        "--dir", "/home", "--dir", "/home/sam", "--dir", "/home/sam/.local",
        "--dir", "/home/sam/.local/share", "--dir", "/home/sam/.local/share/uv",
        "--dir", "/home/sam/.local/share/uv/python", "--ro-bind", str(PYTHON), str(PYTHON),
        "--dir", "/opt/hermes", "--ro-bind", str(HERMES), "/opt/hermes",
        "--bind", str(profile), "/run/hermes-profile",
        "--ro-bind", str(inputs), "/trial", "--bind", str(outputs), "/trial/outputs",
        "--chdir", "/trial", "--setenv", "HOME", "/home/sam",
        "--setenv", "HERMES_REAL_HOME", "/home/sam", "--setenv", "HERMES_HOME", "/run/hermes-profile",
        "--setenv", "TERMINAL_CWD", "/trial", "--setenv", "PYTHONPATH", "/opt/hermes",
        "--setenv", "SSL_CERT_FILE", "/opt/hermes/venv/lib/python3.11/site-packages/certifi/cacert.pem",
        "--unsetenv", "HERMES_CRON_SESSION", "--unsetenv", "HERMES_SESSION_ID",
        "--unsetenv", "HERMES_SESSION_KEY", "--", *command,
    ]


def run_family(family_id: str, freeze: dict[str, Any]) -> dict[str, Any]:
    corpus, policy_path = FAMILY_PATHS[family_id]
    attempt = HERE / "candidate-generation" / family_id
    if attempt.exists():
        raise RuntimeError(f"retry forbidden; retained attempt already exists: {family_id}")
    inputs, outputs, profile = attempt / "inputs", attempt / "outputs", attempt / ".profile"
    inputs.mkdir(parents=True)
    outputs.mkdir()
    (inputs / "outputs").mkdir()
    sources = (
        (corpus, "corpus.json"),
        (HERE / "interface/interface-guide.md", "interface-guide.md"),
        (HERE / "interface/example-source.json", "example-source.json"),
        (HERE / "interface/example-package.json", "example-package.json"),
    )
    for source, name in sources:
        shutil.copy2(source, inputs / name)
    policy = json.loads(policy_path.read_text(encoding="utf-8"))
    if tuple(policy["allowed_visible_inputs"]) != VISIBLE_INPUTS:
        raise RuntimeError(f"visible-input allowlist drift: {family_id}")
    prompt_path = attempt / "prompt.txt"
    prompt_path.write_text(prompt(policy) + "\n", encoding="utf-8")
    make_profile(profile)
    command = [
        "/opt/hermes/venv/bin/python", "/opt/hermes/venv/bin/hermes", "-z",
        prompt_path.read_text(encoding="utf-8"), "--usage-file", "/trial/outputs/usage.json",
        "--model", MODEL, "--provider", PROVIDER, "--toolsets", "file", "--safe-mode",
    ]
    started = datetime.now(timezone.utc).isoformat()
    try:
        process = subprocess.run(sandbox(inputs, outputs, profile, command), text=True, capture_output=True, timeout=900)
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout.decode(errors="replace") if isinstance(exc.stdout, bytes) else (exc.stdout or "")
        stderr = exc.stderr.decode(errors="replace") if isinstance(exc.stderr, bytes) else (exc.stderr or "timeout")
        process = subprocess.CompletedProcess(command, 124, stdout, stderr)
    finished = datetime.now(timezone.utc).isoformat()
    (attempt / "stdout.log").write_text(process.stdout, encoding="utf-8")
    (attempt / "stderr.log").write_text(process.stderr, encoding="utf-8")
    shutil.rmtree(profile, ignore_errors=True)

    package, usage_path = outputs / "package.json", outputs / "usage.json"
    validator_command = [
        sys.executable, str(ROOT / "scripts/validate_procedure_generation_output.py"), str(package),
        "--source", str(corpus), "--policy", str(policy_path),
    ]
    validation = subprocess.run(validator_command, cwd=ROOT, text=True, capture_output=True)
    (attempt / "validator.stdout.log").write_text(validation.stdout, encoding="utf-8")
    (attempt / "validator.stderr.log").write_text(validation.stderr, encoding="utf-8")
    try:
        usage = json.loads(usage_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        usage = {}
    service_valid = (
        process.returncode == 0
        and usage.get("completed") is True
        and usage.get("failed") is False
        and usage.get("cost_status") == "included"
        and usage.get("estimated_cost_usd") == 0.0
        and usage.get("model") == MODEL
        and usage.get("provider") == PROVIDER
    )
    output_files = set(inventory(outputs))
    schema_valid = service_valid and validation.returncode == 0 and output_files == {"package.json", "usage.json"}
    report = {
        "family_id": family_id,
        "started_at": started,
        "finished_at": finished,
        "configured_system": {"model": MODEL, "provider": PROVIDER, "toolsets": ["file"], "safe_mode": True},
        "attempts": {"generation": 1, "model": 1, "provider": 1, "repair": 0, "retry": 0, "executor": 0},
        "attempted": True,
        "service_valid": service_valid,
        "schema_valid": schema_valid,
        "launcher_returncode": process.returncode,
        "validator_returncode": validation.returncode,
        "prompt_semantics": {"imported_from": UPSTREAM_PATH.relative_to(ROOT).as_posix(), "upstream_sha256": sha(UPSTREAM_PATH)},
        "prompt_sha256": sha(prompt_path),
        "source_corpus_sha256": sha(corpus),
        "policy_sha256": sha(policy_path),
        "package_sha256": sha(package) if package.is_file() else None,
        "usage_sha256": sha(usage_path) if usage_path.is_file() else None,
        "input_inventory": inventory(inputs),
        "output_inventory": inventory(outputs),
        "stdout_sha256": sha(attempt / "stdout.log"),
        "stderr_sha256": sha(attempt / "stderr.log"),
        "validator_stdout_sha256": sha(attempt / "validator.stdout.log"),
        "validator_stderr_sha256": sha(attempt / "validator.stderr.log"),
        "freeze_verification": freeze,
        "claim_ceiling": policy["allowed_claim_ceiling"],
    }
    (attempt / "report.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report


def main() -> int:
    output_root = HERE / "candidate-generation"
    summary_path = HERE / "candidate-generation-report.json"
    if output_root.exists() or summary_path.exists():
        raise RuntimeError("candidate generation record exists; repair, retry, and rerun are forbidden")
    freeze = verify_pushed_freeze()
    reports: list[dict[str, Any]] = []
    for family_id in ORDER:
        reports.append(run_family(family_id, freeze))
    both_valid = all(row["service_valid"] and row["schema_valid"] for row in reports) and len(reports) == 2
    summary = {
        "study_id": "pretask-procedure-transfer-v4-candidate-generation",
        "status": "candidates_ready_for_independent_audit" if both_valid else "stopped_fail_closed_invalid_candidate",
        "family_order": list(ORDER),
        "denominators": {
            "intended": 2,
            "attempted": 2,
            "service_valid": sum(row["service_valid"] for row in reports),
            "schema_valid": sum(row["schema_valid"] for row in reports),
        },
        "families": reports,
        "aggregate_attempts": {"generation": 2, "model": 2, "provider": 2, "repair": 0, "retry": 0, "executor": 0},
        "downstream_materialized": False,
        "executor_authorized": False,
        "claim_ceiling": json.loads((HERE / "protocol.json").read_text(encoding="utf-8"))["claim_ceiling"],
        "interpretation": "Candidate generation and schema conformance only; no transfer, capability, utility, expert, professional, production, or readiness claim.",
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0 if both_valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
