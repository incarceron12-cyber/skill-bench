# Aggressive TCS Self-Improvement Cadence Plan

> **For Hermes:** This is a discussion plan only. Do not implement cron changes or repository restructuring until Samuel approves the operating model.

**Goal:** Increase `skill-bench` from a few daily research updates into a high-cadence, self-improving research/build system that expands outward aggressively, consolidates repeatedly, and compounds toward high-quality agentic knowledge-work benchmarks.

**Architecture:** Use a two-loop system: fast 15-minute scout/build cycles during active hours, plus slower consolidation/governance cycles that prevent drift. The system should behave like a production agent organization: every run has a role, output contract, budget, guardrails, and feedback path into the repository.

**Tech Stack:** Hermes cron jobs, GitHub repo `/home/sam/skill-bench`, arXiv/Semantic Scholar/web search, downloaded PDFs/extracted text, Markdown research artifacts, Python scripts, git/gh, optional future Kanban board.

---

## 0. Research basis from initial scan

### Anthropic — effective agents

Key lessons to incorporate:

- Start with simple composable patterns before complex frameworks.
- Distinguish deterministic workflows from flexible agents.
- Use agents where flexibility and dynamic tool use matter enough to justify cost/latency.
- Keep prompts/tools visible and debuggable; abstractions that hide traces make improvement harder.

### Anthropic — context engineering

Key lessons:

- The central problem is no longer only prompt wording, but curating the entire context state.
- Agents should assemble understanding layer-by-layer, preserving only what is useful.
- Context should be intentionally shaped every turn: instructions, tools, memory, retrieved docs, traces, and summaries.

### Anthropic — tools for agents

Key lessons:

- Tools should be designed for non-deterministic agents, not just deterministic API consumers.
- Tool quality should be evaluated with realistic tasks.
- Good tools return meaningful, token-efficient context.
- Tool namespacing and clear boundaries matter.
- Use agents themselves to improve tools against evals.

### Anthropic/AWS/Databricks-style production eval direction

Key lessons:

- Production agent evaluation must inspect full system behavior, not just final answer quality.
- Need task/trial/grader/transcript vocabulary.
- Need root-cause visibility for tool selection, memory retrieval, multi-step reasoning, state changes, and task completion.
- Agent evals become a lifecycle asset: failures drive development and prevent regressions.

### Karpathy AutoResearch

Key lessons:

- Treat the repo and Markdown instruction files as the “research org code.”
- Run many bounded experiments under a fixed budget.
- Keep what improves a metric; revert or discard what does not.
- The human role shifts from writer to research director/advisor.
- The highest-leverage artifact may be the evolving program/instructions, not only the code.

### Self-evolving agent literature / EvoAgentX

Key lessons:

- Self-improvement should be modular, evaluated, and goal-driven.
- Evolution targets can include prompts, skills, tools, workflows, task decompositions, memories, and benchmark scenarios.
- Unbounded self-evolution without evaluation creates drift; every mutation needs a fitness signal.

### Hermes-specific leverage

Hermes already has:

- Cron jobs for durable autonomous loops.
- Skills for reusable procedures.
- Memory for durable user/project preferences.
- Session search for past work.
- GitHub/terminal/file tools for repo evolution.
- Workdir-aware cron jobs that load project context.
- Potential Kanban orchestration if we want task queues later.

---

## 1. Proposed operating model

## Two fronts

### Front A — Research expansion frontier

Purpose: expand outward aggressively.

Activities:

- Search internet/arXiv/Semantic Scholar/GitHub for papers, production systems, benchmark repos, blog posts, and public workflows.
- Download and read papers.
- Add structured reviews.
- Identify concepts from Anthropic, Karpathy, Amazon, Databricks, EvoAgentX, AA-Briefcase, OSWorld, OdysseyBench, SaaS-Bench, MBABench, etc.
- Maintain an expanding topic graph.

Output artifacts:

- `papers/**`
- `reports/scouting/**`
- `docs/state-of-the-art-map.md`
- `docs/production-systems.md`
- `docs/concepts/**`

### Front B — Consolidation/build frontier

Purpose: turn expansion into durable project structure.

Activities:

- Consolidate insights into benchmark design primitives.
- Update templates, rubrics, schemas, task specs.
- Build scripts and dashboards.
- Improve repository architecture.
- Draft sponsor/expert contribution mechanisms.
- Convert repeated workflows into skills or repo scripts.

Output artifacts:

- `docs/benchmark-design-primitives.md`
- `docs/expertise-transfer-system.md`
- `benchmarks/pilots/**`
- `schemas/**`
- `scripts/**`
- `templates/**`
- `docs/sponsor-and-community-strategy.md`

---

## 2. Cadence proposal

Do **not** run one huge agent every 15 minutes. Instead run role-specific microcycles.

### Continuous 24/7 high-cadence loop

Samuel has clarified that the system should continue **throughout the night**, with the mission remaining tightly focused on researching, learning, and building the benchmark. The 15-minute heartbeat therefore runs 24 hours a day; only human-facing delivery is throttled.

| Minute | Role | Purpose | Side effects |
|---:|---|---|---|
| `*/15` | Orchestrator heartbeat | Claim the highest-value queued research/build/consolidation task | Updates queue and dispatch state |
| `2-59/15` | Scout | Search/triage new material when discovery backlog is low | Writes scouting notes and source candidates |
| `5-59/15` | Extractor | Download/extract/read queued sources | Updates paper index/text |
| `8-59/15` | Researcher/reviewer | Read a source or synthesize a narrow concept | Writes reviews/concept notes |
| `11-59/15` | Benchmark builder | Implement a bounded benchmark/repo improvement | Edits scripts/docs/templates/scenarios |
| `0 */2` | Consolidator | Merge duplicates, update maps, prune drift | Larger durable-doc changes |
| `30 9,13,17,21` | Director briefing | Human-facing synthesis and decision requests | Telegram summary/questions |

The jobs should not each repeat every role blindly. A shared priority queue should enforce mission-focused work allocation:

1. unblock benchmark construction;
2. deeply understand relevant production/research methods;
3. convert learning into benchmark artifacts;
4. consolidate accumulated material;
5. expand outward only when the current backlog is healthy.

**Phase 1 cadence:** continuous 15-minute orchestrator heartbeat plus staggered workers, 24/7.
**Phase 2 cadence:** tune worker frequency and concurrency using observed throughput, duplicate rate, review quality, cost, and benchmark artifacts produced.
**Phase 3 cadence:** adopt Hermes Kanban or an equivalent durable dispatcher if the file queue becomes limiting.

---

## 3. Guardrails before increasing cadence

### Required guardrail 1 — write/read separation

Fast scouting jobs should not freely edit everything. They should write to inbox files:

- `inbox/scouting/YYYY-MM-DD-HHMM.md`
- `inbox/sources/YYYY-MM-DD-HHMM.json`

Review/build/consolidation jobs can consume these.

### Required guardrail 2 — commit discipline

Every job should only commit if it made meaningful changes. Commit messages should identify role:

- `scout: add sources for 2026-07-10 1045`
- `review: analyze SaaS-Bench methodology`
- `build: add rubric schema validator`
- `synth: consolidate production agent eval patterns`

### Required guardrail 3 — no self-modifying cron without approval

Cron jobs can propose schedule changes but should not create/remove/update cron jobs unless Samuel explicitly approves.

### Required guardrail 4 — quality gates

Before push:

```bash
python -m py_compile scripts/*.py
python scripts/make_daily_digest.py --limit 3 >/tmp/skill_bench_digest_check.md
 git status --short
```

Later add real tests:

- JSON schema validation for paper index.
- Markdown link checks.
- Duplicate source detection.
- Review completeness checks.

### Required guardrail 5 — consolidation quotas

Expansion creates mess by design. Consolidation must be scheduled:

- Every 2 hours: local consolidation of docs/taxonomy.
- Daily: “what did we learn?” synthesis.
- Weekly: prune/merge/rewrite core docs.

---

## 4. Repository changes I recommend before turning up cadence

### Task 1: Add project instructions

Create `AGENTS.md` or `.hermes.md` in repo root so all cron jobs inherit project rules.

Should define:

- project north star,
- quality bar for paper reviews,
- no hallucinated reading,
- commit/push discipline,
- role-specific output contracts,
- consolidation rhythm.

### Task 2: Add queue/inbox structure

Create:

```text
inbox/scouting/
inbox/review-queue/
inbox/build-ideas/
inbox/questions-for-samuel/
reports/scouting/
reports/consolidation/
docs/concepts/
schemas/
tests/
```

### Task 3: Add machine-readable work queue

Start with a simple file before adopting Hermes Kanban:

```text
data/work_queue.json
```

Fields:

- `id`
- `type`: source | review | build | consolidate | ask_user
- `priority`
- `status`
- `created_at`
- `source`
- `rationale`
- `next_action`

### Task 4: Add review quality checker

Create `scripts/check_review_quality.py` to ensure reviews include:

- one-sentence contribution,
- methodology,
- unique insight,
- transferable patterns,
- limitations,
- relevance to skill-bench,
- action items.

### Task 5: Add self-improvement ledger

Create:

```text
docs/self-improvement-ledger.md
```

Track each proposed system change:

- hypothesis,
- change made,
- expected improvement,
- evidence after runs,
- keep/revert/modify.

This is the Karpathy loop translated from ML experiments to research-org operations.

### Task 6: Add production systems review track

Create:

```text
docs/production-agent-systems.md
papers/production-systems/
```

Initial sources:

- Anthropic: Building Effective Agents
- Anthropic: Effective Context Engineering
- Anthropic: Writing Tools for Agents
- Anthropic: Demystifying Evals for AI Agents
- AWS: Evaluating AI agents at Amazon
- Databricks: Production AI agent evaluations
- Karpathy AutoResearch
- EvoAgentX
- Self-evolving agents surveys

---

## 5. Proposed cron redesign

Current jobs:

- daily morning discovery
- daily midday review
- daily evening synthesis

Proposed replacement/additive jobs after approval:

### Job A — TCS orchestrator heartbeat

Schedule: `*/15 * * * *`

Role:

- Inspect queue/backlogs/recent commits.
- Select the highest-value mission-aligned next action.
- Prevent workers from duplicating work.
- Route effort among research, review, benchmark building, and consolidation.

### Job B — TCS scout

Schedule: `2-59/15 * * * *`

Role:

- Search web/arXiv/GitHub when discovery is the current bottleneck.
- Add candidate sources to queue.
- Write small scouting notes.
- No deep reviews or broad repo edits.

### Job C — TCS source extractor

Schedule: `5-59/15 * * * *`

Role:

- Pull queued sources.
- Download/extract PDFs/pages.
- Update metadata.
- Mark sources read-ready.

### Job D — TCS researcher/reviewer

Schedule: `8-59/15 * * * *`

Role:

- Read one queued source deeply or synthesize one tightly scoped concept.
- Write a comprehensive review/concept artifact.
- Update review status and queue evidence.

### Job E — TCS benchmark builder

Schedule: `11-59/15 * * * *`

Role:

- Consume the highest-priority build task.
- Convert research into benchmark specs, schemas, scripts, rubrics, pilot source packs, or tests.
- Run checks.
- Commit/push only verified improvements.

### Job F — TCS consolidator

Schedule: `0 */2 * * *`

Role:

- Merge concepts.
- Update maps/templates/schemas.
- Deduplicate and prune low-signal material.
- Reprioritize the work queue.
- Create questions for Samuel.

### Job G — Samuel discussion brief

Schedule: `30 9,13,17,21 * * *`

Role:

- Send human-facing summary of work since the previous brief.
- Highlight decisions needed.
- Ask before major implementation/publication/external-action changes.

The research/build system runs continuously overnight; only Telegram brief delivery is intentionally batched to avoid noisy 15-minute messages.

---

## 6. “Talk with me before you implement” protocol

Jobs should classify changes into three levels:

### Level 0 — safe autonomous

Can implement without asking:

- add source metadata,
- download/extract papers,
- write paper reviews,
- update daily reports,
- add small docs sections,
- fix scripts/tests.

### Level 1 — autonomous but report

Can implement, then summarize:

- add templates,
- add schemas,
- add checkers,
- reorganize non-core docs,
- create pilot draft files.

### Level 2 — ask Samuel first

Must ask before implementing:

- changing cron cadence dramatically,
- deleting/replacing existing jobs,
- publishing public-facing claims,
- contacting sponsors/experts,
- changing repo visibility,
- creating many GitHub issues/PRs,
- launching external services,
- spending money/API credits intentionally.

Your current request asks for a dramatic cadence change, so I am treating it as Level 2 and asking for approval before modifying cron.

---

## 7. Proposed first implementation batch after approval

### Batch 1 — repo infrastructure, no cron changes yet

1. Create `.hermes.md` project rules.
2. Create inbox/queue directories.
3. Add `data/work_queue.json`.
4. Add `scripts/queue.py` for add/list/claim/complete.
5. Add `scripts/check_review_quality.py`.
6. Add `docs/self-improvement-ledger.md`.
7. Add `docs/production-agent-systems.md` seeded with the sources above.
8. Commit/push.

### Batch 2 — add high-cadence cron jobs in parallel with existing ones

1. Keep existing daily jobs temporarily.
2. Add new jobs A–F with schedules above.
3. Make them write to queue/inbox.
4. Run each once manually.
5. Inspect output quality.

### Batch 3 — consolidate/reduce noise

1. Pause or remove old daily jobs if new jobs supersede them.
2. Adjust schedules based on observed quality.
3. Add weekly deep consolidation.
4. Add explicit dashboard/index of progress.

---

## 8. Decisions remaining before implementation

Samuel has already decided:

- The research/build loop should run **24/7**, including overnight.
- The mission is the repository goal: researching, learning, and building the benchmark—not generic Hermes self-modification.
- Cadence should be anchored by a 15-minute heartbeat.

Remaining decisions:

1. Delivery volume: should only the four daily discussion briefs message Telegram while overnight workers quietly commit/push? **Recommended: yes.**
2. Autonomy: may builder jobs make Level 1 repo changes without asking, while asking before Level 2 changes? **Recommended: yes.**
3. GitHub workflow: direct commits to `main`, or branches/PRs for builder changes? **Recommended initially: direct small verified commits to main; branches for larger changes.**
4. Resource ceiling: should we cap deep-paper reviews/builds per hour to prevent duplicate work and runaway token/API cost? **Recommended: queue-based cap of one deep review and one build task per 15-minute cycle, with no duplicate claims.**

## Recommendation

Approve **Batch 1 plus the 24/7 queue-driven cadence** together:

- Add the project rules, queue, quality checker, self-improvement ledger, and production-systems track first.
- Then create the continuous orchestrator/scout/extractor/reviewer/builder/consolidator jobs.
- Keep worker deliveries quiet and send four consolidated Telegram briefs per day.
- Run every job once manually, verify artifacts and GitHub commits, then leave the 24/7 loop active.
- Review throughput, duplication, and quality after the first 24 hours and tune schedules without weakening the 15-minute heartbeat.
