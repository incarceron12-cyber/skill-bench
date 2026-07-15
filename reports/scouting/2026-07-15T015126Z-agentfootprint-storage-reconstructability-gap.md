# Scouting note — persistent storage and reconstructability validity

**Timestamp:** 2026-07-15T01:51:26Z

**Scope:** Narrow expansion against charter objectives A/C. At intake the queue had 243 tasks: 235 completed, four blocked, four pending (two human decisions and two consolidations), with no source/research/review task. Existing reviews cover configured-system cost, traces, workspace state, memory, recovery, and auditability, but not persistent post-run data as a resource jointly constrained by reconstructability.

## Substantive finding (triage only)

**The Hidden Footprint: Making Storage a First-Class Metric for LLM Agent Evaluation (AgentFootprint)**

- Immutable record: https://arxiv.org/abs/2607.11149v1
- Immutable PDF: https://arxiv.org/pdf/2607.11149v1
- Official repository: https://github.com/polyuiislab/AgentFootprint
- The arXiv API identifies Chenglin Yu, Hongquan Gui, Ying Yu, Hongxia Yang, and Ming Li; primary category `cs.AI`; submitted 13 July 2026 with no later version. The metadata summary contains no withdrawal notice.
- The **v1 abstract** introduces six serialization-aware metric families for persistent data left by an agent run: total retention, channel composition, duplication, growth, compressibility, and conversation-history reconstructability. It reports that naive byte comparison can miss logical duplication hidden by storage formats; fixed replay of one trajectory across seven persisting frameworks yields a 6.7× retention spread; configurations with equal reported task accuracy differ by 15.7× in retained bytes; three full-history configurations grow superlinearly under repeated observations; 108 instance-normalized SWE-bench Verified exports span three orders of magnitude with no detectable resolve-rate correlation; and content-addressed storage reduces retention 4.8×–32.7× while preserving the paper's reconstructability scores. These are author-reported abstract claims, not independently verified findings.
- Search-indexed official repository documentation exposes a useful audit surface: a framework adapter contract, audited path/channel attribution, separation of agent workspace artifacts from framework home-directory residue, content-defined-chunk fingerprints, fixed-trace controls, and documented-default configurations rather than storage-tuned ones. GitHub API metadata reports an MIT-licensed, non-fork repository whose `main` head is `fb32377518353898a3600ba871639854dc6a4389` (11 July 2026). This is current metadata and documentation triage, not a version-matched release audit.
- The distinctive benchmark question is not simply whether fewer bytes are better. Retention can pay for recovery, replay, debugging, accountability, or context continuity. A valid comparison therefore needs both resource attribution and information/operation preservation: byte-level reconstructability may not establish executable replay, causal diagnosis, policy-compliant retention, or useful recovery.
- This is metadata, abstract, URL, search-indexed official-documentation, repository-metadata, and duplicate triage only. The paper body, appendices, code, adapters, tasks, traces, metric implementations, reconstructability oracle, SWE-bench exports, experiments, raw results, and statistics were not read or audited. No claim is made that framework attribution is fair, defaults are comparable, the metrics preserve operational utility, the release reproduces v1, or any framework is efficient, capable, auditable, or production-ready.

## Benchmark implication to test

Persistent-data evaluation needs a typed chain: `configured system and documented storage policy → task/trajectory and run-root identity → workspace artifact versus framework-residue attribution → physical serialization → logical content/channels and duplication → retention/growth/compressibility observation → reconstruction target and evidence view → successful byte/history reconstruction → executable replay, recovery, diagnosis, or audit use → retention/privacy/cost consequence → bounded claim`. Logical volume, persistence amplification, retained bytes, reconstructability, operational utility, and task outcome must remain separate.

A full audit should recompute at least one path end to end and determine whether run roots and channel rules are complete; whether fixed-trace replay actually holds logical content constant; whether documented defaults differ in enabled recovery/audit features; whether content-defined deduplication and compression compare equivalent information; what reconstructability means and omits; how workspace products are separated from framework residue; whether repeated-observation growth reflects task demand, prompt/history policy, database paging, or adapter behavior; and how task/instance clustering, invalid runs, accuracy matching, uncertainty, and release drift affect comparisons. Existing configured-system, trace, workspace, memory, task-health, metric-monitoring, reliability, privacy, and cost machinery should be reused.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier production-agent evaluation) and C (resource, trace, workspace, and reproducibility instrumentation).
- **Evidence/artifact sought:** immutable-v1 deep review, pinned release audit, and one recomputed attribution→deduplication→reconstructability path.
- **Uncertainty clarified:** whether storage metrics compare equivalent retained information and whether reconstruction supports meaningful recovery/audit rather than only serialized-history recovery.
- **Mode/balance:** one low-priority review restores a minimal research backlog behind two pending consolidations and human/operational blockers; no broad search bundle was added.
- **Duplication/scope:** repository search found no `2607.11149` review/task; a prior scouting note explicitly deferred AgentFootprint. The metric is reusable operating machinery across domains, not a software-engineering scope commitment.
- **Useful completion:** preserve system/default/task/trajectory/root/adapter identities, attribution boundaries, reconstruction target, invalids, uncertainty, release drift, and claim ceilings; map implications to existing contracts without creating a storage-specific subsystem unless executable evidence exposes a real gap.

Added one task: `review-agentfootprint-storage-reconstructability-validity` (priority 11).

## Operational note

The required initial `git pull --ff-only` failed because the HTTPS GitHub remote lacks a noninteractive credential (`could not read Username`). Local `main` was 72 commits ahead of recorded `origin/main`; the run proceeded from local state. The pre-existing untracked `data/papers/source/` tree was not modified.
