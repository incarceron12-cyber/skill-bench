# Scouting note — PM-LLM process-analysis validity gap

- **Timestamp:** 2026-07-16T21:19:35Z
- **Evidence status:** arXiv API metadata/abstract, endpoint checks, repository metadata, current README triage, and local corpus/queue duplicate checks only. The full paper, benchmark prompts, outputs, leaderboards, and evaluator code were **not** deeply read or audited during scouting.

## Substantive candidate — triage only

**PM-LLM-Benchmark: Evaluating Large Language Models on Process Mining Tasks** — Alessandro Berti, Humam Kourani, and Wil M. P. van der Aalst, arXiv:2407.13244v1.

- Immutable record: https://arxiv.org/abs/2407.13244v1
- Immutable PDF: https://arxiv.org/pdf/2407.13244v1
- Official release: https://github.com/fit-alessandro-berti/pm-llm-benchmark
- The arXiv API reports one version submitted 18 July 2024 in `cs.CL`/`cs.DB`; its abstract contains no withdrawal notice. The immutable record, PDF, and repository endpoints returned HTTP 200.
- The abstract describes a benchmark of process-mining-specific and process-specific knowledge and flags public-data constraints and LLM-evaluator bias. It claims most tested models perform some tasks satisfactorily while tiny edge models remain inadequate, but also says evaluator bias prevents a thorough ranking. These are author claims awaiting full-paper verification.
- GitHub identifies a non-fork GPL-3.0 repository, currently at `483fef81cf90766582541db7ec47dc9e9d5899d6` on `main` (verified by `git ls-remote`). The current README labels the release **v2.2**, explicitly says its prompts differ from paper-described v1, lists eight categories, uses a 1–10 expert-LLM judge and summed score, and exposes multiple judge-specific historical leaderboards. File existence and README descriptions do not establish implementation correctness, paper conformance, criterion authority, or score comparability.

## Why this is a narrow, useful gap

The reviewed corpus covers workflow execution, native-state conformance, professional artifacts, scientific analysis, production-derived tasks, generated judges, and benchmark lifecycle drift. Exact title/ID and process-mining searches found no existing review or queue task. This source is distinct because it evaluates a professional analyst work shape over event logs and process models, including inquiry/hypothesis generation, anomaly/conformance analysis, model construction, fairness analysis, and process recommendations—not merely execution of a prescribed workflow.

The reusable validity chain is:

`event-log/process source and authority → process/domain knowledge requirement → analyst inquiry or model/analysis artifact → accepted alternatives and executable/semantic checks → judge evidence view and criterion authority → heterogeneous category score → versioned leaderboard → analytical-quality or model-adequacy claim`.

A plausible narrative can be process-invalid; executable syntax can encode the wrong process; a useful hypothesis need not match one reference; and judge agreement does not establish analyst usefulness. Release v1→v2.2 and judge-specific leaderboard changes also make task, criterion, and scale drift a first-class comparison problem.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier benchmark research) and B (domain expertise-to-evaluation methodology).
- **Concrete evidence:** immutable-v1 full-paper review plus exact-commit release/history audit.
- **Uncertainty clarified:** what process/domain knowledge, event-log inquiry, model construction, recommendation quality, and LLM-judge scores can validly establish; whether scores remain comparable across task and judge versions.
- **Mode:** narrow expansion feeding consolidation; the queue already contains a higher-priority build and a human prerequisite, so this task is intentionally low priority.
- **Duplication/scope check:** no duplicate source or equivalent event-log analyst benchmark review found. Process mining is a bounded work shape for cross-domain source-to-analysis and judge-validity questions, not a permanent scope choice.
- **Useful completion:** reconstruct task/output/criterion units, source provenance, accepted alternatives, evaluator bias and dependence, aggregation, uncertainty, paper-release conformance, and version-specific claim ceilings before proposing machinery.

Added one task: `review-pm-llm-domain-process-analysis-validity` (priority 6). No full-paper claim or implementation task was added.
