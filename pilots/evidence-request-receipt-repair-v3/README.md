# Evidence-request receipt and repair pilot v3

This prospective internal pilot versions, but never modifies, the retained v1/v2 artifacts. It compares the same natural-language request interface with and without a fail-closed interpretation receipt and one bounded repair opportunity. Both conditions use the same frozen parser, scenarios, budgets, release rules, prompt, grader, configured system, and two purposive repeats per scenario shape.

A receipt exposes only `status`, a normalized interpreted topic (or `null`/`multiple topics`), and `repair_eligible`. It never exposes evidence IDs, candidates, availability, values, content, answers, or a menu. An unmatched or ambiguous request in the receipt condition can be repaired once; repair consumes the failed-request charge but has no additional charge. The control condition receives only the ordinary failed/ambiguous access status.

`instrument/conformance-cases.json` contains independently authored positive paraphrases, multi-target ambiguities, unknown-topic negatives, and domain-token perturbations for both shapes. Preflight deterministically checks routing, fail-closed behavior, receipt/parser agreement, the one-repair budget, and the feedback firewall before any model call.

Commands:

```bash
python pilots/evidence-request-receipt-repair-v3/freeze_protocol.py
python pilots/evidence-request-receipt-repair-v3/run_study.py preflight
# commit and push the frozen instrument before execution
python pilots/evidence-request-receipt-repair-v3/run_study.py execute
python pilots/evidence-request-receipt-repair-v3/run_study.py replay
```

This synthetic, purposive instrument supports only exact conformance and execution observations. It does not license claims about inquiry quality, agent/professional capability, expert validity, cross-domain generality, safety, production fitness, or readiness.
