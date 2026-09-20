---
id: guide:skill-inventory
type: guide
status: active
distribution: source-only
---

# Skill 目录导航

本 README 是 Human View，用于快速了解当前可复用 Skill。ordinary Agent runtime 通过 Agent Skills 原生 discovery 按 Trigger / Purpose 选择 Skill，不把本清单作为 Skill selector。

当前仓库维护 15 个 Skill：

## 项目建立 / 系统性能力 Skill（3）

- `establish-requirement-baseline`
- `clarify-architecture`
- `activate-model-collaboration`

这些 Skill 分别承接已有 Method 中具有独立触发与完成边界、但原 12 个执行 Skill 无法安全承载的长期工作责任；它们不接管完整软件开发生命周期。

## AI Development 支撑 Skill（8）

- `clarify-intent`
- `specify`
- `technical-plan`
- `slice-work`
- `readiness-check`
- `execute-unit`
- `systematic-debug`
- `converge`

这些 Skill 当前服务 AI Development Method，但 Skill 身份不等于 Method stage；某个 Method stage 也不要求一定存在对应 Skill。

## 可复用支撑 Skill（3）

- `external-operation`
- `human-review`
- `review-change`

## 平台专项 Skill（1）

- `github-actions-verification`

Skill 必须符合 `docs/architecture/skill-architecture.md` 的 Trigger / Inputs / Procedure / Outputs / Exit / Escalation 与准入要求。Rule 是独立的横切条件约束，可以约束 Skill，也可以在没有 Skill 时约束 direct work；不得为了减少 Rule 数量把普通 policy 机械升级为 Skill。
