# Agent Skills Specification 研究摘要

**研究基线：** 2026-08-18  
**来源性质：** 外部标准 / 规范参考  
**规范入口：** `https://agentskills.io/specification`

## 1. 研究目的

本文件记录 Agent Skills Specification 对 `agentic-dev` Skill Packaging、Discovery 与 Progressive Disclosure 的直接参考价值。

它不是本仓库 Method、Architecture 或 Skill Contract 的语义权威。

`agentic-dev` 采用以下边界：

- Method / Contract 决定 Skill **应该负责什么**；
- Agent Skills Specification 只作为 Skill **如何被通用 Agent Runtime 表达、发现和加载** 的互操作参考；
- Runtime / Vendor 私有能力只有在确有必要时才进入实现，不反向改变 Method。

## 2. 规范中的核心要求

### 2.1 Skill 目录与 `SKILL.md`

一个 Skill 至少是一个包含 `SKILL.md` 的目录。

`SKILL.md` 由两部分组成：

1. YAML Front Matter；
2. Markdown Instructions。

当前规范要求 Front Matter 至少包含：

- `name`；
- `description`。

其中：

- `name` 应与父目录名一致，并满足小写字母、数字和连字符等命名约束；
- `description` 不只描述“做什么”，还应描述“什么时候使用”，以帮助 Agent 做激活判断。

`license`、`compatibility`、`metadata`、`allowed-tools` 等字段为可选项；其中 `allowed-tools` 当前属于实验性能力。

### 2.2 可选资源目录

规范建议按需使用：

- `scripts/`：可执行脚本；
- `references/`：按需读取的补充文档；
- `assets/`：模板、图片、数据等静态资源。

这些目录是组织约定，不是每个 Skill 都必须创建的固定模板。

### 2.3 Progressive Disclosure

规范明确采用分层加载：

1. Runtime 启动时只加载 `name` / `description` 等 Metadata；
2. Skill 被激活后加载完整 `SKILL.md`；
3. 其他资源只在需要时加载。

这与本仓库的 Context Discipline / Progressive Disclosure 原则一致，但两者承担不同层级职责：

- 本仓库原则约束 Agent 应如何控制上下文；
- 外部规范提供一种具体的 Skill Packaging / Loading 机制。

规范还建议控制主 `SKILL.md` 长度，并把详细材料拆到按需引用文件中。该建议是工程优化，不升级为 `agentic-dev` Method 的绝对硬规则。

### 2.4 Validation

规范提供 `skills-ref validate` 作为格式校验方式，可检查 Front Matter 与命名约束。

这类验证可以作为后续 Skill Operationalization 的静态检查能力，但不能替代：

- Contract Review；
- Activation Eval；
- Behavior Eval；
- Current Runtime Evidence。

格式有效不等于 Skill 语义正确。

## 3. 对 `agentic-dev` 的实际影响

### 3.1 已采用

第一批 8 个核心 Skill 已采用最小 Front Matter：

```yaml
---
name: <skill-name>
description: <what + when-to-use>
---
```

这一做法用于提高通用 Agent Runtime 的发现与激活能力，没有改变任何 Skill Contract。

B3 Fresh Runtime Eval 已进一步验证代表性核心 Skill 的实际 Activation / Behavior，而不是只依赖静态格式正确性。

### 3.2 当前不需要采用

当前不因为规范存在就机械增加：

- `license`；
- `compatibility`；
- `metadata`；
- `allowed-tools`；
- `scripts/`；
- `references/`；
- `assets/`。

只有具体 Skill 出现真实需求时再增加。

### 3.3 不进入 Method Authority

以下内容不得从外部规范直接反向写入本仓库 Method：

- 某个 Runtime 的调用方式；
- 某个 Tool Permission 机制；
- 文件数量或目录层级偏好；
- 推荐长度等工程建议；
- Vendor-specific Extension。

如果未来外部规范变化，现有 `agentic-dev` Method / Contract 不自动变化。需要改变本地方法时，必须经过显式 Method Decision。

## 4. 结论

Agent Skills Specification 对本仓库最重要的价值是：

> 为 `agentic-dev` 已定义好的 Skill 语义提供一个通用 Packaging / Discovery / Progressive Disclosure 参考层。

它补齐了 `mattpocock/skills`、`github/spec-kit`、`obra/superpowers` 之外的“外部格式标准”维度，但不成为第四个方法论样本，也不参与本仓库 Method Authority 排序。
