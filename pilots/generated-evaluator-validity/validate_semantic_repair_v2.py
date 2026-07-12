#!/usr/bin/env python3
"""Replay immutable parent and v2 descendant across seven frozen matrices."""
from __future__ import annotations
import hashlib, importlib.util, json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent; REPO=ROOT.parents[1]
CODE=ROOT/'semantic-repair-v2/evaluator.py'; ADAPTER=ROOT/'semantic-repair-v2/adapter.py'
PARENT=ROOT/'semantic-repair-report.json'; HOLDOUT=ROOT/'fifth-family-holdout-v1.json'; REPORT=ROOT/'semantic-repair-v2-report.json'
FORBIDDEN=('case_id','source_family','oracle','inc-204','invoice-export','sev-2','lh-adoption','ops-handoff','vendor-incident','multilingual-edge','experience-memory')
def load(p): return json.loads(p.read_text())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def run(payload):
 p=subprocess.run([sys.executable,'-I',str(CODE)],input=json.dumps(payload),text=True,capture_output=True,cwd=CODE.parent,timeout=5)
 try:return json.loads(p.stdout).get('outcome','execution_error') if p.returncode==0 else 'execution_error'
 except json.JSONDecodeError:return 'execution_error'
def matrix(name,cases,nested=False):
 rows=[]
 for c in cases:
  payload=c.get('observation',c.get('input'))
  expected=c['oracle']['outcome'] if nested else c['oracle']; observed=run(payload)
  rows.append({'case_id':c['case_id'],'expected':expected,'observed':observed,'pass':expected==observed})
 return {'name':name,'passed':sum(x['pass'] for x in rows),'total':len(rows),'results':rows}
def natural_cases():
 spec=importlib.util.spec_from_file_location('nat',ROOT/'natural_output_replay.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
 fixture=load(ROOT/'natural-output-cases-v1.json');base=mod.load_sources(fixture)
 return [{**c,'input':mod.adapt(mod.mutate(base,c['mutation']))} for c in fixture['cases']]
def validate_source(extra=''):
 text=(CODE.read_text()+ADAPTER.read_text()+extra).lower()
 return [word for word in FORBIDDEN if word in text]
def build():
 parent=load(PARENT); holdout=load(HOLDOUT); source=REPO/holdout['source_family']['path']
 matrices=[matrix('historical_transfer',load(ROOT/'transfer-cases.json')['cases'],True),matrix('adjudicated_adversarial',load(ROOT/'adjudication-cases-v2.json')['cases'],True),matrix('natural_output',natural_cases()),matrix('repair_holdout',load(ROOT/'repair-holdout-v1.json')['cases']),matrix('cross_domain',load(ROOT/'cross-domain-holdout-v1.json')['cases']),matrix('fourth_family_holdout',load(ROOT/'fourth-family-holdout-v1.json')['cases']),matrix('fifth_family_holdout',holdout['cases'])]
 parent_by={x['name']:x for x in parent['matrices']}
 deltas=[{'name':m['name'],'parent_passed':parent_by[m['name']]['passed'] if m['name'] in parent_by else None,'child_passed':m['passed'],'delta':m['passed']-parent_by[m['name']]['passed'] if m['name'] in parent_by else None} for m in matrices]
 forbidden=validate_source(); integrity=sha(source)==holdout['source_family']['sha256']
 gates={'implementation_identity_safe':not forbidden,'new_source_integrity':integrity,'new_holdout_exact':matrices[-1]['passed']==matrices[-1]['total'],'all_matrices_exact':all(m['passed']==m['total'] for m in matrices),'critical_safety':all(r['observed']=='unsafe_mutation_or_action' for m in matrices for r in m['results'] if r['expected']=='unsafe_mutation_or_action')}
 sensitivity={m['name']:all(o['passed']==o['total'] for o in matrices if o is not m) for m in matrices}
 return {'schema_version':'1.0','scope':'builder-authored evidence-view adapter calibration only','lineage':{'parent_report':str(PARENT.relative_to(REPO)),'parent_sha256':sha(PARENT),'parent_preserved':True,'child_adapter_sha256':sha(ADAPTER),'child_evaluator_sha256':sha(CODE)},'fresh_holdout':{'path':str(HOLDOUT.relative_to(REPO)),'sha256':sha(HOLDOUT),'source_integrity':integrity,'frozen_status':holdout['status'],'disjointness':holdout['source_family']['disjointness']},'implementation_forbidden_tokens':forbidden,'matrices':matrices,'parent_child_deltas':deltas,'regressions':[d for d in deltas if d['delta'] is not None and d['delta']<0],'gates':gates,'decision':'retain_local_calibration' if all(gates.values()) else 'reject','sensitivity_excluding_each_holdout':sensitivity,'claim_limits':['criterion equivalence','professional validity','general evaluator validity','agent capability','production fitness','deployment readiness']}
def main():
 report=build();REPORT.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'decision':report['decision'],'scores':{m['name']:f"{m['passed']}/{m['total']}" for m in report['matrices']},'regressions':report['regressions']},sort_keys=True));return 0 if all(report['gates'].values()) else 1
if __name__=='__main__':raise SystemExit(main())
