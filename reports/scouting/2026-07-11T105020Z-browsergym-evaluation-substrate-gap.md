# Scouting note — BrowserGym evaluation-substrate gap

**Timestamp:** 2026-07-11T10:50:20Z  
**Scope:** Narrow expansion against charter objectives A/B/C/D after confirming 99 completed tasks, two pending tasks, one blocked real-elicitation task, and BrowserGym as the explicit remaining gap in the interactive-family synthesis. This run did not repeat broad discovery.

## Substantive finding (triage only)

**The BrowserGym Ecosystem for Web Agent Research**

- Immutable arXiv v2 record: https://arxiv.org/abs/2412.05467v2
- Immutable PDF: https://arxiv.org/pdf/2412.05467v2
- Official repository: https://github.com/ServiceNow/BrowserGym
- The search record describes BrowserGym as a shared environment intended to reduce fragmented and inconsistent web-agent evaluation. The official repository exists and its HEAD resolved during scouting to `9e779f087de9a65668b6974d11f9ce9816026e96`.
- This is high leverage because the repository's web/tool/computer evolution synthesis already compares individual benchmark families but explicitly leaves BrowserGym pending. A shared adapter can improve reproducibility while also becoming part of configured-system identity or changing benchmark-specific observations, actions, resets, and evaluator semantics.
- **Evidence status:** search metadata and repository-presence triage only. The paper, appendices, code, adapters, experiments, release history, and evaluator implementations were not read. No claim is made that BrowserGym preserves semantic equivalence across benchmarks, yields valid comparisons, fixes environment instability, or reproduces original benchmark scores.

## Benchmark implication to test

A full audit should treat normalization as a measurement intervention rather than an automatically neutral implementation detail. It should inspect common observation/action contracts, task registration and version identity, benchmark-specific adapters, evaluator and reset behavior, invalid-trial handling, agent representation, and release coupling. Representative adapters should be compared against their benchmark semantics to determine what is preserved, omitted, or transformed.

## Charter decision filter and queue action

- **Objectives advanced:** A (production/benchmark frontier), B (configured-system and validity boundaries), C (evaluation infrastructure), and D (interactive-family consolidation evidence).
- **Evidence/artifact sought:** immutable-v2 full-paper review and pinned official-release audit with page/file locators.
- **Uncertainty clarified:** whether a common browser substrate strengthens reproducibility and comparability or hides construct-relevant benchmark differences.
- **Mode/balance:** one narrow review task; the ready queue otherwise contained one consolidation and one dependent build task.
- **Duplication/scope:** the canonical topic index explicitly marks BrowserGym pending; no review or queued task covered it. Browser interaction is a methodological substrate case, not a domain commitment.
- **Useful completion:** reconstruct the abstraction, task, environment, reset, evaluation, experiment, cost, and maintenance contracts; inspect at least three representative adapters; distinguish paper evidence from current release behavior; derive bounded retain/repair/test implications.

Added `review-browsergym-ecosystem-measurement` (priority 55). No second task was added.
