#!/usr/bin/env python3
"""Build the read-only Astro/Starlight content projection for skill-bench.

The repository remains canonical. This script creates a sanitized, navigable site
projection under site/src/content/docs/generated and a dashboard data file.
"""
from __future__ import annotations

import json
import os
import re
import shutil
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
GENERATED = SITE / "src" / "content" / "docs"
MANAGED_DIRECTORIES = ("charter", "insights", "landscape", "methodology", "papers", "operations", "next-steps")
DATA_OUT = SITE / "src" / "data" / "generated-dashboard.json"
GITHUB_BLOB = "https://github.com/incarceron12-cyber/skill-bench/blob/main/"
GITHUB_TREE = "https://github.com/incarceron12-cyber/skill-bench/tree/main/"
SITE_BASE = "/" + os.environ.get("SITE_BASE", "").strip("/") if os.environ.get("SITE_BASE", "").strip("/") else ""


def internal_url(path: str) -> str:
    """Prefix a root-relative route for project-hosted deployments such as GitHub Pages."""
    return f"{SITE_BASE}{path}"


PAGE_MAP = {
    "PROJECT_CHARTER.md": "/charter/",
    "docs/research-synthesis-index.md": "/insights/",
    "docs/state-of-the-art-map.md": "/landscape/",
    "docs/benchmark-landscape-research-program.md": "/landscape/research-program/",
    "docs/benchmark-design-taxonomy.md": "/methodology/",
    "docs/compounding-system.md": "/operations/compounding-system/",
    "docs/self-improvement-ledger.md": "/operations/improvement-ledger/",
    "papers/topic-index.md": "/papers/",
    "papers/README.md": "/papers/",
    "data/work_queue.json": "/next-steps/",
}


def title_and_body(text: str, fallback: str) -> tuple[str, str]:
    """Extract the first H1 as title and remove it from the rendered body."""
    match = re.search(r"^#\s+(.+?)\s*$", text, flags=re.M)
    if not match:
        return fallback, text
    title = match.group(1).strip()
    body = text[: match.start()] + text[match.end() :]
    return title, body.lstrip("\n")


def normalize_repo_path(source: Path, raw_target: str) -> str | None:
    """Resolve a relative Markdown link to a repository-relative path."""
    target = raw_target.split("#", 1)[0]
    if not target or target.startswith(("/", "#")) or "://" in target or target.startswith("mailto:"):
        return None
    resolved = (source.parent / target).resolve()
    try:
        return resolved.relative_to(ROOT).as_posix()
    except ValueError:
        return None


def site_target(repo_path: str, anchor: str = "") -> str:
    if repo_path in PAGE_MAP:
        return internal_url(PAGE_MAP[repo_path] + anchor)
    if repo_path.startswith("papers/agent-benchmarks/") and repo_path.endswith(".md"):
        slug = Path(repo_path).stem
        return internal_url(f"/papers/{slug}/" + anchor)
    path = ROOT / repo_path
    base = GITHUB_TREE if path.is_dir() else GITHUB_BLOB
    return base + repo_path + anchor


def rewrite_links(text: str, source: Path) -> str:
    """Rewrite repository-relative Markdown links for the generated website."""
    pattern = re.compile(r"(!?\[[^\]]*\])\(([^)]+)\)")

    def replace(match: re.Match[str]) -> str:
        label, target = match.groups()
        if target.startswith(("#", "/")) or "://" in target or target.startswith("mailto:"):
            return match.group(0)
        anchor = ""
        if "#" in target:
            anchor = "#" + target.split("#", 1)[1]
        repo_path = normalize_repo_path(source, target)
        if repo_path is None:
            return match.group(0)
        return f"{label}({site_target(repo_path, anchor)})"

    return pattern.sub(replace, text)


def frontmatter(title: str, description: str, *, page_template: str = "doc") -> str:
    data = {
        "title": title,
        "description": description,
        "template": page_template,
    }
    lines = ["---"]
    for key, value in data.items():
        lines.append(f"{key}: {json.dumps(value, ensure_ascii=False)}")
    lines.extend(["---", ""])
    return "\n".join(lines)


def emit_markdown(source_rel: str, output_rel: str, description: str) -> dict[str, str]:
    source = ROOT / source_rel
    text = source.read_text(errors="replace")
    title, body = title_and_body(text, Path(source_rel).stem.replace("-", " ").title())
    body = rewrite_links(body, source)
    output = GENERATED / output_rel
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(frontmatter(title, description) + body.rstrip() + "\n")
    return {"title": title, "source": source_rel, "url": internal_url("/" + output_rel.removesuffix(".md").replace("/index", "") + "/")}


def review_title(path: Path) -> str:
    text = path.read_text(errors="replace")
    title, _ = title_and_body(text, path.stem)
    return title


def emit_reviews() -> list[dict[str, str]]:
    reviews = []
    for source in sorted((ROOT / "papers" / "agent-benchmarks").glob("*.md"), reverse=True):
        title = review_title(source)
        rel = source.relative_to(ROOT).as_posix()
        _, body = title_and_body(source.read_text(errors="replace"), title)
        body = rewrite_links(body, source)
        slug = source.stem
        output = GENERATED / "papers" / f"{slug}.md"
        output.parent.mkdir(parents=True, exist_ok=True)
        description = "Full-text, evidence-backed review with methodology, strengths, limitations, and Skill Bench implications."
        output.write_text(frontmatter(title, description) + body.rstrip() + "\n")
        date_match = re.match(r"(\d{4}-\d{2}-\d{2})-", slug)
        reviews.append(
            {
                "title": title,
                "slug": slug,
                "url": internal_url(f"/papers/{slug}/"),
                "date": date_match.group(1) if date_match else "",
                "source": rel,
            }
        )
    return reviews


def emit_paper_index(reviews: list[dict[str, str]]) -> dict[str, str]:
    """Render the curated topic map and expose reviews awaiting classification."""
    source = ROOT / "papers" / "topic-index.md"
    text = source.read_text(errors="replace")
    title, body = title_and_body(text, "Paper Review Topic Index")
    linked_slugs = set(re.findall(r"agent-benchmarks/([^/)]+)\.md", text))
    body = rewrite_links(body, source)
    unindexed = [review for review in reviews if review["slug"] not in linked_slugs]
    coverage = len(reviews) - len(unindexed)
    summary = [
        f"> **Corpus coverage:** {len(reviews)} deep reviews · {coverage} assigned in the curated thematic map · {len(unindexed)} recent reviews awaiting thematic placement.",
        "",
    ]
    if unindexed:
        summary.extend(
            [
                "## Recently added, awaiting thematic placement",
                "",
                "These reviews are fully available and searchable. The consolidator should assign their primary research question in the canonical topic index rather than letting this section become a permanent paper dump.",
                "",
                "| Date | Review |",
                "|---|---|",
            ]
        )
        for review in unindexed:
            summary.append(f"| {review['date']} | [{review['title']}]({review['url']}) |")
        summary.append("")
    output = GENERATED / "papers" / "index.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    description = "Thematically organized navigation across the evidence-backed paper review corpus."
    output.write_text(frontmatter(title, description) + "\n".join(summary) + body.rstrip() + "\n")
    return {"title": title, "source": "papers/topic-index.md", "url": internal_url("/papers/")}


def queue_projection() -> tuple[dict[str, int], list[dict[str, object]]]:
    payload = json.loads((ROOT / "data" / "work_queue.json").read_text())
    tasks = payload.get("tasks", payload if isinstance(payload, list) else [])
    counts = Counter(str(task.get("status", "unknown")) for task in tasks)
    pending = sorted(
        (task for task in tasks if task.get("status") in {"pending", "claimed", "blocked"}),
        key=lambda task: (-int(task.get("priority", 0)), str(task.get("created_at", ""))),
    )
    public_tasks = [
        {
            "id": task.get("id", ""),
            "title": task.get("title", "Untitled task"),
            "type": task.get("type", ""),
            "status": task.get("status", ""),
            "priority": task.get("priority", 0),
            "rationale": task.get("rationale", ""),
            "next_action": task.get("next_action", ""),
            "claimed_by": task.get("claimed_by", ""),
        }
        for task in pending
    ]
    return dict(counts), public_tasks


def emit_next_steps(counts: dict[str, int], tasks: list[dict[str, object]]) -> None:
    lines = [
        frontmatter("Next steps", "Live read-only projection of the charter-aligned research and build queue."),
        "> This page is generated from `data/work_queue.json`. The repository queue remains canonical.\n",
        "## Queue status\n",
        "| Status | Tasks |",
        "|---|---:|",
    ]
    for status in ("claimed", "pending", "blocked", "completed"):
        lines.append(f"| {status.title()} | {counts.get(status, 0)} |")
    lines.extend(["", "## Active priorities", ""])
    if not tasks:
        lines.append("No active tasks are currently queued.")
    for task in tasks:
        status = str(task["status"]).upper()
        lines.extend(
            [
                f"### {task['title']}",
                "",
                f"`{status}` · `{task['type']}` · priority **{task['priority']}**",
                "",
                str(task["rationale"]),
                "",
                "**Next action**",
                "",
                str(task["next_action"]),
                "",
            ]
        )
    output = GENERATED / "next-steps" / "index.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines).rstrip() + "\n")


def main() -> int:
    GENERATED.mkdir(parents=True, exist_ok=True)
    for directory in MANAGED_DIRECTORIES:
        managed = GENERATED / directory
        if managed.exists():
            shutil.rmtree(managed)

    pages = [
        emit_markdown("PROJECT_CHARTER.md", "charter/index.md", "Canonical mission, scope, objectives, success criteria, and anti-drift boundaries."),
        emit_markdown("docs/research-synthesis-index.md", "insights/index.md", "Grouped insights, paper relevance tiers, and direct implications for Skill Bench."),
        emit_markdown("docs/state-of-the-art-map.md", "landscape/index.md", "Comparison of benchmark families, strengths, limitations, and open questions."),
        emit_markdown("docs/benchmark-landscape-research-program.md", "landscape/research-program.md", "Research program comparing established benchmarks with newer attempts to improve them."),
        emit_markdown("docs/benchmark-design-taxonomy.md", "methodology/index.md", "Canonical technical synthesis for expertise-to-evaluation benchmark design."),
        emit_markdown("docs/compounding-system.md", "operations/compounding-system.md", "How the 24/7 research, building, consolidation, and briefing loop works."),
        emit_markdown("docs/self-improvement-ledger.md", "operations/improvement-ledger.md", "Evidence ledger for bounded improvements to the research and build system."),
    ]
    reviews = emit_reviews()
    pages.append(emit_paper_index(reviews))
    counts, tasks = queue_projection()
    emit_next_steps(counts, tasks)

    synthesis = (ROOT / "docs" / "research-synthesis-index.md").read_text(errors="replace")
    insight_groups = len(re.findall(r"^##\s+\d+\.", synthesis, flags=re.M))
    dashboard = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "paper_count": len(reviews),
        "insight_group_count": insight_groups,
        "queue": counts,
        "top_tasks": tasks[:5],
        "latest_reviews": reviews[:6],
        "pages": pages,
    }
    DATA_OUT.parent.mkdir(parents=True, exist_ok=True)
    DATA_OUT.write_text(json.dumps(dashboard, indent=2, ensure_ascii=False) + "\n")
    print(
        json.dumps(
            {
                "status": "ok",
                "generated_pages": len(pages) + len(reviews) + 1,
                "reviews": len(reviews),
                "insight_groups": insight_groups,
                "active_tasks": len(tasks),
                "output": str(GENERATED.relative_to(ROOT)),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
