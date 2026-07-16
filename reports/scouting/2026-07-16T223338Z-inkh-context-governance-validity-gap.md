# Scouting note — interaction-native context-governance validity gap

- **Timestamp:** 2026-07-16T22:33:38Z
- **Evidence status:** arXiv API metadata/abstract, immutable endpoint checks, HTML heading/outbound-link inspection, targeted web/repository discovery, and local corpus/queue duplicate checks only. The PDF body, appendices, benchmark implementation, generated episodes, metrics, statistical analyses, and any code/data package were **not** deeply read or audited during scouting.

## Substantive candidate — triage only

**Absorbing Complexity: An Interaction-Native Knowledge Harness for Financial LLM Agents** — Ailiya Borjigin, Igor Stadnyk, Ben Bilski, Maksym Chikita, Dmytro Kyrylenko, Sofiia Pidturkina, and Julia Stadnyk, arXiv:2606.01886v1.

- Immutable record: https://arxiv.org/abs/2606.01886v1
- Immutable PDF: https://arxiv.org/pdf/2606.01886v1
- The arXiv API reports one version submitted 1 June 2026 in `cs.AI`/`cs.CE`; its abstract contains no withdrawal notice. The versioned abstract, PDF, and HTML endpoints returned HTTP 200.
- The abstract proposes an interaction-native knowledge harness (`InKH`) that turns user, market, portfolio, and tool events into structured operational knowledge. It describes passive pre-step context injection, a bounded working-context buffer, temporal graph memory, a wiki audit surface, background extraction, maturity/decay, and write-time invalidation.
- The abstract reports a controlled synthetic benchmark with 24 random seeds, four rounds, 80 episodes per round, six baselines, and 46,080 baseline-conditioned evaluations. It claims effects on task quality, latency, token cost, stale-knowledge use, traceability, and repeated errors, while explicitly limiting the benchmark to architecture-level behavior rather than live trading. These are author claims awaiting full-paper and implementation verification.
- Structural inspection of immutable HTML—not body reading—confirmed sections for state/knowledge objects, context buffers, lifecycle rules, governance constraints, algorithms, synthetic mechanics, data schemas, public-data extension, metrics/statistics, shock adaptation, governance ablation, limitations, and reproduction. Outbound links included FRED, SEC EDGAR, Binance, Graphiti, and unrelated references, but no clearly author-owned benchmark repository was identified. This is not proof that no release exists.

## Why this is a narrow, useful gap

The reviewed corpus already separates memory availability, retrieval, adoption, authority, persistence, update/delete operations, context compression, governance carriage, and online resource cost. No exact title/ID duplicate or review of a **passive pre-step context assembler jointly evaluated for freshness, invalidation, auditability, quality, and serving cost** was found.

The reusable validity chain is:

`versioned event/source and authority → extracted knowledge object → maturity/decay/invalidation state → bounded context selection and delivery → model adoption or justified rejection → action/artifact/state consequence → trace/audit evidence → quality, freshness, latency, and cost claim`.

A simulator-authored “stale” label need not establish real-world factual or user authority; successful context delivery need not establish causal adoption; write-time invalidation need not prevent downstream use; a readable wiki need not support effective human audit; and synthetic latency/token gains do not establish workflow adoption or financial readiness. Finance is therefore a bounded stress case for general event-to-context-to-decision machinery, not a scope commitment.

## Charter decision filter and queue action

- **Objectives advanced:** A (context/memory and production-evaluation frontier) and B (authority-preserving expertise/context transfer into evaluation).
- **Concrete evidence:** immutable-v1 full-paper review plus pinned reproduction/release audit if executable artifacts can be located.
- **Uncertainty clarified:** whether the synthetic process and metrics identify fresh, authorized context delivery, causal use, stale-use prevention, traceability, and resource effects—or only conformance to a co-authored simulator policy.
- **Mode:** narrow expansion. Before this addition the queue had one pending build and one pending human decision, with no source/research/review backlog.
- **Duplication/scope check:** nearest comparators are LongMemEval v2, MemOps, MemSyco, Compliance Trap, Governance Decay, decision-fidelity compression, and online skill/memory budget value; none combines this intervention and measurement package. No finance-specific subsystem is justified.
- **Useful completion:** reconstruct all units, denominators, baselines, observer derivations, treatment parity, uncertainty, governance ablation, public-data transport, and release evidence; bind claims to what survives comparison with existing contracts.

Added one task: `review-inkh-context-governance-validity` (priority 7). No full-paper, reproducibility, implementation-correctness, or production-readiness claim was made during scouting.
