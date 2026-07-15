# Scouting note — automated failure-attribution validity gap

**Timestamp:** 2026-07-15T07:58:12Z  
**Scope:** Narrow expansion against charter objectives A/B/C. Queue inspection initially found 256 tasks: 249 completed, four blocked, two pending human decisions, and one pending consolidation; no source/research/review backlog remained. Existing work covers dependency-aware causal slicing, root/surface labels, multichannel trajectory evidence, task health, and invalid trials, but not the validity of an automated failure auditor evaluated against controlled injected-fault labels.

## Substantive finding — triage only

**Who&When Pro: Can LLMs Really Attribute Failures in AI Agents?** — Jiale Liu, Huajun Xi, Shaokun Zhang, Yifan Zeng, Tianwei Yue, Chi Wang, Jian Kang, Qingyun Wu, Huazheng Wang; arXiv:2607.09996v1.

- Immutable record: https://arxiv.org/abs/2607.09996v1
- Immutable PDF: https://arxiv.org/pdf/2607.09996v1
- Paper-linked project: https://whowhenpro.github.io
- Paper-linked official repository: https://github.com/whowhenpro/whowhen_pro
- The arXiv API identifies immutable v1, submitted 10 July 2026 in `cs.AI`/`cs.MA`; its summary contains no withdrawal notice. The versioned abstract and PDF endpoints returned HTTP 200 during scouting.
- The abstract says a controlled pipeline exactly replays a successful prefix and then injects one failure, yielding 12,326 labeled failed trajectories over three modalities and 26 source benchmarks. These are author-stated construct and scale claims pending full-text and release audit.
- The arXiv HTML exposes the project URL and describes an 18-mode taxonomy, but scouting did not inspect the paper's methods, tables, appendices, prompts, labels, or results. The critical unresolved distinction is among injected deviation, first observable divergence, propagated surface failure, earliest sufficient cause, and natural multi-cause failure.
- GitHub API verification found the paper-linked repository public, live, unarchived, and without a declared license, tags, or releases. Mutable `main` resolved to `db3946cae6895c8056b9b482c283fc3949a6654f`, last committed 12 July 2026. A reviewer must pin the audited commit and establish paper–release timing and correspondence rather than treating `main` as immutable.
- Repository-wide exact title/ID search found no duplicate. STRACE supplies causal-slice methodology; Claw-Eval separates trajectory observer views; existing root/surface and task-health machinery records diagnostic outcomes. None locally audits whether an injected-fault benchmark's “golden” who/when/what labels establish causal-root truth or only recovery of its construction intervention.
- This is **metadata, abstract, endpoint, official-link, repository-metadata, and duplicate triage only**. The paper and release were not read or executed during scouting. No claim is made about fault realism, taxonomy authority or completeness, source-benchmark representativeness, label correctness, evaluator reliability, natural failure prevalence, causal identification, cross-modality transport, professional validity, production utility, or readiness.

## Why this is distinct

A controlled intervention can give unusually strong knowledge of what the generator changed, but that does not automatically identify the earliest sufficient cause of the final failure. The original successful prefix may cease to be valid after an injected state change; the injected action may be recoverable; later propagation may depend on environment or evaluator behavior; and natural agent failures can contain interacting causes rather than one isolated mutation.

The reusable diagnostic chain for `skill-bench` is `configured system and valid environment → successful-prefix evidence → intervention eligibility and exact injected delta → first state/trace divergence → dependency propagation → surfaced check/artifact failure → alternative sufficient causes and recovery → observer view → auditor judgment → bounded attribution claim`. Auditing this chain could sharpen current root/surface and causal-slice guidance for artifact-heavy knowledge work without narrowing the benchmark to multi-agent systems or adopting the source benchmarks as the target domain.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier agent-evaluation evidence), B (diagnostically valid expertise-to-evaluation reasoning), and C (trace/root-cause evaluation infrastructure).
- **Concrete evidence/artifact:** immutable-v1 full-paper review plus commit-pinned official release audit, including paper–release correspondence and row/code inspection.
- **Uncertainty clarified:** when exact-prefix replay plus one injected deviation licenses an intervention-recovery claim, and what extra evidence is needed for causal-root or natural-failure attribution.
- **Mode:** narrow expansion feeding consolidation/validation; no benchmark-domain or multi-agent scope commitment.
- **Duplication/scope:** no local duplicate; STRACE, Claw-Eval, root/surface records, and task-health contracts are required comparators rather than replacements.
- **Useful completion:** reconstruct sampling, injection, labels, observer views, protocols, metrics, uncertainty, ablations, release fidelity, and strict claim ceilings; propose no schema work unless a non-overlapping gap remains.

Added one task: `review-whowhen-pro-failure-attribution-validity` (priority 15). No second task was added; the existing consolidation remains the higher-priority non-human work.

## Operational note

The required initial `git pull --ff-only` failed because the HTTPS GitHub remote lacks a noninteractive credential (`could not read Username`). Pre-existing untracked paper source trees and the AgentFootprint release ZIP were not modified.
