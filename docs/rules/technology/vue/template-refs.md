---
id: rule:vue-template-refs
type: rule
status: active
scope:
  phases: [execute]
  activities: [implementation]
  technologies: [vue3, typescript]
  artifacts: [vue-sfc]
  risks: [nullability, type-safety, dom-lifecycle]
---

# Vue Template Refs

处理 Vue template ref 时，API 选择、可空生命周期与 DOM 时机属于同一任务级责任。

## API 与类型推断

在 Vue 3.5+、Composition API、静态 template ref 场景中，优先利用 `useTemplateRef()` 与 Vue Language Tools 的类型推断。动态组件、低版本、非 SFC 或推断不足时，显式 `ref` / 泛型 / `InstanceType` 等仍是合法路径。

## 可空生命周期

DOM / component template ref 在挂载前可能为空，条件卸载后也可能再次为空。TypeScript 类型与实现必须反映该生命周期，不得仅为消除类型错误无证据使用 non-null assertion。

## DOM 时机

只有当前行为确实依赖 DOM 已挂载或已更新时，才增加 `nextTick`、lifecycle 或 watcher 等时机控制。选择机制由真实 trigger 与现有代码结构决定，不固定单一模式。