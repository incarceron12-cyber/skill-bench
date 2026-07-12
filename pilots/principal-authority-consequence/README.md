# Principal authority → consequence conformance slice

This prospective pilot freezes two structurally different delegated knowledge-work scenarios before grader implementation: an irreversible procurement commitment and an irreversible information disclosure. Each crosses four matched authority/visibility states: agent-visible authorization, principal authorization withheld from the agent, evaluator-only preference, and explicit no-authority.

## Charter/design rationale

This is a bounded cross-domain building/validation slice for charter objectives B and C. It tests the general hypothesis that a grader must not convert private intent into public authorization. The reusable artifact is an executable mandate-to-consequence crosswalk and mutation suite—not a procurement, privacy, or negotiation benchmark. Source rationale and immutable review hashes are in `cases.json`; the relevant evidence is the authorization-state distinction in the UnderSpecBench review, dependency-bearing action chain in MemoryArena, and principal-specific mandate/visibility distinction in SovereignNegotiation-Bench.

Every case declares the exact mandate basis and locator, visibility principals, allowed alternatives, reversibility, expected action, and consequence. `replay.py` uses a separate rule oracle and reports authorization, information-sufficiency, action, and consequence errors independently. It fails closed on missing/mismatched sources, locators, visibility, authority scope, or consequence evidence.

## Run

```bash
python pilots/principal-authority-consequence/replay.py
python -m unittest tests.test_principal_authority_consequence
```

The generated `report.json` is internal calibration evidence only. It can license exact behavior on these frozen cases, not real-user consent/benefit, expert or professional validity, general evaluator validity, agent capability, production fitness, privacy/compliance validity, or readiness.
