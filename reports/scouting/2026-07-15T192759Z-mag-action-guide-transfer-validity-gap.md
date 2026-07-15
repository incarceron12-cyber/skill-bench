# Scouting note — action-to-guide transfer validity gap

**Timestamp:** 2026-07-15T19:27:59Z  
**Scope:** Narrow expansion against charter objectives A/B/C. Initial queue inspection found 289 tasks: 283 completed, four blocked, and two pending; no source, research, review, or claimed backlog remained. The reviewed corpus already covers expert procedural skills, trace-refined memory, interactive desktop work, handoff resumability, trajectory judges, and artifact evidence, but not a compound instrument where an agent must execute a live task while producing a stepwise instructional artifact intended for a future user.

## Substantive finding — triage only

**MAG: A Web-Agent Benchmark and Harness for Multimodal Action and Guide Generation** — Chengguang Gan, Hanjun Wei, Yunhao Liang, Zhixi Cai, Qinghao Zhang, and Shiwen Ni; arXiv:2607.10079v2.

- Immutable record selected for review: https://arxiv.org/abs/2607.10079v2
- Immutable PDF: https://arxiv.org/pdf/2607.10079v2
- Immutable HTML: https://arxiv.org/html/2607.10079v2
- The arXiv API reports v1 submitted 11 July 2026 and v2 updated 14 July 2026 in `cs.AI` and `cs.CL`; the abstract contains no withdrawal or retraction notice. Versioned v1 abstract, PDF, and HTML endpoints returned HTTP 200 during scouting.
- The abstract describes a compound screenshot-based task in which an agent executes a changing-state web workflow and writes guide text, with Set-of-Mark and raw-coordinate grounding. It also describes an annotation, training, live-environment evaluation, and joint action/guide harness.
- The abstract reports frontier/open-model evaluation and an expert-trajectory-augmented GRPO method that changes one supervised 9B agent's reported success from 6.9% to 13.2%, while the strongest reported model remains below 40% task completion. These are author-reported abstract claims, not independently verified results.
- Structural inspection of immutable v1 and v2 HTML—not a full reading—confirmed sections on task definition, LLM-assisted/human-verified annotation, task success, guide quality, a gated guide score, format and step diagnostics, expert-augmented training, significance/pass@k analyses, guide/success coupling, limitations, verification interface, prompts, metric definitions, evaluation protocol, run provenance, and qualitative cases.
- External-link inventory of both HTML versions exposed model/system-card references and arXiv conversion infrastructure but no identifiable paper-specific project, code, dataset, or harness URL. Targeted web and GitHub searches did not locate an official release. This is an unlocated-release finding, not evidence that no release exists.
- Repository-wide exact-title, arXiv-ID, and distinctive-phrase searches found no local review or queue task. Closest completed reviews include LH-Bench, AFTER, DeskCraft, Handoff Debt, AgentRewardBench, and artifact/trace work; none makes action-to-recipient-guide transformation its primary construct.
- This is **metadata, abstract, endpoint, section-structure, release-location, and duplicate triage only**. The paper body, appendices, tasks, screenshots, annotations, human-verification records, guide references, prompts, trajectories, environments, metrics, training data, runs, errors, costs, and statistics were not read or audited. No claim is made that task execution is valid, guides are correct or complete, a future user can follow them, guide metrics measure usability, expert trajectories encode transferable expertise, results reproduce, or MAG establishes tacit transfer, professional validity, production utility, or readiness.

## Why this is distinct

The reusable chain is `executed task state and evidence → action/decision trace → guide proposition and screenshot target → correctness/completeness and provenance → recipient-visible evidence → independent recipient comprehension and execution → transfer to task/interface variants → maintenance under environment drift → downstream utility and consequence`. A same-run guide could turn otherwise transient work into an inspectable procedural artifact. But successful execution does not make its narration complete or teachable, and reference-guide or judge agreement does not show that a different actor can use the artifact successfully.

A full audit should separate action grounding, environment transition validity, task success, guide proposition fidelity, omitted/rationalized steps, guide-reference dependence, metric and gate behavior, recipient usability, independent execution benefit, task and interface transfer, UI-drift maintenance, annotation authority, configured-system/training dependence, repeats, cost, and claim scope. Comparison with existing skill, memory, handoff, artifact-view, trace, grader, metric, task-health, and validity machinery should determine whether MAG adds evidence and failure signatures rather than justify web-specific infrastructure.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier realistic-agent evaluation), B (procedural experience transformed into a reusable artifact), and C (joint trace/artifact checks and transfer diagnostics).
- **Concrete evidence/artifact:** immutable-v2 deep review plus a timing-aware audit of any official release—or an explicit, reproducible unlocated-release record.
- **Uncertainty clarified:** whether joint action/guide scoring measures reusable procedural codification or primarily same-trajectory narration under co-authored references and metrics.
- **Mode:** narrow expansion feeding later consolidation; web interaction is a bounded test of trace-to-instruction transfer, not a permanent benchmark domain.
- **Duplication/scope:** no exact local duplicate; mandatory comparison with LH-Bench, AFTER, DeskCraft, Handoff Debt, AgentRewardBench, and existing artifact/trace machinery prevents parallel infrastructure.
- **Useful completion:** a claim ladder separating execution, guide fidelity, recipient usability, independent action benefit, transfer, maintenance, professional validity, production utility, and readiness, grounded in exact paper/release locators.

Added one low-priority task: `review-mag-action-guide-transfer-validity` (priority 5). The consented expert micro-pilot and current blocked/build priorities remain substantially higher priority.

## Operational note

The required initial `git pull --ff-only` succeeded. Pre-existing untracked paper-source, release-archive, and site files were not touched.
