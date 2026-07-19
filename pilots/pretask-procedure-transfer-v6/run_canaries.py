#!/usr/bin/env python3
"""Run v6 zero-call filesystem-isolation and equal-envelope canaries."""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sandbox(inputs: Path, outputs: Path, command: list[str]) -> list[str]:
    return ["bwrap", "--die-with-parent", "--new-session", "--unshare-pid", "--unshare-net",
            "--proc", "/proc", "--dev", "/dev", "--tmpfs", "/tmp",
            "--ro-bind", "/usr", "/usr", "--ro-bind", "/bin", "/bin",
            "--ro-bind", "/lib", "/lib", "--ro-bind", "/lib64", "/lib64",
            "--dir", "/home", "--dir", "/home/sam", "--ro-bind", str(inputs), "/trial",
            "--bind", str(outputs), "/trial/outputs", "--chdir", "/trial",
            "--setenv", "HOME", "/home/sam", "--setenv", "TERMINAL_CWD", "/trial", "--", *command]


def observation_passes(observed: dict[str, Any], returncode: int, expected: list[str]) -> bool:
    """Fail closed unless every declared isolation property is observed."""
    return (returncode == 0 and observed.get("cwd") == "/trial" and observed.get("visible") == expected
            and observed.get("repo_exists") is False and observed.get("private_exists") is False
            and observed.get("output_write") is True and observed.get("outside_write_succeeded") is False)


PROBE = r'''
import json, os
from pathlib import Path
repo = Path('/home/sam/skill-bench')
out = Path('outputs/canary.txt')
out.write_text('v6-canary\n')
outside_ok = True
try:
    Path('escape.txt').write_text('bad\n')
except OSError:
    outside_ok = False
print(json.dumps({'cwd': os.getcwd(), 'visible': sorted(os.listdir('.')), 'repo_exists': repo.exists(),
                  'private_exists': Path('/trial/private.json').exists(), 'output_write': out.read_text() == 'v6-canary\n',
                  'outside_write_succeeded': outside_ok}, sort_keys=True))
'''


def arm_canary(name: str, support: Path | None, root: Path) -> dict[str, Any]:
    inputs, outputs = root / name / "inputs", root / name / "outputs"
    inputs.mkdir(parents=True); outputs.mkdir()
    shutil.copy2(HERE / "tasks/k4n7/public.md", inputs / "public-task.md")
    shutil.copy2(HERE / "tasks/k4n7/input.json", inputs / "input.json")
    if support:
        shutil.copy2(support, inputs / "procedure-package.json")
    # bubblewrap cannot create a nested bind target beneath an existing
    # read-only bind. Materialize the empty mountpoint before binding inputs;
    # the sibling host output root is then overlaid at exactly that path.
    (inputs / "outputs").mkdir()
    expected = sorted(path.name for path in inputs.iterdir())
    command = ["/usr/bin/python3", "-c", PROBE]
    proc = subprocess.run(sandbox(inputs, outputs, command), text=True, capture_output=True, timeout=30)
    try:
        observed = json.loads(proc.stdout.strip().splitlines()[-1])
    except (json.JSONDecodeError, IndexError):
        observed = {}
    passed = observation_passes(observed, proc.returncode, expected)
    signature = sandbox(Path("<inputs>"), Path("<outputs>"), command)
    return {"arm": name, "passed": passed, "model_calls": 0, "expected_visible": expected,
            "observed": observed, "returncode": proc.returncode, "stderr": proc.stderr[-1000:],
            "sandbox_signature": signature,
            "input_hashes": {path.name: sha(path) for path in inputs.iterdir() if path.is_file()}}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, default=HERE / "canary-report.json")
    args = parser.parse_args()
    protocol = json.loads((HERE / "protocol.json").read_text())
    with tempfile.TemporaryDirectory(prefix="v6-canary-") as tmp:
        root = Path(tmp)
        arms = [arm_canary("no-package", None, root),
                arm_canary("reference", ROOT / "pilots/pretask-procedure-transfer-v4/controls/epsilon/reference.json", root)]
    envelope = protocol["equal_envelope"]
    condition_ids = {row["condition_id"] for row in protocol["conditions"]}
    equal = (set(envelope["applies_to_all_conditions"]) == condition_ids
             and all(row["resource_envelope_id"] == envelope["envelope_id"] for row in protocol["conditions"])
             and arms[0]["sandbox_signature"] == arms[1]["sandbox_signature"])
    report = {"status": "PASS" if equal and all(row["passed"] for row in arms) else "FAIL",
              "model_calls": 0, "provider_calls": 0, "executor_attempts": 0,
              "isolation_canary": "pass" if all(row["passed"] for row in arms) else "fail",
              "equal_envelope_canary": "pass" if equal else "fail", "arms": arms,
              "scope": "Zero-call outer-envelope conformance only; not agent execution or capability evidence."}
    args.report.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
