# Scouting note — harness isolation and comparability gap

**Timestamp:** 2026-07-10T06:57:45Z  
**Scope:** Narrow primary-source search prompted by the active LH pilot's invalid runs: Hermes file tools escaped both task workspaces. The queue was healthy (eight pending tasks), so this run avoided broad discovery and added one lower-priority review only.

## Substantive finding (triage only)

**Harness-Bench: Measuring Harness Effects across Models in Realistic Agent Workflows** — Yao et al., arXiv:2605.27922v1.

- Immutable record: https://arxiv.org/abs/2605.27922v1
- Immutable PDF: https://arxiv.org/pdf/2605.27922v1
- Official release: https://github.com/reacher-z/HarnessBench; remote HEAD `d7ff1255d623177b10b59f858a95f48b7bd070e5`, also tagged `v0.1.6` during this run.
- Project site: https://www.harness-bench.ai/
- The arXiv API reports 106 sandboxed offline tasks and 5,194 trajectories comparing model–harness configurations under shared task environments, budgets, and evaluation protocols. It says runs retain artifacts, traces, usage, and validator outputs and identifies execution-alignment failures involving tool feedback, workspace state, evidence, and output contracts.
- The immutable arXiv pages, project site, and release URL returned successfully. This was **metadata/abstract and URL triage only**; neither the paper nor repository was read in full, and all implementation and causal-comparison claims require verification.

## Why this is distinct

The repository already records configured-system components and has reviewed SkillsBench's paired skill intervention. It does not yet have a deep primary-source/release inspection focused on whether native agent harnesses can be compared while enforcing task-scoped filesystem/network boundaries and preserving auditable execution. That is the exact failure exposed by `build-lh-pilot-grader-ablation`, rather than another general benchmark-family search.

## Charter decision filter and queue action

- **Objectives advanced:** A (production evaluation evidence), C (executable evaluation infrastructure), and D (targeted expansion tied to a current build gate).
- **Evidence/artifact:** eventual immutable-v1 review plus pinned-release inspection, yielding verified launcher-canary, comparability, and failure-attribution implications.
- **Uncertainty clarified:** whether shared sandbox declarations are enforced; which model–harness differences remain identifiable; which trace records support causal rather than surface failure labels.
- **Mode/balance:** narrow expansion; intentionally priority 82 behind the current CTA, Amazon, and launcher work.
- **Duplication/scope:** no existing index, review, report, or queue match for `2605.27922`/Harness-Bench; this applies across task domains and does not redefine the benchmark around coding or one profession.
- **Useful completion:** paper and release evidence are separated, environment and comparison invariants are reconstructed, and only nonduplicative implications are mapped to the current launcher/schema tasks.

Added `review-harness-bench-execution-isolation` (priority 82). No additional candidates were queued.
