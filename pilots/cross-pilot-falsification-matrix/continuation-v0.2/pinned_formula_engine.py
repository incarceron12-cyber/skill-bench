#!/usr/bin/env python3
"""Pinned, deliberately tiny calculator for the v0.2 recalculation conformance case."""
from __future__ import annotations

ENGINE_ID = "skill-bench-json-formula-engine"
ENGINE_VERSION = "0.1.0"
SUPPORTED_EXPRESSION = "units * unit_price"


def calculate(expression: str, inputs: dict[str, int | float]) -> int | float:
    """Evaluate the one predeclared expression without eval or dynamic code."""
    if expression != SUPPORTED_EXPRESSION:
        raise ValueError(f"unsupported expression: {expression}")
    units = inputs.get("units")
    unit_price = inputs.get("unit_price")
    if isinstance(units, bool) or not isinstance(units, (int, float)):
        raise ValueError("units must be numeric")
    if isinstance(unit_price, bool) or not isinstance(unit_price, (int, float)):
        raise ValueError("unit_price must be numeric")
    return units * unit_price
