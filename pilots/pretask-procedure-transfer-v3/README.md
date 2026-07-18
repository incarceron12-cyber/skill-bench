# Pre-task procedure transfer v3: prospective output-contract freeze

## What this slice establishes

This internal-calibration slice freezes an entirely new prospective instrument before procedure generation. It tests the general hypothesis that source-to-procedure transfer can be evaluated without task hindsight only when the source, task, private consequence, output identity, and claim boundary are independently versioned and fail closed.

The two synthetic families are intentionally unlike:

- **family-gamma** is numerical indivisible capacity apportionment with ordering, protected capacity, and a conservation ledger;
- **family-delta** is graph closure with identity-changing transformations and a complete lineage manifest.

They are methodological contrasts, not a commitment to resource allocation, publishing, or any other domain.

## Frozen artifacts and provenance

- `families/*/corpus.json` contains builder-authored source authority, proposition locators and chronology, contradictions, thresholds, artifact conventions, and failure signatures. Every proposition is an `internal_design_hypothesis`; there is no external or expert source.
- `tasks/*/public.md` contains two untouched opaque forms per family. `tasks/*/private.json` freezes expected consequences and checks after source freeze, with every check bound to both a source proposition and an exact sentence in its public task.
- `generation-policies/*.json` exposes exactly one source corpus per family and pins `schemas/procedure-generation-output.schema.json` plus `scripts/validate_procedure_generation_output.py` to commit `a3640af8b7e0788fcc90aace9fc587ea42d50d0a`.
- `preflight/reference-packages/*.json` are builder-authored source-only **conformance witnesses**. They prove that every source proposition and primitive can be represented under the committed contract. They are not model outputs, treatments, executor aids, controls, or evidence of transfer.
- `freeze-manifest.json` pins exact bytes for the contract, sources, policies, witnesses, tasks, and private specs.
- `validate.py` enforces source-before-task chronology, exact hashes, non-reuse of exact v1/v2 bytes, authority labels, source-only visibility, task/private leakage scrubs, exact public bases, exhaustive package bindings, zero attempts, all-false claims, and absence of generation/control/checker/trial directories.

The mutation gate rejects, for both families: null package identity, a launcher that falsely accepts independently invalid output, silent primitive omission, invalid proposition basis, and claim upgrade.

## Deliberate stop boundary

This freeze contains no generated package, treatment control, endpoint checker implementation, model/provider call, executor attempt, or task execution. A later separately queued task may generate one source-only candidate per family only from these exact bytes after this commit is pushed. Any failed output gate must stop the study without repair-in-place.

## Verification

```bash
python pilots/pretask-procedure-transfer-v3/validate.py --check-paths \
  --report pilots/pretask-procedure-transfer-v3/preflight/report.json
python -m unittest tests.test_pretask_procedure_transfer_v3 -v
```

Passing this preflight licenses only the statement that the committed synthetic bytes satisfy the prospective freeze contract. Expert provenance, professional validity, transfer, agent capability, utility, production fitness, and readiness all remain false.
