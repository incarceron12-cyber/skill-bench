# Correction semantic-delta and realization conformance slice

This non-releasable package is a deterministic, builder-authored contract calibration. It tests a general cross-domain hypothesis: **an admitted correction, a faithful context rewrite, successful retrieval, generator exposure, semantic adoption, independent correctness, and a useful consequence are different evidence states.** It is not a RAG, tax, support, procurement, or access-control benchmark.

## Vertical slice

`conformance.json` freezes two unlike synthetic correction families:

1. role-scoped workspace password-reset policy; and
2. time-bounded procurement approval policy.

The package records correction authority and evidence locators, atomic canonical propositions, rewritten representations, adaptation probes, untouched equivalent forms, unrelated collision queries, independent correctness, collateral effects, and rollback. Planted representations cover:

- faithful rewrite;
- unsupported proposition addition;
- scope widening;
- valid-time widening;
- stale/conflicting lower authority; and
- a highly discoverable but wrong object.

Convergence is predeclared as **all required adaptation probes**, not “any probe.” Adaptation probes cannot serve as untouched confirmation. The replay preserves this chain:

```text
admitted correction
→ proposition delta
→ indexed representation
→ retrieval
→ generator exposure
→ semantic adoption
→ independent correctness
→ collateral effect / rollback
```

The discoverable-wrong procurement object intentionally reaches retrieval, exposure, and adoption, while failing authority precedence, independent correctness, collision, and promotion gates. This demonstrates contract behavior only; it is not evidence that the failure is prevalent or that the controls improve an agent.

## Design rationale and provenance

The package converts two completed full-source reviews into executable checks:

- `papers/agent-benchmarks/2026-07-18-openai-tax-ai-correction-eval-loop-validity.md`, especially the correction-attribution-before-promotion result and lines 204–234 / 339–347;
- `papers/agent-benchmarks/2026-07-18-factual-nugget-optimization-correction-validity.md`, especially the correction→realization chain, any/all ambiguity, unsupported worked-example propositions, and lines 148–163 / 223–274.

The reviews support the design distinction, not the synthetic outcomes. OpenAI/Thrive releases no correction rows or trials. INO releases no empirical code, data, nuggets, or traces. Every `synthetic://` locator is an explicit fixture locator, not testimony or external evidence.

The slice reuses `schemas/compounding-lessons.schema.json` for the candidate→validation→promotion→rollback lifecycle and `pilots/experience-memory-transfer/conformance.json` for available→accessed→adopted→consequence separation. The existing contracts represented the lifecycle; the missing artifact was an executable proposition-delta and index-time realization conformance package. No existing schema was changed.

## Replay and tests

```bash
python scripts/validate_correction_realization.py --check-paths \
  --report pilots/correction-realization/replay-report.json \
  pilots/correction-realization/conformance.json
python -m unittest tests.test_correction_realization -v
```

Mutation tests reject missing locators, unsupported additions, scope/modality/time drift, authority-precedence inversion, any-versus-all convergence ambiguity, incomplete required-probe convergence, same-loop correctness promotion, and retrieval-only readiness claims.

## Claim boundary

Licensed claims are limited to exact deterministic fixture conformance. The package licenses **no** empirical effect, expert validity, agent capability, professional utility, safety, transport, cross-domain generality, or deployment readiness claim. It uses no model calls and incurs no cost.
