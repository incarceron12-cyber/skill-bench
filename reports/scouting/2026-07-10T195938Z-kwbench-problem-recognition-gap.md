# Scouting note — unprompted problem-recognition gap

**Timestamp:** 2026-07-10T19:59:38Z  
**Scope:** Narrow search against charter objectives A/B/C after confirming that source/research/review backlog was empty and two evidence-grounded build tasks remained pending. This run targeted a specific construct gap between being told which professional problem to solve and recognizing the problem from a messy situation; it did not repeat broad benchmark discovery.

## Substantive finding (triage only)

**KWBench: Measuring Unprompted Problem Recognition in Knowledge Work**

- Immutable arXiv record: https://arxiv.org/abs/2604.15760v1
- Immutable PDF: https://arxiv.org/pdf/2604.15760v1
- arXiv HTML: https://arxiv.org/html/2604.15760v1
- Project page: https://kwbench.github.io/
- Dataset location: https://huggingface.co/datasets/clio-ai/kwbench
- Search-indexed arXiv metadata identifies version 1 in `cs.AI`, submitted 2026-04-17. The abstract describes a benchmark for whether a model identifies the professional problem implicit in a situation before trying to solve it, rather than receiving the analytical frame in the prompt.
- The official-looking project and dataset locations are discoverable, but the Hugging Face files are access-gated and the project organization's visible GitHub repository appears to be the website rather than an evaluation-code release. A deep review must verify paper-linked ownership, immutable revisions, exact released artifacts, and access boundaries.
- This is **metadata/abstract and release-location triage only**. The full paper, project, and dataset were not read during scouting. Task count, domains, expert authorship, scenario provenance, recognition labels, intervention conditions, graders, statistics, and professional-validity claims require full review.

## Why this is distinct

The local corpus strongly covers executing explicit long-horizon tasks, producing professional artifacts, navigating workspaces, and transferring procedures. It does not directly audit the prior construct of **problem finding**: noticing a hidden anomaly, risk, decision need, or violated expectation when the task does not name the relevant concept. A benchmark can overestimate workplace capability if its prompt supplies the expert framing that ordinarily constitutes much of the work.

The reusable question is not whether skill-bench should adopt KWBench or one occupational framing. It is whether source packs and task prompts should experimentally separate situation-only recognition from named-problem execution; how expert cues, plausible distractors, omission, severity, and urgency become evidence-bearing primitives; whether recognizing a label differs from gathering decisive evidence or taking an appropriate action; and how to avoid rewarding keyword matching to authored scenario templates.

## Charter decision filter and queue action

- **Objectives advanced:** A (realistic knowledge-work benchmark frontier), B (tacit cue and hidden-requirement transfer), and C (task, intervention, artifact, and grader contracts).
- **Evidence/artifact sought:** immutable-v1 full-paper review, verified/pinned official-material audit, and a construct crosswalk to existing expertise-transfer, public/private consequence, task-health, validity, metric, and pilot machinery.
- **Uncertainty clarified:** whether the benchmark independently measures problem recognition; how scenarios and ground truth were expert-grounded; whether framing, execution, and recognition are experimentally separated; whether recognition predicts appropriate evidence gathering/action; and what population of professional work the results support.
- **Mode/balance:** one narrow expansion task at priority 69. There were no pending source, research, or review tasks; two build tasks already provide a healthy consolidation path.
- **Duplication/scope:** no local index entry, paper review, queue item, or scouting note matched `2604.15760`, `KWBench`, or unprompted problem recognition. Consulting critical incidents cover expert/novice paths, but not a direct situation-only versus named-problem measurement design. This is a cross-domain construct case, not a commitment to any one profession.
- **Useful completion:** paper claims and released evidence are separated; scenario provenance, expert grounding, construct decomposition, controls, scoring, uncertainty, leakage, and external validity are audited; at least two released items are traced if access permits; unavailable gated artifacts are documented; only nonduplicate implications enter existing contracts.

Added `review-kwbench-unprompted-problem-recognition` (priority 69). No second task was added.
