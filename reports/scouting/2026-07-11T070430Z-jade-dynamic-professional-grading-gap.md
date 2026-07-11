# Scouting note — expert-grounded dynamic professional grading gap

**Timestamp:** 2026-07-11T07:04:30Z  
**Scope:** Narrow expansion against charter objectives A/B/C after confirming 84 completed tasks, three pending consolidation/build tasks, one blocked real-elicitation task, and no pending source/research/review work. This run targeted scalable grading of open-ended professional artifacts rather than repeating broad agent-benchmark discovery.

## Substantive finding (triage only)

**JADE: Expert-Grounded Dynamic Evaluation for Open-Ended Professional Tasks**

- Immutable arXiv v1 record: https://arxiv.org/abs/2602.06486v1
- Immutable PDF: https://arxiv.org/pdf/2602.06486v1
- Official repository: https://github.com/smiling-world/JADE
- Search-indexed arXiv metadata describes a two-layer evaluator: predefined expert-knowledge “evaluation skills” provide stable criteria, while response-specific criteria adapt to the submitted artifact. Reported experiments use BizBench and transfer subsets from HealthBench and DR.BENCH; the official repository exposes BizBench task data, evaluation configuration, and score-fusion controls.
- This directly targets an unresolved skill-bench tension: static rubrics can miss legitimate response-specific content, while unconstrained holistic judges can be unstable, weakly traceable, and cue-sensitive. It is distinct from the local rubric-modification/rater-effect reviews, artifact-view admissibility, and deterministic provenance graders because it explicitly combines fixed expert criteria with generated, answer-conditioned checks.
- This is **abstract/search-result and repository-description triage only**. The paper, appendices, code, prompts, task files, results, and release history were not read during scouting. No claim is made that JADE’s generated criteria are valid, non-leaky, reproducible, expert-equivalent, construct-preserving, or safe for consequential professional evaluation.

## Benchmark implication to test

A full audit should determine whether dynamic checks discover genuinely necessary response-specific obligations or merely reward evaluator-model preferences; whether they are grounded in public task basis and trusted evidence; whether fixed and generated layers double-count criteria; how fusion weights, judge seeds, and model identity affect decisions; and whether reported expert alignment evaluates criterion validity, score agreement, rank agreement, or only correlation. The released BizBench examples provide an inspectable test of how expert knowledge is encoded and whether evidence/credibility dimensions remain separable from correctness.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier professional-agent evaluation), B (expertise-to-grader transfer), and C (plural, scalable grading infrastructure).
- **Evidence/artifact sought:** immutable-v1 full-paper review plus pinned official-release audit reconstructing expert-skill provenance, dynamic-criterion generation, evidence requirements, fusion, calibration, baselines, uncertainty, and transfer claims with page/file evidence.
- **Uncertainty clarified:** whether a fixed-expert/dynamic-response evaluator can add fair diagnostic coverage without answer-conditioned construct drift, shared judge cues, hidden obligations, or unstable score fusion.
- **Mode/balance:** one narrow expansion task at priority 60; the ready queue is consolidation/build-only and no source/research/review task is pending.
- **Duplication/scope:** repository-wide search found no `JADE`, title, or arXiv-ID match. Business and health tasks are methodological cases, not domain commitments.
- **Useful completion:** inspect representative BizBench tasks and every evaluator stage; distinguish authored expert authority from model-generated criteria; reproduce a small no-cost evaluation if feasible; preserve all release, sample, agreement, and generalization limits; map only nonduplicate implications to existing contracts.

Added `review-jade-dynamic-professional-grading` (priority 60). No second task was added.
