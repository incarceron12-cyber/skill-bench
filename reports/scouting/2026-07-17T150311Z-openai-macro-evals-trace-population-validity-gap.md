# Scouting note — macro-eval trace-population validity gap

- **Timestamp:** 2026-07-17T15:03:11Z
- **Evidence status:** official OpenAI Cookbook page, README, notebook markdown, GitHub API tree, and aggregate run-summary triage only. The notebook was **not** executed during scouting; the 36.9 MB trace archive, 992 trace bundles, saved lower-level labels, helper implementations, generated outputs, individual traces, clustering results, and diagnosis rows were not deeply audited.

## Substantive candidate — triage only

**Macro Evals for Agentic Systems** — OpenAI Cookbook; Shikhar Kwatra, Will Thieme, and Bradley Strauss; published 19 May 2026.

- Official rendered notebook: https://developers.openai.com/cookbook/examples/partners/macro_evals_for_agentic_systems/macro_evals_for_agentic_systems
- Immutable official release: https://github.com/openai/openai-cookbook/tree/0075904c509819f8d746794001a7a27066258956/examples/partners/macro_evals_for_agentic_systems
- The path's latest inspected commit is [`0075904c509819f8d746794001a7a27066258956`](https://github.com/openai/openai-cookbook/commit/0075904c509819f8d746794001a7a27066258956), dated 20 May 2026. The parent repository is public, unarchived, and MIT-licensed.
- The pinned tree contains the notebook and README, two helper modules, requirements/runner files, 2.69 MB of saved labels, 2.03 MB of trace results, a 36.9 MB trace archive, and an aggregate run summary. The README says the package runs offline without an API key from synthetic exported traces and saved Promptfoo labels; the full SQLite trace snapshot and original live label rerun are not included.
- The notebook describes a synthetic EV-order multi-agent workflow, lower-level grading, trace-to-document compression, BERTopic-style recurring-pattern discovery, prevalence/severity ranking, slice lift, and an AgentTrace-style backward suspect score. It repeatedly labels clusters and suspect scores as triage rather than proof of defects or causality.
- The aggregate summary declares 1,000 intended runs: 767 accepted, 213 completed, 10 blocked, 2 failed, and 8 runner errors. Notebook text says 992 runs are bundle-backed. It also records mixed agent versions, 14 generated scenario classes, 83 trace families, automatic review approval, and uneven specialist activation. These are released-record observations, not validated performance or production claims.
- Exact local searches found no prior dedicated review, queue task, or scouting note for this source or method.

## Why this is a narrow, useful gap

The corpus already covers selection-aware trajectory sampling (Signals), open-vocabulary issue compression (Agentic CLEAR), supported root localization (STRACE), exact-prefix intervention (Who&When Pro), and production-practitioner evidence. This source composes those concerns into a distinct production-facing chain:

`eligible run population → retained/valid trace bundle → lower-level label → compressed evidence document → selected focus population → embedding/reduction/cluster → pattern label → prevalence/severity rank → slice concentration → representative trace → backward suspect score → human confirmation → repair → held-out outcome`.

Every transformation can change the licensed claim. Selecting only failure/review-bearing traces prevents cluster shares from becoming deployment prevalence. Saved labels can be useful inputs without being calibrated truth. Document compression defines what clustering can observe. Cluster count, noise treatment, random seeds, and version mixtures can change pattern identity. Frequency × severity is a triage policy, not a universal risk or business-loss function. Temporal proximity and graph centrality can nominate inspection targets without identifying causal roots. Human confirmation, intervention, held-out recurrence, and operational consequence are later missing or separately required joins.

The EV scenario is a bounded synthetic example for reusable trace-population evaluation, not a proposal to narrow `skill-bench` to automotive operations or multi-agent swarms.

## Charter decision filter and queue action

- **Objectives advanced:** A (production agent evaluation), B (valid trace-to-diagnosis claims), C (trace/evidence/metric machinery), and D (connect adjacent reviewed methods rather than adding another isolated source).
- **Concrete evidence:** immutable release audit, clean offline execution, exact denominator and provenance checks, stability/mutation analysis, and a source-grounded research review with retain/repair/test implications.
- **Uncertainty clarified:** when population trace analysis supports an investigation queue, and what additional evidence is needed for defect prevalence, causal root, repair benefit, operational reliability, professional validity, or business consequence.
- **Mode:** narrow expansion with a required consolidation comparison. One priority-97 build and one priority-95 human prerequisite were already pending; this task is priority 64 and does not displace them.
- **Duplication/scope check:** adjacent reviews cover individual links, not this released end-to-end composition. No new schema is proposed unless the audit proves existing trace, metric, task-health, and validity records insufficient.
- **Useful completion:** notebook reproduction from the pinned commit; exact file/code/result evidence; selection, missingness, compression, clustering, ranking, diagnosis, and human-confirmation limits; and falsification tests that preserve investigation utility without promoting triage signals into unsupported production claims.

Added one task: `research-openai-macro-evals-trace-population-validity` (research, priority 64). No other candidate was queued.
