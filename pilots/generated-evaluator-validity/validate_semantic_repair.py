#!/usr/bin/env python3
"""Replay a domain-neutral evaluator repair over all frozen matrices."""
from __future__ import annotations
import hashlib, importlib.util, json, re, subprocess, sys
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parent; REPO=ROOT.parents[1]
CODE=ROOT/'semantic-repair/evaluator.py'; ADAPTER=ROOT/'semantic-repair/adapter.py'
CONTRACT=ROOT/'criterion-observation-contract-v1.json'; FOURTH=ROOT/'fourth-family-holdout-v1.json'
REPORT=ROOT/'semantic-repair-report.json'
FORBIDDEN=('inc-204','invoice-export','sev-2','lh-adoption','ops-handoff','proc-handoff','vendor-incident','lh-skill-adoption','handoff-usability','multilingual-edge')
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(payload):
 p=subprocess.run([sys.executable,'-I',str(CODE)],input=json.dumps(payload),text=True,capture_output=True,cwd=CODE.parent,timeout=5)
 try:return json.loads(p.stdout).get('outcome','execution_error') if p.returncode==0 else 'execution_error'
 except json.JSONDecodeError:return 'execution_error'
def matrix(name,cases,nested=False):
 rows=[]
 for c in cases:
  payload=c['observation'] if 'observation' in c else c['input']
  expected=c['oracle']['outcome'] if nested else c['oracle'];observed=run(payload)
  rows.append({'case_id':c['case_id'],'expected':expected,'observed':observed,'pass':expected==observed})
 return {'name':name,'passed':sum(r['pass'] for r in rows),'total':len(rows),'results':rows}
def natural_cases():
 spec=importlib.util.spec_from_file_location('nat',ROOT/'natural_output_replay.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
 fixture=load(ROOT/'natural-output-cases-v1.json');base=mod.load_sources(fixture)
 return [{**c,'input':mod.adapt(mod.mutate(base,c['mutation']))} for c in fixture['cases']]
def validate_source(extra_text=''):
 text=(CODE.read_text()+ADAPTER.read_text()+extra_text).lower()
 return [token for token in FORBIDDEN if token in text]
def build():
 fourth=load(FOURTH);source=REPO/fourth['source_family']['path']
 matrices=[matrix('historical_transfer',load(ROOT/'transfer-cases.json')['cases'],True),matrix('adjudicated_adversarial',load(ROOT/'adjudication-cases-v2.json')['cases'],True),matrix('natural_output',natural_cases()),matrix('repair_holdout',load(ROOT/'repair-holdout-v1.json')['cases']),matrix('cross_domain',load(ROOT/'cross-domain-holdout-v1.json')['cases']),matrix('fourth_family_holdout',fourth['cases'])]
 forbidden=validate_source();integrity=sha(source)==fourth['source_family']['sha256']
 gates={'domain_literal_free':not forbidden,'fourth_source_integrity':integrity,'all_matrices_exact':all(m['passed']==m['total'] for m in matrices),'critical_safety':all(r['observed']=='unsafe_mutation_or_action' for m in matrices for r in m['results'] if r['expected']=='unsafe_mutation_or_action')}
 sensitivity={m['name']:all(other['passed']==other['total'] for other in matrices if other is not m) for m in matrices}
 return {'schema_version':'1.0','scope':'builder-authored criterion-semantic repair calibration only','components':{'contract':{'path':str(CONTRACT.relative_to(REPO)),'sha256':sha(CONTRACT)},'adapter':{'path':str(ADAPTER.relative_to(REPO)),'sha256':sha(ADAPTER)},'evaluator':{'path':str(CODE.relative_to(REPO)),'sha256':sha(CODE)},'fourth_holdout':{'path':str(FOURTH.relative_to(REPO)),'sha256':sha(FOURTH),'source_sha256_verified':integrity}},'adapter_conformance':{'families':['stateful_workflow','decision_artifact','typed_handoff'],'forbidden_literals_found':forbidden},'matrices':matrices,'gates':gates,'decision':'retain_local_calibration' if all(gates.values()) else 'reject','sensitivity_excluding_each_matrix':sensitivity,'claim_limits':load(CONTRACT)['claim_limits']}
def main():
 report=build();REPORT.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'decision':report['decision'],'scores':{m['name']:f"{m['passed']}/{m['total']}" for m in report['matrices']}},sort_keys=True));return 0 if all(report['gates'].values()) else 1
if __name__=='__main__':raise SystemExit(main())
