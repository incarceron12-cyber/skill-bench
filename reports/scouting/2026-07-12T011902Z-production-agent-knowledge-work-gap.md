# Scouting note — production agent knowledge-work usage gap

**Timestamp:** 2026-07-12T01:19:02Z  
**Scope:** Narrow expansion against charter objectives A/B/D after confirming 127 completed tasks, two pending tasks, one blocked real-elicitation task, and no pending source/research/review task. Existing benchmark-family coverage is strong, so this run targeted production evidence about actual agent-mediated work rather than repeating broad benchmark discovery.

## Substantive finding (triage only)

**How AI Agents Reshape Knowledge Work: Autonomy, Efficiency, and Scope**

- Immutable arXiv v2 record: https://arxiv.org/abs/2606.07489v2
- Immutable PDF: https://arxiv.org/pdf/2606.07489v2
- Authors: Jeremy Yang, Kate Zyskowski, Noah Yonack, and Jerry Ma.
- arXiv API metadata says the paper analyzes production data from Perplexity Search and Computer. It reports a comparison using sessions with near-identical initial queries attempted with both products, plus estimates of autonomous work, follow-up behavior, dissatisfaction, completion time/cost, occupational breadth, cognitive level, expertise breadth, and composite-task incidence.
- This is directly relevant because the corpus has strong benchmark-design, work-centered reporting, and production-evaluation coverage, but no review of observed product use comparing assistant-like search with an autonomous computer agent on ostensibly matched work requests.
- Repository-wide duplicate search found no title or arXiv `2606.07489` match. Existing AlphaEval, JobBench, GDPval, and work-centered reviews are adjacent but do not audit this production telemetry or comparison design.
- This is **metadata/abstract triage only**. The PDF, methods, appendices, data, code, measures, analyses, and robustness checks were not read. All numerical and causal language remains author-reported pending full-text review. No claim is made about productivity, output quality, worker benefit, task completion, occupational representativeness, professional validity, or deployment readiness.

## Benchmark implication to test

A full review should determine whether production telemetry can supply bounded evidence for benchmark task demand, composite-work structure, follow-up/handoff behavior, and cost-aware usefulness. The central validity question is whether near-identical initial queries support a credible comparison once product interface, user selection, task intent/difficulty, completion observation, quality proxies, and model-coded work attributes are considered. The transferable output is a production-use-to-benchmark-demand boundary, not a Perplexity-specific benchmark or a labor-impact claim.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier production evidence), B (demand and workflow evidence entering benchmark design), and D (narrow expansion beyond benchmark releases).
- **Evidence/artifact sought:** immutable-v2 full-paper review with page/section locators and bounded contract implications.
- **Uncertainty clarified:** what production usage can establish about work demand, autonomy, task composition, downstream interaction, time/cost, and quality—and where selection, measurement, and counterfactual assumptions block promotion.
- **Mode/balance:** narrow expansion; the ready queue had no source/research/review task.
- **Duplication/scope:** no repository duplicate; the source spans production knowledge work and will not define a product, occupation, or interface commitment.
- **Useful completion:** reconstruct sampling, matching, product treatments, measures, coding, uncertainty, robustness, proprietary-evidence limits, and exact inference population; separate telemetry, model-coded variables, estimates, and interpretation; derive only nonduplicate retain/repair/test implications.

Added `review-production-agent-knowledge-work-usage-validity` (priority 54). No second task was added. EvoAgentBench (`2607.05202v1`) was triaged but not queued because the corpus already covers self-evolving agents and the production-use gap is more directly charter-relevant.
