#!/usr/bin/env python3
"""Build the prospective zero-call repair protocol and content manifest."""
from __future__ import annotations
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONDITIONS = [
    ("no_second_attempt", False, [], False),
    ("retry_no_new_information", True, [], False),
    ("generic_self_review", True, [], False),
    ("native_render_self_inspection", True, ["native", "render"], False),
    ("consequence_only_feedback", True, ["consequence"], False),
    ("criterion_disclosure", True, ["criterion_text"], True),
]
TASKS = [
    {"task_id":"memo-vendor-selection-v1","shape":"memo","source":"sources/memo-source.json","task":"tasks/memo-task.json","starting_artifact":"artifacts/memo-initial.md","native_view":"artifacts/memo-initial.md","render_view":"views/memo-render.txt","transformation_id":"markdown-text-render-v1","defect_proposition":"The recommendation conflicts with the lowest-cost qualifying vendor in the public evidence.","criterion_id":"memo-r1"},
    {"task_id":"structured-allocation-v1","shape":"structured_native","source":"sources/table-source.json","task":"tasks/structured-task.json","starting_artifact":"artifacts/structured-initial.json","native_view":"artifacts/structured-initial.json","render_view":"views/structured-render.txt","transformation_id":"json-summary-render-v1","defect_proposition":"The declared total conflicts with the sum of native allocation values.","criterion_id":"table-r2"},
]
BOUND_FILES = [
    "README.md", "sources/memo-source.json", "sources/table-source.json", "tasks/memo-task.json", "tasks/structured-task.json",
    "artifacts/memo-initial.md", "artifacts/structured-initial.json", "views/memo-render.txt", "views/structured-render.txt",
    "transformations.json", "execution-envelope.json", "attempt-ledger.json", "prompts.json", "fixtures/calibration.json",
    "checkers/check_fixtures.py", "prepare_freeze.py", "preflight.py"
]

def raw_hash(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def canonical_hash(value): return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def build_protocol():
    envelope = json.loads((HERE / "execution-envelope.json").read_text())
    conditions = []
    for condition_id, repair, information, hidden in CONDITIONS:
        conditions.append({
            "condition_id": condition_id, "repair_authorized": repair, "information_treatment": information,
            "hidden_criterion_access": hidden, "prompt_source": "prompts.json", "tool_id": envelope["tool"]["id"],
            "harness_id": envelope["harness"]["id"], "model_id": envelope["model"]["id"],
            "provider_id": envelope["provider"]["id"], "budget_id": envelope["budget"]["id"]
        })
    assignments = []
    for task in TASKS:
        artifact_hash = raw_hash(HERE / task["starting_artifact"])
        for condition in conditions:
            assignment = {"assignment_id":f'{task["task_id"]}--{condition["condition_id"]}',"task_id":task["task_id"],"condition_id":condition["condition_id"],"starting_artifact_sha256":artifact_hash,"attempts_executed":0}
            assignment["assignment_sha256"] = canonical_hash(assignment)
            assignments.append(assignment)
    return {
        "schema_version":"1.0.0", "instrument_id":"self-inspection-repair-v1", "status":"prospective_zero_call_candidate_freeze",
        "source_reviews":["papers/agent-benchmarks/2026-07-19-tobench-omnimodal-closed-loop-validity.md","papers/agent-benchmarks/2026-07-15-agencybench-feedback-artifact-validity.md"],
        "tasks":TASKS, "conditions":conditions, "assignments":assignments,
        "terminal_states":["criterion_fail","invalid_artifact","insufficient_evidence","observer_invalid","environment_invalid","service_invalid","passed"],
        "repair_record_contract":{"required_sequence":["defect_observation","diagnosis","revision_delta","criterion_local_recheck","collateral_recheck","new_error_assessment","cost"],"observation_unit":"proposition","preserve_first_and_final":True,"condition_blind_checker":True},
        "calibration_kinds":["positive","near_miss","legitimate_alternative","corrupt_artifact","missing_view","observer_failure"],
        "ecological_feedback":{"included":False,"reason":"No authorized participant exists."},
        "claim_ceiling":{"self_correction":False,"agent_capability":False,"professional_validity":False,"utility":False,"production_fitness":False,"readiness":False},
        "next_gate":"separate commit-bound independent freeze audit before any model, provider, or repair-row execution"
    }

def build_manifest(protocol):
    bindings=[]
    for rel in BOUND_FILES + ["protocol.json"]:
        path=HERE/rel
        bindings.append({"path":rel,"bytes":path.stat().st_size,"sha256":raw_hash(path)})
    envelope=json.loads((HERE/"execution-envelope.json").read_text())
    components={name:{"id":value["id"],"sha256":canonical_hash(value)} for name,value in envelope.items()}
    return {"schema_version":"1.0.0","freeze_id":"self-inspection-repair-v1-candidate","status":"awaiting_separate_commit_bound_independent_audit","bindings":bindings,"components":components,"assignment_set_sha256":canonical_hash(protocol["assignments"]),"model_calls":0,"provider_calls":0,"repair_rows_executed":0,"post_freeze_edit_policy":"new version required; never refresh an audited manifest in place","next_gate":protocol["next_gate"]}

def main():
    protocol=build_protocol()
    (HERE/"protocol.json").write_text(json.dumps(protocol,indent=2,sort_keys=True)+"\n")
    manifest=build_manifest(protocol)
    (HERE/"freeze-manifest.json").write_text(json.dumps(manifest,indent=2,sort_keys=True)+"\n")
    print(f'WROTE protocol with {len(protocol["assignments"])} zero-attempt assignments and {len(manifest["bindings"])} bindings')
if __name__ == "__main__": main()
