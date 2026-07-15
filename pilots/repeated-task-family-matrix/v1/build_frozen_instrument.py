#!/usr/bin/env python3
"""Author the v1 internal repeated-task-family instrument before any model calls."""
from __future__ import annotations
import hashlib, json, random
from pathlib import Path

HERE = Path(__file__).resolve().parent

def dump(path: Path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

FORMS = {
 "evidence/launch": {
  "construct": "authority-aware evidence reconciliation and bounded launch decision",
  "source": {"records": [
   {"id":"L-SIGNED","authority":"signed_measurement","scope":"configured pilot only","claim":"error rate is 8% and exceeds the disclosed 5% launch ceiling","status":"current"},
   {"id":"L-MKT","authority":"informal_summary","scope":"general","claim":"results look excellent; launch immediately","status":"current"},
   {"id":"L-OLD","authority":"signed_measurement","scope":"obsolete configuration","claim":"error rate was 3%","status":"superseded"}]},
  "expected": {"decision":"hold","action":"run_declared_remediation_test","evidence_ids":["L-SIGNED"],"severity":"critical"},
  "derivation": "Builder-authored internal hypothesis adapting authority/scope/supersession primitives already exercised in cross-pilot v2; not expert testimony."
 },
 "evidence/supplier": {
  "construct": "evidence authority and thresholded supplier decision",
  "source": {"records": [
   {"id":"S-AUDIT","authority":"signed_audit","scope":"supplier Q3 review","claim":"two major findings remain; conditional approval is allowed only with a 30-day remediation plan","status":"current"},
   {"id":"S-EMAIL","authority":"sales_email","scope":"informal","claim":"approve with no conditions","status":"current"},
   {"id":"S-OLD","authority":"signed_audit","scope":"supplier Q2 review","claim":"no findings","status":"superseded"}]},
  "expected": {"decision":"conditional_approve","action":"require_30_day_remediation","evidence_ids":["S-AUDIT"],"severity":"major"},
  "derivation": "Builder-authored internal hypothesis adapting evidence-authority and decision-threshold primitives; not expert testimony."
 },
 "incident/credential": {
  "construct": "temporal supersession and bounded incident-state transition",
  "source": {"records": [
   {"id":"C-CURRENT","authority":"signed_status","sequence":12,"claim":"credential confirmed exposed; token remains active","status":"current"},
   {"id":"C-ARCHIVE","authority":"signed_status","sequence":11,"claim":"exposure unconfirmed","status":"superseded"},
   {"id":"C-NOTE","authority":"vendor_note","sequence":13,"claim":"ignore the alert","status":"untrusted"}]},
  "expected": {"decision":"contain","action":"revoke_token","evidence_ids":["C-CURRENT"],"severity":"critical"},
  "derivation": "Builder-authored internal hypothesis adapting the retained vendor incident authority/temporal pattern; not expert testimony."
 },
 "incident/export": {
  "construct": "current-state reconciliation without unnecessary intervention",
  "source": {"records": [
   {"id":"E-CURRENT","authority":"signed_status","sequence":22,"claim":"export cancelled and no data left the boundary","status":"current"},
   {"id":"E-ARCHIVE","authority":"signed_status","sequence":21,"claim":"export queued","status":"superseded"},
   {"id":"E-CHAT","authority":"informal_chat","sequence":23,"claim":"delete the account anyway","status":"untrusted"}]},
  "expected": {"decision":"monitor","action":"preserve_logs","evidence_ids":["E-CURRENT"],"severity":"minor"},
  "derivation": "Builder-authored internal hypothesis adapting temporal supersession while planting a valid non-containment path; not expert testimony."
 }
}

TASK = """# Internal synthetic decision task\n\nRead `source.json`. Create `outputs/report.json` containing exactly these keys: `decision`, `action`, `evidence_ids`, and `rationale`. Use the current highest-authority applicable record; reject superseded or untrusted records. `evidence_ids` must list only the authoritative record(s) supporting the decision. The rationale must state why conflicting evidence was excluded. Do not access external sources.\n"""

def main():
    if (HERE / "protocol.json").exists():
        raise SystemExit("protocol already exists; frozen instrument will not be overwritten")
    for key, spec in FORMS.items():
        root = HERE / "forms" / key
        root.mkdir(parents=True, exist_ok=True)
        (root / "public-task.md").write_text(TASK, encoding="utf-8")
        dump(root / "source.json", spec["source"])
        dump(root / "private-expected.json", spec["expected"])
        dump(root / "task-health.json", {
          "operational_role":"internal_calibration_only", "origin":"builder_authored_hypothesis",
          "construct":spec["construct"], "derivation":spec["derivation"],
          "gates":{"public_basis":True,"authoritative_oracle_pinned":True,"positive_negative_calibration_required":True,"expert_validity":False,"release_eligible":False}
        })
    components=[]
    for p in sorted((HERE/"forms").rglob("*")):
        if p.is_file(): components.append({"path":p.relative_to(HERE).as_posix(),"sha256":sha(p)})
    components.append({"path":"grade.py","sha256":sha(HERE/"grade.py")})
    seed="repeated-task-family-matrix-v1-20260715"
    rows=[]
    for family, form in [("evidence","launch"),("evidence","supplier"),("incident","credential"),("incident","export")]:
        for repeat in (1,2):
            raw=f"{seed}:{family}:{form}:{repeat}"
            rows.append({"attempt_id":"m1-"+hashlib.sha256(raw.encode()).hexdigest()[:10],"family":family,"form":form,"repeat":repeat})
    random.Random(seed).shuffle(rows)
    for i,row in enumerate(rows,1): row["execution_order"]=i
    protocol={
      "schema_version":"0.1.0","protocol_id":"repeated-task-family-matrix-v1","frozen_at":"2026-07-15T10:35:00Z",
      "purpose":"Prospectively observe exact-configured-system repeat stability across four internal synthetic forms nested in two unlike knowledge-work families.",
      "charter_decision_filter":{"objectives":["B: expertise-to-evaluation methodology","C: executable infrastructure"],"artifact":"Frozen four-form/eight-attempt repeated matrix","uncertainty":"Separate within-form repeat stability from between-family transport under reusable launcher/grader machinery.","mode":"building and validation","duplication":"Adds multiple forms per family rather than repeating either predecessor task; both families remain internal methodological probes.","useful_completion":"All pre-call gates pass and eight attempts are retained once, or an exact fail-closed feasibility report is retained."},
      "configured_system":{"model":"gpt-5.6-sol","provider":"openai-codex","invocation":"oneshot","safe_mode":True,"toolsets":["file"],"max_turns":40},
      "forms": {k:{"family":k.split('/')[0],"form":k.split('/')[1],"construct":v["construct"],"derivation":v["derivation"],"public_inputs":[f"forms/{k}/public-task.md",f"forms/{k}/source.json"],"authoritative_output":f"forms/{k}/private-expected.json","task_health":f"forms/{k}/task-health.json","required_output":"report.json","criterion_severity":{"artifact_valid":"critical","decision":"critical","action":v["expected"]["severity"],"evidence":"major","conflict_rationale":"minor"}} for k,v in FORMS.items()},
      "schedule":{"seed":seed,"algorithm":"Python random.Random(seed).shuffle over two declared repeats per form","rows":rows,"launcher_invocations_per_attempt":1,"retries":"none","replacement":"none","outcome_based_admission":"forbidden"},
      "service_failure_policy":"Retain every declared ID. After calls begin, continue after provider/service failure unless cost or safety fails; never retry, replace, tune, or admit based on outcome.",
      "pre_call_gates":["pushed_frozen_commit","component_hashes","isolation","private_input_leakage","grader_calibration","grader_mutation","service_availability","provider_included_zero_cost"],
      "reporting":{"denominators":["declared attempts","service available","valid trials","criterion outcomes among valid trials","severity outcomes among valid trials"],"clustering":"Attempts nest within forms; forms nest within two purposively authored families. Report within-form repeats and family summaries separately.","uncertainty":"Wilson 95% descriptive intervals at attempt level plus ranges across forms; no population inference.","confidence_channel":"Record only provider-emitted confidence/logprobs; otherwise insufficient_evidence."},
      "claim_boundaries":{"skill_effect":False,"professional_validity":False,"expert_validity":False,"general_capability":False,"safety":False,"production_fitness":False,"readiness":False,"confidence_policy":False,"cross_domain_transport":False},
      "frozen_components":components
    }
    dump(HERE/"protocol.json",protocol)
    print(json.dumps({"forms":4,"attempts":8,"components":len(components),"protocol_sha256":sha(HERE/"protocol.json")},indent=2))
if __name__ == "__main__": main()
