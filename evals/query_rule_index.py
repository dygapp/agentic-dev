#!/usr/bin/env python3
"""查询 B3 派生规则索引，不创建第二规则权威。

退出码：
- 0：查询或验证完成，且不需要回退
- 2：索引来源陈旧 / 缺失，或查询包含未知 / 未提供的必要维度，需要回退
- 64：索引或查询输入无效
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INDEX = ROOT / "evals" / "rule-retrieval" / "rule-index.json"
REQUIRED_ENTRY_FIELDS = {
    "entry_key",
    "role",
    "source",
    "scope",
    "responsibilities",
    "stages",
    "subjects",
    "conditions",
    "strength",
    "activation_summary",
    "required_checks",
    "relations",
}


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode("utf-8")
    return hashlib.sha1(header + data).hexdigest()


def is_string_list(value: Any, *, allow_empty: bool = True) -> bool:
    return (
        isinstance(value, list)
        and (allow_empty or bool(value))
        and all(isinstance(item, str) and item for item in value)
    )


def validate_index(index: Any) -> list[str]:
    if not isinstance(index, dict):
        return ["index root must be an object"]

    entries = index.get("entries")
    if not isinstance(entries, list):
        return ["index.entries must be a list"]

    allowed_roles = set(index.get("allowed_roles", []))
    allowed_strengths = set(index.get("allowed_strengths", []))
    allowed_relations = set(index.get("allowed_relations", []))
    errors: list[str] = []
    keys: set[str] = set()

    for number, entry in enumerate(entries, start=1):
        if not isinstance(entry, dict):
            errors.append(f"entry {number} must be an object")
            continue

        missing = sorted(REQUIRED_ENTRY_FIELDS - set(entry))
        if missing:
            errors.append(f"entry {number} missing fields: {', '.join(missing)}")
            continue

        raw_key = entry["entry_key"]
        if not isinstance(raw_key, str) or not raw_key:
            errors.append(f"entry {number} has invalid entry_key")
            key = f"<entry-{number}>"
        else:
            key = raw_key
            if key in keys:
                errors.append(f"duplicate entry_key: {key}")
            else:
                keys.add(key)

        if entry["role"] not in allowed_roles:
            errors.append(f"{key}: invalid role {entry['role']!r}")
        if entry["strength"] not in allowed_strengths:
            errors.append(f"{key}: invalid strength {entry['strength']!r}")

        source = entry["source"]
        if not isinstance(source, dict):
            errors.append(f"{key}: source must be an object")
        else:
            for field in ("path", "section", "identity"):
                if not isinstance(source.get(field), str) or not source[field]:
                    errors.append(f"{key}: source.{field} must be a non-empty string")

        for field in ("scope", "responsibilities"):
            if not is_string_list(entry[field], allow_empty=False):
                errors.append(f"{key}: {field} must be a non-empty string list")
        for field in ("stages", "subjects", "conditions", "required_checks"):
            if not is_string_list(entry[field]):
                errors.append(f"{key}: {field} must be a string list")

        if not isinstance(entry["relations"], list):
            errors.append(f"{key}: relations must be a list")
        if not isinstance(entry["activation_summary"], str) or not entry["activation_summary"].strip():
            errors.append(f"{key}: activation_summary must be non-empty")

    for entry in entries:
        if not isinstance(entry, dict):
            continue
        key = entry.get("entry_key", "<unknown>")
        relations = entry.get("relations", [])
        if not isinstance(relations, list):
            continue
        for relation in relations:
            if not isinstance(relation, dict):
                errors.append(f"{key}: relation must be an object")
                continue
            rel_type = relation.get("type")
            target = relation.get("target")
            if rel_type not in allowed_relations:
                errors.append(f"{key}: invalid relation type {rel_type!r}")
            if not isinstance(target, str) or target not in keys:
                errors.append(f"{key}: relation target does not exist: {target!r}")

    return errors


def unique_sources(index: dict[str, Any]) -> list[dict[str, str]]:
    seen: dict[tuple[str, str], dict[str, str]] = {}
    for entry in index["entries"]:
        source = entry["source"]
        key = (source["path"], source["identity"])
        seen.setdefault(key, source)
    return sorted(seen.values(), key=lambda item: (item["path"], item["identity"]))


def check_sources(index: dict[str, Any], root: Path) -> list[dict[str, str]]:
    stale: list[dict[str, str]] = []
    for source in unique_sources(index):
        path = root / source["path"]
        if not path.is_file():
            stale.append(
                {
                    "path": source["path"],
                    "expected_identity": source["identity"],
                    "actual_identity": "",
                    "reason": "missing_source",
                }
            )
            continue

        actual = git_blob_sha1(path)
        if actual != source["identity"]:
            stale.append(
                {
                    "path": source["path"],
                    "expected_identity": source["identity"],
                    "actual_identity": actual,
                    "reason": "source_identity_changed",
                }
            )
    return stale


def require_string_list(query: dict[str, Any], field: str) -> list[str]:
    value = query.get(field)
    if not is_string_list(value, allow_empty=False):
        raise ValueError(f"query.{field} must be a non-empty list of strings")
    return value


def optional_string(query: dict[str, Any], field: str) -> tuple[bool, str | None]:
    if field not in query:
        return False, None
    value = query[field]
    if value is not None and (not isinstance(value, str) or not value):
        raise ValueError(f"query.{field} must be a non-empty string or null")
    return True, value


def optional_string_list(query: dict[str, Any], field: str) -> tuple[bool, list[str]]:
    if field not in query:
        return False, []
    value = query[field]
    if not is_string_list(value):
        raise ValueError(f"query.{field} must be a list of strings")
    return True, value


def vocabulary(index: dict[str, Any]) -> dict[str, set[str]]:
    values = {
        "scope": set(),
        "responsibilities": set(),
        "stage": set(),
        "subject": set(),
        "conditions": set(),
    }
    for entry in index["entries"]:
        values["scope"].update(entry["scope"])
        values["responsibilities"].update(
            item for item in entry["responsibilities"] if item != "*"
        )
        values["stage"].update(entry["stages"])
        values["subject"].update(entry["subjects"])
        values["conditions"].update(entry["conditions"])
    return values


def unknown_query_values(
    index: dict[str, Any],
    scopes: set[str],
    responsibilities: set[str],
    stage_known: bool,
    stage: str | None,
    subject_known: bool,
    subject: str | None,
    conditions_known: bool,
    conditions: set[str],
) -> dict[str, list[str]]:
    known = vocabulary(index)
    unknown: dict[str, list[str]] = {}

    checks: list[tuple[str, set[str]]] = [
        ("scope", scopes - known["scope"]),
        ("responsibilities", responsibilities - known["responsibilities"]),
    ]
    if stage_known and stage is not None:
        checks.append(("stage", {stage} - known["stage"]))
    if subject_known and subject is not None:
        checks.append(("subject", {subject} - known["subject"]))
    if conditions_known:
        checks.append(("conditions", conditions - known["conditions"]))

    for field, values in checks:
        if values:
            unknown[field] = sorted(values)
    return unknown


def prefilter(entry: dict[str, Any], scopes: set[str], responsibilities: set[str]) -> bool:
    if not set(entry["scope"]).issubset(scopes):
        return False
    if entry["strength"] == "core-invariant":
        return True
    entry_resp = set(entry["responsibilities"])
    return "*" in entry_resp or bool(entry_resp & responsibilities)


def is_superseded(entry: dict[str, Any]) -> bool:
    return any(rel.get("type") == "superseded-by" for rel in entry["relations"])


def build_result(entry: dict[str, Any], matched_by: list[str]) -> dict[str, Any]:
    source = entry["source"]
    return {
        "entry_key": entry["entry_key"],
        "source_pointer": {
            "path": source["path"],
            "section": source["section"],
            "identity": source["identity"],
        },
        "activation_summary": entry["activation_summary"],
        "applicability": {
            "role": entry["role"],
            "strength": entry["strength"],
            "scope": entry["scope"],
            "responsibilities": entry["responsibilities"],
            "stages": entry["stages"],
            "subjects": entry["subjects"],
            "conditions": entry["conditions"],
        },
        "required_checks": entry["required_checks"],
        "matched_by": matched_by,
        "relations": entry["relations"],
    }


def query_index(index: dict[str, Any], query: dict[str, Any]) -> tuple[dict[str, Any], int]:
    scopes = set(require_string_list(query, "scope"))
    responsibilities = set(require_string_list(query, "responsibilities"))
    stage_known, stage = optional_string(query, "stage")
    subject_known, subject = optional_string(query, "subject")
    conditions_known, conditions_list = optional_string_list(query, "conditions")
    conditions = set(conditions_list)

    unknown = unknown_query_values(
        index,
        scopes,
        responsibilities,
        stage_known,
        stage,
        subject_known,
        subject,
        conditions_known,
        conditions,
    )
    if unknown:
        return (
            {
                "fallback_required": True,
                "fallback_reason": "query_values_not_modeled",
                "unknown_query_values": unknown,
                "query": query,
                "results": [],
                "metrics": {"indexed_entries": len(index["entries"]), "result_count": 0},
            },
            2,
        )

    results: list[dict[str, Any]] = []
    unresolved: list[dict[str, str]] = []

    for entry in index["entries"]:
        if not prefilter(entry, scopes, responsibilities) or is_superseded(entry):
            continue

        matched_by = ["scope"]
        if entry["strength"] == "core-invariant":
            matched_by.append("core-invariant")
        else:
            matched_by.append("responsibility")

        # 先使用已经明确提供的维度排除不适用条目；只有仍可能适用的
        # 条目缺少必要维度时才要求回退，避免已知不匹配项制造假回退。
        if entry["stages"] and stage_known:
            if stage is None or stage not in entry["stages"]:
                continue
            matched_by.append("stage")
        if entry["subjects"] and subject_known:
            if subject is None or subject not in entry["subjects"]:
                continue
            matched_by.append("subject")
        if entry["conditions"] and conditions_known:
            if not (set(entry["conditions"]) & conditions):
                continue
            matched_by.append("conditions")

        unknown_dimensions: list[str] = []
        if entry["stages"] and not stage_known:
            unknown_dimensions.append("stage")
        if entry["subjects"] and not subject_known:
            unknown_dimensions.append("subject")
        if entry["conditions"] and not conditions_known:
            unknown_dimensions.append("conditions")

        if unknown_dimensions:
            unresolved.append(
                {
                    "entry_key": entry["entry_key"],
                    "reason": "unknown_query_dimensions",
                    "dimensions": ",".join(unknown_dimensions),
                }
            )
            continue

        results.append(build_result(entry, matched_by))

    fallback_required = bool(unresolved)
    payload = {
        "fallback_required": fallback_required,
        "fallback_reason": "query_dimensions_unknown" if fallback_required else None,
        "unresolved_candidates": unresolved,
        "query": query,
        "results": results,
        "metrics": {
            "indexed_entries": len(index["entries"]),
            "result_count": len(results),
            "authority_results": sum(
                item["applicability"]["role"] == "authority" for item in results
            ),
            "pointer_results": sum(
                item["applicability"]["role"] == "pointer" for item in results
            ),
            "consumer_results": sum(
                item["applicability"]["role"] == "consumer" for item in results
            ),
        },
    }
    return payload, 2 if fallback_required else 0


def emit(payload: dict[str, Any]) -> None:
    json.dump(payload, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX)
    parser.add_argument("--query", type=Path, help="查询 JSON 路径；使用 '-' 从 stdin 读取")
    parser.add_argument("--validate-index", action="store_true")
    parser.add_argument("--check-sources", action="store_true")
    args = parser.parse_args()

    try:
        index = load_json(args.index)
    except (OSError, json.JSONDecodeError) as exc:
        emit({"error": "invalid_index_input", "detail": str(exc)})
        return 64

    errors = validate_index(index)
    if errors:
        emit({"error": "invalid_index", "details": errors})
        return 64

    if args.validate_index and not args.query and not args.check_sources:
        emit(
            {
                "valid": True,
                "entries": len(index["entries"]),
                "sources": len(unique_sources(index)),
            }
        )
        return 0

    # 在筛选前校验首轮原型覆盖的所有活动规范性来源，防止旧索引
    # 因为没有先命中新规则而静默漏召回。
    stale = check_sources(index, ROOT)
    if stale:
        emit(
            {
                "fallback_required": True,
                "fallback_reason": "indexed_source_stale_or_missing",
                "stale_sources": stale,
                "results": [],
            }
        )
        return 2

    if args.check_sources and not args.query:
        emit(
            {
                "valid": True,
                "sources_current": True,
                "sources": len(unique_sources(index)),
            }
        )
        return 0

    if args.query is None:
        emit(
            {
                "error": "missing_query",
                "detail": "provide --query, --validate-index, or --check-sources",
            }
        )
        return 64

    try:
        if str(args.query) == "-":
            query = json.load(sys.stdin)
        else:
            query = load_json(args.query)
        if not isinstance(query, dict):
            raise ValueError("query root must be an object")
        payload, code = query_index(index, query)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        emit({"error": "invalid_query", "detail": str(exc)})
        return 64

    emit(payload)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
