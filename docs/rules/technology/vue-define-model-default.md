---
id: rule:vue-define-model-default
type: rule
status: active
scope:
  phases: [execute]
  activities: [implementation]
  technologies: [vue3]
  artifacts: [vue-sfc]
  risks: []
---

# 标准 Component `v-model` 优先 `defineModel`

在支持 `defineModel()` 的 Vue 版本中，当前确实属于标准 component `v-model` contract 且使用方没有更具体兼容 / library contract 时，优先使用 `defineModel()`。不得仅为了使用新 API 改写已有稳定自定义 prop / emit contract。