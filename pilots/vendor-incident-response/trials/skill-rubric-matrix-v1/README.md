# Prospective vendor-v2 Skill × rubric matrix v1

This versioned directory is an internal, synthetic intervention/instrument-separation study. It preserves all earlier vendor pilot and trial bytes.

## Frozen design

`protocol.json` was created before any matrix model call. It freezes the exact vendor-v2 task/workspace, base launcher substrate, model/provider/file-only tool envelope, public guide, independent and guide-shared rubrics, six opaque randomized attempt IDs (three per Skill condition), no replacement/retry/adaptation, eligibility and cost gates, dual-rubric evidence views, four estimands, one-task cluster boundary, and claim ceilings.

The independent rubric's declared construction view contains only the public task and six visible workspace sources. `rubrics/independent-construction-manifest.json` prohibits the guide, shared rubric, grader, calibration cases, and private manifest. A zero-call construction canary tests that filesystem boundary. This is auditable procedural independence, not proof that one builder had no prior conceptual overlap.

The public guide traces every claim to disclosed task/source paths. It adds no private obligation. Both rubrics are private from agents; every retained output is scored by both rubrics on identical bytes. The shared rubric intentionally exposes its guide lineage.

## Commands

```bash
# prospective validation and zero-call firewalls
python scripts/report_vendor_skill_rubric_matrix.py validate
python scripts/run_vendor_skill_rubric_matrix.py construction-canary
python scripts/run_vendor_skill_rubric_matrix.py canary --attempt-id mx-a7f2c1
python -m unittest tests.test_vendor_skill_rubric_matrix -v

# execution only after protocol commit/push and passing cost/isolation gates
python scripts/run_vendor_skill_rubric_matrix.py run --attempt-id <frozen-id>
python scripts/report_vendor_skill_rubric_matrix.py record
python scripts/report_vendor_skill_rubric_matrix.py replay
```

## Claim boundary

This single synthetic source-task cluster can describe retained attempt outcomes, no-Skill/public-Skill score contrasts under each rubric, within-output rubric contrasts, and their interaction. With three attempts per condition and one source task it cannot establish a general Skill effect, capability, expert/professional validity, safety, production fitness, cross-domain generality, or readiness.
