#!/usr/bin/env python3
"""Observer A: native parser based; deliberately has no condition input."""
from __future__ import annotations
import configparser, csv, io, re, xml.etree.ElementTree as ET

def evaluate(family, candidate, view_status="available", transform_status="pinned"):
    if view_status != "available" or transform_status != "pinned": return {"terminal_state":"insufficient_evidence","endpoint":None,"collateral":None,"observer":"a"}
    try:
        if family=="roster":
            rows=list(csv.DictReader(io.StringIO(candidate))); required={"worker","day","hours"}
            if not rows or set(rows[0])!=required: raise ValueError()
            workers={r["worker"] for r in rows}; totals={w:sum(int(r["hours"]) for r in rows if r["worker"]==w) for w in workers}; coverage={d:len({r["worker"] for r in rows if r["day"]==d and int(r["hours"])>0}) for d in ("Monday","Tuesday")}
            endpoint=all(v>=2 for v in coverage.values()) and all(v<=16 for v in totals.values()); collateral=workers=={"Alice","Bob","Cara"}
        elif family=="service":
            cfg=configparser.ConfigParser(); cfg.read_string(candidate); s=cfg["service"]
            endpoint=s["tls_min"]=="1.3" and int(s["timeout_seconds"])<=30 and s.getboolean("audit_enabled"); collateral=s["service_name"]=="ledger" and s["endpoint"]=="/v1/post"
        elif family=="workflow":
            root=ET.fromstring(candidate); width=float(root.attrib["viewBox"].split()[2]); title=next((x.text for x in root if x.tag.endswith("title")),None); nodes={x.attrib["id"] for x in root.iter() if "id" in x.attrib}; edges={x.attrib["data-edge"] for x in root.iter() if "data-edge" in x.attrib}
            endpoint=width<=600 and {"intake->review","review->approve"}<=edges; collateral=title=="Release review" and nodes=={"intake","review","approve"}
        else: raise ValueError()
    except Exception: return {"terminal_state":"invalid_artifact","endpoint":None,"collateral":None,"observer":"a"}
    return {"terminal_state":"passed" if endpoint and collateral else "criterion_fail","endpoint":endpoint,"collateral":collateral,"observer":"a"}
