# Scouting note — diagnosis-to-runtime-intervention validity gap

- **Scouted:** 2026-07-18T21:03:34Z
- **Evidence status:** metadata/abstract and URL triage only; no full-paper reading claim

## Substantive candidate

**AgentTether: Graph-Guided Diagnosis and Runtime Intervention for Reliable LLM Agent Operation** (arXiv:2607.06273v1, submitted 2026-07-07).

- Immutable record: https://arxiv.org/abs/2607.06273v1
- Immutable PDF: https://arxiv.org/pdf/2607.06273v1
- Paper-linked anonymous release: https://anonymous.4open.science/r/AgentTether-9416/
- The arXiv API and HTML record were reachable. The linked release URL was verified in the paper HTML but returned HTTP 403 to this scout's direct request; a reviewer should retry and preserve the blocker if access remains unavailable.

The abstract reports a wrapper that projects trajectories into Transition Units and a dependency-aware Critical Transition Graph, combines an offline normal-behavior model with a run-local detector, converts selected failure-critical subtrajectories into cross-iteration Repair Memory, and optionally maintains guidance through guarded runtime intervention. It reports 261 tau-bench tasks across three domains for Qwen3.7-max, a Banking transfer test with GPT-5.4, and repair of 49/83 and 56/86 initially failed Banking tasks respectively. These are author-reported abstract claims, not audited findings.

## Why this is distinct

The corpus separately covers trace localization (STRACE, Who&When Pro, DRIFT), suffix intervention (Causal Agent Replay), delivered guidance and repair (The Compliance Trap), procedural transfer (AFTER), and evaluator-generated repair (UniClawBench). AgentTether appears to join those stages in one diagnosis → persistent guidance → guarded re-execution loop. That makes it a useful validity test: endpoint recovery may validate a configured repair package without validating the selected causal root, the graph abstraction, reusable memory, cross-model transfer, or production reliability. Initial-failure conditioning, retries/iterations, detector training evidence, changing context/resource envelopes, task order, and release correspondence are the key audit targets.

## Charter decision filter and queue action

- **Objective:** A/B/C — frontier research, expertise/procedure-to-evaluation methodology, and diagnostic evaluation infrastructure.
- **Evidence/artifact:** full immutable-paper review plus timing-aware release audit and denominator reconstruction.
- **Uncertainty:** whether graph-localized subtrajectories and successful guided reruns support causal diagnosis or only configured outcome-conditioned repair.
- **Mode:** targeted expansion/validation; the review backlog was empty, while two consolidation tasks and one human decision were pending.
- **Duplication/scope:** exact repository search found no `AgentTether` or `2607.06273`; existing adjacent reviews are required comparators. Tau-bench is a bounded mechanism case, not a domain commitment.
- **Useful completion:** reconcile all assigned/initially failed/retried/repaired/invalid records, intervention and resource parity, independent localization evidence, memory/order leakage, cross-model/domain transport, and release identity; preserve strict claim ceilings.

Queued one task: `review-agenttether-diagnosis-intervention-validity` (priority 47). No other source was added.
