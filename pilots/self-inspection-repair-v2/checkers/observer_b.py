#!/usr/bin/env python3
"""Observer B: independent line/token projection; deliberately has no condition input."""
from __future__ import annotations
import re

def evaluate(family, candidate, view_status="available", transform_status="pinned"):
    if view_status != "available" or transform_status != "pinned": return {"terminal_state":"insufficient_evidence","endpoint":None,"collateral":None,"observer":"b"}
    try:
        if family=="roster":
            lines=[x.strip() for x in candidate.strip().splitlines()];
            if lines[0]!="worker,day,hours" or len(lines)<2: raise ValueError()
            cells=[x.split(",") for x in lines[1:]]
            if any(len(x)!=3 or not x[2].isdigit() for x in cells): raise ValueError()
            names={x[0] for x in cells}; by_day={d:{x[0] for x in cells if x[1]==d and int(x[2])>0} for d in ("Monday","Tuesday")}; by_name={n:sum(int(x[2]) for x in cells if x[0]==n) for n in names}
            endpoint=min(map(len,by_day.values()))>=2 and max(by_name.values())<=16; collateral=names=={"Alice","Bob","Cara"}
        elif family=="service":
            pairs={m.group(1):m.group(2) for m in re.finditer(r"(?m)^([a-z_]+)=([^\n]+)$",candidate)}
            if set(pairs)!={"service_name","endpoint","tls_min","timeout_seconds","audit_enabled"}: raise ValueError()
            endpoint=pairs["tls_min"]=="1.3" and int(pairs["timeout_seconds"])<=30 and pairs["audit_enabled"].lower()=="true"; collateral=(pairs["service_name"],pairs["endpoint"])==("ledger","/v1/post")
        elif family=="workflow":
            if not candidate.lstrip().startswith("<svg") or not candidate.rstrip().endswith("</svg>"): raise ValueError()
            wm=re.search(r"viewBox=['\"]\S+\s+\S+\s+([0-9.]+)",candidate); tm=re.search(r"<title>(.*?)</title>",candidate)
            if wm is None or tm is None: raise ValueError()
            nodes=set(re.findall(r"<g id=['\"]([^'\"]+)['\"]",candidate)); edges=set(re.findall(r"data-edge=['\"]([^'\"]+)['\"]",candidate))
            endpoint=float(wm.group(1))<=600 and {"intake->review","review->approve"}<=edges; collateral=tm.group(1)=="Release review" and nodes=={"intake","review","approve"}
        else: raise ValueError()
    except Exception: return {"terminal_state":"invalid_artifact","endpoint":None,"collateral":None,"observer":"b"}
    return {"terminal_state":"passed" if endpoint and collateral else "criterion_fail","endpoint":endpoint,"collateral":collateral,"observer":"b"}
