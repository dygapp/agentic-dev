---
id: guide:skills
type: guide
status: active
---

# Skills

当前仓库维护 11 个 Skill：8 个核心 Method Skill、2 个 reusable supporting Skill、1 个平台专项 Skill。

## 核心 Method Skills

- `clarify-intent`
- `specify`
- `technical-plan`
- `slice-work`
- `readiness-check`
- `execute-unit`
- `systematic-debug`
- `converge`

## Reusable supporting Skills

- `external-operation`
- `review-change`

## Platform-specific Skill

- `github-actions-verification`

Skill 是否成立只取决于是否拥有稳定独立执行闭环，不取决于历史分类或希望减少 Rule 数量。完整边界见 `docs/architecture/skill-architecture.md`。

普通横切约束由 `docs/rules/` 中的 Rule 按需发现，不复制到 Skill inventory。