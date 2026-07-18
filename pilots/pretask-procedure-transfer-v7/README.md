# Pre-task procedure transfer v7: source-authorized zero-call freeze

V7 is a prospective mechanical repair of the frozen v6 canary and preflight failures. It preserves every v4/v5/v6 byte, including v6's failed reports, and does not unblock or rescore an earlier version. The epsilon/zeta tasks are synthetic internal mechanism probes, not benchmark domains or professional-validity evidence.

## Design boundaries

- `source-applicability.json` carries forward v6's builder-authored internal authority for the unchanged v4 proposition statements into **v7 internal calibration only**, retains proposition/file hashes and old valid-time labels, and resolves Z-P3 rollback order without editing v4 authority.
- `prepare_freeze.py` materializes answers with a local builder interpreter. `oracle.py` independently implements the source semantics and imports no builder, checker, or preflight. The checker consumes only candidate/private records.
- The public artifact contract is closed at every object level. Repeated keys, condition/treatment fields, unknown payloads, and non-finite numbers fail.
- Recursive JSON comparison requires exact types. Booleans are distinct from numbers; integer-form and decimal/exponent-form numbers are distinct (`1 != 1.0`); object key order and whitespace are irrelevant.
- Z-P3 rollback records still-open descendants from innermost outward and then the target. Ancestor commit remains invalid.
- `run_canaries.py` stages the nested output mountpoint before the read-only `/trial` bind, exercises two zero-call bubblewrap arms, and checks equal sandbox command envelopes. It is filesystem conformance evidence, not an agent trial.
- `preflight.py` checks oracle independence from parsed static/dynamic import dependencies, not comments or docstrings.

## Reproduce

```bash
python pilots/pretask-procedure-transfer-v7/run_canaries.py --report pilots/pretask-procedure-transfer-v7/canary-report.json
python pilots/pretask-procedure-transfer-v7/preflight.py --check-paths --report pilots/pretask-procedure-transfer-v7/preflight-report.json
python -m unittest tests.test_pretask_procedure_transfer_v7 -v
```

No model/provider/executor row is authorized. All seven claim ceilings remain false. Any failed frozen-byte or semantic gate must be retained exactly rather than repaired in place. A separate commit-bound independent freeze review is required before execution can be considered.
