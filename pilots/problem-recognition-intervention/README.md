# Problem-recognition intervention conformance slice

This **non-releasable internal calibration package** exercises the general hypothesis that matched framing conditions can separate recognition from execution. It is not a professional task, agent trial, treatment estimate, or expert-validated benchmark.

The package instantiates the KWBench review's transferable design: the same synthetic evidence appears under situation-only, minimal-frame, and fully-specified conditions; cue extraction, framing, inquiry, action, and artifact state remain separate; and a positive discrepancy has a negative near neighbor. Alternate framings are accepted for the positive case. Invalid environment evidence abstains rather than becoming agent failure.

Provenance is recorded in `conformance.json`. Scenario content is an explicit builder-authored design hypothesis. No gated KWBench rows were used.

Replay and verify:

```bash
python scripts/validate_problem_recognition.py pilots/problem-recognition-intervention/conformance.json --check-paths --report pilots/problem-recognition-intervention/replay-report.json
python -m unittest tests.test_problem_recognition
```

The deterministic replay tests instrumentation semantics only. Expert adjudication, real matched agent trials, repeated/clustered uncertainty, and alternate-path calibration are required before stronger claims.
