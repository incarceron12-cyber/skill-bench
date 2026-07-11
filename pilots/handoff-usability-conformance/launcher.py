#!/usr/bin/env python3
"""Run two predeclared, isolated handoff-artifact attempts.

This reuses the repository's proven bubblewrap/Hermes file-only envelope while
keeping the private grader and repository outside the agent namespace.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, shutil, subprocess
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
PILOT = Path(__file__).resolve().parent
BASE = ROOT / "pilots/configured-artifact-revision/launcher.py"
RUNTIME = Path("/home/sam/.hermes/hermes-agent")
CASES = {
 "analysis-to-decision-memo": {
  "task": "Create outputs/handoff.json for the procurement decision owner. Use only source-pack files. JSON fields: format (memo-v1 or decision-brief-v1), recipient, recommendation, evidence_refs (source IDs), scope, risks (array), decision_request, next_step, blockers (array). Recommend approve only if the scorecard threshold is met and no risk is high. Do not invent evidence.\n",
  "sources": {"supplier-scorecard-v1.txt":"source_id: supplier-scorecard-v1\noverall_score: 84\napproval_threshold: 80\nscope: EU hosting renewal\n", "risk-register-v2.txt":"source_id: risk-register-v2\nhigh_risks: none\nmedium_risk: exit assistance has a 30-day notice requirement\n"},
  "expected": {"recipient":"procurement decision owner","recommendation":"approve","refs":{"supplier-scorecard-v1","risk-register-v2"},"formats":{"memo-v1","decision-brief-v1"},"fields":["scope","risks","decision_request"],"next":"next_step"}},
 "incident-record-to-operations": {
  "task": "Create outputs/handoff.json for the on-call operations lead. Use only source-pack files. JSON fields: format (incident-record-v2 or operations-ticket-v3), recipient, current_state, evidence_refs (source IDs), scope, owner, next_step, blockers (array). Follow the current runbook; if its precondition is unmet, make the next step an explicit block rather than execution. Do not invent evidence.\n",
  "sources": {"incident-timeline-v3.txt":"source_id: incident-timeline-v3\nscope: payments-api eu-west\ncurrent_state: elevated error rate; database failover is not confirmed\nowner: primary on-call\n", "service-runbook-v5.txt":"source_id: service-runbook-v5\nstep: drain payments-api traffic\nprecondition: database failover confirmed\nif_unmet: block drain and request failover confirmation from database on-call\n"},
  "expected": {"recipient":"on-call operations lead","refs":{"incident-timeline-v3","service-runbook-v5"},"formats":{"incident-record-v2","operations-ticket-v3"},"fields":["current_state","scope","owner","blockers"],"next":"next_step"}}
}

def sha(path: Path)->str: return hashlib.sha256(path.read_bytes()).hexdigest()
def dump(path:Path,obj:Any): path.parent.mkdir(parents=True,exist_ok=True); path.write_text(json.dumps(obj,indent=2,sort_keys=True)+"\n")
def load_base():
 spec=importlib.util.spec_from_file_location("revision_launcher",BASE); mod=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(mod); return mod

def materialize(root:Path, case_id:str, base:Any)->dict[str,Path]:
 if root.exists(): raise FileExistsError(root)
 inputs=root/"inputs"; outputs=root/"outputs"; profile=root/".profile"
 (inputs/"source-pack").mkdir(parents=True); (inputs/"outputs").mkdir(); outputs.mkdir()
 case=CASES[case_id]; (inputs/"public-task.md").write_text(case["task"])
 for name,text in case["sources"].items(): (inputs/"source-pack"/name).write_text(text)
 dump(inputs/"manifest.json",{"case_id":case_id,"inputs":"read_only","only_writable":"outputs","files":{p.relative_to(inputs).as_posix():sha(p) for p in inputs.rglob("*") if p.is_file()}})
 base._copy_runtime_profile(profile)
 return {"inputs":inputs,"outputs":outputs,"profile":profile}

def inventory(root:Path)->dict[str,str]: return {p.relative_to(root).as_posix():sha(p) for p in root.rglob("*") if p.is_file()}

def canary(root:Path,case_id:str,base:Any)->dict[str,Any]:
 paths=materialize(root,case_id,base)
 source_names=list(CASES[case_id]["sources"])
 code='''import json,os\nfrom tools.file_tools import read_file_tool,write_file_tool,search_tool\ndef ok(p):\n s=read_file_tool(p,limit=5).lower(); return not any(x in s for x in ("error reading", "file not found", "permission denied", "does not exist"))\nr={"cwd":os.getcwd(),"task":ok("public-task.md"),"sources":all(ok("source-pack/"+p) for p in SOURCE_NAMES),"repo_denied":not ok("/home/sam/skill-bench/data/work_queue.json"),"repo_search":"skill-bench" not in search_tool("skill-bench",target="files",path="/home/sam",limit=10),"output_write":"error" not in write_file_tool("outputs/canary.txt","ok\\n").lower(),"escape_denied":"error" in write_file_tool("escape.txt","bad\\n").lower()}\nprint(json.dumps(r))'''
 code="SOURCE_NAMES="+repr(source_names)+"\n"+code
 proc=subprocess.run(base._bwrap(paths,["/opt/hermes/venv/bin/python","-c",code]),capture_output=True,text=True,timeout=120)
 try: observed=json.loads(proc.stdout.strip().splitlines()[-1])
 except Exception: observed={}
 passed=proc.returncode==0 and observed.get("cwd")=="/trial" and all(observed.get(k) is True for k in ("task","sources","repo_denied","repo_search","output_write","escape_denied"))
 report={"passed":passed,"model_calls":0,"case_id":case_id,"observed":observed,"returncode":proc.returncode,"stderr":proc.stderr[-1000:],"input_inventory":inventory(paths["inputs"]),"launcher_sha256":sha(Path(__file__))}
 shutil.rmtree(paths["profile"],ignore_errors=True); dump(root/"canary-report.json",report)
 if not passed: raise RuntimeError(f"canary failed: {root}")
 return report

def grade(case_id:str, artifact:Path)->dict[str,Any]:
 try: value=json.loads(artifact.read_text()); valid=isinstance(value,dict)
 except Exception: value={}; valid=False
 exp=CASES[case_id]["expected"]
 if not valid: return {"outcome":"invalid_artifact","dimensions":{k:"not_evaluated" for k in ("substantive_correctness","provenance_boundary","destination_fit","recipient_usability","next_operation")}}
 refs=set(value.get("evidence_refs",[])); source_ok=refs==exp["refs"]
 substantive=source_ok and (case_id!="analysis-to-decision-memo" or value.get("recommendation")==exp["recommendation"])
 destination=value.get("format") in exp["formats"] and value.get("recipient")==exp["recipient"] and all(value.get(f) not in (None,"",[]) for f in exp["fields"] if f!="blockers") and all(f in value for f in exp["fields"])
 usability=destination and isinstance(value.get("evidence_refs"),list)
 next_ok=isinstance(value.get(exp["next"]),str) and bool(value.get(exp["next"]).strip())
 if case_id=="incident-record-to-operations": next_ok=next_ok and bool(value.get("blockers")) and "confirm" in value["next_step"].lower()
 dims={"substantive_correctness":"pass" if substantive else "fail","provenance_boundary":"pass" if source_ok else "fail","destination_fit":"pass" if destination else "fail","recipient_usability":"pass" if usability else "fail","next_operation":"pass" if next_ok else "fail"}
 return {"outcome":"pass" if all(v=="pass" for v in dims.values()) else "fail","dimensions":dims}

def run(root:Path,case_id:str)->dict[str,Any]:
 base=load_base(); pre=canary(root/"preflight",case_id,base); paths=materialize(root/"trial",case_id,base); before=inventory(paths["inputs"])
 prompt=(paths["inputs"]/"public-task.md").read_text(); cmd=base._trial_command(prompt); proc=subprocess.run(base._bwrap(paths,cmd),capture_output=True,text=True,timeout=900)
 (root/"redacted-trace.log").write_text(proc.stdout); (root/"launcher-stderr.log").write_text(proc.stderr)
 artifact=paths["outputs"]/"handoff.json"; usage=paths["outputs"]/"usage.json"; complete=proc.returncode==0 and artifact.is_file() and usage.is_file(); valid_env=pre["passed"] and before==inventory(paths["inputs"])
 score=grade(case_id,artifact) if complete and valid_env else {"outcome":"not_scored","dimensions":{}}
 dump(root/"grader-report.json",score)
 report={"attempt_id":root.name,"case_id":case_id,"complete":complete,"valid_environment":valid_env,"returncode":proc.returncode,"configured_system":{"model":"gpt-5.6-sol","provider":"openai-codex","toolsets":["file"],"safe_mode":True},"component_hashes":{"launcher":sha(Path(__file__)),"task":sha(paths["inputs"]/"public-task.md"),"manifest":sha(paths["inputs"]/"manifest.json")},"artifacts":{p.name:{"sha256":sha(p),"bytes":p.stat().st_size} for p in (artifact,usage) if p.is_file()},"grader":score,"trace":{"path":"redacted-trace.log","sha256":sha(root/"redacted-trace.log")},"claim_boundaries":{"human_recipient_usability":False,"expert_validity":False,"capability":False,"cross_domain_generalization":False,"treatment_effect":False,"readiness":False}}
 shutil.rmtree(paths["profile"],ignore_errors=True); dump(root/"trial-report.json",report); return report

def main()->int:
 p=argparse.ArgumentParser(); p.add_argument("case",choices=CASES); p.add_argument("--run-root",type=Path,required=True); a=p.parse_args(); report=run(a.run_root.resolve(),a.case); print(json.dumps(report,indent=2)); return 0 if report["valid_environment"] else 1
if __name__=="__main__": raise SystemExit(main())
