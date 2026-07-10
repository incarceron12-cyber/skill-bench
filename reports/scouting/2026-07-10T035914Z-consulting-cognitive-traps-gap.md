# Scouting note — consulting cognitive-trap benchmark

**Timestamp:** 2026-07-10T03:59:14Z  
**Scope:** Narrow primary-source search for evidence-traceable memo/spreadsheet pilot inputs. The queue was healthy (six pending tasks), so this run added one task only and did not repeat broad agent-benchmark searches.

## Substantive finding (triage only)

**Evaluating Deep Research Agents on Expert Consulting Work: A Benchmark with Verifiers, Rubrics, and Cognitive Traps** — Asthana, Saksena, and Sahu, arXiv:2605.17554v3 (2026).

- Immutable paper record: https://arxiv.org/abs/2605.17554v3
- Immutable PDF: https://arxiv.org/pdf/2605.17554v3
- OpenReview record: https://openreview.net/forum?id=6qtRHQwpC9
- Search-result metadata describes 70 SME-authored management-consulting prompts, cognitive traps intended to penalize surface-pattern reasoning, deterministic verifiers plus rubric grading, and publicly released benchmark/evaluation artifacts.
- This was **abstract/search-metadata triage only**. The paper and artifacts were not read in full during scouting, so the reported design details and counts must be verified against the immutable PDF and release.

## Why this fills a current gap

The queued ACTA review addresses how to elicit tacit expertise, while the first pilot requires source-traceable hidden requirements, professional traps, artifacts, and checks. This benchmark appears to provide the closest downstream primary example of converting SME-authored consulting work into cognitive traps, verifiers, and rubrics. A full review should test whether its authoring and validation evidence is strong enough to instantiate those pilot primitives rather than merely borrowing labels.

The same narrow search surfaced BlueFin, FrontierFinance, an end-to-end business-spreadsheet benchmark, and BankerToolBench. They were deferred because the local index already contains MBABench and other spreadsheet benchmarks, while the consulting source contributes the more distinct cognitive-trap pattern.

## Queue action

Added one task: `review-consulting-cognitive-traps` (priority 87). It requires immutable PDF acquisition, released-artifact inspection, a full evidence-cited review, and explicit mappings to the expertise-transfer schema and first pilot.
