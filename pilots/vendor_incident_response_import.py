"""Test-only import helper for pilot scripts stored under hyphenated directories."""
from __future__ import annotations

import importlib.util
from pathlib import Path
from types import ModuleType


def load_grader(path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location("vendor_incident_grader", path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot import grader from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
