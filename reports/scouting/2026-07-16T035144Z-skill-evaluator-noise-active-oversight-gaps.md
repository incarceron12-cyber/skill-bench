# Scouting note — Skill evaluator-noise and active-oversight gaps

**Timestamp:** 2026-07-16T03:51:44Z

**Scope:** Narrow expansion against charter objectives A/B/C/F. After pull, the queue had 306 tasks: 301 completed, three blocked, two pending, and no claimed work. The pending consolidation of plan-state and criterion-to-outcome boundaries remains the highest autonomous priority; the consented real-expert micro-pilot remains the human prerequisite. Existing reviews are strong on Skill interventions, rater effects, artifact evaluation, feedback, and participation, but do not deeply cover (1) an expert-rated Skill/no-Skill study whose estimated difference is smaller than rater noise or (2) decision-time human steering through semantic action diffs. One targeted arXiv query surfaced these two nonduplicate primary sources. Findings below are **metadata/abstract and structural triage only**, not full-paper reviews.

## 1. Skill package effect versus expert-rater noise

**Skill-Augmented AI Agents for Medical Research Analysis: An Exploratory Multi-Model Human Evaluation in an NSCLC Transcriptomic Biomarker Task** — Qianyu Yao et al.; arXiv:2606.11830v1.

- Immutable record/PDF/HTML: https://arxiv.org/abs/2606.11830v1 · https://arxiv.org/pdf/2606.11830v1 · https://arxiv.org/html/2606.11830v1
- The arXiv API identifies immutable v1 as submitted 10 June 2026 in `cs.AI`; the metadata summary contains no withdrawal notice. HTML returned HTTP 200.
- The abstract reports six model backbones and 21 anonymized outputs: nine native-AI and 12 Skill-augmented outputs. Four non-expert biomedical reviewers and two blinded experts each supplied two ratings per output type, with expert overall quality as the primary outcome.
- Author-reported abstract results are directional but not confirmatory: expert means 5.50 versus 5.11 (difference 0.39; bootstrap 95% CI −0.04 to 0.90; Welch p=0.156), non-expert means 4.72 versus 4.47, and single-rating expert ICC −0.15. The abstract explicitly says the signal was smaller than expert-rating noise.
- Structural HTML inspection—not body reading—confirmed methods for study design, backbones, generation, unified task, Skill package, anonymization, human evaluation, statistical analysis, reviewer agreement, model-specific effects, measurement validity/noise, biological validity, ethics/availability, prompts, inclusion rules, rating anchors, displayed artifacts, and reproducibility boundaries.
- The immutable HTML links an author-associated Skill package: https://github.com/aipoch/medical-research-skills/tree/main/awesome-med-research-skills. No files or history were inspected during scouting.
- Exact-title/ID repository search found no local duplicate. LH-Bench, SkillsBench, industrial codification, Vibe Calibration, and many-facet rater work are adjacent; this source is distinct because it puts a central Skill-intervention estimate next to explicitly poor expert-rater reliability and a biological-validity gap.

**Reusable question:** Can a configured package effect be distinguished from model/output imbalance, intervention differences, and evaluator noise? The needed chain is `Skill package identity → availability/access/routing → observed adoption → artifact evidence → blinded criterion decisions → rater reliability → independent substantive outcome → bounded transfer/use claim`. Expert credentials do not rescue an unreliable instrument, and a small score association does not establish biological correctness, expertise transfer, or professional utility.

## 2. Decision-time semantic diffs and active oversight

**Auditing and Controlling AI Agent Actions in Spreadsheets** — Sadra Sabouri et al.; arXiv:2604.20070v1.

- Immutable record/PDF/HTML: https://arxiv.org/abs/2604.20070v1 · https://arxiv.org/pdf/2604.20070v1 · https://arxiv.org/html/2604.20070v1
- Official Microsoft Research publication page: https://www.microsoft.com/en-us/research/publication/auditing-and-controlling-ai-agent-actions-in-spreadsheets/
- The arXiv API identifies immutable v1 as submitted 22 April 2026 in `cs.HC`, cross-listed in `cs.AI` and `cs.CE`; the metadata summary contains no withdrawal notice. HTML returned HTTP 200.
- The abstract introduces Pista, which decomposes spreadsheet-agent execution into auditable, controllable actions. It reports a formative study (N=8) and within-subjects summative comparison (N=16), with outcomes spanning task result, comprehension, agent perception, workflow role, error detection, steering, and co-ownership. These are author-reported abstract claims.
- Structural HTML inspection—not body reading—confirmed a technology-probe formative study; design goals for traceable/digestible execution, granular intervention/exploration, and task-specification scaffolding; a usability study with financial-analysis tasks; measures and analysis; findings on comprehension, steering, and error correction; discussion of calibrated trust and a “semantic diff” primitive; and limitations.
- The HTML links two `sheetcheck` repositories, but scouting did not establish that they implement or release Pista. No implementation, tasks, study materials, logs, spreadsheets, codebook, or outcomes were inspected.
- Exact-title/ID search found no local duplicate. BankerToolBench was already deliberately deferred for overlap. ArtifactCopilot, DeskCraft, AgencyBench, MBABench, and feedback/participation reviews are adjacent, but none isolates pre-execution semantic-diff inspection and steering as the treatment.

**Reusable question:** Does active participation improve independently observed artifact/state consequences, or mainly comprehension, experience, and self-reported ownership? Preserve `planned action → user-visible semantic diff/evidence → detection → authorized intervention → agent uptake → realized correction → collateral preservation → artifact consequence`, plus comprehension, reliance, burden, and downstream use as separate outcomes. Selected corrections and self-report cannot by themselves establish general oversight effectiveness.

## Evidence limits and queue action

Only arXiv API metadata/abstracts, endpoint status, immutable-HTML headings/outbound-link inventories, targeted primary-source searches, queue/index state, and local duplicate checks were inspected. The papers, appendices, study instruments, participant records, prompts, outputs, ratings, statistics, repositories, and release artifacts were **not read or executed**. No causal Skill effect, biological validity, oversight benefit, calibrated trust, professional validity, production fitness, or readiness claim is made.

Added two low-priority deep-review tasks, subordinate to current consolidation and the human prerequisite:

1. `review-skill-augmented-medical-human-evaluation` (priority 3): immutable-paper plus paper-time/current Skill-package audit, with exact generation/rating dependence and claim ceilings.
2. `review-pista-active-oversight-workflow-validity` (priority 2): full HCI-method and release audit, separating visibility, intervention, realized repair, artifact integrity, experience, burden, and consequence.

Both are method studies rather than domain scope commitments. Useful completion is a source-grounded review that either changes the intervention/evaluator or oversight instrumentation guidance, or documents that the evidence is too weak to do so; no new schema should follow unless an exercised nonduplicate gap remains after comparison with existing machinery.
