# Pre-task procedure transfer v2: prospective input-only prerequisites

This internal-calibration package repairs the v1 source/task treatment failure and records the subsequent fail-closed package-generation attempt. It freezes two structurally unlike, builder-authored family corpora before four new task forms and keeps source authority, public task requirements, and private consequences in separate files.

- `families/` contains generator-visible family corpora and proposition manifests. Every proposition is explicitly an internal design hypothesis, not expert testimony or professional guidance.
- `tasks/` contains two opaque forms per family. Public prompts disclose the objective, inputs, deliverable, and fair consequence basis but not the corpus's complete procedure. Private records bind expected consequences and checks to source propositions and public bases.
- `protocol.json` freezes chronology, split, information envelopes, control-package authoring rules, endpoint independence, leakage scrubs, and claim ceilings.
- `generation/` preserves exactly one corpus-only model attempt per family: prompt, untouched output, usage, stdout/stderr, and report. Both outputs set the required `package_id` to JSON null. The original launcher accepted that defect; the independent readiness validator rejects it. Neither output was repaired or retried.
- `readiness-audit.json` pins every frozen input and generation byte and records the failed structural gate. Control packages, task-conditioned hindsight packages, endpoint checkers, isolation/equal-envelope canaries, and executor attempts were not created or run because the protocol requires stopping at the first failed gate.
- `validate.py` verifies the prospective firewall, all hashes, attempt chronology, reported zero included cost, and the fail-closed generation adjudication. It asserts that execution remains unauthorized.

The two families are methodological contrasts, not a scope commitment: evidence-based decision review produces a memo/register; incident change control produces a bounded state-transition plan/log.

```bash
python pilots/pretask-procedure-transfer-v2/validate.py --check-paths --self-test
python -m unittest tests.test_pretask_procedure_transfer_v2 -v
```

No expert provenance, professional validity, transfer, capability, utility, production fitness, or readiness is claimed. The retained result is a generator/contract failure, not evidence about either procedure family or an executor.