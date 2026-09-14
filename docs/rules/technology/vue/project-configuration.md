---
id: rule:vue-project-configuration
type: rule
status: active
scope:
  phases: [execute]
  activities: [implementation]
  technologies: [vue3, typescript]
  artifacts: [configuration]
  risks: []
---

# Vue + TypeScript 工程配置

新建 Vue + TypeScript bundler-based 工程优先参考 `create-vue` / `@vue/tsconfig`，而不是手工拼装所谓通用 TypeScript 最佳配置。

既有使用方的 `tsconfig`、构建工具、target、alias 和 extends 链继续由项目 Authority 决定；普通功能修改不得为了采用新工程默认值扩大配置迁移范围。