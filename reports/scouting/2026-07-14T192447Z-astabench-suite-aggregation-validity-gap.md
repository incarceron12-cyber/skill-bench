# Scouting note — AstaBench suite-aggregation validity gap

**Timestamp:** 2026-07-14T19:24:47Z  
**Scope:** Narrow expansion against charter objectives A/B/D. Queue inspection found 222 tasks: 216 completed, four blocked, one pending consolidation, and one pending human decision. The newest repeated-evaluation review is complete and awaiting canonical consolidation. Existing reviews cite AstaBench and cover SciAgentArena, AARRI, BrowserGym, scientific-work validity, and production evaluation, but no local review or queue task audits AstaBench's multi-benchmark scientific suite, controlled environment, or aggregate claims.

## Substantive finding (triage only)

**AstaBench: Rigorous Benchmarking of AI Agents with a Scientific Research Suite**

- Immutable record selected for review: https://arxiv.org/abs/2510.21652v2
- Immutable PDF: https://arxiv.org/pdf/2510.21652v2
- Official repository: https://github.com/allenai/asta-bench
- Official dataset surface: https://huggingface.co/datasets/allenai/asta-bench
- OpenReview record: https://openreview.net/forum?id=M7TNf5J26u
- The arXiv API reports Jonathan Bragg and 38 coauthors, categories `cs.AI`/`cs.CL`, initial submission on 24 October 2025, and v2 on 21 April 2026. The summary contains no withdrawal notice. The versioned abstract and PDF returned HTTP 200.
- The **v2 abstract** reports 2,400+ problems spanning the scientific discovery process and multiple domains, including tasks inspired by requests to deployed Asta agents; a controlled scientific-research environment with production-grade search tools; nine science-optimized agent classes; and evaluation of 57 agents across 22 classes. These are author-reported abstract claims, not independently verified findings.
- The official GitHub repository is a non-fork Apache-2.0 project created 21 March 2025, with default branch `main` and latest observed push on 17 June 2026. GitHub search exposes separate solve/score tooling, a frozen scorer subproject, and component-specific metrics, but no commit, tag, release, dataset revision, task bytes, or scorer behavior was audited during scouting. The Hugging Face dataset URL was found through the official surfaces, but a direct verification request reset and is not claimed as inspected.
- Repository-wide duplicate search found citations to arXiv `2510.21652` in acquired SciAgentArena, AARRI, and AlphaEval text, but no review, acquisition record, scouting note, or queue task. The missing question is not simply another scientific benchmark: it is whether a common controlled environment and a “holistic” suite preserve the identities, denominators, evidence views, and claims of heterogeneous component benchmarks.
- This is **metadata, abstract, URL, release-location, and duplicate triage only**. The PDF, appendices, v1/v2 changes, task data, code, prompts, tools, environments, scorer implementations, logs, results, cost calculations, and peer-review record were not fully read or audited. No claim is made that task provenance, scientific validity, aggregate comparability, reproducibility, novelty, productivity, professional competence, general capability, or readiness is established.

## Benchmark implication to test

A multi-benchmark suite needs an explicit chain: `source/use case → component construct and unit → immutable task/form/split → environment/tool and solver identity → scorer evidence view/version → component denominator and uncertainty → aggregation/cost policy → licensed suite claim`. A common runner or environment can reduce operational confounding without making component scores commensurable. “Holistic” coverage, 2,400+ examples, and many agent classes do not themselves establish sampled scientific work, downstream research value, or one scalar capability.

The full review should compare paper-time and current release identities; reconstruct component membership, provenance, selection, exposure, metrics, retries, invalids, missingness, and weighting; test solver-to-score compatibility and environment/tool access controls; and inspect whether cost-normalized or aggregate comparisons preserve task-family differences. Read directly against SciAgentArena's dependent pipelines, AARRI's research-judgment outcomes, BrowserGym's adapter boundary, and existing configured-system/metric/validity machinery. No AstaBench-specific schema follows from triage.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier benchmark family), B (suite/component/claim validity), and D (comparative consolidation input).
- **Evidence/artifact sought:** immutable v2 full-text review, v1/v2 change audit, and pinned official code/dataset release inspection.
- **Uncertainty clarified:** whether controlled tools and multi-family breadth support a coherent scientific-research-assistance claim or only bounded component results under one framework.
- **Mode/balance:** one low-priority review task behind the pending repeated-evaluation consolidation; no broad search or bundle was added.
- **Duplication/scope:** complements rather than repeats SciAgentArena, AARRI, and BrowserGym; science is a comparative work family, not a permanent benchmark scope.
- **Useful completion:** preserve component constructs, units, denominators, environment/scorer identities, missingness, uncertainty, aggregation policy, cost, release drift, and strict claim ceilings.

Added `review-astabench-scientific-suite-aggregation-validity` (priority 20). No second task was added.

## Operational note

The required initial `git pull --ff-only` could not authenticate to the HTTPS GitHub remote (`could not read Username`). Local `main` was 21 commits ahead of recorded `origin/main`; the run proceeded from local state. The pre-existing untracked `data/papers/source/` tree was not modified.
