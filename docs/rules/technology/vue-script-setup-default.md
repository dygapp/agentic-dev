---
id: rule:vue-script-setup-default
type: rule
status: active
scope:
  phases: [execute]
  activities: [implementation]
  technologies: [vue3]
  artifacts: [vue-sfc]
  risks: []
---

# Vue `<script setup>` 默认

在 Vue SFC + Composition API 场景中，新建代码默认优先使用 `<script setup>`。这不是 Options API 的弃用声明，也不构成把既有稳定组件批量迁移到新风格的授权。