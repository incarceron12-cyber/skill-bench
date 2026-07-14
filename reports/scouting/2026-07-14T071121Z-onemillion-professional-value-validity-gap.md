# Scouting note — professional-work-to-economic-value validity gap

**Timestamp:** 2026-07-14T07:11:21Z  
**Scope:** Narrow expansion against charter objectives A/B/D. Queue inspection found 211 tasks: 206 completed, two blocked, and three pending (two consolidations and one human decision). The review backlog was empty, so scouting targeted one explicit comparative gap rather than repeating a broad search: the corpus covers expert-authored occupational tasks, production demand, worker delegation preference, professional rubrics, and value claims, but has not fully audited a released cross-domain benchmark that converts expert-priced tasks and rubric scores into claimed economic value.

## Substantive finding (triage only)

**$OneMillion-Bench: How Far are Language Agents from Human Experts?**

- Immutable arXiv record: https://arxiv.org/abs/2603.07980v1
- Immutable PDF: https://arxiv.org/pdf/2603.07980v1
- Current project release: https://github.com/humanlaya/OneMillion-Bench
- Current dataset surface: https://huggingface.co/datasets/humanlaya-data-lab/OneMillion-Bench
- The arXiv API identifies Qianyu Yang and 22 coauthors, with only v1 submitted and updated 9 March 2026 in `cs.LG`, `cs.AI`, and `cs.CL`; the abstract contains no withdrawal notice.
- The abstract describes 400 expert-curated tasks across law, finance, industry, healthcare, and natural science. It says tasks require retrieval of authoritative sources, resolution of conflicting evidence, application of domain-specific rules, and constraint decisions, with rubric dimensions for factual accuracy, logical coherence, practical feasibility, and professional compliance. These are discovery leads only: task and expert sampling, source-pack realization, actual agent/tool use, output artifacts, rubric authority, judge evidence views, dependence, uncertainty, and result denominators require full verification.
- Search metadata and immutable HTML structure identify a paper section on measuring economic value and an appendix covering evaluation details and cases. Search metadata describes the value estimate as senior-expert task time multiplied by hourly wages. Full review must determine whether time is observed or estimated, whose wages and geography are used, how missingness and ranges are handled, and how rubric scores become dollars; task price, deliverable quality, labor displacement, organizational benefit, and realized value are not interchangeable.
- The paper is cited in local full-text reviews but has no local review or queue task. GDPval and Agents’ Last Exam cover broad expert-authored work; JobBench covers worker delegation preference; AlphaEval covers production demand and selected package outcomes; ResearchRubrics covers expert criterion authoring. None currently audits this particular `task curation → rubric score → expert-time/wage anchor → dollar-value aggregate` chain.
- Current release existence was verified, not audited. Acquisition-time GitHub HEAD is `b82d627db853eda4584572cc261336e19f5c0286`; GitHub reports repository creation on 1 March 2026, Apache-2.0, and latest push on 21 April 2026. The public, ungated Hugging Face dataset reports revision `5cf9d5005e2e1f20b4481ed50846161697e82a73`, last modified 11 March 2026, with eight listed files. The immutable paper HTML did not expose these task-release links in its outbound link set, while the current xbench project page does. Paper-time correspondence, organization/author ownership, dataset completeness, task licensing, and exact empirical bytes therefore remain to be established rather than assumed.
- Narrow alternatives were checked but not queued. UNDERWRITE (`2602.00456v1`) offers expert-first insurance workflows with proprietary knowledge and noisy tools but is a single-domain instrument without a verified release in this triage. SWE-Bench 5G (`2604.26278v1`) offers a useful specification-injection contrast but is narrower than the missing cross-domain value-validity comparison. One task was added to avoid overfilling the healthy consolidation backlog.
- This is **metadata/abstract, section-structure, URL, release-existence, and duplicate triage only**. The PDF, appendices, repository, dataset files, tasks, source materials, rubrics, references, prompts, outputs, judge calls, results, and economic calculations were not fully read or audited. No claim is made that the benchmark represents professional work, measures expert equivalence, identifies labor substitution, estimates economic benefit, or establishes agent reliability, capability, safety, production fitness, professional validity, or readiness.

## Benchmark implication to test

Economic-value reporting needs a typed consequence chain rather than score multiplication: `work/task sampling frame → expert/source authority and task transformation → configured agent and evidence access → artifact/state observation → criterion-level quality with rater validity → deliverable acceptance and alternative paths → expert time/cost counterfactual → adoption and complementary human work → realized workflow outcome → stakeholder value/loss`. Price-like task weights can prioritize a portfolio without validating a dollar-denominated agent contribution. Full review should test expert qualifications and overlap across task/reference/rubric/adjudication roles; source provenance and fair conflict construction; process versus final-answer observability; judge reliability and criterion dependence; task/domain clustering; repeatability and invalid trials; wage/time provenance; nonlinear acceptance thresholds; failure costs; and whether the released instrument reproduces the reported aggregate.

Transfer should reuse existing expertise-transfer, participation/authority, task projection, artifact/evidence-view, configured-system, metric-monitoring, task-health, rater, and validity machinery. The direct comparison is with GDPval, Agents’ Last Exam, JobBench, and AlphaEval; the five domains are an instrument frame, not a scope commitment.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier professional benchmark research), B (expertise-to-evaluation and consequence validity), and D (comparative consolidation).
- **Evidence/artifact sought:** immutable full-v1 review plus pinned GitHub/dataset audit reconstructing task/expert/source/rubric/configuration/result/value lineage and exact release correspondence.
- **Uncertainty clarified:** whether the instrument supports bounded professional-task rubric observations or stronger economic-value, expert-equivalence, and readiness interpretations.
- **Mode/balance:** one low-priority review task restores a minimal research backlog while leaving both pending consolidations ahead of it.
- **Duplication/scope:** fills a task-to-dollar validity gap and requires explicit comparison with existing professional families; it neither duplicates their reviews nor selects one occupation or domain.
- **Useful completion:** verify every frame, role, observer, denominator, release, and transformation; separate task price, score, accepted deliverable, saved expert effort, substitution, organizational outcome, and realized value; preserve strict representativeness, professional-validity, capability, safety, production, and readiness ceilings.

Added `review-onemillion-professional-value-validity` (priority 26). No second task was added.
