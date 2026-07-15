"""Two local adapters for a frozen RFC-derived conditional-resource API.

ReferenceAdapter implements the declared RFC-derived contract. SyntheticAdapter
is a deliberately simplified benchmark world with planted transport defects.
Neither adapter calls or claims equivalence to a production service.
"""
from __future__ import annotations

import copy
import hashlib
import json
from typing import Any


def digest(resource: dict[str, Any], revision: int) -> str:
    raw = json.dumps({"resource": resource, "revision": revision}, sort_keys=True, separators=(",", ":"))
    return '"' + hashlib.sha256(raw.encode()).hexdigest()[:16] + '"'


def initial_state(spec: dict[str, Any]) -> dict[str, Any]:
    state = copy.deepcopy(spec)
    state["etag"] = digest(state["resource"], state["revision"])
    return state


def _valid(payload: Any, partial: bool = False) -> bool:
    if not isinstance(payload, dict) or not payload:
        return False
    allowed = {"title", "status", "owner"}
    if set(payload) - allowed:
        return False
    if not partial and set(payload) != allowed:
        return False
    if "title" in payload and (not isinstance(payload["title"], str) or not payload["title"].strip()):
        return False
    if "status" in payload and payload["status"] not in {"draft", "approved", "archived"}:
        return False
    if "owner" in payload and (not isinstance(payload["owner"], str) or not payload["owner"].strip()):
        return False
    return True


class BaseAdapter:
    name = "base"

    def __init__(self, state_spec: dict[str, Any]):
        self.state = initial_state(state_spec)

    def snapshot(self) -> dict[str, Any]:
        return copy.deepcopy(self.state)

    def _resolve(self, value: Any, initial_etag: str) -> Any:
        if value == "$INITIAL_ETAG":
            return initial_etag
        if value == "$CURRENT_ETAG":
            return self.state["etag"]
        return value

    def execute(self, action: dict[str, Any], initial_etag: str) -> dict[str, Any]:
        raise NotImplementedError

    def _mutate(self, payload: dict[str, Any], method: str) -> None:
        if method == "PUT":
            self.state["resource"] = copy.deepcopy(payload)
        else:
            self.state["resource"].update(copy.deepcopy(payload))
        self.state["revision"] += 1
        self.state["audit"].append({"method": method, "revision": self.state["revision"]})
        self.state["etag"] = digest(self.state["resource"], self.state["revision"])


class ReferenceAdapter(BaseAdapter):
    """Executable oracle for the declared local interpretation of the RFCs."""

    name = "reference-rfc-derived"

    def execute(self, action: dict[str, Any], initial_etag: str) -> dict[str, Any]:
        method = action["method"]
        if method == "GET":
            tag = self._resolve(action.get("if_none_match"), initial_etag)
            if tag == self.state["etag"]:
                return {"status": 304, "body": None, "etag": self.state["etag"]}
            return {"status": 200, "body": copy.deepcopy(self.state["resource"]), "etag": self.state["etag"]}

        if action.get("token") != "writer-token":
            return {"status": 401, "body": {"error": "invalid_token"}}
        payload = action.get("payload")
        if not _valid(payload, partial=method == "PATCH"):
            return {"status": 400, "body": {"error": "invalid_payload"}}
        assert isinstance(payload, dict)
        match = self._resolve(action.get("if_match"), initial_etag)
        if match is not None and match != self.state["etag"]:
            return {"status": 412, "body": {"error": "precondition_failed"}, "etag": self.state["etag"]}

        # Repeating an identical replacement has no additional requested
        # resource effect in this local idempotent-reference interpretation.
        if method == "PUT" and payload == self.state["resource"]:
            return {"status": 200, "body": copy.deepcopy(self.state["resource"]), "etag": self.state["etag"]}
        self._mutate(payload, method)
        return {"status": 200, "body": copy.deepcopy(self.state["resource"]), "etag": self.state["etag"]}


class SyntheticAdapter(BaseAdapter):
    """Planted simplified world: validates shape but omits key transport semantics."""

    name = "synthetic-simplified"

    def execute(self, action: dict[str, Any], initial_etag: str) -> dict[str, Any]:
        method = action["method"]
        if method == "GET":
            # Planted defect: conditional request is ignored.
            return {"status": 200, "body": copy.deepcopy(self.state["resource"]), "etag": self.state["etag"]}
        payload = action.get("payload")
        if not _valid(payload, partial=method == "PATCH"):
            return {"status": 400, "body": {"error": "invalid_payload"}}
        assert isinstance(payload, dict)
        # Planted defects: no authorization or If-Match enforcement and every
        # accepted replacement emits a revision/audit side effect.
        self._mutate(payload, method)
        return {"status": 200, "body": copy.deepcopy(self.state["resource"]), "etag": self.state["etag"]}
