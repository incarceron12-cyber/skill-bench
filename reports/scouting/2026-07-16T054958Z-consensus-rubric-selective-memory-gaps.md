# Scouting note — consensus-rubric and selective-memory validity gaps

**Timestamp:** 2026-07-16T05:49:58Z

**Scope:** Narrow expansion against charter objectives A/B/C. After pull, the queue had 309 tasks: 304 completed, three blocked, two pending, and no claimed work. The actionable backlog was one high-priority consolidation plus one human prerequisite; there were no pending source/research/review tasks. Existing coverage is extensive, so this run used targeted 2026 arXiv searches only for (1) expert-removing rubric pipelines and (2) selective shared persistence in an artifact workspace. Findings are **metadata/abstract and structural triage only**, not full-paper reviews.

## 1. FinResearchBench II: consensus and discrimination are not criterion authority

**FinResearchBench II: A Deep Research Benchmark with Consensus-Derived Gold Rubrics for Distinguishing Financial Report Quality** — Beidi Luan et al.; arXiv:2607.12252v2.

- Immutable current record/PDF/HTML: https://arxiv.org/abs/2607.12252v2 · https://arxiv.org/pdf/2607.12252v2 · https://arxiv.org/html/2607.12252v2
- The arXiv API reports v1 submission on 14 July 2026 and v2 update on 15 July 2026, primary category `cs.CL`; the metadata summary contains no withdrawal notice. All three v2 endpoints returned HTTP 200.
- The abstract reports 104 real-world user queries, 14,450 query-specific candidate rubrics synthesized from model-generated reports, a sampled three-human-expert versus three-LLM comparison, 98.67% label agreement conditional on jointly unanimous items, and two filters: unanimous LLM consistency over every report for a query, then at least one majority-yes and one majority-no across tested systems. It reports attrition to 3,687 consistency-passed and 2,600 distinguishable criteria, then rankings across ten systems. These are author-reported abstract claims.
- Structural HTML inspection—not body reading—confirmed sections for data collection, rubric construction, the expert-free pipeline, within-model batched stability, human–LLM validation, filtering statistics, consensus-derived evaluation, sensitivity analyses, a rubric-evaluation prompt, and query examples. No author-owned code/data link appeared in the immutable HTML outbound-link inventory. Exact-title/ID local search found no duplicate.
- The distinct validity question is whether unanimity and tested-system discrimination produce an authoritative criterion instrument, or preferentially retain judge-stable items that separate this particular report pool. Conditioning agreement on jointly unanimous items cannot establish reliability on disagreements; deriving criteria from model reports and retaining items by observed system outcomes couples source, instrument, and benchmark comparison.

**Reusable chain:** `query/user provenance → intended construct/use → candidate reports → criterion synthesis → expert/LLM evidence views and item decisions → agreement/disagreement frame → consistency filter → distinguishability filter → retained criterion authority/dependence → system scores/ranks → decision and transport claim`.

## 2. Shared selective persistent memory: bytes, adoption, authority, and consequence

**Shared Selective Persistent Memory for Agentic LLM Systems** — Sanjana Pedada, Aditya Dhavala, and Neelraj Patil; arXiv:2607.09493v1.

- Immutable record/PDF/HTML: https://arxiv.org/abs/2607.09493v1 · https://arxiv.org/pdf/2607.09493v1 · https://arxiv.org/html/2607.09493v1
- The arXiv API reports immutable v1 submitted 10 July 2026, primary category `cs.AI`; the metadata summary contains no withdrawal notice. All endpoints returned HTTP 200.
- The abstract describes an implemented collaborative, Git-versioned artifact workspace that retains task specifications, data schemas, tool configurations, and output constraints while discarding session reasoning traces. It reports 96% completion with selective memory versus 79% without memory and 71% with full history across three enterprise scenarios, a 14× task-time and 97× token comparison, and 12/12 zero-token-refresh trials on four public datasets. These are author-reported abstract claims.
- Structural HTML inspection—not body reading—confirmed formulation, memory decomposition, selective forgetting, session-start composition, zero-token refresh, collaborative sharing, implementation, memory-condition ablation, public-data replication, token efficiency, user study, limitations, ethics, and a composition example. The outbound-link inventory exposed related platforms/frameworks but no obvious author-owned release. Exact-title/ID local search found no duplicate.
- The distinct question is whether the reported treatment isolates reusable authorized memory rather than task packaging, stale-history harm, or workspace implementation differences. Retained bytes, session access, prompt composition, semantic adoption, causal use, artifact correctness, cross-user authorization, deletion, refresh equivalence, and collaboration utility are non-inheriting observations.

**Reusable chain:** `source/participant authority → retained item and valid time → selection/forgetting rule → versioned shared workspace and access policy → session composition → agent receipt/adoption → artifact/state change → independent consequence → stale/conflict/deletion behavior → cost and cross-user utility`.

## Evidence limits and queue action

Only arXiv API metadata/abstracts, endpoint status, immutable-HTML headings/outbound-link inventories, targeted web/GitHub result metadata, repository indexes, recent scouting notes, and exact local duplicate searches were inspected. The paper bodies, appendices, prompts, queries, reports, rubrics, labels, expert records, model calls, memory implementation, tasks, artifacts, user-study records, statistics, repositories, and data were **not read or executed**. No claim is made that either instrument is valid, that experts can be removed, that consensus criteria are gold, that selective memory causally improves general capability, or that either system has professional validity, production reliability, transport, or readiness.

Added two low-priority deep-review tasks, subordinate to `consolidate-skill-measurement-and-active-oversight` and the consented expert prerequisite:

1. `review-finresearchbench2-consensus-rubric-validity` (priority 3): immutable-v2 full-paper and release audit, centered on criterion provenance, conditional agreement, outcome-conditioned filtering, dependence, sensitivity, and claim ceilings.
2. `review-shared-selective-persistent-memory-validity` (priority 2): immutable-v1 full-paper and release audit, centered on configured-treatment parity, memory authority/adoption, stale state, sharing, refresh correctness, user evidence, and claim ceilings.

Both are method studies rather than domain commitments. Useful completion is source-grounded evidence that changes reusable rubric or memory instrumentation guidance—or an explicit finding that the empirical basis is too weak. Existing contracts should be reused unless a full review proves an exercised nonduplicate gap.
