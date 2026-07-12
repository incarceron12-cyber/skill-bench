#!/usr/bin/env python3
"""Fail-closed semantic validation for versioned evaluator observation inputs."""
from __future__ import annotations
import hashlib, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[1]
SCHEMA = ROOT / "observation-input-contract.schema.json"
FORBIDDEN_KEYS = {"oracle", "expected", "expected_outcome", "case_id", "family_id", "source_family"}
FORBIDDEN_DOMAIN_TOKENS = (
    "inc-204", "invoice-export", "sev-2", "lh-adoption", "ops-handoff",
    "vendor-incident", "multilingual-edge", "experience-memory",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pointer_get(value, pointer: str):
    current = value
    for token in pointer.lstrip("/").split("/"):
        token = token.replace("~1", "/").replace("~0", "~")
        current = current[int(token)] if isinstance(current, list) else current[token]
    return current


def walk(value, errors: list[str], location: str = "$") -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            if key.lower() in FORBIDDEN_KEYS:
                errors.append(f"{location}: forbidden leakage key {key!r}")
            walk(child, errors, f"{location}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            walk(child, errors, f"{location}[{index}]")
    elif isinstance(value, str):
        lowered = value.lower()
        for token in FORBIDDEN_DOMAIN_TOKENS:
            if re.search(rf"(?<![a-z0-9]){re.escape(token)}(?![a-z0-9])", lowered):
                errors.append(f"{location}: forbidden domain token {token!r}")


def validate(contract: dict, *, check_paths: bool = True) -> list[str]:
    errors: list[str] = []
    try:
        import jsonschema
        jsonschema.Draft202012Validator(json.loads(SCHEMA.read_text())).validate(contract)
    except ImportError:
        errors.append("jsonschema dependency unavailable")
    except Exception as exc:
        errors.append(f"schema: {exc}")
    walk(contract, errors)
    ids = [row.get("observation_id") for row in contract.get("observations", [])]
    if len(ids) != len(set(ids)):
        errors.append("observation_id values must be unique")
    if check_paths:
        locators = [contract.get("qualification_policy", {}), contract.get("criterion_basis", {})]
        for row in contract.get("observations", []):
            locators.append(row.get("legacy_locator", {})); locators.extend(row.get("public_basis", []))
            for comparison in row.get("comparisons", []):
                locators.extend((comparison.get("observed_locator", {}), comparison.get("source_locator", {})))
        cache: dict[str, object] = {}
        for locator in locators:
            rel = locator.get("path")
            if not rel: continue
            path = REPO / rel
            if not path.is_file():
                errors.append(f"missing path: {rel}"); continue
            if sha256(path) != locator.get("sha256"):
                errors.append(f"hash mismatch: {rel}"); continue
            if "json_pointer" in locator:
                try:
                    data = cache.setdefault(rel, json.loads(path.read_text()))
                    pointer_get(data, locator["json_pointer"])
                except Exception as exc:
                    errors.append(f"invalid locator {rel}{locator['json_pointer']}: {exc}")
    return sorted(set(errors))


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_observation_input_contract.py CONTRACT.json", file=sys.stderr); return 2
    contract = json.loads(Path(sys.argv[1]).read_text())
    errors = validate(contract)
    print(json.dumps({"valid": not errors, "errors": errors}, indent=2))
    return 0 if not errors else 1

if __name__ == "__main__":
    raise SystemExit(main())
