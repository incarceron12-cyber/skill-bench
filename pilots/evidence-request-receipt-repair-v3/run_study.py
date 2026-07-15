#!/usr/bin/env python3
"""Conformance, prospective execution, and replay for receipt/repair pilot v3."""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,re,shutil,subprocess,tempfile,unicodedata
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
PROTOCOL=HERE/"protocol.json";EXEC=HERE/"execution";PREFLIGHT=HERE/"preflight"
V1=ROOT/"pilots/evidence-acquisition-matched-agent-v1";BASE_PATH=ROOT/"pilots/configured-artifact-revision/launcher.py"
SCENARIOS={"vendor-disposition":V1/"instrument/scenarios/compliance.json","segment-release":V1/"instrument/scenarios/analysis.json"}
def module(name:str,path:Path)->Any:
 spec=importlib.util.spec_from_file_location(name,path)
 if not spec or not spec.loader:raise RuntimeError(path)
 mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
base=module("err_base",BASE_PATH);grader=module("err_grader",HERE/"instrument/grader.py")
def load(p:Path)->Any:return json.loads(p.read_text())
def dump(p:Path,v:Any)->None:p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,indent=2,sort_keys=True)+"\n")
def sha(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def inventory(root:Path)->dict[str,Any]:return {p.relative_to(root).as_posix():{"sha256":sha(p),"bytes":p.stat().st_size} for p in sorted(root.rglob("*")) if p.is_file()}
def normalize(value:str)->str:
 value=unicodedata.normalize("NFKC",value).lower().replace("_"," ").replace("-"," ")
 return re.sub(r"\s+"," ",re.sub(r"[^\w\s]"," ",value)).strip()
def parse_request(raw:Any,scenario_id:str)->dict[str,Any]:
 if not isinstance(raw,str):return {"status":"parser_error","normalized_interpreted_topic":None,"mapped_evidence_ids":[]}
 text=normalize(raw);policy=load(HERE/"instrument/parser-policy.json");topics=policy["topics"][scenario_id]
 matched=[]
 for topic,triggers in topics.items():
  if any(normalize(t) in text for t in triggers):matched.append(topic)
 status="matched" if len(matched)==1 else "ambiguous" if matched else "unmatched"
 interpreted=matched[0] if status=="matched" else "multiple topics" if status=="ambiguous" else None
 private=policy["topic_to_private_evidence_id"][scenario_id]
 return {"status":status,"normalized_interpreted_topic":interpreted,"mapped_evidence_ids":[private[x] for x in matched]}
def receipt(parsed:dict[str,Any],repair_used:bool)->dict[str,Any]:
 return {"status":parsed["status"],"normalized_interpreted_topic":parsed["normalized_interpreted_topic"],"repair_eligible":parsed["status"] in {"ambiguous","unmatched","parser_error"} and not repair_used}
def conformance()->dict[str,Any]:
 checks=[]
 for case in load(HERE/"instrument/conformance-cases.json")["cases"]:
  obs=parse_request(case["request"],case["scenario_id"]);rcpt=receipt(obs,False)
  passed=obs["status"]==case["expected_status"] and obs["normalized_interpreted_topic"]==case["expected_topic"] and set(rcpt)=={"status","normalized_interpreted_topic","repair_eligible"}
  checks.append({**case,"observed":obs,"receipt":rcpt,"passed":passed})
 malformed=parse_request(["bad"],"vendor-disposition");checks.append({"kind":"malformed","observed":malformed,"receipt":receipt(malformed,False),"passed":malformed["status"]=="parser_error"})
 forbidden=set(load(HERE/"instrument/parser-policy.json")["receipt_forbidden"])
 firewall=all(not any(word in json.dumps(x["receipt"]).lower() for word in forbidden) for x in checks)
 mutation={"ambiguous_stays_ambiguous":parse_request("permit and insurance","vendor-disposition")["status"]=="ambiguous","cross_domain_stays_unmatched":parse_request("permit insurance","segment-release")["status"]=="unmatched","repair_budget_once":receipt(parse_request("unknown","vendor-disposition"),False)["repair_eligible"] and not receipt(parse_request("unknown","vendor-disposition"),True)["repair_eligible"]}
 return {"passed":all(x["passed"] for x in checks) and firewall and all(mutation.values()),"model_calls":0,"checks":checks,"receipt_firewall":firewall,"mutations":mutation}
def verify_protocol(require_pushed:bool)->dict[str,Any]:
 p=load(PROTOCOL);errors=[];rows=p["schedule"]["rows"]
 if len(rows)!=8 or len({x["attempt_id"] for x in rows})!=8:errors.append("schedule must contain eight unique attempts")
 for sid in SCENARIOS:
  for condition in ("natural_request","receipt_repair"):
   if sum(x["scenario_id"]==sid and x["condition_id"]==condition for x in rows)!=2:errors.append(f"missing repeats {sid}/{condition}")
 for item in p["frozen_components"]:
  path=ROOT/item["path"]
  if not path.is_file() or sha(path)!=item["sha256"]:errors.append(f"component drift {item['path']}")
 if any(p["claim_boundaries"].values()):errors.append("claim ceiling upgraded")
 pushed=None
 if require_pushed:
  fetch=subprocess.run(["git","fetch","origin","main"],cwd=ROOT,capture_output=True)
  if fetch.returncode:errors.append("git fetch failed")
  remote=subprocess.run(["git","show","origin/main:pilots/evidence-request-receipt-repair-v3/protocol.json"],cwd=ROOT,capture_output=True)
  if remote.returncode or hashlib.sha256(remote.stdout).hexdigest()!=sha(PROTOCOL):errors.append("protocol not frozen on origin/main")
  else:pushed=subprocess.run(["git","rev-parse","origin/main"],cwd=ROOT,capture_output=True,text=True).stdout.strip()
 return {"passed":not errors,"errors":errors,"protocol_sha256":sha(PROTOCOL),"pushed_commit":pushed}
def materialize(root:Path,scenario:dict[str,Any],condition:str)->dict[str,Path]:
 inputs,outputs,profile=root/"inputs",root/"outputs",root/".profile";(inputs/"outputs").mkdir(parents=True);outputs.mkdir();base._copy_runtime_profile(profile)
 dump(inputs/"public-scenario.json",{"scenario_id":scenario["scenario_id"],"target":scenario["target"],"public_context":scenario["public_context"]})
 dump(inputs/"manifest.json",{"condition_id":condition,"visible":["public-scenario.json","manifest.json"],"only_writable":"outputs","excluded":["evidence menu","answers","parser policy","grader","protocol","repository"]})
 return {"inputs":inputs,"outputs":outputs,"profile":profile}
def isolation_canary()->list[dict[str,Any]]:
 out=[]
 for sid,path in SCENARIOS.items():
  with tempfile.TemporaryDirectory(prefix="err-canary-") as td:
   paths=materialize(Path(td)/"trial",load(path),"receipt_repair")
   code=r'''import json,os
from tools.file_tools import read_file_tool,write_file_tool
def ok(p):return not any(x in read_file_tool(p,limit=3).lower() for x in ("error reading","not found","permission denied","does not exist"))
print(json.dumps({"cwd":os.getcwd(),"public":ok("public-scenario.json"),"private":ok("/home/sam/skill-bench/data/work_queue.json"),"write":"error" not in write_file_tool("outputs/canary.txt","ok\n").lower(),"escape":"error" in write_file_tool("escape.txt","bad\n").lower()}))'''
   proc=subprocess.run(base._bwrap(paths,["/opt/hermes/venv/bin/python","-c",code]),capture_output=True,text=True,timeout=120)
   try:obs=json.loads(proc.stdout.strip().splitlines()[-1])
   except Exception:obs={}
   passed=proc.returncode==0 and obs=={"cwd":"/trial","public":True,"private":False,"write":True,"escape":True}
   out.append({"scenario_id":sid,"passed":passed,"observed":obs,"returncode":proc.returncode})
 return out
def canary()->dict[str,Any]:
 conf=conformance();iso=isolation_canary();proto=verify_protocol(False);result={"passed":conf["passed"] and all(x["passed"] for x in iso) and proto["passed"],"model_calls":0,"conformance":conf,"isolation":iso,"protocol":proto};dump(PREFLIGHT/"canary-report.json",result);return result
def syntax(condition:str)->str:
 base_text='To request evidence: {"action":"request","raw_request":"natural-language request for one evidence topic","intent":"why it matters","requested_scope":"scope","expected_value_basis":"how it could change the decision"}.'
 if condition=="natural_request":return base_text+" Failed or ambiguous routing releases nothing; no interpretation receipt is returned."
 return base_text+' After a failed or ambiguous request, the environment may return one interpretation receipt. If repair_eligible is true, the next turn may use exactly once: {"action":"repair","raw_request":"rephrased request for one topic","intent":"why","requested_scope":"scope","expected_value_basis":"decision relevance"}. No candidate list is provided.'
def prompt_for(s:dict[str,Any],condition:str,transcript:list[dict[str,Any]],turn:int)->str:
 text=(HERE/"instrument/prompt-template.md").read_text()
 for a,b in {"{target}":s["target"],"{public_context}":s["public_context"],"{transcript}":json.dumps(transcript,indent=2),"{turn_file}":f"turn-{turn}.json","{request_syntax}":syntax(condition)}.items():text=text.replace(a,b)
 return text
def command(prompt:str,usage:str)->list[str]:return ["/opt/hermes/venv/bin/python","/opt/hermes/venv/bin/hermes","-z",prompt,"--usage-file",f"/trial/outputs/{usage}","--model","gpt-5.6-sol","--provider","openai-codex","--toolsets","file","--safe-mode"]
def release(parsed:dict[str,Any],rid:str,step:int,s:dict[str,Any],budget:float,charge:float,is_repair:bool)->tuple[dict[str,Any],float,dict[str,Any]|None]:
 budget=max(0,budget-charge)
 if parsed["status"]!="matched":return {"access_event_id":f"access-{step}","request_id":rid,"status":"ambiguous" if parsed["status"]=="ambiguous" else "failed","evidence_id":None,"content_locator":None,"reason":f"Parser status {parsed['status']}; no release."},budget,None
 eid=parsed["mapped_evidence_ids"][0];atom=next(x for x in s["evidence_atoms"] if x["evidence_id"]==eid)
 # A repair receives credit for the 0.5 already charged on the failed original request.
 budget=max(0,budget-atom["cost"]+(.5 if is_repair else 0.0))
 if atom["availability"]=="delayed":status="delayed";pending=atom
 elif atom["availability"] in {"restricted","unavailable"}:status="denied";pending=None
 else:status="released";pending=None
 return {"access_event_id":f"access-{step}","request_id":rid,"status":status,"evidence_id":eid,"content_locator":f"transcript.step-{step}.content" if status=="released" else None,"reason":"Frozen access policy."},budget,pending
def run_attempt(p:dict[str,Any],row:dict[str,Any])->dict[str,Any]:
 root=EXEC/"attempts"/row["attempt_id"];s=load(SCENARIOS[row["scenario_id"]]);condition=row["condition_id"];paths=materialize(root/"trial",s,condition);before=inventory(paths["inputs"])
 transcript=[];requests=[];receipts=[];repairs=[];events=[];budget=3.0;pending=None;repair_pending=False;repair_used=False;final={};procs=[]
 for turn in range(1,6):
  if pending:
   events.append({"access_event_id":f"access-{len(events)+1}-release","request_id":requests[-1]["request_id"],"status":"released","evidence_id":pending["evidence_id"],"content_locator":f"transcript.turn-{turn}.delayed-content","reason":"One-step delay elapsed."});transcript.append({"kind":"access","status":"released","evidence_id":pending["evidence_id"],"content":pending["content"],"remaining_budget":budget});pending=None
  proc=subprocess.run(base._bwrap(paths,command(prompt_for(s,condition,transcript,turn),f"usage-turn-{turn}.json")),capture_output=True,text=True,timeout=900);procs.append(proc);(root/f"redacted-trace-turn-{turn}.log").write_text(proc.stdout);(root/f"launcher-stderr-turn-{turn}.log").write_text(proc.stderr)
  try:action=load(paths["outputs"]/f"turn-{turn}.json")
  except Exception:action={"action":"invalid"}
  transcript.append({"kind":"agent_action","turn":turn,"action":action})
  if action.get("action")=="terminal":final=action;break
  is_repair=action.get("action")=="repair" and condition=="receipt_repair" and repair_pending and not repair_used
  rid=f"request-{len(requests)+1}";parsed=parse_request(action.get("raw_request"),s["scenario_id"]);record={"request_id":rid,"turn":turn,"kind":"repair" if is_repair else "request","raw_expression":str(action.get("raw_request",action)),"parser":{"parser_id":"parser.semantic-topic.v3",**parsed}}
  requests.append(record)
  if is_repair:repair_used=True;repair_pending=False;repairs.append({"request_id":rid,"from_receipt_id":receipts[-1]["receipt_id"]})
  elif repair_pending:repair_pending=False
  if condition=="receipt_repair":
   rc={"receipt_id":f"receipt-{len(receipts)+1}",**receipt(parsed,repair_used)};receipts.append(rc);transcript.append({"kind":"request_receipt",**rc})
   if rc["repair_eligible"]:repair_pending=True
  charge=0.0 if is_repair else (0.5 if parsed["status"]!="matched" else 0.0)
  ev,budget,pending=release(parsed,rid,len(events)+1,s,budget,charge,is_repair);events.append(ev);message={"kind":"access","status":ev["status"],"remaining_budget":budget}
  if ev["status"]=="released":message.update({"evidence_id":ev["evidence_id"],"content":next(x["content"] for x in s["evidence_atoms"] if x["evidence_id"]==ev["evidence_id"])})
  transcript.append(message)
 if not final:final={"action":"invalid","uncertainty":"No terminal artifact emitted."}
 usages=[load(paths["outputs"]/f"usage-turn-{i}.json") if (paths["outputs"]/f"usage-turn-{i}.json").is_file() else {} for i in range(1,len(procs)+1)]
 service=bool(procs) and all(x.returncode==0 for x in procs) and all(x.get("completed") is True and x.get("failed") is False for x in usages);cost_valid=all(x.get("cost_status")=="included" and x.get("estimated_cost_usd")==0.0 for x in usages);artifact_valid=final.get("action")=="terminal" and isinstance(final.get("evidence_ids"),list)
 released={x["evidence_id"] for x in events if x["status"]=="released"};grade=grader.grade(final,s,released,artifact_valid);dump(root/"grade.json",grade)
 report={**row,"service_valid":service,"cost_valid":cost_valid,"environment_valid":before==inventory(paths["inputs"]),"artifact_valid":artifact_valid,"requests":requests,"receipts":receipts,"repairs":repairs,"access_events":events,"released_ids":sorted(released),"adoption":{"kind":"terminal_citation_proxy_only","cited_released_ids":sorted(set(final.get("evidence_ids",[]))&released)},"final":final,"grade":grade,"usage":usages,"artifacts":inventory(paths["outputs"]),"claim_boundaries":p["claim_boundaries"]};dump(root/"trial-report.json",report);shutil.rmtree(paths["profile"],ignore_errors=True);return report
def metrics(t:dict[str,Any])->dict[str,Any]:return {"requests":len(t["requests"]),"matched":sum(x["parser"]["status"]=="matched" for x in t["requests"]),"ambiguous":sum(x["parser"]["status"]=="ambiguous" for x in t["requests"]),"unmatched":sum(x["parser"]["status"]=="unmatched" for x in t["requests"]),"receipts":len(t["receipts"]),"repairs":len(t["repairs"]),"released":len(t["released_ids"]),"adopted":len(t["adoption"]["cited_released_ids"]),"endpoint_quality":t["grade"]["endpoint_quality"],"decision_loss":t["grade"]["decision_loss"],"total_tokens":sum(x.get("total_tokens",0) or 0 for x in t["usage"])}
def report(p:dict[str,Any],trials:list[dict[str,Any]])->dict[str,Any]:
 cells={}
 for sid in SCENARIOS:
  cells[sid]={}
  for condition in ("natural_request","receipt_repair"):
   xs=sorted([x for x in trials if x["scenario_id"]==sid and x["condition_id"]==condition],key=lambda x:x["repeat"]);cells[sid][condition]={"intended":2,"eligible":sum(all(x[k] for k in ("service_valid","cost_valid","environment_valid","artifact_valid")) for x in xs),"attempt_ids":[x["attempt_id"] for x in xs],"decomposition":[metrics(x) for x in xs]}
 return {"protocol":{"path":"pilots/evidence-request-receipt-repair-v3/protocol.json","sha256":sha(PROTOCOL)},"denominators":{"intended":8,"service_valid":sum(x["service_valid"] for x in trials),"environment_valid":sum(x["environment_valid"] for x in trials),"artifact_valid":sum(x["artifact_valid"] for x in trials)},"cells":cells,"no_shape_pooling":True,"descriptive_only":True,"claim_boundaries":p["claim_boundaries"],"interpretation":"Exact purposive synthetic observations only; request, receipt, repair, access, citation proxy, stop, endpoint, and cost remain separate."}
def execute()->dict[str,Any]:
 pre=canary();verified=verify_protocol(True)
 if not pre["passed"] or not verified["passed"]:
  result={"status":"blocked_before_model_calls","preflight":pre,"protocol":verified,"model_calls":0};dump(HERE/"feasibility-report.json",result);return result
 if EXEC.exists():raise FileExistsError("execution exists; retries forbidden")
 EXEC.mkdir();p=load(PROTOCOL);trials=[run_attempt(p,x) for x in p["schedule"]["rows"]];result=report(p,trials);dump(EXEC/"study-report.json",result);return result
def replay()->dict[str,Any]:
 p=load(PROTOCOL);trials=[load(EXEC/"attempts"/x["attempt_id"]/"trial-report.json") for x in p["schedule"]["rows"]];rebuilt=report(p,trials)
 if rebuilt!=load(EXEC/"study-report.json"):raise ValueError("replay mismatch")
 return rebuilt
def main()->int:
 ap=argparse.ArgumentParser();ap.add_argument("mode",choices=["preflight","execute","replay"]);a=ap.parse_args();result=canary() if a.mode=="preflight" else execute() if a.mode=="execute" else replay();passed=result.get("passed",result.get("status")!="blocked_before_model_calls");print(json.dumps({"mode":a.mode,"passed":passed,"status":result.get("status","verified"),"denominators":result.get("denominators")},indent=2));return 0 if passed else 1
if __name__=="__main__":raise SystemExit(main())
