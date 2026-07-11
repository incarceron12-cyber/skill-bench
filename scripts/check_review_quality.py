#!/usr/bin/env python3
"""Check that skill-bench paper reviews meet the evidence standard."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REQUIRED_SECTIONS = {
    "contribution": [r"^##\s+One-sentence contribution", r"^##\s+One sentence contribution"],
    "relevance": [r"^##\s+Why this matters", r"^##\s+Relevance"],
    "methodology": [r"^##\s+Methodology"],
    "unique_insight": [r"^##\s+Unique insight"],
    "transfer": [r"^##\s+Transferable", r"^##\s+Transfer"],
    "limitations": [r"^##\s+Failure modes", r"^##\s+Limitations"],
    "actions": [r"^##\s+Action items", r"^##\s+Concrete changes", r"^##\s+Concrete repository"],
}

NON_REVIEW_FILES = {"readme.md", "topic-index.md"}


def review_files(path: Path):
    if path.is_file():
        return [path]
    return sorted(p for p in path.rglob("*.md") if p.name.lower() not in NON_REVIEW_FILES)


def check(path: Path) -> list[str]:
    text = path.read_text(errors="replace")
    issues = []
    for name, patterns in REQUIRED_SECTIONS.items():
        if not any(re.search(pattern, text, flags=re.I | re.M) for pattern in patterns):
            issues.append(f"missing section: {name}")
    if not re.search(r"https?://", text):
        issues.append("missing source URL")
    if len(text.split()) < 350:
        issues.append("review is too short (<350 words)")
    if "abstract-only" not in text.lower() and not re.search(r"local (text|pdf)|text_path|pdf_path|date read", text, re.I):
        issues.append("missing evidence of full-text/local-paper reading")
    return issues


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?", default="papers")
    ap.add_argument("--allow-empty", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    root = Path(args.path)
    files = review_files(root) if root.exists() else []
    if not files and not args.allow_empty:
        print("No review files found", file=sys.stderr)
        return 2
    failures = {str(p): check(p) for p in files}
    failures = {p: issues for p, issues in failures.items() if issues}
    if args.json:
        print(json.dumps({"checked": len(files), "failures": failures}, indent=2))
    else:
        print(f"Checked {len(files)} review(s)")
        for path, issues in failures.items():
            print(f"FAIL {path}")
            for issue in issues:
                print(f"  - {issue}")
        if not failures:
            print("PASS")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
