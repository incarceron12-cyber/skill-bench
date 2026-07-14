#!/usr/bin/env python3
"""Zero-model-call bubblewrap canaries for construction and agent views."""
from __future__ import annotations
import hashlib
import json
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(__file__).resolve().parent
HERMES = Path("/home/sam/.hermes/hermes-agent")
PYTHON = Path("/home/sam/.local/share/uv/python/cpython-3.11-linux-x86_64-gnu")


def sha(path: Path) -> str: return hashlib.sha256(path.read_bytes()).hexdigest()
def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def copy_rel(rel: str, stage: Path) -> None:
    source, target = ROOT / rel, stage / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def command(stage: Path, outputs: Path, code: str) -> list[str]:
    return [
        "bwrap", "--die-with-parent", "--new-session", "--unshare-pid", "--proc", "/proc", "--dev", "/dev", "--tmpfs", "/tmp",
        "--ro-bind", "/usr", "/usr", "--ro-bind", "/bin", "/bin", "--ro-bind", "/lib", "/lib", "--ro-bind", "/lib64", "/lib64", "--ro-bind", "/etc", "/etc",
        "--dir", "/home", "--dir", "/home/sam", "--dir", "/home/sam/.local", "--dir", "/home/sam/.local/share", "--dir", "/home/sam/.local/share/uv", "--dir", "/home/sam/.local/share/uv/python",
        "--ro-bind", str(PYTHON), str(PYTHON), "--dir", "/opt/hermes", "--ro-bind", str(HERMES), "/opt/hermes",
        "--ro-bind", str(stage), "/trial", "--bind", str(outputs), "/trial/outputs", "--chdir", "/trial",
        "--setenv", "HOME", "/home/sam", "--setenv", "TERMINAL_CWD", "/trial", "--setenv", "PYTHONPATH", "/opt/hermes",
        "--", "/opt/hermes/venv/bin/python", "-c", code,
    ]


PROBE = r'''
import json, os
from tools.file_tools import read_file_tool, search_tool, write_file_tool
def readable(path):
    value = read_file_tool(path, limit=5)
    return not any(x in value.lower() for x in ("error", "not found", "denied", "does not exist"))
result = {
  "cwd": os.getcwd(),
  "allowed_readable": {p: readable(p) for p in ALLOWED},
  "prohibited_denied": {p: not readable(p) for p in PROHIBITED},
  "repository_search": search_tool("skill-bench", target="files", path="/home/sam", limit=20),
}
write_ok = write_file_tool("outputs/canary.txt", "zero-call-canary\n")
write_bad = write_file_tool("escape.txt", "must-not-write\n")
result["output_write_succeeded"] = "error" not in write_ok.lower()
result["outside_write_denied"] = any(x in write_bad.lower() for x in ("error", "denied", "read-only", "permission"))
print(json.dumps(result, sort_keys=True))
'''


def execute(kind: str, cluster: str, view: str, allowed: list[str], prohibited: list[str]) -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="nonceiling-canary-") as temp:
        base = Path(temp); stage = base / "stage"; outputs = base / "outputs"
        stage.mkdir(); outputs.mkdir(); (stage / "outputs").mkdir()
        for rel in allowed: copy_rel(rel, stage)
        code = "ALLOWED=" + repr(allowed) + "\nPROHIBITED=" + repr(prohibited) + "\n" + PROBE
        proc = subprocess.run(command(stage, outputs, code), text=True, capture_output=True, timeout=120)
        try: observed = json.loads(proc.stdout.strip().splitlines()[-1])
        except (json.JSONDecodeError, IndexError): observed = {}
        passed = (
            proc.returncode == 0 and observed.get("cwd") == "/trial"
            and all(observed.get("allowed_readable", {}).values())
            and all(observed.get("prohibited_denied", {}).values())
            and "skill-bench" not in str(observed.get("repository_search", ""))
            and observed.get("output_write_succeeded") is True and observed.get("outside_write_denied") is True
        )
        return {
            "kind":kind, "cluster":cluster, "view":view, "passed":passed, "model_calls":0,
            "isolation_substrate":"bubblewrap mount namespace", "tool_interface":"Hermes tools.file_tools read/search/write",
            "allowed_inputs":[{"path":p, "sha256":sha(ROOT / p)} for p in allowed], "prohibited_probes":prohibited,
            "observed":observed, "returncode":proc.returncode, "stderr":proc.stderr[-2000:],
            "limitations":["Canary tests configured file-tool visibility, not resistance to an unconfigured terminal tool; measured agents are restricted to file tools.", "No provider request or model call occurs."],
        }


def construction(cluster: str) -> dict[str, Any]:
    manifest_path = ROOT / cluster / "rubrics/independent-construction-manifest.json"
    manifest = json.loads(manifest_path.read_text())
    allowed = [x["path"] for x in manifest["allowed_inputs"]]
    prohibited = [
        f"{cluster}/public-guide.md", f"{cluster}/rubrics/shared.json", "protocol.json",
        "calibration/case-manifest.json", "calibration/grade_calibration.py", "/home/sam/skill-bench/data/work_queue.json",
    ]
    if cluster == "vendor": prohibited.append("vendor/workspace/protected/incident-lock.txt")
    report = execute("independent_rubric_construction_firewall", cluster, "independent_construction", allowed, prohibited)
    report["construction_manifest_sha256"] = sha(manifest_path)
    return report


def agent(cluster: str, condition: str) -> dict[str, Any]:
    if cluster == "lh":
        allowed = ["lh/public-task.md", "lh/sources/measurement-evidence.csv", "lh/sources/ablation-evidence.csv", "lh/sources/adoption-summary.md"]
    else:
        allowed = ["vendor/public-task.md", "vendor/workspace/context.json", "vendor/workspace/current/status-seq-6.json", "vendor/workspace/current/status-seq-7.json", "vendor/workspace/archive/status-seq-5.json", "vendor/workspace/inbox/vendor-note.txt", "vendor/workspace/noise/status-template.json"]
    if condition == "public_skill": allowed.append(f"{cluster}/public-guide.md")
    prohibited = [
        f"{cluster}/rubrics/independent.json", f"{cluster}/rubrics/shared.json", "protocol.json",
        "calibration/case-manifest.json", "calibration/calibration-report.json", "calibration/grade_calibration.py",
        "/home/sam/skill-bench/data/work_queue.json",
    ]
    if condition == "no_skill": prohibited.append(f"{cluster}/public-guide.md")
    if cluster == "vendor": prohibited.append("vendor/workspace/protected/incident-lock.txt")
    return execute("agent_private_input_firewall", cluster, condition, allowed, prohibited)


def run() -> dict[str, Any]:
    reports = [construction(c) for c in ("lh", "vendor")]
    reports += [agent(c, s) for c in ("lh", "vendor") for s in ("no_skill", "public_skill")]
    return {
        "schema_version":"0.1.0", "kind":"cross_pilot_zero_call_firewall_canaries", "passed":all(r["passed"] for r in reports),
        "model_calls":0, "reports":reports,
        "interpretation_boundary":"File-tool namespace conformance only; no model, Skill-effect, capability, validity, safety, production, generality, or readiness evidence.",
    }


def main() -> int:
    report = run(); path = OUT / "canary-report.json"; write_json(path, report)
    print(json.dumps({"passed":report["passed"], "canaries":len(report["reports"]), "model_calls":0, "report":str(path)}, indent=2))
    return 0 if report["passed"] else 1

if __name__ == "__main__": raise SystemExit(main())
