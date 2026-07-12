# Provenance-first evaluator conformance suite

This prospective internal calibration tests whether one domain-neutral evaluator can consume provenance-pinned observed-versus-authoritative comparisons across three work shapes: a structured professional artifact, a stateful action trace, and handoff/memory state.

## Freeze boundary

`freeze_inputs.py` created every authoritative artifact, each observed mutation as its own file, the transformation record, qualification policy, criterion basis, schema-valid observation contract, and separate private oracle **before** `candidate/evaluator.py` was authored. The input contract contains no oracle, expected outcome, rationale, case-family, or domain-token fields. Its locators and SHA-256 hashes are checked by the pre-existing fail-closed validator. The candidate sees only the observation rows.

The non-compensatory policy requires exact safety/authority, invalid-environment, and insufficient-evidence behavior plus representation invariance and exact overall agreement. No aggregate score can compensate for a critical gate failure.

## Reproduce

```bash
python pilots/generated-evaluator-validity/validate_observation_input_contract.py pilots/provenance-first-evaluator/evaluator-inputs/observation-contract.json
python pilots/provenance-first-evaluator/replay.py
python -m unittest tests.test_provenance_first_evaluator -v
```

All sources and mutations are builder-authored, redistributable repository fixtures. This suite does not license criterion equivalence, expert/professional validity, general evaluator validity, agent capability, production fitness, or deployment readiness.
