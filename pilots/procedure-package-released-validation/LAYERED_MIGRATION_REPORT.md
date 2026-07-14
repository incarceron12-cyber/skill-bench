# Layered migration report

## Result

The pre-implementation matrix in `layered-migration-freeze.json` was exercised
without changing the v0.1 fixture, either released adapter, either prior adapter
report, either raw v0.1 replay report, or any copied release source byte.
Machine-readable outcomes are in `reports/*.layered.report.json`.

| Instrument | Package layer | Environment layer | Trial layer | Licensed result |
|---|---|---|---|---|
| Builder v0.1 calibration | `pass` | `pass` | `pass` | Exact internal fixture/replay behavior only |
| SOP-Bench Aircraft Inspection | `fail` | `insufficient_evidence` | `insufficient_evidence` | Answer-bearing/access defect recorded; no replay or trial claim |
| Anchor task 2000 | `fail` | `insufficient_evidence` | `insufficient_evidence` | Stateful inventory represented; exposed-oracle defect recorded; no replay or trial claim |

This separates two source-package access failures from absent environment and
trial observations. In particular, the Anchor terminal-state checker is now
representable as a stateful shape without inventing an Odoo runtime, terminal
snapshot, trajectory, or accepted alternative.

## Verification scope

Eleven mutation/regression tests cover access leakage, answer-bearing tools,
hash drift, missing runtime and terminal state, trace-derived endpoint
substitution, invented alternatives, unavailable-to-pass promotion, cross-layer
claim promotion, all three expected migrations, and a valid stateful inventory
with unavailable trial evidence. The unchanged v0.1 validator and old adapter
validator remain separate regression targets.

No professional correctness, expert approval, benchmark capability, safety,
production fitness, or deployment readiness is claimed.
