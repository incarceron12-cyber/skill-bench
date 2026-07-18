# Release graph R

## Objective
Construct a safe publication set from the item graph while retaining source-to-output lineage.

## Inputs
| Item | Release label | Marked segments | Mandatory dependencies |
|---|---|---|---|
| K7 | direct | none | none |
| K8 | transform | `account` and `email` | K7 |
| K9 | direct | none | K8 |
| K10 | transform | `location` | K12 |
| K11 | direct | none | K10 |
| K12 | unlabeled | none | none |

For a `transform` item, remove all named segments and give the transformed output a new identity formed by appending `-public`.

## Deliverable
Write `publication.md` listing released identities and a complete manifest with source identity, released identity or null, disposition, transformation, dependency state, and reason for every source item.

## Fair consequence basis
An item's own label governs its initial eligibility, and every required transformation must remove all marked segments. Release also requires every mandatory dependency to be released. Failed dependencies propagate withholding to dependent items. Every source item appears exactly once in the manifest.
