# Pilot: advise on adopting skill-grounded scoring

**Status:** non-releasable internal calibration pilot; the evidence-link check is executable, but no domain expert has approved the procedures, task, or rubric.

## Scenario

Act as a benchmark program analyst advising a program lead whether to adopt skill-grounded scoring now, reject it, or run a controlled pilot. Produce a spreadsheet-compatible evidence matrix and decision memo from the supplied evidence pack. The critical incident is that the evidence contains both attractive aggregate agreement results and weak individual human/automated concordance, plus a promising but seven-run execution ablation.

This scenario tests evidence reconciliation and decision calibration, not recall of LH-Bench. The task must be answerable from supplied files with network denied.

## Files

- `source-pack/decision-evidence.csv`: row-level decision evidence derived from the deep local LH-Bench review.
- `source-pack/manifest.json`: source authority, visibility, locators, and derivation.
- `public-skill.md`: public workflow principles and artifact interface.
- `candidate-procedures.json`: two plural candidate routes, explicitly pending expert approval.
- `rubric-skeleton.json`: public requirements and private held-out consequences.
- `expertise-transfer.json`: authoring/evidence graph fixture.
- `benchmark-bundle.json`: executable-contract task skeleton with zero fabricated trials.
- `validation-plan.md`: evidence required to move beyond schema validity.

## Executable evidence-link slice

Run the deterministic public check against an output pair:

```bash
python scripts/grade_lh_evidence.py \
  --matrix outputs/evidence-matrix.csv \
  --memo outputs/recommendation.md
```

The grader emits `check-result-v0.1`. It checks six deliberately inspectable properties: required columns, evidence-ID resolution, exact source authority, exact source scope, exact caveat preservation, and numeric memo citation linkage. Calibration fixtures live under `calibration/`: one cautious pass plus agreement-overclaim, tiny-ablation-overclaim, and malformed-source failures.

This is intentionally **not** an entailment grader or a substitute for professional judgment. Exact string preservation makes a bounded provenance failure surface executable; contradiction reconciliation, causal appropriateness, decision quality, and alternative valid phrasings remain human-calibrated. The distinction follows the consulting review's separation of source existence, support, authority, scope, and freshness rather than pretending one citation check establishes them all.

## Difficulty knobs

| Knob | Easier | Harder | Construct guarded |
|---|---|---|---|
| Caveat salience | caveat in same row | caveat only in reviewed source locator | evidence retrieval vs reconciliation |
| Contradiction distance | adjacent agreement/validity rows | separate files/sections | context tracking |
| Distractor quality | explicit “directional” labels | polished adoption summary using E01/E08 only | overclaim resistance |
| Source count | one reviewed source | independent expert notes and production evidence | authority selection |
| Decision stakes | internal pilot | public procurement/release | threshold judgment |
| Missingness | all scopes supplied | unequal run counts/exclusions require qualification | missing-data reasoning |

Do not increase difficulty by hiding a new obligation. Every variant must preserve the public basis and update provenance.

## Professional traps

1. **Agreement-is-validity:** cite κ=0.60 and variance=0.10 as proof that automated scores reflect professional quality, omitting κ=0.06/0.08 and the one-expert threshold evidence.
2. **Tiny-ablation causality:** cite the +0.87 Codex delta or 2/7 no-skill deployments as a stable causal effect while omitting the seven-run scope and harness/integration confounds.

Both are evidence-backed failure signatures from the reviewed source, not arbitrary tricks. The deterministic grader's provenance convention is public; human check boundaries for contradiction and causal judgment remain private held-out consequences of disclosed principles.

## Provenance boundary

The review and underlying immutable PDF/text were actually read by the research worker recorded in the queue. This build consumes that reviewed artifact; it does not claim a new paper review. Spreadsheet columns, memo format, candidate route details, weights, and adoption-threshold wording are **unvalidated design hypotheses** introduced by the benchmark builder. They are release-gated accordingly.
