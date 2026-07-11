# Bounded revision request

Revise `workspace/original-incident-brief.md` and write the complete revised artifact to `outputs/revised-incident-brief.md`.

## Required change (exactly one must-change predicate)

Add this exact provenance line once under **Evidence used**:

`- Authoritative status source: workspace/current/signed-status.json (INC-204).`

This public requirement is grounded by the copied brief's existing INC-204 evidence statement and the supplied signed-status source.

## Preservation envelope

- Preserve every existing nonblank line exactly, including ordering, except for inserting the required line.
- Do not delete, paraphrase, reorder, or duplicate existing content.
- Do not add any other content.
- Forbidden changes include altered incident facts, recommendations, safety limits, source assessments, and benchmark disclaimer.
- Permitted normalization: one trailing newline only.

If any required input is unreadable or contradictory, do not guess; write `outputs/invalid-environment.txt` with the reason and do not create the revised artifact.
