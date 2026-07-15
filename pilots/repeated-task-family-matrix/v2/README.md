# Repeated task-family matrix v2

This internal synthetic pilot repairs v1's underdisclosed exact-label defect with a **publicly disclosed controlled vocabulary**. Every form discloses three accepted decision labels and three accepted action labels; evidence selection and rationale are graded separately. The tradeoff is explicit: deterministic fairness improves, but the construct is label mapping rather than open-ended professional expression.

The four newly authored forms span two unlike methodological families (`resource_governance` and `record_integrity`). Each form traces its design hypothesis to a local full-paper review in `task-health.json`. They are not expert-authored professional tasks, and no v1 observed phrase, grade, output, or outcome is an authoring, calibration, or admission source. `protocol.json` pins the pre-v2 v1 Git tree and preflight rejects v1 byte drift.

Before model calls, each form's grader must accept the canonical value and two disclosed alternative realizations for both decision and action, reject two near-neighbor wrong values for both fields, reject wrong evidence and invalid JSON, and accept a second rationale form. Isolation, private-input leakage, service, included-cost, component-hash, origin/main, and pushed-instrument gates are also fail-closed.

Workflow:

```bash
python build_frozen_instrument.py
python run_matrix.py preflight                 # zero model calls
# commit and push frozen README/protocol/forms/grader/runner
python run_matrix.py preflight --require-pushed
python run_matrix.py execute                   # each declared attempt once
python run_matrix.py replay
```

Execution retains separate intended, service-valid, environment-valid, grader-valid, and substantively graded denominators. No retry, replacement, tuning, or outcome-based admission is allowed. Provider confidence is recorded only when genuinely emitted. The study cannot establish expertise, professional validity, general capability, safety, production fitness, readiness, confidence-policy utility, or population transport.
