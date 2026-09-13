---
id: rule:vue-reactive-generic-boundary
type: rule
status: active
scope:
  phases: [execute]
  activities: [implementation]
  technologies: [vue3, typescript]
  artifacts: [code]
  risks: [type-safety, reactivity]
---

# Vue `reactive<T>` 边界

不要默认用 `reactive<T>()` 泛型参数强行定义返回对象类型，因为 nested ref unwrapping 可能使输出模型与泛型输入不同。优先使用初始化值推断、明确的变量 / interface 边界和正常 narrowing，不用 `any` / assertion 掩盖不匹配。