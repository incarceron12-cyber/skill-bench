# Scouting note — partial benchmark decision-validity gap

**Timestamp:** 2026-07-15T05:15:02Z  
**Scope:** Narrow expansion against charter objectives A/C. Queue inspection found 251 tasks: 244 completed, four blocked, two pending human decisions, and one pending build; no source/research/review task remained. Existing reviews cover reduced-panel rank fidelity, psychometric task selection, repeated-trial reliability, and metric validity, but not whether a partial task run preserves a predeclared pairwise benchmark decision under explicit coverage and unresolved-comparison constraints.

## Substantive finding — triage only

**How Many Tasks Are Enough for Agent Benchmark Decisions? A Replay Analysis of Public LLM Agent Benchmarks** — Wei-Jung Huang, arXiv:2607.12338v1.

- Immutable record: https://arxiv.org/abs/2607.12338v1
- Immutable PDF target: https://arxiv.org/pdf/2607.12338v1
- Official repository: https://github.com/WilliamWJHuang/How-Many-Tasks-Are-Enough-for-Agent-Benchmark-Decisions
- The arXiv API identifies immutable v1, submitted 14 July 2026 in `cs.AI`, with the comment “KDD 2026 Workshop Agentic AI Evaluation and Trustworthiness”; its summary contains no withdrawal notice. The versioned abstract endpoint returned HTTP 200. The versioned PDF endpoint returned HTTP 404 during scouting, so full-text acquisition remains a review prerequisite.
- The abstract reports replaying completed public task-level records from SWE-bench, AppWorld, and tau-bench. It defines a partial budget as sufficient only when it supports the completed benchmark's pairwise decision, covers required task groups, and keeps unresolved comparisons below a target fraction. Under its strict reported setting, first-sufficient fractions vary from 15% for AppWorld and 25% for tau-bench to 90% for SWE-bench Verified; SWE-bench Lite reportedly fails all targets through 95% under the primary coverage rule. These are author-reported abstract claims, not independently verified results.
- GitHub API verification found the official public MIT-licensed repository live and unarchived. Its mutable `main` head was `1117405cfecdee730e01071d859d3c3383f22711` (commit timestamp 14 July 2026); no tags or GitHub releases were present. Web search exposes data-provenance and reviewer-facing replay/check material, but scouting did not inspect or execute repository files.
- Repository-wide duplicate search found no title or arXiv-ID match. The closest local work is *Efficient Benchmarking of AI Agents* and *Agent Psychometrics*, which optimize or model reduced panels; this candidate instead appears to evaluate preservation of selected pairwise conclusions with explicit group-coverage and unresolved-decision requirements.
- This is **metadata, abstract, endpoint, repository-metadata, release-location, and duplicate triage only**. The paper body, appendices, public records, code, task orders, comparison sets, statistical procedures, sensitivity analyses, and replay outputs were not read or audited. No claim is made that the proposed fractions support prospective early stopping, rank preservation, construct or diagnostic coverage, configured-system reliability, transport to artifact-heavy knowledge work, capability, professional validity, or readiness.

## Why this is distinct

A task fraction is not itself an evaluation guarantee. “Enough” depends on the decision target, minimum effect, task-selection/order policy, coverage requirements, dependence and clustering, allowed unresolved comparisons, missing/invalid records, and whether the completed benchmark is treated as a truth target or merely another finite instrument. Retrospectively reproducing selected pairwise signs can coexist with lost failure-mode coverage, unstable subgroup conclusions, changed rankings, or an invalid full-benchmark decision.

For `skill-bench`, the reusable object is a prospective decision-preservation contract: `full task frame and construct groups → configured-system comparison set → task order/selection policy → minimum decision-relevant difference → partial evidence and missingness → group coverage → paired decision and uncertainty → unresolved allowance → stopping/reporting rule → full-form bridge → bounded use claim`. Artifact-heavy knowledge-work tasks also have dependent rubric checks and heterogeneous costs, so task-level savings may not preserve criterion, domain, severity, or diagnostic coverage.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier scalable agent evaluation) and C (cost-aware benchmark operation and metric machinery).
- **Concrete evidence/artifact:** immutable-v1 full-paper review plus commit-pinned execution/audit of the official public replay package.
- **Uncertainty clarified:** when a partial run preserves a named completed-record pairwise decision, and why that is weaker than preserving rankings, construct/diagnostic coverage, prospective stopping validity, or cross-family transport.
- **Mode:** narrow expansion feeding consolidation/validation; coding and web benchmarks are public replay substrates, not a scope commitment.
- **Duplication check:** adjacent reduced-panel and psychometric reviews answer different selection/rank/difficulty questions; the new review must compare them directly rather than collecting another generic efficiency paper.
- **Useful completion:** reconstruct estimands, order/selection, thresholds, coverage, paired dependence, missingness, uncertainty, sensitivity, and exact replay provenance; retain strict claim ceilings.

Added one task: `review-partial-agent-benchmark-decision-validity` (priority 18). No second task was added.

## Operational note

The required initial `git pull --ff-only` failed because the HTTPS GitHub remote lacks a noninteractive credential (`could not read Username`). Pre-existing untracked source trees and the AgentFootprint release ZIP were not modified.
