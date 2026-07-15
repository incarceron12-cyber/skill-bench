# Scouting note — production evaluation selective re-execution gap

**Timestamp:** 2026-07-15T06:37:23Z  
**Scope:** Narrow expansion against charter objectives A/C. Queue inspection found 253 tasks: 246 completed, four blocked, two pending human decisions, and one pending consolidation; no source/research/review task remained. Existing reviews cover production measurement, offline/online metric association, task-health lifecycle, judge reliability, partial benchmark decisions, and signal-enriched review sampling, but not record-level schema-failure recovery in a high-throughput governed evaluation pipeline.

## Substantive finding — triage only

**Operationalising Multi-Dimensional Evaluation for Conversational Agents: A Scalable, Governed Pipeline with Selective Re-evaluation and Model Benchmarking** — Niranjan Kumar M, Balaji Nagarajan, Karthik Nair, Faysal Satter, and Nithin Surendran, arXiv:2607.12085v1.

- Immutable record: https://arxiv.org/abs/2607.12085v1
- Immutable PDF target: https://arxiv.org/pdf/2607.12085v1
- Immutable HTML: https://arxiv.org/html/2607.12085v1
- The arXiv API identifies immutable v1, submitted 13 July 2026 in `cs.AI`, with no withdrawal notice in the summary. At scouting time the versioned abstract and HTML endpoints returned HTTP 200, while the versioned PDF endpoint returned HTTP 404.
- The abstract describes a configuration-driven production pipeline over retail-chatbot logs with normalization, sharding, asynchronous execution, schema-constrained scoring, versioned configuration, validation logs, and record-level provenance. Its “selective re-evaluation” is explicitly restricted to incomplete, malformed, or schema-invalid records rather than outcome-based rerunning.
- The authors report approximately 50,000 processed records per day, more than two million evaluated interactions, and validation on 12,980 stratified-random human-labeled records from four trained annotators. They report macro F1 of 0.93 and 89% human-acceptability accuracy for translation. These are author-reported abstract claims, not independently verified results.
- The canonical abstract page exposes no author-owned code, data, configuration, annotation guide, run corpus, or project link. Exact-title/code web search found no official implementation surface. A full review must verify whether the HTML or references provide a reproducible release and reconstruct the evaluation target and denominators.
- Repository-wide duplicate search found no title or arXiv-ID match. The closest local work is *Measuring Agents in Production*, the Nubank offline/online evaluation review, Anthropic's task-health lifecycle, Signals trajectory triage, and the partial benchmark decision audit. This candidate appears distinct because it treats schema validity, record identity, and retry eligibility as governed operational state at production volume.
- This is **metadata, abstract, endpoint, link-location, and duplicate triage only**. The paper body, tables, annotation protocol, rater agreement, split construction, model configurations, score prompts, schema, failure distribution, costs, and pipeline implementation were not read or audited. No claim is made that the reported metrics establish conversational quality, production utility, causal system improvement, agent capability, professional validity, reliability, or readiness.

## Why this is distinct

Selective re-evaluation can be legitimate recovery or an outcome-conditioned source of bias. The reusable boundary is `immutable record and configured evaluator identity → typed execution/schema status → retry eligibility fixed without outcome access → retained attempts and costs → valid observation → human-reference comparison → bounded operational use`. A malformed-output retry must not silently become a second chance after a substantive failure; asynchronous sharding must not duplicate, omit, or mix configuration versions; and a high aggregate judge metric must not substitute for criterion-, subgroup-, intent-, or decision-threshold calibration.

For `skill-bench`, this could sharpen existing trial, task-health, metric, and provenance machinery without creating a conversational-agent subsystem. Artifact-heavy evaluations also experience parser failures, missing evidence views, invalid environments, and grader schema errors. The relevant question is whether a production system cleanly separates service/execution validity from substantive failure and preserves every attempt, rather than whether its retail domain should shape benchmark scope.

## Charter decision filter and queue action

- **Objectives advanced:** A (production agent evaluation evidence) and C (operational trial, provenance, retry, and metric machinery).
- **Concrete evidence/artifact:** immutable-v1 full-text review reconstructing record identity, configuration/version control, schema lifecycle, retry policy, human-validation design, missingness, cost, and claim limits; release audit if an official artifact is located.
- **Uncertainty clarified:** when selective re-execution repairs evaluator invalidity without outcome-conditioned retries or denominator drift, and what the reported human comparison actually validates.
- **Mode:** narrow expansion feeding consolidation/validation; retail conversation is only a production-scale stress case, not a scope commitment.
- **Duplication check:** adjacent local sources address portfolio practices, offline/online association, task health, review sampling, or reduced-task decisions—not record-level invalidity recovery and configuration-safe asynchronous evaluation at reported production scale.
- **Useful completion:** compare directly with those sources; preserve strict boundaries among schema validity, substantive criterion outcome, judge agreement, human acceptability, operational throughput, downstream utility, and readiness; propose no new schema unless a non-overlapping contract gap remains.

Added one task: `review-production-eval-selective-reexecution-validity` (priority 17). No second task was added.

## Operational note

The required initial `git pull --ff-only` failed because the HTTPS GitHub remote lacks a noninteractive credential (`could not read Username`). Local `main` was 96 commits ahead of `origin/main` before this scouting change. Pre-existing untracked paper source trees and the AgentFootprint release ZIP were not modified.
