---
id: rule:typescript-type-safety
type: rule
status: active
scope:
  phases: [execute]
  activities: [implementation]
  technologies: [typescript]
  artifacts: [code, configuration]
  risks: []
---

# TypeScript 类型安全

TypeScript 实现默认利用类型系统表达真实边界，而不是通过重复注解、`any` 或 assertion 消除编译器反馈。

## 保留有效推断

默认不为所有局部变量、`ref`、`computed` 重复声明显而易见的类型。显式类型优先用于公共 API、union / nullable / external input、复杂值和需要稳定边界的位置。

## 不把 `any` 当默认逃生口

对真实未知输入优先使用 `unknown`、union、runtime guard 与正常控制流 narrowing。既有使用方无关 `any` 不因此自动进入当前执行范围，但新变化不得用 `any` 或无证据 assertion 掩盖可表达的类型责任。

## 严格检查由当前项目边界决定

新建或明确允许调整的 TypeScript 工程默认优先保持严格类型检查。既有项目是否开启、加强或迁移 strict 由项目 Authority 决定；普通功能修改不得为了采用该默认值擅自重写整个 `tsconfig`。