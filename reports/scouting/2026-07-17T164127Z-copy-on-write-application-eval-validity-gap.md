# Scouting note — copy-on-write application-evaluation validity gap

- **Timestamp:** 2026-07-17T16:41:27Z
- **Evidence status:** arXiv API metadata/abstract, immutable endpoint checks, exact repository duplicate search, arXiv HTML link triage, and GitHub API repository/tree triage only. The paper body, libraries, application fork, released result archive, tasks, agent traces, scores, interventions, and statistical analyses were **not** deeply read, executed, or audited during scouting.

## Substantive candidate — triage only

**Copy-on-Write Scoring: Application-Specific Agent Evaluations** — Joanna Roy and Sven Hoelzel; arXiv:2607.14336v1.

- Immutable record/PDF/HTML: https://arxiv.org/abs/2607.14336v1 · https://arxiv.org/pdf/2607.14336v1 · https://arxiv.org/html/2607.14336v1
- Official library: https://github.com/trail-ml/agent-cow-python at inspected commit [`3376d3e06b8855c2e1a2d62606725ef7512d21b6`](https://github.com/trail-ml/agent-cow-python/commit/3376d3e06b8855c2e1a2d62606725ef7512d21b6)
- Official Plane application fork/results: https://github.com/JoannaRoy/plane-cow at inspected preview commit [`46d48a94029ce097e3331875bd6714b37ea3ae70`](https://github.com/JoannaRoy/plane-cow/commit/46d48a94029ce097e3331875bd6714b37ea3ae70)
- The arXiv API identifies a `cs.SE`/`cs.AI` v1 submitted 15 July 2026. Its summary contains no withdrawal/retraction notice. The immutable record, PDF, and HTML returned HTTP 200; the PDF response reported `application/pdf` and 827,936 bytes.
- The abstract proposes PostgreSQL-level copy-on-write isolation so agents can operate in an application environment while producing session- and operation-level scores. It reports a Plane project-management demonstration in which tool-surface findings were followed by fixes and measured improvements. These are author-stated abstract claims awaiting full-paper and release audit.
- The MIT library was public, unarchived, and exposed an untruncated 55-object tree with PostgreSQL, blob, scoring, examples, and test modules. The Plane fork was public and unarchived under AGPL-3.0; its untruncated 6,150-object preview tree included agent/application code and a 538,236-byte `results.zip`. Repository presence and file counts establish inspectability only, not successful reproduction or agreement with paper results.
- Exact searches for the title, arXiv ID, and method name found no prior local review, queue task, or scouting note.

## Why this is a narrow, useful gap

The corpus already covers synthetic application replicas and native-state predicates (AutomationBench, SaaS-Bench, WorkArena), matched transition transport, action-boundary effects, evaluator retry, and production trajectory review. It does not directly audit the proposed **in-application write-isolation chain**:

`application/version and parent state → task and authorized effect → agent session → reads and attempted operations → database overlay writes → non-database/collateral effects → operation matching → session score → diagnosed tool-surface defect → intervention → matched rerun → held-out workflow and production consequence`.

Copy-on-write can be valuable cross-domain machinery because it may reduce replica drift while retaining realistic application logic and making state deltas inspectable. But database isolation does not automatically cover caches, queues, background jobs, object stores, emails, network calls, clocks, concurrency, transaction ordering, permission boundaries, or external side effects. A matched row-level write may not establish semantic workflow correctness, and an improved post-fix score may bundle changed tools, tasks, prompts, data, or run conditions unless the intervention contrast is frozen. Session/operation scores also require explicit intended, eligible, valid, substantive, and repeated denominators before they support reliability or deployment claims.

Plane is a bounded demonstration for reusable state-observation and evaluation infrastructure, not a proposal to narrow `skill-bench` to project management, PostgreSQL applications, or API agents.

## Charter decision filter and queue action

- **Objectives advanced:** A (production agent evaluation), B (valid state/observer/intervention claims), and C (realistic environment, state-delta, and grader machinery).
- **Concrete evidence:** immutable-v1 full-paper review plus pinned release audit and smallest feasible reproduction across the library, Plane fork, and result archive.
- **Uncertainty clarified:** when database copy-on-write supports isolated application-operation conformance and actionable diagnosis, and what additional observer, side-effect, repetition, intervention, transport, and consequence evidence is required.
- **Mode:** narrow expansion. The queue had one pending human prerequisite and three fail-closed blocked builds but no review backlog; one review task adds a distinct executable production mechanism without restarting broad search.
- **Duplication/scope check:** adjacent work covers replicas, synthetic transport, selected native-state observers, and production retries, but not direct application execution through a database overlay. No schema is proposed unless the audit shows existing environment/state/trace/validity contracts are insufficient.
- **Useful completion:** section/page/path-grounded method and release audit; isolation/reset and observer-coverage analysis; exact task/intervention denominators; reproduction status; and nonduplicate retain/repair/test implications while keeping conformance, workflow correctness, causal diagnosis, repair benefit, reliability, safety, professional validity, production fitness, and readiness separate.

Added one task: `review-copy-on-write-application-eval-validity` (review, priority 69). No other candidate was queued. `AI Agents Do Not Fail Alone: The Context Fails First` (arXiv:2607.14275v1) was triaged but not added because its abstract-level context-quality claim overlaps existing configured-system, context-governance, criterion-validity, and grader-consensus coverage; a future scout should add it only if a release audit reveals distinct causal or predictive-validity evidence rather than another context checklist.
