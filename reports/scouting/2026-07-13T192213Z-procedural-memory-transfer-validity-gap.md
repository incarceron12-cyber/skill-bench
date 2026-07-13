# Scouting note — procedural-memory transfer validity gap

**Timestamp:** 2026-07-13T19:22:13Z  
**Scope:** Narrow expansion against charter objectives A/B/C. Queue inspection found 182 tasks: 178 completed, two blocked, two pending (one build and one consolidation), no claimed work, and no pending source/research/review task. The reviewed corpus covers expert-authored skills, paired skill/no-skill evaluation, skill-relation projection, context updates, longitudinal adaptation, and workplace-shaped tasks, but not a benchmark that explicitly crosses procedural-memory refinement with transfer across tasks, professional roles, and model backbones.

## Substantive finding (triage only)

**Managing Procedural Memory in LLM Agents: Control, Adaptation, and Evaluation**

- Immutable arXiv record: https://arxiv.org/abs/2606.23127v1
- Immutable PDF: https://arxiv.org/pdf/2606.23127v1
- arXiv HTML: https://arxiv.org/html/2606.23127v1
- The arXiv API identifies Julia Belikova, Rauf Parchiev, Evgeny Egorov, Grigorii Davydenko, Gleb Gusev, Andrey Savchenko, and Maksim Makarenko; v1 was submitted 22 June 2026 in `cs.AI`, with `cs.CL` and `cs.SE` cross-lists and no later version returned during this run.
- The abstract introduces AFTER, reported as 382 enterprise tasks spanning six professional roles and 22 procedural skills, with controlled settings for local improvement, cross-task transfer, cross-role transfer, and cross-model generalization.
- The abstract reports one refinement round improving aggregate performance by 3.7–6.7 points and skills evolved from diverse multi-model traces reaching 73.1% cross-model test accuracy, while some skills specialize and lose effectiveness under transfer. These are discovery leads only: task provenance, role definitions, split independence, baseline identity, repeated-run uncertainty, selection, refinement budget, trace visibility, evaluator overlap, negative transfer, and statistical support require full-paper verification.
- The abstract and all three immutable arXiv URLs resolved successfully. Targeted search did not identify an author-owned code or dataset repository; a reviewer must verify release claims and inspect any artifact URLs in the complete paper.
- Repository-wide duplicate search found neither the title nor arXiv ID. SkillsBench studies paired skill efficacy; LH-Bench studies expert-authored procedural guidance and rubrics; SLBench studies relations within skills; Agentic Context Engineering and the self-evolving-agent survey address update governance and longitudinal confounds. None currently audits a task × role × model transfer matrix for learned procedural memory or tests whether diverse trace sources improve transport rather than leak evaluator/task structure.
- This is **metadata/abstract and URL triage only**. The paper, appendices, task corpus, skills, traces, refinement prompts, split construction, graders, configurations, and result records were not fully read or audited. No claim is made that the tasks are realistic enterprise work, the skills encode expert knowledge, the gains are causal or reliable, cross-role transfer occurred, or the system is production-ready.

## Benchmark implication to test

Procedural memory is an intervention with a provenance-bearing lifecycle, not a static prompt. A valid transfer claim should preserve the generating tasks and models, trace/evaluator visibility, update operator and budget, before/after skill identity, task/role/model split relations, negative-transfer and forgetting outcomes, and matched reset/no-update controls. AFTER may add an empirical design for separating local adaptation, near transfer, role transport, and backbone transport, but professional-role labels and higher held-out scores do not by themselves establish tacit expertise transfer or reusable workplace competence. A full audit should test whether its matrix supplies nonduplicate evidence for the existing procedural-skill, longitudinal-stream, configured-system, feedback-firewall, task-health, metric, and validity contracts.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier procedural-memory and realistic-agent evaluation), B (expertise-to-evaluation and transfer validity), and C (longitudinal/configured-system evaluation machinery).
- **Evidence/artifact sought:** immutable full-paper review plus any official release audit, reconstructing task and role provenance, skill representation and refinement, trace-source treatments, split graph, model/scaffold identity, graders, repeats, uncertainty, costs, negative transfer, and release completeness.
- **Uncertainty clarified:** whether the reported local/cross-task/cross-role/cross-model results isolate reusable procedural transfer from task overlap, evaluator cues, trace-source diversity, model/scaffold changes, or selection.
- **Mode/balance:** narrow expansion; one high-priority build and one consolidation task remain ready, while the research/review backlog was empty.
- **Duplication/scope:** nonduplicate transfer-matrix question; six reported roles are a bounded test of reusable intervention/transfer machinery, not a commitment to those professions or to self-improving agents as the benchmark scope.
- **Useful completion:** verify every headline number from full text; inspect any released tasks, skills, traces, code, graders, and results; audit role/task sourcing, split independence, update budgets, leakage, matched controls, forgetting/negative transfer, uncertainty, and reproducibility; preserve strict expert-transfer, occupational, professional-validity, general-capability, production, and readiness ceilings.

Added `review-after-procedural-memory-transfer-validity` (priority 47). No second task was added.
