# Scouting note — search-time contamination gap

**Timestamp:** 2026-07-10T10:30:14Z  
**Scope:** Narrow search against research-agenda question 5 (leakage versus trustworthy public evaluation). The queue had three pending operating-layer builds and no pending research/review task, so this run added one lower-priority review rather than repeating broad benchmark discovery.

## Substantive finding (triage only)

**Search-Time Contamination in Deep Research Agents: Measuring Performance Inflation in Public Benchmark Evaluation** — Wang et al., arXiv:2606.05241v1.

- Immutable record: https://arxiv.org/abs/2606.05241v1
- Immutable PDF: https://arxiv.org/pdf/2606.05241v1
- The arXiv API identifies v1, published 2026-06-03, in `cs.CR`/`cs.AI`; the abstract, HTML, and PDF URLs were reachable during this run.
- The abstract defines three increasingly severe retrieval-time contamination classes: benchmark-metadata leakage, question-context leakage, and explicit-answer leakage. It reports detection algorithms, evaluation on six public benchmarks, widespread contamination, and performance inflation of up to 4%, then recommends isolated sandboxes, transparent search trajectories, and controlled benchmark access.
- This is **metadata/abstract and URL triage only**. The paper was not read in full during scouting; its methodology, causal attribution, prevalence, uncertainty, and mitigation claims require immutable full-text review. No official code or dataset URL was identified from the arXiv record during triage.

## Why this is distinct

The repository already distinguishes public requirements from private consequences, records configured execution boundaries, and warns that lessons can memorize private answers. It does not yet have primary-source evidence on contamination that occurs *during retrieval-enabled evaluation*. That threat is distinct from pretraining contamination, valid retrieval of domain evidence, evaluator-cue leakage, and accidental access to local private graders. It directly affects whether public or semi-private source packs and web-enabled trials support capability claims.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier validity evidence), B (expertise/source-pack-to-evaluation methodology), and C (trace, provenance, isolation, validity, and task-operation contracts).
- **Evidence/artifact sought:** a full immutable-v1 review reconstructing the six-benchmark study, contamination detectors, validation protocol, score-inflation estimand, uncertainty, replication dependencies, and mitigation evidence.
- **Uncertainty clarified:** how to distinguish legitimate evidence gathering from construct-bypassing leakage; which traces and access controls license scores; and whether detection matches causally establish inflation.
- **Mode/balance:** narrow expansion into an uncovered validity threat; priority 74 keeps the three pending builds ahead of it.
- **Duplication/scope:** no match for arXiv `2606.05241` or search-time contamination existed in the paper index, reviews, scouting reports, or queue. Deep research is the study setting, not a proposed scope boundary.
- **Useful completion:** claims are checked against full text; false-positive/negative and search-index/time dependencies are assessed; and only nonduplicate implications are mapped into existing source-pack, trial, execution, validity, and task-health objects.

Added `review-search-time-contamination` (priority 74). No second candidate was queued.
