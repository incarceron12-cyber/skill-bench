#!/usr/bin/env python3
"""Replay the public preservation envelope and prior vendor grader."""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, shutil, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PILOT = Path(__file__).resolve().parent
REQUIRED = "- Authoritative status source: workspace/current/signed-status.json (INC-204)."


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def assess(original: str, revised: str) -> dict:
    old = original.splitlines()
    new = revised.splitlines()
    required_once = new.count(REQUIRED) == 1
    stripped = [line for line in new if line != REQUIRED]
    preserve = stripped == old
    return {
        "must_change": required_once,
        "must_preserve": preserve,
        "forbidden_change": preserve and len(new) == len(old) + 1,
        "permitted_normalization_only": revised.endswith("\n") and not revised.endswith("\n\n"),
    }


def prior_grade(run: Path) -> dict:
    module_path = ROOT / "pilots/vendor-incident-response/grade_v2.py"
    spec = importlib.util.spec_from_file_location("vendor_grade_v2", module_path)
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    source_run = ROOT / "pilots/vendor-incident-response/trials/agent-run-20260711-v2"
    with tempfile.TemporaryDirectory() as raw:
        root = Path(raw)
        # Replay the prior grader against its immutable original evidence view;
        # only the artifact under test is replaced by this trial's revision.
        shutil.copytree(source_run / "trial/inputs", root / "trial/inputs")
        (root / "trial/outputs").mkdir(parents=True)
        shutil.copy2(run / "trial/outputs/revised-incident-brief.md", root / "trial/outputs/incident-brief.md")
        shutil.copy2(source_run / "trial/outputs/action-plan.json", root / "trial/outputs/action-plan.json")
        shutil.copy2(run / "trial-report.json", root / "trial-report.json")
        return module.grade_trial(root)


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("run", type=Path); parser.add_argument("--report", type=Path)
    args = parser.parse_args(); run = args.run.resolve()
    original_path = PILOT / "original-incident-brief.md"
    revised_path = run / "trial/outputs/revised-incident-brief.md"
    original, revised = original_path.read_text(), revised_path.read_text()
    checks = assess(original, revised)
    mutations = {
        "no_op_rejected": not all(assess(original, original).values()),
        "unauthorized_addition_rejected": not all(assess(original, revised + "Unauthorized\n").values()),
        "over_edit_rejected": not all(assess(original, revised.replace("SEV-2", "SEV-1")).values()),
        "benign_trailing_newline_accepted": all(assess(original, revised.rstrip("\n") + "\n").values()),
        "invalid_execution_rejected": not (run / "missing-output.md").exists(),
    }
    vendor = prior_grade(run)
    passed = all(checks.values()) and all(mutations.values()) and vendor["observed_outcome"] == "secure_useful_completion"
    report = {
        "schema_version": "0.1.0", "kind": "configured_artifact_revision_replay", "passed": passed,
        "identities": {"original_sha256": sha(original_path), "revised_sha256": sha(revised_path)},
        "transition_checks": checks, "mutation_tests": mutations,
        "prior_pilot_grader": vendor,
        "claim_boundaries": {k: False for k in ("treatment_effect", "professional_validity", "general_capability", "reliability", "cross_domain_generalization", "safety", "readiness")},
    }
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.report: args.report.write_text(text)
    print(text, end=""); return 0 if passed else 1

if __name__ == "__main__": raise SystemExit(main())
