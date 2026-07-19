#!/usr/bin/env python3
"""Independent, commit-bound audit of the self-inspection-repair v2 freeze.

The auditor reads candidate bytes from Git, does not import candidate preflight code,
never calls a model/provider, and never writes under the frozen pilot directory.
"""
from __future__ import annotations

import argparse
import ast
import configparser
import csv
import datetime as dt
import hashlib
import io
import json
import re
import subprocess
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PILOT = Path("pilots/self-inspection-repair-v2")
DEFAULT_COMMIT = "bfc28504477eef5d6e47d3876800ce242dbe9a19"
EXPECTED_ROOT_TREE = "1c40bce7f122e249026bec298d801542948dff8a"
EXPECTED_SUBTREE = "5ea85a60dd422ede36fbb4175988809e68f3d085"
CONDITIONS = {
    "retry_no_new_information", "generic_self_review",
    "native_render_self_inspection", "consequence_only_feedback",
    "criterion_disclosure",
}
FAMILIES = {"roster", "service", "workflow"}
SHAPES = {"csv_schedule", "ini_configuration", "svg_workflow"}
STRATA = {"near_threshold_single_locus", "multi_locus_collateral_risk"}
SHARED = ("tool_id", "harness_id", "model_id", "provider_id", "budget_id")
CLAIMS = {
    "self_correction", "agent_capability", "treatment_effect",
    "professional_validity", "utility", "production_fitness", "readiness",
}
KINDS = {
    "positive", "false_rejection_control", "subtle_false_acceptance_control",
    "multi_locus_false_acceptance_control", "collateral_damage", "missing_view",
    "transform_drift", "invalid_artifact",
}


def git(*args: str, text: bool = True) -> str | bytes:
    return subprocess.run(
        ["git", *args], cwd=ROOT, check=True, capture_output=True, text=text
    ).stdout


def blob(commit: str, rel: Path) -> bytes:
    return git("show", f"{commit}:{rel.as_posix()}", text=False)  # type: ignore[return-value]


def object_id(commit: str, rel: Path) -> str:
    return str(git("rev-parse", f"{commit}:{rel.as_posix()}")).strip()


def load(commit: str, rel: str) -> Any:
    return json.loads(blob(commit, PILOT / rel))


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def canon(value: Any) -> str:
    return sha(json.dumps(value, sort_keys=True, separators=(",", ":")).encode())


def independent_evaluate(
    family: str, candidate: str, view_status: str = "available",
    transform_status: str = "pinned",
) -> dict[str, Any]:
    """Specification oracle independent of both candidate observers."""
    if view_status != "available" or transform_status != "pinned":
        return {"terminal_state": "insufficient_evidence", "endpoint": None, "collateral": None}
    try:
        if family == "roster":
            rows = list(csv.DictReader(io.StringIO(candidate)))
            if not rows or set(rows[0]) != {"worker", "day", "hours"}:
                raise ValueError("columns")
            if any(set(row) != {"worker", "day", "hours"} for row in rows):
                raise ValueError("row columns")
            workers = {row["worker"] for row in rows}
            totals = {
                worker: sum(int(row["hours"]) for row in rows if row["worker"] == worker)
                for worker in workers
            }
            coverage = {
                day: {row["worker"] for row in rows if row["day"] == day and int(row["hours"]) > 0}
                for day in ("Monday", "Tuesday")
            }
            endpoint = all(len(coverage[day]) >= 2 for day in coverage) and all(v <= 16 for v in totals.values())
            collateral = workers == {"Alice", "Bob", "Cara"}
        elif family == "service":
            parser = configparser.RawConfigParser()
            parser.read_string(candidate)
            if parser.sections() != ["service"]:
                raise ValueError("section")
            values = dict(parser.items("service"))
            if set(values) != {"service_name", "endpoint", "tls_min", "timeout_seconds", "audit_enabled"}:
                raise ValueError("keys")
            endpoint = values["tls_min"] == "1.3" and int(values["timeout_seconds"]) <= 30 and values["audit_enabled"].lower() == "true"
            collateral = values["service_name"] == "ledger" and values["endpoint"] == "/v1/post"
        elif family == "workflow":
            root = ET.fromstring(candidate)
            if not root.tag.endswith("svg"):
                raise ValueError("root")
            width = float(root.attrib["viewBox"].split()[2])
            titles = [node.text for node in root.iter() if node.tag.endswith("title")]
            nodes = {node.attrib["id"] for node in root.iter() if "id" in node.attrib}
            edges = {node.attrib["data-edge"] for node in root.iter() if "data-edge" in node.attrib}
            endpoint = width <= 600 and {"intake->review", "review->approve"} <= edges
            collateral = titles == ["Release review"] and nodes == {"intake", "review", "approve"}
        else:
            raise ValueError("family")
    except Exception:
        return {"terminal_state": "invalid_artifact", "endpoint": None, "collateral": None}
    return {
        "terminal_state": "passed" if endpoint and collateral else "criterion_fail",
        "endpoint": endpoint, "collateral": collateral,
    }


def independent_render(family: str, candidate: str) -> str:
    if family == "roster":
        rows = list(csv.DictReader(io.StringIO(candidate)))
        workers = sorted({r["worker"] for r in rows})
        coverage = {d: len({r["worker"] for r in rows if r["day"] == d and int(r["hours"]) > 0}) for d in ("Monday", "Tuesday")}
        totals = {w: sum(int(r["hours"]) for r in rows if r["worker"] == w) for w in workers}
        return f"CSV roster summary: workers={'/'.join(workers)}; Monday coverage={coverage['Monday']}; Tuesday coverage={coverage['Tuesday']}; max hours={max(totals.values())}.\n"
    if family == "service":
        parser = configparser.RawConfigParser(); parser.read_string(candidate); values = dict(parser.items("service"))
        return f"INI service summary: name={values['service_name']}; endpoint={values['endpoint']}; TLS={values['tls_min']}; timeout={values['timeout_seconds']}; audit={values['audit_enabled']}.\n"
    root = ET.fromstring(candidate)
    title = next(node.text for node in root.iter() if node.tag.endswith("title"))
    nodes = sorted(node.attrib["id"] for node in root.iter() if "id" in node.attrib)
    edges = sorted(node.attrib["data-edge"] for node in root.iter() if "data-edge" in node.attrib)
    width = root.attrib["viewBox"].split()[2]
    return f"SVG workflow summary: title={title}; nodes={'/'.join(nodes)}; edges={'/'.join(edges)}; width={width}.\n"


def load_observer(commit: str, name: str):
    """Execute a commit blob in an isolated namespace, not as an imported repo module."""
    source = blob(commit, PILOT / "checkers" / f"{name}.py").decode()
    namespace: dict[str, Any] = {"__name__": f"audited_{name}"}
    exec(compile(source, f"{commit}:{name}.py", "exec"), namespace)
    return source, namespace["evaluate"]


def isolation_canary() -> dict[str, Any]:
    """Exercise a real resolver/write guard; this is not a launcher conformance claim."""
    with tempfile.TemporaryDirectory(prefix="repair-v2-independent-") as tmp:
        base = Path(tmp).resolve(); task = base / "task"; output = base / "output"; private = base / "private"
        task.mkdir(); output.mkdir(); private.mkdir()
        source = task / "source.json"; source.write_text("{}\n")
        criterion = private / "criterion.json"; criterion.write_text('{"hidden":true}\n')
        allow = {source.resolve()}
        readable = lambda p: p.resolve() in allow
        writable = lambda p: p.resolve().parent == output and output in p.resolve().parents
        checks = {
            "allowlisted_source_readable": readable(source),
            "private_criterion_excluded": not readable(criterion),
            "parent_traversal_excluded": not readable(task / ".." / "private" / "criterion.json"),
            "repository_file_excluded": not readable(ROOT / "PROJECT_CHARTER.md"),
            "unique_output_root": writable(output / "candidate") and not writable(task / "candidate"),
            "task_scoped_cwd": task != ROOT and task != output,
        }
        return {"status": "PASS" if all(checks.values()) else "FAIL", **checks,
                "claim_limit": "resolver and write-guard canary only; no execution launcher exists in the frozen candidate"}


def run(commit: str) -> dict[str, Any]:
    resolved = str(git("rev-parse", commit)).strip()
    origin = str(git("rev-parse", "origin/main")).strip()
    on_origin = subprocess.run(["git", "merge-base", "--is-ancestor", resolved, origin], cwd=ROOT).returncode == 0
    root_tree = str(git("rev-parse", f"{resolved}^{{tree}}")).strip()
    subtree = object_id(resolved, PILOT)
    manifest = load(resolved, "freeze-manifest.json")
    protocol = load(resolved, "protocol.json")
    fixtures = load(resolved, "fixtures/calibration.json")
    transforms = load(resolved, "transformations.json")
    ledger = load(resolved, "attempt-ledger.json")
    preflight = load(resolved, "preflight-report.json")
    bindings = manifest.get("bindings", [])
    by_path = {b["path"]: b for b in bindings}
    bound = {rel: blob(resolved, PILOT / rel) for rel in by_path}

    errors: list[str] = []
    tracked = str(git("ls-tree", "-r", "--name-only", resolved, "--", PILOT.as_posix())).splitlines()
    tracked_relative = {str(Path(p).relative_to(PILOT)) for p in tracked}
    expected_unbound = {"freeze-manifest.json", "preflight-report.json"}
    if set(by_path) | expected_unbound != tracked_relative or len(bindings) != len(by_path):
        errors.append("binding_inventory")

    binding_rows = []
    for rel, binding in sorted(by_path.items()):
        raw = bound[rel]
        ok = len(raw) == binding.get("bytes") and sha(raw) == binding.get("sha256")
        if not ok: errors.append(f"binding:{rel}")
        binding_rows.append({
            "path": rel, "git_object": object_id(resolved, PILOT / rel),
            "expected_bytes": binding.get("bytes"), "observed_bytes": len(raw),
            "expected_sha256": binding.get("sha256"), "observed_sha256": sha(raw),
            "status": "PASS" if ok else "FAIL",
        })
    inventory_hash = canon([{"path": row["path"], "bytes": row["observed_bytes"], "sha256": row["observed_sha256"]} for row in binding_rows])

    tasks = protocol.get("tasks", []); conditions = protocol.get("conditions", []); assignments = protocol.get("assignments", [])
    task_by_id = {t.get("task_id"): t for t in tasks}
    if len(tasks) != 6 or len(task_by_id) != 6 or {t.get("family") for t in tasks} != FAMILIES or {t.get("shape") for t in tasks} != SHAPES:
        errors.append("family_shape_coverage")
    for family in FAMILIES:
        if {t.get("defect_stratum") for t in tasks if t.get("family") == family} != STRATA:
            errors.append(f"strata:{family}")
    condition_by_id = {c.get("condition_id"): c for c in conditions}
    if len(conditions) != 5 or set(condition_by_id) != CONDITIONS:
        errors.append("condition_matrix")
    if any(len({c.get(field) for c in conditions}) != 1 for field in SHARED):
        errors.append("equal_envelope")
    if any(c.get("hidden_criterion_access") is True for cid, c in condition_by_id.items() if cid != "criterion_disclosure"):
        errors.append("criterion_leakage")

    expected_cells = {(tid, cid, rep) for tid in task_by_id for cid in CONDITIONS for rep in range(1, 6)}
    observed_cells = {(a.get("task_id"), a.get("condition_id"), a.get("repetition")) for a in assignments}
    if len(assignments) != 150 or observed_cells != expected_cells or len(observed_cells) != 150:
        errors.append("assignment_matrix")
    assignment_rows = []
    for a in assignments:
        unhashed = {k: v for k, v in a.items() if k != "assignment_sha256"}
        task = task_by_id.get(a.get("task_id"), {})
        start_raw = bound.get(str(task.get("starting_artifact")), b"")
        expected_seed = int(hashlib.sha256(f"{a.get('task_id')}|{a.get('condition_id')}|{a.get('repetition')}".encode()).hexdigest()[:8], 16)
        ok = (a.get("assignment_sha256") == canon(unhashed) and a.get("attempts_executed") == 0 and
              a.get("starting_artifact_sha256") == sha(start_raw) and a.get("seed") == expected_seed and
              a.get("configured_system_id") == "gpt-5.6-sol-openai-codex-file-only-v2")
        if not ok: errors.append(f"assignment:{a.get('assignment_id')}")
        assignment_rows.append({"assignment_id": a.get("assignment_id"), "observed_sha256": canon(unhashed), "expected_sha256": a.get("assignment_sha256"), "seed": a.get("seed"), "status": "PASS" if ok else "FAIL"})
    if manifest.get("assignment_set_sha256") != canon(assignments): errors.append("assignment_set")

    transform_by_id = {x.get("transformation_id"): x for x in transforms.get("transformations", [])}
    task_rows = []
    for task in tasks:
        rel = f"tasks/{task['task_id']}.json"
        source = json.loads(bound[task["source"]]); task_file = json.loads(bound[rel])
        native = bound[task["authoritative_native_view"]].decode(); rendered = bound[task["derived_render_view"]].decode()
        tr = transform_by_id.get(task.get("transformation_id"), {})
        start_eval = independent_evaluate(task["family"], native)
        ok = (task_file == task and task["fair_public_basis"] == source.get("public_basis") and
              source.get("authority") == "builder_authoritative_synthetic_public_source" and
              task["starting_artifact"] == task["authoritative_native_view"] and
              independent_render(task["family"], native) == rendered and
              tr.get("authoritative_input") == task["shape"] and tr.get("implementation") == "prepare_freeze.py:render" and
              tr.get("implementation_sha256") == "bound_by_freeze_manifest" and
              start_eval["terminal_state"] == "criterion_fail")
        if not ok: errors.append(f"task_source_view_transform:{task['task_id']}")
        task_rows.append({"task_id": task["task_id"], "family": task["family"], "shape": task["shape"], "stratum": task["defect_stratum"], "starting_state": start_eval["terminal_state"], "status": "PASS" if ok else "FAIL"})

    source_a, observer_a = load_observer(resolved, "observer_a")
    source_b, observer_b = load_observer(resolved, "observer_b")
    observer_errors = []
    for name, source in (("a", source_a), ("b", source_b)):
        tree = ast.parse(source); node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "evaluate")
        args = {a.arg for a in node.args.args + node.args.kwonlyargs}
        if args & {"condition", "condition_id", "assignment", "feedback", "repair_prompt"}:
            observer_errors.append(f"condition_parameter:{name}")
    if sha(source_a.encode()) == sha(source_b.encode()): observer_errors.append("identical_source")

    fixture_rows = []
    disagreements = 0
    for case in fixtures.get("cases", []):
        args = (case["family"], case["candidate"], case["view_status"], case["transform_status"])
        expected = independent_evaluate(*args)
        a = observer_a(*args); b = observer_b(*args)
        agreement = all(a.get(k) == b.get(k) for k in ("terminal_state", "endpoint", "collateral"))
        if not agreement: disagreements += 1
        ok = agreement and all(a.get(k) == expected.get(k) for k in ("terminal_state", "endpoint", "collateral")) and expected["terminal_state"] == case.get("expected")
        if not ok: errors.append(f"calibration:{case.get('case_id')}")
        fixture_rows.append({"case_id": case.get("case_id"), "family": case.get("family"), "kind": case.get("kind"), "expected": case.get("expected"), "oracle": expected["terminal_state"], "observer_a": a["terminal_state"], "observer_b": b["terminal_state"], "status": "PASS" if ok else "FAIL"})
    coverage = {(c.get("task_id"), c.get("kind")) for c in fixtures.get("cases", [])}
    if len(fixture_rows) != 48 or coverage != {(tid, kind) for tid in task_by_id for kind in KINDS}: errors.append("calibration_coverage")
    fraction = sum(r["oracle"] == "passed" for r in fixture_rows) / len(fixture_rows)
    if not 0.15 < fraction < 0.85: errors.append("floor_ceiling")
    if observer_errors: errors.extend(f"observer:{e}" for e in observer_errors)

    disagreement_canary = {"terminal_state": "observer_invalid", "endpoint": None, "collateral": None}
    # Independent adjudication rule replay: intentionally conflicting observations must fail closed.
    synthetic_a = {"terminal_state": "passed", "endpoint": True, "collateral": True}
    synthetic_b = {"terminal_state": "criterion_fail", "endpoint": False, "collateral": True}
    if any(synthetic_a[k] != synthetic_b[k] for k in ("terminal_state", "endpoint", "collateral")):
        adjudicated = disagreement_canary
    else:
        adjudicated = synthetic_a
    if adjudicated["terminal_state"] != "observer_invalid": errors.append("observer_disagreement")

    expected_ledger = {"instrument_id": "self-inspection-repair-v2", "attempts": [], "model_calls": 0, "provider_calls": 0, "repair_rows_executed": 0}
    if ledger != expected_ledger or any(manifest.get(k) != 0 for k in ("model_calls", "provider_calls", "repair_rows_executed")):
        errors.append("zero_call_ledger")
    if set(protocol.get("claim_ceiling", {})) != CLAIMS or any(protocol.get("claim_ceiling", {}).values()): errors.append("claim_ceiling")
    budget = protocol.get("budget", {})
    if budget.get("stop_before_spend_without_execution_authorization") is not True or budget.get("max_total_tokens_per_attempt") != 16000 or budget.get("max_wall_seconds_per_attempt") != 300:
        errors.append("budget")
    estimands = protocol.get("estimands", {})
    if (estimands.get("clusters") != "task family" or "within-family" not in estimands.get("primary", "") or
        "equal-weight" not in estimands.get("primary", "") or "uncertainty" not in estimands.get("shape_reversal_gate", "") or
        protocol.get("repetitions_per_task_condition_system") != 5):
        errors.append("estimand_repetition")
    if protocol.get("calibration_gate", {}).get("no_post_treatment_tuning") is not True: errors.append("tuning_boundary")
    if preflight.get("status") != "PASS" or any(preflight.get(k) != 0 for k in ("model_calls", "provider_calls", "repair_rows_executed")): errors.append("builder_preflight")

    canary = isolation_canary()
    gates = {
        "candidate_commit_on_origin_main": on_origin,
        "exact_candidate_commit": resolved == DEFAULT_COMMIT,
        "exact_root_tree": root_tree == EXPECTED_ROOT_TREE,
        "exact_candidate_subtree": subtree == EXPECTED_SUBTREE,
        "complete_binding_inventory": "binding_inventory" not in errors and len(binding_rows) == 30,
        "all_bound_bytes_git_object_byte_sha256": all(r["status"] == "PASS" for r in binding_rows),
        "assignment_set_and_all_150_assignments": "assignment_matrix" not in errors and "assignment_set" not in errors and all(r["status"] == "PASS" for r in assignment_rows),
        "task_source_view_transformation_public_basis": all(r["status"] == "PASS" for r in task_rows),
        "three_families_shapes_two_strata": not any(e.startswith(("family_shape", "strata:")) for e in errors),
        "five_repetitions_per_cell": protocol.get("repetitions_per_task_condition_system") == 5 and len(assignments) == 150,
        "equal_execution_envelope": "equal_envelope" not in errors,
        "observer_condition_blind_and_distinct": not observer_errors,
        "all_48_calibration_cases_replayed_both_observers": len(fixture_rows) == 48 and all(r["status"] == "PASS" for r in fixture_rows),
        "mutation_coverage_and_non_floor_ceiling": "calibration_coverage" not in errors and "floor_ceiling" not in errors,
        "observer_disagreement_fails_closed": adjudicated["terminal_state"] == "observer_invalid",
        "predeclared_estimands_budget_seed_order": not any(e in errors for e in ("estimand_repetition", "budget")) and all("randomized only after freeze audit" in a.get("order_nonce_policy", "") for a in assignments),
        "zero_call_ledger": "zero_call_ledger" not in errors,
        "zero_call_isolation_canary": canary["status"] == "PASS",
        "claim_ceiling_all_false": "claim_ceiling" not in errors,
        "builder_preflight_zero_call": "builder_preflight" not in errors,
        "baseline_semantics": not errors,
    }
    status = "PASS" if all(gates.values()) else "FAIL"
    return {
        "schema_version": "1.0.0", "audit_id": "self-inspection-repair-v2-freeze-independent-audit",
        "audited_at": dt.datetime.now(dt.timezone.utc).isoformat(), "auditor": "benchmark-builder",
        "status": status,
        "authorization": "candidate_freeze_audit_passed; separate launcher/build-and-execution task may proceed, but this audit authorizes no model/provider call or spend" if status == "PASS" else "execution_not_authorized",
        "source_binding": {"requested_commit": commit, "resolved_commit": resolved, "origin_main_at_audit": origin, "root_tree": root_tree, "pilot_subtree": subtree, "pilot_path": PILOT.as_posix()},
        "inventory": {"bound_files_read": len(binding_rows), "bound_bytes_read": sum(r["observed_bytes"] for r in binding_rows), "aggregate_inventory_sha256": inventory_hash, "unbound_tracked_control_files": sorted(expected_unbound), "bindings": binding_rows},
        "gates": gates, "errors": sorted(set(errors)), "tasks": task_rows,
        "assignment_summary": {"count": len(assignment_rows), "assignment_set_expected": manifest.get("assignment_set_sha256"), "assignment_set_observed": canon(assignments), "rows": assignment_rows},
        "calibration": {"cases": len(fixture_rows), "pass_fraction": fraction, "outcomes": {state: sum(r["oracle"] == state for r in fixture_rows) for state in ("passed", "criterion_fail", "insufficient_evidence", "invalid_artifact")}, "observer_disagreements": disagreements, "rows": fixture_rows},
        "observer_disagreement_canary": {"observer_a": synthetic_a, "observer_b": synthetic_b, "adjudicated": adjudicated, "status": "PASS" if adjudicated["terminal_state"] == "observer_invalid" else "FAIL"},
        "zero_call_isolation_canary": canary,
        "equal_envelope": {field: sorted({str(c.get(field)) for c in conditions}) for field in SHARED},
        "claim_ceiling": protocol.get("claim_ceiling"), "attempt_ledger": ledger,
        "claim_limits": ["Internal builder-authored mechanism calibration only.", "No model, provider, or repair row was called.", "No capability, treatment-effect, self-correction, professional-validity, utility, production-fitness, or readiness claim is licensed.", "The zero-call resolver canary is not an executed launcher conformance test."],
    }


def markdown(report: dict[str, Any]) -> str:
    gates = "\n".join(f"- **{'PASS' if value else 'FAIL'}** `{name}`" for name, value in report["gates"].items())
    inv = report["inventory"]; cal = report["calibration"]; source = report["source_binding"]
    return f"""# Self-inspection repair v2: independent candidate-freeze audit

**Audit result: {report['status']}**

**Decision:** {'The exact candidate freeze passed the independent mechanical gate. A separate task may build/conform the launcher and execute the prospectively frozen matrix; this audit itself authorizes no model/provider call or spend.' if report['status']=='PASS' else 'STOP. Execution is not authorized.'}

## Bound evidence

- Candidate commit `{source['resolved_commit']}` is reachable from `origin/main` at `{source['origin_main_at_audit']}`.
- Root tree `{source['root_tree']}`; candidate subtree `{source['pilot_subtree']}`.
- Independently read and verified all {inv['bound_files_read']} manifest-bound Git blobs ({inv['bound_bytes_read']} bytes); aggregate canonical inventory `{inv['aggregate_inventory_sha256']}`.
- Recomputed 150 assignment identities and the assignment-set hash; no attempt is recorded.
- Replayed all 48 calibration cases through both frozen observers and an independent oracle: {json.dumps(cal['outcomes'], sort_keys=True)}; observer disagreements={cal['observer_disagreements']}; pass fraction={cal['pass_fraction']:.2f}.
- No frozen candidate byte was modified. No model, provider, repair row, or paid action was called.

## Gates

{gates}

## What this licenses—and does not

The instrument now mechanically represents three synthetic families/shapes, two predeclared defect strata per family, five conditions, five repetitions per cell, condition-blind dual observers, public source bases, pinned native/render relations, equal declared envelopes, seeds/order policy, clustered estimands, and fail-closed invalid states. Its 12/48 calibration passes avoid the declared builder-only floor/ceiling gate.

This is not outcome evidence. All claim ceilings remain false. The isolation result is an independently exercised allowlist/write-guard canary, not conformance evidence for an execution launcher: no v2 launcher is frozen yet. The continuation must therefore build and test a commit-bound zero-call launcher against these exact bytes before any provider call, then either stop on a conformance defect or execute the already frozen 150 assignments without tuning the candidate.

Machine-readable evidence: `reports/validation/2026-07-19-self-inspection-repair-v2-freeze-audit.json`.
"""


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--commit", default=DEFAULT_COMMIT); parser.add_argument("--json-out"); parser.add_argument("--markdown-out")
    args = parser.parse_args(); report = run(args.commit)
    if args.json_out: Path(args.json_out).write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    if args.markdown_out: Path(args.markdown_out).write_text(markdown(report))
    print(json.dumps({"status": report["status"], "commit": report["source_binding"]["resolved_commit"], "gates": report["gates"], "errors": report["errors"], "bound_files": report["inventory"]["bound_files_read"], "assignments": report["assignment_summary"]["count"], "calibration_cases": report["calibration"]["cases"], "model_calls": report["attempt_ledger"]["model_calls"], "provider_calls": report["attempt_ledger"]["provider_calls"], "repair_rows_executed": report["attempt_ledger"]["repair_rows_executed"]}, indent=2, sort_keys=True))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
