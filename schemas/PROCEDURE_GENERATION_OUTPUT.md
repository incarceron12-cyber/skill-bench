# Source-only procedure-generation output contract

## Purpose and boundary

`procedure-generation-output.schema.json` is the pre-generation contract for a candidate procedure distilled from one frozen source corpus. It is intentionally narrower than `procedure-package.schema.json`: this contract judges **generator output identity, source coverage, and information hygiene before task execution**; the older package contract judges a fully assembled procedure/data/tool/oracle execution instrument. Neither contract establishes expertise or professional validity.

The contract was added after the retained v2 pre-task procedure study produced two packages with `package_id: null` and its launcher nevertheless reported both as valid. The v2 files remain immutable. The validator here is independent of that launcher and no model or task execution is part of this calibration slice.

## Enforced invariants

1. `package_id`, package version, family/version, and exact source SHA-256 are non-empty and schema-valid.
2. The generation view is source-only and exactly equals a predeclared path allowlist; downstream task IDs and private-path fragments fail closed.
3. Every source proposition has exactly one reciprocal binding to one or more generated clauses; clauses and primitive bases may not cite unknown propositions.
4. Every source contradiction, threshold, artifact convention, and failure signature is either projected once or represented by a typed omission. Silent loss and project/omit overlap are rejected.
5. The seven project claim ceilings remain explicitly false. Structural conformance licenses only the statement that this validator accepts these exact synthetic bytes.
6. A launcher report is untrusted evidence. If it says `launcher_valid: true` for independently invalid bytes, the validator emits `false launcher acceptance`.

The committed valid fixture reuses the already frozen builder-authored family-alpha corpus only as internal contract calibration. It includes a typed omission to exercise the no-silent-loss partition. The null-identity fixture and false-acceptance report are planted defects, not provider outputs. They reproduce the v2 defect class without modifying or rerunning v2.

## Verification

```bash
python scripts/validate_procedure_generation_output.py \
  schemas/fixtures/procedure-generation-output-valid.json \
  --source pilots/pretask-procedure-transfer-v2/families/evidence-decision/corpus.json \
  --policy schemas/fixtures/procedure-generation-output-policy.json
python -m unittest tests.test_procedure_generation_output -v
```

A future v3 may reference this committed contract and validator only after freezing entirely new source and task bytes prospectively. This artifact does not authorize v3 authoring, model calls, executor attempts, or claims of transfer, capability, utility, production fitness, or readiness.
