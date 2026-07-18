#!/usr/bin/env python3
"""Make the two frozen v3 source-only generation attempts exactly once.

The launcher verifies the pushed freeze, exposes only one corpus in each sandbox,
retains every provider-facing record, and refuses to rerun an existing attempt.
It invokes the independently committed validator after each call but never edits,
repairs, or retries candidate output.
"""
from __future__ import annotations

import hashlib
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
FAMILIES = {
    "family-gamma": (
        HERE / "families/capacity-apportionment/corpus.json",
        HERE / "generation-policies/family-gamma.json",
    ),
    "family-delta": (
        HERE / "families/dependency-release/corpus.json",
        HERE / "generation-policies/family-delta.json",
    ),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inventory(path: Path) -> dict[str, dict[str, Any]]:
    return {
        item.relative_to(path).as_posix(): {"sha256": sha256(item), "bytes": item.stat().st_size}
        for item in sorted(path.rglob("*"))
        if item.is_file()
    }


def git_bytes(revision: str, path: Path) -> bytes:
    relative = path.relative_to(ROOT).as_posix()
    return subprocess.run(
        ["git", "show", f"{revision}:{relative}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    ).stdout


def verify_pushed_freeze() -> dict[str, Any]:
    subprocess.run(["git", "fetch", "origin", "main"], cwd=ROOT, check=True, capture_output=True)
    origin_commit = subprocess.run(
        ["git", "rev-parse", "origin/main"], cwd=ROOT, check=True, capture_output=True, text=True
    ).stdout.strip()
    manifest_path = HERE / "freeze-manifest.json"
    protocol_path = HERE / "protocol.json"
    for path in (manifest_path, protocol_path):
        if git_bytes("origin/main", path) != path.read_bytes():
            raise RuntimeError(f"local bytes differ from pushed origin/main: {path.relative_to(ROOT)}")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    checked: list[dict[str, str]] = []
    for component in manifest["component_hashes"]:
        path = ROOT / component["path"]
        actual = sha256(path)
        origin_hash = hashlib.sha256(git_bytes("origin/main", path)).hexdigest()
        if actual != component["sha256"] or origin_hash != component["sha256"]:
            raise RuntimeError(f"frozen component hash mismatch: {component['path']}")
        checked.append({"path": component["path"], "sha256": actual})
    preflight = json.loads((HERE / "preflight/report.json").read_text(encoding="utf-8"))
    if preflight.get("status") != "PASS" or preflight.get("errors"):
        raise RuntimeError("committed zero-call preflight report is not passing")
    return {
        "origin_commit": origin_commit,
        "protocol_sha256": sha256(protocol_path),
        "manifest_sha256": sha256(manifest_path),
        "component_hashes": checked,
        "preflight_report_sha256": sha256(HERE / "preflight/report.json"),
    }


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


def bwrap(inputs: Path, outputs: Path, profile: Path, command: list[str]) -> list[str]:
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


def prompt(policy: dict[str, Any]) -> str:
    visible = policy["allowed_visible_inputs"][0]
    claims = json.dumps(policy["allowed_claim_ceiling"], sort_keys=True)
    return f"""Produce one reusable procedure from corpus.json only. Do not infer any downstream task, identifier, filename, endpoint, check, rubric, answer, or claim. Preserve every proposition and each contradiction, threshold, artifact convention, and failure signature through a reciprocal binding or typed omission. Read only corpus.json and write only outputs/package.json. Do not copy or seek repository context.

Write strict JSON with exactly these top-level keys: schema_version, package_id, package_version, source_identity, generation_context, proposition_bindings, clauses, omissions, contradictions, thresholds, artifact_conventions, failure_signatures, claim_ceiling.
- schema_version is "0.1.0" and package_version is "1.0.0".
- package_id is a lowercase identifier beginning with a letter.
- source_identity has family_id "{policy['expected_family_id']}", family_version "{policy['expected_family_version']}", and source_corpus_sha256 "{policy['source_corpus_sha256']}".
- generation_context is exactly generator_kind "model_corpus_only_once", source_only true, task_context_visible false, generation_attempt 1, visible_inputs ["{visible}"].
- proposition_bindings contains every and only source proposition once. Each has proposition_id, nonempty unique clause_ids, and transformation chosen from verbatim, bounded_paraphrase, combined_synthesis. Its clause_ids must exactly equal clauses whose proposition_basis contains that proposition.
- clauses are nonempty and each has lowercase clause_id, instruction, and nonempty unique proposition_basis. Every clause must be bound and use only source proposition IDs.
- omissions is an array. A typed omission has source_kind (contradiction, threshold, artifact_convention, or failure_signature), source_object_id, reason_kind (not_applicable_to_package_scope, unsupported_transformation, or unresolved_source_ambiguity), and rationale. Do not silently omit.
- contradictions, thresholds, artifact_conventions, and failure_signatures each project every corresponding source object not explicitly omitted. Each item has lowercase item_id, exact source_object_id, proposition_basis exactly matching that source object's propositions or basis, and content.
- claim_ceiling is exactly {claims}.
Use no additional properties. Preserve source meaning without adding task-conditioned content. Produce no other artifact."""


def run_family(family_id: str, corpus: Path, policy_path: Path, freeze: dict[str, Any]) -> bool:
    attempt = HERE / "generation" / family_id
    if attempt.exists():
        raise RuntimeError(f"attempt already exists; retry forbidden: {attempt}")
    inputs = attempt / "inputs"
    outputs = attempt / "outputs"
    profile = attempt / ".profile"
    inputs.mkdir(parents=True)
    outputs.mkdir()
    (inputs / "outputs").mkdir()
    shutil.copy2(corpus, inputs / "corpus.json")
    policy = json.loads(policy_path.read_text(encoding="utf-8"))
    prompt_path = attempt / "prompt.txt"
    prompt_path.write_text(prompt(policy) + "\n", encoding="utf-8")
    make_profile(profile)
    command = [
        "/opt/hermes/venv/bin/python", "/opt/hermes/venv/bin/hermes", "-z", prompt_path.read_text(encoding="utf-8"),
        "--usage-file", "/trial/outputs/usage.json", "--model", MODEL, "--provider", PROVIDER,
        "--toolsets", "file", "--safe-mode",
    ]
    started = datetime.now(timezone.utc).isoformat()
    try:
        process = subprocess.run(bwrap(inputs, outputs, profile, command), text=True, capture_output=True, timeout=900)
    except subprocess.TimeoutExpired as exc:
        timeout_stdout = exc.stdout.decode("utf-8", errors="replace") if isinstance(exc.stdout, bytes) else (exc.stdout or "")
        timeout_stderr = exc.stderr.decode("utf-8", errors="replace") if isinstance(exc.stderr, bytes) else (exc.stderr or "timeout")
        process = subprocess.CompletedProcess(command, 124, timeout_stdout, timeout_stderr)
    finished = datetime.now(timezone.utc).isoformat()
    (attempt / "stdout.log").write_text(process.stdout, encoding="utf-8")
    (attempt / "stderr.log").write_text(process.stderr, encoding="utf-8")
    shutil.rmtree(profile, ignore_errors=True)

    package = outputs / "package.json"
    adjudication_command = [
        sys.executable, str(ROOT / "scripts/validate_procedure_generation_output.py"), str(package),
        "--source", str(corpus), "--policy", str(policy_path),
    ]
    adjudication = subprocess.run(adjudication_command, cwd=ROOT, text=True, capture_output=True)
    (attempt / "adjudication.stdout.log").write_text(adjudication.stdout, encoding="utf-8")
    (attempt / "adjudication.stderr.log").write_text(adjudication.stderr, encoding="utf-8")
    valid = process.returncode == 0 and adjudication.returncode == 0
    report = {
        "family_id": family_id,
        "started_at": started,
        "finished_at": finished,
        "model": MODEL,
        "provider": PROVIDER,
        "toolsets": ["file"],
        "safe_mode": True,
        "source_only": True,
        "generation_attempts": 1,
        "model_attempts": 1,
        "provider_attempts": 1,
        "repair_attempts": 0,
        "executor_attempts": 0,
        "returncode": process.returncode,
        "adjudication_returncode": adjudication.returncode,
        "launcher_valid": valid,
        "package_sha256": sha256(package) if package.exists() else None,
        "prompt_sha256": sha256(prompt_path),
        "source_corpus_sha256": sha256(corpus),
        "policy_sha256": sha256(policy_path),
        "freeze_verification": freeze,
        "input_inventory": inventory(inputs),
        "output_inventory": inventory(outputs),
        "stdout_sha256": sha256(attempt / "stdout.log"),
        "stderr_sha256": sha256(attempt / "stderr.log"),
        "adjudication_stdout_sha256": sha256(attempt / "adjudication.stdout.log"),
        "adjudication_stderr_sha256": sha256(attempt / "adjudication.stderr.log"),
        "claim_ceiling": policy["allowed_claim_ceiling"],
    }
    (attempt / "report.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return valid


def main() -> int:
    if (HERE / "generation").exists():
        raise RuntimeError("generation directory already exists; all retries are forbidden")
    freeze = verify_pushed_freeze()
    results: dict[str, bool] = {}
    for family_id, (corpus, policy) in FAMILIES.items():
        try:
            results[family_id] = run_family(family_id, corpus, policy, freeze)
        except Exception as exc:  # retain the other predeclared attempt, but never retry this one
            results[family_id] = False
            print(f"{family_id}: {exc}", file=sys.stderr)
    summary = {
        "passed": all(results.values()) and set(results) == set(FAMILIES),
        "results": results,
        "package_generation_attempts": 2,
        "model_attempts": 2,
        "provider_attempts": 2,
        "executor_attempts": 0,
        "repair_attempts": 0,
    }
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0 if summary["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
