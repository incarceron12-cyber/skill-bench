# Dependency topology versus endpoint closure — conformance slice

This package is an **inert, builder-authored internal contract calibration**. It extends the generic cross-resource observation envelope; it is not a device schema and runs no agent, database, service, or network operation.

## Charter decision filter

- **Objective:** charter B/C — turn a reusable expertise-to-evaluation boundary into executable benchmark machinery.
- **Artifact/evidence:** two schema-valid matched forms, four retained planted cases, semantic replay, and mutation/backward-compatibility tests.
- **Uncertainty clarified:** whether dependency-edge fidelity, endpoint closure, prerequisite masking, persistence, collateral state, and cleanup can remain distinct.
- **Mode:** building and validation.
- **Duplication/scope check:** extends `schemas/resource-observation-envelope.schema.json`; it neither replaces benchmark-bundle checks nor narrows the project to device automation.
- **Useful completion:** mutations cannot launder a wrong path into edge success, a masked stage into an observed failure, acknowledgement into persistence, or endpoint success into collateral/reset success.

## Matched design

`package.json` freezes six local operations, five check families, horizon 12, and budget 12. Its two forms vary only the declared topology treatment (`direct_authorized_transfer` versus `role_rebound_transfer`). Each form freezes endpoint role/authority/valid interval, claim identity and source locator, permitted transformation/invariances, typed dependency edges, and downstream checks.

The four retained cases prove exact validator behavior:

1. endpoint/global closure pass while the required path is unauthorized;
2. failed source access censors downstream transformation, target, endpoint, and closure opportunities;
3. write acknowledgement without authoritative re-observation fails persistence;
4. endpoint/global closure pass while prohibited collateral state and cleanup residue fail separately.

## Evidence and rationale

| Element | DevicesWorld review locator | Status |
|---|---|---|
| edge-and-endpoint chain | `Unique insight`, lines 95–105 | Source-grounded boundary; JSON representation is project-authored |
| stable semantic endpoint roles | lines 101–103; transfer item 1, lines 152–155 | Cross-domain adaptation |
| claim/value, source, transformation, invariance, authorization, downstream checks | transfer item 2, lines 154–156 | Source-grounded fields; synthetic values are calibration only |
| access/capture/transformation/write/persistence stages | transfer item 3, lines 156–157 | Source-grounded stage split |
| separate edge, endpoint, global, collateral, cleanup families | transfer item 4, lines 157–158 | Source-grounded measurement split |
| prerequisite censoring | limitation 27, lines 134–136; transfer item 5, lines 158–159 | Source-grounded masking rule |
| matched topology forms | lines 103–105; transfer item 6, lines 159–160 | Source-grounded design requirement |
| post-write re-observation | lines 87–90; transfer item 7, lines 160–161 | Source-grounded attempt/persistence split |
| collateral and reset checks | limitations 21–23, lines 128–131; transfer items 8–9, lines 161–163 | Source-grounded separate outcomes |

All endpoints, values, locators, transformations, evidence strings, and outcomes are synthetic. The fixture licenses only the exact claim that the current validator detects these four planted contrasts. It does **not** establish coordination capability, professional validity, safety, reliability, production fitness, or readiness.

## Run

```bash
python pilots/cross-resource-observation-envelope/dependency-topology-v1/replay.py
python -m unittest tests.test_dependency_topology_conformance -v
```
