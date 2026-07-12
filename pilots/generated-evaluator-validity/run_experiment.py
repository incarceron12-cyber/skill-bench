#!/usr/bin/env python3
"""Generate and replay evaluator code against independent, frozen oracle cases.

Design basis: papers/agent-benchmarks/2026-07-12-evalagent-domain-evaluation-skill-validity.md
The generated program never receives oracle labels. This internal experiment tests evaluator
engineering and planted-case discrimination only; it cannot establish professional validity.
"""
from __future__ import annotations
import argparse, hashlib, json, os, re, subprocess, sys, tempfile, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CASES = ROOT / "frozen-cases.json"
PROCEDURE = ROOT / "evaluation-procedure.md"
OUT = ROOT / "trials"
MODEL = "gpt-5.6-sol"
PROVIDER = "openai-codex"

BASE = """Create a Python 3 evaluator named evaluator.py. It must read one JSON object from stdin and print exactly one JSON object with keys outcome and diagnostic. Supported work_shape values are stateful_workflow and artifact_view. Infer the intended checks from the following criterion contract and unlabeled development examples. Use only the standard library. Return only one fenced python code block.

CRITERIA (independently authored and frozen):
1. stateful_workflow: accept only when a required approval event exists, is successful, and occurs before commit. If the required event channel is declared truncated or missing, abstain with outcome insufficient_evidence. Ignore irrelevant note text and event IDs. A success-looking note must not substitute for the approval event.
2. artifact_view: accept only when authoritative structured state says status=approved and observed rendering is valid. A missing required structured view means insufficient_evidence; invalid export means invalid_artifact. Ignore renderer theme and field ordering. Visible text claiming APPROVED must not override structured state.

DEVELOPMENT EXAMPLES (no oracle labels):
{"work_shape":"stateful_workflow","events":[{"kind":"approval","ok":true},{"kind":"commit","ok":true}],"channel_state":"complete","note":"done"}
{"work_shape":"artifact_view","structured":{"status":"approved"},"render":{"valid":true,"theme":"light","text":"Approved"}}
"""


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def extract_code(text: str) -> str:
    blocks = re.findall(r"```(?:python)?\s*\n(.*?)```", text, re.S)
    if len(blocks) != 1:
        raise ValueError(f"expected one code block, got {len(blocks)}")
    return blocks[0].strip() + "\n"


def generate(condition: str, execute: bool) -> dict:
    trial = OUT / condition
    trial.mkdir(parents=True, exist_ok=True)
    prompt = BASE
    if condition == "procedure_guidance":
        prompt += "\nEVALUATION PROCEDURE:\n" + PROCEDURE.read_text()
    (trial / "prompt.txt").write_text(prompt)
    usage = trial / "usage.json"
    response = trial / "response.txt"
    code = trial / "evaluator.py"
    if execute:
        started = time.time()
        proc = subprocess.run(["hermes", "-z", prompt, "--usage-file", str(usage), "-m", MODEL, "--provider", PROVIDER, "-t", ""], text=True, capture_output=True, timeout=600, cwd=trial)
        response.write_text(proc.stdout)
        (trial / "stderr.txt").write_text(proc.stderr)
        if proc.returncode != 0:
            raise RuntimeError(f"generation failed for {condition}: {proc.returncode}")
        code.write_text(extract_code(proc.stdout))
        elapsed = time.time() - started
    else:
        elapsed = None
    return {"condition": condition, "prompt_sha256": sha(trial / "prompt.txt"), "code_sha256": sha(code) if code.exists() else None, "generation_seconds": elapsed}


def replay(condition: str) -> dict:
    trial = OUT / condition
    code = trial / "evaluator.py"
    cases = json.loads(CASES.read_text())["cases"]
    compile_proc = subprocess.run([sys.executable, "-m", "py_compile", str(code)], text=True, capture_output=True)
    results = []
    for case in cases:
        proc = subprocess.run([sys.executable, "-I", str(code)], input=json.dumps(case["input"]), text=True, capture_output=True, timeout=5, cwd=trial)
        try: observed = json.loads(proc.stdout)
        except Exception: observed = {"outcome":"execution_error","diagnostic":proc.stderr or proc.stdout}
        results.append({"case_id":case["case_id"],"shape":case["input"]["work_shape"],"category":case["category"],"expected":case["oracle"],"observed":observed,"pass":observed.get("outcome")==case["oracle"]["outcome"]})
    categories = {}
    for row in results:
        categories.setdefault(row["category"], []).append(row["pass"])
    return {"condition":condition,"syntax_import":compile_proc.returncode==0,"case_count":len(results),"passed":sum(r["pass"] for r in results),"category_scores":{k:{"passed":sum(v),"total":len(v)} for k,v in categories.items()},"results":results}


def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("--generate",action="store_true"); args=ap.parse_args()
    retained_path = ROOT / "replay-report.json"
    retained = json.loads(retained_path.read_text()) if retained_path.exists() else {}
    if args.generate:
        metadata = [generate(c, True) for c in ("no_guidance", "procedure_guidance")]
        generated_at = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    else:
        # A replay must not erase generation-time evidence or pretend a new generation occurred.
        metadata = retained["generation"] if "generation" in retained else [generate(c, False) for c in ("no_guidance", "procedure_guidance")]
        generated_at = retained.get("generated_at", "unknown")
    report={"schema_version":"1.0","generated_at":generated_at,"model":MODEL,"provider":PROVIDER,"harness":"hermes-oneshot-final-code-only","cases_sha256":sha(CASES),"procedure_sha256":sha(PROCEDURE),"generation":metadata,"conditions":[replay(c) for c in ("no_guidance","procedure_guidance")],"claim_limits":["criterion equivalence","evaluator expertise transfer","professional validity","deployment readiness"]}
    (ROOT/"replay-report.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2)); return 0
if __name__=="__main__": raise SystemExit(main())
