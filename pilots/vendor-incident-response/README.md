# Vendor incident response pilot

**Status:** internal, synthetic, non-releasable. No expert testimony or configured-agent trial is represented.

## General hypothesis

The source-authority, valid-time, persistent-workspace, artifact, action-safety, and cross-record evidence machinery can compose unchanged in a stateful incident-coordination task that is structurally different from the LH spreadsheet/memo pilot.

This advances charter objectives B and C through building/validation. Useful completion is narrow: validators resolve every path/hash, the deterministic grader detects all planted outcomes, and unsupported claims remain false. It does **not** establish professional validity, agent capability, representativeness, cross-domain generalization, real-world safety, or release readiness.

## Package

- `public-task.md`: public requirement and fair basis for private consequences.
- `workspace/`: current authoritative status, superseded status, service map, ordinary untrusted note, protected state, and lexical distractor.
- `pilot-manifest.json`: typed authority, valid time, inventory/mutation policy, artifact contracts, public/private checks, review provenance, and false claim gates.
- `benchmark-bundle.json`: valid existing benchmark-bundle contract; no schema fork and no fabricated trial.
- `expertise-transfer.json`: valid review-to-primitive record that explicitly says no domain expert participated.
- `calibration-cases.json`: six planted observations: secure useful completion, evidence error, unsafe action/mutation, over-refusal, invalid environment, and safe but incomplete work.
- `grade.py` / `grader-report.json`: executable classifier and replayed source-integrity report.
- `evidence-chain-audit.json`: intended-use → construct → requirement → response view → check → metric → bounded claim audit.

## Evidence basis and adaptations

Every hidden consequence maps to a public rule. Workspace role/valid-time/integrity requirements derive from the full Workspace-Bench review; source-authority and placement-to-consequence distinctions derive from the full ClawSafety review; initial-state and invalid-run boundaries derive from the full Workflow-GYM review. The incident scenario, fields, severity labels, artifact conventions, and thresholds are **unvalidated builder hypotheses**, not professional standards.

## Reuse comparison with LH pilot

| Boundary | LH skill-adoption pilot | This pilot | Result |
|---|---|---|---|
| Primary structure | Evidence CSV + recommendation memo about benchmark adoption | Persistent incident workspace + Markdown/JSON state decision | Meaningfully different task/state structure |
| Existing bundle validator | Used | Used unchanged | Reused |
| Existing expertise-transfer validator | Used | Used unchanged | Reused |
| Existing evidence-chain checker | Used | Used unchanged | Reused |
| Public/private fair basis | Evidence reconciliation requirement | Current/obsolete/ordinary-source authority rules | Reused pattern |
| Workspace/action machinery | Mostly interface/static source pack | Pinned inventory, protected zone, untrusted ordinary source, action consequences | Composed in a pilot package |
| Agent trial | Incomplete matched pair | None | Capability remains false |
| Expert validity | Failed/not run | Not run | Remains false |
| Schema extension | Prior work added reusable contracts | None | No fork required |

## Replay

```bash
python pilots/vendor-incident-response/grade.py --output pilots/vendor-incident-response/grader-report.json
python scripts/validate_benchmark.py pilots/vendor-incident-response/benchmark-bundle.json --check-paths
python scripts/validate_expertise_transfer.py pilots/vendor-incident-response/expertise-transfer.json --check-paths
python scripts/audit_evidence_chain.py pilots/vendor-incident-response/evidence-chain-audit.json --check-paths
python -m unittest tests.test_vendor_incident_pilot -v
```

The grader report is retained because it is real execution evidence. It licenses only deterministic fixture conformance at the recorded hashes.
