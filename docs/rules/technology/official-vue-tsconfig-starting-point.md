---
id: rule:official-vue-tsconfig-starting-point
type: rule
status: active
scope:
  phases: [execute]
  activities: [implementation]
  technologies: [vue3, typescript]
  artifacts: [configuration]
  risks: []
---

# Vue + TypeScript 新工程优先官方配置起点

新建 Vue + TypeScript bundler-based 工程优先参考 `create-vue` / `@vue/tsconfig`，而不是手工拼装所谓通用 TypeScript 最佳配置。既有使用方的 `tsconfig`、构建工具、target、alias 和 extends 链继续由项目 Authority 决定。