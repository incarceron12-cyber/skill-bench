# Commit-bound freeze custody

`schemas/freeze-custody.schema.json` and `scripts/validate_freeze_custody.py` define a prospective, append-only custody envelope for benchmark freezes. The contract is intentionally separate from task, grader, metric, and validity contracts: it answers **which immutable bytes were frozen, what gates those bytes actually produced, which freeze authorized execution, and how a later repair is recorded without rewriting history**.

## Charter fit and claim boundary

This bounded building/validation slice advances charter objectives B and C. It produces a reusable schema, semantic validator, historical conformance fixture, and mutation tests. It clarifies whether source packs, instruments, graders, and retained failures remain reconstructable after their live paths change. The mechanism is domain-neutral and does not make custody the benchmark construct.

The fixture is internal contract calibration. It makes no agent-capability, construct-validity, expert-provenance, professional-validity, or readiness claim. It does not rerun or repair any pilot.

## Lifecycle

```text
immutable commit/tree/blob identities
  -> observed gate states resolved from those historical blobs
  -> optional execution closure against that exact freeze
  -> append-only adjudication of later changed bindings
  -> separately identified successor version
```

A freeze contains:

- a full Git commit and root-tree identity;
- exactly one manifest blob plus typed component/external bindings;
- Git object identity for every binding and byte size/SHA-256 for blobs;
- gate outcomes with JSON Pointers into bound historical evidence.

A successor must have a different freeze ID, instrument version, and descendant commit. Its adjudication must enumerate **every predecessor binding whose Git object changed**. The successor may reuse paths, but it cannot reuse the predecessor's identity. This permits live development while preserving the failed or superseded parent as an immutable historical record.

An execution closure names the freeze that authorized execution, the source commit, the exact manifest blob, and the execution-package tree. Every frozen binding must have the same Git object at the execution source. A manifest refreshed after execution therefore cannot close an older run.

## Evidence-to-rule map

Primary project evidence:

- `docs/concepts/pretask-procedure-transfer-v6-v7-custody-adjudication.md`
- `reports/validation/2026-07-19-pretask-procedure-v6-v7-custody-adjudication.json`
- `scripts/audit_v6_v7_freeze_custody.py`
- `scripts/validate_provenance_boundary.py`

| Enforced rule | Evidence and rationale |
|---|---|
| Commit plus root tree and per-path Git object identity | The adjudication concludes that a path plus mutable manifest is not durable custody and recommends commit/blob/tree identity (concept §§Reconstruction method, Reusable design consequence). `validate_provenance_boundary.py` already fails closed on historical commit/blob mismatch. |
| Blob size and SHA-256 close at the same commit | The replay recomputed all historical v7 size/hash bindings at both audited sources (concept lines 19–31; machine report `historical_binding_recomputation`). Git identity protects repository custody; SHA-256 preserves the existing content-addressed contract. |
| Gate states resolve from bound historical JSON | The v6 canary and preflight changed from FAIL to PASS after repair, so current green reports cannot replace the observed frozen failure (concept §§Two v6 states, Limits; machine report `state_adjudication`). |
| Changed predecessor bindings are exhaustively enumerated | The case audit explicitly fails when a changed binding is omitted and found six rewritten v6 bindings plus the v7 manifest refresh (concept lines 29–31, 39–52; machine report `retrospective_mutation`). |
| Repair creates a distinct successor and append-only adjudication | The reusable consequence says a repair must be a new version or append-only adjudication rather than a refreshed audited manifest (concept lines 88–99). |
| Execution closure uses the original manifest and frozen bindings | The v7 execution remains licensed only at its freeze/execution commits; current HEAD's refreshed manifest is not execution-time evidence (concept §§V7 execution closure, Claim adjudication; machine report `execution_closure`). |
| Claim ceiling stays false in calibration | The adjudication establishes custody facts only, not transfer, capability, utility, expert, professional, production, or readiness claims (concept §Limits; machine report `claim_ceiling`). |

## Authoring a future freeze

1. Commit the prospective instrument, manifest, source pack, external bindings, and gate reports before execution.
2. Record the full commit, root tree, and each manifest/component/external Git object. For blobs also record byte size and SHA-256.
3. Record each gate state separately, pointing to a bound JSON evidence blob and a stable JSON Pointer. Never infer an old outcome from the live file.
4. Run:

   ```bash
   python scripts/validate_freeze_custody.py path/to/custody-record.json
   ```

5. Bind execution to the validated freeze ID, exact manifest blob, execution source commit, and execution-package tree.
6. If any frozen binding later changes, leave the old freeze record untouched. Add an adjudication listing every changed predecessor binding and create a successor with a new ID/version and identities.
7. Do not describe a successor's PASS as retroactively changing its predecessor's FAIL. Re-score or re-run only under a separately authorized protocol.

## Conformance fixture

`fixtures/freeze-custody/v6-v7-breach-conformance.json` is a compact projection of the committed v6/v7 custody facts. It records the original audited freeze, the later repaired state as a distinct successor, the seven changed bound paths (six v6 files plus the refreshed v7 manifest), the historical FAIL and later PASS gate states, and execution closure against the original manifest.

`tests/test_freeze_custody_contract.py` plants the prohibited alternatives and requires rejection of:

- in-place frozen-byte re-identification;
- audited-manifest hash refresh;
- an omitted changed binding;
- replacement of historical FAIL with PASS;
- closure against the post-hoc manifest.

The valid case accepts the separately versioned successor/adjudication chain and verifies that Git reconstructs the old FAIL bytes while the live path contains later PASS bytes.

## Scope and continuation

This contract applies prospectively. Historical pilots are not mass-migrated, and pretask-procedure-transfer v1–v7 remains closed. A future freeze author can adopt this envelope when producing a new instrument version. Integration into a common freeze generator should wait until a second independently authored freeze exercises the format; that evidence can show which fields are reusable versus repository-specific.
