---
id: guide:choosing-next-step
type: guide
status: active
---

# 根据项目当前状态选择下一步

当用户问“下一步具体做什么”时，AI 不应从 Skill 清单随机挑选，也不应只凭一般软件工程经验生成一份大而全计划。

判断应来自：

```text
Consumer 当前项目事实
+
本 Guide 的方法导航
→ 当前最主要阻塞责任
→ 对应 Skill / Guide
```

本 Guide 不是状态机，也不拥有项目当前状态。

## 1. 先恢复 Consumer 当前事实

至少读取当前任务真正需要的：

- 根 `AGENTS.md`；
- Project / Requirement / Architecture 的稳定入口；
- current work / Roadmap；
- 当前已有 Specification / plan / execution unit / findings；
- installed Skills；
- 当前任务适用的 Consumer-local constraints。

历史聊天、旧计划、模型记忆和 upstream Guide 都不能替代这些项目事实。

## 2. 找最靠前的真实阻塞

优先解决会让下游工作建立在猜测上的缺口，而不是选择“看起来最有产出”的动作。

| 当前事实 | 建议下一责任 |
|---|---|
| Repository 还没有建立 | [`bootstrap-new-project.md`](bootstrap-new-project.md) |
| Existing Repository 尚未安装 `agentic-dev` Skills | [`adopting-agentic-dev.md`](adopting-agentic-dev.md) |
| Requirement Authority 分散、冲突、owner 不清，或多个 Feature 被同一需求缺口阻塞 | `establish-requirement-baseline` |
| 多个当前 / 预期 Feature 共同依赖长期、高成本难逆的 systemic architecture driver | `clarify-architecture` |
| 当前 Feature 目标 / Scope / 用户可见行为 / Acceptance 仍有高影响产品歧义 | `clarify-intent` |
| 当前 Feature intent 已清楚，但 WHAT / WHY / Acceptance 还没有稳定 Specification | `specify` |
| 实施前存在必须跨多个 execution unit 稳定的 HOW | `technical-plan` |
| Specification 已 Ready，需要形成可独立执行的工作单元 | `slice-work` |
| 已有目标 Execution Unit，但不确定是否真的可执行 | `readiness-check` |
| Execution Unit 已 Ready | `execute-unit` |
| 出现 unexpected failure / defect | `systematic-debug` |
| 多个 Unit 基本完成，需要判断完整 change 是否真的 Ready | `converge` |
| 当前责任需要安全修改 GitHub / 外部 API / review environment / shared state | `external-operation` |
| GitHub Actions 本身是关键验证路径 | `github-actions-verification` |
| 需要产品 / 业务 / 架构 / 工程责任人集中理解和确认 | `human-review` |
| 项目希望启用多 Agent / 多模型协作 | `activate-model-collaboration` |

一个项目可以同时存在多个问题，但一次回答应指出当前最主要的 1 个下一责任，以及为什么它优先。

## 3. 不要把所有步骤都变成当前计划

例如当前 Requirement Baseline 尚未成立时，不需要同时制定：

```text
完整 Architecture
→ 全部 Feature Specification
→ 所有 Execution Units
→ CI / deploy
```

此时更合适的是：

```text
当前主要缺口：Requirement Baseline
下一责任：establish-requirement-baseline
完成后重新判断 Architecture / Feature readiness
```

方法论通过反复“读取当前事实 → 选择下一责任”推进，而不是一次冻结整个未来状态机。

## 4. 三类常见项目状态

### Requirement 还没有稳定下来

迹象：

- 原始材料很多，但没有唯一 owner；
- 同一业务规则多个文档冲突；
- 多个 Feature 都在重复询问相同业务事实；
- Fresh Context 无法判断当前产品事实。

下一步通常是 `establish-requirement-baseline`，而不是逐 Feature 编码。

### Requirement 足够，但存在系统性 Architecture blocker

迹象：

- 多个 Feature 都依赖同一共享 contract / core data / integration / deployment boundary；
- 这是长期、高成本难逆问题；
- 不解决会迫使每个 Feature 各自猜一遍。

下一步通常是 `clarify-architecture`。

### Requirement / Architecture 已足够

如果当前已有明确 Feature，可以进入：

```text
clarify-intent
→ specify
→ technical-plan?（按需）
→ slice-work
→ readiness-check
→ execute-unit
→ converge
```

这不是强制固定流程。某些步骤可以因当前项目事实已经满足而直接跳过；每个 Skill 自己定义 Trigger 和 Exit。

## 5. 输出“下一步建议”时至少说明

建议包含：

- 当前观察到的项目状态；
- 当前最主要缺口；
- 下一责任 / Skill；
- 支持该判断的 Consumer-local facts；
- 为什么不是另一个常见责任；
- 当前不需要提前做什么；
- 哪些条件满足后需要重新判断。

不需要把整个 Guide 或所有 Skill 重新解释一遍。

## 6. Guide 与 Skill 的边界

本 Guide 只负责“选下一类工作”。

一旦选定 `execute-unit`、`specify`、`clarify-architecture` 等责任，就读取 installed Skill 的 `SKILL.md` 执行，不继续用本 Guide 维护第二套 procedure。
