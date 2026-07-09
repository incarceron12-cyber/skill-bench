#!/usr/bin/env python3
"""Discover, download, and lightly index papers for skill-bench.

No API keys are required. The script uses arXiv Atom search and Semantic Scholar
when available. It downloads PDFs for arXiv papers and extracts text using
`pdftotext` when installed, otherwise it stores metadata and the PDF path.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "papers"
PDF_DIR = DATA / "pdfs"
TEXT_DIR = DATA / "text"
INDEX = DATA / "index.json"
CONFIG = ROOT / "scripts" / "config.json"

ARXIV_NS = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}


def slugify(s: str, n: int = 80) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s.lower()).strip("-")
    return s[:n].strip("-") or "paper"


def load_json(path: Path, default):
    if path.exists():
        return json.loads(path.read_text())
    return default


def save_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")


def fetch(url: str, timeout: int = 45) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "skill-bench/0.1"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def parse_arxiv_entries(xml: str, discovered_via: str) -> list[dict]:
    root = ET.fromstring(xml)
    out = []
    for e in root.findall("a:entry", ARXIV_NS):
        abs_url = e.findtext("a:id", default="", namespaces=ARXIV_NS)
        arxiv_id = abs_url.rsplit("/abs/", 1)[-1]
        title = " ".join((e.findtext("a:title", default="", namespaces=ARXIV_NS) or "").split())
        summary = " ".join((e.findtext("a:summary", default="", namespaces=ARXIV_NS) or "").split())
        authors = [a.findtext("a:name", default="", namespaces=ARXIV_NS) for a in e.findall("a:author", ARXIV_NS)]
        cats = [c.attrib.get("term", "") for c in e.findall("a:category", ARXIV_NS)]
        published = e.findtext("a:published", default="", namespaces=ARXIV_NS)
        updated = e.findtext("a:updated", default="", namespaces=ARXIV_NS)
        out.append({
            "id": "arxiv:" + arxiv_id,
            "arxiv_id": arxiv_id,
            "title": title,
            "authors": authors,
            "summary": summary,
            "categories": cats,
            "published": published,
            "updated": updated,
            "url": f"https://arxiv.org/abs/{arxiv_id}",
            "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}",
            "source": "arxiv",
            "discovered_via": discovered_via,
        })
    return out


def arxiv_search(query: str, max_results: int) -> list[dict]:
    # arXiv's search syntax is finicky. Search terms are routed through all:,
    # while quoted/AND-heavy query strings are kept intact where possible.
    if any(op in query for op in ['"', ' AND ', ' OR ', 'ANDNOT']):
        raw = query.replace(' ', '+')
    else:
        raw = "all:" + query.replace(" ", "+")
    q = urllib.parse.quote(raw, safe=":+\"")
    url = (
        "https://export.arxiv.org/api/query?"
        f"search_query={q}&sortBy=submittedDate&sortOrder=descending&max_results={max_results}"
    )
    xml = fetch(url).decode("utf-8", errors="replace")
    return parse_arxiv_entries(xml, query)


def arxiv_by_ids(ids: list[str]) -> list[dict]:
    if not ids:
        return []
    url = "https://export.arxiv.org/api/query?id_list=" + urllib.parse.quote(",".join(ids))
    xml = fetch(url).decode("utf-8", errors="replace")
    return parse_arxiv_entries(xml, "seed_arxiv_ids")


def extract_pdf_text(pdf_path: Path, text_path: Path) -> bool:
    text_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        subprocess.run(["pdftotext", "-layout", str(pdf_path), str(text_path)], check=True, timeout=120)
        return text_path.exists() and text_path.stat().st_size > 100
    except Exception:
        return False


def download_pdf(paper: dict) -> dict:
    if "pdf_url" not in paper:
        return paper
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    TEXT_DIR.mkdir(parents=True, exist_ok=True)
    aid = paper.get("arxiv_id", paper["id"]).replace("/", "_")
    stem = f"{aid}-{slugify(paper['title'], 50)}"
    pdf_path = PDF_DIR / f"{stem}.pdf"
    text_path = TEXT_DIR / f"{stem}.txt"
    if not pdf_path.exists():
        try:
            pdf_path.write_bytes(fetch(paper["pdf_url"], timeout=90))
            time.sleep(3)  # be gentle to arXiv
        except Exception as exc:
            paper["download_error"] = str(exc)
            return paper
    paper["pdf_path"] = str(pdf_path.relative_to(ROOT))
    paper["pdf_sha256"] = hashlib.sha256(pdf_path.read_bytes()).hexdigest()
    if not text_path.exists():
        extract_pdf_text(pdf_path, text_path)
    if text_path.exists():
        paper["text_path"] = str(text_path.relative_to(ROOT))
        paper["text_chars"] = text_path.stat().st_size
    return paper


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default=str(CONFIG))
    ap.add_argument("--max-results", type=int, default=None)
    ap.add_argument("--no-download", action="store_true")
    args = ap.parse_args()

    cfg = load_json(Path(args.config), {})
    queries = cfg.get("queries", [])
    max_results = args.max_results or int(cfg.get("max_results_per_query", 5))
    download = bool(cfg.get("download_pdfs", True)) and not args.no_download

    DATA.mkdir(parents=True, exist_ok=True)
    index = load_json(INDEX, {"papers": {}, "runs": []})
    before = set(index["papers"].keys())
    discovered = []

    # Curated seed IDs keep foundational/known-relevant papers in the corpus even
    # when keyword search drifts toward irrelevant fresh arXiv results.
    seed_ids = cfg.get("seed_arxiv_ids", [])
    if seed_ids:
        try:
            for p in arxiv_by_ids(seed_ids):
                if download:
                    p = download_pdf(p)
                old = index["papers"].get(p["id"], {})
                old.update(p)
                old.setdefault("review_status", "unreviewed")
                old["last_seen"] = dt.datetime.utcnow().isoformat() + "Z"
                index["papers"][p["id"]] = old
                discovered.append(p["id"])
        except Exception as exc:
            print(f"WARN seed id lookup failed: {exc}", file=sys.stderr)
        time.sleep(3)

    for q in queries:
        try:
            papers = arxiv_search(q, max_results)
        except Exception as exc:
            print(f"WARN query failed: {q}: {exc}", file=sys.stderr)
            continue
        for p in papers:
            if download:
                p = download_pdf(p)
            old = index["papers"].get(p["id"], {})
            old.update(p)
            old.setdefault("review_status", "unreviewed")
            old["last_seen"] = dt.datetime.utcnow().isoformat() + "Z"
            index["papers"][p["id"]] = old
            discovered.append(p["id"])
        time.sleep(3)

    after = set(index["papers"].keys())
    new_ids = sorted(after - before)
    index["runs"].append({
        "timestamp": dt.datetime.utcnow().isoformat() + "Z",
        "queries": queries,
        "discovered_count": len(discovered),
        "new_count": len(new_ids),
        "new_ids": new_ids,
    })
    save_json(INDEX, index)

    print(json.dumps({
        "status": "ok",
        "total_papers": len(index["papers"]),
        "new_count": len(new_ids),
        "new_ids": new_ids[:20],
        "index": str(INDEX.relative_to(ROOT)),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
