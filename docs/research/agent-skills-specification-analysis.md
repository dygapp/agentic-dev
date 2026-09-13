---
id: research:agent-skills-specification
type: research
status: active
---

# Agent Skills Specification 研究摘要

**研究基线：** 2026-09-13  
**来源性质：** 外部标准 / 规范参考  
**规范入口：** `https://agentskills.io/specification`

## 1. 研究目的

本文件记录 Agent Skills Specification 对 `agentic-dev` Skill Packaging、Discovery 与 Progressive Disclosure 的互操作参考。它不是本仓库 Method / Architecture / Skill 的规范性 Authority。

## 2. 当前规范要点

一个 Skill 至少包含 `SKILL.md`，由 YAML Front Matter 与 Markdown instructions 组成。

当前规范的顶层必需字段：

- `name`；
- `description`。

当前可选字段包括：

- `license`；
- `compatibility`；
- `metadata`；
- `allowed-tools`（实验性）。

`metadata` 是规范提供的扩展点，采用 string → string mapping；自定义扩展 key 应使用足够独特的命名，避免与其他实现冲突。

规范还支持按需组织：

- `scripts/`；
- `references/`；
- `assets/`。

这些是可选资源，不是固定模板要求。

## 3. Progressive Disclosure

规范的核心加载模型为：

1. Runtime 先读取 Skill metadata；
2. Skill 被选择后读取完整 `SKILL.md`；
3. references / scripts / assets 只在需要时加载。

这与 `agentic-dev` 的渐进式披露原则相容，但外部规范只定义 Skill 包装与发现，不决定本仓 Method 或 Rule Discovery。

## 4. V4 采用方式

V4 保持 Agent Skills 顶层互操作字段不变，并把本仓逻辑身份放入官方 `metadata` 扩展点：

```yaml
---
name: example
description: ...
metadata:
  agentic-dev-id: "skill:example"
  agentic-dev-type: "skill"
  agentic-dev-status: "active"
---
```

不得为了统一本仓其他 Markdown schema 而给 `SKILL.md` 增加规范未定义的自定义顶层 `id/type/status`。

V4 Rule Discovery Tool 不扫描 Skill metadata；Skill 继续由 Agent Skills 原生 `name` / `description` 机制发现。Rule 与 Skill 是两套职责不同的发现路径。

## 5. Validation 边界

`skills-ref validate` 等格式检查可以验证包装与 Front Matter 约束，但不能替代：

- Skill 职责 / Contract Review；
- Activation Eval；
- Behavior Eval；
- Current Runtime Evidence。

格式有效不等于 Skill 语义正确。

## 6. 结论

Agent Skills Specification 为 `agentic-dev` 的 Skill 提供通用 Packaging / Discovery / Progressive Disclosure 互操作层；本仓 Method、Skill 边界和 Rule Discovery 架构仍由各自 current owner 定义。