# Objective-grounded elicitation conformance slice

## Scope and charter fit

This zero-call internal calibration advances charter objectives **B** (expertise-to-evaluation methodology) and **C** (executable infrastructure). It tests a cross-domain design claim: an evaluator can keep a frozen elicitation objective, question opportunity and exposure, caused response, supported or unsupported profile revision, respondent correction, objective progress, semantic uptake, artifact/state consequence, stopping error, and burden separate.

The two retained work shapes are intentionally unlike:

- `procurement-decision`: an evidence-backed recommendation memo with an authority-sensitive conflict; and
- `incident-handoff`: a stateful operational handoff with an escalation boundary.

Each builder-authored synthetic pack is crossed with `no_elicitation`, `fixed_probe`, `adaptive_probe`, `oracle_profile`, `inferred_profile`, and `corrupted_profile` under an identical frozen downstream evidence/resource envelope. The 12 deterministic episodes include answers, refusal, nonresponse, spontaneous/probed/respondent-inferred/model-inferred/oracle-supplied claims, correction, justified escalation, premature and unsupported closure, artifact success without profile fidelity, and separate burden.

## Evidence and design rationale

The package hash-pins:

- `papers/agent-benchmarks/2026-07-17-inciteresearch-prequestion-elicitation-validity.md`, especially review lines 21–25, 152–169, and 235–261, for the profile-claim ladder, true/inferred/corrupted controls, correction, criterion independence, equal resources, and consequence separation;
- `papers/agent-benchmarks/2026-07-17-organizational-tacit-knowledge-simulation-validity.md`, especially review lines 158–176 and 223–255, for claim routing, authority, claim-state stopping, burden, and the synthetic claim ceiling;
- `docs/benchmark-design-taxonomy.md`, the section headed “Objective-grounded elicitation is a claim-routing episode, not question style,” for prospectively frozen objectives, terminal claim states, event lineage, stop errors, and separate denominators. `provenance-boundary.json` preserves the authoring-time Git commit/blob/SHA while checking three bounded live semantic locators, so unrelated canonical edits do not invalidate the fixture; and
- every retained artifact, validator, and test in `pilots/interaction-evidence-conformance/` through explicit provenance hashes. That prior pilot remains byte-preserved rather than copied or modified.

The reusable implementation is `scripts/validate_objective_grounded_elicitation.py`, a domain-neutral observer over frozen public claim packs, objectives, and episodes. This is a conformance package, not a new repository schema.

## Oracle firewall and claim ceiling

`private/oracle.json` contains planted private claim truth and expected classifications/final states. It is hash-pinned and unavailable to the observer during classification. Public `claim-packs.json` deliberately omits claim truth. `oracle_profile` episodes receive a treatment profile with explicit `oracle_supplied` provenance; that does not authorize the observer to read the private oracle. The replay compares results with the oracle only after public-record classification.

All claims, responses, roles, corrections, profiles, and consequences are builder-authored synthetic data. The package provides **no evidence** of human or expert participation, an elicitation effect, professional validity, scientific utility, agent capability, safety, production fitness, or readiness. Artifact/state success does not imply profile fidelity. The consented-session and elicitation-session-contract gates remain blocked.

## Files

- `claim-packs.json` — two public frozen packs, authority metadata, unknown/sensitive fields, rival interpretations, and consequences; no private truth.
- `objectives.json` — beneficiary/use, required/optional claims, authority, question policy, stop/escalation rules, burden/loss, criterion identity, and consequence for each pack.
- `episodes.json` — six-condition matrix, public event records, separate claim/progress/uptake/effect/stop/burden records, matched resource envelope, provenance, and false claim flags.
- `private/oracle.json` — planted truth and expected classifications/final states; excluded from evaluator input.
- `provenance-boundary.json` — immutable authoring-time taxonomy identity plus hashed historical/live semantic locators; it fails closed on path, historical-object, locator, or locator-hash drift without pinning the entire mutable live taxonomy.
- `build_fixture.py` — deterministic authoring script; no model, network, or human calls.
- `../../scripts/validate_objective_grounded_elicitation.py` — public-record validator, observer, denominator report, and post-classification oracle replay.
- `replay-report.json` — retained real execution output.
- `../../tests/test_objective_grounded_elicitation.py` — replay and required leakage/promotion/correction/coupling/resource/stopping/burden mutations.

## Reproduce

```bash
python pilots/objective-grounded-elicitation-conformance/build_fixture.py
python scripts/validate_objective_grounded_elicitation.py --check-paths \
  --report pilots/objective-grounded-elicitation-conformance/replay-report.json
python -m unittest tests.test_objective_grounded_elicitation -v
```

Useful completion is exact replay of the two-pack × six-condition matrix, complete provenance/hash checks, rejection of every required mutation, separate denominators, and retention of every false claim flag.
