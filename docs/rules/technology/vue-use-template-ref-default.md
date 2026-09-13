---
id: rule:vue-use-template-ref-default
type: rule
status: active
scope:
  phases: [execute]
  activities: [implementation]
  technologies: [vue3, typescript]
  artifacts: [vue-sfc]
  risks: [type-safety]
---

# Vue 静态 Template Ref 优先 `useTemplateRef`

在 Vue 3.5+、Composition API、静态 template ref 场景中，优先利用 `useTemplateRef()` 与 Vue Language Tools 的类型推断。动态组件、低版本、非 SFC 或推断不足时，显式 `ref` / 泛型 / `InstanceType` 等仍是合法路径。