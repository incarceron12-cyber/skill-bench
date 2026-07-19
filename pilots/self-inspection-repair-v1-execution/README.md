# Self-inspection repair v1 bounded execution

This package is the **separate execution layer** for the immutable instrument at
`pilots/self-inspection-repair-v1`, frozen at commit
`7d976a28b9f33337f2f90519964361388b3eae7f`. It does not modify or refresh any
v1 byte.

`launcher.py` verifies the independent PASS audit and every frozen Git blob,
requires its own exact launcher bytes on `origin/main`, reruns an outer-envelope
canary for all 12 assignments, checks the equal execution envelope, and requires
an exact-provider historical included-zero-cost witness before any call. It then
retains exactly one attempt per assignment (the two `no_second_attempt` rows use
zero provider calls), stopping before further calls if a usage record does not
confirm included zero cost.

Each retained assignment includes its complete prompt/information view, input
and output hashes, stdout-only redacted trace, usage/cost, typed terminal state,
and proposition-level observation → diagnosis → delta → criterion-local and
collateral rechecks → new-error/cost record. The study report keeps first/final
outcomes separate from six-condition descriptive contrasts.

```bash
python pilots/self-inspection-repair-v1-execution/launcher.py preflight
python pilots/self-inspection-repair-v1-execution/launcher.py execute
python pilots/self-inspection-repair-v1-execution/launcher.py replay
python -m unittest tests.test_self_inspection_repair_execution -v
```

The package licenses no self-correction, capability, treatment-effect,
professional-validity, utility, production-fitness, or readiness claim. A single
builder-authored two-shape run cannot support those claims.
