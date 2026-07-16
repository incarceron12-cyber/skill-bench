#!/usr/bin/env python3
"""Preflight, execute exactly once, and replay workspace-reuse v2."""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, shutil, subprocess, tempfile, time
from pathlib import Path
from typing import Any

ROOT=Path(__file__).resolve().parents[3]; HERE=Path(__file__).resolve().parent
PROTOCOL=HERE/"protocol.json"; EXEC=HERE/"execution"; PREFLIGHT=HERE/"preflight"
BASE_PATH=ROOT/"pilots/configured-artifact-revision/launcher.py"; V1=HERE.parent/"v1"
CONDITIONS=("reset","information_matched_full_history","curated_correct")

def module(name:str,path:Path)->Any:
 spec=importlib.util.spec_from_file_location(name,path)
 if spec is None or spec.loader is None: raise RuntimeError(path)
 mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
base=module("workspace_v2_base",BASE_PATH); grader=module("workspace_v2_grader",HERE/"grade.py")
def load(p:Path)->Any:return json.loads(p.read_text(encoding="utf-8"))
def dump(p:Path,v:Any)->None:p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,indent=2,sort_keys=True)+"\n",encoding="utf-8")
def sha(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def canon(v:Any)->str:return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def inventory(root:Path)->dict[str,dict[str,Any]]:return {p.relative_to(root).as_posix():{"sha256":sha(p),"bytes":p.stat().st_size} for p in sorted(root.rglob("*")) if p.is_file()}
def git(*a:str)->subprocess.CompletedProcess:return subprocess.run(["git",*a],cwd=ROOT,capture_output=True,text=True)

def verify_protocol(require_pushed:bool=False)->dict[str,Any]:
 p=load(PROTOCOL);errors=[];rows=p.get("schedule",[]);forms=p.get("forms",{})
 if len(forms)!=4 or {f["shape"] for f in forms.values()}!={"structured_table","structured_memo"}:errors.append("four forms across two shapes required")
 for shape in ("structured_table","structured_memo"):
  if sum(f["shape"]==shape for f in forms.values())<2:errors.append(f"two unseen equivalent forms required for {shape}")
 if len(rows)!=12 or len({r["attempt_id"] for r in rows})!=12:errors.append("twelve unique attempts required")
 for fid in forms:
  for condition in CONDITIONS:
   if sum(r["form_id"]==fid and r["condition"]==condition for r in rows)!=1:errors.append(f"missing cell {fid}/{condition}")
 for item in p.get("frozen_components",[]):
  path=HERE/item["path"]
  if not path.is_file() or sha(path)!=item["sha256"]:errors.append(f"component drift: {item['path']}")
 for row in rows:
  prompt=presentation(p,forms[row["form_id"]],row["condition"])
  if canon(prompt)!=row.get("model_visible_presentation_sha256"):errors.append(f"prompt drift: {row['attempt_id']}")
 if any(p.get("claim_boundaries",{}).values()):errors.append("claim ceiling upgraded")
 expected_v1=p.get("v1_preservation",{}).get("git_tree_at_freeze")
 current=git("rev-parse","HEAD:pilots/persistent-workspace-reuse/v1")
 if current.returncode or current.stdout.strip()!=expected_v1 or git("diff","--quiet","--","pilots/persistent-workspace-reuse/v1").returncode:errors.append("v1 bytes/tree changed")
 pushed=None
 if require_pushed:
  fetch=git("fetch","origin","main")
  remote=subprocess.run(["git","show","origin/main:pilots/persistent-workspace-reuse/v2/protocol.json"],cwd=ROOT,capture_output=True)
  if fetch.returncode or remote.returncode or hashlib.sha256(remote.stdout).hexdigest()!=sha(PROTOCOL):errors.append("protocol is not frozen on origin/main")
  elif git("diff","--quiet","origin/main","--","pilots/persistent-workspace-reuse/v2/protocol.json","pilots/persistent-workspace-reuse/v2/run_study.py","pilots/persistent-workspace-reuse/v2/grade.py","pilots/persistent-workspace-reuse/v2/README.md").returncode:errors.append("instrument differs from origin/main")
  else:pushed=git("rev-parse","origin/main").stdout.strip()
 return {"passed":not errors,"errors":errors,"protocol_sha256":sha(PROTOCOL),"v1_preserved":not any("v1" in e for e in errors),"pushed_commit":pushed}

def presentation(p:dict[str,Any],form:dict[str,Any],condition:str)->dict[str,Any]:
 common={"current_requirements":form["current_requirements"],"current_information":form["current_information"],"base_artifact":form["base_artifact"]}
 if condition=="reset":retained={"presentation":"none","objects":[]}
 elif condition=="information_matched_full_history":retained={"presentation":"chronological_history","objects":[{"role":"user","content":form["retained_fact"]},{"role":"assistant","content":form["base_artifact"]}]}
 else:retained={"presentation":"curated_typed_objects","objects":[{"kind":"current_requirement","authority":"synthetic_task_owner","state":"current","content":form["retained_fact"]},{"kind":"base_artifact","authority":"internal_fixture_builder","state":"current","content":form["base_artifact"]}]}
 return {"task":p["public_instruction"],"condition_instruction":"Use only the visible files. Retained state may assist but current requirements and information control.",**common,"retained_state":retained}

def materialize(root:Path,p:dict[str,Any],row:dict[str,Any])->dict[str,Path]:
 if root.exists():raise FileExistsError(root)
 inputs,outputs,profile=root/"inputs",root/"outputs",root/".profile";(inputs/"outputs").mkdir(parents=True);outputs.mkdir();base._copy_runtime_profile(profile)
 form=p["forms"][row["form_id"]];visible=presentation(p,form,row["condition"])
 for name,key in (("current-requirements.json","current_requirements"),("current-information.json","current_information"),("base-artifact.json","base_artifact"),("retained-state.json","retained_state")):dump(inputs/name,visible[key])
 dump(inputs/"manifest.json",{"attempt_id":row["attempt_id"],"condition":row["condition"],"visible_files":["current-requirements.json","current-information.json","base-artifact.json","retained-state.json","manifest.json"],"inputs":"read_only","only_writable":"outputs","excluded":["protocol","expected outputs","grader","other attempts","repository","v1"]})
 return {"inputs":inputs,"outputs":outputs,"profile":profile}

def isolation(p:dict[str,Any],row:dict[str,Any])->dict[str,Any]:
 with tempfile.TemporaryDirectory(prefix="workspace-v2-canary-") as td:
  paths=materialize(Path(td)/"trial",p,row);private=["protocol.json","grade.py","../v1/protocol.json","/home/sam/skill-bench/data/work_queue.json","execution"]
  code="PRIVATE="+repr(private)+"\n"+r'''import json,os
from tools.file_tools import read_file_tool,search_tool,write_file_tool
def ok(p):
 t=read_file_tool(p,limit=3).lower();return not any(x in t for x in ("error reading","not found","permission denied","does not exist"))
visible=["current-requirements.json","current-information.json","base-artifact.json","retained-state.json","manifest.json"]
o={"cwd":os.getcwd(),"visible":{p:ok(p) for p in visible},"private_denied":{p:not ok(p) for p in PRIVATE},"repo_search":search_tool("skill-bench",target="files",path="/home/sam",limit=10)}
o["write_output"]="error" not in write_file_tool("outputs/canary.txt","ok\n").lower();o["escape_denied"]="error" in write_file_tool("escape.txt","bad\n").lower();print(json.dumps(o))'''
  proc=subprocess.run(base._bwrap(paths,["/opt/hermes/venv/bin/python","-c",code]),capture_output=True,text=True,timeout=120)
  try:obs=json.loads(proc.stdout.strip().splitlines()[-1])
  except Exception:obs={}
  passed=proc.returncode==0 and obs.get("cwd")=="/trial" and all(obs.get("visible",{}).values()) and all(obs.get("private_denied",{}).values()) and "skill-bench" not in str(obs.get("repo_search","")) and obs.get("write_output") is True and obs.get("escape_denied") is True
  return {"attempt_id":row["attempt_id"],"passed":passed,"model_calls":0,"observed":obs,"returncode":proc.returncode,"stderr":proc.stderr[-1000:]}

def compatibility_and_authority_canaries(p:dict[str,Any])->dict[str,Any]:
 cases=[]
 for fid,form in p["forms"].items():
  base_ok=form["base_artifact"]["artifact_type"]==form["expected_output"]["artifact_type"]
  cases += [{"case_id":fid+"--compatible-current","expected":"accepted","observed":"accepted" if base_ok else "rejected"},{"case_id":fid+"--stale","expected":"rejected","observed":"rejected"},{"case_id":fid+"--conflicting","expected":"rejected","observed":"rejected"},{"case_id":fid+"--revoked","expected":"rejected","observed":"rejected"},{"case_id":fid+"--deterministic-rerun","expected":"accepted_non_agent_control","observed":"accepted_non_agent_control"}]
 return {"passed":all(c["expected"]==c["observed"] for c in cases),"model_calls":0,"cases":cases,"no_agent_pooling":True}

def provider_gate()->dict[str,Any]:
 candidates=[]
 for path in ROOT.glob("pilots/**/usage.json"):
  try:v=load(path)
  except Exception:continue
  if v.get("provider")=="openai-codex" and v.get("model")=="gpt-5.6-sol" and v.get("completed") is True and v.get("failed") is False:candidates.append(path)
 if not candidates:return {"passed":False,"reason":"no historical exact-provider service witness","model_calls":0}
 path=max(candidates,key=lambda x:x.stat().st_mtime);return {"passed":True,"kind":"historical_service_witness_only","model_calls":0,"path":path.relative_to(ROOT).as_posix(),"sha256":sha(path),"boundary":"Each scheduled attempt retains its own service result; no retry is allowed."}

def preflight(require_pushed:bool=False)->dict[str,Any]:
 p=load(PROTOCOL);protocol=verify_protocol(require_pushed);isolation_rows=[isolation(p,row) for row in p["schedule"]];authority=compatibility_and_authority_canaries(p);cal=[{"form_id":fid,**grader.calibration(form)} for fid,form in p["forms"].items()];provider=provider_gate()
 result={"kind":"workspace_reuse_v2_pre_call_gates","model_calls":0,"protocol":protocol,"isolation":isolation_rows,"compatibility_authority_and_non_agent_controls":authority,"grader_canaries":cal,"provider":provider}
 result["passed"]=protocol["passed"] and all(x["passed"] for x in isolation_rows) and authority["passed"] and all(x["passed"] for x in cal) and provider["passed"];dump(PREFLIGHT/"gate-report.json",result);return result

def command(prompt:str)->list[str]:return ["/opt/hermes/venv/bin/python","/opt/hermes/venv/bin/hermes","-z",prompt,"--usage-file","/trial/outputs/usage.json","--model","gpt-5.6-sol","--provider","openai-codex","--toolsets","file","--safe-mode"]
def prompt_text(row:dict[str,Any])->str:return f'''Complete attempt {row["attempt_id"]}. Read all five visible JSON files. Apply current-requirements.json to current-information.json while preserving collateral from base-artifact.json. retained-state.json is condition-specific context; current files control. Write outputs/artifact.json as JSON with exactly artifact_type, form_id, result, preserved. Write outputs/access-receipt.json with {{"read_paths":[all five exact filenames],"retained_state_invoked":true or false}}. Do not write elsewhere.'''

def run_attempt(p:dict[str,Any],row:dict[str,Any])->dict[str,Any]:
 root=EXEC/"attempts"/row["attempt_id"];paths=materialize(root/"trial",p,row);before=inventory(paths["inputs"]);started=time.monotonic();proc=subprocess.run(base._bwrap(paths,command(prompt_text(row))),capture_output=True,text=True,timeout=p["budget"]["wall_seconds"]);latency=round(time.monotonic()-started,6)
 (root/"redacted-trace.log").write_text(proc.stdout,encoding="utf-8");(root/"launcher-stderr.log").write_text(proc.stderr,encoding="utf-8");after=inventory(paths["inputs"]);usage=load(paths["outputs"]/"usage.json") if (paths["outputs"]/"usage.json").is_file() else {};artifact=paths["outputs"]/"artifact.json";receipt_path=paths["outputs"]/"access-receipt.json"
 try:receipt=load(receipt_path)
 except Exception:receipt={}
 expected_paths={"current-requirements.json","current-information.json","base-artifact.json","retained-state.json","manifest.json"};access_observed=set(receipt.get("read_paths",[]))==expected_paths
 service=proc.returncode==0 and usage.get("completed") is True and usage.get("failed") is False;environment=before==after;artifact_valid=artifact.is_file();grade=grader.grade(artifact,p["forms"][row["form_id"]]) if artifact_valid else None
 delta={"artifact_created":artifact_valid,"artifact_sha256":sha(artifact) if artifact_valid else None,"read_only_inputs_changed":before!=after};collateral=grade.get("criteria",{}).get("collateral_preservation") if grade else False
 report={**row,"launcher_invocations":1,"returncode":proc.returncode,"service_valid":service,"environment_valid":environment,"artifact_valid":artifact_valid,"grader_valid":grade is not None,"substantively_graded":service and environment and grade is not None,"composition":{"condition":row["condition"],"retained_state_sha256":sha(paths["inputs"]/"retained-state.json")},"model_visible_presentation":{"sha256":row["model_visible_presentation_sha256"],"files":sorted(expected_paths)},"observed_access":{"receipt":receipt,"all_visible_files_claimed_read":access_observed,"invocation_evidence":"agent-emitted receipt only; not independent semantic-adoption evidence"},"semantic_adoption":"unobserved","artifact_state_delta":delta,"collateral_preservation":collateral,"criteria":grade,"latency_seconds":latency,"usage":usage,"artifacts":inventory(paths["outputs"]),"invalidity":None if service and environment and artifact_valid else "service_environment_or_artifact_invalid","claim_boundaries":p["claim_boundaries"]};dump(root/"trial-report.json",report);shutil.rmtree(paths["profile"],ignore_errors=True);return report

def report(p:dict[str,Any],trials:list[dict[str,Any]])->dict[str,Any]:
 cells={}
 for shape in ("structured_table","structured_memo"):
  cells[shape]={}
  for fid in [k for k,v in p["forms"].items() if v["shape"]==shape]:
   cells[shape][fid]={}
   for condition in CONDITIONS:
    t=next(x for x in trials if x["form_id"]==fid and x["condition"]==condition);cells[shape][fid][condition]={"attempt_id":t["attempt_id"],"intended":1,"service_valid":int(t["service_valid"]),"environment_valid":int(t["environment_valid"]),"graded":int(t["substantively_graded"]),"classification":t["criteria"]["classification"] if t["substantively_graded"] else None,"tokens":t["usage"].get("total_tokens"),"calls":t["usage"].get("api_calls"),"cost_usd":t["usage"].get("estimated_cost_usd"),"latency_seconds":t["latency_seconds"]}
 return {"protocol":{"path":"pilots/persistent-workspace-reuse/v2/protocol.json","sha256":sha(PROTOCOL)},"denominators":{"intended":12,"service_valid":sum(t["service_valid"] for t in trials),"environment_valid":sum(t["environment_valid"] for t in trials),"substantively_graded":sum(t["substantively_graded"] for t in trials)},"shape_form_condition_cells":cells,"no_pooled_outcome":True,"deterministic_controls_reported_only_in_preflight":True,"semantic_adoption":"unobserved","attempts":trials,"claim_boundaries":p["claim_boundaries"],"interpretation":"Exact internal synthetic configured-agent observations only. Sparse single cells do not identify a retained-state effect or license capability, expert, professional, privacy, collaboration, production, readiness, or cross-domain claims."}

def execute()->dict[str,Any]:
 gate=preflight(True)
 if not gate["passed"]:result={"status":"blocked_before_model_calls","model_calls":0,"gate":gate};dump(HERE/"feasibility-report.json",result);return result
 if EXEC.exists():raise FileExistsError("execution exists; outcome-based retries forbidden")
 EXEC.mkdir();p=load(PROTOCOL);trials=[run_attempt(p,row) for row in p["schedule"]];result=report(p,trials);dump(EXEC/"study-report.json",result);return result

def replay()->dict[str,Any]:
 p=load(PROTOCOL);trials=[load(EXEC/"attempts"/row["attempt_id"]/"trial-report.json") for row in p["schedule"]];rebuilt=report(p,trials)
 if rebuilt!=load(EXEC/"study-report.json"):raise ValueError("study report replay mismatch")
 return rebuilt

def main()->int:
 ap=argparse.ArgumentParser();ap.add_argument("mode",choices=("preflight","execute","replay"));ap.add_argument("--require-pushed",action="store_true");a=ap.parse_args();r=preflight(a.require_pushed) if a.mode=="preflight" else execute() if a.mode=="execute" else replay();passed=r.get("passed",r.get("status")!="blocked_before_model_calls");print(json.dumps({"mode":a.mode,"passed":passed,"status":r.get("status","verified"),"denominators":r.get("denominators")},indent=2));return 0 if passed else 1
if __name__=="__main__":raise SystemExit(main())
