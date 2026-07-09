#!/usr/bin/env python3
"""Create a research digest scaffold from discovered papers.

This is deliberately not a substitute for the LLM reading step. It surfaces
metadata and extracted-text paths so the cron agent can read the actual papers
and write thoughtful synthesis.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "data" / "papers" / "index.json"
REPORTS = ROOT / "reports" / "daily"


def load_index():
    if not INDEX.exists():
        raise SystemExit("No paper index found. Run scripts/discover_papers.py first.")
    return json.loads(INDEX.read_text())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=12)
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    idx = load_index()
    papers = list(idx.get("papers", {}).values())
    papers.sort(key=lambda p: p.get("published") or p.get("updated") or "", reverse=True)
    selected = papers[: args.limit]
    today = dt.datetime.utcnow().strftime("%Y-%m-%d")

    lines = [
        f"# Daily Research Digest Scaffold — {today}",
        "",
        "This scaffold lists papers discovered/downloaded by the local pipeline. The human-facing cron summary should read the extracted text paths and synthesize insights, not merely restate abstracts.",
        "",
        "## Candidate papers",
        "",
    ]
    for i, p in enumerate(selected, 1):
        lines += [
            f"### {i}. {p.get('title','Untitled')}",
            "",
            f"- ID: `{p.get('id')}`",
            f"- URL: {p.get('url')}`" if False else f"- URL: {p.get('url')}",
            f"- Published: {p.get('published','')[:10]}",
            f"- Authors: {', '.join(p.get('authors', [])[:8])}",
            f"- Categories: {', '.join(p.get('categories', []))}",
            f"- PDF: `{p.get('pdf_path','not downloaded')}`",
            f"- Extracted text: `{p.get('text_path','not extracted')}` ({p.get('text_chars','?')} chars)",
            "",
            "**Abstract:** " + (p.get("summary", "")[:1200]),
            "",
            "**Skill-bench reading prompts:**",
            "- What is the unique evaluation/design insight?",
            "- What methodology can be adapted into artifact-centered benchmark design?",
            "- What domain-knowledge primitives does it imply?",
            "- What should be added to the taxonomy or pilot scenarios?",
            "",
        ]
    text = "\n".join(lines)
    if args.write:
        REPORTS.mkdir(parents=True, exist_ok=True)
        path = REPORTS / f"{today}-scaffold.md"
        path.write_text(text)
        print(path.relative_to(ROOT))
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
