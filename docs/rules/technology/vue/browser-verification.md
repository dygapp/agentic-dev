---
id: rule:vue-browser-verification
type: rule
status: active
scope:
  phases: [execute, converge]
  activities: [verification]
  technologies: [vue3]
  artifacts: [vue-sfc, user-interface]
  risks: [browser-behavior, visual-fidelity]
---

# Vue 浏览器 / 视觉验证按风险扩展

变化涉及用户交互、DOM 生命周期、异步竞态或视觉验收义务时，静态 type-check / build 通常不足，应按当前验收责任扩展到 component、integration、browser 或 visual evidence。不存在相应风险时，不机械运行所有层级。