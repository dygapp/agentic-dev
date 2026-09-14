---
id: rule:typescript-type-safety
type: rule
status: active
scope:
  phases: [execute]
  activities: [implementation]
  technologies: [typescript]
  artifacts: [code]
  risks: [type-safety]
---

# TypeScript 类型安全

TypeScript 代码实现默认利用类型系统表达真实边界，而不是通过重复注解、`any` 或 assertion 消除编译器反馈。

## 保留有效推断

默认不为所有局部变量、`ref`、`computed` 重复声明显而易见的类型。显式类型优先用于公共 API、union / nullable / external input、复杂值和需要稳定边界的位置。

## 不把 `any` 当默认逃生口

对真实未知输入优先使用 `unknown`、union、runtime guard 与正常控制流 narrowing。既有使用方无关 `any` 不因此自动进入当前执行范围，但新变化不得用 `any` 或无证据 assertion 掩盖可表达的类型责任。
