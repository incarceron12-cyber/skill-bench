# Scouting note — decision fidelity under context compression

**Timestamp:** 2026-07-15T09:39:05Z  
**Scope:** Narrow expansion against charter objectives A/B. Queue inspection found 262 tasks: 254 completed, four blocked, two pending human decisions, and two pending consolidations; no source/research/review backlog remained. The completed ACON audit and executable compression slice separate endpoint success, efficiency, and state fidelity, but the corpus does not directly test whether a plausible compressed evidence view changes the downstream judgment induced by the source.

## Substantive finding — triage only

**When Summaries Distort Decisions: Information Fidelity in LLM-Compressed Financial Analysis** — Hoyoung Lee, Suhwan Park, Seunghan Lee, Jun Seo, Jaehoon Lee, Sungdong Yoo, Minjae Kim, CheolWon Na, Zhangyang Wang, Zach Golkhou, Minkyu Kim, Sotirios Sabanis, Alejandro Lopez-Lira, Dhagash Mehta, Soonyoung Lee, Chanyeol Choi, Wonbin Ahn, and Yongjae Lee; arXiv:2606.29251v2.

- Immutable record: https://arxiv.org/abs/2606.29251v2
- Immutable PDF: https://arxiv.org/pdf/2606.29251v2
- The arXiv API identifies immutable v2, submitted 28 June 2026 and revised 8 July 2026 in `cs.AI` and `q-fin.CP`; its summary contains no withdrawal notice. The versioned abstract and PDF endpoints returned HTTP 200 during scouting.
- The abstract frames information fidelity as whether compression changes the decision induced by the source. It reports experiments over financial filings and earnings-call transcripts, fluent and factually plausible compressed contexts that nevertheless alter downstream decisions, decontextualization of evidence from caveats, compressor-model dependence, and a multiple-candidate source-audit procedure called Agentic Context Compression. These are author-reported abstract claims, not independently verified findings.
- Structural inspection of immutable v2 HTML—not a full reading—confirmed sections on formalization, naive/contextualized/agentic compression, datasets, decision model, baselines, fidelity loss, model dependency, decontextualization, an industry case study, limitations, budget sensitivity, inter-model agreement, decision movement, and prompts.
- The canonical HTML exposed no paper-specific author-owned code, data, or project URL. Exact-title, ID, GitHub, and Hugging Face searches found the arXiv record and third-party mirrors but no verifiable official release. A reviewer must renew that search and record release absence explicitly if it remains unverified.
- Repository-wide exact-title, ID, and signature-phrase searches found no duplicate. ACON and the existing compression conformance slice are the closest local evidence, but they target state fidelity and next-action sufficiency rather than a source-to-compression-to-decision preservation experiment.
- This is **metadata, abstract, endpoint, section-structure, release-location, and duplicate triage only**. The paper body, methods, tables, appendices, source records, prompts, model outputs, statistical analyses, industry case, and artifacts were not read or audited. No claim is made that the reported decision flips are valid, incorrect, economically consequential, representative, causal, transferable beyond the studied setting, or evidence of investment quality, professional validity, production fitness, or readiness.

## Why this is distinct

State fidelity and decision fidelity overlap but are not interchangeable. A summary can omit source details yet preserve one declared choice, preserve every extracted fact yet detach a qualifier and reverse that choice, or preserve a decision that was wrong under the source. The reusable measurement chain is `authoritative source and task-time evidence view → compressor treatment and budget → compressed propositions with source locators and qualifier/dependency relations → downstream decision policy/model → decision preservation and direction of movement → independently warranted decision correctness → stakeholder consequence and loss`.

For `skill-bench`, finance is a bounded stress case rather than a scope commitment. The same distinction applies when agents compress research packets, handoff notes, evolving workspaces, incident evidence, or expert procedures before producing consequential artifacts. A full audit could determine whether current compression machinery should add no new primitives, or instead make decision-specific probes, caveat/dependency preservation, compressor–consumer coupling, and disagreement-triggered source reinspection more explicit.

## Charter decision filter and queue action

- **Objectives advanced:** A (context/workspace and evaluation frontier) and B (valid evidence-to-judgment transfer).
- **Concrete evidence/artifact:** immutable-v2 full-paper review reconstructing sampling, source authority, treatments, budgets, model roles, factuality/fidelity estimands, decision movement, uncertainty, prompts, case-study evidence, and release status.
- **Uncertainty clarified:** when compression preserves a declared decision, whether that differs from source/state fidelity and decision correctness, and how compressor/consumer coupling limits transport.
- **Mode:** narrow expansion feeding later consolidation/validation; no finance-domain narrowing.
- **Duplication/scope:** no local duplicate; ACON and the existing conformance slice are required comparators.
- **Useful completion:** separate source/state fidelity, task sufficiency, decision preservation, decision correctness, professional consequence, and readiness; propose no new subsystem unless a non-overlapping primitive is evidenced.

Added one task: `review-compression-decision-fidelity` (priority 12). No additional source was queued because two canonical consolidations and two human prerequisites remain higher priority.

## Operational note

The required initial `git pull --ff-only` succeeded. Local `main` was 118 commits ahead of `origin/main` before this scouting change. Pre-existing untracked paper/release artifacts were not modified.
