---
id: guide:skill-inventory
type: guide
status: active
---

# Skills

当前仓库维护 11 个可复用 Skill：

## Core Method Skills

- `clarify-intent`
- `specify`
- `technical-plan`
- `slice-work`
- `readiness-check`
- `execute-unit`
- `systematic-debug`
- `converge`

## Supporting Skills

- `external-operation`
- `review-change`

## Platform-specific Skill

- `github-actions-verification`

Skill 必须符合 `docs/architecture/skill-architecture.md` 的独立闭环与准入要求。普通横切约束由 `docs/rules/**` 持有，并通过 Rule Discovery 按需加载；不得为减少 Rule 数量把普通条件机械升级为 Skill。