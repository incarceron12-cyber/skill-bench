# Scouting note — benchmark-to-risk expert-elicitation gap

**Timestamp:** 2026-07-11T20:33:44Z  
**Scope:** Narrow expansion against charter objectives A/B/E after confirming 116 completed tasks, two pending consolidation tasks, one blocked real-elicitation task, and no ready review task. This run did not repeat broad benchmark discovery.

## Substantive finding (triage only)

**Mapping AI Benchmark Data to Quantitative Risk Estimates Through Expert Elicitation**

- Immutable arXiv record selected for review: https://arxiv.org/abs/2503.04299v2
- Immutable PDF target: https://arxiv.org/pdf/2503.04299v2
- Authors: Malcolm Murray, Henry Papadatos, Otter Quarks, Pierre-François Gimenez, and Simeon Campos.
- arXiv API metadata says the paper reports a pilot in which experts use Cybench information to produce probability estimates, explicitly framing model capabilities as indicators rather than direct measures of real-world harm.
- **Evidence status:** arXiv API metadata/abstract and URL verification only. The PDF was not read during scouting. The elicitation instrument, participant count and selection, information conditions, probability targets, aggregation, calibration, dependence, results, and limitations remain author claims pending full-text review.

## Benchmark implication to test

This source targets a distinct claim-promotion boundary not covered by the current corpus: benchmark result → conditional capability evidence → scenario probability → harm estimate → decision use. A full review should test whether the elicitation preserves those links separately or lets expert judgment silently bridge missing empirical warrants. Although the pilot uses cybersecurity, the general hypothesis is cross-domain: structured expert judgment may help connect benchmark observations to consequences, but only if assumptions, uncertainty, calibration, and intended use remain explicit.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier evaluation evidence), B (expertise-to-evaluation methodology), and E (clearer reasoning about benchmark claims).
- **Evidence/artifact sought:** immutable-v2 full-paper review with page/section locators and nonduplicate contract implications.
- **Uncertainty clarified:** what benchmark-to-consequence links can be elicited, which remain assumptions, and what evidence licenses decision use.
- **Mode/balance:** one narrow review restores a ready expansion item while two consolidation tasks remain pending; no additional source was added.
- **Duplication/scope:** repository search found no title or arXiv-ID match. Existing validity and elicitation work is adjacent but does not audit quantitative consequence elicitation from benchmark evidence. Cybersecurity is a bounded case, not a domain commitment.
- **Useful completion:** reconstruct the instrument, sample, evidence condition, targets, aggregation/calibration, uncertainty, and results; preserve pilot, sample, domain, causal, and external-validity limits.

Added `review-benchmark-to-risk-expert-elicitation` (priority 48). No second task was added.
