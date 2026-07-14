# Scouting note — production-pattern workflow projection and public/private validity

**Timestamp:** 2026-07-14T23:51:15Z  
**Scope:** Narrow expansion against charter objectives A/B/C. At intake the queue had 235 tasks: 228 completed, four blocked, two pending human decisions, and one pending consolidation; no source/research/review task remained. Existing reviews cover stateful SaaS and office tasks, integrated workplace substrates, language-simulated occupational environments, and source-to-task projection, but not the combination of production workflow-pattern provenance, synthetic SaaS state, policy-document use, API discovery, assertion rewards, and private-form leaderboard transport.

## Substantive finding (triage only)

**AutomationBench**

- Immutable record: https://arxiv.org/abs/2604.18934v1
- Immutable PDF: https://arxiv.org/pdf/2604.18934v1
- Official paper-linked repository: https://github.com/zapier/AutomationBench
- The arXiv API identifies Daniel Shepard and Robin Salimans; primary category `cs.AI`; submitted 21 April 2026 with no later version. The metadata summary contains no withdrawal notice. The versioned abstract, PDF, and official GitHub URLs returned HTTP 200.
- The **v1 abstract** says the benchmark projects real workflow patterns from Zapier into cross-application REST-API tasks spanning Sales, Marketing, Operations, Support, Finance, and HR. Agents must discover endpoints, follow layered business rules, and handle irrelevant or misleading records; grading is programmatic and end-state-only. It reports that the best tested frontier models score below 10%. These are author-reported abstract claims, not independently verified findings.
- The official repository README currently describes 600 scored domain tasks plus 200 unscored simple tasks across 47 simulated SaaS tools. It exposes both assertion-fraction partial credit and all-assertions strict completion, and distinguishes the public release from a held-out private leaderboard form that is said to follow the same distribution and assertion framework. The GitHub API reports a repository created 23 February 2026, updated 14 July 2026, last pushed 7 July 2026, with `main` as default and no machine-resolved SPDX license. This is current release-surface evidence, not a paper-time release audit.
- The distinctive validity question is whether **production-pattern provenance survives projection**. A workflow inspired by Zapier usage can support demand relevance without proving that the synthetic initial state, policy, endpoint set, accepted transitions, assertions, and omissions preserve the original professional work. End-state-only assertions may admit unsafe or destructive paths, double-count dependent consequences, or miss artifact usability and collateral state. Dense partial credit used as a reward signal can also change the intervention and expose evaluator structure.
- The public/private boundary is independently important: shared authoring language or asserted distributional similarity does not establish form equivalence, score transport, contamination resistance, or directional agreement. Private tasks and exact leaderboard evidence must remain unavailable evidence unless auditable records support those claims.
- This is metadata, abstract, official-README, URL, repository-metadata, and duplicate triage only. The PDF body, appendices, repository code, task bytes, workflow sources, simulator state, policy documents, assertions, trajectories, results, private tasks, and statistics were not read or audited. No claim is made that AutomationBench establishes professional workflow performance, public/private equivalence, general capability, safety, or readiness.

## Benchmark implication to test

Production-derived workflow benchmarks need a typed chain: `observed workflow pattern and sampling frame → source authority and valid time → projection/transformation ledger → synthetic initial state and app semantics → public policy/evidence → discoverable endpoint/action set → agent observations and transitions → intended and collateral terminal state → assertion dependency graph → partial/strict score → public/private form bridge → bounded claim`. Each link needs version identity and missing-evidence states.

A full audit should reconstruct at least one released cross-application task end to end and compare it with SaaS-Bench, OfficeBench, WorkArena L1/++, TheAgentCompany, OccuBench, and existing task-projection evidence. It should test assertion necessity/dependence, pre-satisfied state, alternative valid paths, protected/collateral mutations, policy authority and evidence adoption, endpoint-discovery parity, simulator reset validity, reward leakage, family-level clustering, release drift, and whether any empirical bridge supports public/private transport.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier production-origin benchmark), B (workflow-pattern-to-task-and-score projection), and C (stateful simulator, grader, and lifecycle evidence).
- **Evidence/artifact sought:** immutable-v1 deep review, pinned official-release audit, and one source-pattern→task→state→assertion reconstruction.
- **Uncertainty clarified:** whether real workflow-pattern provenance and final-state checks survive synthetic projection, and whether public/private directional agreement is evidenced rather than asserted.
- **Mode/balance:** one low-priority review restores a minimal worker research backlog behind the pending consolidation and human/operational blockers; no broad search bundle was added.
- **Duplication/scope:** adjacent benchmark families do not combine this production provenance, policy/API-discovery treatment, dense assertion reward, and private-form boundary. Business automation is a bounded method case, not a permanent scope choice.
- **Useful completion:** preserve source/sampling authority, projection transformations, simulator and reset identity, policy evidence, endpoint/action coverage, assertion dependence and collateral effects, partial/strict score roles, invalids, clustering, private-form missingness/bridging, release drift, cost, and strict claim ceilings.

Added one task: `review-automationbench-workflow-projection-validity` (priority 14).

Toolathlon-Verified and STAGE-Claw were triaged but not queued: the former substantially overlaps the existing web/tool/computer evolution stream, while the latter overlaps Anchor, state-based workflow, and generated-task conformance work more directly than AutomationBench fills the identified production-projection/private-form gap.

## Operational note

The required initial `git pull --ff-only` failed because the HTTPS GitHub remote lacks a noninteractive credential (`could not read Username`). Local `main` was 52 commits ahead of recorded `origin/main`; the run proceeded from local state. The pre-existing untracked `data/papers/source/` tree was not modified.
