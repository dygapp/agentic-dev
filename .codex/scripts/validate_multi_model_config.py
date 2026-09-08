#!/usr/bin/env python3
"""验证实验分支中的 Codex 多模型配置与当前本地模型目录。"""

from __future__ import annotations

import json
import subprocess
import sys
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = ROOT / ".codex" / "config.toml"
AGENT_DIR = ROOT / ".codex" / "agents"
REQUIRED_AGENT_FIELDS = {
    "name",
    "description",
    "developer_instructions",
    "model",
    "model_reasoning_effort",
    "sandbox_mode",
}
VALID_SANDBOX_MODES = {"read-only", "workspace-write"}
EXPECTED_AGENT_NAMES = {
    "fast_explorer",
    "implementation_worker",
    "quality_reviewer",
    "critical_reviewer",
}


def read_toml(path: Path) -> dict[str, object]:
    with path.open("rb") as stream:
        return tomllib.load(stream)


def load_model_catalog() -> dict[str, set[str]]:
    result = subprocess.run(
        ["codex", "debug", "models"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        detail = result.stderr.strip() or "没有诊断信息"
        raise RuntimeError(f"无法读取当前 Codex 模型目录：{detail}")

    payload = json.loads(result.stdout)
    return {
        model["slug"]: {
            level["effort"] for level in model.get("supported_reasoning_levels", [])
        }
        for model in payload.get("models", [])
        if model.get("visibility") == "list"
    }


def validate() -> list[str]:
    errors: list[str] = []
    config = read_toml(CONFIG_PATH)
    agents_config = config.get("agents")
    if not isinstance(agents_config, dict):
        errors.append(".codex/config.toml 缺少 [agents] 配置")
    else:
        if agents_config.get("enabled") is not True:
            errors.append("agents.enabled 必须为 true")
        concurrency = agents_config.get("max_concurrent_threads_per_session")
        if not isinstance(concurrency, int) or not 1 <= concurrency <= 3:
            errors.append("并发上限必须是 1 到 3 之间的整数")

    try:
        catalog = load_model_catalog()
    except (RuntimeError, json.JSONDecodeError) as error:
        errors.append(str(error))
        catalog = {}

    seen_names: set[str] = set()
    agent_paths = sorted(AGENT_DIR.glob("*.toml"))
    if not agent_paths:
        errors.append(".codex/agents 中没有自定义代理配置")

    for path in agent_paths:
        agent = read_toml(path)
        missing = sorted(REQUIRED_AGENT_FIELDS - agent.keys())
        if missing:
            errors.append(f"{path.name} 缺少字段：{', '.join(missing)}")
            continue

        for field in ("name", "description", "developer_instructions", "model"):
            if not isinstance(agent[field], str) or not agent[field].strip():
                errors.append(f"{path.name} 的 {field} 必须是非空字符串")

        name = agent["name"]
        if not isinstance(name, str) or not name:
            errors.append(f"{path.name} 的 name 必须是非空字符串")
        elif name in seen_names:
            errors.append(f"代理名称重复：{name}")
        else:
            seen_names.add(name)

        sandbox_mode = agent["sandbox_mode"]
        if sandbox_mode not in VALID_SANDBOX_MODES:
            errors.append(f"{path.name} 使用了无效 sandbox_mode：{sandbox_mode}")

        model = agent["model"]
        effort = agent["model_reasoning_effort"]
        if catalog and model not in catalog:
            errors.append(f"{path.name} 请求的模型当前不可见：{model}")
        elif catalog and effort not in catalog[model]:
            errors.append(f"{path.name} 的模型 {model} 不支持推理强度 {effort}")

    missing_agents = sorted(EXPECTED_AGENT_NAMES - seen_names)
    unexpected_agents = sorted(seen_names - EXPECTED_AGENT_NAMES)
    if missing_agents:
        errors.append(f"缺少实验代理：{', '.join(missing_agents)}")
    if unexpected_agents:
        errors.append(f"存在未登记实验代理：{', '.join(unexpected_agents)}")

    writable_agents = []
    for path in agent_paths:
        agent = read_toml(path)
        if agent.get("sandbox_mode") == "workspace-write":
            writable_agents.append(agent.get("name"))
    if writable_agents != ["implementation_worker"]:
        errors.append("必须且只能由 implementation_worker 使用 workspace-write")

    if isinstance(agents_config, dict) and catalog:
        default_model = agents_config.get("default_subagent_model")
        default_effort = agents_config.get("default_subagent_reasoning_effort")
        if default_model not in catalog:
            errors.append(f"默认子代理模型当前不可见：{default_model}")
        elif default_effort not in catalog[default_model]:
            errors.append(
                f"默认子代理模型 {default_model} 不支持推理强度 {default_effort}"
            )

    return errors


def main() -> int:
    try:
        errors = validate()
    except (OSError, tomllib.TOMLDecodeError) as error:
        print(f"配置读取失败：{error}", file=sys.stderr)
        return 1

    if errors:
        for error in errors:
            print(f"失败：{error}", file=sys.stderr)
        return 1

    print("通过：Codex 多模型配置结构有效，所选模型和推理强度在当前目录中可见。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
