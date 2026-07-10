# Artifact transition conformance slice

This internal synthetic package operationalizes the DELEGATE-52 review's general hypothesis: requested-delta correctness and preservation-envelope integrity are independent, while round-trip recovery is only a metamorphic observation. It is cross-domain machinery, not a document-editing benchmark.

`validate.py` deterministically replays six planted cases from `conformance.json`: a forward no-op with perfect recovery, an authorized edit plus unauthorized accounting-style addition, permitted normalization, a preserved initial defect, invalid parse, and failed inverse. It fails closed on undeclared invariances, predicate-coverage drift, stale initial identity, and any expected outcome that does not follow from the typed predicates.

The fixture is builder-authored calibration only. It provides no expert validity, agent capability, professional quality, prevalence, or readiness evidence. Design evidence and immutable release identity are recorded in the fixture's provenance block.

Run: `python pilots/artifact-transition-conformance/validate.py pilots/artifact-transition-conformance/conformance.json --report pilots/artifact-transition-conformance/replay-report.json`.
