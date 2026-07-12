# Held-out provenance-observation transfer

This prospective validation slice freezes hash-pinned JSON artifacts from two structurally different pilots that predate the queue task: the LH skill-adoption matched-pair records and vendor incident-response action-plan records. `freeze_inputs.py` records each source commit/time, pointers, operators, policy, thresholds, and a physically separate oracle before any extension.

The unchanged observation adapter was run first. Both cases produced correct relations but the v1 decision was `invalid_artifact_or_environment`: it hard-coded a required top-level `environment` object even when the frozen policy declared environment not applicable. That frozen failure is retained in `replay-report.json`. A single generic v1.1 extension, containing no pilot/domain/case tokens, preserves v1 derivation and adds an explicit `environment_required: false` policy. It was replayed once.

The replay removes case/shape identity on its blind pass, reverses criteria and declared set order, and probes hash/pointer mismatch, missing evidence, path escape, forbidden leakage fields, and representation failure. The source paths are references; prior pilot and evaluator bytes are not edited.

```bash
python pilots/provenance-observation-heldout-transfer/replay.py
python -m unittest tests.test_provenance_observation_heldout_transfer -v
```

A passing report establishes only exact adapter behavior for these two frozen pre-existing artifacts and mappings. It does **not** establish criterion equivalence, expert/professional validity, general evaluator validity, agent capability, production fitness, or readiness.
