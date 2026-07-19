# Custody adjudication: retrospective v6 repair after v7 execution

**Decision:** **historical custody was breached; commit-bound v7 execution closure remains hash-verifiable.** Commit `0cb5bea98ca3f1cbb698a04bc4b285a7fe5d69d1` repaired six files inside the already frozen v6 pilot and refreshed their six bindings in the already independently audited and executed v7 manifest. The repair did not change a v7 task, treatment, endpoint, assignment, or execution-package byte. The original audited states remain recoverable from Git, so the 32 retained v7 endpoint observations still close at their source commits—but current `HEAD` must not be described as preserving the exact failed v6 bytes or the original audited v7 manifest.

- Machine adjudication: [`reports/validation/2026-07-19-pretask-procedure-v6-v7-custody-adjudication.json`](../../reports/validation/2026-07-19-pretask-procedure-v6-v7-custody-adjudication.json)
- Replay audit: [`scripts/audit_v6_v7_freeze_custody.py`](../../scripts/audit_v6_v7_freeze_custody.py)
- Regression tests: [`tests/test_v6_v7_freeze_custody.py`](../../tests/test_v6_v7_freeze_custody.py)
- Original independent freeze review: [`pretask-procedure-transfer-v7-independent-freeze-review.md`](pretask-procedure-transfer-v7-independent-freeze-review.md)
- Original execution-validity review: [`pretask-procedure-transfer-v7-execution-validity-review.md`](pretask-procedure-transfer-v7-execution-validity-review.md)

## Why this slice advances the charter

This is building/validation under charter objectives B and C. The concrete artifact is a replayable, append-only custody record that distinguishes an instrument's observed historical state from a later repaired working-tree state. It clarifies whether a manifest rewrite destroys the underlying trial evidence or instead narrows the preservation claims that can be made about it. The machinery is reusable wherever source packs, graders, or failed release gates are later repaired; custody and journals remain synthetic mechanism families, not benchmark scope.

No pilot or execution file was edited. No model, provider, executor, oracle, checker, canary, preflight, repair row, or retry row was run.

## Reconstruction method

The audit reads bytes directly from Git and binds five milestones:

| Role | Commit |
|---|---|
| Independently audited v7 freeze source | `0b7f9306ec6c3a18d4f5bba98af3eabd2ea7f200` |
| V7 execution source snapshot | `a6d06f988dcdd56e6e3cb46845c652b9f1ace3e3` |
| Independent execution-audit record | `b025bf2c0ae6ce00312c3740a4cca5435e829574` |
| Immediate pre-repair parent | `79bb86a1b0bacede1209695ab565234fc1a64277` |
| Retrospective repair | `0cb5bea98ca3f1cbb698a04bc4b285a7fe5d69d1` |

At both `0b7f930…` and `a6d06f9…`, it parses the historical v7 manifest and recomputes all 22 component and 33 external-binding sizes and SHA-256 values from the same commit. It then diffs the repair against its parent, requires every changed v6 pilot file to have been an audited v7 external binding, and requires the six refreshed manifest entries to equal exactly those six changes. It separately rejects any repair-time change to a non-manifest v7 file or the v7 execution package. The test also compares the committed JSON report byte-for-byte with a fresh reconstruction.

This design fails if a changed binding is omitted, if a declared historical hash does not close, if an unexpected repair path appears, or if a task/treatment/execution byte changed.

## Exact findings

### 1. The two historical v7 snapshots close

All 55 bindings match at both the independently audited freeze commit and the execution source commit: 22/22 v7 components and 33/33 external bindings, with zero mismatches. The original v7 manifest is byte-identical at those two commits. The independent freeze review was therefore correct about the exact commit it audited, and execution used the same historical binding inventory.

### 2. The repair changed six bound v6 files

The repair changed these already-bound pilot files:

1. `pilots/pretask-procedure-transfer-v6/README.md`
2. `pilots/pretask-procedure-transfer-v6/canary-report.json`
3. `pilots/pretask-procedure-transfer-v6/freeze-manifest.json`
4. `pilots/pretask-procedure-transfer-v6/preflight-report.json`
5. `pilots/pretask-procedure-transfer-v6/preflight.py`
6. `pilots/pretask-procedure-transfer-v6/run_canaries.py`

It also changed the v6 test, queue, and `pilots/pretask-procedure-transfer-v7/freeze-manifest.json`. The v7 manifest refresh replaced exactly the six old v6 size/hash pairs with the six repaired pairs. No changed v6 pilot path was absent from the original v7 external inventory.

The complete before/after byte sizes, Git blob IDs, SHA-256 values, and old/new manifest declarations are in the machine report. This is not mere metadata drift: the retained failed canary and preflight observations changed from fail records to pass records, alongside their implementations and v6 manifest.

### 3. Two v6 states must remain separate

- **Pre-repair v6 (`79bb86a…`):** the frozen failed pre-execution state that v7 originally bound. Its canary and preflight fail. This is the historical evidence needed to understand why v7 existed.
- **Post-repair v6 (`0cb5bea…`):** a post-hoc infrastructure repair whose canary and preflight pass. It may be useful as repaired implementation evidence, but it is not a prospective new instrument and cannot replace the failed state in the v7 lifecycle record.

Git history preserves both states. The current working tree does not preserve the exact failed v6 bytes. Refreshing the old v7 manifest made it internally consistent with repaired `HEAD`, but it did not make those bytes the ones independently audited or used at execution.

### 4. V7 execution closure survives—narrowly and commit-bound

The repair changed only the v7 manifest within the v7 instrument and changed nothing under `pilots/pretask-procedure-transfer-v7-execution/`. All original bindings close at the freeze and execution commits, and the original manifest is identical across them. Therefore the retained assignment, task/treatment, output, usage, and endpoint records remain hash-verifiable as a commit-bound 32-row execution.

The correct inference is not “nothing material changed.” It is:

> The original v7 freeze and execution snapshots remain auditable in immutable Git history; later `HEAD` custody no longer reproduces their parent-failure and manifest bytes.

The later rewrite does not rescore the 24/32 endpoint result, repair the two artifact-invalid outputs, identify the generated-versus-no-package mechanism contrast, or alter the zero generated-versus-raw contrast. It changes the lifecycle-preservation claim, not the stored trial outcomes.

## Claim adjudication

### Licensed

- At `0b7f930…` and `a6d06f9…`, v7 bound and verified the exact failed v6 bytes then present.
- Those bytes and the original manifest remain recoverable and hash-verifiable from Git.
- The v7 task/treatment/execution closure remains hash-verifiable at the original commits because the repair changed no task, treatment, endpoint, assignment, or execution-package byte.

### Not licensed

- Current `HEAD` preserves the exact failed v6 pilot bytes.
- Current `HEAD`'s v7 manifest is the manifest independently audited or used at execution.
- The repair retroactively converted frozen v6 failure into a pass.
- The lifecycle completed without a later rewrite of prior frozen evidence.

Historical reviews remain valid when read as commit-bound findings. Their preservation language must not be generalized to current filesystem custody after `0cb5bea`.

## Reusable design consequence

A path plus mutable manifest is not durable custody. Future freezes should bind immutable object identity—at minimum commit plus Git blob/tree ID—and treat a later repair as a new version or append-only adjudication. A successor may point to a failed parent's historical commit; it should not require that the live path retain old bytes forever. Conversely, changing live bytes and refreshing an already audited manifest must never be represented as preserving the same freeze.

The lifecycle rule becomes:

```text
historical commit/blob identity → observed gate state → append-only adjudication
  → prospective successor identity → separate execution closure
```

A green current test suite is implementation evidence for current bytes. It is not evidence that a prior fail-closed observation was preserved in place.

## Limits

This audit establishes repository custody facts, not benchmark construct validity. The task families, procedures, endpoints, and authority remain builder-authored synthetic calibration artifacts. There are two fixed families and one attempt per cell. No transfer, agent capability, utility, expert provenance, professional validity, production fitness, or readiness claim is licensed. No v8 or rerun follows from this adjudication.
