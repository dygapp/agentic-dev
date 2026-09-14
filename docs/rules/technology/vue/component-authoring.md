---
id: rule:vue-component-authoring
type: rule
status: active
scope:
  phases: [execute]
  activities: [implementation]
  technologies: [vue3]
  artifacts: [vue-sfc]
  risks: []
---

# Vue 组件 Authoring

设计或修改 Vue 3 SFC 组件时，相关组件 contract 作为一个任务级规范集合处理。

## `<script setup>` 默认

在 Vue SFC + Composition API 场景中，新建代码默认优先使用 `<script setup>`。这不是 Options API 的弃用声明，也不构成把既有稳定组件批量迁移到新风格的授权。

## Props 保持单向输入

Props 遵循父到子的单向数据流。子组件不得直接修改 prop 本身。需要可编辑语义时，根据当前契约选择本地 state、emit、标准 component `v-model` 或使用方已定义的共享状态机制。

## Props / Emits 声明保持契约责任

TypeScript SFC 中 `defineProps` / `defineEmits` 可以使用 runtime declaration 或 type declaration，但同一声明不能混用两种模式。当前契约需要 runtime validation 时，不得为了更简洁的类型声明删除运行时责任。

## 标准 Component `v-model`

在支持 `defineModel()` 的 Vue 版本中，当前确实属于标准 component `v-model` contract 且使用方没有更具体兼容 / library contract 时，优先使用 `defineModel()`。不得仅为了使用新 API 改写已有稳定自定义 prop / emit contract。