# Completion-evidence conformance slice

This internal synthetic pilot exercises a reusable boundary for executable knowledge-work artifacts:

```text
pinned source + valid environment + accepted setup
→ zero-exit independent execution
→ complete artifact + semantic check
→ endpoint status
→ self-report calibration
→ downstream eligibility
```

It converts the release-audited DeployBench failure into executable checks without adding a deployment-specific schema. `run.py` receives only each case's observation; expected labels remain calibration oracles in `suite.json`. The committed report is an exact deterministic replay.

## Design choices

- **Execution beats artifact presence.** A nonzero exit cannot pass merely because partial/nonempty files exist.
- **Semantic evidence beats nonemptiness.** A complete but wrong output fails.
- **Evaluator deltas are separate.** If evaluator action satisfies an agent requirement, the trial is instrument-invalid rather than agent success.
- **Alternate paths are admissible when predeclared.** The equivalent setup passes without matching the canonical implementation.
- **Invalid runs leave the endpoint denominator.** Service, harness, and instrument invalidity are separately typed.
- **Completion is a claim.** Honest partial status differs from false success even though neither is downstream-eligible.
- **Eligibility is narrow.** It means only that this synthetic prerequisite projection passed; it does not imply task completion beyond the projection, reproduction, professional utility, or readiness.

The ten frozen cases cover clean success, partial artifacts with nonzero execution, stale source, unavailable asset/service, evaluator-supplied requirement, semantically wrong nonempty output, an accepted alternate setup, honest partial abstention, false success, and harness invalidity.

## Run

```bash
python pilots/completion-evidence-conformance/run.py
python -m unittest tests.test_completion_evidence_conformance
```

## Evidence and limits

See `provenance.json`. The primary source is the full DeployBench review and its pinned-release audit. All cases and labels are builder-authored adaptations for contract calibration. This artifact makes no agent-capability, deployment, reproduction, grader-population, professional-validity, safety, production-fitness, or readiness claim.
