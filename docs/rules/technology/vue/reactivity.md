---
id: rule:vue-reactivity
type: rule
status: active
scope:
  phases: [execute]
  activities: [implementation]
  technologies: [vue3, typescript]
  artifacts: [code]
  risks: [reactivity, side-effect, type-safety]
---

# Vue 响应式设计

设计或修改 Vue reactive state / computed / composable 时，保持响应性语义、类型边界和副作用责任一致。

## Computed 保持纯派生

`computed` getter 默认保持无副作用。网络请求、其他 state mutation、DOM 操作等外部副作用应进入 watcher、事件、生命周期或更适合的机制。

## `reactive<T>` 不强行定义返回模型

不要默认用 `reactive<T>()` 泛型参数强行定义返回对象类型，因为 nested ref unwrapping 可能使输出模型与泛型输入不同。优先使用初始化值推断、明确的变量 / interface 边界和正常 narrowing，不用 `any` / assertion 掩盖不匹配。

## Composable 返回值保持可消费的响应性

Composable 返回多个 reactive values 时，默认优先返回包含多个 refs 的普通对象，使调用方解构后仍保持 reactivity。当前 API 有明确理由返回 reactive object 时可以保留，但调用方不得无意解构后仍假设普通变量保持 property reactivity。