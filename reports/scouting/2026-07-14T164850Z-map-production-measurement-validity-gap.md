# Scouting note — production-agent measurement-practice validity gap

**Timestamp:** 2026-07-14T16:48:50Z  
**Scope:** Narrow expansion against charter objectives A/B/D/E. Queue inspection found 214 tasks: 209 completed, three blocked, one pending consolidation, and one pending human decision; no source/research/review task remained. Existing work already covers production telemetry, production-derived trajectory evaluation, offline/online association, and official engineering experience reports, so this run targeted one missing primary empirical view: cross-domain practitioner evidence about how deployed agents are actually scoped and evaluated.

## Substantive finding (triage only)

**Measuring Agents in Production (MAP)**

- Immutable latest arXiv record: https://arxiv.org/abs/2512.04123v4
- Immutable latest PDF: https://arxiv.org/pdf/2512.04123v4
- OpenReview record: https://openreview.net/forum?id=FxNCt9xtOZ
- The arXiv API identifies Melissa Z. Pan and 24 coauthors, first submission on 2 December 2025, latest update on 4 June 2026, and categories `cs.CY`, `cs.AI`, `cs.LG`, and `cs.SE`; the latest abstract contains no withdrawal notice. All three URLs returned HTTP 200 during this run. Search metadata reports an accepted OpenReview poster.
- The **v4 abstract** says the study combines 20 in-depth case-study interviews with a survey of 86 deployed-systems practitioners across 26 domains. It reports that 68% of agents execute at most ten steps before human intervention, 70% use prompting of off-the-shelf models rather than weight tuning, 74% rely primarily on human evaluation, and reliability—defined in the abstract as consistent correct behavior over time—is the top development challenge. These are author-reported abstract claims, not findings independently verified during scouting.
- MAP is distinct from the reviewed Perplexity production-usage study, which observes product-conditioned delegation attempts and telemetry; AgentLens, which operationalizes a production-inspired trajectory instrument on 16 Java scenarios; Nubank, which studies an adaptively selected offline/online metric association; and Amazon/Anthropic engineering reports, which describe organization-specific evaluation frameworks. MAP instead offers primary interview/survey evidence about practitioner choices across domains. A full review can test whether those choices are representative, measured consistently, or effective rather than treating reported prevalence as design validation.
- Version identity is a first-order issue. Search-visible v3/PDF metadata reports 306 practitioners, whereas the latest v4 abstract narrows the survey claim to 86 deployed-systems practitioners. The review must reconstruct eligibility, exclusions, denominators, and changed claims across versions rather than combining them.
- Repository-wide searches found citations to arXiv `2512.04123` in several local full texts but no local MAP review, acquisition record, or queue task. Existing reviews mention MAP only as related work.
- No verified official data/code release was found in narrow searches. The review should inspect appendices, survey/interview instruments, OpenReview revisions and reviews, and any linked artifacts before deciding inspectability or reproducibility.
- This is **metadata, abstract, URL, acceptance, version-drift, and duplicate triage only**. The PDF, appendices, OpenReview reviews, instruments, coding procedures, sample flow, tables, qualitative evidence, and any supplementary artifacts were not fully read or audited. No claim is made that MAP represents deployed-agent practice, identifies successful methods, validates human evaluation, establishes reliability interventions, or supports capability, safety, professional validity, production fitness, or readiness.

## Benchmark implication to test

Production-practice evidence needs a typed chain: `target deployment population → recruitment and deployed-system eligibility → organization/domain/respondent hierarchy → instrument item and coding → reported practice/challenge → configured system and operating context → observed measurement/monitoring behavior → intervention or design choice → repeated production outcome → stakeholder decision/loss`. A reported majority practice is not evidence that the practice works. Full review should test sample selection, nonresponse and duplicate-organization dependence, domain weighting, retrospective/self-report error, construct definitions, qualitative coding and agreement, missingness, denominator changes, and whether “reliability,” “human evaluation,” “steps,” “intervention,” and “successful deployment” have operational measures.

The reusable question for `skill-bench` is whether real deployment practice changes task-horizon choices, human-review conditions, configured-system records, repeated-trial reliability, metric monitoring, and claim ceilings. Transfer should reuse existing configured-system, participation, trace, task-health, metric-monitoring, rater, and validity machinery rather than creating a MAP-specific schema or treating current industry practice as normative.

## Charter decision filter and queue action

- **Objectives advanced:** A (production-agent evaluation frontier), B (measurement-to-claim validity), D (comparative consolidation), and E (clarifying prevalence versus effectiveness).
- **Evidence/artifact sought:** immutable-v4/OpenReview-grounded full review reconstructing sampling, instruments, coding, denominators, version changes, reported evaluation practice, reliability construct, and released evidence.
- **Uncertainty clarified:** whether MAP supplies bounded descriptive evidence about selected deployed-system practitioners or supports stronger claims about effective production evaluation.
- **Mode/balance:** one low-priority review task restores a minimal research backlog while leaving the pending interaction consolidation and human decision ahead of it.
- **Duplication/scope:** complements rather than repeats production telemetry, production-derived benchmark, and vendor-method reviews; the 26-domain frame is evidence to audit, not a benchmark scope commitment.
- **Useful completion:** separate self-reported prevalence, actual use, measurement quality, intervention choice, and downstream effectiveness; preserve respondent/organization/domain hierarchy, missingness, and strict professional-validity, capability, safety, production, and readiness ceilings.

Added `review-map-production-measurement-validity` (priority 23). No second task was added.

## Operational note

The required initial `git pull --ff-only` could not authenticate to the HTTPS GitHub remote (`could not read Username`), although local `main` initially matched the recorded `origin/main` at `ac06699`. This run proceeded from that local state and did not alter the pre-existing untracked `data/papers/source/` tree.
