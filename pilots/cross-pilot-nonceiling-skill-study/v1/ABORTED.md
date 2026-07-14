# v1 prospective stop record

**Status: aborted before model calls.** This file is additive; no previously frozen v1 byte was changed.

## Gate evidence

- `calibration/case-manifest.json` hash-binds ten builder-authored planted cases: positive, minimally wrong, shortcut, abstention/invalid, and alternative-valid for both clusters.
- `calibration/grade_calibration.py` replayed the independent and guide-shared rubrics on identical artifact bytes.
- Positive and alternative-valid cases scored 1.0 under both rubrics in both clusters. Shortcut and invalid cases failed both rubrics.
- The LH minimally-wrong case deliberately omitted the public task's `{{PROSPECTIVE:...}}` marker. The independent rubric failed it (11/12), while the frozen shared rubric passed it (12/12). Therefore the shared rubric did not discriminate the required minimally-wrong case. `calibration/calibration-report.json` records `passed: false` and the exact error `non-discrimination: lh/shared`.
- `preflight/canary-report.json` separately records six passing, zero-call bubblewrap/file-tool checks: two independent-construction views and four cluster-by-Skill agent views. Allowed files were readable, private/protected inputs and the repository were absent, writes outside `outputs/` were denied, and no model/provider call occurred.

The calibration failure activates `protocol.json`'s prospective failure action. None of the eight attempt IDs may run, regardless of the passing namespace canaries. This is evidence of an instrument blind spot, not evidence about a model, procedural guide, profession, safety, or readiness.

## Precise continuation

Preserve all v1 bytes and create **v2** prospectively. Before freezing v2 cases, make the guide-shared LH rubric explicitly operationalize the already-public distinction between source-reported numbers and analyst-chosen prospective thresholds (public task line 10; public guide step 6). Rebuild and hash a v2 grader/rubric package, rerun all five case classes for both rubrics and clusters, and require strict positive/minimally-wrong and positive/shortcut discrimination plus alternative-path parity. Only a separately committed passing v2 calibration and repeated zero-call canaries may unlock a new opaque schedule. Do not reuse the v1 attempt IDs or call results, and retain the same claim ceilings.
