#!/usr/bin/env python3
"""Preflight, execute once, and replay the prospective request-interface study."""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, re, shutil, subprocess, tempfile, unicodedata
from pathlib import Path
from typing import Any

ROOT=Path(__file__).resolve().parents[2]; HERE=Path(__file__).resolve().parent
PROTOCOL=HERE/"protocol.json"; EXEC=HERE/"execution"; PREFLIGHT=HERE/"preflight"
V1=ROOT/"pilots/evidence-acquisition-matched-agent-v1"
BASE_PATH=ROOT/"pilots/configured-artifact-revision/launcher.py"
SCENARIO_PATHS={"vendor-disposition":V1/"instrument/scenarios/compliance.json","segment-release":V1/"instrument/scenarios/analysis.json"}

def module(name:str,path:Path)->Any:
    spec=importlib.util.spec_from_file_location(name,path)
    if spec is None or spec.loader is None: raise RuntimeError(f"cannot import {path}")
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod
base=module("eri_base",BASE_PATH); grader=module("eri_grader",HERE/"instrument/grader.py")
def load(p:Path)->Any:return json.loads(p.read_text())
def dump(p:Path,v:Any)->None:p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,indent=2,sort_keys=True)+"\n")
def sha(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def inventory(root:Path)->dict[str,Any]:return {p.relative_to(root).as_posix():{"sha256":sha(p),"bytes":p.stat().st_size} for p in sorted(root.rglob("*")) if p.is_file()}
def git(*args:str)->subprocess.CompletedProcess:return subprocess.run(["git",*args],cwd=ROOT,capture_output=True,text=True)

def normalize_topic(value:str)->str:
    value=unicodedata.normalize("NFKC",value).lower().replace("_"," ").replace("-"," ")
    return re.sub(r"\s+"," ",value).strip()

def parse_request(action:dict[str,Any],scenario:dict[str,Any],interface:str)->dict[str,Any]:
    if interface=="natural_request":
        raw=action.get("raw_request")
        if not isinstance(raw,str): return {"status":"parser_error","mapped_evidence_ids":[],"interpreted_scope":"malformed natural request","confidence":None}
        text=raw.lower(); mapped=[a["evidence_id"] for a in scenario["evidence_atoms"] if any(alias in text for alias in a["aliases"])]
    else:
        topic=action.get("request_topic")
        if not isinstance(topic,str): return {"status":"parser_error","mapped_evidence_ids":[],"interpreted_scope":"malformed structured request","confidence":None}
        policy=load(HERE/"instrument/parser-policy.json")["structured_synonyms"][scenario["scenario_id"]]; normalized=normalize_topic(topic)
        mapped=[eid for eid,synonyms in policy.items() if normalized in {normalize_topic(x) for x in synonyms}]
    status="matched" if len(mapped)==1 else "ambiguous" if mapped else "unmatched"
    return {"status":status,"mapped_evidence_ids":mapped,"interpreted_scope":str(action.get("requested_scope") or action.get("request_topic") or action.get("raw_request")),"confidence":1.0 if status=="matched" else .5 if status=="ambiguous" else 0.0}

def verify_protocol(require_pushed:bool)->dict[str,Any]:
    p=load(PROTOCOL); errors=[]; rows=p["schedule"]["rows"]
    if len(rows)!=8 or len({r["attempt_id"] for r in rows})!=8:errors.append("schedule must have eight unique attempts")
    for sid in SCENARIO_PATHS:
        for interface in ("natural_request","structured_request"):
            if sum(r["scenario_id"]==sid and r["interface_id"]==interface for r in rows)!=2:errors.append(f"two repeats missing {sid}/{interface}")
    for item in p["frozen_components"]:
        path=ROOT/item["path"]
        if not path.is_file() or sha(path)!=item["sha256"]:errors.append(f"component drift {item['path']}")
    if any(p["claim_boundaries"].values()):errors.append("claim ceiling upgraded")
    pushed=None
    if require_pushed:
        fetch=git("fetch","origin","main")
        if fetch.returncode: errors.append("git fetch failed")
        remote=subprocess.run(["git","show","origin/main:pilots/evidence-request-interface-v2/protocol.json"],cwd=ROOT,capture_output=True)
        if remote.returncode or hashlib.sha256(remote.stdout).hexdigest()!=sha(PROTOCOL):errors.append("protocol bytes not frozen on origin/main")
        else:pushed=git("rev-parse","origin/main").stdout.strip()
    return {"passed":not errors,"errors":errors,"protocol_sha256":sha(PROTOCOL),"pushed_commit":pushed,"component_count":len(p["frozen_components"])}

def materialize(root:Path,scenario:dict[str,Any],interface:str)->dict[str,Path]:
    if root.exists():raise FileExistsError(root)
    inputs,outputs,profile=root/"inputs",root/"outputs",root/".profile"
    (inputs/"outputs").mkdir(parents=True);outputs.mkdir();base._copy_runtime_profile(profile)
    public={"scenario_id":scenario["scenario_id"],"target":scenario["target"],"public_context":scenario["public_context"]}
    dump(inputs/"public-scenario.json",public);dump(inputs/"manifest.json",{"interface_id":interface,"inputs":"read_only","only_writable":"outputs","visible":["public-scenario.json","manifest.json"],"excluded":["answers","evidence menu","grader","parser policy","protocol","repository","other attempts"]})
    return {"inputs":inputs,"outputs":outputs,"profile":profile}

def parser_canaries()->dict[str,Any]:
    checks=[]
    for sid,path in SCENARIO_PATHS.items():
        scenario=load(path); policy=load(HERE/"instrument/parser-policy.json")["structured_synonyms"][sid]
        for eid,synonyms in policy.items():
            for synonym in synonyms:
                obs=parse_request({"request_topic":synonym},scenario,"structured_request")
                checks.append({"scenario_id":sid,"case":"exact_synonym","input":synonym,"expected":eid,"observed":obs,"passed":obs["status"]=="matched" and obs["mapped_evidence_ids"]==[eid]})
        for negative in ("", "all evidence", "unknown topic", "permit insurance audit"):
            obs=parse_request({"request_topic":negative},scenario,"structured_request")
            checks.append({"scenario_id":sid,"case":"negative_control","input":negative,"expected":"unmatched","observed":obs,"passed":obs["status"]=="unmatched" and not obs["mapped_evidence_ids"]})
        malformed=parse_request({"request_topic":["not","a","string"]},scenario,"structured_request")
        checks.append({"scenario_id":sid,"case":"malformed","expected":"parser_error","observed":malformed,"passed":malformed["status"]=="parser_error"})
    return {"passed":all(x["passed"] for x in checks),"model_calls":0,"checks":checks}

def canary()->dict[str,Any]:
    isolation=[]
    for sid,path in SCENARIO_PATHS.items():
        with tempfile.TemporaryDirectory(prefix="eri-canary-") as td:
            paths=materialize(Path(td)/"trial",load(path),"structured_request")
            private=["/home/sam/skill-bench/data/work_queue.json","protocol.json","grader.py","parser-policy.json","answers.json"]
            code="PRIVATE="+repr(private)+"\n"+r'''import json,os
from tools.file_tools import read_file_tool,search_tool,write_file_tool
def readable(p):
 t=read_file_tool(p,limit=5).lower();return not any(x in t for x in ("error reading","not found","permission denied","does not exist"))
o={"cwd":os.getcwd(),"visible":{p:readable(p) for p in ["public-scenario.json","manifest.json"]},"private_denied":{p:not readable(p) for p in PRIVATE},"repo_search":search_tool("skill-bench",target="files",path="/home/sam",limit=10)}
o["write_output"]="error" not in write_file_tool("outputs/canary.txt","ok\n").lower();o["escape_denied"]="error" in write_file_tool("escape.txt","bad\n").lower();print(json.dumps(o))'''
            proc=subprocess.run(base._bwrap(paths,["/opt/hermes/venv/bin/python","-c",code]),capture_output=True,text=True,timeout=120)
            try:obs=json.loads(proc.stdout.strip().splitlines()[-1])
            except Exception:obs={}
            passed=proc.returncode==0 and obs.get("cwd")=="/trial" and all(obs.get("visible",{}).values()) and all(obs.get("private_denied",{}).values()) and "skill-bench" not in str(obs.get("repo_search","")) and obs.get("write_output") is True and obs.get("escape_denied") is True
            isolation.append({"scenario_id":sid,"passed":passed,"model_calls":0,"observed":obs,"returncode":proc.returncode,"stderr":proc.stderr[-1000:]})
    template=(HERE/"instrument/prompt-template.md").read_text(); firewall={"passed":all(x not in template for x in ["correct_decision","severe_required_ids","endpoint_quality"]),"model_calls":0}
    parsers=parser_canaries(); protocol=verify_protocol(False)
    result={"passed":all(x["passed"] for x in isolation) and firewall["passed"] and parsers["passed"] and protocol["passed"],"model_calls":0,"isolation":isolation,"feedback_firewall":firewall,"parser_conformance":parsers,"protocol":protocol}
    dump(PREFLIGHT/"canary-report.json",result);return result

def request_syntax(interface:str)->str:
    if interface=="natural_request":return 'To request evidence, use: {"action":"request","raw_request":"natural-language request for one evidence item","intent":"why it matters","requested_scope":"scope","expected_value_basis":"how it could change the decision"}'
    return 'To request evidence, use: {"action":"request","request_topic":"one concise evidence topic, not multiple topics","intent":"why it matters","requested_scope":"scope","expected_value_basis":"how it could change the decision"}. No menu or valid topic list is provided; malformed, combined, or unknown topics fail closed.'
def prompt_for(s:dict[str,Any],interface:str,transcript:list[dict[str,Any]],turn:int)->str:
    text=(HERE/"instrument/prompt-template.md").read_text()
    for old,new in {"{target}":s["target"],"{public_context}":s["public_context"],"{transcript}":json.dumps(transcript,indent=2),"{turn_file}":f"turn-{turn}.json","{request_syntax}":request_syntax(interface)}.items():text=text.replace(old,new)
    return text
def command(prompt:str,usage_name:str)->list[str]:return ["/opt/hermes/venv/bin/python","/opt/hermes/venv/bin/hermes","-z",prompt,"--usage-file",f"/trial/outputs/{usage_name}","--model","gpt-5.6-sol","--provider","openai-codex","--toolsets","file","--safe-mode"]

def access(parsed:dict[str,Any],rid:str,step:int,s:dict[str,Any],budget:float)->tuple[dict[str,Any],float,dict[str,Any]|None]:
    if parsed["status"]!="matched":
        status="ambiguous" if parsed["status"]=="ambiguous" else "failed"
        return {"access_event_id":f"access-{step}","step":step,"request_id":rid,"evidence_id":None,"status":status,"content_locator":None,"observer_id":"environment.synthetic.v2","transformation":"none","reason":f"Parser status {parsed['status']}; no evidence released."},max(0,budget-.5),None
    eid=parsed["mapped_evidence_ids"][0];atom=next(a for a in s["evidence_atoms"] if a["evidence_id"]==eid);budget=max(0,budget-atom["cost"])
    if atom["availability"] in {"restricted","unavailable"}:status="denied";pending=None;reason=f"{atom['availability'].title()} evidence denied under frozen policy."
    elif atom["availability"]=="delayed":status="delayed";pending=atom;reason="Evidence queued for one-step delayed release."
    else:status="released";pending=None;reason="Matched admissible evidence released."
    return {"access_event_id":f"access-{step}","step":step,"request_id":rid,"evidence_id":eid,"status":status,"content_locator":f"transcript.step-{step}.content" if status=="released" else None,"observer_id":"environment.synthetic.v2","transformation":"none","reason":reason},budget,pending

def run_attempt(p:dict[str,Any],row:dict[str,Any])->dict[str,Any]:
    root=EXEC/"attempts"/row["attempt_id"];s=load(SCENARIO_PATHS[row["scenario_id"]]);interface=row["interface_id"];paths=materialize(root/"trial",s,interface);before=inventory(paths["inputs"])
    transcript=[];requests=[];events=[];budget=3.0;pending=None;final={};procs=[]
    for turn in range(1,5):
        if pending is not None:
            ev={"access_event_id":f"access-{len(events)+1}-release","step":len(requests)+1,"request_id":requests[-1]["request_id"],"evidence_id":pending["evidence_id"],"status":"released","content_locator":f"transcript.turn-{turn}.delayed-content","observer_id":"environment.synthetic.v2","transformation":"none","reason":"Frozen one-step delay elapsed."};events.append(ev);transcript.append({"kind":"access","status":"released","evidence_id":pending["evidence_id"],"content":pending["content"],"remaining_budget":budget});pending=None
        out=paths["outputs"]/f"turn-{turn}.json";usage=f"usage-turn-{turn}.json";proc=subprocess.run(base._bwrap(paths,command(prompt_for(s,interface,transcript,turn),usage)),capture_output=True,text=True,timeout=900);procs.append(proc)
        (root/f"redacted-trace-turn-{turn}.log").write_text(proc.stdout);(root/f"launcher-stderr-turn-{turn}.log").write_text(proc.stderr)
        try:action=load(out)
        except Exception:action={"action":"invalid","raw_output_locator":f"trial/outputs/turn-{turn}.json"}
        transcript.append({"kind":"agent_action","turn":turn,"action":action})
        if action.get("action")=="terminal":final=action;break
        rid=f"request-{len(requests)+1}";parsed=parse_request(action,s,interface);raw=action.get("raw_request",action.get("request_topic",action))
        req={"request_id":rid,"step":len(requests)+1,"interface_id":interface,"raw_expression":str(raw),"intent":str(action.get("intent","Unparseable request intent.")),"requested_scope":str(action.get("requested_scope","Unspecified scope.")),"expected_value_basis":str(action.get("expected_value_basis","No valid expected-value basis emitted.")),"parser_interpretation":{"parser_id":"parser.deterministic-keyword.v1-replay" if interface=="natural_request" else "parser.exact-topic.v2",**parsed,"evidence_locator":f"trial/outputs/turn-{turn}.json"}};requests.append(req)
        ev,budget,pending=access(parsed,rid,req["step"],s,budget);events.append(ev);message={"kind":"access","status":ev["status"],"evidence_id":ev["evidence_id"],"remaining_budget":budget}
        if ev["status"]=="released":message["content"]=next(a["content"] for a in s["evidence_atoms"] if a["evidence_id"]==ev["evidence_id"])
        transcript.append(message)
        if budget<=0:transcript.append({"kind":"budget_state","message":"Budget exhausted; terminal action required.","remaining_budget":0})
    if not final:final={"action":"invalid","uncertainty":"No terminal artifact emitted."}
    usages=[load(paths["outputs"]/f"usage-turn-{n}.json") if (paths["outputs"]/f"usage-turn-{n}.json").is_file() else {} for n in range(1,len(procs)+1)]
    service=bool(procs) and all(x.returncode==0 for x in procs) and all(u.get("completed") is True and u.get("failed") is False for u in usages);cost_valid=all(u.get("cost_status")=="included" and u.get("estimated_cost_usd")==0.0 for u in usages);artifact_valid=final.get("action")=="terminal" and isinstance(final.get("evidence_ids"),list)
    released={e["evidence_id"] for e in events if e["status"]=="released"};grade=grader.grade(final,s,released,artifact_valid);dump(root/"grade.json",grade)
    report={**row,"launcher_invocations":len(procs),"returncodes":[x.returncode for x in procs],"service_valid":service,"cost_valid":cost_valid,"environment_valid":before==inventory(paths["inputs"]),"artifact_valid":artifact_valid,"requests":requests,"access_events":events,"released_ids":sorted(released),"adoption":{"kind":"terminal_citation_proxy_only","cited_released_ids":sorted(set(final.get("evidence_ids",[]))&released)},"final":final,"grade":grade,"usage":usages,"artifacts":inventory(paths["outputs"]),"claim_boundaries":p["claim_boundaries"]};dump(root/"trial-report.json",report);shutil.rmtree(paths["profile"],ignore_errors=True);return report

def metrics(t:dict[str,Any])->dict[str,Any]:
    return {"selected":len(t["requests"]),"expressed_validly":sum(r["parser_interpretation"]["status"]!="parser_error" for r in t["requests"]),"parser_matched":sum(r["parser_interpretation"]["status"]=="matched" for r in t["requests"]),"parser_ambiguous":sum(r["parser_interpretation"]["status"]=="ambiguous" for r in t["requests"]),"access_released":len(t["released_ids"]),"adopted_by_terminal_citation_proxy":len(t["adoption"]["cited_released_ids"]),"endpoint_quality":t["grade"]["endpoint_quality"],"decision_loss":t["grade"]["decision_loss"],"severe_omissions":len(t["grade"]["severe_omissions"]),"total_tokens":sum(u.get("total_tokens",0) or 0 for u in t["usage"])}
def report(p:dict[str,Any],trials:list[dict[str,Any]])->dict[str,Any]:
    cells={};pairs=[]
    for sid in SCENARIO_PATHS:
        cells[sid]={}
        for interface in ("natural_request","structured_request"):
            xs=sorted([t for t in trials if t["scenario_id"]==sid and t["interface_id"]==interface],key=lambda x:x["repeat"]);cells[sid][interface]={"intended":2,"eligible":sum(t["service_valid"] and t["cost_valid"] and t["environment_valid"] and t["artifact_valid"] for t in xs),"attempt_ids":[t["attempt_id"] for t in xs],"decomposition":[metrics(t) for t in xs]}
        for repeat in (1,2):
            n=next(t for t in trials if t["scenario_id"]==sid and t["interface_id"]=="natural_request" and t["repeat"]==repeat);s=next(t for t in trials if t["scenario_id"]==sid and t["interface_id"]=="structured_request" and t["repeat"]==repeat);mn,ms=metrics(n),metrics(s)
            pairs.append({"scenario_id":sid,"repeat":repeat,"natural_attempt_id":n["attempt_id"],"structured_attempt_id":s["attempt_id"],"eligible":all(t["service_valid"] and t["cost_valid"] and t["environment_valid"] and t["artifact_valid"] for t in (n,s)),"structured_minus_natural":{k:ms[k]-mn[k] for k in mn}})
    return {"protocol":{"path":"pilots/evidence-request-interface-v2/protocol.json","sha256":sha(PROTOCOL)},"v1_audit":{"path":"pilots/evidence-request-interface-v2/v1-root-surface-audit.json","sha256":sha(HERE/"v1-root-surface-audit.json")},"denominators":{"intended":8,"service_valid":sum(t["service_valid"] for t in trials),"environment_valid":sum(t["environment_valid"] for t in trials),"artifact_valid":sum(t["artifact_valid"] for t in trials)},"cells":cells,"paired_descriptive_contrasts":pairs,"no_pooled_effect":True,"adoption_measure":"terminal citation proxy only","claim_boundaries":p["claim_boundaries"],"interpretation":"Exact internal request-interface observations only; n=2 purposive repeats per cell. Selection, expression, parser, access, citation proxy, stopping, and endpoint are reported separately."}
def execute()->dict[str,Any]:
    pre=canary();verified=verify_protocol(True)
    if not pre["passed"] or not verified["passed"]:
        result={"status":"blocked_before_model_calls","preflight":pre,"protocol":verified,"model_calls":0};dump(HERE/"feasibility-report.json",result);return result
    if EXEC.exists():raise FileExistsError("execution exists; retries forbidden")
    EXEC.mkdir();p=load(PROTOCOL);trials=[run_attempt(p,row) for row in p["schedule"]["rows"]];result=report(p,trials);dump(EXEC/"study-report.json",result);return result
def replay()->dict[str,Any]:
    p=load(PROTOCOL);trials=[load(EXEC/"attempts"/r["attempt_id"]/"trial-report.json") for r in p["schedule"]["rows"]];rebuilt=report(p,trials)
    if rebuilt!=load(EXEC/"study-report.json"):raise ValueError("study report replay mismatch")
    return rebuilt
def main()->int:
    ap=argparse.ArgumentParser();ap.add_argument("mode",choices=["preflight","execute","replay"]);args=ap.parse_args();result=canary() if args.mode=="preflight" else execute() if args.mode=="execute" else replay();passed=result.get("passed",result.get("status")!="blocked_before_model_calls");print(json.dumps({"mode":args.mode,"status":result.get("status","verified"),"passed":passed,"denominators":result.get("denominators")},indent=2));return 0 if passed else 1
if __name__=="__main__":raise SystemExit(main())
