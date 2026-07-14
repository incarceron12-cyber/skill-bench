# Interaction evidence conformance slice

## Scope and charter fit

This zero-call internal calibration advances charter objectives **B** (expertise-to-evaluation methodology) and **C** (executable infrastructure). It tests the general cross-domain hypothesis that an interaction observer can keep **opportunity, exercise, receipt, authority, semantic uptake or justified rejection, state-preserving repair, endpoint effect, and burden** separate. It does not define a desktop or human-agent benchmark.

The concrete artifact is a frozen 12-case matrix over two unlike retained knowledge-work shapes:

- an evidence-backed decision memo with retained uncertainty and appendix identity; and
- a stateful workspace repair with protected audit and unrelated customer state.

Each shape includes `full_information`, `no_channel`, `scripted`, and `simulator` conditions. The cases plant unavailable, unexercised, ignored, justified-rejection, adopted-but-ineffective, beneficial, harmful/collateral-damage, and invalid-environment outcomes. The observer retains invalid episodes and reports different denominators for environment validity, opportunity, exercise, uptake, matched effect evidence, and burden.

## Evidence and rationale

The fixture records hashes for the full local reviews, immutable PDFs, and DeskCraft release provenance.

- `papers/agent-benchmarks/2026-07-14-deskcraft-interactive-workflow-validity.md`, especially its interaction chain and design rules (review lines 171–201 and 271–282; paper pp. 6–12), motivates typed triggers, receipt/adoption separation, matched conditions, transition preservation, endpoint effect, and burden.
- `papers/agent-benchmarks/2026-07-13-hasbench-configurable-human-participation-validity.md`, especially review lines 102–115 and 161–172 (paper pp. 4–6), motivates participant realization, scoped authority, availability/exercise/uptake/effect separation, and plural burden.

The implementation reuses these repository concepts rather than adding a desktop-specific schema. `scripts/validate_interaction_evidence.py` is a domain-neutral observer over prospective frozen records. It does not inspect task semantics or infer adoption from endpoint success.

## Oracle firewall and claim boundary

`private/oracle.json` is hash-pinned but explicitly excluded from the observer's evaluator inputs. The replay classifies each episode first, then uses the oracle only to test conformance. All testimony, participants, states, traces, and outcomes are builder-authored synthetic records. `scripted_policy` and `model_simulator` realizations may not be labeled as humans.

This slice provides **no evidence** of human collaboration, causal interaction benefit, professional validity, agent capability, safety, production fitness, or readiness. The two “beneficial” labels mean only that the deterministic observer recognized a planted frozen synthetic treatment/control relation; they are not empirical effect estimates.

## Files

- `episodes.json` — frozen public requirements, condition vectors, state/message/receipt hashes, authority, trigger, transition, endpoint, burden, environment, and provenance records.
- `private/oracle.json` — expected conformance outcomes, unavailable to the observer during classification.
- `build_fixture.py` — deterministic authoring script; no model, network, or human calls.
- `../../scripts/validate_interaction_evidence.py` — observer, semantic validator, denominator report, and replay CLI.
- `replay-report.json` — retained execution result.
- `../../tests/test_interaction_evidence_conformance.py` — base checks and required mutations for trigger drift, authority mismatch, message/receipt hash mismatch, endpoint-only adoption inference, state-damage omission, and simulator-to-human promotion.

## Reproduce

```bash
python pilots/interaction-evidence-conformance/build_fixture.py
python scripts/validate_interaction_evidence.py --check-paths \
  --report pilots/interaction-evidence-conformance/replay-report.json
python -m unittest tests.test_interaction_evidence_conformance -v
```

Useful completion is exact replay of all planted categories, complete provenance/hash checks, rejection of every required mutation, and separate denominators without claim promotion.
