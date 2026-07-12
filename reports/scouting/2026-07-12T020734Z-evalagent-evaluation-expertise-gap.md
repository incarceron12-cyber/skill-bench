# Scouting note — evaluation-expertise automation gap

**Timestamp:** 2026-07-12T02:07:34Z  
**Scope:** Narrow expansion against charter objectives A/B/C. Repository inspection found 132 completed tasks, no pending or claimed work, and one blocked real-elicitation task. Existing benchmark, grader, and expertise-transfer coverage is strong, so this run targeted a specific missing link: whether evaluation-domain expertise can be encoded into reusable skills that produce executable agent-evaluation artifacts.

## Substantive finding (triage only)

**An Empirical Study of Automating Agent Evaluation**

- arXiv record: https://arxiv.org/abs/2605.11378
- PDF: https://arxiv.org/pdf/2605.11378
- Search metadata identifies Kang Zhou and collaborators and describes EvalAgent as combining procedural instructions, reusable code/templates, and dynamically retrieved API documentation in a trace-based pipeline that produces metrics and executable evaluation artifacts.
- This is directly relevant because the corpus separately covers expert procedural skills, rubric authoring, judge reliability, task generation, and production eval lifecycles, but no review currently audits an empirical system that attempts to encode evaluator expertise and automate construction of the evaluation itself.
- Repository-wide duplicate search found no title or arXiv `2605.11378` match.
- This is **metadata/search-result triage only**. The PDF, appendices, experiments, repository, skills, generated code, tests, examples, and release were not read or inspected. The official implementation URL must be identified from the paper and pinned during review. No claim is made about grader validity, evaluator equivalence, expertise transfer, cost reduction, reliability, reproducibility, scalability, or cross-domain generalization.

## Benchmark implication to test

A full paper-and-release audit should separate at least five claims: generated artifact completeness, executable conformance, agreement with a reference evaluator, preservation of the intended construct, and transfer of evaluation-domain expertise. It should determine which skill components contribute under ablation, whether generated checks fail safely, how human/reference judgments were established, and whether errors reveal missing tacit evaluation knowledge or ordinary code-generation failures. The transferable output is a cross-domain evaluator-expertise-to-instrument boundary, not a commitment to automated grading or a coding-only benchmark.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier evaluation systems), B (expertise-to-evaluation transformation), and C (scalable executable evaluation machinery).
- **Evidence/artifact sought:** immutable full-paper review plus pinned official-release audit with page/file locators.
- **Uncertainty clarified:** whether reusable evaluation skills preserve domain knowledge and construct meaning, versus merely improving evaluator-code completion.
- **Mode/balance:** narrow expansion; the ready queue was empty.
- **Duplication/scope:** no repository duplicate; adjacent sources cover components but not automated evaluator assembly. The general hypothesis is cross-domain and must not narrow the project to coding.
- **Useful completion:** reconstruct inputs, skill components, artifacts, tasks, baselines/ablations, reference judgments, executable tests, failure taxonomy, cost, and release evidence; explicitly bound conformance, validity, expertise-transfer, equivalence, and scalability claims.

Added `review-evalagent-domain-evaluation-skill-validity` (priority 52). No second task was added.
