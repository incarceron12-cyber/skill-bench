# Scouting note — Self-GC context-object lifecycle validity gap

- **Timestamp:** 2026-07-17T08:49:18Z
- **Evidence status:** arXiv API metadata/abstract, immutable endpoint checks, exact local corpus/queue duplicate search, targeted web release discovery, and GitHub repository-search triage only. The paper body, appendices, study sessions, prompts, context objects, evaluator, statistical analyses, online experiment, and reported results were **not** deeply read or audited during scouting.

## Substantive candidate — triage only

**Self-GC: Self-Governing Context for Long-Horizon LLM Agents** — Xubin Hao, Hongjin Meng, Xin Yin, Jiawei Zhu, and Chenpeng Cao; arXiv:2607.00692v1.

- Immutable record/PDF/HTML: https://arxiv.org/abs/2607.00692v1, https://arxiv.org/pdf/2607.00692v1, and https://arxiv.org/html/2607.00692v1
- The arXiv API identifies v1, submitted 1 July 2026, and its summary contains no withdrawal/retraction notice. All three immutable endpoints returned HTTP 200.
- The abstract frames long-horizon context as structured user turns, tool spans, files, plans, constraints, and skill state rather than a disposable text suffix. It describes indexed objects; side-planner proposals to fold, mask, or prune; and harness-enforced recoverable sidecars, safe commit boundaries, and cache-aware commits.
- The abstract reports a 33-session Hard Set, a 332-session production-derived suite, a future-continuation “no-impact” outcome, token pruning, several planner backbones and heuristic baselines, and an online account-level production split. All construction details, denominators, dependence, observer validity, uncertainty, failure patterns, token figures, and production claims await full-paper audit.
- Targeted exact-title/author/framework web search and GitHub repository search did not locate an author-owned code or dataset release. This is only an acquisition-time search result; the reviewer must inspect the full paper and references before recording release availability or absence.
- Repository-wide searches for the exact title, arXiv ID, and framework name found no prior review, queue task, or scouting note.

## Why this is a narrow, useful gap

The corpus already audits lossy context compression (ACON), plan eviction, governance decay, decision fidelity under compression, persistent memory, and workspace provenance. Self-GC appears to expose a different chain:

`context-object creation and authority → indexed identity and dependency → planner-proposed fold/mask/prune → harness admission and commit → recoverable sidecar/cache state → later access and reconstruction → future behavioral/artifact/state effect → token/cost and consequence`.

That chain could connect context engineering to workspace and trace contracts without reducing context quality to answer accuracy or token count. But an unchanged selected future continuation may not establish proposition completeness, locator preservation, alternative-future sufficiency, artifact integrity, authorized use, correct decisions, or consequences. A production-derived session suite is not automatically representative of production work; an online account-level treatment requires its own assignment, interference, outcome, and configured-system audit. The source is relevant as cross-domain runtime lifecycle methodology, not as a reason to narrow the benchmark to context-management agents.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier and production-system research), B (evidence/context-to-evaluation methodology), and C (workspace, trace, reliability, metric, and validity machinery).
- **Concrete evidence:** immutable-v1 deep review and timing-aware release audit covering object types and authority, intervention lineage, commit/recovery semantics, study sampling, continuation observer, online split, uncertainty, costs, and failures.
- **Uncertainty clarified:** whether object-level lifecycle control preserves decision-relevant context or only one selected continuation under one configured observer, and whether reported efficiency transports without stale-state, authority, artifact, or consequence loss.
- **Mode:** narrow expansion. The queue already has two higher-priority consolidation tasks and a human prerequisite; this review is priority 66 and does not displace them.
- **Duplication/scope check:** adjacent reviews provide comparison machinery but do not audit harness-enforced context-object lifecycle and recoverability. No Self-GC-specific schema or context-agent scope commitment is proposed.
- **Useful completion:** section/page-grounded claim audit and nonduplicate retain/repair/test implications while keeping semantic equivalence, general capability, professional validity, production fitness, safety, and readiness claims false unless separately evidenced.

Added one task: `review-self-gc-context-object-lifecycle-validity` (review, priority 66). No other candidate was queued.
