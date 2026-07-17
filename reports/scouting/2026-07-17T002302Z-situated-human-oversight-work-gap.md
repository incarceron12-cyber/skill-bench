# Scouting note — situated human-oversight work gap

- **Timestamp:** 2026-07-17T00:23:02Z
- **Evidence status:** arXiv API metadata/abstract, immutable endpoint checks, arXiv-HTML heading/outbound-link triage, official Microsoft Research publication-page endpoint verification, and local corpus/queue duplicate searches only. The PDF/body, participant appendix, usage-scenario appendix, interview guide, qualitative coding, quotations, findings, and limitations were **not** deeply read or audited during scouting.

## Substantive candidate — triage only

**Human oversight of agentic systems in practice: Examining the oversight work, challenges, and heuristics of developers using software agents** — Shipi Dhanorkar, Samir Passi, and Mihaela Vorvoreanu, arXiv:2606.05391v1.

- Immutable record: https://arxiv.org/abs/2606.05391v1
- Immutable PDF: https://arxiv.org/pdf/2606.05391v1
- Official publication page: https://www.microsoft.com/en-us/research/publication/human-oversight-of-agentic-systems-in-practice-examining-the-oversight-work-challenges-and-heuristics-of-developers-using-software-agents/
- The arXiv API reports one version submitted 3 June 2026 in `cs.SE`/`cs.AI`, with no withdrawal notice in the abstract. Versioned abstract, PDF, and HTML endpoints returned HTTP 200; the official Microsoft Research page also returned HTTP 200.
- The abstract describes an exploratory qualitative study based on interviews with 17 experienced developers. It reports four forms of emergent oversight work—**a priori control, co-planning, real-time monitoring, and post hoc review**—plus situated challenges and developer heuristics such as treating test results as guarantees of code correctness. These are author claims awaiting full-paper verification.
- HTML heading triage shows dedicated sections for participation criteria, recruitment and organizational context, data collection and analysis, four oversight forms, four post-hoc heuristics, implications, limitations, participant demographics, agent-usage scenarios, and the interview topic guide. No paper-linked dataset, transcript corpus, codebook, analysis package, or study repository was identified among the outbound links during scouting. Release absence and empirical reproducibility remain review questions, not established defects.

## Why this is a narrow, useful gap

The corpus already reviews designed oversight interfaces (Pista and HANSEL), evidence packets (ArtifactCopilot), reusable evaluation-policy encoding without demonstrated expert authority (Human-on-the-Bridge), and a broader production-practitioner survey (Measuring Agents in Production). Exact title/ID searches found no review, queue task, or prior scouting note for this study. Its distinct evidence chain is:

`real agent-use episode and developer context → oversight opportunity → control/planning/monitoring/review action → chosen evidence view and heuristic → acceptance, intervention, escalation, or nonaction → artifact/state consequence → effort and organizational outcome`.

Interview themes can reveal work that benchmark designers otherwise omit, especially proactive control and co-planning before an observable failure. But reported heuristics are not validated grader rules: passing tests can miss specification errors, reviewing only familiar code can create selective blind spots, and a participant account cannot by itself establish prevalence, safety, productivity, or causal oversight efficacy. Software development is a bounded empirical setting for a general human-work-allocation and scalable-evaluation question, not a benchmark scope commitment.

## Charter decision filter and queue action

- **Objectives advanced:** A (production/human-evaluation frontier), B (expertise/work-to-evaluation methodology), C (realistic trace and oversight observations), and E (human learning).
- **Concrete evidence:** immutable-v1 full-paper review covering the sample, interview instrument, coding method, findings, negative cases, appendices, and publication metadata.
- **Uncertainty clarified:** which oversight work occurs before, during, and after agent action; which evidence views and heuristics users actually rely on; and what task, trace, artifact/state, burden, authority, and consequence observations are needed to evaluate that work without mistaking reported practice for effective practice.
- **Mode:** narrow expansion feeding consolidation. Before addition the queue had one pending human prerequisite, no claimed work, no pending review/research/source task, and three blocked builds.
- **Duplication/scope check:** adjacent sources study interface treatments, encoded evaluation policy, or broad practitioner portfolios; none reconstructs this study's situated developer oversight taxonomy and heuristics. No software-engineering or oversight-specific subsystem is proposed.
- **Useful completion:** separate descriptive themes from prevalence and efficacy; audit recruitment, organizational dependence, coding/researcher roles, stopping/saturation, negative cases, and release limits; compare the four forms and heuristics against adjacent evidence; and derive bounded retain/repair/test implications for existing general machinery.

Added one task: `review-human-oversight-agentic-systems-practice` (priority 9). No full-paper, representativeness, heuristic-validity, oversight-effect, safety, productivity, professional-validity, or readiness claim was made during scouting.
