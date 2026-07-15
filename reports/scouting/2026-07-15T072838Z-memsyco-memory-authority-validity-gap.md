# Scouting note — memory-as-evidence authority gap

**Timestamp:** 2026-07-15T07:28:38Z  
**Scope:** Narrow expansion against charter objectives A/B. Queue inspection found 254 tasks: 248 completed, four blocked, two pending human decisions, and no source/research/review backlog. Existing memory reviews distinguish storage, retrieval, adoption, updates, and downstream action, but none directly audits whether a retrieved user memory has legitimate decision authority when it conflicts with factual evidence, exceeds its scope, or has been superseded.

## Substantive finding — triage only

**MemSyco-Bench: Benchmarking Sycophancy in Agent Memory** — Zhishang Xiang, Zerui Chen, Yunbo Tang, Zhimin Wei, Ruqin Ning, Yujie Lin, Qinggang Zhang, and Jinsong Su, arXiv:2607.01071v2.

- Immutable record: https://arxiv.org/abs/2607.01071v2
- Immutable PDF: https://arxiv.org/pdf/2607.01071v2
- Official repository: https://github.com/XMUDeepLIT/MemSyco-Bench
- The arXiv API identifies v2 as latest, updated 2 July 2026 in `cs.IR`/`cs.AI`; its summary contains no withdrawal notice. The versioned abstract and PDF endpoints both returned HTTP 200 during scouting.
- The abstract says the benchmark covers five distinctions: rejecting memory as factual evidence, respecting applicable scope, resolving conflict between memory and objective evidence, tracking updates, and using valid memory for personalization. These are author-stated construct claims pending full-text and task-level audit.
- Search metadata for the repository data card reports 1,550 examples across five categories. Scouting did not inspect the released rows, generation pipeline, labels, prompts, graders, results, or baselines, so item count and paper–release correspondence remain review questions.
- GitHub API verification found the official public MIT-licensed repository live and unarchived. Mutable `main` resolved to `c31e2c85ee8cc3c6f643587b8a6f4b5ad5eb3bf6`, last pushed 7 July 2026; no tags or GitHub releases were present. A reviewer must pin the audited commit rather than treating `main` as immutable.
- Repository-wide duplicate search before queue insertion found no title or arXiv-ID match. The adjacent local sources—MemoryArena, LongMemEval-V2, EvoMemBench, ClawArena, SovereignPA, and the action-and-memory synthesis—cover experience dependence, updates, authority, and consequence separately, but do not isolate memory's evidential authority through these five contrasts.
- This is **metadata, abstract, endpoint, repository-presence, and duplicate triage only**. The paper and release were not read during scouting. No claim is made about dataset validity, natural prevalence, reference truth, user-preference fidelity, treatment parity, grader accuracy, model behavior, general memory capability, safety, professional validity, production fitness, or readiness.

## Why this is distinct

The reusable benchmark-design question is not merely whether memory was available or retrieved, but whether it was entitled to affect the decision. A useful chain is `memory origin and authority → valid scope/time → retrieval and observed access → conflict/supersession relation → semantic adoption or rejection → downstream artifact/action consequence`. Endpoint agreement alone cannot localize whether a failure arose in the memory bank, retrieval, temporal reconstruction, authority weighting, evidence comparison, or final decision.

For `skill-bench`, this is directly relevant to messy source packs and persistent workspaces: user preferences, prior notes, obsolete policies, and authoritative evidence should not have equal status. The benchmark could sharpen source-role, valid-time, contradiction, and adoption primitives without narrowing the project to conversational memory or accepting synthetic authored labels as real-user truth.

## Charter decision filter and queue action

- **Objectives advanced:** A (memory and realistic-agent benchmark frontier) and B (authority-sensitive expertise/evidence transfer).
- **Concrete evidence/artifact:** immutable-v2 full-text review plus pinned release audit reconstructing the task families, source and label authority, generation/filtering lineage, memory treatments, graders, baselines, results, uncertainty, and release correspondence.
- **Uncertainty clarified:** whether MemSyco-Bench observes authority-sensitive evidence use or agreement with an authored synthetic oracle, and which memory-to-decision failure stages are identifiable.
- **Mode:** narrow expansion feeding consolidation; memory is a cross-domain evidence mechanism, not a benchmark scope commitment.
- **Duplication/scope:** no local duplicate; adjacent reviews do not isolate the same memory-as-evidence-authority contrast.
- **Useful completion:** compare directly with adjacent memory/action sources, update grouped conclusions only if evidence changes them, preserve strict claim ceilings, and avoid new schema work unless a non-overlapping contract gap remains.

Added one task: `review-memsyco-memory-authority-validity` (priority 16). No second task was added; Long-Horizon-Terminal-Bench and conversational workflow-boundary testing were triaged but deferred because dense partial grading and black-box testing overlap stronger existing coverage, whereas memory authority is the narrower identified gap.

## Operational note

The required initial `git pull --ff-only` failed because the HTTPS GitHub remote lacks a noninteractive credential (`could not read Username`). Local `main` was 100 commits ahead of `origin/main` before this scouting change. Pre-existing untracked paper source trees and the AgentFootprint release ZIP were not modified.
