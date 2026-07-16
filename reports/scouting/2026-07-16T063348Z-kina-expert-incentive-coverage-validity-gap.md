# Scouting note — KINA expert-incentive and coverage-validity gap

**Timestamp:** 2026-07-16T06:33:48Z

**Scope:** Narrow expansion against charter objectives A/B/F. After pull, the queue had 311 tasks: 306 completed, three blocked, two pending, and no claimed work. The autonomous research backlog contained one low-priority selective-memory review; the consented real-expert micro-pilot remained the higher-priority human prerequisite. Existing coverage includes ELAIPBench's contingent author/verifier compensation, expert-participation provenance, task health, psychometrics, and bounded-budget comparison, but not a benchmark that combines a formal reviewer-incentive theorem, purported empirical mechanism validation, expert-elicited coverage anchors, and rank-stability reporting. Findings below are **metadata/abstract and structural triage only**, not a full-paper review.

## Substantive finding — triage only

**Knowledge Index of Noah's Ark (KINA)** — Sheng Jin et al.; arXiv:2606.05104v2.

- Immutable record/PDF/HTML: https://arxiv.org/abs/2606.05104v2 · https://arxiv.org/pdf/2606.05104v2 · https://arxiv.org/html/2606.05104v2
- The arXiv API reports v1 submission on 3 June 2026 and v2 update on 4 June 2026, primary category `cs.AI`; the metadata summary contains no withdrawal notice. The immutable v2 abstract, PDF, and HTML endpoints returned HTTP 200.
- The abstract reports 899 multiple-choice knowledge items across 261 fine-grained disciplines. It describes (1) a coverage-style objective over expert-elicited anchors with a `(1−1/e)` greedy guarantee applying to the proxy rather than population representativeness; (2) a bonus-on-bar review tournament claimed to weakly first-order-stochastically dominate flat payment in released-review quality under an incentive threshold `B > ΔC / Δp_min`; (3) evaluation of 42 models; (4) five tool-use evaluations; and (5) bootstrap rank-stability statistics. These are author-reported abstract claims.
- Structural HTML inspection—not body reading—confirmed sections for the two formal guarantees; selection by disciplinary-prototype coverage; bonus-on-bar review; construction; rank stability; empirical validation of the tournament mechanism; tool use and disciplinary diagnostics; proofs; recruitment testing; annotation/review manuals; accepted/rejected examples; appeal handling; LLM filtering; agentic workflow verification; a datasheet; maintenance; and error reporting.
- The immutable HTML links an official-looking dataset and project site: https://huggingface.co/datasets/2077AIDataFoundation/KINA and https://www.2077ai.com/datasets/dataset-kina. Targeted search also found public repositories at https://github.com/weihao1115/KINA-Benchmark and https://github.com/2077AI/KINA. Scouting verified that the repository API endpoints existed but did not inspect files, commits, history, releases, dataset contents, or provenance; a full audit must establish which release is author-owned and paper-linked at what revision.
- Exact-title, arXiv-ID, and `KINA` repository searches found no local review, queue task, or scouting note.

## Why this is distinct

ELAIPBench already shows a real writer–evidence-verifier–answer-verifier contest with contingent pay, but its deep review found no formal game, complete payoff ledger, fixed-pay contrast, or behavioral mechanism evidence. KINA is nonduplicate because it explicitly supplies a comparative theorem and an empirical-validation section. The important question is whether the theorem's assumptions, assignment process, quality variable, noisy bar, effort costs, success-probability gap, and realized bonus are observed closely enough to support a claim about contribution quality—or only a conditional model and selected released outcomes.

The reusable chain is:

`intended construct/use → disciplinary population and expert-anchor authority → coverage proxy and selection algorithm → candidate contribution/review unit → participant expertise, assignment, effort cost, and information → quality state and independent observer → bar/noise/bonus/payment event → revision/appeal/release decision → retained-item validity and contributor welfare → configured-system response matrix → uncertainty/rank decision → transport claim`.

A greedy guarantee for an authored proxy does not establish representativeness of a discipline, profession, or consequential workflow. A theorem about released-review quality does not by itself establish that realized contributors exerted more effort, that selected items are valid, that payment is fair or affordable, or that the mechanism transports to richer agent tasks. Bootstrap instability can bound one leaderboard comparison while leaving task sampling, construct coverage, judge validity, contamination, and capability interpretation unresolved.

## Evidence limits and charter decision filter

Only arXiv API metadata/abstract, endpoint status, immutable-HTML headings/outbound-link inventory, search-result metadata, GitHub repository API existence, local indexes/queue/recent notes, and the completed ELAIPBench review were inspected. The KINA paper body, proofs, appendices, prompts, taxonomy, anchors, items, reviewers, assignments, bars, payments, revisions, appeals, empirical analyses, model runs, repositories, dataset, code, and site were **not read or executed**. No claim is made that KINA is representative, incentive compatible in practice, higher quality than fixed pay, fair, affordable, contamination-free, professionally valid, or suitable for realistic knowledge-work-agent evaluation.

- **Objectives advanced:** A (benchmark validity and expert-participation frontier), B (authority-preserving source/anchor-to-instrument transformation), and F (limited-resource expert incentives).
- **Concrete evidence/artifact:** an immutable-v2 full-paper and pinned official-release audit with exact theorem, mechanism, participant, denominator, payoff, empirical-comparison, coverage, and rank-stability evidence.
- **Uncertainty clarified:** when a formal incentive comparison plus observed tournament outcomes licenses a realized mechanism claim, and when optimizing expert-elicited coverage supports only proxy coverage rather than disciplinary or occupational representativeness.
- **Mode:** narrow expansion feeding human learning and later validation; KINA's MCQ domain is a mechanism test bed, not a scope commitment.
- **Duplication/scope check:** no exact duplicate; mandatory comparison with ELAIPBench and reuse of existing participation, validity, task-health, metric, and psychometric machinery prevents a parallel ontology.
- **Useful completion:** reusable incentive and coverage instrumentation with explicit claim ceilings, or an evidence-backed rejection if assumptions, denominators, release provenance, or empirical contrasts are insufficient.

Added one lowest-priority review task: `review-kina-incentive-representativeness-validity` (priority 1), subordinate to the selective-memory review and consented expert prerequisite.
