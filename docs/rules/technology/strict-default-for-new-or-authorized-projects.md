---
id: rule:strict-default-for-new-or-authorized-projects
type: rule
status: active
scope:
  phases: [execute]
  activities: [implementation]
  technologies: [typescript]
  artifacts: [configuration]
  risks: [type-safety]
---

# 新建或已授权工程优先严格类型检查

新建或明确允许调整的 Vue + TypeScript 工程默认优先保持 `strict: true`。既有项目是否开启、加强或迁移 strict 由项目 Authority 决定；普通功能修改不得为采用该默认值擅自重写整个 `tsconfig`。