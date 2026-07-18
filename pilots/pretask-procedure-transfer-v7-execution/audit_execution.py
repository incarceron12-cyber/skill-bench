#!/usr/bin/env python3
"""Verify and inventory the one-shot v7 matrix; reconstruct exact frozen prompts."""
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
V7 = ROOT / "pilots/pretask-procedure-transfer-v7"
CLAIMS = {"agent_capability": False, "expert_provenance": False, "production_fitness": False,
          "professional_validity": False, "readiness": False, "transfer": False, "utility": False}


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    spec = importlib.util.spec_from_file_location("v7_execution_launcher", HERE / "execute_matrix.py")
    assert spec and spec.loader
    launcher = importlib.util.module_from_spec(spec); spec.loader.exec_module(launcher)
    assignments = load(V7 / "assignments.json")["rows"]
    summary = load(HERE / "execution-report.json")
    pre = load(HERE / "preexecution-report.json"); canary = load(HERE / "execution-canary-report.json")
    errors: list[str] = []
    if pre.get("status") != "PASS" or pre.get("executor_attempts") != 0:
        errors.append("preexecution_gate")
    if canary.get("status") != "PASS" or canary.get("executor_attempts") != 0:
        errors.append("canary_gate")
    if summary.get("status") != "complete" or summary.get("claim_ceiling") != CLAIMS:
        errors.append("summary_status_or_claims")
    prompt = launcher.prompt(); prompt_hash = hashlib.sha256(prompt.encode()).hexdigest()
    rows, evidence, totals = [], {}, {"api_calls": 0, "input_tokens": 0, "output_tokens": 0,
                                      "reasoning_tokens": 0, "total_tokens": 0, "estimated_cost_usd": 0.0}
    for assignment in assignments:
        trial = HERE / "execution" / f"{assignment['schedule_index']:02d}-{assignment['task_id']}"
        report_path = trial / "trial-report.json"; usage_path = trial / "outputs/usage.json"
        result_path = trial / "outputs/result.json"; trace_path = trial / "redacted-trace.log"
        stderr_path = trial / "launcher-stderr.log"; prompt_path = trial / "prompt.txt"
        if not report_path.is_file():
            errors.append(f"missing_trial:{assignment['schedule_index']}"); continue
        report, usage = load(report_path), load(usage_path)
        prompt_path.write_text(prompt, encoding="utf-8")
        if ({k: report.get(k) for k in ("schedule_index", "task_id", "family_id", "condition_id")}
                != {k: assignment[k] for k in ("schedule_index", "task_id", "family_id", "condition_id")}):
            errors.append(f"assignment_drift:{assignment['schedule_index']}")
        if (report.get("attempts") != 1 or report.get("repair_attempts") != 0 or report.get("retry_attempts") != 0
                or report.get("attempt_state") != "attempted" or report.get("claim_ceiling") != CLAIMS):
            errors.append(f"attempt_or_claim:{assignment['schedule_index']}")
        if report.get("prompt_sha256") != prompt_hash or sha(prompt_path) != prompt_hash:
            errors.append(f"prompt_hash:{assignment['schedule_index']}")
        if not (usage.get("completed") is True and usage.get("failed") is False
                and usage.get("cost_status") == "included" and usage.get("estimated_cost_usd") == 0.0
                and usage.get("model") == "gpt-5.6-sol" and usage.get("provider") == "openai-codex"):
            errors.append(f"service_cost:{assignment['schedule_index']}")
        for key in ("api_calls", "input_tokens", "output_tokens", "reasoning_tokens", "total_tokens"):
            totals[key] += usage.get(key, 0)
        totals["estimated_cost_usd"] += usage.get("estimated_cost_usd", 0.0)
        files = [report_path, usage_path, result_path, trace_path, stderr_path, prompt_path]
        if not all(path.is_file() for path in files):
            errors.append(f"missing_evidence:{assignment['schedule_index']}")
        evidence[str(assignment["schedule_index"])] = {
            path.relative_to(ROOT).as_posix(): {"sha256": sha(path), "bytes": path.stat().st_size}
            for path in files if path.is_file()
        }
        rows.append({"schedule_index": assignment["schedule_index"], "attempt_state": report["attempt_state"],
                     "service_valid": report["service_valid"], "environment_valid": report["environment_valid"],
                     "artifact_valid": report["artifact_valid"], "checker_scored": report["checker_scored"],
                     "endpoint_pass": report["endpoint_pass"], "api_calls": usage.get("api_calls"),
                     "total_tokens": usage.get("total_tokens"), "included_cost_usd": usage.get("estimated_cost_usd")})
    denominators = summary.get("denominators", {})
    expected = {"intended": 32, "attempted": 32, "skipped": 0, "invalid": 0, "service_valid": 32,
                "environment_valid": 32, "artifact_valid": sum(row["artifact_valid"] for row in rows),
                "checker_scored": sum(row["checker_scored"] for row in rows),
                "endpoint_pass": sum(row["endpoint_pass"] for row in rows)}
    if denominators != expected:
        errors.append("strict_denominator_mismatch")
    report = {"audit_id": "pretask-procedure-transfer-v7-execution-audit", "status": "PASS" if not errors else "FAIL",
              "errors": errors, "execution_report": {"path": (HERE / "execution-report.json").relative_to(ROOT).as_posix(),
              "sha256": sha(HERE / "execution-report.json")}, "preexecution_report_sha256": sha(HERE / "preexecution-report.json"),
              "execution_canary_report_sha256": sha(HERE / "execution-canary-report.json"),
              "prompt_retention": {"status": "exact_bytes_reconstructed_postexecution_from_launcher_prompt_function",
              "sha256": prompt_hash, "count": len(rows), "limitation": "Prompt files were retained after calls; trial reports prospectively recorded the same byte hash."},
              "denominators": denominators, "resource_totals": totals, "rows": rows, "evidence_inventory": evidence,
              "attempts": {"executor": len(rows), "model": len(rows), "provider": len(rows), "repair": 0, "retry": 0},
              "claim_ceiling": CLAIMS, "interpretation": "Audit of retention and arithmetic only. All seven claims remain false."}
    output = HERE / "execution-audit-report.json"
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": report["status"], "errors": errors, "denominators": denominators,
                      "resource_totals": totals, "prompt_files": len(rows)}, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
