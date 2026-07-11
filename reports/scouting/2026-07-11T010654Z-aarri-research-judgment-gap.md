# Scouting note — research-lifecycle judgment and stopping gap

**Timestamp:** 2026-07-11T01:06:54Z  
**Scope:** Narrow search against charter objectives A/B/C after confirming 74 completed tasks, three pending tasks (two consolidation and one dependency-gated replication), one blocked elicitation build, and no pending source/research/review work. This run targeted realistic knowledge work in which context sensitivity, independent judgment, stopping, and collaboration matter, rather than repeating broad benchmark discovery.

## Substantive finding (triage only)

**Act As a Real Researcher: A Suite of Benchmarks Evaluating Frontier LLMs and Agentic Harnesses in Research Lifecycle (AARRI-Bench)**

- Immutable arXiv record: https://arxiv.org/abs/2606.07462v1
- Immutable PDF location: https://arxiv.org/pdf/2606.07462v1
- Official public task repository: https://github.com/AARR-bench/AARRI-bench
- Web-indexed arXiv metadata describes AARRI-Bench as a suite for research-intern activities with both end-to-end research evaluation and fine-grained process assessment. The official repository describes its targets as context sensitivity, independent judgment, knowing when to quit, and collaboration; indexed task examples include data awareness, citation-cascade tracing, dead-end escape, and area-chair judgment.
- This is distinct from the local broad occupational/task-validity reviews, KWBench's unprompted problem recognition, long-horizon execution reliability, and expert-rubric work. It appears to combine professional research artifacts with stopping, provenance, context, and judgment interventions in a released containerized task suite.
- This is **metadata, search-result, and repository-description triage only**. The full paper, appendices, task files, graders, containers, results, human baselines, and release history were not read during scouting. No claim is made that the tasks are representative of research work, expert-authored, professionally valid, contamination-resistant, fairly hidden, reproducible, or correctly graded.

## Benchmark implication to test

Research competence may require more than completing a named workflow: an agent must recognize evidence defects, abandon unproductive paths, decide when evidence is sufficient, preserve citation lineage, and coordinate judgments. A full audit should determine whether AARRI-Bench operationalizes these as fair, observable professional consequences or as benchmark-specific traps; whether end-to-end and process scores remain separate; whether alternate valid research paths are accepted; and whether the public release exposes answer-bearing artifacts or grader assumptions.

## Charter decision filter and queue action

- **Objectives advanced:** A (realistic knowledge-work frontier), B (expert judgment into fair task/check primitives), and C (artifact/process/trace evaluation).
- **Evidence/artifact sought:** immutable-v1 full-paper review plus pinned official-release audit, reconstructing task origins, expert authority, suite assembly, interventions, environments, graders, baselines, estimands, and claim limits with page/file evidence.
- **Uncertainty clarified:** whether context sensitivity, stopping, collaboration, citation provenance, and independent judgment can be validly measured in released research-lifecycle tasks and which machinery transfers across domains.
- **Mode/balance:** one narrow expansion task at priority 62; the ready backlog is consolidation-heavy and had no pending source/research/review task.
- **Duplication/scope:** repository search found no `2606.07462`, `AARRI`, or title match. Academic research is a methodological case, not a permanent domain commitment.
- **Useful completion:** audit at least one task from every released family; distinguish paper claims from release evidence; test hidden-obligation fairness, leakage, alternate paths, environment validity, grader sufficiency, and representativeness; add no duplicate implementation task.

Added `review-aarri-research-judgment-lifecycle` (priority 62). No second task was added. HORIZON (`2604.11978v1`) was triaged but deferred because its horizon-dependent degradation overlaps the just-reviewed operational-reliability profile and existing long-horizon/trace evidence more than AARRI fills the judgment/stopping gap.
