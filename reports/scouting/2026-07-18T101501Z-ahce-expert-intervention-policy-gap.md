# Scouting note — learned expert-intervention policy validity gap

- **Timestamp:** 2026-07-18T10:15:01Z
- **Evidence status:** arXiv metadata/abstract, immutable endpoint checks, HTML heading/external-link triage, targeted release search, and exact repository duplicate searches only. The PDF/source body, methods, participant records, prompts, model outputs, task records, analyses, code, or data were **not** deeply read, downloaded into the repository, reproduced, or audited during scouting.

## Substantive candidate — triage only

**Requesting Expert Reasoning: Augmenting LLM Agents with Learned Collaborative Intervention** — Zhiming Wang, Jinwei He, and Feng Lu; arXiv:2602.22546v1.

- Immutable record/PDF/source: https://arxiv.org/abs/2602.22546v1 · https://arxiv.org/pdf/2602.22546v1 · https://export.arxiv.org/e-print/2602.22546v1
- The arXiv metadata reports v1 dated 26 February 2026. Record, PDF, and source endpoints returned HTTP 200 in this check, with 41,158 HTML bytes, 1,654,679 PDF bytes, and 1,365,737 source-package bytes. The abstract contains no withdrawal or retraction notice.
- The abstract introduces AHCE, an on-demand human–AI collaboration framework whose Problem Identification Module detects impasses, whose Human Feedback Module uses a learned policy to request and synthesize unstructured expert guidance, and whose Query Execution Module resumes action. It reports a 32% increase on normal-difficulty Minecraft tasks and nearly 70% on highly difficult tasks with “minimal human intervention.” These are author-stated claims awaiting full-paper verification; scouting did not establish whether the percentages are relative changes or percentage points.
- Structural HTML triage exposes sections for a zero-shot baseline, preliminary failure study, the three modules, open-ended process-dependent tasks, results, and ablations. This is navigation evidence, not a methods review.
- The HTML exposed no obvious external author code/data link beyond a NeurIPS reference, and targeted exact-title, author, AHCE, and Human Feedback Module searches found no credible official release. This is a time-bounded unresolved release observation, not proof of nonrelease.
- Exact arXiv-ID/title searches found no local review or queue task. Existing YIELD, HAS-Bench, CentaurEval, targeted-inquiry interface, and expert-participation work covers adjacent interaction, participation, and evidence-acquisition boundaries, but not a learned policy that decides when to solicit expert reasoning and translates the reply into an executable plan.

## Why this is a narrow, useful gap

The reusable chain is:

`eligible impasse and request opportunity → trigger policy → expert identity/authority/availability → request content → received guidance → synthesis and interpretation → plan adoption → action/state transition → task consequence → intervention burden and value`.

This directly advances charter objectives A, B, C, and F. The project needs to distinguish expertise delivered from expertise requested, understood, adopted, and made consequential. AHCE may offer a concrete intervention policy and execution trace, while also creating serious validity questions: who the “experts” were and how many contributed; whether their knowledge, instructions, consent, compensation, and independence were recorded; whether the policy was trained or selected on overlapping tasks; whether requests occurred at comparable opportunities; whether endpoint gains identify request timing, guidance content, synthesis, or the whole configured package; and whether “minimal” counts human preparation, waiting, response, and correction burden.

Minecraft is a bounded mechanism case, not a benchmark scope commitment. Game success cannot establish tacit-expertise transfer, professional judgment, expert substitution, cross-domain transport, economic value, or readiness. The full review should preserve task/repeat clusters, missing/failed requests, assistance eligibility, baseline/treatment resource parity, human and model costs, and every link from raw response to executed consequence.

## Charter decision filter and queue action

- **Objectives advanced:** A (human evaluation and production-relevant agent interaction), B (expertise-to-evaluation method), C (traceable intervention machinery), and F (cost-aware expert participation).
- **Concrete evidence:** immutable-v1 full-paper/source review and release audit reconstructing contributor provenance, request opportunities, policies, interactions, synthesis/adoption, outcomes, denominators, ablations, and burden.
- **Uncertainty clarified:** whether AHCE measures genuine expert-reasoning acquisition and efficient intervention, or a coupled configured-package effect under selected game tasks.
- **Mode:** narrow expansion. One autonomous build and one human-decision task were pending, while the review backlog was empty; this avoids another broad landscape search.
- **Duplication/scope check:** exact duplicate searches were negative; adjacent reviews cover different links. Reuse participation, evidence-acquisition, configured-system, intervention, resource, and validity machinery rather than creating a game or human-feedback subsystem.
- **Useful completion:** source-locate the complete request-to-consequence chain, audit contributor and release evidence, resolve percentage and denominator semantics, compare adjacent mechanisms, and preserve strict claim ceilings.

Added one task: `review-ahce-expert-intervention-policy-validity` (review, priority 52). No second source was queued.
