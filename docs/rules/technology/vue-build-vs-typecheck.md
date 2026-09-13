---
id: rule:vue-build-vs-typecheck
type: rule
status: active
scope:
  phases: [execute, converge]
  activities: [verification]
  technologies: [vue3, typescript]
  artifacts: [vue-sfc, code]
  risks: [type-safety]
---

# Vue Build 不等于类型检查

Vite 对 TypeScript 的构建职责主要是 transpilation，不负责完整 Vue SFC 类型检查。因此 `vite build` 成功不能单独证明 Vue SFC / TypeScript 类型责任闭环。

需要类型证据时，应解析并实际执行使用方当前 Vue-aware type-check 机制，例如其已配置的 `vue-tsc` 路径。