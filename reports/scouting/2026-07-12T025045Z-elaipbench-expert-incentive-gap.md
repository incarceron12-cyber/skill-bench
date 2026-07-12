# Scouting note — expert benchmark-author incentive gap

**Timestamp:** 2026-07-12T02:50:45Z  
**Scope:** Narrow expansion against charter objectives A/B/F. Repository inspection found 135 completed tasks, one pending build-validation task, one blocked real-elicitation task, and no pending source/research/review work. The corpus has strong participation-governance and expert-labor-economics coverage but no audit of an implemented incentive mechanism for expert benchmark authors and verifiers.

## Substantive finding (triage only)

**ELAIPBench: A Benchmark for Expert-Level Artificial Intelligence Paper Understanding**

- Immutable arXiv target: https://arxiv.org/abs/2510.10549v2
- PDF: https://arxiv.org/pdf/2510.10549v2
- Search metadata describes paired Question Writer and Answer Verifier roles with performance-contingent compensation, presented as a game-theoretic mechanism intended to make careful annotation an equilibrium. The benchmark concerns expert AI-paper questions, but the transferable research question is how contributor incentives affect benchmark-item construction and verification.
- Repository-wide duplicate search found no title, `ELAIPBench`, or arXiv `2510.10549` match.
- This is **metadata/search-result triage only**. The PDF, appendices, participants, payoff equations, empirical results, code, data, instructions, and any official release were not read or inspected. No claim is made about incentive compatibility, annotation quality, expert validity, fairness, contributor welfare, cost, scalability, reproducibility, or cross-domain transfer.

## Benchmark implication to test

A full paper-and-release audit should separate a theoretical equilibrium under stated assumptions from observed contributor behavior and benchmark quality. It should reconstruct selection, compensation, writer/verifier information and dependence, item acceptance and disputes, exclusions and attrition, quality/difficulty measures, costs, and failure modes. The relevant comparison is with existing participation-governance and expert-labor-economics evidence; the goal is a reusable expert-contribution incentive analysis, not an AI-paper QA scope commitment.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier benchmark construction), B (expertise-to-evaluation transformation), and F (feasible expert participation and incentives).
- **Evidence/artifact sought:** immutable full-paper review plus pinned official-release audit, with page/file locators.
- **Uncertainty clarified:** whether an implemented author-verifier payment game improves expert contribution quality, versus selecting or reshaping observable item properties under untested assumptions.
- **Mode/balance:** narrow expansion; no ready source/research/review task existed.
- **Duplication/scope:** no repository duplicate; adjacent reviews do not audit an implemented author-verifier mechanism. The domain is a bounded case for a cross-domain participation hypothesis.
- **Useful completion:** distinguish mechanism theory from empirical evidence and bound quality, expertise, fairness, welfare, cost, scalability, and generalization claims.

Added `review-elaipbench-expert-author-incentive-validity` (priority 51). No second task was added.
