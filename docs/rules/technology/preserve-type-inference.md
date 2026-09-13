---
id: rule:preserve-type-inference
type: rule
status: active
scope:
  phases: [execute]
  activities: [implementation]
  technologies: [typescript]
  artifacts: [code]
  risks: [type-safety]
---

# 保留有效类型推断

默认不为所有局部变量、`ref`、`computed` 重复声明显而易见的类型。显式类型优先用于公共 API、union / nullable / external input、复杂值和需要稳定边界的位置。