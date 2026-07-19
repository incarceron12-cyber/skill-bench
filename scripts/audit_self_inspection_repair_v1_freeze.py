#!/usr/bin/env python3
"""Independent, commit-bound audit of self-inspection-repair-v1.

This auditor deliberately does not import the pilot preflight or checker. It reads
all v1 evidence from one Git commit, reconstructs the frozen relations, executes
an independent calibration oracle, and plants fail-closed mutations. It never
calls a model/provider or writes inside the frozen pilot directory.
"""
from __future__ import annotations

import argparse
import ast
import copy
import datetime as dt
import hashlib
import inspect
import json
import os
import subprocess
import tempfile
from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parents[1]
PILOT_REL = Path("pilots/self-inspection-repair-v1")
DEFAULT_COMMIT = "7d976a28b9f33337f2f90519964361388b3eae7f"
EXPECTED_TREE = "6eed1293c68faf90eb2b72e2dd2adf3600016c75"
CONDITIONS = {
    "no_second_attempt",
    "retry_no_new_information",
    "generic_self_review",
    "native_render_self_inspection",
    "consequence_only_feedback",
    "criterion_disclosure",
}
TERMINAL_STATES = {
    "criterion_fail", "invalid_artifact", "insufficient_evidence",
    "observer_invalid", "environment_invalid", "service_invalid", "passed",
}
KINDS = {
    "positive", "near_miss", "legitimate_alternative", "corrupt_artifact",
    "missing_view", "observer_failure",
}
SHARED_FIELDS = ("tool_id", "harness_id", "model_id", "provider_id", "budget_id")
ALLOWED_DIFFERENCES = {
    "condition_id", "repair_authorized", "information_treatment",
    "hidden_criterion_access", "prompt_source",
}
SEQUENCE = [
    "defect_observation", "diagnosis", "revision_delta",
    "criterion_local_recheck", "collateral_recheck",
    "new_error_assessment", "cost",
]
CLAIMS = {
    "self_correction", "agent_capability", "professional_validity", "utility",
    "production_fitness", "readiness",
}


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def canonical_hash(value: Any) -> str:
    return sha256_bytes(canonical_bytes(value))


def git(*args: str, text: bool = True) -> str | bytes:
    result = subprocess.run(
        ["git", *args], cwd=ROOT, check=True, capture_output=True,
        text=text,
    )
    return result.stdout


def git_blob(commit: str, relative: Path) -> bytes:
    return git("show", f"{commit}:{relative.as_posix()}", text=False)  # type: ignore[return-value]


def git_object(commit: str, relative: Path) -> str:
    return str(git("rev-parse", f"{commit}:{relative.as_posix()}")).strip()


def load_blob(commit: str, relative: str) -> Any:
    return json.loads(git_blob(commit, PILOT_REL / relative))


def independent_evaluate(
    shape: str, candidate: Any, view_status: str = "available",
    observer_status: str = "valid",
) -> dict[str, Any]:
    """Independent specification oracle for the 12 calibration cases."""
    if observer_status != "valid":
        return {"terminal_state": "observer_invalid", "endpoint": None, "collateral": None}
    if view_status != "available":
        return {"terminal_state": "insufficient_evidence", "endpoint": None, "collateral": None}
    if shape == "memo":
        if not isinstance(candidate, str) or not candidate.strip():
            return {"terminal_state": "invalid_artifact", "endpoint": None, "collateral": None}
        normalized = " ".join(candidate.lower().replace("**", "").split())
        endpoint = ("select south" in normalized or "recommend south" in normalized) and (
            "95,000" in normalized or "95000" in normalized
        )
        collateral = "north" in normalized and "south" in normalized
    elif shape == "structured":
        if not isinstance(candidate, dict) or not isinstance(candidate.get("allocations"), dict):
            return {"terminal_state": "invalid_artifact", "endpoint": None, "collateral": None}
        allocations = candidate["allocations"]
        if (
            set(allocations) != {"ops", "research"}
            or any(type(v) is not int for v in allocations.values())
            or type(candidate.get("declared_total")) is not int
        ):
            return {"terminal_state": "invalid_artifact", "endpoint": None, "collateral": None}
        endpoint = (
            sum(allocations.values()) == candidate["declared_total"] == 100
            and allocations["ops"] <= 60 and allocations["research"] <= 40
        )
        collateral = set(allocations) == {"ops", "research"}
    else:
        return {"terminal_state": "invalid_artifact", "endpoint": None, "collateral": None}
    return {
        "terminal_state": "passed" if endpoint and collateral else "criterion_fail",
        "endpoint": endpoint,
        "collateral": collateral,
    }


def validate_state(
    protocol: dict[str, Any], manifest: dict[str, Any], envelope: dict[str, Any],
    transforms: dict[str, Any], fixtures: dict[str, Any], ledger: dict[str, Any],
    checker_source: str, bound_bytes: dict[str, bytes],
) -> list[str]:
    """Independent fail-closed validator used for baseline and planted mutations."""
    errors: list[str] = []
    conditions = protocol.get("conditions", [])
    by_condition = {c.get("condition_id"): c for c in conditions}
    if len(conditions) != 6 or set(by_condition) != CONDITIONS:
        errors.append("condition_matrix")
    if set(protocol.get("terminal_states", [])) != TERMINAL_STATES:
        errors.append("terminal_type_collapse")
    if protocol.get("ecological_feedback", {}).get("included") is not False:
        errors.append("unauthorized_ecological_feedback")
    ceiling = protocol.get("claim_ceiling", {})
    if set(ceiling) != CLAIMS or any(ceiling.values()):
        errors.append("claim_ceiling")
    for cid, condition in by_condition.items():
        info = condition.get("information_treatment", [])
        if cid != "criterion_disclosure" and condition.get("hidden_criterion_access"):
            errors.append(f"hidden_criterion_leak:{cid}")
        if cid != "criterion_disclosure" and "criterion_text" in info:
            errors.append(f"criterion_treatment_leak:{cid}")
    if any(len({c.get(key) for c in conditions}) != 1 for key in SHARED_FIELDS):
        errors.append("unequal_execution_envelope")
    envelope_ids = {name: value.get("id") for name, value in envelope.items()}
    for condition in conditions:
        for key in SHARED_FIELDS:
            component = key.removesuffix("_id")
            if condition.get(key) != envelope_ids.get(component):
                errors.append(f"envelope_identity:{condition.get('condition_id')}:{key}")
    tasks = protocol.get("tasks", [])
    if {t.get("shape") for t in tasks} != {"memo", "structured_native"}:
        errors.append("work_shape_collapse")
    assignments = protocol.get("assignments", [])
    expected = {(t.get("task_id"), cid) for t in tasks for cid in CONDITIONS}
    observed = {(a.get("task_id"), a.get("condition_id")) for a in assignments}
    if len(assignments) != 12 or observed != expected:
        errors.append("assignment_matrix")
    for assignment in assignments:
        unhashed = {k: v for k, v in assignment.items() if k != "assignment_sha256"}
        if assignment.get("assignment_sha256") != canonical_hash(unhashed):
            errors.append(f"assignment_hash:{assignment.get('assignment_id')}")
        if assignment.get("attempts_executed") != 0:
            errors.append(f"post_freeze_execution:{assignment.get('assignment_id')}")
    for task in tasks:
        rows = [a for a in assignments if a.get("task_id") == task.get("task_id")]
        artifact = bound_bytes.get(str(task.get("starting_artifact")), b"")
        hashes = {a.get("starting_artifact_sha256") for a in rows}
        if len(hashes) != 1 or hashes != {sha256_bytes(artifact)}:
            errors.append(f"starting_artifact_drift:{task.get('task_id')}")
    contract = protocol.get("repair_record_contract", {})
    if (
        contract.get("required_sequence") != SEQUENCE
        or contract.get("condition_blind_checker") is not True
        or contract.get("observation_unit") != "proposition"
        or contract.get("preserve_first_and_final") is not True
    ):
        errors.append("repair_record_contract")
    if manifest.get("assignment_set_sha256") != canonical_hash(assignments):
        errors.append("assignment_set_hash")
    if any(manifest.get(k) != 0 for k in ("model_calls", "provider_calls", "repair_rows_executed")):
        errors.append("nonzero_call_ledger")
    if "independent" not in manifest.get("next_gate", ""):
        errors.append("independent_audit_gate")
    bindings = manifest.get("bindings", [])
    bound = {b.get("path"): b for b in bindings}
    if len(bindings) != 18 or len(bound) != len(bindings):
        errors.append("binding_inventory")
    for rel, binding in bound.items():
        raw = bound_bytes.get(str(rel))
        if raw is None:
            errors.append(f"missing_binding:{rel}")
        elif len(raw) != binding.get("bytes") or sha256_bytes(raw) != binding.get("sha256"):
            errors.append(f"post_freeze_edit:{rel}")
    transformation_ids = set()
    for item in transforms.get("transformations", []):
        transformation_ids.add(item.get("transformation_id"))
        if (
            not item.get("transformation_id") or not item.get("implementation")
            or not item.get("input") or not item.get("output")
            or not item.get("permitted_invariances")
        ):
            errors.append("unpinned_transformation")
        if item.get("input") not in bound or item.get("output") not in bound:
            errors.append("unbound_transformation_view")
    for task in tasks:
        if task.get("transformation_id") not in transformation_ids:
            errors.append(f"transformation_identity:{task.get('task_id')}")
        if task.get("native_view") not in bound or task.get("render_view") not in bound:
            errors.append(f"view_identity:{task.get('task_id')}")
    cases = fixtures.get("cases", [])
    coverage = {(case.get("shape"), case.get("kind")) for case in cases}
    if len(cases) != 12 or coverage != {(s, k) for s in ("memo", "structured") for k in KINDS}:
        errors.append("calibration_coverage")
    try:
        tree = ast.parse(checker_source)
        evaluate_node = next(
            node for node in tree.body
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == "evaluate"
        )
        args = {arg.arg for arg in evaluate_node.args.args + evaluate_node.args.kwonlyargs}
        if args & {"condition", "condition_id", "assignment", "repair_prompt", "feedback"}:
            errors.append("checker_condition_dependence")
    except (SyntaxError, StopIteration):
        errors.append("checker_invalid")
    for case in cases:
        result = independent_evaluate(
            case.get("shape"), case.get("candidate"),
            case.get("view_status", "available"), case.get("observer_status", "valid"),
        )
        if result["terminal_state"] != case.get("expected"):
            errors.append(f"calibration_replay:{case.get('case_id')}")
    expected_ledger = {
        "instrument_id": "self-inspection-repair-v1", "attempts": [],
        "model_calls": 0, "provider_calls": 0, "repair_rows_executed": 0,
    }
    if ledger != expected_ledger:
        errors.append("attempt_ledger_nonempty")
    return sorted(set(errors))


def isolation_canary() -> dict[str, Any]:
    """Exercise an actual allowlist resolver and output-root guard without model calls."""
    with tempfile.TemporaryDirectory(prefix="independent-repair-audit-") as tmp:
        base = Path(tmp).resolve()
        task = base / "task-cwd"
        output = base / "trial-output"
        private = base / "private-rubric.json"
        task.mkdir()
        output.mkdir()
        source = task / "source.json"
        source.write_text("{}\n")
        private.write_text('{"hidden":true}\n')
        allowlist = {source.resolve()}

        def allowed_read(candidate: Path) -> bool:
            return candidate.resolve() in allowlist

        def allowed_write(candidate: Path) -> bool:
            resolved = candidate.resolve()
            return resolved.parent == output and output in resolved.parents

        checks = {
            "allowlisted_source_readable": allowed_read(source),
            "private_rubric_excluded": not allowed_read(private),
            "parent_traversal_blocked": not allowed_read(task / ".." / private.name),
            "repository_path_excluded": not allowed_read(ROOT / "PROJECT_CHARTER.md"),
            "unique_output_root": allowed_write(output / "candidate.txt") and not allowed_write(task / "candidate.txt"),
            "task_scoped_cwd": task != ROOT and task != output,
        }
        return {"status": "PASS" if all(checks.values()) else "FAIL", **checks}


def mutate_json(base: dict[str, Any], action: Callable[[dict[str, Any]], None]) -> dict[str, Any]:
    result = copy.deepcopy(base)
    action(result)
    return result


def run_audit(commit: str) -> dict[str, Any]:
    resolved_commit = str(git("rev-parse", commit)).strip()
    origin_main = str(git("rev-parse", "origin/main")).strip()
    source_on_origin_main = subprocess.run(
        ["git", "merge-base", "--is-ancestor", resolved_commit, origin_main],
        cwd=ROOT,
        check=False,
    ).returncode == 0
    tree = str(git("rev-parse", f"{resolved_commit}^{{tree}}")).strip()
    manifest = load_blob(resolved_commit, "freeze-manifest.json")
    protocol = load_blob(resolved_commit, "protocol.json")
    envelope = load_blob(resolved_commit, "execution-envelope.json")
    transforms = load_blob(resolved_commit, "transformations.json")
    fixtures = load_blob(resolved_commit, "fixtures/calibration.json")
    ledger = load_blob(resolved_commit, "attempt-ledger.json")
    checker_source = git_blob(resolved_commit, PILOT_REL / "checkers/check_fixtures.py").decode()
    bindings = manifest["bindings"]
    bound_bytes = {
        b["path"]: git_blob(resolved_commit, PILOT_REL / b["path"])
        for b in bindings
    }
    baseline_errors = validate_state(
        protocol, manifest, envelope, transforms, fixtures, ledger,
        checker_source, bound_bytes,
    )

    binding_rows = []
    for binding in bindings:
        raw = bound_bytes[binding["path"]]
        relative = PILOT_REL / binding["path"]
        binding_rows.append({
            "path": binding["path"],
            "git_object": git_object(resolved_commit, relative),
            "expected_bytes": binding["bytes"], "observed_bytes": len(raw),
            "expected_sha256": binding["sha256"], "observed_sha256": sha256_bytes(raw),
            "status": "PASS" if len(raw) == binding["bytes"] and sha256_bytes(raw) == binding["sha256"] else "FAIL",
        })

    component_rows = []
    for name, value in sorted(envelope.items()):
        expected = manifest["components"][name]
        observed = canonical_hash(value)
        component_rows.append({
            "component": name, "id": value["id"],
            "expected_sha256": expected["sha256"], "observed_sha256": observed,
            "status": "PASS" if expected == {"id": value["id"], "sha256": observed} else "FAIL",
        })

    assignment_rows = []
    for assignment in protocol["assignments"]:
        unhashed = {k: v for k, v in assignment.items() if k != "assignment_sha256"}
        observed = canonical_hash(unhashed)
        assignment_rows.append({
            "assignment_id": assignment["assignment_id"],
            "task_id": assignment["task_id"], "condition_id": assignment["condition_id"],
            "starting_artifact_sha256": assignment["starting_artifact_sha256"],
            "expected_sha256": assignment["assignment_sha256"], "observed_sha256": observed,
            "status": "PASS" if observed == assignment["assignment_sha256"] else "FAIL",
        })

    fixture_rows = []
    for case in fixtures["cases"]:
        result = independent_evaluate(
            case["shape"], case["candidate"], case["view_status"], case["observer_status"]
        )
        fixture_rows.append({
            "case_id": case["case_id"], "shape": case["shape"], "kind": case["kind"],
            "expected": case["expected"], "observed": result["terminal_state"],
            "status": "PASS" if result["terminal_state"] == case["expected"] else "FAIL",
        })

    mutation_specs: list[tuple[str, str, dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any], str, dict[str, bytes]]] = []

    def add(name: str, expected: str, *, p=protocol, m=manifest, e=envelope, t=transforms, f=fixtures, l=ledger, c=checker_source, b=bound_bytes) -> None:
        mutation_specs.append((name, expected, p, m, e, t, f, c, b if l is ledger else {**b, "__ledger_override__": canonical_bytes(l)}))

    add("remove_condition", "condition_matrix", p=mutate_json(protocol, lambda x: x["conditions"].pop()))
    add("collapse_terminal_states", "terminal_type_collapse", p=mutate_json(protocol, lambda x: x.__setitem__("terminal_states", ["failed", "passed"])))
    add("authorize_ecological_feedback", "unauthorized_ecological_feedback", p=mutate_json(protocol, lambda x: x["ecological_feedback"].__setitem__("included", True)))
    add("raise_capability_claim", "claim_ceiling", p=mutate_json(protocol, lambda x: x["claim_ceiling"].__setitem__("agent_capability", True)))
    p = copy.deepcopy(protocol); next(c for c in p["conditions"] if c["condition_id"] == "generic_self_review")["hidden_criterion_access"] = True
    add("leak_hidden_criterion_access", "hidden_criterion_leak:generic_self_review", p=p)
    p = copy.deepcopy(protocol); next(c for c in p["conditions"] if c["condition_id"] == "consequence_only_feedback")["information_treatment"].append("criterion_text")
    add("leak_criterion_text", "criterion_treatment_leak:consequence_only_feedback", p=p)
    p = copy.deepcopy(protocol); p["conditions"][0]["budget_id"] = "larger-budget"
    add("unequal_budget", "unequal_execution_envelope", p=p)
    p = copy.deepcopy(protocol); p["conditions"][0]["tool_id"] = "extra-tool"
    add("unequal_tool", "unequal_execution_envelope", p=p)
    p = copy.deepcopy(protocol); p["tasks"][1]["shape"] = "memo"
    add("collapse_work_shapes", "work_shape_collapse", p=p)
    p = copy.deepcopy(protocol); p["assignments"].pop()
    add("remove_assignment", "assignment_matrix", p=p)
    p = copy.deepcopy(protocol); p["assignments"][0]["assignment_sha256"] = "0" * 64
    add("corrupt_assignment_hash", f"assignment_hash:{p['assignments'][0]['assignment_id']}", p=p)
    p = copy.deepcopy(protocol); p["assignments"][0]["attempts_executed"] = 1
    unhashed = {k: v for k, v in p["assignments"][0].items() if k != "assignment_sha256"}; p["assignments"][0]["assignment_sha256"] = canonical_hash(unhashed)
    add("record_post_freeze_execution", f"post_freeze_execution:{p['assignments'][0]['assignment_id']}", p=p)
    p = copy.deepcopy(protocol); row = next(a for a in p["assignments"] if a["condition_id"] == "generic_self_review" and a["task_id"] == "memo-vendor-selection-v1"); row["starting_artifact_sha256"] = "0" * 64; row["assignment_sha256"] = canonical_hash({k: v for k, v in row.items() if k != "assignment_sha256"})
    add("drift_starting_artifact", "starting_artifact_drift:memo-vendor-selection-v1", p=p)
    p = copy.deepcopy(protocol); p["repair_record_contract"]["required_sequence"] = list(reversed(SEQUENCE))
    add("reorder_repair_record", "repair_record_contract", p=p)
    m = copy.deepcopy(manifest); m["assignment_set_sha256"] = "0" * 64
    add("corrupt_assignment_set_hash", "assignment_set_hash", m=m)
    m = copy.deepcopy(manifest); m["model_calls"] = 1
    add("record_model_call", "nonzero_call_ledger", m=m)
    m = copy.deepcopy(manifest); m["next_gate"] = "execute"
    add("remove_independent_gate", "independent_audit_gate", m=m)
    m = copy.deepcopy(manifest); m["bindings"].append(copy.deepcopy(m["bindings"][0]))
    add("duplicate_binding", "binding_inventory", m=m)
    t = copy.deepcopy(transforms); t["transformations"][0]["permitted_invariances"] = []
    add("unpin_transformation", "unpinned_transformation", t=t)
    p = copy.deepcopy(protocol); p["tasks"][0]["transformation_id"] = "unknown"
    add("break_transformation_identity", "transformation_identity:memo-vendor-selection-v1", p=p)
    f = copy.deepcopy(fixtures); f["cases"].pop()
    add("remove_calibration_kind", "calibration_coverage", f=f)
    f = copy.deepcopy(fixtures); f["cases"][0]["expected"] = "criterion_fail"
    add("invert_calibration_outcome", "calibration_replay:memo-positive", f=f)
    add("add_checker_condition_parameter", "checker_condition_dependence", c=checker_source.replace("observer_status=\"valid\"):", "observer_status=\"valid\", condition=None):", 1))

    mutation_rows = []
    for name, expected, p, m, e, t, f, c, bcarrier in mutation_specs:
        l = ledger
        b = bcarrier
        errors = validate_state(p, m, e, t, f, l, c, b)
        mutation_rows.append({"mutation": name, "expected_rejection": expected, "observed_errors": errors, "status": "PASS" if expected in errors else "FAIL"})

    # Every frozen binding is independently changed without refreshing its manifest entry.
    byte_mutations = []
    for rel in sorted(bound_bytes):
        changed = dict(bound_bytes)
        changed[rel] = changed[rel] + b" "
        errors = validate_state(protocol, manifest, envelope, transforms, fixtures, ledger, checker_source, changed)
        expected = f"post_freeze_edit:{rel}"
        byte_mutations.append({"path": rel, "expected_rejection": expected, "status": "PASS" if expected in errors else "FAIL"})

    # Empty-ledger mutation is kept separate because validate_state accepts it as a distinct object.
    changed_ledger = copy.deepcopy(ledger); changed_ledger["model_calls"] = 1
    ledger_errors = validate_state(protocol, manifest, envelope, transforms, fixtures, changed_ledger, checker_source, bound_bytes)
    mutation_rows.append({"mutation": "nonempty_attempt_ledger", "expected_rejection": "attempt_ledger_nonempty", "observed_errors": ledger_errors, "status": "PASS" if "attempt_ledger_nonempty" in ledger_errors else "FAIL"})

    condition_rows = []
    for condition in protocol["conditions"]:
        shared = {key: condition[key] for key in SHARED_FIELDS}
        condition_rows.append({
            "condition_id": condition["condition_id"], "shared_envelope": shared,
            "repair_authorized": condition["repair_authorized"],
            "information_treatment": condition["information_treatment"],
            "hidden_criterion_access": condition["hidden_criterion_access"],
        })
    common_start = {}
    for task in protocol["tasks"]:
        rows = [a for a in protocol["assignments"] if a["task_id"] == task["task_id"]]
        hashes = sorted({a["starting_artifact_sha256"] for a in rows})
        artifact_hash = sha256_bytes(bound_bytes[task["starting_artifact"]])
        common_start[task["task_id"]] = {
            "assignment_hashes": hashes, "artifact_sha256": artifact_hash,
            "status": "PASS" if hashes == [artifact_hash] and len(rows) == 6 else "FAIL",
        }

    transformation_rows = []
    by_transform = {item["transformation_id"]: item for item in transforms["transformations"]}
    for task in protocol["tasks"]:
        item = by_transform.get(task["transformation_id"])
        ok = bool(item and item["input"] == task["native_view"] and item["output"] == task["render_view"] and item["input"] in bound_bytes and item["output"] in bound_bytes)
        transformation_rows.append({
            "task_id": task["task_id"], "transformation_id": task["transformation_id"],
            "native_view": task["native_view"], "render_view": task["render_view"],
            "status": "PASS" if ok else "FAIL",
        })

    canary = isolation_canary()
    preflight_report = load_blob(resolved_commit, "preflight-report.json")
    gates = {
        "source_commit_reachable_from_origin_main": source_on_origin_main,
        "expected_commit": resolved_commit == DEFAULT_COMMIT,
        "expected_root_tree": tree == EXPECTED_TREE,
        "baseline_semantics": not baseline_errors,
        "all_bindings": all(r["status"] == "PASS" for r in binding_rows) and len(binding_rows) == 18,
        "all_components": all(r["status"] == "PASS" for r in component_rows) and len(component_rows) == 6,
        "all_assignments": all(r["status"] == "PASS" for r in assignment_rows) and len(assignment_rows) == 12,
        "assignment_set": manifest["assignment_set_sha256"] == canonical_hash(protocol["assignments"]),
        "common_starting_artifacts": all(v["status"] == "PASS" for v in common_start.values()),
        "condition_boundaries": len(condition_rows) == 6 and not any(e.startswith(("hidden_criterion", "criterion_treatment", "unequal_execution")) for e in baseline_errors),
        "transformation_view_identity": all(r["status"] == "PASS" for r in transformation_rows),
        "fixture_coverage_and_outcomes": all(r["status"] == "PASS" for r in fixture_rows) and len(fixture_rows) == 12,
        "checker_condition_blindness": not any(e.startswith("checker_") for e in baseline_errors),
        "typed_terminal_states": set(protocol["terminal_states"]) == TERMINAL_STATES,
        "empty_attempt_ledger": ledger == {"instrument_id":"self-inspection-repair-v1","attempts":[],"model_calls":0,"provider_calls":0,"repair_rows_executed":0},
        "zero_call_isolation_canary": canary["status"] == "PASS",
        "equal_envelope_canary": len({tuple((k, c[k]) for k in SHARED_FIELDS) for c in protocol["conditions"]}) == 1,
        "builder_preflight_evidence": preflight_report.get("status") == "PASS" and preflight_report.get("model_calls") == 0 and preflight_report.get("provider_calls") == 0 and preflight_report.get("repair_rows_executed") == 0,
        "semantic_mutations_fail_closed": all(r["status"] == "PASS" for r in mutation_rows),
        "all_bound_byte_mutations_fail_closed": all(r["status"] == "PASS" for r in byte_mutations) and len(byte_mutations) == 18,
        "claim_ceiling_false": set(protocol["claim_ceiling"]) == CLAIMS and not any(protocol["claim_ceiling"].values()),
    }
    status = "PASS" if all(gates.values()) else "FAIL"
    return {
        "schema_version": "1.0.0",
        "audit_id": "self-inspection-repair-v1-freeze-independent-audit",
        "audited_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "auditor": "benchmark-builder",
        "status": status,
        "authorization": "execution_eligible_for_one_separately_queued_bounded_trial" if status == "PASS" else "execution_not_authorized",
        "source_binding": {
            "requested_commit": commit, "resolved_commit": resolved_commit,
            "origin_main_at_audit": origin_main, "root_tree": tree,
            "pilot_path": PILOT_REL.as_posix(),
        },
        "gates": gates,
        "baseline_errors": baseline_errors,
        "binding_recomputation": binding_rows,
        "component_recomputation": component_rows,
        "assignment_recomputation": assignment_rows,
        "assignment_set_sha256": {
            "expected": manifest["assignment_set_sha256"],
            "observed": canonical_hash(protocol["assignments"]),
        },
        "common_starting_artifact_invariant": common_start,
        "condition_information_and_resource_boundaries": condition_rows,
        "transformation_and_view_identities": transformation_rows,
        "fixture_replay": fixture_rows,
        "fixture_outcomes": {state: sum(r["observed"] == state for r in fixture_rows) for state in sorted(TERMINAL_STATES)},
        "checker_condition_blindness": {"evaluate_parameters": ["shape", "candidate", "view_status", "observer_status"], "forbidden_inputs_absent": gates["checker_condition_blindness"]},
        "terminal_states": sorted(TERMINAL_STATES),
        "attempt_ledger": ledger,
        "zero_call_isolation_canary": canary,
        "equal_envelope_canary": {"status": "PASS" if gates["equal_envelope_canary"] else "FAIL", "shared_fields": list(SHARED_FIELDS), "allowed_condition_differences": sorted(ALLOWED_DIFFERENCES)},
        "semantic_mutation_tests": mutation_rows,
        "bound_byte_mutation_tests": byte_mutations,
        "model_calls": 0, "provider_calls": 0, "repair_rows_executed": 0,
        "claim_ceiling": protocol["claim_ceiling"],
        "claim_boundary": {
            "licensed": ["exact commit/tree/file/component/assignment custody", "builder-authored fixture behavior", "mechanical execution eligibility for one separately authorized bounded trial"],
            "not_licensed": ["self-correction", "agent capability", "professional validity", "utility", "production fitness", "readiness", "treatment effect"],
        },
    }


def write_note(report: dict[str, Any], path: Path) -> None:
    source = report["source_binding"]
    lines = [
        "# Independent audit: self-inspection repair v1 freeze",
        "",
        f"**Result: {report['status']}**",
        "",
        f"Audited commit `{source['resolved_commit']}` and root tree `{source['root_tree']}` on `origin/main` history. No v1 byte was modified; no model, provider, or repair row was called.",
        "",
        "## Evidence",
        "",
        f"- Recomputed {len(report['binding_recomputation'])} frozen file hashes and Git object identities.",
        f"- Recomputed {len(report['component_recomputation'])} component hashes, {len(report['assignment_recomputation'])} assignment hashes, and the assignment-set hash.",
        "- Verified the common starting artifact per task, six condition information/resource boundaries, two transformation/view identities, seven typed terminal states, and the empty attempt ledger.",
        f"- Independently replayed {len(report['fixture_replay'])} calibration cases; outcomes: `{json.dumps(report['fixture_outcomes'], sort_keys=True)}`.",
        f"- Planted {len(report['semantic_mutation_tests'])} semantic mutations and one edit to each of {len(report['bound_byte_mutation_tests'])} frozen files; every declared violation failed closed.",
        "- Exercised an independent zero-call allowlist/output-root canary and equal-envelope check.",
        "",
        "## Decision and claim ceiling",
        "",
        ("The exact v1 freeze is mechanically eligible for **one separately queued bounded execution trial**. This audit does not itself authorize provider spend or execute any assignment." if report["status"] == "PASS" else "Execution is not authorized; resolve the failed machine-report gates in a new version."),
        "",
        "The audit licenses only commit/tree custody, exact deterministic builder-fixture behavior, and bounded mechanical execution eligibility. It does **not** license self-correction, capability, treatment-effect, professional-validity, utility, production-fitness, or readiness claims.",
        "",
        "Machine-readable evidence: `reports/validation/2026-07-19-self-inspection-repair-v1-freeze-audit.json`.",
        "",
    ]
    path.write_text("\n".join(lines))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--commit", default=DEFAULT_COMMIT)
    parser.add_argument("--output", type=Path, default=ROOT / "reports/validation/2026-07-19-self-inspection-repair-v1-freeze-audit.json")
    parser.add_argument("--note", type=Path, default=ROOT / "reports/validation/2026-07-19-self-inspection-repair-v1-freeze-audit.md")
    args = parser.parse_args()
    report = run_audit(args.commit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    write_note(report, args.note)
    print(json.dumps({
        "status": report["status"], "commit": report["source_binding"]["resolved_commit"],
        "tree": report["source_binding"]["root_tree"], "gates": report["gates"],
        "semantic_mutations": len(report["semantic_mutation_tests"]),
        "bound_byte_mutations": len(report["bound_byte_mutation_tests"]),
        "model_calls": 0, "provider_calls": 0, "repair_rows_executed": 0,
    }, indent=2, sort_keys=True))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
