# Scouting note — layer-isolated deterministic-scaffold validity gap

- **Timestamp:** 2026-07-17T21:35:18Z
- **Evidence status:** arXiv API metadata/abstract, targeted web/GitHub discovery, and exact repository duplicate searches only. The paper body, appendices, claimed production system, harness, cases, mutations, baselines, tenant fixtures, or result records were **not** deeply read, downloaded, or executed during scouting.

## Substantive candidate — triage only

**Layer-Isolated Evaluation: Gating the Deterministic Scaffold of a Production LLM Agent with a No-LLM, Regression-Locked Test Harness** — Sawyer Zhang, Alexander Wang, and Sophie Lei; arXiv:2606.11686v1.

- Immutable record/PDF/HTML: https://arxiv.org/abs/2606.11686v1 · https://arxiv.org/pdf/2606.11686v1 · https://arxiv.org/html/2606.11686v1
- The arXiv API identifies a `cs.CL`/`cs.AI` v1 submitted and last updated 10 June 2026. Its summary contains no withdrawal or retraction notice.
- The abstract describes one deployed ordering agent split into ontology, intent, routing, decomposition, escalation, safety, memory, and cross-cutting envelope/defense layers, each tested in deterministic no-LLM “pure” mode. It reports 238 cases across 23 slices, but says 225 run; seven non-safety regression injections; aggregate losses of only 1.7–5.9 percentage points for six local regressions while matching slices lose 25–91 points; matching-slice worst rank in 5/7 and top-three rank in 7/7; and replication on a second tenant. These are author-stated abstract claims awaiting full-paper and artifact verification.
- Targeted search found arXiv HTML/PDF but no identifiable author-owned code or data repository. Search snippets expose a claimed path, `eval/experiments/p2_regression_injection.py`, which makes release discovery and paper/release conformance a concrete review action rather than evidence that the code is public.
- Exact title, ID, and mechanism searches found no local review or queue duplicate. Adjacent work covers dependency edges, causal diagnosis, injected faults, harness isolation, task health, repeated reliability, and production monitoring, but not this baseline-locked no-LLM layer-slice design.

## Why this is a narrow, useful gap

The relevant chain is:

`production requirement/incident → architectural layer boundary → pure-mode fidelity → layer-specific assertion slice and coverage → locked baseline → controlled mutation → observed slice and aggregate deltas → localization rule → cross-tenant transport → live stochastic behavior → production consequence`.

Per-layer gates may expose aggregate masking and accelerate regression triage. They can also encode the expected localization by construction: a mutation targeted at a named layer and assertions authored for that layer do not independently validate the layer taxonomy, causal root, completeness, or live-agent consequence. The unexplained 238-versus-225 case accounting, excluded safety mutation, slice dependence, baseline maintenance, tenant selection, and pure/live boundary therefore matter to any claim beyond deterministic scaffold conformance.

The ordering-agent setting is a bounded mechanism case for reusable component-evaluation and diagnostic-validity machinery, not a proposal to narrow `skill-bench` to commerce or CI testing.

## Charter decision filter and queue action

- **Objectives advanced:** A (production evaluation frontier), B (component and diagnostic claim validity), and C (layer/assertion, mutation, metric, task-health, and configured-system records).
- **Concrete evidence:** immutable-v1 full-paper review plus timing-aware audit of any author-owned harness, fixtures, mutations, baselines, and raw results.
- **Uncertainty clarified:** when a deterministic slice supports conformance, masking, localization, adequacy, or transport—and which stochastic reliability, causal, production-outcome, professional-validity, or readiness claims remain unsupported.
- **Mode:** narrow expansion. Two recent source integrations await consolidation, so only one lower-priority review was added rather than restarting broad search.
- **Duplication/scope check:** adjacent mechanisms exist, but no exact duplicate was found; the review must compare them and add no commerce- or CI-specific schema.
- **Useful completion:** page/path-grounded reconstruction of suite authority, case accounting, pure-mode fidelity, baselines, mutation design, slice dependence, coverage honesty, denominators, two-tenant evidence, release conformance, costs, and bounded retain/repair/test implications.

Added one task: `review-layer-isolated-deterministic-scaffold-validity` (review, priority 57). No other task was queued.
