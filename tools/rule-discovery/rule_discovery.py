#!/usr/bin/env python3
"""V4 deterministic Rule Discovery and repository metadata lint.

This tool deliberately supports only the frozen agentic-dev Front Matter subset:
- top-level scalar fields;
- one-level nested mappings;
- inline arrays of scalar strings.

The subset is valid YAML, but unsupported YAML constructs fail closed instead of being
silently interpreted. Rule normative bodies are never read for candidate matching.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import sys
from dataclasses import dataclass
from typing import Any, Iterable, Sequence

SCOPE_KEYS = ("phases", "activities", "technologies", "artifacts", "risks")
RULE_KEYS = {"id", "type", "status", "scope"}
COMMON_TYPES = {
    "method",
    "architecture",
    "rule",
    "guide",
    "research",
    "project",
    "repository",
    "eval-guide",
}
MAX_TASK_TOKENS_PER_DIMENSION = 6
TOKEN_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
RESOURCE_ID_RE = re.compile(r"^[a-z0-9]+(?::[a-z0-9]+(?:-[a-z0-9]+)*)+$")
RULE_ID_RE = re.compile(r"^rule:[a-z0-9]+(?:-[a-z0-9]+)*$")


class ContractError(ValueError):
    pass


@dataclass(frozen=True)
class ParsedMarkdown:
    metadata: dict[str, Any]
    body: str


@dataclass(frozen=True)
class RuleRecord:
    id: str
    path: Path
    locator: str
    scope: dict[str, tuple[str, ...]]


def _parse_scalar(raw: str, *, source: str, line_no: int) -> Any:
    value = raw.strip()
    if value == "":
        raise ContractError(f"{source}:{line_no}: empty scalar value")

    if value.startswith("["):
        if not value.endswith("]"):
            raise ContractError(f"{source}:{line_no}: malformed inline array")
        inner = value[1:-1].strip()
        if not inner:
            return []
        items: list[str] = []
        for item in inner.split(","):
            parsed = _parse_scalar(item.strip(), source=source, line_no=line_no)
            if not isinstance(parsed, str):
                raise ContractError(f"{source}:{line_no}: arrays must contain scalar strings")
            items.append(parsed)
        return items

    if value.startswith("{") or value.endswith("}"):
        raise ContractError(f"{source}:{line_no}: inline mappings are not supported")

    if value.startswith('"'):
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError as exc:
            raise ContractError(f"{source}:{line_no}: invalid quoted string: {exc.msg}") from exc
        if not isinstance(parsed, str):
            raise ContractError(f"{source}:{line_no}: quoted value must be a string")
        return parsed

    if value.startswith("'"):
        if len(value) < 2 or not value.endswith("'"):
            raise ContractError(f"{source}:{line_no}: invalid single-quoted string")
        return value[1:-1].replace("''", "'")

    # Frozen V4 metadata uses strings only. Keep bare values as strings instead of
    # letting YAML implicit typing create booleans / numbers unexpectedly.
    return value


def parse_front_matter_text(text: str, *, source: str) -> ParsedMarkdown:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ContractError(f"{source}: missing YAML Front Matter")

    end_index: int | None = None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            end_index = idx
            break
    if end_index is None:
        raise ContractError(f"{source}: unterminated YAML Front Matter")

    metadata: dict[str, Any] = {}
    active_mapping: dict[str, Any] | None = None
    active_mapping_name: str | None = None

    for offset, raw_line in enumerate(lines[1:end_index], start=2):
        if "\t" in raw_line:
            raise ContractError(f"{source}:{offset}: tabs are not allowed in Front Matter")
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue

        indent = len(raw_line) - len(raw_line.lstrip(" "))
        line = raw_line.strip()
        if ":" not in line:
            raise ContractError(f"{source}:{offset}: expected key: value")
        key, raw_value = line.split(":", 1)
        key = key.strip()
        if not TOKEN_RE.fullmatch(key):
            raise ContractError(f"{source}:{offset}: invalid metadata key {key!r}")

        if indent == 0:
            if key in metadata:
                raise ContractError(f"{source}:{offset}: duplicate key {key!r}")
            if raw_value.strip() == "":
                nested: dict[str, Any] = {}
                metadata[key] = nested
                active_mapping = nested
                active_mapping_name = key
            else:
                metadata[key] = _parse_scalar(raw_value, source=source, line_no=offset)
                active_mapping = None
                active_mapping_name = None
            continue

        if indent != 2 or active_mapping is None:
            raise ContractError(
                f"{source}:{offset}: only one two-space nested mapping level is supported"
            )
        if key in active_mapping:
            raise ContractError(
                f"{source}:{offset}: duplicate key {active_mapping_name}.{key}"
            )
        if raw_value.strip() == "":
            raise ContractError(f"{source}:{offset}: nested mappings cannot contain deeper mappings")
        active_mapping[key] = _parse_scalar(raw_value, source=source, line_no=offset)

    body = "\n".join(lines[end_index + 1 :]).strip()
    return ParsedMarkdown(metadata=metadata, body=body)


def parse_front_matter_file(path: Path) -> ParsedMarkdown:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise ContractError(f"{path}: unable to read UTF-8 Markdown: {exc}") from exc
    return parse_front_matter_text(text, source=str(path))


def _validate_token_list(value: Any, *, field: str, source: str) -> tuple[str, ...]:
    if not isinstance(value, list):
        raise ContractError(f"{source}: {field} must be an inline string array")
    result: list[str] = []
    seen: set[str] = set()
    for token in value:
        if not isinstance(token, str) or not TOKEN_RE.fullmatch(token):
            raise ContractError(f"{source}: {field} contains illegal token {token!r}")
        if token in seen:
            raise ContractError(f"{source}: {field} contains duplicate token {token!r}")
        seen.add(token)
        result.append(token)
    return tuple(result)


def _validate_task_signal_value(
    value: Any, *, field: str
) -> tuple[str, ...] | None:
    if value is None:
        return None
    tokens = _validate_token_list(value, field=field, source="task-signals")
    if len(tokens) > MAX_TASK_TOKENS_PER_DIMENSION:
        raise ContractError(
            f"task-signals: {field} contains too many tokens "
            f"({len(tokens)} > {MAX_TASK_TOKENS_PER_DIMENSION})"
        )
    return tokens


def validate_rule(parsed: ParsedMarkdown, *, path: Path, locator: str) -> RuleRecord:
    metadata = parsed.metadata
    unknown = set(metadata) - RULE_KEYS
    missing = RULE_KEYS - set(metadata)
    if unknown:
        raise ContractError(f"{path}: unknown Rule top-level fields: {sorted(unknown)}")
    if missing:
        raise ContractError(f"{path}: missing Rule fields: {sorted(missing)}")

    rule_id = metadata["id"]
    if not isinstance(rule_id, str) or not RULE_ID_RE.fullmatch(rule_id):
        raise ContractError(f"{path}: invalid Rule id {rule_id!r}")
    if metadata["type"] != "rule":
        raise ContractError(f"{path}: discoverable Rule must have type: rule")
    if metadata["status"] != "active":
        raise ContractError(f"{path}: discoverable Rule must have status: active")
    if not parsed.body:
        raise ContractError(f"{path}: Rule normative body is empty")

    scope = metadata["scope"]
    if not isinstance(scope, dict):
        raise ContractError(f"{path}: scope must be a mapping")
    if set(scope) != set(SCOPE_KEYS):
        missing_scope = set(SCOPE_KEYS) - set(scope)
        unknown_scope = set(scope) - set(SCOPE_KEYS)
        details = []
        if missing_scope:
            details.append(f"missing={sorted(missing_scope)}")
        if unknown_scope:
            details.append(f"unknown={sorted(unknown_scope)}")
        raise ContractError(f"{path}: invalid scope shape ({', '.join(details)})")

    normalized: dict[str, tuple[str, ...]] = {}
    for key in SCOPE_KEYS:
        normalized[key] = _validate_token_list(scope[key], field=f"scope.{key}", source=str(path))
    if not any(normalized.values()):
        raise ContractError(f"{path}: Rule must restrict at least one scope dimension")

    return RuleRecord(id=rule_id, path=path, locator=locator, scope=normalized)


def validate_task_signals(signals: Any) -> dict[str, tuple[str, ...] | None]:
    if not isinstance(signals, dict):
        raise ContractError("task signals must be a JSON object")
    if set(signals) != set(SCOPE_KEYS):
        missing = set(SCOPE_KEYS) - set(signals)
        unknown = set(signals) - set(SCOPE_KEYS)
        details = []
        if missing:
            details.append(f"missing={sorted(missing)}")
        if unknown:
            details.append(f"unknown={sorted(unknown)}")
        raise ContractError(f"invalid task signal shape ({', '.join(details)})")

    normalized: dict[str, tuple[str, ...] | None] = {}
    for key in SCOPE_KEYS:
        normalized[key] = _validate_task_signal_value(signals[key], field=key)
    return normalized


def _relative_locator(path: Path, repo_root: Path) -> str:
    try:
        return path.relative_to(repo_root).as_posix()
    except ValueError as exc:
        raise ContractError(f"Rule file resolves outside repository root: {path}") from exc


def _walk_rule_files(root: Path) -> Iterable[Path]:
    if not root.exists() or not root.is_dir():
        raise ContractError(f"Rule root is missing or not a directory: {root}")

    walk_errors: list[OSError] = []

    def onerror(error: OSError) -> None:
        walk_errors.append(error)

    found: list[Path] = []
    try:
        for current, dirs, files in os.walk(root, followlinks=False, onerror=onerror):
            dirs.sort()
            files.sort()
            current_path = Path(current)
            for filename in files:
                if filename.endswith(".md"):
                    found.append(current_path / filename)
    except OSError as exc:
        raise ContractError(f"unable to scan Rule root {root}: {exc}") from exc

    if walk_errors:
        raise ContractError(f"incomplete Rule scan under {root}: {walk_errors[0]}")
    return found


def scan_rules(*, repo_root: Path, rule_roots: Sequence[Path]) -> list[RuleRecord]:
    repo_root = repo_root.resolve()
    seen_physical: dict[Path, str] = {}
    seen_ids: dict[str, str] = {}
    records: list[RuleRecord] = []

    for configured_root in rule_roots:
        root = configured_root if configured_root.is_absolute() else repo_root / configured_root
        root = root.resolve()
        try:
            root.relative_to(repo_root)
        except ValueError as exc:
            raise ContractError(f"Rule root must be inside repository root: {root}") from exc

        for path in _walk_rule_files(root):
            try:
                physical = path.resolve(strict=True)
            except OSError as exc:
                raise ContractError(f"unable to resolve Rule file {path}: {exc}") from exc
            if physical in seen_physical:
                raise ContractError(
                    f"same physical Rule scanned more than once: {path} and {seen_physical[physical]}"
                )
            locator = _relative_locator(physical, repo_root)
            seen_physical[physical] = locator
            record = validate_rule(parse_front_matter_file(physical), path=physical, locator=locator)
            if record.id in seen_ids:
                raise ContractError(
                    f"duplicate Rule id {record.id!r}: {seen_ids[record.id]} and {record.locator}"
                )
            seen_ids[record.id] = record.locator
            records.append(record)

    return sorted(records, key=lambda item: item.id)


def discover(
    *, repo_root: Path, rule_roots: Sequence[Path], signals: Any
) -> dict[str, Any]:
    normalized_signals = validate_task_signals(signals)
    records = scan_rules(repo_root=repo_root, rule_roots=rule_roots)
    candidates: list[dict[str, str]] = []

    for record in records:
        applicable = True
        for key in SCOPE_KEYS:
            rule_tokens = record.scope[key]
            if not rule_tokens:
                continue
            task_tokens = normalized_signals[key]
            if task_tokens is None:
                continue
            if not (set(rule_tokens) & set(task_tokens)):
                applicable = False
                break
        if applicable:
            candidates.append({"id": record.id, "path": record.locator})

    return {
        "status": "ok",
        "scanned": len(records),
        "candidate_count": len(candidates),
        "candidates": candidates,
    }


def _is_fixture_or_generated(relative: Path) -> bool:
    parts = relative.parts
    if len(parts) >= 2 and parts[0] == "evals" and parts[1] == "fixtures":
        return True
    if len(parts) >= 2 and parts[0] == "evals" and parts[1] in {"results", "workspace"}:
        return True
    return False


def validate_skill(parsed: ParsedMarkdown, *, path: Path) -> str:
    metadata = parsed.metadata
    if not parsed.body:
        raise ContractError(f"{path}: SKILL.md body is empty")
    for required in ("name", "description", "metadata"):
        if required not in metadata:
            raise ContractError(f"{path}: missing Skill field {required!r}")

    # Project lint intentionally does not reimplement the full Agent Skills schema.
    # It validates only the fields agentic-dev owns plus required discovery metadata.
    if any(key in metadata for key in ("id", "type", "status")):
        raise ContractError(f"{path}: SKILL.md must not use custom top-level id/type/status")

    name = metadata["name"]
    description = metadata["description"]
    project_meta = metadata["metadata"]
    if not isinstance(name, str) or not TOKEN_RE.fullmatch(name):
        raise ContractError(f"{path}: invalid Skill name {name!r}")
    if path.parent.name != name:
        raise ContractError(f"{path}: Skill name must match parent directory")
    if not isinstance(description, str) or not description.strip():
        raise ContractError(f"{path}: Skill description must be a non-empty string")
    if not isinstance(project_meta, dict):
        raise ContractError(f"{path}: Skill metadata must be a string mapping")
    if not all(isinstance(key, str) and isinstance(value, str) for key, value in project_meta.items()):
        raise ContractError(f"{path}: Skill metadata must contain string keys and values")

    expected = {
        "agentic-dev-id": f"skill:{name}",
        "agentic-dev-type": "skill",
        "agentic-dev-status": "active",
    }
    for key, value in expected.items():
        if project_meta.get(key) != value:
            raise ContractError(f"{path}: metadata.{key} must be {value!r}")
    return expected["agentic-dev-id"]


def validate_common_resource(parsed: ParsedMarkdown, *, path: Path) -> str:
    metadata = parsed.metadata
    if not parsed.body:
        raise ContractError(f"{path}: Markdown body is empty")
    for required in ("id", "type", "status"):
        if required not in metadata:
            raise ContractError(f"{path}: missing common Front Matter field {required!r}")
    resource_id = metadata["id"]
    resource_type = metadata["type"]
    status = metadata["status"]
    if not isinstance(resource_id, str) or not RESOURCE_ID_RE.fullmatch(resource_id):
        raise ContractError(f"{path}: invalid resource id {resource_id!r}")
    if resource_type not in COMMON_TYPES:
        raise ContractError(f"{path}: unsupported current resource type {resource_type!r}")
    if status != "active":
        raise ContractError(f"{path}: current Markdown must have status: active")
    if resource_type == "rule":
        raise ContractError(f"{path}: Rule resources must live in configured Rule roots")
    return resource_id


def lint_repository(*, repo_root: Path, rule_roots: Sequence[Path]) -> dict[str, Any]:
    repo_root = repo_root.resolve()
    rules = scan_rules(repo_root=repo_root, rule_roots=rule_roots)
    rule_paths = {record.path.resolve() for record in rules}
    ids: dict[str, str] = {record.id: record.locator for record in rules}
    skill_count = 0
    resource_count = 0

    for current, dirs, files in os.walk(repo_root, followlinks=False):
        current_path = Path(current)
        relative_dir = current_path.relative_to(repo_root)
        dirs[:] = sorted(
            d
            for d in dirs
            if d != ".git"
            and not _is_fixture_or_generated(relative_dir / d)
        )
        for filename in sorted(files):
            if not filename.endswith(".md"):
                continue
            path = (current_path / filename).resolve()
            relative = path.relative_to(repo_root)
            if _is_fixture_or_generated(relative):
                continue
            if path in rule_paths:
                continue

            parsed = parse_front_matter_file(path)
            if path.name == "SKILL.md":
                resource_id = validate_skill(parsed, path=path)
                skill_count += 1
            else:
                resource_id = validate_common_resource(parsed, path=path)
                resource_count += 1

            locator = relative.as_posix()
            if resource_id in ids:
                raise ContractError(
                    f"duplicate current resource id {resource_id!r}: {ids[resource_id]} and {locator}"
                )
            ids[resource_id] = locator

    return {
        "status": "ok",
        "rules": len(rules),
        "skills": skill_count,
        "markdown_resources": resource_count,
        "fixture_markdown_excluded": True,
    }


def _load_signals(args: argparse.Namespace) -> Any:
    if bool(args.signals_json) == bool(args.signals_file):
        raise ContractError("provide exactly one of --signals-json or --signals-file")
    try:
        if args.signals_json:
            return json.loads(args.signals_json)
        return json.loads(Path(args.signals_file).read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError, UnicodeError) as exc:
        raise ContractError(f"unable to load task signals: {exc}") from exc


def _paths(values: Sequence[str] | None) -> list[Path]:
    return [Path(value) for value in (values or ["docs/rules"])]


def _emit(payload: dict[str, Any]) -> None:
    json.dump(payload, sys.stdout, ensure_ascii=False, sort_keys=False)
    sys.stdout.write("\n")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="agentic-dev V4 Rule Discovery Tool")
    parser.add_argument("--repo-root", default=".", help="repository root (default: current directory)")
    subparsers = parser.add_subparsers(dest="command", required=True)

    discover_parser = subparsers.add_parser("discover", help="return deterministic Rule locators")
    discover_parser.add_argument("--rules-root", action="append", dest="rule_roots")
    discover_parser.add_argument("--signals-json")
    discover_parser.add_argument("--signals-file")

    lint_parser = subparsers.add_parser("lint", help="validate V4 current Markdown / Rule / Skill metadata")
    lint_parser.add_argument("--rules-root", action="append", dest="rule_roots")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    repo_root = Path(args.repo_root).resolve()
    rule_roots = _paths(getattr(args, "rule_roots", None))

    try:
        if args.command == "discover":
            payload = discover(repo_root=repo_root, rule_roots=rule_roots, signals=_load_signals(args))
        elif args.command == "lint":
            payload = lint_repository(repo_root=repo_root, rule_roots=rule_roots)
        else:  # pragma: no cover - argparse owns command validation
            raise ContractError(f"unknown command {args.command!r}")
    except ContractError as exc:
        _emit({"status": "fail-closed", "candidates": [], "diagnostics": [str(exc)]})
        return 2

    _emit(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())