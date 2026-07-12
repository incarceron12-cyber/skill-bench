#!/usr/bin/env python3
"""Execute predeclared fixed-trace model-judge conditions without oracle access."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
PROTOCOL = json.loads((HERE / "model-judge-protocol.json").read_text())
CASES = json.loads((HERE / "evaluator-inputs.json").read_text())
OUT = HERE / "model-runs"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def extract_json(text: str) -> dict:
    text = text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    return json.loads(text)


def validate(result: dict) -> None:
    if set(result) != {"rubric", "verdicts"} or not isinstance(result["rubric"], str):
        raise ValueError("output must contain exactly rubric and verdicts")
    expected = {c["case_id"] for c in CASES["cases"]}
    verdicts = result["verdicts"]
    if not isinstance(verdicts, list) or {v.get("case_id") for v in verdicts} != expected or len(verdicts) != len(expected):
        raise ValueError("each frozen case_id must occur exactly once")
    for verdict in verdicts:
        if set(verdict) != {"case_id", "verdict", "reason"} or verdict["verdict"] not in {"pass", "fail", "abstain"}:
            raise ValueError("invalid verdict record")


def prompt(condition: dict) -> str:
    return """You are an unrestricted evaluator of synthetic knowledge-work records. Judge only the supplied fields; do not infer an oracle, hidden reference, professional norm, or omitted fact.\n\nCONDITION:\n%s\n\nReturn JSON only with exactly this shape: {\"rubric\":\"...\",\"verdicts\":[{\"case_id\":\"...\",\"verdict\":\"pass|fail|abstain\",\"reason\":\"...\"}]}. Include every case exactly once.\n\nFROZEN CASES:\n%s""" % (condition["rubric_instruction"], json.dumps(CASES, sort_keys=True))


def main() -> int:
    if OUT.exists():
        raise FileExistsError(f"refusing to overwrite retained stochastic evidence: {OUT}")
    OUT.mkdir()
    calls = 0
    for condition in PROTOCOL["conditions"]:
        for repeat in range(1, condition["repeats"] + 1):
            calls += 1
            stem = f"{condition['condition_id']}-r{repeat}"
            usage = OUT / f"{stem}-usage.json"
            cmd = [PROTOCOL["configured_system"]["runtime"], "-z", prompt(condition), "--usage-file", str(usage),
                   "--model", PROTOCOL["configured_system"]["model"], "--provider", PROTOCOL["configured_system"]["provider"],
                   "--safe-mode"]
            if PROTOCOL["configured_system"]["toolsets"] != "none":
                cmd.extend(["--toolsets", PROTOCOL["configured_system"]["toolsets"]])
            proc = subprocess.run(cmd, text=True, capture_output=True, timeout=PROTOCOL["configured_system"]["timeout_seconds"])
            (OUT / f"{stem}-stderr.log").write_text(proc.stderr)
            raw = OUT / f"{stem}-raw.txt"
            raw.write_text(proc.stdout)
            record = {"condition_id": condition["condition_id"], "repeat": repeat, "returncode": proc.returncode,
                      "protocol_sha256": sha(HERE / "model-judge-protocol.json"), "inputs_sha256": sha(HERE / "evaluator-inputs.json"),
                      "raw_sha256": sha(raw), "usage_sha256": sha(usage) if usage.exists() else None, "valid": False}
            try:
                if proc.returncode != 0:
                    raise ValueError(f"provider return code {proc.returncode}")
                result = extract_json(proc.stdout)
                validate(result)
                record["result"] = result
                record["valid"] = True
            except (ValueError, json.JSONDecodeError) as exc:
                record["invalid_reason"] = str(exc)
            (OUT / f"{stem}.json").write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
    manifest = {"status": "executed", "calls": calls, "protocol_sha256": sha(HERE / "model-judge-protocol.json"),
                "inputs_sha256": sha(HERE / "evaluator-inputs.json"), "oracle_access": False,
                "records": [f"{c['condition_id']}-r{r}.json" for c in PROTOCOL["conditions"] for r in range(1, c["repeats"] + 1)]}
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    print(json.dumps(manifest, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
