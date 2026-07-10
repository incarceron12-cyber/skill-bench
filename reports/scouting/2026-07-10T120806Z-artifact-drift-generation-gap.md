# Scouting note — cross-artifact drift in benchmark generation

**Timestamp:** 2026-07-10T12:08:06Z  
**Scope:** Narrow search against charter objectives B/C and research-agenda questions 2, 3, and 4 after the queue fell to one pending consolidation task and no pending review. This run searched specifically for primary evidence on keeping task instructions, environment state, ground truth, and verifiers mutually consistent rather than repeating broad agent-benchmark discovery.

## Substantive finding (triage only)

**Anchor: Mitigating Artifact Drift in Agent Benchmark Generation** — Ivanov and Rana, arXiv:2605.26321v1.

- Immutable record: https://arxiv.org/abs/2605.26321v1
- Immutable PDF: https://arxiv.org/pdf/2605.26321v1
- Official release: https://github.com/agentic-labs/erp-bench; reachable `main`/HEAD `ceba3880af555129b5278e056a0c20f2fb5a0ba9`.
- Project/data entry point: https://erpbench.ai
- The arXiv API identifies v1, published 2026-05-25 in `cs.AI`. The abstract names **artifact drift** as disagreement among independently created instructions, environments, oracles, and verifiers. Anchor instead formalizes a domain expert's business-workflow specification as a constraint program and claims to jointly generate natural-language instructions, environment configuration, a solver-certified solution, and a state-based verifier.
- The reported application is ERP-Bench: 300 procurement/manufacturing tasks in Odoo 19. The abstract reports that generation parameters predict realized difficulty and that frontier models satisfy explicit constraints in 26.1% of trials but achieve the claimed optimum in 17.4%. These are claims to audit, not established findings for skill-bench.
- The immutable arXiv record/PDF and official Git repository were reachable. This is **metadata/abstract, canonical-URL, and Git-ref triage only**. Neither the full paper nor release was read during scouting; specification fidelity, solver assumptions, verifier soundness/completeness, alternative valid solutions, environment coupling, difficulty claims, and reward-hacking surfaces require full review.

## Why this is distinct

The repository now has strong contracts for provenance, artifacts/checks, task health, validity, metric monitoring, and artifact-view admissibility. It does not yet have primary evidence on a compiler-like benchmark-authoring architecture where one expert-authored specification is intended to generate all mutually dependent task artifacts. This source can test a particularly important hidden requirement: local validity of each artifact does not establish global consistency of the benchmark instrument.

ERP is only the released methodological case. The reusable question is whether a single authoritative specification and executable constraints can reduce drift across any domain while preserving natural-language fairness, legitimate alternative paths, expert meaning, and professionally relevant—not merely solver-convenient—difficulty.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier benchmark evidence), B (expertise-to-evaluation methodology), and C (authoring, verifier, validity, and task-health infrastructure).
- **Evidence/artifact sought:** a full immutable-v1 paper and pinned-release review, including end-to-end traces of one procurement and one manufacturing task from specification through verifier.
- **Uncertainty clarified:** whether single-source generation ensures satisfiability, executability, fair disclosure, oracle optimality, verifier soundness/completeness, controlled difficulty, and resistance to reward hacking—and which invariants transfer to skill-bench.
- **Mode/balance:** narrow expansion into an uncovered construction failure; priority 71 leaves the existing canonical consolidation ahead of it.
- **Duplication/scope:** no `2605.26321`, Anchor artifact-drift, or equivalent single-specification compilation task existed in the paper index, reviews, reports, or queue. This does not narrow the project to ERP.
- **Useful completion:** paper claims and release behavior are separated; at least two task lineages are audited; residual drift and claim limits are documented; and only nonduplicate changes are mapped into existing contracts.

Added `review-anchor-artifact-drift-generation` (priority 71). No second task was added.
