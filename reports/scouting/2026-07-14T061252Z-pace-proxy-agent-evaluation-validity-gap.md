# Scouting note — proxy-to-agentic evaluation validity gap

**Timestamp:** 2026-07-14T06:12:52Z  
**Scope:** Narrow expansion against charter objectives A/B/D. Queue inspection found 209 tasks: 205 completed, two blocked, and two pending consolidations. The review backlog was empty but the implementation/consolidation backlog was healthy, so scouting targeted one explicit gap rather than repeating a broad search: the corpus covers within-benchmark panel reduction and task-level psychometrics, but not cross-instrument prediction of expensive configured-agent scores from cheap non-agentic items.

## Substantive finding (triage only)

**PACE: A Proxy for Agentic Capability Evaluation**

- Immutable latest arXiv record: https://arxiv.org/abs/2607.02032v2
- Immutable PDF: https://arxiv.org/pdf/2607.02032v2
- Author-linked code: https://github.com/neulab/pace
- Author-linked dataset: https://huggingface.co/datasets/neulab/pace-bench
- The arXiv API identifies Yueqi Song, Lintang Sutawika, Jiarui Liu, Lindia Tjuatja, Jiayi Geng, Yunze Xiao, Daniel Lee, Aditya Bharat Soni, Vincent Lo, Xiang Yue, and Graham Neubig as authors. It records v1 on 2 July 2026 and v2 on 6 July 2026; the abstract contains no withdrawal notice.
- The abstract describes a learned proxy that selects atomic instances from 19 non-agentic benchmarks and regresses their scores onto four expensive agentic benchmarks. It reports experiments across 14 models, leave-one-model-out mean absolute error below 4%, Spearman correlation above 0.80, pairwise ranking accuracy around 85%, and cost below 1% of full agentic evaluation. These are discovery leads only: exact targets, source pools, model/configuration frame, selection nesting, hyperparameter access, uncertainty, cost accounting, and every denominator require full verification.
- Structural inspection of immutable v2 HTML—not a full reading—confirmed sections on regression, local/global instance selection, experimental setup, performance–cost tradeoffs, selected-allocation analysis, bootstrap analysis, budget sweeps, Lasso/Ridge baselines, and limitations. The released code and data were not inspected.
- The paper’s distinctive question differs from the already reviewed *Efficient Benchmarking of AI Agents* (`2603.23749v1`). That work selects mid-difficulty tasks **inside an agent benchmark** to preserve rankings under some scaffold/temporal shifts; PACE learns a mapping **across instruments**, from cheap atomic items to full agentic aggregate scores. This adds a criterion/predictive-validity and construct-substitution problem: high held-out-model correlation can coexist with losing harness, tool, memory, interaction, artifact, safety, recovery, and consequence demands.
- The official links are embedded in the immutable paper HTML. `git ls-remote` verified acquisition-time code HEAD `dc2ef80e00addd519e7d8479f875cc3ecb46c6cb`; GitHub reports the repository was pushed on 7 July 2026, after v2. The Hugging Face API verified a public, ungated dataset at revision `ce177cfe25bc8c8259cadecb56d4db8d9d36ab18`, last modified 6 July 2026. Paper/release correspondence and license terms remain unaudited, so current bytes must not be treated as the exact empirical instrument.
- Repository-wide searches for the arXiv ID, exact title, “PACE-Bench,” and “proxy benchmark” found no duplicate source, review, or queue task. Efficient Benchmarking and Agent Psychometrics address task reduction/difficulty; the configured-system and validity work addresses harness identity and claim promotion. None currently audits whether a cheap non-agentic proxy preserves agentic scores, rankings, diagnostics, or decisions under new models, scaffolds, benchmark versions, and capability shifts.
- A neighboring paper, *Beyond Static Leaderboards: Predictive Validity for the Evaluation of LLM Agents* (`2606.19704v1`), was verified but not queued. Its position-level OOD ranking thesis overlaps existing validity and configured-system work, while PACE provides the more concrete released cross-instrument test and is therefore the stronger single addition under a healthy backlog.
- This is **metadata/abstract, URL, section-structure, release-existence, and duplicate triage only**. The PDF, appendices, code, dataset, source/target response matrices, selected items, configurations, results, and bootstrap records were not fully read or audited. No claim is made that PACE predicts unseen agent architectures, future benchmark versions, configured systems, diagnostic failures, professional quality, safety, production performance, or deployment readiness.

## Benchmark implication to test

A cheap proxy needs an explicit transport argument rather than correlation alone: `target agentic construct and configured-system frame → source atomic-item pool and exposure → model/configuration sampling frame → selection/training/validation partition → frozen proxy and score mapping → held-out model/scaffold/time/benchmark-version predictions → rank, absolute-score, calibration, subgroup, and decision loss → periodic full-suite sentinel → drift/saturation trigger → licensed use`. Full review should test whether leave-one-model-out validation is nested outside feature/item selection; whether model families and shared training data make folds dependent; whether aggregate target scores hide diagnostic reversals; whether the proxy survives scaffold/harness changes; whether selected atomic items leak benchmark identity or target outcomes; and whether uncertainty and residuals justify model selection or routing decisions. A proxy may be useful for development triage while remaining invalid for professional-quality, artifact, safety, or readiness claims.

Any transfer should extend existing response-matrix, configured-system, metric-monitoring, task-health, psychometric, and validity machinery rather than create a PACE-specific schema. The key comparison is full-suite sentinel versus proxy, not proxy versus nothing.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier scalable agent evaluation), B (validity and intervention/instrument separation), and D (comparative consolidation after review).
- **Evidence/artifact sought:** immutable full-v2 review plus pinned code/dataset audit reconstructing source/target frames, model/configuration identities, selection and validation, result denominators, uncertainty, cost, release correspondence, and drift policy.
- **Uncertainty clarified:** whether atomic non-agentic items can support a bounded cheap prediction of expensive agent-benchmark aggregates, and which agentic constructs or configured-system changes invalidate that substitution.
- **Mode/balance:** one low-priority review task restores a minimal research backlog while leaving both pending consolidations at higher priority.
- **Duplication/scope:** complements rather than repeats within-benchmark task reduction and psychometrics; the four target benchmarks are an instrument-transport case, not a scope commitment or a proposal to replace realistic knowledge-work evaluation.
- **Useful completion:** verify the complete selection/validation pipeline and releases; separate score prediction, rank preservation, calibration, subgroup/diagnostic preservation, decision loss, and temporal/scaffold transport; compare directly with the reviewed mid-range filter; preserve strict configured-agent, professional-validity, capability, safety, production, and readiness ceilings.

Added `review-pace-proxy-agent-evaluation-validity` (priority 25). No second task was added.
