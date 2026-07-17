# Scouting note — InciteResearch pre-question elicitation validity gap

**Scouted:** 2026-07-17T07:21:00Z  
**Evidence status:** abstract/metadata-only triage; no full-paper claims

## Candidate

**Jie Yu and Song Qiu, “More Than Can Be Said: A Benchmark and Framework for Pre-Question Scientific Ideation”**

- Immutable arXiv v1 record: https://arxiv.org/abs/2605.06345v1
- Immutable PDF: https://arxiv.org/pdf/2605.06345v1
- arXiv ID: `2605.06345v1`, submitted 2026-05-07
- URL verification: both immutable record and PDF returned HTTP 200; the arXiv API summary contains no withdrawal/retraction notice.
- Release triage: exact-title and `InciteResearch` + `TF-Bench` web/GitHub searches found no clearly author-owned implementation or dataset. This is only an acquisition-time search result; a reviewer must inspect the complete paper and references before recording release absence.

## Why this is a distinct gap

The abstract presents InciteResearch as converting vague or domain-unrelated inputs into a five-dimensional researcher profile anchored by “friction,” then producing a seven-stage causal derivation and a necessity check. TF-Bench reportedly separates domain-related from domain-unrelated inspirations across four scientific modes and grades generated proposals for novelty/impact.

That makes it a direct test of a missing expertise-transfer boundary: **pre-question problem formulation**, before an expert can state an actionable task. Existing reviews cover analytic annotation (Data Therapist), historical next-question imitation (YIELD), simulated novice friction (SimInstruct), networked claim routing, and downstream benchmark-to-risk judgment. None directly audits whether a system recovers a researcher’s own latent concern rather than generating a persuasive new interpretation and scoring it with a coupled evaluator.

The general hypothesis is cross-domain: an elicitation benchmark needs evidence joining `question/input opportunity → caused contributor observation → supported claim/profile update → contributor correction or acceptance → objective/artifact consequence`. Fluent reframing or model-judge novelty cannot substitute for those joins.

## Charter decision filter

- **Objective advanced:** A (frontier research), B (expertise-to-evaluation methodology), D (targeted expansion before reconsolidation), and E (clarify a key validity distinction).
- **Concrete evidence:** immutable full-text/release audit and a claim-bounded review reconstructing participants/inputs, elicitation state, benchmark units, baselines, evaluator evidence views, denominators, uncertainty, and ablations.
- **Uncertainty clarified:** whether TF-Bench measures caused tacit-state elicitation, semantic fidelity, and researcher utility, or configured proposal generation plus judge agreement.
- **Mode:** narrow expansion; the queue already has two higher-priority consolidation tasks, so this review is priority 76 and does not displace them.
- **Duplication/scope check:** repository-wide title/ID search returned no match; the scientific domain is a methodological test bed, not a benchmark scope commitment.
- **Useful completion:** full-paper and release evidence support explicit retain/repair/test implications while keeping researcher acceptance, scientific validity, impact, transfer, and readiness claims false unless separately evidenced.

## Queue action

Added one task: `review-inciteresearch-prequestion-elicitation-validity` (review, priority 76). No other candidates were queued.
