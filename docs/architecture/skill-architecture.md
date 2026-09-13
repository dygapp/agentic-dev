---
id: architecture:skill
type: architecture
status: active
---

# Skill 架构

## 1. Skill 定义

Skill 是拥有稳定独立执行闭环的能力：

```text
Trigger / Purpose
→ Inputs
→ Procedure
→ Outputs
→ Exit Conditions
→ Escalation
```

Skill 实现既定 Method，不创建隐藏生命周期，也不通过自身存在取得仓库写入、集成、发布或部署授权。

## 2. 当前分类

### 核心 Method Skills（8）

- `clarify-intent`
- `specify`
- `technical-plan`
- `slice-work`
- `readiness-check`
- `execute-unit`
- `systematic-debug`
- `converge`

### Reusable supporting Skills（2）

- `external-operation`：对外部可变状态执行读取、最小操作、重新读取验证和有界升级；
- `review-change`：对当前最终变更执行 authority-aware review，输出 findings 或通过结论。

### Platform-specific Skills（1）

- `github-actions-verification`

总数为 11。新增 supporting Skill 不意味着重新打开核心 Method Skill 设计。

## 3. Rule 边界

以下内容默认不是 Skill：

- 实现最小化、差异范围、数据访问有界性；
- 证据类型、视觉证据、migration completion；
- Git commit 约束；
- 语言 / 术语约束；
- 技术 API / framework 约束；
- 外部操作过程中的单项授权或并发不变量。

它们由 Rule 按任务 signals 发现，Skill 只在过程真正需要时消费候选 Rule。

## 4. Agent Skills 互操作

每个 `SKILL.md` 必须遵守当前 Agent Skills Specification。`name` 与 `description` 为 required top-level fields；本仓逻辑 `id/type/status` 通过官方 `metadata` string map 扩展：

```yaml
metadata:
  agentic-dev-id: "skill:example"
  agentic-dev-type: "skill"
  agentic-dev-status: "active"
```

不得添加规范未定义的自定义 top-level metadata key。

## 5. 准入门禁

新增 Skill 至少证明：独立 trigger、稳定输入、可重复 procedure、稳定输出、明确退出 / 升级、可组合性、单一语义 owner，以及有辨识力的行为评估。仅“重要”“可复用”“多个 Skill 都要遵守”“存在步骤”不足以升级为 Skill。