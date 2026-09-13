---
id: research:vue3-typescript
type: research
status: active
---

# Vue 3 + TypeScript 技术研究

**研究日期：** 2026-09-02  
**性质：** 非规范性 Research

## 1. 研究范围

本研究识别 Vue 3 + TypeScript 中值得长期保留的官方语义、工程默认、常见误用和验证责任。V4 已取消 monolithic Technology Profile 作为 runtime owner；当前规范语义由 `docs/rules/technology/**` 中可独立发现的最小 Rules 持有。

## 2. 研究时外部基线

研究时确认的外部锚点包括：

- Vue 稳定线 `3.5.42`；当时 `3.6.0-rc.6` 仍是预发布；
- Vue 官方 docs 与 SFC / Composition API / props / emits / v-model / computed / watchers / template refs / composables 文档；
- TypeScript `7.0.2`；
- Vue Language Tools `3.3.11`，并观察到 TypeScript 7 迁移期间 `vue-tsc` 的真实兼容变化；
- `@vue/tsconfig` 0.9.1 作为 Vue 官方维护的 bundler-based 配置参考。

这些版本只是研究成立时的证据范围，不是 Consumer 当前版本事实。实际任务必须从 Consumer 仓库重新解析版本、lockfile、scripts 与 Architecture Authority。

## 3. 长期技术结论

### SFC / component contracts

- 在 SFC + Composition API 且没有更具体 Consumer 约束时，`<script setup>` 是合理默认；不得为统一风格机械迁移既有 Options API。
- Props 是父→子单向输入；子组件不得直接修改 prop 本身。
- `defineProps` / `defineEmits` 的 runtime declaration 与 type declaration 不应在同一声明中混用；当前契约需要 runtime validation 时不能为了类型简洁删除它。
- 标准 component `v-model` 在适用 Vue 版本可使用 `defineModel()`；已有稳定自定义 prop / emit contract 不因新 API 存在而自动改写。

### Reactivity / type safety

- 不推荐用 `reactive<T>()` 强行规定返回类型；优先利用初始化值推断，并在真实边界建立明确类型。
- `computed` 表达派生状态，getter 应保持无副作用。
- Composable 返回多个 refs 时，普通对象通常更有利于调用方安全解构并保持 reactivity；不得假设解构 `reactive()` 对象后普通变量仍保持 property reactivity。
- 保留有效类型推断，不机械重复显而易见类型；公共边界、nullable/union/external input 等真实契约处再显式标注。
- `any` 不应成为默认逃生口；真实未知输入优先 `unknown` / union / runtime guard 与正常 narrowing。
- 新建或明确授权的 Vue + TS 项目可以从严格类型检查和官方 tsconfig 起点开始；Existing Consumer 是否迁移 strict 属于项目级配置责任。

### Template refs / watchers

- Vue 3.5+ 静态 template ref 可优先 `useTemplateRef()`，但 mount 前或条件卸载后仍可能为空；不得仅为消除类型错误无证据使用 non-null assertion。
- `watch` 跟踪显式 source；`watchEffect` 在同步执行阶段自动收集依赖，异步 callback 在首个 `await` 后的访问不自动纳入之前的同步依赖收集。
- 可能产生 stale async work、subscription 或其他外部资源的 watcher 应建立 cleanup / cancellation / currentness guard。

### Build / type-check boundary

- Vite build/transpilation 成功不等于 Vue SFC / TypeScript 类型检查通过。
- SFC 类型责任需要 Consumer 当前 Vue-aware type-check 机制的真实执行证据。
- TypeScript / Vue Language Tools 的 semver 看起来兼容不能替代当前工具实际运行；历史上 TypeScript 7 迁移已经出现过真实兼容缺口。

## 4. Verification responsibilities

不同 change type 需要不同证据：

- SFC/template/props/emits：至少当前 Vue-aware type-check；若改变运行时行为，再补组件/集成行为证据。
- computed/composable/reactivity：type-check + 与状态变化相关的行为验证。
- watcher/lifecycle/async side effect：除静态检查外，验证触发时机、stale work、cleanup、mount/unmount 等真实行为。
- DOM/template ref/user interaction：根据风险增加 runtime/browser evidence；存在 visual-fidelity claim 时需要视觉证据。
- tsconfig/module/build integration：实际 type-check + build，必要时运行时加载证据；不得用默认值猜 Consumer 的显式配置。
- tooling compatibility failure：属于 verification gap，不得用 build PASS 代替必需的 type-check。

## 5. Consumer override boundary

实际裁决顺序保持：

1. 客观 Vue / TypeScript 语义；
2. Consumer 当前版本与 Architecture / ADR；
3. Consumer-local Rules；
4. 通用工程默认；
5. 普通实现偏好。

因此：Vue 3.4 Consumer 不得使用 3.5-only API；既有 Options API migration plan 优先于通用 `<script setup>` 默认；Element Plus 等第三方组件事实必须从相应 Consumer dependency / 官方资料解析，不能由 Vue/TS Rule 猜测。

## 6. V4 当前落点

本研究中的规范性技术语义已经拆分到独立 Rules，包括：

- props / emits / `script setup` / `defineModel`；
- `reactive` / computed / composable / watcher；
- template ref lifecycle / `useTemplateRef`；
- type inference / `any` / strict / official tsconfig；
- build-vs-typecheck；
- risk-based browser visual verification。

目录只服务人类组织；实际适用性由每个 Rule 自己的 Front Matter 和 Rule Discovery 决定。

## 7. 结论

Vue 3 + TypeScript 的长期价值不是一份每次整体加载的大 Profile，而是一组可以按具体 technology/artifact/risk signals 独立发现的 Rules。版本与官方证据继续保留在本 Research；Consumer 当前事实必须在实际仓库中重新确认。