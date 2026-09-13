---
id: rule:vue-props-one-way-input
type: rule
status: active
scope:
  phases: [execute]
  activities: [implementation]
  technologies: [vue3]
  artifacts: [vue-sfc]
  risks: [state-ownership]
---

# Vue Props 单向输入

Vue props 遵循父到子的单向数据流。子组件不得直接修改 prop 本身。需要可编辑语义时，根据当前契约选择本地 state、emit、标准 component `v-model` 或使用方已定义的共享状态机制。