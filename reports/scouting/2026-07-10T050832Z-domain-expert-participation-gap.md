# Scouting note — domain-expert participation gap

**Timestamp:** 2026-07-10T05:08:32Z

**Scope:** Narrow primary-source search for charter objective F: making expert participation feasible under limited resources. The queue was healthy (seven pending tasks), so this run avoided another broad benchmark search and added one lower-priority review for the otherwise uncovered participation/ownership layer.

## Substantive finding (triage only)

**Key Considerations for Domain Expert Involvement in LLM Design and Evaluation: An Ethnographic Study** — Szymanski, Anuyah, Li, and Metoyer, arXiv:2602.14357v1; IUI 2026.

- Immutable record: https://arxiv.org/abs/2602.14357v1
- Immutable PDF: https://arxiv.org/pdf/2602.14357v1
- Publication record: https://toby.li/publications/c50/
- The arXiv API reports a 14-page paper based on a 12-week ethnographic study of a team building a pedagogical chatbot, with observations and interviews spanning developers and domain experts. Its abstract identifies four practices: data-collection workarounds, augmentation when expert input was scarce, co-development of evaluation criteria, and hybrid expert–developer–LLM evaluation. It also identifies expert motivation and trust, participatory-design structure, ownership, and integration of expert knowledge as unresolved challenges.
- The immutable arXiv record and PDF returned HTTP 200 during this run.
- This was **metadata/abstract triage only**. The PDF was not read during scouting; study methods, observations, participant statements, and recommendations must be verified from full text.

## Why this fills a distinct gap

The repository has executable contracts for representing expert claims and a queued ACTA review for eliciting tacit cognition, but no primary-source task addresses how experts are recruited, motivated, supported, credited, consented, or given decision rights. This source appears to address that collaboration layer from observed practice rather than offering another task taxonomy. Its bounded pedagogical setting must not be generalized without scrutiny; useful completion is a cross-domain workflow whose claims remain tied to evidence and whose unvalidated incentive proposals are explicitly labeled.

The search also surfaced XpertBench (arXiv:2604.02368v4), which reports more than 1,000 expert submissions across professional domains, and a participatory manufacturing benchmark on OpenReview. They were deferred to avoid backlog inflation: the ethnographic source more directly studies motivation, trust, consent, ownership, and role design, while the other candidates can be revisited if its full text lacks operational recruitment or contribution evidence.

## Charter decision filter and queue action

- **Objective advanced:** charter F, with support for B and E.
- **Evidence/artifact sought:** a full-text review plus a role/decision-rights matrix, consent/provenance record, contribution-unit design, reciprocal-output and attribution options, review gates, and pilot measures.
- **Uncertainty clarified:** whether low-cost expert participation can preserve trust, ownership, and useful expert authority rather than treating experts as annotation labor.
- **Mode:** targeted expansion and human learning; intentionally lower priority than the current build/review backlog.
- **Duplication/scope check:** distinct from ACTA elicitation and benchmark authoring; the pedagogical case is evidence for a general collaboration hypothesis, not a new domain scope.
- **Useful completion:** observed evidence, author proposals, and skill-bench adaptations are separated, limitations are explicit, and the resulting workflow defines testable participation outcomes.

Added one task: `review-domain-expert-participation-ethnography` (priority 84).
