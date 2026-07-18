# Scouting note — policy-grounded supervision/decision-utility gap

- **Timestamp:** 2026-07-18T22:22:42Z
- **Evidence status:** arXiv API metadata/abstract, immutable endpoint checks, arXiv-HTML outbound-link discovery, web release search, and exact local duplicate searches only. The PDF/source body, cases, policy corpus, expert decisions, questionnaire instrument/rows, system implementation, memory records, traces, or analyses were **not** deeply read, downloaded into the repository, executed, reproduced, or audited during scouting.

## Substantive candidate — triage only

**Pezego-HITL: A policy-grounded large language model architecture for agricultural extension in Ghana** — Shunbao Li et al.; arXiv:2607.13934v1 (submitted 2026-07-15).

- Immutable record/PDF/HTML/source: https://arxiv.org/abs/2607.13934v1 · https://arxiv.org/pdf/2607.13934v1 · https://arxiv.org/html/2607.13934v1 · https://export.arxiv.org/e-print/2607.13934v1
- At scouting time these endpoints returned HTTP 200 with observed response sizes of 43,943, 2,103,611, 453,407, and 2,044,318 bytes respectively.
- The abstract describes a two-year design/evaluation programme, a P-EVAL protocol treating policy-constrained assessment as a safety/helpfulness/latency/expert-workload allocation problem, 1,240 simulated field cases, offline automatic-judge calibration against human expert decisions (`κ=0.77`), validated-memory routing/cache reuse, and questionnaires from 30 Ghanaian extension officers and 36 smallholder farmers. It reports policy-alignment, agronomic-utility, latency, and cache-reuse endpoints. These are author-stated abstract claims awaiting full-paper verification.
- The immutable HTML exposed no project code/data link; the only candidate implementation-related outbound link found was the cited model page at https://huggingface.co/Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash. Exact-title web search also found no official project release. A reviewer should retry release discovery rather than infer permanent absence.
- Exact title, ID, and distinctive-phrase searches found no local review or queue task. Existing AgentRewardBench, Pista/HiLSVA, online skill-memory value, Scalable Delphi, production-validity, and participation reviews cover adjacent judge, oversight, memory, proxy-estimation, and human-study boundaries, but not this joint policy/safety/utility/latency/supervision allocation instrument.

## Why this is a narrow, useful gap

The reusable chain is:

`authorized/versioned policy and agronomic evidence → simulated or real query provenance → expert decision/disagreement/adjudication → calibrated automatic observer → memory admission and valid-time scope → routing/cache opportunity and realized reuse → advice artifact → policy and agronomic checks → escalation and expert burden → recipient uptake/decision → crop, household, and adverse consequence → longitudinal non-regression`.

This is directly relevant to charter objectives A–C and E because it joins domain authority, scalable grading, context/memory reuse, human oversight, resource cost, and decision support in one reported production-oriented system. It also presents a sharp validity boundary: agreement with expert decisions, simulated-query endpoint scores, cache reuse, lower latency, and stakeholder questionnaires do not by themselves establish correct policy authority, safe stale-memory handling, reduced realized expert workload, advice adoption, agronomic benefit, expert substitution, or deployment readiness.

## Charter decision filter and queue action

- **Objectives advanced:** A (production evaluation, human/expert evaluation, context/memory), B (authority-to-advice-to-consequence lineage), C (plural graders, routing, resource and supervision records), and E (decision-relevant claim boundaries).
- **Concrete evidence:** immutable-v1 full-paper review with PDF/text provenance, release-presence audit, and reconstruction of case, expert-label, observer, routing, workload, questionnaire, and outcome denominators.
- **Uncertainty clarified:** whether P-EVAL measures a configured simulated-query package and stakeholder perceptions or supports stronger supervision-allocation, decision-utility, field-effectiveness, or safe-reuse claims.
- **Mode:** narrow expansion/human learning. Two higher-priority consolidations and one human decision remain pending; this adds one lower-priority review buffer rather than repeating a broad search.
- **Duplication/scope check:** exact searches were negative and adjacent reviews are explicit comparators. Ghanaian agricultural extension is a bounded mechanism case, not a benchmark-domain commitment.
- **Useful completion:** separate policy provenance, gold-label authority, judge calibration, memory eligibility, cache realization, expert workload, perceived utility, actual uptake, real consequence, and readiness; reuse existing contracts and preserve claim ceilings.

Added one task: `review-pezego-policy-expert-workload-validity` (review, priority 42). No second task was queued. `Beyond Consistent Scenarios` (arXiv:2607.12414v1) was triaged but deferred because its expert-elicited cross-impact scenario mathematics is less direct than the current missing evaluation/supervision/consequence boundary and risks drifting into domain modeling without an immediate benchmark artifact.
