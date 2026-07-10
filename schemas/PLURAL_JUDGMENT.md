# Plural judgment conformance

This contract is a bounded executable adaptation of the identification ladder in
`papers/agent-benchmarks/2026-07-11-expert-disagreement-human-feedback-validity.md`
(lines 95–186). It advances charter objectives B/C by testing machinery for
plural professional judgment without adopting the source's clinical domain.

The fixture preserves observer independence, evidence views, prospective
framework provenance, repeat links, rationales, uncertainty, reducibility
checks, and an explicit governance aggregation. The validator fails closed:

- `irreducible_disagreement` requires every declared reducibility gate;
- framework stratification requires prospective declarations and repeat checks;
- repeat links must retain observer and case identity;
- aggregation weights and output must be reproducible;
- an output no observer endorses must preserve every input as dissent; and
- claim limits must deny prevalence, professional validity, consensus, and
  cross-domain generality.

The schema is separate because existing trial grader observations and metric
records cannot represent prospective evaluative frameworks, repeat ratings,
reducibility dispositions, or unendorsed policy aggregation without conflating
an observation, decision rule, and validity claim. This is internal synthetic
contract calibration—not evidence about experts, a profession, or an agent.

Run:

```bash
python scripts/validate_plural_judgment.py schemas/fixtures/plural-judgment-conformance.json
python -m unittest tests.test_plural_judgment
```
