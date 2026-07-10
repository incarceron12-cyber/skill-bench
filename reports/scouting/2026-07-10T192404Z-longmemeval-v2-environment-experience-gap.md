# Scouting note — environment-experience memory validity gap

**Timestamp:** 2026-07-10T19:24:04Z  
**Scope:** Narrow search against charter objectives A/B/C after finding no pending source, research, or review work. This run targeted the under-covered boundary between persistent memory and learned professional/environment procedure; it did not repeat broad agent-benchmark discovery.

## Substantive finding (triage only)

**LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues**

- Immutable arXiv record: https://arxiv.org/abs/2605.12493v1
- Immutable PDF: https://arxiv.org/pdf/2605.12493v1
- Official repository: https://github.com/xiaowu0162/LongMemEval-V2
- arXiv API metadata identifies version 1, submitted 2026-05-12, with 451 manually curated questions over histories reaching 500 trajectories and 115M tokens.
- The abstract distinguishes five experience-memory targets: static state, dynamic state, workflow knowledge, environment gotchas, and premise awareness. It evaluates memory as compact evidence gathering for downstream question answering and reports a file-backed coding-agent approach alongside RAG baselines.
- GitHub's repository search identifies `xiaowu0162/LongMemEval-V2` as the official repository. A deep review must verify that relationship from the paper/project, pin a revision, inspect data and evaluation code, and determine what is actually released.
- This is **metadata/abstract and release-location triage only**. The full paper and repository were not read during scouting. Dataset construction, expert curation, source trajectories, question validity, leakage controls, metrics, costs, uncertainty, and claims require full review.

## Why this is distinct

The repository already covers persistent workspace state, evolving evidence, expert-authored procedures, and agentic context evolution. It does not yet have a direct full-source case on whether an agent can transform many prior environment trajectories into inspectable, reusable experiential knowledge—especially workflow rules, failure signatures, affordances, and premise checks—and whether a QA proxy licenses claims about better future task performance.

The reusable question is not whether skill-bench should become a web-agent memory benchmark. It is how trajectory-derived experience should be represented, provenance-linked, retrieved, and validated as evidence of procedural transfer; how memory extraction quality is separated from downstream reasoning and action; and which counterfactual task-performance or intervention tests are needed before calling a memory store an “experienced colleague.”

## Charter decision filter and queue action

- **Objectives advanced:** A (memory and configured-agent evaluation), B (experience-to-procedure transfer), and C (trace, provenance, and diagnostic contracts).
- **Evidence/artifact sought:** immutable-v1 full-paper review, pinned official-release audit, and a crosswalk to existing expertise-transfer, context-evolution, workspace, trace, validity, metric, and task-health machinery.
- **Uncertainty clarified:** whether curated QA measures usable environment expertise; whether trajectory evidence preserves authority, valid time, causality, failed attempts, and premise scope; which gains come from storage, retrieval, coding-agent reasoning, or larger inference budgets; and whether downstream transfer is demonstrated.
- **Mode/balance:** one narrow expansion task at priority 71. Source/research/review backlog was empty; one build was active and one dependent build remained pending.
- **Duplication/scope:** no local index entry, review, queue task, or scouting note matched `2605.12493`, `LongMemEval-V2`, or `AgentRunbook`. ACE studies context evolution but not this released trajectory-to-environment-experience evaluation. Web environments are a methodological case, not a scope commitment.
- **Useful completion:** paper claims and release evidence are separated; at least two question/history/evidence paths are traced; curation, leakage, evidence fidelity, confounds, cost, and downstream-validity boundaries are audited; only nonduplicate implications enter existing contracts.

Added `review-longmemeval-v2-environment-experience-memory` (priority 71). No second task was added.
