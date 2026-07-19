# Scouting note — payment-integration Skill/validity gap

- **Timestamp:** 2026-07-19T01:08:15Z
- **Evidence status:** arXiv abstract metadata, immutable endpoint checks, arXiv-HTML outbound-link discovery, official GitHub API metadata/commit history, web release search, prior-scout review, and exact local duplicate searches only. The PDF/source body, repository files, projects, task instances, Skill, rubrics, checks, prompts, traces, result rows, or experiments were **not** deeply read, downloaded into the repository, executed, reproduced, or audited during scouting.

## Substantive candidate — triage only

**Alipay-PIBench: A Realistic Payment Integration Benchmark for Coding Agents** — Shiyu Ying, Xuejie Cao, Yingfan Ma, Yuanhao Dong, Wenyu Chen, Bowen Song, and Lin Zhu; arXiv:2607.14573v1 (submitted 2026-07-16).

- Immutable record/PDF/HTML/source: https://arxiv.org/abs/2607.14573v1 · https://arxiv.org/pdf/2607.14573v1 · https://arxiv.org/html/2607.14573v1 · https://export.arxiv.org/e-print/2607.14573v1
- At scouting time these endpoints returned HTTP 200 with observed response sizes of 42,101, 1,045,424, 301,812, and 711,913 bytes respectively; the source endpoint resolved to `/src/2607.14573v1`.
- The abstract describes nine product-specific repository projects and 18 task instances paired into Basic functional-completion and Advanced risk-aware-hardening scenarios. It reports deterministic static, unit, integration, and end-to-end checks plus LLM-assisted semantic assessment; six coding-agent models; rubric pass rate; and a with/without `alipay-payment-integration` Skill contrast averaging +10.31 percentage points, with model/product/scenario heterogeneity. These are author-stated abstract claims awaiting full-paper and release verification.
- The immutable arXiv HTML links the official release https://github.com/inclusionAI/PIBench. GitHub API inspection found an MIT-licensed repository created 2026-07-06 with two observed commits: init commit `e2782ad0d2b0559170401680e6d06be1ee1eac17` (2026-07-16T10:30:06Z) and current `main` head `17c8c42e77f27a64548b07d1693979ac51c66fb2` (2026-07-17T03:13:18Z), whose message says it adds arXiv paper links. Repository content and release completeness were not inspected during scouting.
- Exact arXiv-ID, title, repository-name, payment-integration, payment-state, and transaction-state queue searches found no local review or task. A 2026-07-17 scout had explicitly triaged and deferred Alipay-PIBench because a revision-derived expertise/artifact candidate was then more direct; the now-verified official paper-linked release creates a distinct, timing-aware audit path. Existing coding/tool evolution, SkillsBench/SkillGenBench, executable artifact/science, harness, action-authority, safety, and configured-system work supplies comparators rather than this joint payment-state/Skill/rubric case.

## Why this is a narrow, useful gap

The reusable chain is:

`authorized/versioned product and integration requirements → repository/task projection → Basic/Advanced obligation pair → configured agent/harness/service state → procedural-Skill treatment and actual adoption → client/server code and calls → payment outcome evidence → transaction/business-state consistency → risk/safety hardening → deterministic and semantic observers → aggregation → transport/professional consequence`.

This directly advances charter objectives A–C and E. Payment integration is a consequential software workflow where apparent source completion can diverge from executable behavior, asynchronous outcome handling, business-state consistency, and risk controls. The paper/release may expose how layered executable checks and semantic rubrics observe those differences, while the paired Skill condition is a useful test of intervention/instrument separation.

The claim ceiling is equally important. Repository-specific rubric gain does not by itself establish that the Skill is source-faithful expert guidance, that it was behaviorally adopted, that the comparison has equal runtime/context/tool envelopes, that checks cover legitimate alternative implementations or adverse states, that an LLM judge is valid, or that a passing integration is safe, production-fit, professionally acceptable, or readiness evidence.

## Charter decision filter and queue action

- **Objectives advanced:** A (realistic benchmark and production-system evidence), B (requirements-to-state-to-consequence lineage), C (layered executable and semantic observers plus Skill ablation), and E (clear claim ceilings).
- **Concrete evidence:** immutable-v1 full-paper review and timing-aware audit of the official release, with task/rubric/treatment/result reconstruction and retain/repair/test implications.
- **Uncertainty clarified:** whether the reported Skill contrast isolates transferable procedural value or a benchmark-specific bundle, and which payment-correctness/risk/professional claims the released checks can support.
- **Mode:** narrow expansion/human learning. The queue had two pending consolidations and one human decision but no pending review; one low-priority review restores a small research buffer without repeating a broad search.
- **Duplication/scope check:** exact queue searches were negative; the prior scout's deferral is acknowledged rather than overwritten. Payment is a bounded high-consequence mechanism case, not a permanent domain commitment.
- **Useful completion:** source/page/path-grounded reconstruction of project/task provenance, paired obligations, Skill authority and treatment parity, harness/service state, check topology, judge validity, denominators, release correspondence, and claim ceilings; reuse existing contracts and add no payment-specific schema or pilot.

Added one task: `review-alipay-pibench-payment-integration-validity` (review, priority 40). No second task was queued.
