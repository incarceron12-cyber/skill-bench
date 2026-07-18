# Scouting note — executable expert-reasoning verification gap

- **Timestamp:** 2026-07-18T07:14:35Z
- **Evidence status:** arXiv API metadata/abstract, immutable endpoint checks, HTML heading/external-link triage, targeted release search, and exact repository duplicate searches only. The PDF body, methods, appendices, DESI catalogue rows, expert adjudication records, prompts, code, outputs, or result tables were **not** deeply read, downloaded, reproduced, or audited during scouting.

## Substantive candidate — triage only

**Executable verification through formalized expert reasoning in astronomical spectroscopy** — Haosong Wang, Ting Tan, Ji Yao, Jiajun Zhang, Qian Zheng, Christophe Yèche, Jean-Paul Kneib, and Huanyuan Shan; arXiv:2607.06128v1.

- Immutable record/PDF/HTML: https://arxiv.org/abs/2607.06128v1 · https://arxiv.org/pdf/2607.06128v1 · https://arxiv.org/html/2607.06128v1
- The arXiv API reports immutable v1 submitted and last updated 7 July 2026, 26 pages, in `astro-ph.CO` and `astro-ph.IM`; its summary contains no withdrawal or retraction notice. Record, PDF, and HTML endpoints returned HTTP 200; the PDF response reported 1,839,340 bytes.
- The abstract introduces FORMA, an executable verification protocol intended to turn expert reasoning into evidence extraction, physically constrained hypothesis generation, alternative testing, auditable consistency checks, and a credibility score. Applied to a DESI visual-inspection catalogue, a medium-or-higher threshold reportedly selects 331 definite predictions with 95.5% binary agreement with expert-adjudicated classes. These are author-stated claims awaiting full-paper verification.
- HTML structure exposes method sections for a Visual Interpreter, Hypothesis Analyst, Analysis Auditor, Report Writer, feature score/credibility rating, tools/knowledge base, dataset composition, feature-score limitations, and counterfactual evidence-ablation tests. This is structural triage, not a methods review.
- The HTML's visible release-like external links and targeted title/author/FORMA GitHub searches exposed no author code or data repository. The paper includes a “Code availability” heading, so release status must be checked from the full text rather than inferred from search failure.
- Exact arXiv ID, title, `FORMA`, and spectroscopy searches found no local queue task or review. Existing ResearchRubrics, PaperBench, LQCDMaster, and expert-disagreement work covers adjacent links but not this particular expert-reasoning → executable scientific-verification transformation.

## Why this is a narrow, useful gap

The reusable chain is:

`expert catalogue and adjudication authority → formalized observational procedure → evidence extraction → constrained candidate hypotheses → explicit alternative tests → auditor evidence view and consistency checks → credibility score and threshold → selected/abstained decision → independent scientific correctness → downstream scientific use`.

This directly advances charter objective B: expertise should become evidence-bearing, executable benchmark machinery rather than an untraceable checklist. FORMA may supply a concrete method for preserving evidence, alternatives, physical constraints, and audit steps. It also raises strong validity questions: whether the formalization is source-faithful or model-inferred; whether the same catalogue informs procedure, score, threshold, and comparator; whether 331 selected cases hide a coverage/abstention tradeoff; whether expert agreement is treated as scientific ground truth; whether score components are independently validated; and whether counterfactual ablations test causal evidence use rather than prompt sensitivity. Agreement on one bounded catalogue does not establish scientific correctness, expertise transfer, cross-domain validity, production fitness, or readiness.

Astronomical spectroscopy is a bounded mechanism case, not a proposed benchmark scope.

## Charter decision filter and queue action

- **Objectives advanced:** A (expert judgment, scientific/artifact evaluation, scalable verification) and B (expertise-to-executable-evaluation methodology).
- **Concrete evidence:** immutable-v1 full-paper review plus code/data availability audit, with exact lineage from expert labels/procedure through evidence, alternatives, checks, score, threshold, selection, and claim.
- **Uncertainty clarified:** whether FORMA independently verifies candidate conclusions using a faithful expert procedure or chiefly reproduces a selectively covered catalogue with coupled construction and evaluation.
- **Mode:** narrow expansion. The queue had one autonomous review and one build task; one bounded source adds evidence without repeating broad search.
- **Duplication/scope check:** adjacent reviewed sources do not cover this transformation; reuse existing evidence, expertise-transfer, criterion, observer, artifact, metric, task-health, and validity machinery, and add no astronomy-specific subsystem absent stronger evidence.
- **Useful completion:** reconstruct all transformations and denominators; audit expert authority/disagreement, coverage/abstention, threshold sensitivity, coupling/leakage, counterfactual evidence tests, and reproducibility; preserve strict claim ceilings.

Added one task: `review-forma-executable-expert-verification-validity` (review, priority 56). No second source was queued.
