# Scouting note — professional-email recipient-consequence validity gap

- **Timestamp:** 2026-07-18T00:50:00Z
- **Evidence status:** arXiv API metadata/abstract, URL checks, targeted duplicate search, GitHub repository metadata/tree inspection, and small README/code inspection only. The paper body, appendices, participant flow, ethics materials, private dataset, complete analyses, or reported results were **not** deeply read, downloaded, reproduced, or audited during scouting.

## Substantive candidate — triage only

**Playful AI in Professional Email: A Field Experiment on Tone and Recipient Engagement** — Ziv Ben-Zion and Teddy Lazebnik; arXiv:2607.11749v1.

- Immutable record/PDF: https://arxiv.org/abs/2607.11749v1 · https://arxiv.org/pdf/2607.11749v1
- Official analysis repository: https://github.com/zivbz1/Playful-AI-in-Professional-Email at inspected commit [`e42fae22fdee831f0d47fd6deab7cfefee5cd0bb`](https://github.com/zivbz1/Playful-AI-in-Professional-Email/commit/e42fae22fdee831f0d47fd6deab7cfefee5cd0bb).
- HEAD checks returned HTTP 200 for the immutable arXiv record/PDF and repository. The arXiv API reports v1 submitted and last updated 13 July 2026; its summary contains no withdrawal or retraction notice.
- The abstract describes a randomized crossover field experiment in which 121 employees at six companies sent 16,880 work emails over three weeks under unaided, GPT-5 playful-rewrite, and GPT-5 professional-rewrite conditions. It reports condition effects on automated positivity, no direct condition effects on opening/replying/time, and a significant indirect pathway through within-sender positivity. These are author-stated abstract claims awaiting full-paper verification; the mediation interpretation is especially not established by this triage.
- GitHub API inspection found a public, unarchived, non-fork repository with no declared license and only four files. The README says the canonical R pipeline and an independent Python implementation expect an email-level CSV and produce descriptive, mixed-model, survival, and mediation outputs. The Python code visibly uses sender-clustered GEE, sender-stratified Cox models, within-sender positivity centering, and Sobel indirect effects. The README states that the 16,880-row de-identified dataset is request-only for ethical reasons and that no raw email text, names, or addresses are included. Thus the release exposes analysis logic but not the empirical rows needed to reproduce the study.
- Exact ID/title searches found no local review, queue task, or scouting note. Existing reviews cover criterion-to-business-outcome association, Nubank offline/online evaluation, the Chiron workflow field study, AlphaEval production demand, professional value, and production telemetry, but none directly audits sender-randomized AI transformation of a real communication artifact joined to recipient behavior.

## Why this is a narrow, useful gap

The relevant chain is:

`sender/workplace/recipient population → consent and communication authority → crossover assignment, order, and period → original email and rewrite exposure → sender inspection/adoption/edit/send → delivered artifact identity and tone observation → recipient exposure and measurement → open/reply/time event → direct treatment estimand → mediator observation and temporal assumptions → conditional engagement effect → communication utility, burden, productivity, value, or stakeholder consequence`.

This is unusually useful because most reviewed professional-artifact benchmarks stop at authored checks, model judgments, or synthetic state. A real field intervention with recipient events can test the downstream-consequence rung that the charter treats as distinct from artifact conformance. Yet sender randomization does not automatically randomize email positivity, recipient attention, email purpose, or the mediator; repeated emails nest within senders, companies, and potentially recipients; period/order, carryover, adoption, missing tracking, censoring, and workplace selection can alter the estimand; automated sentiment and LLM-detection scores need observer validity; and a Sobel product of a randomized treatment path and an observational within-sender mediator path is not automatically a causally identified mediation effect. Opens and replies are also engagement proxies, not necessarily quality, trust, productivity, value, or benefit.

Professional email is a bounded communication-artifact stress case for reusable treatment-fidelity, recipient/consequence, clustered-outcome, mediation, participation, privacy, and validity machinery—not a proposal to narrow `skill-bench` to writing or workplace email.

## Charter decision filter and queue action

- **Objectives advanced:** A (production and realistic knowledge-work evidence), B (artifact-to-recipient consequence and validity), and E (a clear field-experiment lesson for benchmark interpretation).
- **Concrete evidence:** immutable-v1 full-paper review plus a pinned audit of the canonical R analysis, Python verification, unavailable-data boundary, participant/company/email denominators, treatment realization, observers, outcomes, and statistical estimands.
- **Uncertainty clarified:** when a transformed professional artifact can be linked to recipient behavior; which direct, associative, mediated, utility, value, capability, and readiness claims are actually licensed; and what benchmark evidence is still missing between artifact score and downstream consequence.
- **Mode:** narrow expansion/human learning. Two evidence-backed consolidations and one human prerequisite were pending, but no autonomous review task remained; one review restores a bounded evidence path without restarting broad search.
- **Duplication/scope check:** adjacent reviews cover separate links, not this real sender-randomized artifact-to-recipient chain. Reuse existing consequence, metric, configured-system, participation, artifact, and validity records; add no email-specific schema or pilot.
- **Useful completion:** page/path-grounded reconstruction of recruitment and sampling, consent/privacy, crossover sequence and carryover, sender/company/recipient hierarchy, email eligibility, treatment delivery/adoption, content and observer validity, event capture/censoring, direct and indirect estimands, model assumptions, missingness/exclusions, multiplicity, robustness, paper-code-data conformance, and bounded retain/repair/test implications.

Added one task: `review-professional-email-recipient-consequence-validity` (review, priority 57). No other candidate was queued. PolyWorkBench surfaced in search but was not queued because immutable v1/v2 full text is already present locally and this run found no evidence that a new duplicate task was warranted.
