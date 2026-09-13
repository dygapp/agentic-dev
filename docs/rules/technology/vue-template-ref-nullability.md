---
id: rule:vue-template-ref-nullability
type: rule
status: active
scope:
  phases: [execute]
  activities: [implementation]
  technologies: [vue3, typescript]
  artifacts: [vue-sfc]
  risks: [nullability, type-safety]
---

# Vue Template Ref 可空生命周期

DOM / component template ref 在挂载前可能为空，条件卸载后也可能再次为空。TypeScript 类型与实现必须反映该生命周期，不得仅为消除类型错误无证据使用 non-null assertion。