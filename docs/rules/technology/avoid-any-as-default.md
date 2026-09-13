---
id: rule:avoid-any-as-default
type: rule
status: active
scope:
  phases: [execute]
  activities: [implementation]
  technologies: [typescript]
  artifacts: [code]
  risks: [type-safety]
---

# 不把 `any` 当默认逃生口

对真实未知输入优先使用 `unknown`、union、runtime guard 与正常控制流 narrowing。既有使用方无关 `any` 不因此自动进入当前执行范围，但新变化不得用 `any` 或无证据 assertion 掩盖可表达的类型责任。