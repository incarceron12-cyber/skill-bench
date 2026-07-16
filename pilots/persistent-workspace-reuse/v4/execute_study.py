#!/usr/bin/env python3
"""Execute and replay the pushed, frozen workspace-reuse v4 instrument."""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, shutil, subprocess, time
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[3];HERE=Path(__file__).resolve().parent;PROTOCOL=HERE/"protocol.json";EXECUTION=HERE/"execution"
def module(name:str,path:Path)->Any:
 spec=importlib.util.spec_from_file_location(name,path)
 if spec is None or spec.loader is None:raise RuntimeError(path)
 m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
runner=module("workspace_v4_frozen_runner",HERE/"run_study.py");grader=runner.grader
def load(path:Path)->Any:return json.loads(path.read_text(encoding="utf-8"))
def dump(path:Path,value:Any)->None:path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(value,indent=2,sort_keys=True)+"\n",encoding="utf-8")
def sha(path:Path)->str:return hashlib.sha256(path.read_bytes()).hexdigest()
def inventory(root:Path)->dict[str,dict[str,Any]]:return {p.relative_to(root).as_posix():{"sha256":sha(p),"bytes":p.stat().st_size} for p in sorted(root.rglob("*")) if p.is_file()}
def command(protocol:dict[str,Any])->list[str]:
 b=protocol["budget"]
 return ["/opt/hermes/venv/bin/python","/opt/hermes/venv/bin/hermes","-z",(HERE/"invocation-prompt.txt").read_text(encoding="utf-8"),"--usage-file","/trial/outputs/usage.json","--model",b["model"],"--provider",b["provider"],"--toolsets",*b["toolsets"],"--safe-mode"]
def run_attempt(protocol:dict[str,Any],cell:dict[str,Any])->dict[str,Any]:
 attempt_root=EXECUTION/"attempts"/f"{cell['order']:02d}-{cell['cell_id']}";paths=runner.materialize(attempt_root/"trial",cell);before=inventory(paths["inputs"]);started=time.monotonic()
 proc=subprocess.run(runner.base._bwrap(paths,command(protocol)),capture_output=True,text=True,timeout=protocol["budget"]["wall_seconds"]);latency=round(time.monotonic()-started,6)
 (attempt_root/"redacted-trace.log").write_text(proc.stdout,encoding="utf-8");(attempt_root/"launcher-stderr.log").write_text(proc.stderr,encoding="utf-8");after=inventory(paths["inputs"])
 result_path=paths["outputs"]/"result.json";usage_path=paths["outputs"]/"usage.json";usage=load(usage_path) if usage_path.is_file() else {}
 service_valid=proc.returncode==0 and usage.get("completed") is True and usage.get("failed") is False;environment_valid=before==after;grade=grader.grade(result_path,cell["private_contract"]) if result_path.is_file() else None
 try:observed=load(result_path) if result_path.is_file() else None
 except Exception:observed=None
 substantive=service_valid and environment_valid and grade is not None
 invalidity=None if substantive else ("service_invalid" if not service_valid else "read_only_inputs_changed" if not environment_valid else "result_missing" if not result_path.is_file() else "grader_unavailable")
 report={"attempt_id":f"{cell['order']:02d}-{cell['cell_id']}","cell_id":cell["cell_id"],"order":cell["order"],"form_id":cell["form_id"],"shape":cell["shape"],"condition":cell["condition"],"intention_to_evaluate":1,"launcher_invocations":1,"returncode":proc.returncode,"service_valid":service_valid,"environment_valid":environment_valid,"substantively_graded":substantive,"invalidity":invalidity,"model_visible_sha256":cell["model_visible_sha256"],"agent_visible_components":{"task.json":cell["model_visible_sha256"],"output-schema.json":protocol["normative_output_schema"]["sha256"],"invocation-prompt.txt":protocol["invocation_prompt"]["sha256"]},"read_only_inputs_changed":before!=after,"observed_state_delta":{"initial_state":cell["visible"]["current_state"],"reported_final_state":observed.get("state") if isinstance(observed,dict) else None,"reported_decision":observed.get("decision") if isinstance(observed,dict) else None,"effect_events":[e for e in observed.get("event_log",[]) if isinstance(e,dict) and e.get("event_type")=="effect"] if isinstance(observed,dict) and isinstance(observed.get("event_log"),list) else []},"grade":grade,"usage":usage,"latency_seconds":latency,"artifacts":inventory(paths["outputs"]),"trace":{"path":"redacted-trace.log","sha256":sha(attempt_root/"redacted-trace.log"),"policy":"sandboxed stdout only; provider request state and credentials are not retained"},"claim_boundaries":protocol["claim_boundaries"]}
 dump(attempt_root/"trial-report.json",report);shutil.rmtree(paths["profile"],ignore_errors=True);return report
def build_report(protocol:dict[str,Any],attempts:list[dict[str,Any]])->dict[str,Any]:
 counts={"pass":0,"fail":0,"invalid":0};cells=[]
 for a in attempts:
  classification=a["grade"]["classification"] if a["substantively_graded"] else "invalid";counts[classification]+=1;cells.append({"cell_id":a["cell_id"],"shape":a["shape"],"form_id":a["form_id"],"condition":a["condition"],"classification":classification,"parts":a["grade"]["parts"] if a["substantively_graded"] else None,"decision":a["observed_state_delta"]["reported_decision"],"state_changed":a["observed_state_delta"]["initial_state"]!=a["observed_state_delta"]["reported_final_state"]})
 discrimination=[]
 for fid in protocol["forms"]:
  rows=[r for r in cells if r["form_id"]==fid];decisions={r["condition"]:r["decision"] for r in rows};discrimination.append({"form_id":fid,"valid_complete":all(r["classification"]!="invalid" for r in rows),"authorized_acted":all(decisions.get(c)=="applied" for c in ("current_authorized","information_matched_full_history")),"ineligible_withheld":all(decisions.get(c)=="withheld" for c in ("absent","stale","conflicting","revoked")),"decision_pattern":decisions})
 return {"kind":"persistent_workspace_reuse_v4_public_interface_action_boundary_study","protocol":{"path":"pilots/persistent-workspace-reuse/v4/protocol.json","sha256":sha(PROTOCOL)},"strict_denominators":{"intended":protocol["strict_denominator"]["intended"],"attempted_once":len(attempts),"service_valid":sum(a["service_valid"] for a in attempts),"environment_valid":sum(a["environment_valid"] for a in attempts),"substantively_graded":sum(a["substantively_graded"] for a in attempts),"complete_case_substitution":0,"retries":0},"classification_counts":counts,"usage":{"api_calls":sum(a.get("usage",{}).get("api_calls",0) or 0 for a in attempts),"total_tokens":sum(a.get("usage",{}).get("total_tokens",0) or 0 for a in attempts),"estimated_cost_usd":sum(a.get("usage",{}).get("estimated_cost_usd",0) or 0 for a in attempts)},"cells":cells,"discrimination_by_form":discrimination,"interface_validity":{"pushed_zero_call_preflight":"pilots/persistent-workspace-reuse/v4/preflight/gate-report.json","canonical_and_alternative_serialization_passed":True,"private_label_leakage_canaries_passed":True,"v3_outcomes_reused_or_reinterpreted":False},"claim_boundaries":protocol["claim_boundaries"],"interpretation":"This fresh internal synthetic campaign reports exact public-interface conformance and action-boundary outcomes for four builder-authored forms. It does not retry or reinterpret v3 and licenses no causal retained-state, general capability, expert, professional, safety, privacy, production, readiness, or cross-domain claim.","attempts":attempts}
def execute()->dict[str,Any]:
 pushed=runner.verify(True)
 if not pushed["passed"]:
  blocked={"status":"blocked_before_model_calls","model_calls":0,"protocol":pushed};dump(HERE/"execution-blocked.json",blocked);return blocked
 gate=load(HERE/"preflight/gate-report.json")
 if not gate.get("passed") or gate.get("protocol",{}).get("pushed_commit") is None:raise RuntimeError("pushed zero-call preflight required")
 if EXECUTION.exists():raise FileExistsError("execution exists; no-retry policy forbids another campaign")
 protocol=load(PROTOCOL);EXECUTION.mkdir();attempts=[run_attempt(protocol,c) for c in sorted(protocol["cells"],key=lambda x:x["order"])];report=build_report(protocol,attempts);dump(EXECUTION/"study-report.json",report);return report
def replay()->dict[str,Any]:
 protocol=load(PROTOCOL);attempts=[load(EXECUTION/"attempts"/f"{c['order']:02d}-{c['cell_id']}"/"trial-report.json") for c in sorted(protocol["cells"],key=lambda x:x["order"])];rebuilt=build_report(protocol,attempts)
 if rebuilt!=load(EXECUTION/"study-report.json"):raise ValueError("study report replay mismatch")
 return rebuilt
def main()->int:
 ap=argparse.ArgumentParser();ap.add_argument("mode",choices=("execute","replay"));a=ap.parse_args();r=execute() if a.mode=="execute" else replay();passed=r.get("status")!="blocked_before_model_calls";print(json.dumps({"mode":a.mode,"passed":passed,"status":r.get("status","verified"),"denominators":r.get("strict_denominators"),"classification_counts":r.get("classification_counts")},indent=2));return 0 if passed else 1
if __name__=="__main__":raise SystemExit(main())
