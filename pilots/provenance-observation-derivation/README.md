# Provenance-pinned observation derivation slice

This prospective internal calibration exercises the boundary that the earlier `pilots/provenance-first-evaluator/` suite intentionally did not: deriving typed comparison relations and sufficiency states from frozen files rather than accepting authored relations.

## Design and provenance

`freeze_inputs.py` was executed before `adapter.py` was authored. It froze eight builder-authored cases across two reusable JSON shapes (record/set state and ordered workflow state), authoritative files, observed files, criteria, transformation identity, split, adjudication procedure, hashes, and a physically separate private oracle. Inputs are redistributable internal fixtures. The adapter receives only manifest cases, criteria, and repository root. It resolves JSON pointers and typed operators (`equal`, `set_equal`, `member`); it rejects stale hashes, escaped paths, bad pointers, unsupported representations/operators, and oracle/rationale/family/domain/label fields.

`replay.py` executes the frozen policy once, performs a second pass with criteria reversed and case identity removed, checks object-order and declared set-order invariance, and runs fail-closed mutations. Reports separate relation-level errors from final-decision errors. A non-compensatory failure yields rejection.

## Reproduce

```bash
python pilots/provenance-observation-derivation/replay.py
python -m unittest tests.test_provenance_observation_derivation -v
```

The slice can establish only exact behavior on these internal cases. It does **not** license criterion equivalence, expert/professional validity, general evaluator validity, agent capability, production fitness, or deployment readiness.
