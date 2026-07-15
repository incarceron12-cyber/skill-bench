# Scouting note — simulated feedback and artifact-evaluation validity

**Timestamp:** 2026-07-15T00:54:11Z  
**Scope:** Narrow expansion against charter objectives A/B/C. At intake the queue had 239 tasks: 232 completed, four blocked, two pending human decisions, and one pending consolidation; no source/research/review task remained. The corpus now has strong coverage of professional artifacts, long-horizon workflows, user-simulator decision fidelity, rubric dependence, and artifact-view admissibility, but no review of a released benchmark that combines million-token executions, iterative simulated-user feedback, deliverable-specific rubrics, and visual plus functional sandbox checks.

## Substantive finding (triage only)

**AgencyBench: Benchmarking the Frontiers of Autonomous Agents in 1M-Token Real-World Contexts**

- Immutable record: https://arxiv.org/abs/2601.11044v4
- Immutable PDF: https://arxiv.org/pdf/2601.11044v4
- Immutable HTML: https://arxiv.org/html/2601.11044v4
- Official repository: https://github.com/GAIR-NLP/AgencyBench
- The arXiv API identifies Keyu Li et al.; category `cs.AI`; first submitted 16 January 2026 and updated to v4 on 23 April 2026. The metadata summary contains no withdrawal notice. The versioned abstract, PDF, HTML, and official repository URLs returned HTTP 200.
- The **v4 abstract** describes 32 scenarios and 138 tasks derived from daily AI usage, each with specific queries, deliverables, and rubrics; it reports averages of 90 tool calls, one million tokens, and hours of execution. Automated evaluation combines an LLM user simulator that supplies iterative feedback with Docker-sandbox visual and functional rubric assessment. It reports differences by model family, resource efficiency, feedback-driven correction, tool preference, and scaffold. These are author-reported abstract claims, not independently verified findings.
- The official repository is a concrete release surface rather than a paper-only proposal. GitHub metadata currently reports an MIT license, `main` default branch, creation on 17 September 2025, last push on 23 January 2026, and repository update on 10 July 2026. This is current metadata, not an audit of paper-time or version-matched release bytes.
- The distinctive validity question is the **coupled intervention-observer loop**. Simulated feedback can reveal requirements, steer repairs, or leak rubric-adjacent information; the same system is then judged on rubric-defined visual and functional deliverables. Endpoint quality, feedback uptake, self-correction, simulator fidelity, observer coverage, and professional acceptance are different estimands. Long context and many calls increase operational stress but do not by themselves establish realistic work, necessity, efficiency, or downstream usefulness.
- This is metadata, abstract, URL, repository-metadata, and duplicate triage only. The paper body, appendices, repository files, tasks, prompts, simulator policy, deliverable bytes, rubrics, judges, sandbox, trajectories, results, human-study records, and statistics were not read or audited. No claim is made that the tasks are representative, the simulator is faithful, the visual/functional checks are valid, the released code reproduces v4, or any system is professionally useful or ready.

## Benchmark implication to test

Feedback-mediated artifact benchmarks need a typed chain: `usage/demand source → scenario/task projection → public query and source pack → simulator identity, authority, evidence view, and feedback policy → feedback event and information delta → agent uptake and revision → delivered native artifact/state → renderer/extractor/toolchain identity → visual and functional observations → criterion applicability/dependence → score → human or downstream acceptance → bounded claim`. They also need matched no-feedback or controlled-feedback comparisons before calling gains self-correction.

A full review should reconstruct at least one released task end to end and determine whether its long context is necessary rather than padding; whether the simulator asks, answers, critiques, or discloses target information; whether simulated feedback corresponds to any observed real-user behavior; whether criterion text or reference information leaks through feedback; whether visual and functional checks observe the same artifact and accepted alternatives; whether criterion dependence makes aggregation compensatory; how judge reliability, sandbox failures, invalid trials, repeat variance, call/token cost, and scaffold identity are handled; and whether release bytes match v4. Compare with PaperBench, SciVisAgentBench, UniClawBench, DeskCraft, AgencyBench-adjacent HAS-Bench, User-simulator decision fidelity, and the repository's artifact-admissibility and feedback-intervention chains.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier realistic-agent and release research), B (feedback-to-artifact-to-score validity), and C (scalable artifact, simulator, and observer diagnostics).
- **Evidence/artifact sought:** immutable-v4 deep review, pinned release audit, and one query→feedback→revision→artifact→visual/functional-check reconstruction.
- **Uncertainty clarified:** whether iterative simulation and plural artifact checks diagnose long-horizon work or create a coupled treatment/evaluator shortcut, and what claim the released evidence can support.
- **Mode/balance:** one low-priority review restores a minimal research backlog behind the pending consolidation and operational/human blockers; no broad search bundle was added.
- **Duplication/scope:** existing reviews cover each ingredient separately but not their released composition at million-token scale. The benchmark's heterogeneous scenarios test reusable feedback/artifact machinery and do not narrow `skill-bench` to one profession.
- **Useful completion:** preserve task and release provenance, context necessity, simulator role/authority/information flow, feedback and uptake events, artifact/view identity, visual/functional criterion dependence, human evidence, scaffold/configuration, invalids, repeats, cost, release drift, and strict claim ceilings; derive repairs using existing contracts unless a concrete executable gap remains.

Added one task: `review-agencybench-feedback-artifact-validity` (priority 13).

ArchEval and AutoResearchBench were not queued: both are more domain-specific and overlap the already mature scientific/executable-work streams. AgencyBench fills the narrower unresolved composition gap between simulated feedback, long-horizon artifact production, and plural automated observation.

## Operational note

The required initial `git pull --ff-only` failed because the HTTPS GitHub remote lacks a noninteractive credential (`could not read Username`). Local `main` was 63 commits ahead of recorded `origin/main`; the run proceeded from local state. The pre-existing untracked `data/papers/source/` tree was not modified.
