#!/usr/bin/env python3
"""Materialize the prospective v2 repair instrument; never executes model/provider rows."""
from __future__ import annotations
import csv, hashlib, io, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONDITIONS = [
    ("retry_no_new_information", []),
    ("generic_self_review", ["generic_review_instruction"]),
    ("native_render_self_inspection", ["native_artifact", "pinned_render"]),
    ("consequence_only_feedback", ["typed_consequence_without_criterion_text"]),
    ("criterion_disclosure", ["public_basis_criterion_text"]),
]
FAMILIES = {
 "roster": {
  "shape":"csv_schedule", "extension":"csv", "transform":"csv-summary-v1",
  "source":{"authority":"builder_authoritative_synthetic_public_source","public_basis":["Exactly Alice, Bob, and Cara must remain represented.","Monday and Tuesday each require at least two assigned workers.","No worker may exceed 16 total scheduled hours."],"claim_limit":"Internal mechanism calibration only; no workforce-policy or professional-validity claim."},
  "subtle":"worker,day,hours\nAlice,Monday,8\nBob,Monday,8\nCara,Tuesday,8\n",
  "multi":"worker,day,hours\nAlice,Monday,8\nBob,Monday,16\nBob,Tuesday,8\nCara,Tuesday,0\n",
  "positive":"worker,day,hours\nAlice,Monday,8\nBob,Monday,8\nCara,Tuesday,8\nAlice,Tuesday,8\n",
  "alternative":"worker,day,hours\nAlice,Monday,4\nCara,Monday,8\nBob,Tuesday,8\nCara,Tuesday,4\n",
  "collateral_damage":"worker,day,hours\nAlice,Monday,8\nBob,Monday,8\nAlice,Tuesday,8\nBob,Tuesday,8\n",
  "render":"CSV roster summary: workers={workers}; Monday coverage={monday}; Tuesday coverage={tuesday}; max hours={max_hours}.\n",
  "endpoint":"both days have >=2 workers and every worker has <=16 hours", "collateral":"worker identity set remains exactly Alice/Bob/Cara"
 },
 "service": {
  "shape":"ini_configuration", "extension":"ini", "transform":"ini-summary-v1",
  "source":{"authority":"builder_authoritative_synthetic_public_source","public_basis":["Keep service_name=ledger and endpoint=/v1/post.","tls_min must be 1.3.","timeout_seconds must be no greater than 30 and audit_enabled must be true."],"claim_limit":"Internal mechanism calibration only; no security, deployment, or professional-validity claim."},
  "subtle":"[service]\nservice_name=ledger\nendpoint=/v1/post\ntls_min=1.3\ntimeout_seconds=31\naudit_enabled=true\n",
  "multi":"[service]\nservice_name=ledger\nendpoint=/v1/post\ntls_min=1.2\ntimeout_seconds=45\naudit_enabled=false\n",
  "positive":"[service]\nservice_name=ledger\nendpoint=/v1/post\ntls_min=1.3\ntimeout_seconds=30\naudit_enabled=true\n",
  "alternative":"[service]\nendpoint=/v1/post\nservice_name=ledger\naudit_enabled=TRUE\ntimeout_seconds=20\ntls_min=1.3\n",
  "collateral_damage":"[service]\nservice_name=payments\nendpoint=/v2/post\ntls_min=1.3\ntimeout_seconds=20\naudit_enabled=true\n",
  "render":"INI service summary: name={name}; endpoint={endpoint}; TLS={tls}; timeout={timeout}; audit={audit}.\n",
  "endpoint":"TLS=1.3, timeout<=30, audit=true", "collateral":"service_name and endpoint remain ledger and /v1/post"
 },
 "workflow": {
  "shape":"svg_workflow", "extension":"svg", "transform":"svg-graph-summary-v1",
  "source":{"authority":"builder_authoritative_synthetic_public_source","public_basis":["Preserve nodes intake, review, approve and the title Release review.","The SVG viewBox width must be at most 600.","Directed edges intake->review and review->approve are required."],"claim_limit":"Internal mechanism calibration only; no process-design or professional-validity claim."},
  "subtle":"<svg viewBox='0 0 601 400'><title>Release review</title><g id='intake'/><g id='review'/><g id='approve'/><path data-edge='intake->review'/><path data-edge='review->approve'/></svg>\n",
  "multi":"<svg viewBox='0 0 700 400'><title>Release review</title><g id='intake'/><g id='review'/><g id='approve'/><path data-edge='intake->approve'/></svg>\n",
  "positive":"<svg viewBox='0 0 600 400'><title>Release review</title><g id='intake'/><g id='review'/><g id='approve'/><path data-edge='intake->review'/><path data-edge='review->approve'/></svg>\n",
  "alternative":"<svg viewBox='0 0 500 300'><title>Release review</title><g id='approve'/><g id='review'/><g id='intake'/><path data-edge='review->approve'/><path data-edge='intake->review'/></svg>\n",
  "collateral_damage":"<svg viewBox='0 0 500 300'><title>Other</title><g id='intake'/><g id='review'/><path data-edge='intake->review'/><path data-edge='review->approve'/></svg>\n",
  "render":"SVG workflow summary: title={title}; nodes={nodes}; edges={edges}; width={width}.\n",
  "endpoint":"required directed edges exist and viewBox width<=600", "collateral":"title and exact required node set are preserved"
 }
}

def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True)+"\n")
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def canon(value): return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def render(family, text):
    if family=="roster":
        rows=list(csv.DictReader(io.StringIO(text))); workers=sorted({r["worker"] for r in rows}); cov={d:len({r["worker"] for r in rows if r["day"]==d and int(r["hours"])>0}) for d in ("Monday","Tuesday")}; totals={w:sum(int(r["hours"]) for r in rows if r["worker"]==w) for w in workers}
        return FAMILIES[family]["render"].format(workers="/".join(workers),monday=cov["Monday"],tuesday=cov["Tuesday"],max_hours=max(totals.values()))
    if family=="service":
        vals=dict(line.split("=",1) for line in text.splitlines() if "=" in line)
        return FAMILIES[family]["render"].format(name=vals["service_name"],endpoint=vals["endpoint"],tls=vals["tls_min"],timeout=vals["timeout_seconds"],audit=vals["audit_enabled"])
    import re
    title=re.search(r"<title>(.*?)</title>",text).group(1); nodes=sorted(re.findall(r"<g id=['\"](.*?)['\"]",text)); edges=sorted(re.findall(r"data-edge=['\"](.*?)['\"]",text)); width=re.search(r"viewBox=['\"]\S+\s+\S+\s+(\d+)",text).group(1)
    return FAMILIES[family]["render"].format(title=title,nodes="/".join(nodes),edges="/".join(edges),width=width)

def main():
    tasks=[]; cases=[]
    for family,spec in FAMILIES.items():
        dump(HERE/f"sources/{family}-rules.json", {"source_id":f"{family}-rules-v2",**spec["source"]})
        for stratum in ("subtle","multi"):
            task_id=f"{family}-{stratum}-v2"; artifact=HERE/f"artifacts/{task_id}.{spec['extension']}"; artifact.parent.mkdir(parents=True,exist_ok=True); artifact.write_text(spec[stratum])
            view=HERE/f"views/{task_id}.txt"; view.parent.mkdir(parents=True,exist_ok=True); view.write_text(render(family,spec[stratum]))
            task={"task_id":task_id,"family":family,"shape":spec["shape"],"defect_stratum":"near_threshold_single_locus" if stratum=="subtle" else "multi_locus_collateral_risk","source":f"sources/{family}-rules.json","fair_public_basis":spec["source"]["public_basis"],"starting_artifact":str(artifact.relative_to(HERE)),"authoritative_native_view":str(artifact.relative_to(HERE)),"derived_render_view":str(view.relative_to(HERE)),"transformation_id":spec["transform"],"endpoint_outcome":{"type":"boolean","definition":spec["endpoint"]},"collateral_outcome":{"type":"boolean","definition":spec["collateral"]}}
            dump(HERE/f"tasks/{task_id}.json",task); tasks.append(task)
            for kind,key,expected,view_status,transform_status in [
                ("positive","positive","passed","available","pinned"),("false_rejection_control","alternative","passed","available","pinned"),("subtle_false_acceptance_control","subtle","criterion_fail","available","pinned"),("multi_locus_false_acceptance_control","multi","criterion_fail","available","pinned"),("collateral_damage","collateral_damage","criterion_fail","available","pinned"),("missing_view","positive","insufficient_evidence","missing","pinned"),("transform_drift","positive","insufficient_evidence","available","different"),("invalid_artifact",None,"invalid_artifact","available","pinned")]:
                cases.append({"case_id":f"{task_id}-{kind}","task_id":task_id,"family":family,"kind":kind,"candidate":spec[key] if key else "not a valid artifact","expected":expected,"view_status":view_status,"transform_status":transform_status})
    transformations=[]
    for family,spec in FAMILIES.items(): transformations.append({"transformation_id":spec["transform"],"implementation":"prepare_freeze.py:render","implementation_sha256":"bound_by_freeze_manifest","authoritative_input":spec["shape"],"derived_output":"text/plain","permitted_invariances":["ordering where semantics are unchanged","whitespace"]})
    dump(HERE/"transformations.json",{"transformations":transformations})
    dump(HERE/"fixtures/calibration.json",{"authority":"builder_authored_contract_calibration_only","cases":cases})
    conditions=[{"condition_id":cid,"information_treatment":info,"repair_authorized":True,"hidden_criterion_access":cid=="criterion_disclosure","tool_id":"file-only-v2","harness_id":"isolated-repair-v2","model_id":"gpt-5.6-sol","provider_id":"openai-codex","budget_id":"equal-repair-budget-v2"} for cid,info in CONDITIONS]
    assignments=[]
    for task in tasks:
        for c,_ in CONDITIONS:
            for rep in range(1,6):
                a={"assignment_id":f"{task['task_id']}--{c}--r{rep}","task_id":task["task_id"],"family":task["family"],"condition_id":c,"configured_system_id":"gpt-5.6-sol-openai-codex-file-only-v2","repetition":rep,"seed":int(hashlib.sha256(f"{task['task_id']}|{c}|{rep}".encode()).hexdigest()[:8],16),"order_nonce_policy":"sha256(task|condition|repetition), randomized only after freeze audit","attempts_executed":0,"starting_artifact_sha256":sha(HERE/task["starting_artifact"])}; a["assignment_sha256"]=canon(a); assignments.append(a)
    protocol={"schema_version":"2.0.0","instrument_id":"self-inspection-repair-v2","status":"prospective_zero_call_candidate_freeze","general_hypothesis":"Information-specific repair support can outperform equal-budget retry across independent artifact shapes without increasing collateral damage.","scope_boundary":"Three synthetic mechanism families are not domain commitments or evidence of professional performance.","source_reviews":["reports/validation/2026-07-19-self-inspection-repair-v1-outcome-validity-audit.md","papers/agent-benchmarks/2026-07-19-tobench-omnimodal-closed-loop-validity.md","papers/agent-benchmarks/2026-07-15-agencybench-feedback-artifact-validity.md"],"tasks":tasks,"conditions":conditions,"assignments":assignments,"repetitions_per_task_condition_system":5,"budget":{"max_total_tokens_per_attempt":16000,"max_wall_seconds_per_attempt":300,"cost_ceiling_usd_total":25.0,"stop_before_spend_without_execution_authorization":True},"invalid_retry_policy":{"invalid_artifact":"no score; one infrastructure retry only if retained evidence proves transport corruption","insufficient_evidence":"no score; no agent retry unless missing view is an environment defect","observer_invalid":"no score; condition-blind adjudication required","service_invalid":"no score; retry with same assignment nonce and no new task information"},"observer_policy":{"observers":["checkers/observer_a.py","checkers/observer_b.py"],"condition_blind":True,"agreement_required":True,"disagreement_terminal_state":"observer_invalid","adjudication":"retain both outputs; independent reviewer may classify observer defect but may not infer endpoint"},"estimands":{"primary":"For each treatment vs retry_no_new_information: within-family mean repair-pass difference, then equal-weight mean across three families; report family-clustered uncertainty.","shape_reversal_gate":"No treatment-effect claim if a predeclared family contrast reverses sign or uncertainty includes zero.","secondary":["collateral-preservation difference","tokens per valid attempt","wall time per valid attempt"],"unit":"independent repetition within frozen task-condition-configured-system cell","clusters":"task family"},"calibration_gate":{"builder_authored_only":True,"reject_floor_or_ceiling":True,"required_pass_fraction_open_interval":[0.15,0.85],"no_post_treatment_tuning":True},"claim_ceiling":{"self_correction":False,"agent_capability":False,"treatment_effect":False,"professional_validity":False,"utility":False,"production_fitness":False,"readiness":False},"next_gate":"separate commit-bound independent freeze audit before any model, provider, or repair-row execution"}
    dump(HERE/"protocol.json",protocol)
    dump(HERE/"attempt-ledger.json",{"instrument_id":"self-inspection-repair-v2","attempts":[],"model_calls":0,"provider_calls":0,"repair_rows_executed":0})
    # Manifest binds all candidate bytes except generated reports and itself.
    files=[p for p in HERE.rglob("*") if p.is_file() and "__pycache__" not in p.parts and p.name not in {"freeze-manifest.json","preflight-report.json"}]
    bindings=[{"path":str(p.relative_to(HERE)),"bytes":p.stat().st_size,"sha256":sha(p)} for p in sorted(files)]
    dump(HERE/"freeze-manifest.json",{"schema_version":"2.0.0","instrument_id":"self-inspection-repair-v2","bindings":bindings,"assignment_set_sha256":canon(assignments),"model_calls":0,"provider_calls":0,"repair_rows_executed":0,"next_gate":protocol["next_gate"]})
    print(json.dumps({"tasks":len(tasks),"assignments":len(assignments),"calibration_cases":len(cases),"bindings":len(bindings)},sort_keys=True))
if __name__=="__main__": main()
