# Scouting note — many-facet rater-measurement gap

**Timestamp:** 2026-07-10T23:19:34Z  
**Scope:** Narrow psychometric search against charter objectives A/B/C after confirming two pending consolidation/build tasks and no pending source/research/review work. This run targeted rater-severity and task-difficulty decomposition in scalable grading rather than repeating broad agent-benchmark discovery.

## Substantive finding (triage only)

**Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model**

- Immutable arXiv record: https://arxiv.org/abs/2505.18486v2
- Immutable PDF location: https://arxiv.org/pdf/2505.18486v2
- Authors: Hong Jiao, Dan Song, and Won-Chan Lee.
- arXiv API metadata reports ten LLM configurations compared with human expert raters on two writing-task types, using holistic and analytic scores, quadratic weighted kappa, consistency statistics, and a Many-Facet Rasch model to examine rater effects.
- The candidate is distinct because the local corpus treats judge agreement, expert disagreement, clustered uncertainty, and evidence-view differences, but repository search found no Many-Facet Rasch or generalizability-theory analysis that jointly separates response quality, task/prompt difficulty, and rater severity.
- This is **metadata and abstract triage only**. The full paper and any underlying data, prompts, rubrics, code, or supplements were not read during scouting. No claim is made that its favored models are reliable, interchangeable with experts, operationally suitable, or transferable from educational writing to realistic knowledge work.

## Benchmark implication to test

Aggregate agreement can conceal systematic severity, differential functioning, prompt sensitivity, and disconnected rating designs. A full review can test whether a many-facet measurement treatment adds a reusable validity layer for configured graders: which facets are identifiable, what connectivity and replication are required, whether rater adjustment is defensible, and which variance or fit evidence is needed before pooling human and model judgments.

## Charter decision filter and queue action

- **Objectives advanced:** A (scalable evaluation and expert judgment), B (valid transformation of professional judgment into scores), and C (grader, metric, task-health, and validity records).
- **Evidence/artifact sought:** immutable-v2 full-paper review and audit of any official primary materials, with the design and model reconstructed from page/table evidence.
- **Uncertainty clarified:** whether human scores form a justified criterion; whether model, prompt, task, response, and rater effects are separable; and whether severity adjustment licenses score comparability or operational substitution.
- **Mode/balance:** one narrow expansion task at priority 64, below the two current implementation/consolidation priorities.
- **Duplication/scope:** local search found no record for the paper, its arXiv ID, Many-Facet Rasch, or generalizability theory. AgentRewardBench and plural-judgment work are explicit comparisons. Educational writing is a measurement case, not a domain commitment.
- **Useful completion:** reconstruct and critique the crossed design, metrics, many-facet specification, fit/differential-rater diagnostics, missingness and uncertainty; separate paper from release evidence; and map only nonduplicate requirements into existing machinery.

Added `review-many-facet-human-ai-rater-effects` (priority 64). No second task was added.
