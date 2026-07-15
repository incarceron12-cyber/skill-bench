# Temporal artifact conformance slice v0.2

This versioned, internal synthetic package tests a general hypothesis from the complete CutVerse review: a static or final appearance cannot establish ordered behavior, synchronization, editable structure, export identity, or preservation. The machinery applies to timelines, event logs, simulations, scheduled workflows, and audiovisual artifacts; it is not a media benchmark.

## Executable artifact

`generate_fixture.py` independently authors byte-pinned source, editable-native, rendered-window, and export evidence views for eleven planted cases. `validate.py` fails closed and emits one typed result per observer (`pass`, `fail`, `insufficient_evidence`, or `invalid_artifact`). `fixture.json` predeclares the frame basis, half-open interval semantics, exact track/component identity, one-frame synchronization tolerance, source→native→render→export lineage, permitted split-sequence invariance, and preservation/forbidden-change predicates.

The replay distinguishes exact and tolerance-boundary passes; timing, track, component, and preservation failures; absent source/native/render evidence; plausible output with non-editable native state; export declarations that disagree with bytes; and a legitimate split sequence with equivalent consequences. Render evidence is not inferred from native evidence: the two views are independently authored, separately hashed, and separately observed.

## Evidence and adaptation boundary

- **Paper evidence:** CutVerse records synchronized screen/event demonstrations and grades selected GUI milestones (paper Sections 3.2–3.4, pp. 5–8; examples pp. 25–26). The review documents that these views do not establish native project structure, temporal behavior, export bytes, or editability: `papers/agent-benchmarks/2026-07-15-cutverse-temporal-creative-artifact-validity.md`, especially lines 78–101, 201–222, and 299–307.
- **Release evidence:** `data/sources/releases/2605.19484v1-cutverse/provenance.json` pins a post-v1 official harness snapshot. It is used only for version-boundary provenance and does not establish the paper's benchmark or results.
- **Project adaptation:** the synthetic timeline, one-frame tolerance, observer outcomes, planted cases, and split-sequence equivalence are builder-authored calibration machinery. They are not CutVerse data or reported empirical findings.

No existing schema required modification. The package composes the repository's existing artifact-view, transition, evidence sufficiency, invariance, and hash-lineage concepts in a temporal fixture.

## Reproduce

```bash
python pilots/artifact-transition-conformance/v0.2-temporal/generate_fixture.py
python pilots/artifact-transition-conformance/v0.2-temporal/validate.py \
  pilots/artifact-transition-conformance/v0.2-temporal/fixture.json \
  --report pilots/artifact-transition-conformance/v0.2-temporal/replay-report.json
python -m unittest tests.test_temporal_artifact_conformance
```

The fixture provides no creative or professional quality, expert validity, model capability, reliability, production fitness, or readiness evidence.
