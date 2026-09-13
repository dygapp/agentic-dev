---
id: rule:vue-props-emits-declaration-mode
type: rule
status: active
scope:
  phases: [execute]
  activities: [implementation]
  technologies: [vue3, typescript]
  artifacts: [vue-sfc]
  risks: [type-safety]
---

# Vue Props / Emits 声明模式

TypeScript SFC 中 `defineProps` / `defineEmits` 可以使用 runtime declaration 或 type declaration，但同一声明不能混用两种模式。当前契约需要 runtime validation 时，不得为了更简洁的类型声明删除运行时责任。