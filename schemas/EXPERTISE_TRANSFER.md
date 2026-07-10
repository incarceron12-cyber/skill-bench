# Expertise-to-evaluation authoring contract v0.1

`expertise-transfer.schema.json` and `scripts/validate_expertise_transfer.py`
turn an authoring workflow into a checked evidence graph:

```text
expert/observed claim → benchmark primitive → critical-incident scenario
                      → source/trap/artifact → observable check → gated release
```

This contract is upstream of `benchmark-bundle.schema.json`. The authoring packet
records why a requirement or check exists and whether it is ready; a benchmark
bundle records an executable task and its trials. A later export can translate a
passed authoring packet into one or more bundles without discarding provenance.

## Seven bounded stages

1. **Elicitation:** capture claims at their actual evidence strength. A benchmark
   review or synthetic hypothesis must not masquerade as domain-expert testimony.
2. **Primitive mapping:** translate claims into requirements, evidence rules,
   contradictions, thresholds, conventions, caveats, traps, failure signatures,
   preferences, and safety constraints.
3. **Scenario design:** place primitives in a role, stakeholder decision, and
   critical incident that can expose expert/novice differences.
4. **Source pack:** bind scenarios to ranked, provenance-bearing sources and
   explicit traps with failure signatures and fairness rationales.
5. **Rubric:** map every check to primitives, artifact evidence, explicit pass/fail
   boundaries, and observable failure signatures.
6. **Pilot validation:** require empirical run/adjudication evidence rather than
   declaring quality from schema completeness.
7. **Release review:** separately gate leakage and expert validity and preserve
   known limitations.

The validator requires every stage before `current_stage` to have passed and
requires evidence paths for passed gates. `releasable` is impossible until all
seven gates plus leakage and expert-validity review pass.

## Session-derived projection validity

Optional `session_projections` make the transformation from an observed episode
to a benchmark counterfactual inspectable. They preserve the episode and
resolution, typed and hashed transformations, omissions, answer-bearing hindsight,
target, independent equivalence evidence, authorization, and the exact claim the
record licenses. Real demand may license `demand_inspired_task`; it does not by
itself license `session_replay_fidelity`. Replay additionally requires an
independent equivalent review, evidence for every omission's irrelevance, and no
answer-bearing hindsight used to author the task or rubric. `internal_synthetic`
records remain licensed only for internal conformance tests.

Optional `rubric_dimensions` reject identical task-specific guidance copied across
nominally distinct dimensions. Shared guidance is valid only when every affected
score is explicitly `holistic` and names the same `holistic_group`.

## Anti-surprise-check invariant

Private and hidden checks must name at least one **public** basis primitive. They
may test a held-out consequence of a disclosed professional principle, a safety
necessity, or an internal calibration property; they cannot create an undisclosed
obligation. This makes the review principle “private consequences, not hidden
rules” executable rather than advisory.

## Provenance and rationale

| Contract choice | Design reason | Evidence |
|---|---|---|
| Claims retain basis, contributor, locator, confidence, corroboration, and provenance | Builder interpretation must remain distinguishable from expert statements, observed work, and source evidence. | `.hermes.md` evidence standard; `reports/scouting/2026-07-10T030657Z-expert-elicitation-gap.md` |
| Every primitive maps bidirectionally to scenarios and checks | Tacit expertise only becomes evaluable when it changes scenario evidence and scoring. | `docs/compounding-system.md`, “How domain expertise becomes a benchmark” |
| Scenarios require a decision and critical incident | Generic job descriptions do not expose difficult cues, judgments, or failure signatures. | `templates/task-metadata.md` §§2–4; `docs/concepts/cognitive-task-analysis-to-benchmark-authoring.md` |
| Traps require mechanism, source links, failure signature, and fairness basis | “Trick questions” without a professional rationale reduce validity. | `.hermes.md` benchmark-building standard; `templates/task-metadata.md` §§4, 11 |
| Checks require observable evidence and explicit failure signatures | State transitions and artifact hooks reduce judge degrees of freedom. | `papers/agent-benchmarks/2026-07-10-lh-bench-skill-grounded-evaluation.md` |
| Quality and release are staged gates | Schema-valid does not mean expert-valid, leakage-safe, calibrated, or releasable. | LH-Bench review limitations and action items |
| Projection lineage is not equivalence | A real source can be rewritten with omitted failures and answer-bearing hindsight; claim licensing must follow transformation evidence. | `papers/agent-benchmarks/2026-07-11-enterpriseclawbench-session-derived-validity.md` §§Two public-safe traces, Unique insight |

The fixture is intentionally at the **rubric** stage and `not_ready`. It is based
on a full benchmark review, not a domain-expert session, and says so in both the
contributor record and release limitations. The reviewed CTA method and the
session record at `templates/expertise-elicitation-session.md` define how a future
real contribution should be captured; neither upgrades the synthetic fixture to
expert testimony.

## Validate

```bash
python scripts/validate_expertise_transfer.py --check-paths \
  tests/fixtures/valid-expertise-transfer.json
python -m unittest tests.test_validate_expertise_transfer -v
```

`--check-paths` checks source-pack paths, provenance local paths, and quality-gate
evidence paths against repository files. Output artifact paths are contracts for
future runs and are not required to exist while authoring.
