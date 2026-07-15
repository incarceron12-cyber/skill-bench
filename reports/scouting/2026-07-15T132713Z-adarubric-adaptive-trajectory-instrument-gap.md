# Scouting note — adaptive trajectory-rubric validity gap

**Timestamp:** 2026-07-15T13:27:13Z  
**Scope:** Narrow expansion against charter objectives A/B/C. Initial queue inspection found 269 tasks: 265 completed, three blocked, one pending human prerequisite, and no source, research, or review backlog. The corpus already covers expert-written rubrics, generated-rubric score alignment, model-judge reliability, rater effects, dynamic criteria, and criterion operating envelopes, so this run searched only for an empirical adaptive-instrument design rather than repeating broad grader discovery.

## Substantive finding — triage only

**AdaRubric: Task-Adaptive Rubrics for Reliable LLM Agent Evaluation and Reward Learning** — Liang Ding; arXiv:2603.21362v3.

- Immutable current record: https://arxiv.org/abs/2603.21362v3
- Immutable current PDF: https://arxiv.org/pdf/2603.21362v3
- Paper-linked repository: https://github.com/alphadl/AdaRubrics
- The arXiv API identifies v3 as current, originally submitted 22 March 2026 and updated 10 May 2026 in `cs.AI` and `cs.CL`, with the comment “KnowFM @ ACL 2026.” Its summary contains no withdrawal or retraction notice. The versioned abstract, PDF, and HTML endpoints and linked repository returned HTTP 200 during scouting; the repository HEAD resolved to `d16cd65944c190c1daa6a46e11ce8b104178b85e` but was not audited or established as the paper snapshot.
- The abstract describes an LLM-generated task-specific rubric, step-wise per-dimension trajectory scoring with confidence weighting, three filters including `DimensionAwareFilter`, and dense preference-learning rewards. It reports tests on WebArena, ToolBench, and AgentBench, zero-shot transfer to SWE-bench, and multimodal extension to VisualWebArena and OSWorld.
- The abstract reports Pearson `r = 0.79` against human rankings, Krippendorff’s alpha `= 0.83`, and DPO task-success gains of 6.8–8.5 percentage points. These are author-reported abstract claims, not independently verified findings. Correlation, inter-call agreement, criterion authority, threshold decisions, and downstream treatment effects are different estimands.
- Structural inspection of immutable-v2 HTML—not a full reading—confirmed sections on adaptive rubric generation, step-level scoring, confidence aggregation, filtering, human correlation, repeated-call reliability, ablations, preference learning, cross-domain/multimodal tests, rubric examples, limitations, and theoretical analysis. The reviewer must use current v3 and inspect version changes rather than relying on this structural lead.
- Repository-wide exact-title and arXiv-ID search found no local source, review, or queue task. The closest completed review is `papers/agent-benchmarks/2026-07-15-llm-generated-rubric-meta-evaluation.md`, which studies induced aggregate-score alignment over paper-replication repositories, not adaptive trajectory dimensions, repeated scoring, human rankings, or downstream preference filtering.
- Search also surfaced *An Empirical Study of Automating Agent Evaluation* (`2605.11378`), but it was rejected as a duplicate because the full v2 paper and official Agent-EvalKit release are already deeply reviewed locally.
- This is **metadata, abstract, endpoint, section-structure, release-location, and duplicate triage only**. The v3 body, appendices, tables, prompts, trajectory samples, human annotations, statistics, training/evaluation splits, code, repository history, experiments, costs, and release correspondence were not read or audited. No claim is made that generated dimensions are authorized or complete, confidence is calibrated, step scores observe valid evidence, alpha measures fixed-instrument reliability, filtering prevents consequential masking, DPO gains are caused by rubric quality, or the method supports general evaluator validity, professional judgment, cross-domain transport, production fitness, or readiness.

## Why this is distinct

The reusable chain is `public task and authority → generated dimension/criterion → criterion applicability and accepted alternatives → trajectory evidence view at each step → configured judge call and confidence signal → dimension/step aggregation → hard-gate or compensatory filter → human criterion/decision comparison → training-pair selection → held-out agent outcome`. Each link can fail independently.

AdaRubric may add stronger empirical evidence than generated-rubric plausibility or five-output score correlation because it reportedly includes expert rankings, repeated calls, interactive trajectories, filters, and downstream training. But the same task description may co-author both criterion and score; inter-run alpha may hold trajectories and generated rubrics differently than claimed; aggregate rank correlation can hide mandatory-criterion errors; and training-pair selection plus evaluation on related families can conflate instrument quality with reward shaping and shared lineage. A full audit should freeze the call topology and distinguish fixed-trajectory/fixed-rubric, fixed-trajectory/regenerated-rubric, and rerun-agent variance.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier grader research), B (task-to-criterion transfer), and C (validated evaluation machinery).
- **Concrete evidence/artifact:** immutable-v3 deep review plus exact-commit official-release audit and a comparison against existing generated-rubric, judge-reliability, rater, and criterion-envelope evidence.
- **Uncertainty clarified:** whether task-adaptive rubric generation improves criterion/decision validity or only judge–human aggregate association and training utility under one configured pipeline.
- **Mode:** narrow expansion/validation; web/tool agents and reward learning are comparator settings, not scope commitments.
- **Duplication/scope:** no local AdaRubric duplicate; EvalAgent was explicitly rejected as already covered. Existing schemas should be reused unless full evidence demonstrates a missing primitive.
- **Useful completion:** separate adaptability, criterion authority/completeness, evidence-view validity, inter-call repeatability, human agreement, threshold/decision equivalence, reward usefulness, transport, cost, and readiness.

Added one task: `review-adarubric-adaptive-trajectory-instrument-validity` (priority 8). The consented human elicitation prerequisite remains much higher priority.

## Operational note

The required initial `git pull --ff-only` succeeded. Pre-existing untracked paper-source, release, and site files were not touched.
