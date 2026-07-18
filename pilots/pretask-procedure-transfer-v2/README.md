# Pre-task procedure transfer v2: prospective input-only prerequisites

This internal-calibration package repairs the v1 source/task treatment failure without generating a procedure package or calling a model. It freezes two structurally unlike, builder-authored family corpora before four new task forms and keeps source authority, public task requirements, and private consequences in separate files.

- `families/` contains generator-visible family corpora and proposition manifests. Every proposition is explicitly an internal design hypothesis, not expert testimony or professional guidance.
- `tasks/` contains two opaque forms per family. Public prompts disclose the objective, inputs, deliverable, and fair consequence basis but not the corpus's complete procedure. Private records bind expected consequences and checks to source propositions and public bases.
- `protocol.json` freezes chronology, split, information envelopes, control-package authoring rules, endpoint independence, leakage scrubs, and claim ceilings.
- `readiness-audit.json` pins all source/task bytes and records zero package-generation, model, and provider attempts.
- `validate.py` verifies the prospective firewall and all hashes. It does **not** declare the experiment execution-ready: package generation, package/control hashes, isolation, provider, and execution gates remain unrun.

The two families are methodological contrasts, not a scope commitment: evidence-based decision review produces a memo/register; incident change control produces a bounded state-transition plan/log.

```bash
python pilots/pretask-procedure-transfer-v2/validate.py --check-paths --self-test
python -m unittest tests.test_pretask_procedure_transfer_v2 -v
```

No expert provenance, professional validity, transfer, capability, utility, production fitness, or readiness is claimed.