#!/usr/bin/env python3
"""Gate, execute once, and replay the frozen repeated task-family matrix."""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, math, shutil, subprocess, tempfile
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[3]; HERE=Path(__file__).resolve().parent
PROTOCOL=HERE/"protocol.json"; EXEC=HERE/"execution"; PREFLIGHT=HERE/"preflight"
BASE=ROOT/"pilots/configured-artifact-revision/launcher.py"

def module(name: str, path: Path) -> Any:
 s=importlib.util.spec_from_file_location(name,path)
 if s is None or s.loader is None: raise RuntimeError(f"cannot import {path}")
 m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
base=module("matrix_base",BASE); grader=module("matrix_grader",HERE/"grade.py")
def load(p): return json.loads(p.read_text(encoding="utf-8"))
def dump(p,v): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(v,indent=2,sort_keys=True)+"\n",encoding="utf-8")
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def inv(root): return {p.relative_to(root).as_posix():{"sha256":sha(p),"bytes":p.stat().st_size} for p in sorted(root.rglob("*")) if p.is_file()}

def verify_protocol(protocol, require_pushed=False):
 errors=[]
 if len(protocol.get("forms",{}))!=4: errors.append("exactly four forms required")
 rows=protocol.get("schedule",{}).get("rows",[])
 if len(rows)!=8 or len({r["attempt_id"] for r in rows})!=8: errors.append("eight unique attempts required")
 for key in protocol.get("forms",{}):
  if sum(r["family"]+"/"+r["form"]==key for r in rows)!=2: errors.append(f"two repeats required: {key}")
 for c in protocol.get("frozen_components",[]):
  p=HERE/c["path"]
  if not p.is_file() or sha(p)!=c["sha256"]: errors.append(f"component drift: {c['path']}")
 if any(protocol.get("claim_boundaries",{}).values()): errors.append("claim ceiling upgraded")
 pushed=None
 if require_pushed:
  fetch=subprocess.run(["git","fetch","origin","main"],cwd=ROOT,capture_output=True,text=True)
  if fetch.returncode: errors.append("git fetch origin/main failed")
  remote=subprocess.run(["git","show","origin/main:pilots/repeated-task-family-matrix/v1/protocol.json"],cwd=ROOT,capture_output=True)
  if remote.returncode or hashlib.sha256(remote.stdout).hexdigest()!=sha(PROTOCOL): errors.append("frozen protocol bytes are not on origin/main")
  else: pushed=subprocess.run(["git","rev-parse","origin/main"],cwd=ROOT,capture_output=True,text=True).stdout.strip()
 return {"passed":not errors,"errors":errors,"protocol_sha256":sha(PROTOCOL),"component_count":len(protocol["frozen_components"]),"pushed_commit":pushed}

def materialize(root,key):
 if root.exists(): raise FileExistsError(root)
 inputs=root/"inputs"; outputs=root/"outputs"; profile=root/".profile"; inputs.mkdir(parents=True); (inputs/"outputs").mkdir(); outputs.mkdir()
 form=HERE/"forms"/key
 shutil.copy2(form/"public-task.md",inputs/"public-task.md"); shutil.copy2(form/"source.json",inputs/"source.json")
 dump(inputs/"manifest.json",{"form":key,"inputs":"read_only","only_writable":"outputs","agent_toolsets":["file"],"private_roles_excluded":["protocol","private_expected","task_health","grader","preflight","other_attempts","repository"]})
 base._copy_runtime_profile(profile)
 return {"inputs":inputs,"outputs":outputs,"profile":profile}

def isolation_canary(key):
 with tempfile.TemporaryDirectory(prefix="matrix-canary-") as td:
  paths=materialize(Path(td)/"trial",key)
  code=r'''import json,os
from tools.file_tools import read_file_tool,search_tool,write_file_tool
def ok(p):
 t=read_file_tool(p,limit=3).lower(); return not any(x in t for x in ("error reading","not found","permission denied","does not exist"))
private=["private-expected.json","task-health.json","protocol.json","grade.py","/home/sam/skill-bench/data/work_queue.json"]
o={"cwd":os.getcwd(),"public":{p:ok(p) for p in ["public-task.md","source.json","manifest.json"]},"private_denied":{p:not ok(p) for p in private},"write_output":"error" not in write_file_tool("outputs/canary.txt","ok\n").lower(),"escape_denied":"error" in write_file_tool("escape.txt","bad\n").lower(),"repository_search":search_tool("skill-bench",target="files",path="/home/sam",limit=10)}
print(json.dumps(o,sort_keys=True))'''
  proc=subprocess.run(base._bwrap(paths,["/opt/hermes/venv/bin/python","-c",code]),capture_output=True,text=True,timeout=120)
  try: obs=json.loads(proc.stdout.strip().splitlines()[-1])
  except Exception: obs={}
  passed=proc.returncode==0 and obs.get("cwd")=="/trial" and all(obs.get("public",{}).values()) and all(obs.get("private_denied",{}).values()) and obs.get("write_output") is True and obs.get("escape_denied") is True and "skill-bench" not in str(obs.get("repository_search",""))
  return {"form":key,"passed":passed,"model_calls":0,"observed":obs,"returncode":proc.returncode,"stderr":proc.stderr[-1000:]}

def calibration(protocol):
 rows=[]; passed=True
 for key,spec in protocol["forms"].items():
  exp=load(HERE/spec["authoritative_output"])
  with tempfile.TemporaryDirectory() as td:
   p=Path(td)/"report.json"
   positive={"decision":exp["decision"],"action":exp["action"],"evidence_ids":exp["evidence_ids"],"rationale":"The other record is superseded or untrusted by authority."}
   cases={"positive":positive,"wrong_decision":positive|{"decision":"wrong"},"wrong_evidence":positive|{"evidence_ids":["UNTRUSTED"]},"invalid":None,"alternative_valid":positive|{"rationale":"Authority makes the current record controlling; the informal or superseded conflict is excluded."}}
   results={}
   for name,value in cases.items():
    if value is None: p.write_text("not json",encoding="utf-8")
    else: dump(p,value)
    g=grader.grade(p,exp); results[name]=g["classification"]
   ok=results=={"positive":"pass","wrong_decision":"fail","wrong_evidence":"fail","invalid":"fail","alternative_valid":"pass"}; passed &= ok
   rows.append({"form":key,"passed":ok,"results":results})
 return {"kind":"deterministic_grader_calibration_and_mutation","passed":passed,"model_calls":0,"cases":rows,"mutation_requirement":"decision and evidence mutations must each flip pass to fail"}

def provider_gate():
 candidates=[]
 for p in ROOT.glob("pilots/**/usage.json"):
  try: v=load(p)
  except Exception: continue
  if v.get("provider")=="openai-codex" and v.get("model")=="gpt-5.6-sol" and v.get("completed") is True and v.get("failed") is False and v.get("cost_status")=="included" and v.get("estimated_cost_usd")==0.0: candidates.append((p.stat().st_mtime,p,v))
 if not candidates: return {"passed":False,"reason":"no retained exact-provider included-cost availability witness","model_calls":0}
 _,p,v=max(candidates)
 return {"passed":True,"kind":"historical_service_availability_and_included_zero_cost_canary","model_calls":0,"evidence_path":p.relative_to(ROOT).as_posix(),"evidence_sha256":sha(p),"provider":v["provider"],"model":v["model"],"cost_status":v["cost_status"],"estimated_cost_usd":v["estimated_cost_usd"],"boundary":"Historical pre-call feasibility only; each declared attempt retains its own service and cost result."}

def preflight(require_pushed):
 protocol=load(PROTOCOL); pv=verify_protocol(protocol,require_pushed); iso=[isolation_canary(k) for k in protocol["forms"]]; cal=calibration(protocol); provider=provider_gate()
 report={"kind":"repeated_matrix_pre_call_gates","model_calls":0,"protocol":pv,"isolation_and_leakage":iso,"grader_calibration_and_mutation":cal,"service_and_cost":provider}
 report["passed"]=pv["passed"] and all(x["passed"] for x in iso) and cal["passed"] and provider["passed"]
 dump(PREFLIGHT/"gate-report.json",report); return report

def trial_cmd(prompt): return ["/opt/hermes/venv/bin/python","/opt/hermes/venv/bin/hermes","-z",prompt,"--usage-file","/trial/outputs/usage.json","--model","gpt-5.6-sol","--provider","openai-codex","--toolsets","file","--safe-mode"]
def run_attempt(protocol,row):
 root=EXEC/"attempts"/row["attempt_id"]; key=row["family"]+"/"+row["form"]; paths=materialize(root/"trial",key); before=inv(paths["inputs"])
 prompt=(paths["inputs"]/"public-task.md").read_text()+"\nWork only from source.json and write the required output under outputs/."
 proc=subprocess.run(base._bwrap(paths,trial_cmd(prompt)),capture_output=True,text=True,timeout=900)
 (root/"redacted-trace.log").write_text(proc.stdout,encoding="utf-8"); (root/"launcher-stderr.log").write_text(proc.stderr,encoding="utf-8")
 after=inv(paths["inputs"]); changed=before!=after; usage=load(paths["outputs"]/"usage.json") if (paths["outputs"]/"usage.json").is_file() else {}
 report_path=paths["outputs"]/"report.json"; service=proc.returncode==0 and usage.get("completed") is True and usage.get("failed") is False; cost=usage.get("cost_status")=="included" and usage.get("estimated_cost_usd")==0.0
 valid=service and cost and not changed and report_path.is_file(); grade=grader.grade(report_path,load(HERE/protocol["forms"][key]["authoritative_output"])) if valid else None
 if grade: dump(root/"grade.json",grade)
 conf={"status":"insufficient_evidence","reason":"Pinned provider usage/trace emitted no declared token-logprob or calibrated-confidence channel"}
 trial={"attempt_id":row["attempt_id"],"execution_order":row["execution_order"],"family":row["family"],"form":row["form"],"repeat":row["repeat"],"launcher_invocations":1,"service_available":service,"cost_gate_passed":cost,"valid_trial":valid,"returncode":proc.returncode,"input_integrity":not changed,"usage":usage,"grade":grade,"confidence_channel":conf,"artifacts":inv(paths["outputs"]),"claim_boundaries":protocol["claim_boundaries"]}
 dump(root/"trial-report.json",trial); shutil.rmtree(paths["profile"],ignore_errors=True); return trial

def wilson(k,n,z=1.95996398454):
 if not n:return None
 p=k/n; d=1+z*z/n; c=(p+z*z/(2*n))/d; h=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/d; return [round(max(0,c-h),6),round(min(1,c+h),6)]
def build_report(protocol):
 trials=[load(EXEC/"attempts"/r["attempt_id"]/"trial-report.json") if (EXEC/"attempts"/r["attempt_id"]/"trial-report.json").is_file() else {**r,"status":"unstarted","service_available":False,"valid_trial":False,"grade":None} for r in protocol["schedule"]["rows"]]
 valid=[t for t in trials if t["valid_trial"]]; service=sum(t["service_available"] for t in trials); passes=sum(t.get("grade",{}).get("classification")=="pass" for t in valid)
 forms={}
 for key in protocol["forms"]:
  fam,form=key.split("/"); xs=[t for t in trials if t["family"]==fam and t["form"]==form]; vx=[t for t in xs if t["valid_trial"]]
  forms[key]={"declared":2,"service_available":sum(t["service_available"] for t in xs),"valid":len(vx),"pass_outcomes":sum(t.get("grade",{}).get("classification")=="pass" for t in vx),"repeat_agreement":len(vx)==2 and vx[0]["grade"]["classification"]==vx[1]["grade"]["classification"]}
 severity={s:{"passed":0,"failed":0} for s in ("critical","major","minor")}
 for t in valid:
  for o in t["grade"]["observations"]: severity[o["severity"]]["passed" if o["passed"] else "failed"]+=1
 families={f:{"forms":2,"declared":sum(t["family"]==f for t in trials),"valid":sum(t["family"]==f and t["valid_trial"] for t in trials),"form_pass_rates":[forms[k]["pass_outcomes"]/forms[k]["valid"] if forms[k]["valid"] else None for k in forms if k.startswith(f+"/")]} for f in ("evidence","incident")}
 return {"schema_version":"0.1.0","report_id":"repeated-task-family-matrix-v1","protocol":{"path":PROTOCOL.relative_to(ROOT).as_posix(),"sha256":sha(PROTOCOL)},"declared_attempts":8,"service_availability":{"successes":service,"denominator":8,"rate":service/8,"wilson_95":wilson(service,8)},"trial_validity":{"successes":len(valid),"denominator":8,"rate":len(valid)/8,"wilson_95":wilson(len(valid),8)},"criterion_outcome":{"passes":passes,"denominator_valid_trials":len(valid),"rate":passes/len(valid) if valid else None,"wilson_95":wilson(passes,len(valid))},"severity_outcomes":severity,"within_form":forms,"between_family_descriptive":families,"attempt_rows":trials,"confidence_channel":{"status":"insufficient_evidence","coverage":0,"denominator":8},"claim_boundaries":protocol["claim_boundaries"],"interpretation":"Internal four-form/two-family configured-system repeat evidence only; purposive builder-authored forms and small clustered denominators prohibit skill, professional/expert validity, general capability, safety, production, readiness, confidence-policy, or transport claims."}
def execute():
 gate=preflight(True)
 if not gate["passed"]:
  dump(HERE/"feasibility-report.json",{"status":"blocked_before_model_calls","gate_report":str((PREFLIGHT/"gate-report.json").relative_to(ROOT)),"failed_gates":gate,"model_calls":0}); return {"status":"blocked","model_calls":0}
 if EXEC.exists(): raise FileExistsError("execution exists; retries/replacements forbidden")
 EXEC.mkdir(); protocol=load(PROTOCOL)
 for row in protocol["schedule"]["rows"]:
  run_attempt(protocol,row)
 report=build_report(protocol); dump(EXEC/"study-report.json",report); return report
def replay():
 protocol=load(PROTOCOL); report=build_report(protocol); retained=load(EXEC/"study-report.json")
 if report!=retained: raise ValueError("replay mismatch")
 return report
def main():
 p=argparse.ArgumentParser(); p.add_argument("mode",choices=["preflight","execute","replay"]); p.add_argument("--require-pushed",action="store_true"); a=p.parse_args()
 result=preflight(a.require_pushed) if a.mode=="preflight" else execute() if a.mode=="execute" else replay()
 print(json.dumps({"mode":a.mode,"passed":result.get("passed",True),"declared_attempts":result.get("declared_attempts"),"status":result.get("status","verified")},indent=2)); return 0 if result.get("passed",True) else 1
if __name__=="__main__": raise SystemExit(main())
