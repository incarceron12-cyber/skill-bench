# Scouting note — scalable proxy-elicitation validity gap

- **Timestamp:** 2026-07-18T09:28:27Z
- **Evidence status:** arXiv API metadata/abstract, immutable endpoint checks, HTML heading/external-link triage, author project-page triage, targeted release search, and exact repository duplicate searches only. The PDF/source body, appendices, prompts, benchmark rows, human-study records, panel outputs, analyses, or code/data artifacts were **not** deeply read, downloaded, reproduced, or audited during scouting.

## Substantive candidate — triage only

**Scalable Delphi: Large Language Models for Structured Risk Estimation** — Tobias Lorenz and Mario Fritz; arXiv:2602.08889v1.

- Immutable record/PDF: https://arxiv.org/abs/2602.08889v1 · https://arxiv.org/pdf/2602.08889v1
- Author project page: https://t-lorenz.com/projects/scalable-delphi/
- The arXiv API reports immutable v1 submitted and last updated 9 February 2026 in `cs.AI`; its summary contains no withdrawal or retraction notice. Record and PDF endpoints returned HTTP 200, with 41,893 HTML bytes and 334,564 PDF bytes in this check. The e-print endpoint returned HTTP 429, so source acquisition remains unresolved rather than absent. The author project page returned HTTP 200 and links an author-hosted PDF.
- The abstract proposes an LLM adaptation of Delphi using diverse expert personas, iterative refinement, and rationale sharing. Because target risk quantities are unobservable, it evaluates necessary conditions through calibration against verifiable proxies, evidence sensitivity, and alignment with human expert judgments. It reports correlations of `r=0.87–0.95` against three capability benchmarks, systematic response to added evidence, one comparison in which the LLM panel is closer to a human panel than two human panels are to each other, and a reduction from months to minutes. These are author-stated claims awaiting full-paper verification.
- Structural HTML triage exposes sections for the elicitation protocol, design rationale, necessary conditions, corroborating evidence, calibration, evidence sensitivity, qualitative analysis, expert alignment, limitations, complete prompt structures, personas/persona ablation, and benchmark data. This is navigation evidence, not a methods review.
- Neither the arXiv HTML nor the author project page exposed an obvious code/dataset repository, and targeted GitHub/Hugging Face search returned no credible author release. This is a time-bounded unresolved release observation, not proof of nonrelease.
- Exact ID/title/phrase searches found no local review or queue task. Existing benchmark-to-risk expert elicitation work studies human warrants from benchmark observations to consequences, while Human on the Bridge studies expert-authored evaluator context; neither evaluates substituting an LLM panel for the upstream structured expert-judgment process.

## Why this is a narrow, useful gap

The reusable warrant chain is:

`unobservable target and decision use → decomposition and elicitation protocol → persona/model/configuration panel → independent information and discussion rounds → aggregate estimate and uncertainty → verifiable proxy calibration → evidence intervention sensitivity → human-panel comparison and disagreement → target-domain transport → decision consequence`.

This directly advances charter objectives A, B, E, and F. Near-zero-cost expert participation is a project goal, but replacing unavailable experts with model personas could erase precisely the authority, situated cues, disagreement, and tacit judgment the benchmark aims to preserve. The paper may instead provide a useful bounded proxy instrument if it clearly separates observable necessary conditions from the unobservable target claim.

The review must test whether benchmark scores are legitimately mapped to the elicited risk quantities; whether correlations use independent units and uncertainty appropriate to repeated tasks, benchmarks, models, or panels; whether model personas create actual epistemic diversity or dependent samples; whether evidence additions are prospective interventions rather than answer cues; whether human panels are independent, sufficiently powered, and comparable; and whether calibration on observable proxies transports to unobservable high-stakes risks. Panel agreement is not expert authority, closeness to one human aggregate is not source-faithful expertise, and elapsed generation time is not complete cost or decision utility. Cybersecurity is a bounded method case, not a benchmark scope commitment.

## Charter decision filter and queue action

- **Objectives advanced:** A (expert judgment and scalable evaluation), B (expertise-to-evaluation methodology), E (clear distinctions among evidence and project hypotheses), and F (feasible expert participation).
- **Concrete evidence:** immutable-v1 full-paper review and release audit reconstructing prompts, personas, rounds, benchmark/proxy mappings, human-panel provenance, dependence, uncertainty, interventions, denominators, and resource claims.
- **Uncertainty clarified:** which necessary conditions can warrant a configured LLM proxy-estimation instrument and which authority, tacit-transfer, professional-judgment, decision-utility, and replacement claims still require real experts.
- **Mode:** narrow expansion. One build task is pending, the only other pending task requires human authorization, and the autonomous review backlog was empty; this avoids another broad benchmark search.
- **Duplication/scope check:** adjacent reviews cover different edges. Reuse participation, configured-system, metric, task-health, resource, and validity machinery; add no LLM-panel or cybersecurity subsystem absent stronger evidence.
- **Useful completion:** source-locate every estimate and denominator, audit independence/calibration/transport/release status, compare against the two adjacent reviews, and preserve strict claim ceilings.

Added one task: `review-scalable-delphi-proxy-elicitation-validity` (review, priority 53). No second source was queued.
