# Vue 3 + TypeScript Technology Profile

**Profile ID：** `vue3-typescript`  
**状态：** Draft v0.1 — WI-05 Targeted Eval Pending  
**性质：** Technology Profile + Verification Profile 规范性 Draft

## 1. 目的与适用范围

本文定义 `agentic-dev` 对 **Vue 3 + TypeScript** 工程开发的首个代表性 Technology Profile Draft。

当前研究与验证锚点：

- Vue：稳定线 `3.5.x`，精确研究版本 `3.5.42`；
- TypeScript：精确研究版本 `7.0.2`；
- Vue Language Tools / `vue-tsc`：精确研究版本 `3.3.11`；
- Vue 官方文档：`vuejs/docs main@b75d188ab16bf83bd1f364a77dfd2315be8f3fa4`；
- `@vue/tsconfig`：`vuejs/tsconfig main@dc7af0b6a1e8a66239950a65423c5456ef5ba739`。

本文适合 Vue 3 SFC、Composition API、TypeScript、Vue-aware type checking 等场景。它不要求 Existing Consumer 把实际依赖升级到上述精确版本，而是用这些版本建立当前可追溯的证据基线。

明确不覆盖：

- Vue 3.6 RC / Vapor Mode；
- Element Plus 或其他组件库 API；
- Nuxt 等上层框架特有语义；
- Consumer 的目录、构建脚本、测试框架、浏览器工具、CI 命令；
- Options API 到 Composition API 的强制迁移；
- 新的 Task-oriented Skill。

## 2. Evidence Baseline

### 2.1 Vue

- Vue stable release：`v3.5.42`，2026-08-27；
- Vue 3.6 当前仍为 `v3.6.0-rc.6` 预发布线；
- Vue 官方文档主线：`vuejs/docs main@b75d188ab16bf83bd1f364a77dfd2315be8f3fa4`。

主要官方语义来源：

- TypeScript with Composition API；
- `<script setup>`；
- Props / Component Events / Component `v-model`；
- Computed / Watchers / Template Refs；
- Composables。

### 2.2 TypeScript

- TypeScript stable release：`7.0.2`；
- TypeScript 7.0 正式发布：2026-07-08；
- 本 Profile 只把 TS7-specific 变化应用于明确标记的版本边界，不把所有通用 TypeScript 规则错误限制为 TS7 独有。

主要官方语义来源：

- TypeScript Handbook；
- Narrowing / Type Inference；
- `strict` / `noImplicitAny` 等 TSConfig 语义；
- TypeScript 7.0 官方发布说明。

### 2.3 Vue tooling

- Vue Language Tools：`v3.3.11`；
- `vue-tsc` 是 Vue SFC 的 CLI type-check 工具；
- TypeScript 7 切换期间出现过真实工具兼容迁移，说明“版本看起来满足范围”不能替代当前实际 type-check evidence。

### 2.4 Vue 官方工程配置

`@vue/tsconfig` 当前基线体现的官方维护默认包括：

- `strict: true`；
- bundler-based 场景使用 ES module / bundler resolution；
- Vue JSX 采用 `jsx: preserve` / `jsxImportSource: vue`；
- `verbatimModuleSyntax: true`；
- TypeScript `target` 不应被误解为 Vite 最终构建 target。

这些是新建 / 明确允许调整工程时的重要默认参考，不自动覆盖 Existing Consumer 当前 tsconfig。

## 3. Architecture Fit

本 Profile 属于 Technology Profile，而不是 Core Method、Engineering Discipline 或 Task-oriented Skill：

- 规则依赖 Vue 3.5、SFC、Vue reactivity、Vue macros、Vue Language Tools 和 TypeScript 语义；
- 跨技术栈的复杂度正当性、已有能力复用和 diff scope 继续服从 `engineering-disciplines.md`；
- 当前没有独立稳定任务入口、输出、Stage Return 或调度价值，因此新增 Skill 没有职责证据；
- Verification Profile 与 Vue / TypeScript 的技术变更类型高度耦合，作为本 Profile 的组成部分维护。

Vue 与 TypeScript 组合的真实联合边界包括：

1. `.vue` template 与 `<script setup lang="ts">` 的类型检查；
2. `defineProps` / `defineEmits` / template refs / reactivity API 与 TypeScript 类型推断的交互；
3. Vite 转译与 Vue-aware type-check 的职责分离；
4. TypeScript 主版本变化对 Vue Language Tools 和 type-check evidence 的影响。

Vue-specific、TypeScript-specific 和联合工具链规则仍分别表达，不能为了组合制造不存在的共同语义。

## 4. Technology Constraints

### TC-01 `<script setup>` 的适用语义

在 Vue SFC + Composition API 场景中，`<script setup>` 是 Vue 官方推荐语法。

这不意味着：

- Options API 已不受支持；
- Existing Consumer 必须批量迁移；
- 当前 Unit 可以顺带改写无关组件。

Consumer 已确认的迁移策略或架构约束优先于本条 Engineering Default 的使用方式。

### TC-02 Props 是单向输入

Props 遵循父 → 子单向数据流。子组件不得直接修改 prop 本身。

需要可编辑语义时，根据当前契约选择本地 state、emit、标准 component `v-model` 或 Consumer 已定义的共享状态机制。

### TC-03 Props / Emits declaration mode

在 TypeScript SFC 中，`defineProps` / `defineEmits` 可以使用 runtime declaration 或 type declaration，但同一声明不能同时混用两种模式。

如果当前契约确实需要 runtime validation，不得为了类型表达更简洁而删除运行时责任。

### TC-04 `reactive<T>()` 泛型边界

不使用 `reactive<T>()` 泛型参数来强行定义返回对象类型。Vue 的 nested ref unwrapping 可能使返回类型与输入泛型模型不同。

优先使用：

- 初始化值推断；
- 明确变量 / interface 边界；
- 正常 narrowing。

不得通过 `any` 或 assertion 掩盖真实不匹配。

### TC-05 Computed 是派生状态

`computed` getter 应保持无副作用。网络请求、其他 state mutation、DOM 操作或其他外部副作用应进入 watcher、事件、生命周期或更适合的当前机制。

### TC-06 Template ref 生命周期

Vue 3.5+ 静态 template ref 可以使用 `useTemplateRef()`。对应 DOM / component 实例：

- 挂载前可能为空；
- `v-if` 等条件卸载后可能再次为空。

类型与实现必须反映这个生命周期，不得仅为消除类型错误无证据使用 non-null assertion。

### TC-07 Watcher 依赖与清理

- `watch` 追踪显式 source；
- `watchEffect` 在同步执行阶段自动收集依赖；异步 callback 只追踪第一个 `await` 之前访问的依赖；
- 可能产生 stale async work、subscription 或其他外部资源的副作用应建立失效 / cleanup 责任；Vue 3.5+ 可以使用 `onWatcherCleanup`，现有 `onCleanup` 入口仍可按当前代码使用。

### TC-08 Vite build 不等于 Vue SFC type-check

Vite 对 TypeScript 的构建职责是 transpilation，不负责完整 type checking。

因此：

> `vite build` 成功不能单独证明 Vue SFC / TypeScript 类型责任已经闭环。

需要类型证据时，应解析并实际执行 Consumer 当前 Vue-aware type-check 机制。

## 5. Engineering Defaults

### ED-01 保留有效类型推断

默认不为所有局部变量、`ref`、`computed` 重复声明显而易见的类型。

显式类型优先用于：

- 公共 API / component contract；
- union / nullable / external input；
- 无法可靠推断的复杂值；
- 当前代码需要稳定边界的位置。

### ED-02 不把 `any` 当默认逃生口

对真实未知输入，优先使用可收窄类型（如 `unknown`、union、runtime guard）并通过正常控制流 narrowing。

Existing Consumer 已存在的无关 `any` 不因此进入当前 Unit cleanup。

### ED-03 新建 / 明确允许调整的工程优先严格类型检查

Vue 官方维护的 `@vue/tsconfig` 使用 `strict: true`。新建或明确允许调整的 Vue + TS 工程默认优先保持严格类型检查。

Existing Consumer 是否开启、加强或迁移 strict 属于项目配置责任：普通 Feature Unit 不得为了 Profile 自动改写整个 tsconfig。

TypeScript 主版本变化后必须重新读取 Consumer 显式配置，不依赖默认值假设。

### ED-04 Composable 返回值优先保持可解构 reactivity

一个 composable 返回多个 reactive values 时，默认优先返回包含多个 refs 的普通对象，使调用方解构后仍保持 reactivity。

当前 API 有明确理由返回 reactive object 时可以保留，但调用方不得无意解构后仍假设普通变量保持 property reactivity。

### ED-05 标准 component `v-model` 优先复用当前 Vue 能力

Vue 3.4+ 对标准 component `v-model` 推荐 `defineModel()`。

只在当前确实是标准 `v-model` contract 且 Consumer 没有更具体兼容 / library contract 时采用。不得仅为了使用新 API 改写已有稳定自定义 prop / emit contract。

### ED-06 Vue 3.5+ 静态 template ref 优先 `useTemplateRef`

在 Vue 3.5+、Composition API、静态 template ref 场景中，优先利用 `useTemplateRef()` 与 Vue Language Tools 的类型推断。

动态组件、低于 3.5、非 SFC 或推断不足时，显式 `ref` / 泛型 / `InstanceType` 等仍是合法路径。

### ED-07 新建 bundler-based Vue 工程优先官方起点

新建 Vue + TypeScript bundler-based 工程优先参考 `create-vue` / `@vue/tsconfig`，而不是手工拼装所谓“通用 TypeScript 最佳配置”。

Existing Consumer 的 tsconfig、构建工具、target、alias 和 extends 链继续由项目权威决定。

## 6. Known Misuse / Avoid

### KM-01 Build green ⇒ type safe

错误：只运行 Vite build 就宣称 Vue SFC / TypeScript types 已验证。

### KM-02 直接修改 prop

错误：子组件把 prop 当作本地可写 state。

### KM-03 Computed 中执行副作用

错误：为了“响应式”把网络请求、DOM mutation 或其他副作用放入 computed getter。

### KM-04 异步 watcher 没有失效责任

错误：source 快速变化时旧请求 / subscription 仍可能回写新状态，却没有 cleanup、cancellation 或 currentness guard。

### KM-05 `reactive<T>` + assertion 掩盖类型问题

错误：用泛型强行定义 `reactive()` 返回类型，再通过 assertion / `any` 消除 nested unwrapping 带来的不一致。

### KM-06 无意解构 reactive object

错误：解构 `reactive()` object 后仍假设普通变量保留 property reactivity。

### KM-07 Template ref 无条件 `!`

错误：忽略 mount / conditional unmount 生命周期，只为通过 type-check 使用 non-null assertion。

### KM-08 仅靠版本号假设 `vue-tsc` 兼容

错误：只根据 semver 或“最新版”推断 TypeScript / Vue Language Tools 可用性，而不运行 Consumer 当前 type-check。

### KM-09 越权解释 Element Plus

错误：把本 Profile 当成 Element Plus component props、events、lifecycle 或 behavior 的 Authority。

遇到组件库特有事实时，本 Profile只提供通用 Vue / TypeScript / verification 规则；具体组件语义必须从 Consumer 依赖和相应权威解析。

## 7. Capability Reuse & Extension Boundary

优先检查并复用 Vue / TypeScript 当前已经提供的能力，例如：

- component props / emits / `v-model`；
- Composition API / composables；
- computed / watcher / lifecycle；
- template refs；
- TypeScript inference / narrowing；
- Vue-aware type checking；
- 官方维护 tsconfig defaults。

但“框架已有能力”不是绝对禁止自有实现：当前功能、安全、性能、可观察性、生命周期或公共契约存在真实不匹配时，可以基于当前证据保留项目自有实现或薄适配。

不得为了复用：

- 扩大依赖面；
- 改变产品行为；
- 覆盖 Consumer Architecture / ADR；
- 顺带迁移无关代码。

## 8. Consumer Override Boundary

Profile 是默认工程基线，不是 Consumer 的最终项目事实。

裁决顺序：

1. 当前客观 Vue / TypeScript 技术语义；
2. Consumer 已确认的技术版本与 Architecture / ADR；
3. Consumer-local engineering rules；
4. 本 Profile Engineering Defaults；
5. 普通实现偏好。

典型边界：

- Consumer 当前继续使用 Options API：不得因为 ED-01 / `<script setup>` 推荐而批量迁移；
- Consumer 使用 Vue 3.4：不得使用 3.5 才存在的 `useTemplateRef()`；
- Consumer 使用 TypeScript 6：不得机械套用 TS7 版本特定规则；
- Consumer 已有 type-check script：优先实际运行它，不凭 Profile 发明替代命令；
- Consumer 没有 Vue-aware type-check，而 Completion 必须证明 SFC 类型：这是 Verification Gap，不是 Profile 自动授予完成证据。

普通项目偏好可以覆盖 Engineering Default，但不能把客观技术语义改写为错误事实。

## 9. Verification Profile

本节只定义 **Change Type → Verification Responsibility**，具体命令从 Consumer Repository Authority 解析。

### VP-01 SFC / template / props / emits 类型契约

通常至少需要：

- Consumer 当前 Vue-aware type-check；
- 若同时改变 runtime component behavior，再增加当前行为验证。

纯 `tsc` 对 `.ts` 文件通过不能自动证明 `.vue` template contract。

### VP-02 派生状态 / reactivity logic

涉及 computed、state transform、composable reactivity：

- type-check 证明类型契约；
- 当前行为测试证明状态变化结果；
- 存在依赖追踪 / 解构风险时，测试应覆盖 source 更新后的响应。

### VP-03 Watcher / lifecycle / async side effect

至少考虑：

- type-check；
- 触发时机；
- stale work / cleanup；
- mount / unmount；
- 当前验收涉及的快速连续变化。

静态检查通常不足。

### VP-04 DOM / template ref / user interaction

至少考虑：

- type-check；
- mounted / conditional unmount；
- 用户可见交互的 runtime / browser evidence；
- 有视觉验收义务时的 visual evidence。

### VP-05 tsconfig / module / build integration

涉及 alias、module resolution、build config、TypeScript 主版本：

- 实际 type-check；
- 实际 build；
- 必要时 runtime / browser evidence；
- 读取 Consumer 显式 tsconfig / extends 链，不用默认值代替项目事实。

### VP-06 TypeScript-only 类型变化

如果变化只影响纯 TS 类型且没有 runtime / SFC / build obligation：

- 当前 type-check 可以作为核心证据；
- 仍按 Acceptance Obligation 判断消费者是否需要行为验证。

### VP-07 Vue tooling compatibility failure

如果 `vue-tsc` / language tools / TypeScript 组合本身无法运行：

- 工具失败不是业务 PASS；
- 不用 `vite build` 替代必要 type-check；
- 检查 Consumer 实际版本、lockfile、scripts 和当前官方工具支持；
- 在授权范围内修复、升级或 pin，或者明确返回验证缺口。

### Verification Risk Escalation

出现以下风险时按需扩大验证：

- 公共 component contract；
- watcher / lifecycle / async race；
- 多入口 / 多状态交互；
- 用户可见 DOM / visual behavior；
- build / module resolution / TypeScript major change；
- compatibility / performance / security-sensitive path。

不为了形式完整机械运行所有验证层。

## 10. Targeted Eval Gate

本 Draft 在正式集成前必须通过 Fresh Runtime Capability Targeted Eval：

- `C-VTS-01` — Vite build 与 type-check 分离；
- `C-VTS-02` — computed / watcher 职责；
- `C-VTS-03` — prop mutation / standard v-model；
- `C-VTS-04` — `reactive<T>` 与 composable destructure；
- `C-VTS-05` — template ref 生命周期；
- `C-VTS-06` — TypeScript 7 tooling compatibility；
- `C-VTS-07` — Consumer Override；
- `C-VTS-08` — Element Plus Authority Boundary；
- `C-VTS-09` — 风险驱动验证扩展。

每个场景必须：

- 独立 Fresh Runtime；
- 只读取当前 Profile 和场景材料；
- 不读取 expected behavior / assertions / 历史结果；
- 逐 assertion 语义判分；
- 失败后修订 Draft，并用新的 Fresh Runtime 重新验证受影响场景。

在该门禁完成前，状态保持：

`Draft v0.1 — WI-05 Targeted Eval Pending`

## 11. Lifecycle

- **Producer：** 当前 `agentic-dev` Repository Authority 授权的 Technology Profile 维护职责；
- **Trigger：** Foundation v1 F2 已集成 Technology Profile Contract，并冻结首个代表性 Vue 3 + TypeScript Profile；
- **Consumer：** 执行 Vue / TypeScript 工作的 Agent、`execute-unit` 的技术上下文、未来适用 Task-oriented Skill、Foundation v1 Existing Consumer Adoption；
- **Persistence：** 实际集成后，以 `docs/technology-profiles/vue3-typescript.md` 作为当前唯一 Profile 入口；Research 只保留证据，不竞争规范性权威；
- **Update：** Vue / TypeScript / Vue Language Tools 版本变化、官方语义变化、Targeted Eval、Consumer Adoption 或上游 Contract 变化触发重新检查；
- **Supersede：** 新版本必须明确取代当前 Baseline；历史版本可以追溯，但只能有一个当前有效入口；
- **Escalation：** 如果修订要求改变 Core Method、Engineering Capability Architecture、Consumer Architecture、公共难逆契约或安全 / 隐私高风险默认，返回对应更高权威处理。

## 12. Non-goals

本文不定义：

- Vue / TypeScript 完整 API 手册；
- Element Plus component API；
- Nuxt、Pinia、Router、Vitest、Playwright 的完整规则；
- 所有项目统一 lint / test / build 命令；
- 所有组件必须采用 `<script setup>`；
- 所有 Existing Consumer 必须升级 Vue / TypeScript；
- `vue-skill` / `typescript-skill`；
- Foundation v1 的第二个 Technology Profile。