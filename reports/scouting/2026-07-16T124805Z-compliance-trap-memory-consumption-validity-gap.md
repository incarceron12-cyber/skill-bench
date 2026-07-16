# Scouting note — conflicting-memory trajectory-consumption validity gap

**Timestamp:** 2026-07-16T12:48:05Z

**Scope:** Narrow expansion under charter objectives A/B/C. Queue intake found 323 tasks, with 318 completed, two pending, three blocked, and no claimed work; one substantive signed-criterion build and one human prerequisite are already pending. Existing memory coverage is strong, so this run searched only for a missing post-retrieval trajectory diagnosis rather than repeating broad memory or benchmark discovery. Findings are **metadata, abstract, endpoint, and structural-HTML triage only**, not a full-paper review.

## Substantive finding — triage only

**The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory** — Yixiong Chen, Xinyi Bai, and Alan Yuille; arXiv:2607.10608v1.

- Immutable record: https://arxiv.org/abs/2607.10608v1
- Immutable PDF: https://arxiv.org/pdf/2607.10608v1
- Immutable HTML: https://arxiv.org/html/2607.10608v1
- The arXiv API identifies v1 as submitted and last updated 12 July 2026 in `cs.AI`; its metadata summary contains no withdrawal notice. The record, PDF, and HTML endpoints returned HTTP 200.
- The abstract introduces an Entry–Propagation–Recovery (E-P-R) trajectory framework and reports tests on WebArena plus a controlled MemTrapBench. It claims that task-wrong memory often changes the first exposed decision, repeated exposure propagates the error, and recovery after divergence is weak; it further reports similar compliance rates but larger absolute damage for stronger baseline agents. These are author-reported abstract claims requiring full-paper verification.
- Structural HTML inspection—not body reading—confirmed methods for E-P-R, compliance subsets, paired statistics, WebArena and MemTrapBench; results split entry, propagation, conditional damage, and outcome-selection concerns; appendices for task pools, memory authoring/audit, four-gate decomposition, recovery judging, per-trace annotation, a 2×2 decoy factorial, delivery-channel probes, cross-family and short-horizon controls, and retry-on-fail ablations.
- The immutable HTML outbound-link inventory exposed no author-owned code, data, task, trajectory, annotation, or result repository. Targeted title and `MemTrapBench` searches located only the paper surfaces, not a verified release.
- Exact title/ID searches found no local review, queue task, or scouting note. The closest completed review, MemSyco-Bench, explicitly identifies post-retrieval arbitration but evaluates open-ended endpoints and does not observe trajectory entry, continued adoption, recovery, or realized action. Plans Don't Persist studies forced-prefix context perturbations but discards the counterfactual action. This candidate appears to test the missing trajectory rung, although a full review must reject it as duplicative if E-P-R reduces to co-derived action labels without valid interventions or consequences.

## Why this is distinct

The reusable validity chain is:

`versioned memory/source and authority → decision-time retrieval/presentation → first action-opportunity exposure → semantic adoption or justified rejection → propagated action/state divergence → correction opportunity and information budget → recovery attempt → restored or residual artifact/state consequence → observer validity and at-risk denominators → bounded memory-control or safety claim`.

A memory-aligned action is not automatically caused by memory; persistence after an early wrong turn may reflect environment irreversibility rather than continued compliance; and task-level recovery can occur without repairing the trajectory-level policy. Conversely, conditioning only on completed failures or memory-compliant traces can create outcome-selection bias. The review should test the exact E-P-R event definitions, exposure/opportunity denominators, pair/factorial equivalence, action and state observers, recovery judge reliability, WebArena/MemTrapBench construction independence, invalid/missing runs, cluster-aware uncertainty, and whether any release permits replay.

## Charter decision filter and queue action

- **Objectives advanced:** A (frontier context/memory and realistic-agent evaluation), B (authority-preserving evidence consumption rather than retrieval alone), and C (trajectory, intervention, recovery, and state-consequence instrumentation).
- **Concrete evidence/artifact:** an immutable-v1 deep review and pinned release audit if an official artifact is located.
- **Uncertainty clarified:** whether E-P-R identifies memory entry, propagation, and recovery as distinct mechanisms or only partitions co-authored trajectory outcomes under a bundled treatment.
- **Mode:** narrow expansion feeding reusable consolidation/validation; browser tasks are a controlled method test, not a scope commitment.
- **Duplication check:** MemSyco covers authority/arbitration at the answer endpoint; existing trace and recovery reviews cover adjacent links but not matched conflicting-memory consumption across a consequential trajectory.
- **Useful completion:** retain/repair/test guidance for exposure opportunities, first divergence, continued adoption, recovery, residual consequence, and conditional-damage denominators—or an evidence-backed conclusion that the source adds no valid evidence beyond MemSyco and existing trace machinery.

Added one lowest-priority task: `review-compliance-trap-memory-consumption-validity` (priority 1), subordinate to the current build and human prerequisite. No second task was added. No claim is made that the full paper was read, that MemTrapBench or results are released, that memory caused the reported actions, that E-P-R identifies causal mechanisms, or that the method supports general memory capability, safety, professional validity, production fitness, or readiness.
