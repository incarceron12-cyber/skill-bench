# Provenance-observation negative controls

This prospective replay freezes three pre-existing, hash-pinned JSON artifacts from two structurally distinct pilots at commit `43ea727`. The physically separate oracle was declared before replay. Adapter v1.1 is reused byte-for-byte; the replay refuses to run if its hash changes.

The controls are fair consequences of public fields and generic operators: equal identifiers and equal action sets are matching controls; two pre-existing booleans with opposite values test substantive contradiction; crossing the vendor artifact's public authorized and blocked sets tests authority mismatch; absent observed/source pointers test insufficient observation and missing authority; applying a set operator to a scalar tests invalid representation; and requiring an undeclared environment tests environment invalidity. No private rubric answer is copied into a mapping, and no artifact is modified.

Blind replay removes IDs, permutes case/criterion order, and verifies path escape, hash/pointer mismatch, forbidden leakage fields, and domain-token independence. This validates only exact behavior on the frozen controls. Criterion equivalence, expert/professional validity, capability, general evaluator validity, production fitness, and readiness remain false.

```bash
python pilots/provenance-observation-negative-controls/replay.py
python -m unittest tests.test_provenance_observation_negative_controls -v
```
