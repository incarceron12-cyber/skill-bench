# Scouting note — requirement-to-model-to-code-to-report validity gap

**Timestamp:** 2026-07-15T19:48:18Z  
**Scope:** Narrow expansion against charter objectives A/B/C. Queue inspection found 290 tasks: 284 completed, four blocked, and two pending; no source, research, review, or claimed backlog remained. Recent scouting has already covered memory, feedback, permissions, privacy, user constraints, procedural transfer, and production evaluation, so this run searched only for an unrepresented cross-artifact professional-work chain.

## Substantive finding — triage only

**Opti-Agent-Bench: Benchmarking End-to-End Optimization R&D Agents on Real-World Business Problems** — Yongchang Fu, Xinjie Huang, Chengjun Dai, Chengzhe Feng, Junshao Zhang, and Hong Zhu; arXiv:2607.10768v1.

- Immutable record: https://arxiv.org/abs/2607.10768v1
- Immutable PDF: https://arxiv.org/pdf/2607.10768v1
- Immutable HTML: https://arxiv.org/html/2607.10768v1
- Paper-associated release found by exact-title search and pinned for review: https://github.com/huiliyi-XJ/Opti-Agent-Bench/tree/6e030101b488226c3b05cb5347b90c0155ca1cf0
- The arXiv API identifies immutable v1 as submitted 12 July 2026. Its abstract contains no withdrawal or retraction notice, and all three versioned arXiv endpoints returned HTTP 200 during scouting.
- The abstract defines an end-to-end chain from business-language requirements through problem understanding, mathematical modeling, algorithm/implementation, and report generation. It claims anti-template semantic traps, modular evaluation, cross-module consistency checks, and an ORAC framework that addresses both task and scoring validity. It names constraint omission, model–code inconsistency, and report–implementation divergence as observed failure modes. These are author-reported abstract claims, not independently verified findings.
- Structural inspection of immutable-v1 HTML—not a full reading—confirmed sections on the formulation gap, ORAC validity, four evaluation modules, partial-module evaluation, cross-module metrics, task design, evaluator-agent architecture, failure taxonomy, and appendices with example tasks, rubrics, references, and expected failures.
- The immutable HTML did not expose the benchmark repository. Exact-title search located the repository above; GitHub API metadata identifies it as created after arXiv v1, with pinned head `6e030101b488226c3b05cb5347b90c0155ca1cf0` dated 15 July 2026. Root inventory exposes tasks, pipeline, scripts, results, documentation, and separate code/data licenses. Its pinned README identifies 11 open tasks plus one holdout, four pipeline stages, retained aggregate paper tables, withheld raw transcripts/robustness dumps, and partially withheld reference/holdout material. Only this README and root metadata were inspected; no task, solver, rubric, checker, result, or pipeline code was read or executed.
- Repository-wide exact-title, arXiv-ID, and distinctive-phrase searches found no local review or queue task. Closest completed work—DORA, SciAgentArena, ResearchClawBench, SOP-Bench, BigFinanceBench, and the artifact/evidence-chain machinery—covers adjacent pipelines but not business requirement → formal model → executable implementation → stakeholder report consistency as the primary instrument.
- This is **metadata, abstract, endpoint, section-structure, release-location, root-inventory, pinned-README, and duplicate triage only**. The paper body, appendices, tasks, data, formulations, solvers, holdout, hidden truth, evaluator prompts, rubrics, checkers, outputs, transcripts, tables, statistics, costs, and source code were not read or audited. No claim is made that the business problems are authentic, task semantics are complete, ORAC is valid, cross-module checks are independent, implementations solve the intended problems, reports are decision-useful, results reproduce, or the benchmark establishes optimization expertise, professional validity, capability, production fitness, or readiness.

## Why this is distinct

The reusable chain is `business demand and authority → natural-language requirement and ambiguity → formal variable/objective/constraint claim → executable implementation and solver state → result evidence → report proposition and limitation → cross-artifact consistency → recipient decision/use → professional consequence`. A benchmark can score each artifact locally while still missing a contradiction between artifacts; conversely, consistency with one authored formulation can preserve a mistaken requirement interpretation. Anti-template traps may test requirement reading, but they can also become recognizable authored cues. An evaluator agent may inspect semantic alignment while sharing task-author assumptions and incomplete evidence views.

A full audit should separate demand provenance, requirement authority, formulation completeness, accepted alternatives, code executability, solver/reference correctness, local module quality, cross-module entailment, report evidence and limitations, evaluator calibration, hidden/reference leakage, invalid/retry denominators, release correspondence, recipient utility, and transport. Existing provenance, artifact-view, composite-workflow, rubric, metric, task-health, trace, and validity machinery should host any reusable lessons unless an exercised nonduplicate gap is proven.

## Charter decision filter and queue action

- **Objectives advanced:** A (realistic knowledge-work benchmark frontier), B (domain requirements transformed into explicit formal and artifact claims), and C (cross-artifact checks and executable outcomes).
- **Concrete evidence/artifact:** immutable-v1 deep review plus a timing-aware audit of the pinned post-v1 release.
- **Uncertainty clarified:** whether modular and cross-module scoring validly measures requirement translation across professional artifacts, or primarily co-authored reference/evaluator agreement.
- **Mode:** narrow expansion feeding later consolidation; optimization R&D is a bounded test of cross-artifact semantic consistency, not a permanent domain choice.
- **Duplication/scope:** no exact local duplicate; mandatory comparison with DORA, SciAgentArena, ResearchClawBench, SOP-Bench, BigFinanceBench, and existing artifact/evidence-chain machinery prevents parallel infrastructure.
- **Useful completion:** a claim ladder and failure taxonomy separating demand, requirement, formulation, implementation, report, cross-artifact consistency, recipient use, professional validity, production fitness, and readiness, grounded in exact paper/release locators.

Added one low-priority task: `review-opti-agent-bench-cross-module-validity` (priority 5). The consented expert micro-pilot and pending request-receipt consolidation remain substantially higher priority.
