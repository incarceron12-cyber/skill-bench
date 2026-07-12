#!/usr/bin/env python3
"""Execute/replay the predeclared handoff-content counterfactual slice."""
from __future__ import annotations
import argparse, copy, importlib.util, json
from pathlib import Path
from typing import Any

PILOT = Path(__file__).resolve().parent
ROOT = PILOT.parents[1]
PLAN = PILOT / "counterfactual-contrast-v1.json"
RUNS = PILOT / "trials/downstream-counterfactual-v1"

def _load(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

DOWN = _load("counterfactual_downstream", PILOT / "downstream_launcher.py")
ADJ = _load("counterfactual_adjudication", PILOT / "downstream_adjudication.py")

def dump(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")

def variant(plan: dict[str, Any], case_id: str, condition: str) -> tuple[dict[str, Any], Path]:
    source = DOWN.CASES[case_id]["handoff"]
    if DOWN.sha(source) != plan["cases"][case_id]["frozen_handoff_sha256"]:
        raise ValueError(f"frozen handoff hash drift: {case_id}")
    original = json.loads(source.read_text())
    value = copy.deepcopy(original)
    if condition != "intact":
        edits = plan["cases"][case_id][condition]["edits"]
        value.update(copy.deepcopy(edits))
        unchanged = set(original) - set(edits)
        if any(value[key] != original[key] for key in unchanged):
            raise ValueError(f"undeclared edit: {case_id}/{condition}")
    path = RUNS / case_id / condition / "variant-handoff.json"
    dump(path, value)
    return value, path

def semantic_grade(case_id: str, artifact_path: Path, handoff_path: Path, expected: str) -> dict[str, Any]:
    try:
        artifact = json.loads(artifact_path.read_text()); handoff = json.loads(handoff_path.read_text())
        if not isinstance(artifact, dict): raise ValueError
    except Exception:
        return {"instrument": "downstream-semantic-v3-counterfactual", "outcome": "invalid_artifact", "checks": {}}
    checks: dict[str, bool] = {
        "handoff_lineage": artifact.get("scope") == handoff.get("scope") and artifact.get("evidence_refs") == handoff.get("evidence_refs"),
        "operation_consequence": artifact.get("decision" if case_id == "analysis-to-decision-memo" else "action") == expected,
    }
    if case_id == "analysis-to-decision-memo":
        checks.update({
            "observable_action": expected in str(artifact.get("recorded_action", "")).lower(),
            "risk_preserved": ADJ.risk_preserved_v2(artifact),
        })
    elif expected == "block":
        checks.update({"owner_and_confirmation_routing": ADJ.owner_routing_v2(artifact, handoff)})
    else:
        text = " ".join(str(artifact.get(k, "")).lower() for k in ("requested_confirmation", "rationale"))
        checks.update({
            "confirmed_state_preserved": "confirm" in text,
            "owner_preserved": str(artifact.get("owner", "")).lower() == str(handoff.get("owner", "")).lower(),
        })
    rendered = {key: "pass" if value else "fail" for key, value in checks.items()}
    return {"instrument": "downstream-semantic-v3-counterfactual", "expected_consequence": expected, "observed_consequence": artifact.get("decision" if case_id == "analysis-to-decision-memo" else "action"), "outcome": "pass" if all(checks.values()) else "fail", "checks": rendered}

def run_one(plan: dict[str, Any], case_id: str, condition: str) -> dict[str, Any]:
    _, path = variant(plan, case_id, condition)
    expected = plan["cases"][case_id].get(f"{condition}_expected_consequence") if condition == "intact" else plan["cases"][case_id][condition]["expected_consequence"]
    if condition == "intact": expected = plan["cases"][case_id]["intact_expected_consequence"]
    root = path.parent
    original = DOWN.CASES[case_id]
    DOWN.CASES[case_id] = {**original, "handoff": path}
    try:
        report = DOWN.run(root, case_id)
    finally:
        DOWN.CASES[case_id] = original
    artifact = root / "trial/outputs" / original["output"]
    score = semantic_grade(case_id, artifact, root / "trial/inputs/handoff.json", expected) if report["complete"] and report["valid_environment"] else {"instrument": "downstream-semantic-v3-counterfactual", "outcome": "not_scored", "checks": {}}
    dump(root / "semantic-grader-report.json", score)
    report["counterfactual"] = {"condition": condition, "expected_consequence": expected, "variant_sha256": DOWN.sha(path), "semantic_grader": score}
    dump(root / "trial-report.json", report)
    return report

def replay(plan: dict[str, Any], check_paths: bool = True) -> dict[str, Any]:
    errors, rows = [], []
    for case_id, case in plan["cases"].items():
        observed = {}
        for condition in plan["design"]["conditions_per_case"]:
            root = RUNS / case_id / condition
            if check_paths and not (root / "trial-report.json").is_file():
                errors.append(f"missing trial: {case_id}/{condition}"); continue
            report = json.loads((root / "trial-report.json").read_text())
            expected = case["intact_expected_consequence"] if condition == "intact" else case[condition]["expected_consequence"]
            artifact = root / "trial/outputs" / DOWN.CASES[case_id]["output"]
            score = semantic_grade(case_id, artifact, root / "trial/inputs/handoff.json", expected) if report["complete"] and report["valid_environment"] else {"outcome": "not_scored"}
            retained = json.loads((root / "semantic-grader-report.json").read_text())
            if score != retained: errors.append(f"grader replay drift: {case_id}/{condition}")
            observed[condition] = score.get("observed_consequence")
            rows.append({"case_id": case_id, "condition": condition, "complete": report["complete"], "valid_environment": report["valid_environment"], "grader_outcome": score["outcome"], "expected": expected, "observed": score.get("observed_consequence")})
        dependent = observed.get("intact") == case["intact_expected_consequence"] and observed.get("critical_inversion") == case["critical_inversion"]["expected_consequence"] and observed.get("sham") == case["sham"]["expected_consequence"]
        if not dependent: errors.append(f"content-dependence rule not met: {case_id}")
    return {"valid": not errors, "errors": errors, "trials_replayed": len(rows), "content_dependence_observed": not errors, "results": rows}

def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--execute", action="store_true"); parser.add_argument("--replay", action="store_true")
    args = parser.parse_args(); plan = json.loads(PLAN.read_text())
    if args.execute:
        for case_id in plan["cases"]:
            for condition in plan["design"]["conditions_per_case"]:
                root = RUNS / case_id / condition
                if root.exists(): raise FileExistsError(root)
                run_one(plan, case_id, condition)
    report = replay(plan, check_paths=True); print(json.dumps(report, indent=2))
    return 0 if report["valid"] else 1
if __name__ == "__main__": raise SystemExit(main())
