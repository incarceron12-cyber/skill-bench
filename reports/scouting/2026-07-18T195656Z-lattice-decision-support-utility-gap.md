# Scouting note — decision-support utility validity gap

- **Timestamp:** 2026-07-18T19:56:56Z
- **Evidence status:** arXiv API metadata/abstract, immutable endpoint and size checks, outbound-link discovery from arXiv HTML, official GitHub repository metadata, and exact repository duplicate searches only. The PDF/HTML/source body, six dimensions, 16 task types, 1,200 queries, rubric definitions, judge prompts, copilot outputs, human feedback, analyses, code, or data were **not** deeply read, downloaded into the repository, executed, reproduced, or audited during scouting.

## Substantive candidate — triage only

**LATTICE: Evaluating Decision Support Utility of Crypto Agents** — Aaron Chan, Tengfei Li, Tianyi Xiao, Angela Chen, Junyi Du, and Xiang Ren; arXiv:2604.26235v1.

- Immutable record/PDF/HTML/source: https://arxiv.org/abs/2604.26235v1 · https://arxiv.org/pdf/2604.26235v1 · https://arxiv.org/html/2604.26235v1 · https://export.arxiv.org/e-print/2604.26235v1
- Official implementation linked by the immutable arXiv HTML: https://github.com/SaharaLabsAI/lattice-benchmark (live `main` HEAD observed as `29cf51ea4d105b315ae3852a63f2260852a1d5ab`, committed 2026-04-30; MIT license).
- The arXiv API identifies a 29 April 2026 `cs.CR`/`cs.AI` submission. Its abstract presents six decision-support dimensions, 16 end-to-end copilot task types, LLM-judge scoring without expert labels or external ground truth, and a comparison of six production crypto copilots on 1,200 queries. It reports similar aggregate scores but larger dimension/task differences and suggests user-priority-dependent product choice. These are author-stated claims awaiting full-paper and release verification.
- At scouting time the immutable record, PDF, HTML, and source endpoints returned HTTP 200 with 44,228, 587,600, 279,007, and 368,347 bytes respectively.
- Exact title, ID, repository, and decision-support searches found no local review, queue task, or scouting note. Existing criterion-validity, benchmark-to-risk elicitation, production-evaluation, contextual-rubric, human/AI-rater, and recipient-consequence work supplies adjacent links, but no reviewed source directly claims to evaluate **user decision-support utility** while intentionally omitting expert ground truth and observed user decisions.

## Why this is a narrow, useful gap

The reusable chain is:

`user decision and loss → information need and authority → task/query projection → configured copilot response → criterion applicability and evidence view → judge observation → dimension vector → user-priority aggregation → recommendation or selection → actual uptake/decision → downstream benefit, burden, and harm`.

This directly advances charter objectives A, B, and E. It tests a central claim boundary for realistic knowledge work: response properties that appear helpful to an LLM judge, decision-support quality, preference-sensitive product selection, actual human decision improvement, and consequential utility are not interchangeable. The source may offer an unusually inspectable negative case because the abstract explicitly substitutes scalable judge rubrics for expert labels and external ground truth.

A full review should reconstruct the six constructs and 16 task types; source and authority for each query, criterion, and weight; query/category sampling and exclusions; production-copilot version/configuration and live-data identity; judge models, prompts, evidence views, call topology, invalids, repeats, calibration, uncertainty, and aggregation; human-feedback role; user-priority analysis; and release-to-paper reconstruction. It should test criterion polarity/applicability, dimension dependence, answer-evidence sufficiency, judge-model swaps, score/weight sensitivity, missingness, live-source drift, and whether any human decision, uptake, loss, or outcome is observed.

## Charter decision filter and queue action

- **Objectives advanced:** A (production evaluation, human evaluation, and benchmark validity), B (response→decision→consequence warrants), and E (decision-relevant understanding of what “utility” can mean).
- **Concrete evidence:** immutable-v1 full-paper review plus timing-aware audit of the official release at a pinned commit, including representative score reconstruction and sensitivity checks where feasible.
- **Uncertainty clarified:** whether LATTICE establishes a useful response-quality instrument for configured copilots, a preference-sensitive product-selection instrument, or actual decision-support utility—and which additional human/outcome evidence separates those claims.
- **Mode:** narrow expansion. The only autonomous pending task is higher-priority v7 lifecycle consolidation; one lower-priority review restores a small research buffer without repeating broad search.
- **Duplication/scope check:** exact searches were negative. Crypto is a bounded decision-support mechanism case, not a benchmark-domain commitment. Existing metric, observer, rater, configured-system, consequence, release, and validity machinery should be reused rather than extended by default.
- **Useful completion:** reproduce the released task/rubric/judge/result chain where inspectable, identify the highest warranted claim, and preserve decision improvement, financial benefit, safety, professional validity, production fitness, and readiness claim ceilings.

Added one task: `review-lattice-decision-support-utility-validity` (review, priority 47). No second task was queued. Recent alternatives such as EvoAgentBench and SLEUTH were not reconsidered because prior scouting explicitly identified them as duplicative of the procedural-transfer and analytical-hypothesis/evidence-acquisition corpus.
