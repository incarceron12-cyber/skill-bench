# Scouting note — successor resumability and handoff-debt gap

**Timestamp:** 2026-07-13T22:00:18Z  
**Scope:** Narrow expansion against charter objectives A/B/C. Queue inspection found 190 tasks before this run: 186 completed, two blocked, and two prerequisite-ordered pending consolidation/build tasks, with no pending source/research/review work. The reviewed corpus covers delegated-artifact integrity, typed handoffs, localized repair, persistent workspaces, and memory-conditioned action, but not a controlled benchmark of a successor resuming an interrupted predecessor state under alternative handoff records.

## Substantive finding (triage only)

**Handoff Debt: The Rediscovery Cost When Coding Agents Take Over Interrupted Tasks**

- Immutable arXiv record: https://arxiv.org/abs/2606.02875v1
- Immutable PDF: https://arxiv.org/pdf/2606.02875v1
- Immutable HTML: https://arxiv.org/html/2606.02875v1
- The arXiv API identifies Dipesh KC and Anjila Budathoki as authors; v1 was submitted and last updated 1 June 2026 in `cs.AI`, with no later version in the API record.
- The abstract introduces a takeover protocol that interrupts a coding agent at deterministic handoff points, freezes repository state, and exposes a successor to one of four views: repository only, raw trace, summary notes, or structured notes. It reports 75 source tasks, 181 handoff-point tasks, 724 takeover runs per successor model, and three successor models (2,172 takeover runs in total).
- The reported primary effect is on **rediscovery cost**, not merely endpoint success: context-bearing handoffs reduce median agent events by 20–59% and cumulative prompt tokens by 42–63% relative to repository-only takeover, while solved-rate effects are smaller and model-dependent. These figures are discovery leads requiring full-text verification, clustered analysis, and release audit.
- Structural inspection of the immutable HTML—not a full reading—confirmed dedicated methods/results sections for handoff-point detection, handoff states, all four views, source-task construction, runtime, models, validation/metrics, rediscovery cost, solved-rate effects, cross-model checks, limitations, reproducibility details, prompt/handoff schemas, an example structured handoff, and observed failure modes.
- No paper-specific code/data/results link was present among the immutable HTML's external links, and targeted exact-title/author web searches found the arXiv/Semantic Scholar records and third-party summaries but no verifiable author-owned release. A full review must search more deeply and record release absence if it remains unverified.
- Repository-wide title, ID, and phrase searches found no duplicate. Delegate52 asks whether delegated work preserves source and artifact boundaries; AgentCoop types handoffs and repair; HAS-Bench models participation events. None currently compares frozen takeover views or estimates the effort another configured agent needs to resume identical partial work.
- This is **metadata/abstract, URL, and section-structure triage only**. The PDF, appendices, task pool, run records, prompts, statistical analyses, and any artifacts were not fully read or audited. No claim is made that structured notes causally improve human or cross-domain handoffs, preserve all relevant state, establish professional collaboration, or improve capability/readiness.

## Benchmark implication to test

A realistic knowledge-work benchmark may need a distinct **resumability** unit: `predecessor task/state/trace → interruption rule → frozen handoff state → visible handoff record → successor reconstruction/action → terminal artifact/state`, with resume effort and endpoint quality reported separately. The view intervention must pin repository/workspace bytes, predecessor and successor identities, summary author/generator, token accounting, validation state, and retry/missingness policy. Otherwise extra context length, predecessor quality, checkpoint selection, summary leakage, solver familiarity, or repeated-task dependence can masquerade as lower handoff debt. The general hypothesis is cross-domain: structured, authority- and evidence-bearing state records can reduce successor rediscovery while preserving independent verification. Coding provides an executable bounded test, not a permanent scope choice.

## Charter decision filter and queue action

- **Objectives advanced:** A (realistic long-horizon benchmark design), B (state/trace-to-handoff transformation validity), and C (reusable workspace, trace, metric, and configured-system machinery).
- **Evidence/artifact sought:** immutable full-paper review plus any pinned author-owned release, reconstructing source/handoff sampling, interruption equivalence, view payloads, run topology, efficiency/success estimands, uncertainty, invalid runs, and reproducibility.
- **Uncertainty clarified:** whether the reported cost reductions isolate useful resumability information or reflect added context, generated-note cues, selected checkpoints, repeated-task structure, or configured-solver effects.
- **Mode/balance:** one narrow expansion task restores a small review backlog without displacing higher-priority consolidation/build work.
- **Duplication/scope:** complements existing artifact-integrity and typed-handoff reviews; software repositories are a bounded executable case for a reusable successor-resumability protocol.
- **Useful completion:** verify all headline denominators/effects and task dependence; audit prompts/schemas and release coverage; compare existing handoff, workspace, memory, context-compression, metric, and validity machinery; preserve strict human-handoff, professional-realism, causal-generalization, capability, production, and readiness ceilings.

Added `review-handoff-debt-successor-resumability` (priority 42). No second task was added.
