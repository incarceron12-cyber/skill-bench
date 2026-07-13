# Scouting note — skill-logic relation-validity gap

**Timestamp:** 2026-07-13T17:29:51Z  
**Scope:** Narrow expansion against charter objectives A/B/C. Queue inspection found 171 completed tasks, two pending consolidation tasks, two blocked tasks, and no pending source/research/review work. Existing reviews cover expert-authored procedural skills, paired skill/no-skill trials, action authorization, generated-task conformance, and configured-system isolation, but not executable tests of dependencies among instructions inside a skill or whether failures originate in agent execution versus low-salience skill wording.

## Substantive finding (triage only)

**SLBench: Evaluating How LLM Agents Follow Logical Relations in Skills**

- Immutable arXiv record: https://arxiv.org/abs/2607.09016v1
- Immutable PDF: https://arxiv.org/pdf/2607.09016v1 (verified HTTP 200, `application/pdf`, 511,047 bytes during this run)
- arXiv HTML/full-text rendering: https://arxiv.org/html/2607.09016v1
- The immutable v1 HTML identifies Xuan Chen, Chengpeng Wang, Lu Yan, and Xiangyu Zhang (Purdue University), dated 10 July 2026 in `cs.CR`; arXiv also lists `cs.SE`.
- The abstract introduces SkillLogic, a framework for extracting relations among skill instructions and constructing executable tests. It reports an eight-relation taxonomy including preconditions, constraints, and fallbacks; a scan of more than 5,000 public skills where 70% contained at least one relation; and an 86-case benchmark selected for high-confidence, high-impact, locally testable relations.
- The abstract reports Codex and Claude Code evaluations across six backbones, unsafe rates up to 70%, a human audit attributing violations to both agent gaps and low-salience skill text, and a targeted SLGuard scaffold reducing violations by 63%. These numbers and interpretations are discovery leads only; exact denominators, selection, configurations, repeats, uncertainty, audit protocol, scaffold comparison, and leakage controls require full-paper verification.
- The rendered paper says each target agent receives the original skill, user prompt, local environment, and deterministic grader. It also states that SkillLogic itself is implemented as a two-step skill run by a helper agent using Codex/GPT-5.4. This makes generated relation extraction, case construction, target execution, grading, and mitigation separate components whose validity must be audited rather than collapsed into one score.
- Targeted HTML and web searches found no author-owned code or dataset URL. A reviewer must verify whether the 5,000-skill sample, 86 cases, relation annotations, graders, human-audit records, prompts, trajectories, and SLGuard implementation are released or reproducible.
- Repository-wide duplicate search found neither the title nor arXiv ID. LH-Bench and SkillsBench study skill-grounded work and paired skill efficacy; Anchor studies generated-component conformance; UnderSpecBench studies action boundaries. None directly audits intra-skill dependency semantics, relation-level test generation, skill-text salience, or whether an inference scaffold changes the intervention being measured.
- This is **metadata/abstract plus targeted HTML triage only**. The complete paper, appendices, relation corpus, generated cases, human audit, trajectories, graders, and mitigation experiments were not fully read or inspected. No claim is made that the taxonomy is complete, the generated tests preserve skill intent, the reported failures are unsafe in production, or SLGuard generally improves reliability.

## Benchmark implication to test

A skill is a dependency-bearing intervention, not a flat list of instructions. Preconditions, temporal order, mutual exclusion, constraints, exceptions, fallback/recovery behavior, cleanup obligations, and stop/escalation rules should retain their public textual basis and become separately testable relations. But automatically extracted relations and generated tests are projections: relation existence, intended semantics, case validity, observer sufficiency, agent realization, consequence severity, and mitigation effect require distinct evidence. A full audit can test whether this machinery strengthens the existing procedural-skill, task-generation, action-boundary, trace, and root/surface contracts without turning `skill-bench` into a benchmark of skill files or coding agents.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier skill-guided agent reliability and evaluation), B (translating procedural expertise into explicit dependency-bearing checks), and C (executable task-generation, grader, trace, and diagnosis machinery).
- **Evidence/artifact sought:** immutable full-paper review and any official-release audit, reconstructing relation definitions, sampling and filtering, generation prompts, human validation, executable environments/graders, target-agent configurations, unsafe/inconclusive labels, audit reliability, mitigation intervention, uncertainty, and release completeness.
- **Uncertainty clarified:** whether relation-grounded executable cases preserve the meaning and authority of skill instructions, and whether failures can be separated among skill ambiguity/salience, generated-test error, agent execution, grader observation, and real consequence.
- **Mode/balance:** narrow expansion; two consolidation tasks remain ready, while source/research/review backlog was empty.
- **Duplication/scope:** nonduplicate relation-semantics question; coding skills are a bounded test of reusable procedural-dependency machinery, not a profession or benchmark-scope commitment.
- **Useful completion:** verify every headline number and comparison from full text; inspect any released corpus/code; audit relation authority, case-generation fidelity, selection, human-review reliability, configured-system identity, repeats/uncertainty, leakage, severity, and SLGuard ablation; map only nonduplicate obligations to existing contracts while preserving strict general-reliability, safety, production, professional-validity, and readiness limits.

Added `review-slbench-skill-relation-validity` (priority 44). No second task was added.
