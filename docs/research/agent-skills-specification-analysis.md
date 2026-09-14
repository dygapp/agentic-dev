---
id: research:agent-skills-specification
type: research
status: active
---

# Agent Skills Specification 研究摘要

**研究基线：** 2026-09-14  
**来源性质：** 外部标准 / 规范参考  
**规范入口：** `https://agentskills.io/specification`

## 1. 研究目的

本文件记录 Agent Skills Specification 对 `agentic-dev` Skill Packaging、Discovery 与 Progressive Disclosure 的互操作参考。它不是本仓库 Method / Architecture / Skill / Rule 的规范性 Authority。

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

## 3. Progressive Disclosure 与大小参照

规范的核心加载模型为：

1. Runtime 先读取 Skill metadata；规范示意约 `~100 tokens`；
2. Skill 被选择后读取完整 `SKILL.md` instructions；官方推荐 `< 5000 tokens`；
3. references / scripts / assets 只在需要时加载。

规范同时建议主 `SKILL.md` 保持在 `500 lines` 以下，并把更详细的参考内容移到单独文件；reference 文件应保持聚焦，文件引用避免形成很深的链条。

这说明 Progressive Disclosure 优化的是**激活前 metadata 成本 + 激活后的完整任务说明 + 按需参考资源**，而不是把一个任务说明机械拆成大量最小文件。

该数值是 Agent Skills 对 `SKILL.md` 的外部推荐，不自动成为 Rule 的规范。`agentic-dev` Rule Architecture 只把 `5000 tokens / 500 lines` 作为任务级 Rule 文件的上限复核参照：Rule 通常应更小，但是否拆分仍首先由任务语义边界、共同发现 / 共同消费关系和总加载成本决定。

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

Agent Skills Specification 为 `agentic-dev` 的 Skill 提供通用 Packaging / Discovery / Progressive Disclosure 互操作层；其“metadata → 完整 instructions → 按需 resources”的结构与文件大小建议也为 Rule granularity 提供工程参照，但本仓 Method、Skill 边界和 Rule Discovery / Granularity 架构仍由各自 current owner 定义。