# Scouting note — cross-domain prompt-injection and action-safety gap

**Timestamp:** 2026-07-10T15:26:53Z  
**Scope:** Narrow search against charter objectives A/B/C and the explicit safety/prompt-injection question in `docs/state-of-the-art-map.md`. The queue already had two implementation/consolidation tasks and two evidence-gated blocked tasks, so this run did not repeat broad benchmark discovery.

## Substantive finding (triage only)

**ClawSafety: “Safe” LLMs, Unsafe Agents** — Bowen Wei et al.

- Immutable arXiv record: https://arxiv.org/abs/2604.01438v2
- Immutable arXiv PDF: https://arxiv.org/pdf/2604.01438v2
- Official project page: https://weibowen555.github.io/ClawSafety/
- Official repository: https://github.com/weibowen555/ClawSafety (HEAD verified as `5baf6fb40ab41bce40debf502f08e05320280d20`)
- The arXiv API identifies v2, published 2026-04-01 and updated 2026-04-04 in `cs.AI`. Its abstract reports 120 adversarial scenarios spanning software engineering, finance, healthcare, law, and DevOps; skill-file, trusted-email, and web injection channels; 2,520 sandboxed trials; action-trace analysis; and comparisons across five model backbones and three agent frameworks.
- The immutable abstract/PDF, official project page, and repository returned HTTP 200, and repository HEAD was verified. This is **metadata/abstract, canonical-URL, and release-location triage only**. Neither the full paper nor release was read during scouting; all scenario-realism, attack-rate, action-trace, domain-grounding, sandbox, and model/framework claims require full review.

## Why this is distinct

The local evidence base now covers workspace dependencies, evolving information, execution isolation, rubric reliability, and configured-system effects, but it has no indexed or queued primary-source review of adversarial instructions embedded in ordinary professional evidence channels. The state-of-the-art map explicitly leaves prompt injection and safety unresolved.

ClawSafety is especially relevant because the injected material appears where knowledge-work agents normally obtain legitimate context: procedural skill files, messages from apparently trusted senders, and web sources. A review can test whether the benchmark separates source authority from content, useful completion from safe refusal, attempted from realized harm, and backbone effects from framework/tool-policy effects. It can also test whether legal, clinical, financial, confidentiality, integrity, and destructive-action consequences are actually domain-grounded and observable.

The reusable question is not whether skill-bench should become an OpenClaw or personal-agent benchmark. It is how adversarial evidence, authority boundaries, consequential side effects, safety/utility tradeoffs, and configured-system security should be represented across knowledge-work domains.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier realistic-agent safety evidence), B (trusted evidence, hidden requirements, and safety constraints), and C (source-pack, trace, artifact/state, configured-system, and validity contracts).
- **Evidence/artifact sought:** a full immutable-v2 paper review plus pinned official-release inspection with page/file evidence.
- **Uncertainty clarified:** expert/domain grounding; injection-channel comparability; public basis and authority; safe refusal versus useful completion; attempted/partial/realized harm observability; sandbox validity; repeated-trial uncertainty; and model-by-framework treatment validity.
- **Mode/balance:** narrow expansion at priority 66, below the existing build/consolidation work; one review item replenishes the research backlog without displacing implementation.
- **Duplication/scope:** no local index, review, scouting note, or queue item matched `2604.01438` or ClawSafety. Existing ClawArena and workspace work cover evolving evidence and dependencies, not adversarial authority or action safety. Personal agents are a methodological case, not a scope boundary.
- **Useful completion:** paper and release claims are separated; scenario provenance, sandbox, evidence views, metrics, uncertainty, and configured-system comparisons are audited; only nonduplicate implications map into existing contracts.

Added `review-clawsafety-cross-domain-injection-validity` (priority 66). No second task was added.
