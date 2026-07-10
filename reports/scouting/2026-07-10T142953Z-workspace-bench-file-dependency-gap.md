# Scouting note — large-scale workspace/file-dependency gap

**Timestamp:** 2026-07-10T14:29:53Z  
**Scope:** Narrow search against charter objectives A/B/C and the context/workspace-engineering gap. The queue had one pending cross-record build and two evidence-gated blocked builds, so this run did not repeat broad agent-benchmark discovery.

## Substantive finding (triage only)

**Workspace-Bench 1.0: Benchmarking AI Agents on Workspace Tasks with Large-Scale File Dependencies** — Zirui Tang et al.

- Immutable arXiv record: https://arxiv.org/abs/2605.03596v4
- Immutable arXiv PDF: https://arxiv.org/pdf/2605.03596v4
- Official repository: https://github.com/OpenDataBox/Workspace-Bench (HEAD verified as `83689946b4de655df212195ead4f46458e3bc8e6`)
- Official project site: https://workspace-bench.github.io/
- Official Lite dataset: https://huggingface.co/datasets/Workspace-Bench/Workspace-Bench-Lite
- The arXiv API identifies v4, published 2026-05-05 and updated 2026-05-14 in `cs.AI`, `cs.CL`, `cs.DB`, and `cs.LG`. Its abstract reports five worker profiles, 74 file types, 20,476 files (up to 20 GB), 388 dependency-graph-linked tasks, 7,399 rubrics, four harnesses, seven models, a human comparison, and a 100-task Lite subset intended to reduce evaluation cost while preserving the benchmark distribution.
- The immutable abstract and PDF returned HTTP 200; the official repository, site, and dataset were located and the repository HEAD was verified. This is **metadata/abstract, canonical-URL, and release-location triage only**. Neither the full paper nor release was read during scouting; all construction, human-performance, agent-performance, distribution-preservation, and authenticity claims require full review.

## Why this is distinct

The repository covers evolving information (ClawArena), configured context adaptation (ACE), occupational artifacts (GDPval), and execution isolation, but has no review or map entry for workspace-scale dependency discovery and safe multi-file modification. Workspace-Bench can test whether file-dependency graphs are useful evidence/provenance machinery or answer-bearing author metadata; whether realistic file volume adds professional construct coverage rather than retrieval load alone; and whether graders observe correct, non-destructive workspace state rather than only a named deliverable.

The reusable question is not whether skill-bench should become a file-navigation benchmark. It is how implicit cross-file evidence, workspace state, artifact edits, extraneous-change checks, evaluator access, and cost-reduced suite assembly should be represented and validated across knowledge-work domains.

## Charter decision filter and queue action

- **Objectives advanced:** A (realistic knowledge-work benchmark evidence), B (dependency structure as expertise/evidence transfer), and C (source-pack, artifact-view, task-health, metric, and assembly contracts).
- **Evidence/artifact sought:** a full immutable-v4 paper review plus pinned official-repository/dataset inspection and an end-to-end task trace.
- **Uncertainty clarified:** workspace authenticity; expert role and task provenance; dependency-path leakage; retrieval versus domain judgment; safe-edit scoring; grader/human evidence-view comparability; clustering and uncertainty; and Lite-suite construct preservation.
- **Mode/balance:** narrow expansion at priority 67, below the pending build; it creates one review item rather than a broad source backlog.
- **Duplication/scope:** no local index, review, scouting note, queue item, or state-of-the-art row matched `2605.03596` or Workspace-Bench. Workspace/file tasks are a methodological case, not a scope boundary.
- **Useful completion:** paper and release claims are separated, representative task lineage is traced, claimed human and Lite comparisons are audited, and only nonduplicate requirements map to existing contracts.

Added `review-workspace-bench-file-dependency-validity` (priority 67). No second task was added.
