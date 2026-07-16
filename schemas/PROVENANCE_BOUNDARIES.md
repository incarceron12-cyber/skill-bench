# Frozen evidence and live canonical dependencies

`validate_provenance_boundary.py` implements a narrow boundary for historical
benchmark artifacts that cite a canonical design document which legitimately
continues to evolve.

A record contains two independently checked identities:

1. **Historical snapshot** — repository-relative path, Git commit, Git blob, and
   SHA-256. The validator reads the object from Git, verifies all three identities,
   and checks that each required semantic anchor existed at that commit.
2. **Live canonical dependency** — the same exact path, an expected semantic role,
   and explicit text anchors. The live file need not retain the historical byte
   hash, but it must exist and preserve every cited semantic anchor.

Callers supply the expected path and semantic role rather than trusting those
values from the record. This makes path substitution and silent role changes
validation failures. Missing commits, blobs, snapshots, or anchors also fail
closed.

The exception is deliberately unavailable to immutable task, source-pack,
grader, launcher, runtime, trial-output, and report artifacts. In a legacy frozen
component list, `validate_frozen_component_set` applies the historical/live rule
to exactly one declared canonical document and continues to verify every other
component against its current byte hash.

Current bounded applications:

- `pilots/dynamic-criterion-conformance/provenance-boundary.json`
- `pilots/delayed-obligation-heldout-v2/provenance-boundary.json`

These records repair replayability, not validity. They do not change either
pilot's cases, obligations, expected outcomes, grading behavior, retained reports,
or claim ceilings.
