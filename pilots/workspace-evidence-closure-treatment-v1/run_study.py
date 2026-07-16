#!/usr/bin/env python3
"""Preflight, execute once, and replay the frozen workspace-closure treatment."""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, random, shutil, subprocess, tempfile, time
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2]; HERE=Path(__file__).resolve().parent
PROTOCOL=HERE/"protocol.json"; EXEC=HERE/"execution"; PREFLIGHT=HERE/"preflight-report.json"
BASE=ROOT/"pilots/configured-artifact-revision/launcher.py"; CAL=HERE/"instrument/calibration-cases.json"
def module(name:str,path:Path)->Any:
 spec=importlib.util.spec_from_file_location(name,path)
 if spec is None or spec.loader is None:raise RuntimeError(path)
 mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
base=module("workspace_treatment_base",BASE)
def load(p:Path)->Any:return json.loads(p.read_text(encoding="utf-8"))
def dump(p:Path,v:Any)->None:p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,indent=2,sort_keys=True)+"\n",encoding="utf-8")
def sha(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def inv(p:Path)->dict[str,Any]:return {x.relative_to(p).as_posix():{"sha256":sha(x),"bytes":x.stat().st_size} for x in sorted(p.rglob("*")) if x.is_file()}
def grade(shape:str,artifact:Any)->dict[str,Any]:
 if shape=="record":
  expected={"owner":"North team","deadline":"2026-08-15","budget_usd":12500,"decision":"conditional approval","caveat":"Approval is conditional on legal review."}
  passed={k:artifact.get(k)==v for k,v in expected.items()} if isinstance(artifact,dict) else {k:False for k in expected}
  retained=sum(passed[k] for k in ("owner","decision","caveat"));introduced=int(isinstance(artifact,dict) and artifact.get("owner") not in (None,"North team"))
 else:
  text=artifact if isinstance(artifact,str) else ""; requirements={"title":"delta migration handoff","contact":"priya shah","decision":"defer migration","evidence":"840 ms","threshold":"500 ms","caveat":"retest after index remediation before rescheduling"}
  low=text.lower();passed={k:v in low for k,v in requirements.items()};retained=sum(passed[k] for k in ("title","contact"));introduced=int("proceed" in low or "rollout is ready" in low)
 return {"artifact_complete":bool(artifact),"independent_correctness":all(passed.values()) and introduced==0,"obligation_coverage":{"passed":sum(passed.values()),"total":len(passed),"checks":passed},"predicate_satisfaction":all(passed.values()),"source_entailment":all(passed.values()) and introduced==0,"repair_retention":{"passed":retained,"total":3 if shape=="record" else 2},"newly_introduced_errors":introduced,"severe_defect":not all(passed.values()) or introduced>0}
def calibration()->dict[str,Any]:
 rows=[]
 for c in load(CAL)["cases"]:
  g=grade(c["shape"],c["artifact"]);e=c["expected"];ok=g["independent_correctness"]==e["correct"] and g["obligation_coverage"]["passed"]==e["obligations"] and g["repair_retention"]["passed"]==e["retained"] and g["newly_introduced_errors"]==e["introduced"];rows.append({"case_id":c["case_id"],"passed":ok,"observed":g})
 return {"passed":all(x["passed"] for x in rows),"model_calls":0,"cases":rows}
def verify_protocol(remote:bool)->dict[str,Any]:
 p=load(PROTOCOL);errors=[];rows=p["schedule"]
 if len(rows)!=8 or len({x["attempt_id"] for x in rows})!=8:errors.append("schedule must retain eight unique attempts")
 for s in ("record","memo"):
  for c in ("no_workspace","workspace"):
   if sum(x["shape"]==s and x["condition"]==c for x in rows)!=2:errors.append(f"missing two repeats: {s}/{c}")
 for x in p["frozen_components"]:
  q=ROOT/x["path"]
  if not q.is_file() or sha(q)!=x["sha256"]:errors.append("component drift: "+x["path"])
 pushed=None
 if remote:
  subprocess.run(["git","fetch","origin","main"],cwd=ROOT,capture_output=True)
  r=subprocess.run(["git","show","origin/main:pilots/workspace-evidence-closure-treatment-v1/protocol.json"],cwd=ROOT,capture_output=True)
  if r.returncode or hashlib.sha256(r.stdout).hexdigest()!=sha(PROTOCOL):errors.append("protocol bytes are not frozen on origin/main")
  else:pushed=subprocess.run(["git","rev-parse","origin/main"],cwd=ROOT,capture_output=True,text=True).stdout.strip()
 return {"passed":not errors,"errors":errors,"protocol_sha256":sha(PROTOCOL),"pushed_commit":pushed}
def materialize(root:Path,row:dict[str,Any])->dict[str,Path]:
 inputs,outputs,profile=root/"inputs",root/"outputs",root/".profile";(inputs/"sources").mkdir(parents=True);(inputs/"outputs").mkdir();outputs.mkdir();shape=HERE/"instrument"/row["shape"]
 shutil.copy2(shape/"task.md",inputs/"task.md")
 for p in (shape/"sources").iterdir():shutil.copy2(p,inputs/"sources"/p.name)
 if row["condition"]=="workspace":shutil.copy2(HERE/"instrument/public-guide.md",inputs/"public-guide.md")
 dump(inputs/"manifest.json",{"attempt_id":row["attempt_id"],"pair_nonce":row["pair_nonce"],"condition":row["condition"],"inputs":"read_only","only_writable":"outputs","excluded":["protocol","grader","private checks","other attempts","repository"]});base._copy_runtime_profile(profile);return {"inputs":inputs,"outputs":outputs,"profile":profile}
def canary(row:dict[str,Any])->dict[str,Any]:
 with tempfile.TemporaryDirectory(prefix="wec-canary-") as td:
  p=materialize(Path(td)/"trial",row);code='''import json,os\nfrom tools.file_tools import read_file_tool,write_file_tool\ndef ok(x):return not any(s in read_file_tool(x,limit=3).lower() for s in ("not found","permission denied","does not exist","error reading"))\nprint(json.dumps({"cwd":os.getcwd(),"task":ok("task.md"),"private":ok("/home/sam/skill-bench/data/work_queue.json"),"write":"error" not in write_file_tool("outputs/canary.txt","ok\\n").lower(),"escape":"error" in write_file_tool("escape.txt","bad\\n").lower()}))''';proc=subprocess.run(base._bwrap(p,["/opt/hermes/venv/bin/python","-c",code]),capture_output=True,text=True,timeout=120)
  try:o=json.loads(proc.stdout.strip().splitlines()[-1])
  except Exception:o={}
  return {"passed":proc.returncode==0 and o=={"cwd":"/trial","task":True,"private":False,"write":True,"escape":True},"observed":o,"model_calls":0}
def preflight(remote:bool=False)->dict[str,Any]:
 p=load(PROTOCOL);cal=calibration();cs=[canary(next(x for x in p["schedule"] if x["condition"]==c)) for c in ("no_workspace","workspace")];proto=verify_protocol(remote);probe=load(ROOT/"pilots/prospective-allocation-telemetry/v4/configured-provider-probe/probe-report.json");usage=load(ROOT/"pilots/prospective-allocation-telemetry/v4/configured-provider-probe/outputs/usage.json");service=probe.get("passed") is True and probe.get("model_calls")==1 and usage.get("completed") is True and usage.get("failed") is False and usage.get("estimated_cost_usd")==0.0
 r={"passed":cal["passed"] and all(x["passed"] for x in cs) and proto["passed"] and service,"model_calls":0,"calibration":cal,"isolation":cs,"protocol":proto,"retained_no_cost_provider_probe":{"passed":service,"report_sha256":sha(ROOT/"pilots/prospective-allocation-telemetry/v4/configured-provider-probe/probe-report.json")},"feedback_firewall":{"passed":all(x not in (HERE/"instrument/public-guide.md").read_text().lower() for x in ("12500","840 ms","defer migration","north team")),"private_checks_exposed":False}}
 r["passed"]&=r["feedback_firewall"]["passed"];dump(PREFLIGHT,r);return r
def prompt(row:dict[str,Any])->str:
 t=(HERE/"instrument"/row["shape"]/"task.md").read_text();extra="\nUse the assigned procedure in public-guide.md and produce both requested outputs." if row["condition"]=="workspace" else "\nNo workspace procedure is assigned. Produce the requested final artifact."
 return t+extra+f"\nPair nonce {row['pair_nonce']} is an attempt label only; do not include it in the artifact. Stop after writing outputs."
def artifact(paths:dict[str,Path],shape:str)->Any:
 p=paths["outputs"]/("allocation.json" if shape=="record" else "handoff.md")
 if not p.is_file():return None
 try:return load(p) if shape=="record" else p.read_text()
 except Exception:return None
def run_attempt(row:dict[str,Any],protocol:dict[str,Any])->dict[str,Any]:
 root=EXEC/"attempts"/row["attempt_id"];paths=materialize(root/"trial",row);before=inv(paths["inputs"]);started=time.monotonic();cmd=["/opt/hermes/venv/bin/python","/opt/hermes/venv/bin/hermes","-z",prompt(row),"--usage-file","/trial/outputs/usage.json","--model","gpt-5.6-sol","--provider","openai-codex","--toolsets","file","--safe-mode"];proc=subprocess.run(base._bwrap(paths,cmd),capture_output=True,text=True,timeout=900);lat=round(time.monotonic()-started,3);(root/"redacted-trace.log").parent.mkdir(parents=True,exist_ok=True);(root/"redacted-trace.log").write_text(proc.stdout);(root/"launcher-stderr.log").write_text(proc.stderr);u=load(paths["outputs"]/"usage.json") if (paths["outputs"]/"usage.json").is_file() else {};a=artifact(paths,row["shape"]);g=grade(row["shape"],a);service=proc.returncode==0 and u.get("completed") is True and u.get("failed") is False;environment=before==inv(paths["inputs"]);artpath=paths["outputs"]/("allocation.json" if row["shape"]=="record" else "handoff.md");digest=sha(artpath) if artpath.is_file() else None;wp=paths["outputs"]/"workspace.json";w=load(wp) if wp.is_file() else None;workspace_status={"applicable":row["condition"]=="workspace","record_closure":isinstance(w,dict) and all(k in w for k in ("obligations","checks","artifact_sha256","report_fresh","new_errors")),"execution_to_byte_lineage":isinstance(w,dict) and w.get("artifact_sha256")==digest,"report_freshness":isinstance(w,dict) and w.get("report_fresh") is True}
 eligible=service and environment and a is not None and u.get("cost_status")=="included" and u.get("estimated_cost_usd")==0.0
 r={**row,"validity":{"service":service,"environment":environment,"artifact":a is not None,"included_cost":u.get("cost_status")=="included" and u.get("estimated_cost_usd")==0.0,"eligible":eligible},"outcomes":g,"workspace_closure":workspace_status,"artifact_sha256":digest,"usage":{"api_calls":u.get("api_calls"),"input_tokens":u.get("input_tokens"),"output_tokens":u.get("output_tokens"),"reasoning_tokens":u.get("reasoning_tokens"),"total_tokens":u.get("total_tokens"),"estimated_cost_usd":u.get("estimated_cost_usd"),"cost_status":u.get("cost_status")},"latency_seconds":lat,"input_inventory":before,"output_inventory":inv(paths["outputs"]),"claim_boundaries":protocol["claim_boundaries"]};dump(root/"trial-report.json",r);shutil.rmtree(paths["profile"],ignore_errors=True);return r
def mean(xs:list[float])->float|None:return round(sum(xs)/len(xs),4) if xs else None
def report(p:dict[str,Any],trials:list[dict[str,Any]])->dict[str,Any]:
 shapes={}
 for shape in ("record","memo"):
  rows={}
  for cond in ("no_workspace","workspace"):
   xs=[x for x in trials if x["shape"]==shape and x["condition"]==cond];valid=[x for x in xs if x["validity"]["eligible"]];rows[cond]={"intended":2,"retained":len(xs),"eligible":len(valid),"completion":[x["outcomes"]["artifact_complete"] for x in xs],"independent_correctness":[x["outcomes"]["independent_correctness"] for x in valid],"obligation_coverage":[x["outcomes"]["obligation_coverage"] for x in valid],"predicate_satisfaction":[x["outcomes"]["predicate_satisfaction"] for x in valid],"source_entailment":[x["outcomes"]["source_entailment"] for x in valid],"workspace_closure":[x["workspace_closure"] for x in xs],"repair_retention":[x["outcomes"]["repair_retention"] for x in valid],"new_errors":[x["outcomes"]["newly_introduced_errors"] for x in valid],"severe_defects":[x["outcomes"]["severe_defect"] for x in valid],"latency_seconds":[x["latency_seconds"] for x in xs],"tokens":[x["usage"]["total_tokens"] for x in xs],"cost":[{"usd":x["usage"]["estimated_cost_usd"],"status":x["usage"]["cost_status"]} for x in xs],"attempt_ids":[x["attempt_id"] for x in xs]}
  pairs=[]
  for repeat in (1,2):
   a=next((x for x in trials if x["shape"]==shape and x["condition"]=="no_workspace" and x["repeat"]==repeat),None);b=next((x for x in trials if x["shape"]==shape and x["condition"]=="workspace" and x["repeat"]==repeat),None)
   pairs.append({"repeat":repeat,"eligible":bool(a and b and a["validity"]["eligible"] and b["validity"]["eligible"]),"correctness_difference":int(b["outcomes"]["independent_correctness"])-int(a["outcomes"]["independent_correctness"]) if a and b else None,"coverage_difference":b["outcomes"]["obligation_coverage"]["passed"]-a["outcomes"]["obligation_coverage"]["passed"] if a and b else None,"new_error_difference":b["outcomes"]["newly_introduced_errors"]-a["outcomes"]["newly_introduced_errors"] if a and b else None})
  eligible=[x for x in pairs if x["eligible"]];shapes[shape]={"cells":rows,"paired_effects":{"pairs":pairs,"mean_correctness_difference":mean([x["correctness_difference"] for x in eligible]),"mean_coverage_difference":mean([x["coverage_difference"] for x in eligible]),"mean_new_error_difference":mean([x["new_error_difference"] for x in eligible]),"clustered_uncertainty":"Two paired repeats in this purposive shape; exact pair differences are shown. No interval or population inference is warranted."}}
 return {"protocol":{"sha256":sha(PROTOCOL)},"denominators":{"intended":8,"retained":len(trials),"service_valid":sum(x["validity"]["service"] for x in trials),"eligible":sum(x["validity"]["eligible"] for x in trials),"service_invalid":sum(not x["validity"]["service"] for x in trials)},"shapes_reported_separately":shapes,"no_pooled_effect":True,"claim_boundaries":p["claim_boundaries"],"interpretation":"Prospectively frozen internal synthetic matched attempts only. Pair differences do not establish expertise transfer, universal workflow efficacy, professional validity, reliability, production fitness, or readiness."}
def execute()->dict[str,Any]:
 pre=preflight(True)
 if not pre["passed"]:return {"status":"blocked_before_model_calls","model_calls":0,"preflight":pre}
 if EXEC.exists():raise FileExistsError("execution exists; replacement and hidden retry forbidden")
 EXEC.mkdir();p=load(PROTOCOL);trials=[]
 for row in sorted(p["schedule"],key=lambda x:x["execution_order"]):trials.append(run_attempt(row,p))
 r=report(p,trials);dump(EXEC/"study-report.json",r);return r
def replay()->dict[str,Any]:
 p=load(PROTOCOL);trials=[load(EXEC/"attempts"/x["attempt_id"]/"trial-report.json") for x in p["schedule"]];r=report(p,trials)
 if r!=load(EXEC/"study-report.json"):raise ValueError("study report replay mismatch")
 return r
def main()->int:
 ap=argparse.ArgumentParser();ap.add_argument("mode",choices=("calibration","preflight","execute","replay"));a=ap.parse_args();r=calibration() if a.mode=="calibration" else preflight(False) if a.mode=="preflight" else execute() if a.mode=="execute" else replay();print(json.dumps({"mode":a.mode,"passed":r.get("passed",r.get("status")!="blocked_before_model_calls"),"status":r.get("status","verified"),"denominators":r.get("denominators")},indent=2));return 0 if r.get("passed",r.get("status")!="blocked_before_model_calls") else 1
if __name__=="__main__":raise SystemExit(main())
