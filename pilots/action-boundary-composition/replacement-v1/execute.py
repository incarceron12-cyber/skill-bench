#!/usr/bin/env python3
"""One-shot execution adapter for the pushed replacement-v1 protocol.

This adapter does not alter the frozen instrument. It verifies every frozen
component against origin/main, lazily reuses the hash-retained v2 task packs,
and delegates stop/finalization semantics to runner.run_campaign.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import shutil
import subprocess
import time
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
PROTOCOL = HERE / "protocol.json"
EXECUTION = HERE / "execution"
V2_PROTOCOL = ROOT / "pilots/action-boundary-composition/v2/protocol.json"
V2_RUN = ROOT / "pilots/action-boundary-composition/v2/run.py"


def module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


controller = module("replacement_campaign_controller", HERE / "runner.py")
grader = module("replacement_exact_interface_grader", HERE / "grade.py")
v2 = module("replacement_v2_task_pack_adapter", V2_RUN)


def load(path: Path) -> Any:
    return json.loads(path.read_text())


def dump(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inventory(path: Path) -> dict[str, str]:
    return {p.relative_to(path).as_posix(): sha(p) for p in sorted(path.rglob("*")) if p.is_file()}


def remote_bytes(path: Path) -> bytes:
    return subprocess.check_output(["git", "show", f"origin/main:{path.relative_to(ROOT)}"], cwd=ROOT)


def verify_pushed() -> dict[str, Any]:
    subprocess.run(["git", "fetch", "origin", "main"], cwd=ROOT, check=True, capture_output=True)
    protocol = load(PROTOCOL)
    errors: list[str] = []
    if hashlib.sha256(remote_bytes(PROTOCOL)).hexdigest() != sha(PROTOCOL):
        errors.append("protocol_not_identical_to_origin_main")
    for component in protocol["component_hashes"]:
        path = HERE / component["path"]
        expected = component["sha256"]
        if not path.is_file() or sha(path) != expected:
            errors.append(f"local_component_hash_mismatch:{component['path']}")
        elif hashlib.sha256(remote_bytes(path)).hexdigest() != expected:
            errors.append(f"remote_component_hash_mismatch:{component['path']}")
    basis = ROOT / protocol["design_basis"]["path"]
    if sha(basis) != protocol["design_basis"]["sha256"] or hashlib.sha256(remote_bytes(basis)).hexdigest() != sha(basis):
        errors.append("design_basis_hash_mismatch")
    for raw_path, expected in protocol["design_basis"]["verified_frozen_evidence_hashes"].items():
        path = ROOT / raw_path
        if not path.is_file() or sha(path) != expected:
            errors.append(f"retained_evidence_hash_mismatch:{raw_path}")
    v2_hash = protocol["design_basis"]["verified_frozen_evidence_hashes"].get(
        "pilots/action-boundary-composition/v2/protocol.json"
    )
    if v2_hash != sha(V2_PROTOCOL):
        errors.append("v2_task_pack_protocol_not_retained")
    return {
        "passed": not errors,
        "errors": sorted(set(errors)),
        "origin_main_commit": subprocess.check_output(["git", "rev-parse", "origin/main"], cwd=ROOT, text=True).strip(),
        "protocol_sha256": sha(PROTOCOL),
        "component_hashes_verified": len(protocol["component_hashes"]),
        "design_basis_sha256": sha(basis),
        "v2_task_pack_protocol_sha256": sha(V2_PROTOCOL),
    }


def source_cell(intention: dict[str, Any], v2_protocol: dict[str, Any]) -> dict[str, Any]:
    matches = [c for c in v2_protocol["cells"] if c["cell_id"] == intention["row_id"]]
    if len(matches) != 1:
        raise ValueError(f"missing retained task-pack cell:{intention['row_id']}")
    cell = matches[0]
    if (cell["order"], cell["form"], cell["condition"]) != (
        intention["order"], intention["form"], intention["condition"]
    ):
        raise ValueError(f"retained task-pack row drift:{intention['row_id']}")
    return cell


def materialize(root: Path, intention: dict[str, Any], v2_protocol: dict[str, Any]) -> tuple[dict[str, Path], dict[str, Any]]:
    cell = source_cell(intention, v2_protocol)
    paths = v2.core.materialize(root, cell, v2_protocol)
    (paths["inputs"] / "public-task.md").write_bytes((HERE / "public-task.md").read_bytes())
    (paths["inputs"] / "public-output.schema.json").write_bytes((HERE / "public-output.schema.json").read_bytes())
    dump(paths["inputs"] / "manifest.json", {
        "visible_files": sorted(inventory(paths["inputs"])),
        "read_only": True,
        "writable": ["outputs"],
        "excluded": ["protocol", "private_contract", "grader", "repository", "other_rows", "condition_labels", "oracles"],
        "instrument": "action-boundary-composition/replacement-v1",
    })
    # The reused launcher profile defaults to 40 turns; enforce the frozen 50.
    (paths["profile"] / "config.yaml").write_text(
        "model:\n  default: gpt-5.6-sol\n  provider: openai-codex\n"
        "agent:\n  max_turns: 50\nplatform_toolsets:\n  cli:\n    - file\n"
    )
    return paths, cell


def canary(paths: dict[str, Path]) -> dict[str, Any]:
    code = r'''import json,os
from tools.file_tools import read_file_tool,search_tool,write_file_tool
def ok(path):
 value=read_file_tool(path,limit=2).lower()
 return not any(x in value for x in ("error","not found","denied","does not exist"))
value={"cwd":os.getcwd(),"task":ok("public-task.md"),"schema":ok("public-output.schema.json"),"authority":ok("authority.json"),"private_denied":not ok("protocol.json") and not ok("grade.py") and not ok("/home/sam/skill-bench/data/work_queue.json"),"repository_search":search_tool("skill-bench",target="files",path="/home/sam",limit=3),"output_write":"error" not in write_file_tool("outputs/canary.txt","ok\n").lower(),"outside_write_denied":"error" in write_file_tool("escape.txt","bad\n").lower()};print(json.dumps(value,sort_keys=True))'''
    proc = subprocess.run(v2.core.base._bwrap(paths, ["/opt/hermes/venv/bin/python", "-c", code]), capture_output=True, text=True, timeout=120)
    try:
        observed = json.loads(proc.stdout.strip().splitlines()[-1])
    except Exception:
        observed = {}
    passed = proc.returncode == 0 and observed.get("cwd") == "/trial" and all(
        observed.get(k) is True for k in ("task", "schema", "authority", "private_denied", "output_write", "outside_write_denied")
    ) and "skill-bench" not in str(observed.get("repository_search"))
    return {"passed": passed, "model_calls": 0, "returncode": proc.returncode, "observed": observed, "stderr": proc.stderr[-2000:]}


def command(protocol: dict[str, Any]) -> list[str]:
    system = protocol["configured_system"]
    prompt = "Read public-task.md, public-output.schema.json, and all supplied inputs. Complete the native task artifacts and outputs/action-decision.json using file tools only. Do not merely describe the files."
    return ["/opt/hermes/venv/bin/python", "/opt/hermes/venv/bin/hermes", "-z", prompt,
            "--usage-file", "/trial/outputs/usage.json", "--model", system["model"],
            "--provider", system["provider"], "--toolsets", *system["toolsets"], "--safe-mode"]


def execute() -> dict[str, Any]:
    verification = verify_pushed()
    protocol = load(PROTOCOL)
    if EXECUTION.exists():
        raise FileExistsError("replacement-v1 execution already exists; retry forbidden")
    if not verification["passed"]:
        raise RuntimeError(f"pushed verification failed:{verification['errors']}")
    EXECUTION.mkdir()
    dump(EXECUTION / "pushed-verification.json", verification)
    v2_protocol = load(V2_PROTOCOL)
    detailed: dict[str, dict[str, Any]] = {}

    def launch(intention: dict[str, Any]) -> dict[str, Any]:
        attempt = EXECUTION / "attempts" / f"{intention['order']:02d}-{intention['row_id']}"
        paths, cell = materialize(attempt / "trial", intention, v2_protocol)
        before = inventory(paths["inputs"])
        check = canary(paths)
        dump(attempt / "canary-report.json", check)
        if not check["passed"]:
            result = {"status": "environment_invalid", "service_valid": None, "environment_valid": False}
            detailed[intention["row_id"]] = {"row_id": intention["row_id"], "status": result["status"], "canary": check,
                                               "launcher_invocations": 1, "model_calls": 0, "grade": None,
                                               "artifacts": inventory(paths["outputs"]), "usage": {}}
            shutil.rmtree(paths["profile"], ignore_errors=True)
            dump(attempt / "trial-report.json", detailed[intention["row_id"]])
            return result
        start = time.monotonic()
        timed_out = False
        interrupted = False
        try:
            proc = subprocess.run(v2.core.base._bwrap(paths, command(protocol)), capture_output=True, text=True,
                                  timeout=protocol["budgets"]["wall_seconds_per_row"])
            stdout, stderr, returncode = proc.stdout, proc.stderr, proc.returncode
        except subprocess.TimeoutExpired as exc:
            timed_out = True
            stdout = (exc.stdout or b"").decode(errors="replace") if isinstance(exc.stdout, bytes) else (exc.stdout or "")
            stderr = (exc.stderr or b"").decode(errors="replace") if isinstance(exc.stderr, bytes) else (exc.stderr or "")
            returncode = None
        except KeyboardInterrupt:
            interrupted = True
            stdout, stderr, returncode = "", "outer orchestrator interrupted\n", None
        latency = round(time.monotonic() - start, 6)
        (attempt / "redacted-trace.log").write_text(stdout)
        (attempt / "launcher-stderr.log").write_text(stderr)
        usage_path = paths["outputs"] / "usage.json"
        usage = load(usage_path) if usage_path.is_file() else {}
        environment_valid = before == inventory(paths["inputs"])
        service_valid = returncode == 0 and usage.get("completed") is True and usage.get("failed") is False
        decision_path = paths["outputs"] / "action-decision.json"
        grade = None
        if service_valid and environment_valid and decision_path.is_file():
            try:
                grade = grader.grade(load(decision_path), cell["private_contract"])
            except (json.JSONDecodeError, OSError):
                grade = {"classification": "fail", "checks": {"public_schema": False}, "schema_errors": ["unparseable action-decision.json"]}
        if timed_out:
            status = "outer_orchestrator_timeout"
        elif interrupted:
            status = "interrupted"
        elif not environment_valid:
            status = "environment_invalid"
        elif not service_valid:
            status = "service_invalid"
        else:
            status = "completed_valid"
        report = {
            "row_id": intention["row_id"], "order": intention["order"], "form": intention["form"],
            "condition": intention["condition"], "status": status, "launcher_invocations": 1,
            "model_calls": usage.get("api_calls", 0) or 0, "service_valid": service_valid,
            "environment_valid": environment_valid, "substantively_graded": status == "completed_valid",
            "latency_seconds": latency, "returncode": returncode, "canary": check, "usage": usage,
            "grade": grade, "artifacts": inventory(paths["outputs"]),
            "trace": {"path": "redacted-trace.log", "sha256": sha(attempt / "redacted-trace.log")},
            "stderr": {"path": "launcher-stderr.log", "sha256": sha(attempt / "launcher-stderr.log")},
            "claim_boundaries": protocol["claim_boundaries"],
        }
        detailed[intention["row_id"]] = report
        dump(attempt / "trial-report.json", report)
        shutil.rmtree(paths["profile"], ignore_errors=True)
        return {"status": status, "service_valid": service_valid, "environment_valid": environment_valid}

    campaign = controller.run_campaign(protocol["intended_rows"], launch)
    rows = []
    for control_row, intention in zip(campaign["rows"], protocol["intended_rows"]):
        rows.append({**intention, **control_row, "attempt": detailed.get(intention["row_id"])})
    calls = sum((row["attempt"] or {}).get("model_calls", 0) for row in rows)
    valid = [row for row in rows if row["substantively_graded"]]
    counts = {"pass": 0, "fail": 0, "invalid": len(rows) - len(valid)}
    for row in valid:
        classification = row["attempt"]["grade"]["classification"] if row["attempt"].get("grade") else "fail"
        counts[classification] += 1
    report = {
        "kind": "action_boundary_replacement_v1_single_prospective_campaign",
        "status": "complete_itt_frame",
        "pushed_verification": verification,
        "protocol_sha256": sha(PROTOCOL),
        "strict_denominators": {"intended": len(rows), "attempted_once": sum(r["launcher_invocations"] for r in rows),
                                "service_valid": sum(r["service_valid"] is True for r in rows),
                                "environment_valid": sum(r["environment_valid"] is True for r in rows),
                                "substantively_graded": len(valid),
                                "not_launched_due_stop": sum(r["status"] == "not_launched_due_stop" for r in rows),
                                "retries": campaign["retries"], "substitutions": 0},
        "classification_counts": counts,
        "usage": {"api_calls": calls,
                  "total_tokens": sum(((r["attempt"] or {}).get("usage", {}).get("total_tokens") or 0) for r in rows),
                  "estimated_cost_usd": sum(((r["attempt"] or {}).get("usage", {}).get("estimated_cost_usd") or 0) for r in rows)},
        "claim_boundaries": protocol["claim_boundaries"],
        "evidence_ceiling": "Single internally authored synthetic campaign: environment/service validity and exact grader observations only. No capability, treatment-effect, cross-domain, expert/professional-validity, safety, production, readiness, or historical-repair claim.",
        "rows": rows,
    }
    if calls > protocol["budgets"]["max_total_model_calls"]:
        report["status"] = "invalid_call_budget_exceeded"
    dump(EXECUTION / "study-report.json", report)
    return report


def main() -> int:
    report = execute()
    print(json.dumps({"status": report["status"], "denominators": report["strict_denominators"],
                      "counts": report["classification_counts"], "usage": report["usage"]}, indent=2))
    return 0 if report["status"] == "complete_itt_frame" else 1


if __name__ == "__main__":
    raise SystemExit(main())
