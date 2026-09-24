# Skill 目录导航

`skills/**` 是 `agentic-dev` 唯一正式的 Consumer runtime product。ordinary Agent 使用宿主原生 Agent Skills discovery 根据 `name` / `description` 选择 Skill；本 README 只用于人类浏览。

当前维护 15 个 canonical Skills：

## 项目基础 / 系统性责任
- `establish-requirement-baseline`
- `clarify-architecture`
- `activate-model-collaboration`

## Feature / change 执行责任
- `clarify-intent`
- `specify`
- `technical-plan`
- `slice-work`
- `readiness-check`
- `execute-unit`
- `systematic-debug`
- `converge`

## 可复用支撑责任
- `external-operation`
- `human-review`
- `review-change`

## 平台专项责任
- `github-actions-verification`

每个 Skill 的 Trigger、Inputs、Procedure、Outputs、Exit / Escalation 由自己的 `SKILL.md` 持有。Consumer-specific policy 继续由 Consumer Repository Authority 负责，不通过 Provider runtime 注入。
