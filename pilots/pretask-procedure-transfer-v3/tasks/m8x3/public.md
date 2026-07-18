# Release graph M

## Objective
Determine the releasable item set and preserve a complete lineage record for all supplied source items.

## Inputs
| Item | Release label | Marked segments | Mandatory dependencies |
|---|---|---|---|
| N1 | direct | none | none |
| N2 | transform | `phone` | N1 |
| N3 | direct | none | N2 |
| N4 | withhold | none | none |
| N5 | direct | none | N4 |
| N6 | unlabeled | none | none |

For a `transform` item, remove every marked segment and assign a new released identity by appending `-clean` to the source identity.

## Deliverable
Write `release.md` with the final released identities and one manifest row per source item containing source identity, released identity or null, disposition, transformation, dependency state, and reason.

## Fair consequence basis
Apply each item's own release label and the stated transformation before deciding release. A mandatory dependency must itself be released; otherwise the dependent item is withheld and the reason must identify the failed dependency. Do not omit or duplicate source items in the manifest.
