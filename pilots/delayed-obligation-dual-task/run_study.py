#!/usr/bin/env python3
"""Conformance, isolated execution, deterministic grading, and replay."""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,shutil,subprocess,tempfile,time
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
PROTOCOL=HERE/"protocol.json";SCENARIOS=HERE/"instrument/scenarios.json";CAL=HERE/"instrument/calibration-cases.json";EXEC=HERE/"execution";PREFLIGHT=HERE/"preflight/canary-report.json";BASE=ROOT/"pilots/configured-artifact-revision/launcher.py"
def module(name:str,path:Path)->Any:
 spec=importlib.util.spec_from_file_location(name,path)
 if spec is None or spec.loader is None:raise RuntimeError(path)
 mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
base=module("delayed_base",BASE)
def load(p:Path)->Any:return json.loads(p.read_text())
def dump(p:Path,v:Any)->None:p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,indent=2,sort_keys=True)+"\n")
def sha(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def inventory(root:Path)->dict[str,Any]:return {p.relative_to(root).as_posix():{"sha256":sha(p),"bytes":p.stat().st_size} for p in sorted(root.rglob("*")) if p.is_file()}
def classify(o:dict[str,bool])->str:
 if not o["encoded"]:return "encoding_retention_failure"
 if not o["update_accessed"]:return "cue_monitoring_access_failure"
 if not o["updated_state"] or o["obsolete_action"]:return "update_reconciliation_failure"
 if o["premature"] or not o["cue_accessed"] or not o["due_inferred"]:return "due_status_or_timing_failure"
 if o["intended_current"] and not o["realized_current"]:return "action_realization_failure"
 if not o["intended_current"] or not o["realized_current"]:return "due_status_or_timing_failure"
 if not o["primary_preserved"]:return "collateral_primary_work_loss"
 return "success"
def calibration()->dict[str,Any]:
 results=[]
 for c in load(CAL)["cases"]:
  observed=classify(c["observed"]);results.append({"case_id":c["case_id"],"expected":c["expected"],"observed":observed,"passed":observed==c["expected"]})
 return {"passed":all(x["passed"] for x in results),"model_calls":0,"results":results}
def scenario(sid:str)->dict[str,Any]:return next(x for x in load(SCENARIOS)["scenarios"] if x["scenario_id"]==sid)
def treatment(condition:str,turn:int,s:dict[str,Any],prior_query:bool)->str:
 o=s["obligation"]
 if condition=="oracle_reminder":return f"Oracle-derived reminder: {'the current update is '+o['update'] if turn==2 else 'the current due action is '+o['updated_id'] if turn==3 else 'retain the authorized obligation until updated or due'}."
 if condition=="channel_hint":return "Neutral channel hint: consider querying obligation_channel now for information that may be available next turn. No action or answer is disclosed."
 return "Neutral interruption: continue the primary work. No obligation channel, action, or answer is disclosed."
def public_event(turn:int,s:dict[str,Any],prior_query:bool)->str:
 o=s["obligation"]
 if turn==1:return "Authorized instruction: "+o["original_instruction"]
 if turn==2:return ("Queried obligation channel: "+o["update"]) if prior_query else "Primary-work checkpoint reached; no obligation-channel content was accessed."
 return o["due_cue"]+((" Queried obligation channel confirms: "+o["update"]) if prior_query else "")
def primary_ok(a:dict[str,Any],s:dict[str,Any])->bool:
 p=a.get("primary",{});return p.get("decision")==s["primary"]["correct_decision"] and set(s["primary"]["required_source_ids"])<=set(p.get("source_ids",[])) and isinstance(p.get("rationale"),str) and len(p["rationale"].strip())>=20
def state_has(a:dict[str,Any],oid:str,statuses:set[str]|None=None)->bool:
 return any(x.get("obligation_id")==oid and (statuses is None or x.get("status") in statuses) for x in a.get("obligation_state",[]) if isinstance(x,dict))
def observations(actions:list[dict[str,Any]],s:dict[str,Any],condition:str)->dict[str,bool]:
 o=s["obligation"];q1="obligation_channel" in actions[0].get("monitoring_queries",[]);q2="obligation_channel" in actions[1].get("monitoring_queries",[]);update_accessed=condition=="oracle_reminder" or q1
 realized=[set(a.get("realized_actions",[])) for a in actions];intended=[set(a.get("intended_actions",[])) for a in actions]
 return {"encoded":state_has(actions[0],o["original_id"]),"update_accessed":update_accessed,"updated_state":state_has(actions[1],o["updated_id"]) or state_has(actions[2],o["updated_id"]),"cue_accessed":True,"due_inferred":state_has(actions[2],o["updated_id"],{"due","completed"}),"premature":any(o["updated_id"] in realized[i] or o["original_id"] in realized[i] for i in (0,1)),"obsolete_action":o["original_id"] in realized[2],"intended_current":o["updated_id"] in intended[2],"realized_current":o["updated_id"] in realized[2],"primary_preserved":all(primary_ok(a,s) for a in actions)}
def verify_protocol(require_remote:bool)->dict[str,Any]:
 errors=[]
 if not PROTOCOL.is_file():return {"passed":False,"errors":["protocol missing"]}
 p=load(PROTOCOL);rows=p["schedule"]["rows"]
 if len(rows)!=6 or len({x["attempt_id"] for x in rows})!=6:errors.append("matrix must have six unique attempts")
 for item in p["frozen_components"]:
  q=ROOT/item["path"]
  if not q.is_file() or sha(q)!=item["sha256"]:errors.append("component drift: "+item["path"])
 remote=None
 if require_remote:
  f=subprocess.run(["git","fetch","origin","main"],cwd=ROOT,capture_output=True)
  r=subprocess.run(["git","show","origin/main:pilots/delayed-obligation-dual-task/protocol.json"],cwd=ROOT,capture_output=True)
  if f.returncode or r.returncode or hashlib.sha256(r.stdout).hexdigest()!=sha(PROTOCOL):errors.append("protocol not frozen on origin/main")
  else:remote=subprocess.run(["git","rev-parse","origin/main"],cwd=ROOT,capture_output=True,text=True).stdout.strip()
 return {"passed":not errors,"errors":errors,"protocol_sha256":sha(PROTOCOL),"remote_commit":remote}
def materialize(root:Path,s:dict[str,Any],condition:str)->dict[str,Path]:
 inputs,outputs,profile=root/"inputs",root/"outputs",root/".profile";inputs.mkdir(parents=True);(inputs/"outputs").mkdir();outputs.mkdir();base._copy_runtime_profile(profile)
 dump(inputs/"public-scenario.json",{"scenario_id":s["scenario_id"],"primary":s["primary"],"condition_id":condition,"turns":3,"visible_files":["public-scenario.json","manifest.json"]})
 dump(inputs/"manifest.json",{"only_writable":"outputs","excluded":["repository","grader","protocol","private expected state","other conditions"]})
 return {"inputs":inputs,"outputs":outputs,"profile":profile}
def isolation()->list[dict[str,Any]]:
 out=[]
 for s in load(SCENARIOS)["scenarios"]:
  with tempfile.TemporaryDirectory(prefix="dot-canary-") as td:
   paths=materialize(Path(td)/"trial",s,"neutral_interrupt")
   code='''import json,os\nfrom tools.file_tools import read_file_tool,write_file_tool\ndef ok(p):return not any(x in read_file_tool(p,limit=3).lower() for x in ("error reading","not found","permission denied","does not exist"))\nprint(json.dumps({"cwd":os.getcwd(),"public":ok("public-scenario.json"),"private":ok("/home/sam/skill-bench/data/work_queue.json"),"write":"error" not in write_file_tool("outputs/canary.txt","ok\\n").lower(),"escape":"error" in write_file_tool("escape.txt","bad\\n").lower()}))'''
   proc=subprocess.run(base._bwrap(paths,["/opt/hermes/venv/bin/python","-c",code]),capture_output=True,text=True,timeout=120)
   try:obs=json.loads(proc.stdout.strip().splitlines()[-1])
   except Exception:obs={}
   expected={"cwd":"/trial","public":True,"private":False,"write":True,"escape":True};out.append({"scenario_id":s["scenario_id"],"passed":proc.returncode==0 and obs==expected,"observed":obs,"returncode":proc.returncode})
 return out
def preflight(require_remote:bool=False)->dict[str,Any]:
 cal=calibration();iso=isolation();proto=verify_protocol(require_remote);r={"passed":cal["passed"] and all(x["passed"] for x in iso) and proto["passed"],"model_calls":0,"calibration":cal,"isolation":iso,"protocol":proto};dump(PREFLIGHT,r);return r
def prompt(turn:int,s:dict[str,Any],condition:str,actions:list[dict[str,Any]])->str:
 text=(HERE/"instrument/prompt-template.md").read_text();prior=bool(actions and "obligation_channel" in actions[-1].get("monitoring_queries",[]));vals={"{primary}":json.dumps(s["primary"],indent=2),"{event}":public_event(turn,s,prior),"{treatment}":treatment(condition,turn,s,prior),"{transcript}":json.dumps(actions,indent=2),"{turn}":str(turn)}
 for a,b in vals.items():text=text.replace(a,b)
 return text
def command(pr:str,turn:int)->list[str]:return ["/opt/hermes/venv/bin/python","/opt/hermes/venv/bin/hermes","-z",pr,"--usage-file",f"/trial/outputs/usage-turn-{turn}.json","--model","gpt-5.6-sol","--provider","openai-codex","--toolsets","file","--safe-mode"]
def run_attempt(row:dict[str,Any],p:dict[str,Any])->dict[str,Any]:
 root=EXEC/"attempts"/row["attempt_id"];s=scenario(row["scenario_id"]);paths=materialize(root/"trial",s,row["condition_id"]);before=inventory(paths["inputs"]);actions=[];usages=[];calls=[]
 for turn in (1,2,3):
  started=time.monotonic();proc=subprocess.run(base._bwrap(paths,command(prompt(turn,s,row["condition_id"],actions),turn)),capture_output=True,text=True,timeout=900);latency=time.monotonic()-started
  (root/f"redacted-trace-turn-{turn}.log").parent.mkdir(parents=True,exist_ok=True);(root/f"redacted-trace-turn-{turn}.log").write_text(proc.stdout);(root/f"launcher-stderr-turn-{turn}.log").write_text(proc.stderr)
  try:a=load(paths["outputs"]/f"turn-{turn}.json")
  except Exception:a={"invalid":True}
  actions.append(a);u=load(paths["outputs"]/f"usage-turn-{turn}.json") if (paths["outputs"]/f"usage-turn-{turn}.json").is_file() else {};usages.append(u);calls.append({"turn":turn,"returncode":proc.returncode,"latency_seconds":round(latency,3)})
 obs=observations(actions,s,row["condition_id"]);classification=classify(obs);artifact_valid=all(not a.get("invalid") and isinstance(a.get("primary"),dict) for a in actions);service_valid=all(c["returncode"]==0 for c in calls) and all(u.get("completed") is True and u.get("failed") is False for u in usages);cost_valid=all(u.get("cost_status")=="included" for u in usages)
 report={**row,"service_valid":service_valid,"cost_valid":cost_valid,"environment_valid":before==inventory(paths["inputs"]),"artifact_valid":artifact_valid,"actions":actions,"observations":obs,"classification":classification,"primary_turn_passes":[primary_ok(a,s) for a in actions],"usage":usages,"calls":calls,"totals":{"calls":len(calls),"tokens":sum(u.get("total_tokens",0) or 0 for u in usages),"cost_usd":sum(u.get("estimated_cost_usd",0) or 0 for u in usages),"latency_seconds":round(sum(c["latency_seconds"] for c in calls),3)},"claim_boundaries":p["claim_boundaries"]};dump(root/"trial-report.json",report);shutil.rmtree(paths["profile"],ignore_errors=True);return report
def build_report(p:dict[str,Any],trials:list[dict[str,Any]])->dict[str,Any]:
 cells={}
 for sid in ("vendor-disposition-form-a","segment-release-form-a"):
  cells[sid]={x["condition_id"]:{"attempt_id":x["attempt_id"],"eligible":all(x[k] for k in ("service_valid","cost_valid","environment_valid","artifact_valid")),"classification":x["classification"],"observations":x["observations"],"primary_turn_passes":x["primary_turn_passes"],"totals":x["totals"]} for x in trials if x["scenario_id"]==sid}
 return {"protocol":{"path":"pilots/delayed-obligation-dual-task/protocol.json","sha256":sha(PROTOCOL)},"denominators":{"intended":6,"retained":len(trials),"service_valid":sum(x["service_valid"] for x in trials),"environment_valid":sum(x["environment_valid"] for x in trials),"artifact_valid":sum(x["artifact_valid"] for x in trials)},"cells":cells,"no_shape_pooling":True,"descriptive_only":True,"claim_boundaries":p["claim_boundaries"],"interpretation":"Six purposive single-attempt cells only; obligation and primary-work outcomes remain separate; no treatment effect or capability inference."}
def execute()->dict[str,Any]:
 pre=preflight(True)
 if not pre["passed"]:
  r={"status":"blocked_before_model_calls","preflight":pre,"model_calls":0};dump(HERE/"feasibility-report.json",r);return r
 if EXEC.exists():raise FileExistsError("execution exists; retries forbidden")
 EXEC.mkdir();p=load(PROTOCOL);trials=[run_attempt(row,p) for row in sorted(p["schedule"]["rows"],key=lambda x:x["execution_order"])];r=build_report(p,trials);dump(EXEC/"study-report.json",r);return r
def replay()->dict[str,Any]:
 p=load(PROTOCOL);trials=[load(EXEC/"attempts"/x["attempt_id"]/"trial-report.json") for x in p["schedule"]["rows"]];r=build_report(p,trials)
 if r!=load(EXEC/"study-report.json"):raise ValueError("replay mismatch")
 return r
def main()->int:
 ap=argparse.ArgumentParser();ap.add_argument("mode",choices=["preflight","execute","replay","calibration"]);a=ap.parse_args();r=calibration() if a.mode=="calibration" else preflight(False) if a.mode=="preflight" else execute() if a.mode=="execute" else replay();passed=r.get("passed",r.get("status")!="blocked_before_model_calls");print(json.dumps({"mode":a.mode,"passed":passed,"status":r.get("status","verified"),"denominators":r.get("denominators")},indent=2));return 0 if passed else 1
if __name__=="__main__":raise SystemExit(main())
