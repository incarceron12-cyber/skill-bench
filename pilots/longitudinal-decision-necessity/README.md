# Longitudinal decision-necessity conformance slice

This is a **zero-call, internally authored synthetic calibration fixture**. It tests a general benchmark-design obligation, not vendor-risk or research-publication competence:

> Prior evidence supports a longitudinal-decision claim only when a prospective intervention on that evidence changes the justified action set while immediate state remains fixed.

## Evidence and rationale

The slice implements the four-way distinction in the full LongMedBench review (`papers/agent-benchmarks/2026-07-14-longmedbench-longitudinal-clinical-validity.md`, especially lines 133–148 and 181–209): history volume, access, necessity, and consequence validity are separate. It also implements MemoryArena's evidence-to-action warning (`papers/agent-benchmarks/2026-07-13-memoryarena-interdependent-experience-action.md`, lines 61–69 and 114–134): authored dependence does not establish visibility, adoption, or causal use.

The fixture therefore freezes two distinct knowledge-work shapes before observation and crosses each with `correct`, `absent`, `irrelevant`, `stale`, and `contradictory` history. Every evidence atom preserves event, record, availability, and valid time; authority; relevance; and transformation lineage. Each condition records availability → visibility → adoption, a plural admissible action set (including ask, abstain, escalate, and an alternative valid procedure), observer coverage, and an explicitly non-professional synthetic consequence oracle.

Recorded next behavior is retained only as a behavioral witness and is forbidden from inheriting normative appropriateness. Chronology permits multiple acceptable sequences rather than claiming a unique order unsupported by visible evidence. Missing and invalid observations remain in the ten-cell frozen denominator and cannot silently become failures or disappear.

Existing benchmark-bundle, longitudinal, validity, metric, experience-memory, and context-compression contracts are referenced rather than duplicated. The small validator is an exercised conformance interface for obligations not jointly represented by one existing fixture; it is not a new general schema.

## Run

```bash
python scripts/validate_longitudinal_decision_necessity.py \
  pilots/longitudinal-decision-necessity/conformance.json \
  --check-paths \
  --report pilots/longitudinal-decision-necessity/replay-report.json
python -m unittest tests.test_longitudinal_decision_necessity
```

The replay report may support only claims about this exact deterministic fixture. It does **not** establish agent capability, memory improvement, professional or clinical validity, safety, production fitness, readiness, population prevalence, or cross-domain generality.
