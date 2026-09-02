# Vue 3 + TypeScript Technology Profile 研究

**状态：** Candidate / Architecture Fit Pending  
**研究日期：** 2026-09-02  
**agentic-dev 基线：** `master@16151149ab52211e266839a110fc9a3c73415623`

## 1. 研究目标

本文为 Engineering Capability Foundation v1 的 F3 / WI-05 提供研究证据，目标是形成首个代表性的：

> **Vue 3 + TypeScript Technology Profile**

研究重点不是复制 Vue / TypeScript 官方文档，而是识别哪些当前技术语义、默认工程实践、常见误用和验证责任值得进入长期 Profile，并验证 `docs/architecture/technology-profile-contract.md` 是否足以承载真实技术能力。

本研究不建立 `vue-skill` / `typescript-skill`，不吸收 Element Plus、Spring、Gradle，也不修改 Core Method。

## 2. 当前版本基线

### 2.1 Vue

当前官方 GitHub Release API 显示：

- 最新稳定版：`vue@3.5.42`；
- 发布时间：2026-08-27；
- 当前 3.6 线仍处于 `v3.6.0-rc.6` 预发布状态。

因此本轮规范性 Profile 以 **Vue 3.5 stable line** 为当前基线，并记录精确研究锚点 `v3.5.42`。

Vue 3.6 RC、Vapor Mode 及其他仅存在于 3.6 预发布线的语义不进入 Foundation v1 Profile。

来源：

- https://github.com/vuejs/core/releases/tag/v3.5.42
- https://github.com/vuejs/core/releases/tag/v3.6.0-rc.6

### 2.2 Vue 官方文档

本轮使用的 Vue 官方文档仓库基线：

`vuejs/docs main@b75d188ab16bf83bd1f364a77dfd2315be8f3fa4`

重点页面：

- https://vuejs.org/guide/typescript/overview
- https://vuejs.org/guide/typescript/composition-api
- https://vuejs.org/api/sfc-script-setup.html
- https://vuejs.org/guide/components/props
- https://vuejs.org/guide/components/events
- https://vuejs.org/guide/components/v-model
- https://vuejs.org/guide/essentials/computed
- https://vuejs.org/guide/essentials/watchers
- https://vuejs.org/guide/essentials/template-refs
- https://vuejs.org/guide/reusability/composables

这些来源主要承担 **Official Semantics / Official Recommendation** 证据。

### 2.3 TypeScript

当前官方 GitHub Release API 显示：

- 当前稳定版：`TypeScript 7.0.2`；
- Release 更新时间：2026-08-20；
- TypeScript 7.0 正式发布于 2026-07-08。

TypeScript 7 是新的原生编译器实现，但官方说明其类型检查逻辑以兼容既有 TypeScript 语义为目标。

来源：

- https://github.com/microsoft/TypeScript/releases/tag/v7.0.2
- https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/
- https://www.typescriptlang.org/docs/handbook/2/everyday-types.html
- https://www.typescriptlang.org/docs/handbook/2/narrowing.html
- https://www.typescriptlang.org/docs/handbook/type-inference.html
- https://www.typescriptlang.org/tsconfig/strict.html

### 2.4 Vue Language Tools / `vue-tsc`

当前 Vue Language Tools 最新稳定 Release：

`v3.3.11`（2026-08-21）。

版本演进证据：

- `v3.3.7` 与 TypeScript 7.0.2 曾出现 `vue-tsc` 兼容失败；
- `v3.3.8` changelog 明确记录“upgrade to TypeScript 7 and support @typescript/typescript6”；
- 当前 `vue-tsc` README 仍声明 TypeScript `>=5.0.0`，并把自己定义为 Vue SFC 的命令行 type-check 工具。

来源：

- https://github.com/vuejs/language-tools/releases/tag/v3.3.11
- https://github.com/vuejs/language-tools/blob/master/CHANGELOG.md
- https://github.com/vuejs/language-tools/blob/master/packages/tsc/README.md
- https://github.com/vuejs/language-tools/issues/6124

这一组证据用于 **Tooling Compatibility / Freshness**，不把历史 issue 提升为 Vue 或 TypeScript 语言语义。

### 2.5 `@vue/tsconfig`

当前官方 Vue tsconfig 仓库基线：

`vuejs/tsconfig main@dc7af0b6a1e8a66239950a65423c5456ef5ba739`（0.9.1）。

其基础配置明确体现：

- `strict: true`；
- bundler 场景采用 `module: ESNext` / `moduleResolution: bundler`；
- Vue JSX 使用 `jsx: preserve` / `jsxImportSource: vue`；
- `verbatimModuleSyntax: true`；
- 由构建工具决定实际构建 target 时，不应把 TypeScript 的 `target` 误当作最终浏览器构建目标。

来源：

- https://github.com/vuejs/tsconfig
- https://github.com/vuejs/tsconfig/blob/main/tsconfig.json

这属于 Vue 官方维护的成熟工程默认，不表示所有 Existing Consumer 必须无条件迁移到完全相同配置。

## 3. Research → Profile 的 Architecture Fit 初步判断

当前证据支持将目标继续保持为 **Technology Profile**，而不是 Method / Engineering Discipline / Skill：

- 规则明显依赖 Vue 3.5、SFC、Composition API、Vue Reactivity、Vue Language Tools 和 TypeScript 版本语义；
- 它们不是跨技术栈生命周期规则，因此不属于 Core Method；
- 其中“最小实现 / existing capability reuse / diff scope”继续由 Engineering Discipline 提供上层约束；
- 当前没有独立稳定任务流程、输入 / 输出 / Stage Return，不能证明需要 Task-oriented Skill；
- Verification Profile 与 Vue / TypeScript 变更类型高度相关，适合作为同一 Profile 的组成部分。

组合 Vue 3 + TypeScript 的理由不是“二者经常一起使用”，而是本轮发现以下真实联合决策边界：

1. Vue SFC template 与 `<script setup lang="ts">` 的类型检查由 Vue Language Tools / `vue-tsc` 联合实现；
2. `defineProps` / `defineEmits` / template refs / `reactive()` 的类型语义依赖 Vue 编译器与 TypeScript 类型系统共同工作；
3. Vite 转译不等于 Vue SFC TypeScript type-check，因此验证责任天然跨 Vue tooling 与 TypeScript；
4. TypeScript 主版本变化会直接影响 Vue Language Tools 兼容性与 type-check evidence availability。

因此一个组合 Profile 有真实工程价值，但正文仍应把 Vue-specific、TypeScript-specific 和联合工具链规则分区，不能制造不存在的共同语义。

## 4. Candidate Technology Constraints

以下候选规则主要由官方语义支持。

### TC-01 SFC + Composition API 的 `<script setup>`

当项目使用 Vue SFC + Composition API，且 Consumer Authority 没有相反约束时，`<script setup>` 是 Vue 官方推荐语法。

这不是“所有 Vue 代码必须迁移到 `<script setup>`”的强制规则：

- Options API 仍是支持的 Vue API；
- Existing Consumer 的既有架构或迁移策略可以保留 Options API；
- 当前 Unit 不得为了 Profile 一致性顺带迁移无关组件。

### TC-02 Props 是单向输入

Props 属于父 → 子单向数据流。子组件不得直接修改 prop 本身。

需要修改语义时应根据当前契约选择：

- 本地 state；
- emit；
- 标准 component `v-model`；
- Consumer 已定义的共享状态机制。

Profile 不规定所有双向场景必须使用同一种机制。

### TC-03 `defineProps` / `defineEmits` declaration mode

`defineProps` / `defineEmits` 可以采用 runtime declaration 或 type declaration，但同一个声明不能同时混用两种模式。

Type-based declaration 在 TypeScript SFC 中通常更直接，但如果当前契约需要自定义 runtime validation，应保留对应 runtime responsibility，不能为了“类型更漂亮”删除运行时校验。

### TC-04 `reactive()` 泛型边界

Vue 官方不推荐使用 `reactive<T>()` 泛型参数来指定返回对象类型，因为 `reactive()` 返回类型包含 nested ref unwrapping，可能与泛型输入模型不同。

优先：

- 使用初始化值推断；
- 必要时给接收变量 / interface 建立清晰类型边界；
- 不用 assertion / `any` 强行压平不匹配。

### TC-05 computed 是派生状态

`computed` getter 应保持无副作用；不要在 computed 中发请求、修改其他状态或直接操作 DOM。

真正副作用应使用 watcher、事件、生命周期或更适合的当前机制。

### TC-06 template ref 生命周期

Vue 3.5+ 的静态 template ref 可以使用 `useTemplateRef()`；对应 DOM / component 实例在挂载前、条件卸载后可能为空。

TypeScript 代码必须反映该生命周期，不能仅为消除类型错误无证据使用 non-null assertion。

### TC-07 watcher 依赖与清理

- `watch` 只跟踪显式 source；
- `watchEffect` 在同步执行阶段自动收集依赖；异步 callback 只会追踪第一个 `await` 之前访问的依赖；
- 当副作用可能产生 stale async work、订阅或其他外部资源时，应建立 cleanup；Vue 3.5+ 可以使用 `onWatcherCleanup`，已有 `onCleanup` 入口仍可按当前代码使用。

### TC-08 Vite build 不等于 TypeScript type-check

Vue 官方明确说明 Vite dev server / bundler 对 TypeScript 是 transpilation-only，不执行 type-check。

因此：

> `vite build` 成功不能单独证明 Vue SFC / TypeScript 类型责任已经闭环。

需要类型证据时，应解析 Consumer 当前 Vue-aware type-check 机制并实际执行。

## 5. Candidate Engineering Defaults

### ED-01 保留有效类型推断

TypeScript 和 Vue 都提供较强类型推断。默认不为所有局部变量、`ref`、`computed` 人工重复声明显而易见的类型。

显式类型主要用于：

- 公共边界；
- union / nullable / external input；
- 无法可靠推断的复杂值；
- 当前代码需要稳定契约的位置。

### ED-02 不使用 `any` 作为默认逃生口

`any` 会关闭后续类型检查。对于真实未知输入，优先使用可收窄的类型（例如 `unknown` / union / runtime guard）并通过正常控制流完成 narrowing。

Existing Consumer 已经存在的局部 `any` 不要求在无关 Unit 中顺带清理。

### ED-03 新建 / 明确允许的 Vue + TS 工程优先严格类型检查

Vue 官方 `@vue/tsconfig` 使用 `strict: true`，TypeScript 6+ 也把 strict 作为默认方向。

但 Existing Consumer 是否开启或加强 strict 是项目级配置责任：

- 不在普通 Feature Unit 中因为 Profile 自动改写整个 tsconfig；
- 如果当前项目 strict=false，Profile 可以记录差异 / 风险，但是否迁移应由项目计划处理；
- TypeScript 主版本升级后必须重新检查当前显式配置，不依赖“默认值应该一样”的假设。

### ED-04 Composable 返回值默认保留可解构的 reactivity

Vue 官方 composable 约定推荐返回包含多个 refs 的普通对象，使调用方解构后仍保持 reactivity。

如果当前 API 有明确理由返回 reactive object，可以保留；但不要在调用方无意解构 reactive object 后假设 reactivity 仍然存在。

### ED-05 标准 component `v-model` 优先使用 Vue 当前能力

Vue 3.4+ 官方推荐 `defineModel()` 作为标准 component `v-model` 的实现方式。

适用条件：

- 当前确实是标准 `v-model` 契约；
- Consumer 没有兼容层 / library contract 等更具体限制。

不要仅为了使用新 API 改写已有稳定自定义 prop / emit contract。

### ED-06 `useTemplateRef` 作为 3.5+ 静态模板引用默认

在 Vue 3.5+、Composition API、静态 template ref 场景中，优先使用 `useTemplateRef()` 及 Vue Language Tools 的类型推断，而不是重复维护名称相同的 `ref(null)`。

动态组件、非 SFC、版本低于 3.5 或类型推断不足时，显式泛型 / `InstanceType` 等仍是合法路径。

### ED-07 新建 bundler-based Vue 项目优先从官方配置起点开始

对于新建、Vite/bundler-based Vue + TypeScript 项目，优先参考 `create-vue` / `@vue/tsconfig`，而不是手工拼装一套“通用 TS 最佳配置”。

Existing Consumer 的 `tsconfig`、构建工具、目标环境和 alias 仍由项目权威决定。

## 6. Candidate Known Misuse

### KM-01 build green ⇒ type safe

错误：只运行 Vite build 就宣称 TypeScript / template types 已验证。

### KM-02 直接修改 prop

错误：子组件把 prop 当本地可写 state。

### KM-03 computed 中执行副作用

错误：为了“响应式”把网络请求、DOM mutation 或其他副作用放入 computed getter。

### KM-04 watcher 异步副作用无失效处理

错误：source 快速变化时旧请求 / subscription 仍可能回写新状态，却没有 cleanup / cancellation / currentness guard。

### KM-05 `reactive<T>` + assertion 掩盖实际类型

错误：先强制泛型，再通过断言处理 Vue nested unwrapping 产生的不一致。

### KM-06 盲目解构 reactive object

错误：解构 `reactive()` object 后仍假设普通变量保持 property reactivity。

### KM-07 template ref 无条件 `!`

错误：忽略挂载 / 卸载生命周期，只为通过 type-check 使用 non-null assertion。

### KM-08 版本号“够新”就假设 `vue-tsc` 可用

错误：仅根据 `typescript` / `vue-tsc` semver 范围推断兼容性，不执行 Consumer 当前 type-check 命令。

TypeScript 7 切换原生实现后已经出现过真实工具兼容迁移，因此这一点必须以 Current Evidence 裁决。

### KM-09 Profile 自动扩张到 Element Plus

错误：遇到 Element Plus 组件时，把当前 Vue + TypeScript Profile 当成 Element Plus API 权威。

Profile 可以应用通用 Vue / TS / verification 规则，但 Element Plus-specific props、lifecycle、component behavior 必须从 Consumer 依赖和对应官方资料解析。

## 7. Verification Profile Candidate

Profile 不规定固定命令，下面只定义稳定的 **Change Type → Verification Responsibility** 映射。

### VP-01 SFC / template / props / emits type contract

通常至少需要：

- Consumer 当前 Vue-aware type-check；
- 如果改变运行时组件行为，再增加当前组件 / 集成行为验证。

只有 `tsc` 对纯 `.ts` 通过，不能自动证明 `.vue` template contract。

### VP-02 纯派生状态 / reactivity 逻辑

涉及 `computed`、state transform、composable reactivity：

- type-check 证明类型契约；
- 当前行为测试证明状态变化结果；
- 对依赖追踪 / 解构边界有风险时，测试必须覆盖 source 更新后的反应结果。

### VP-03 watcher / lifecycle / async side effect

至少考虑：

- type-check；
- 触发时机；
- stale work / cleanup；
- mount / unmount；
- 多次快速变化等当前验收差异。

仅静态检查通常不足。

### VP-04 DOM / template ref / user interaction

至少考虑：

- type-check；
- mounted / conditional unmount 行为；
- 用户可见交互时的 browser/runtime evidence；
- 视觉要求存在时的 visual evidence。

### VP-05 tsconfig / module / build integration

涉及 alias、module resolution、build config、TypeScript 主版本：

- 实际 type-check；
- 实际 build；
- 必要时运行时加载 / browser evidence；
- 不用 TypeScript 默认值代替 Consumer 的显式 tsconfig / extends 链。

### VP-06 TypeScript-only domain types

如果变化只影响纯 TS 类型且没有运行时 / SFC / build 契约：

- 当前 type-check 可以是核心证据；
- 仍需根据 Acceptance Obligation 判断是否存在需要行为验证的消费者。

### VP-07 Vue tooling compatibility failure

如果 `vue-tsc` / language server / TypeScript 组合本身无法运行：

- 工具失败不是业务 PASS；
- 不得用 `vite build` 替代必要 type-check；
- 应检查 Consumer 实际版本、lockfile、现有 scripts 和当前官方工具支持；
- 在授权范围内修复 / 升级 / pin 兼容工具，或明确返回验证缺口。

## 8. Consumer Override Boundary Candidate

Profile 进入 Consumer 后按以下顺序裁决：

1. 客观 Vue / TypeScript 语义；
2. Consumer 已确认的技术版本与 Architecture / ADR；
3. Consumer-local engineering rules；
4. Profile Engineering Defaults；
5. 普通实现偏好。

示例：

- Consumer 明确在迁移期继续使用 Options API：不得因为 Profile 推荐 `<script setup>` 就批量迁移；
- Consumer 使用 Vue 3.4：不得调用 3.5 才存在的 `useTemplateRef`；
- Consumer 使用 TypeScript 6：不得机械套用 TypeScript 7 的版本特定默认变化；
- Consumer 已有明确 type-check script：优先实际运行它，而不是用 Profile 发明 `vue-tsc` 命令；
- Consumer 没有 Vue-aware type-check，而当前 Completion 必须证明 SFC 类型：这是 verification gap，不是“Profile 已给命令所以直接假设可用”。

## 9. Candidate Targeted Eval

为了验证 Profile 而不是验证模型是否背诵 Vue 文档，场景应显式提供当前 Profile 作为隔离 Repository Authority，并测试冲突判断。

计划物化以下场景：

### C-VTS-01 — Vite build 与 type-check 分离

给定 Vite build PASS、无 Vue-aware type-check current evidence。

必须拒绝把 build 当作 SFC type-check evidence，并解析 Consumer 当前 type-check mechanism。

### C-VTS-02 — computed / watcher 职责

给定纯派生值通过 watcher 回写 state，同时存在真实 async side effect。

应把纯派生值收敛到 computed，并把副作用留在 watcher / effect；不得机械“所有 watcher 都错”。

### C-VTS-03 — Prop mutation / v-model

给定子组件直接修改 prop、当前需求是标准双向编辑。

应保持 one-way props，使用当前 Vue contract（3.4+ 可优先 `defineModel`）或明确 prop / emit；不得直接修改 prop。

### C-VTS-04 — `reactive<T>` 与 composable destructure

给定 `reactive<MyState>()` + composable 返回 reactive object 后被解构。

应分别识别泛型返回类型边界与解构 reactivity 风险，不用 `any` 解决。

### C-VTS-05 — template ref 生命周期

给定 Vue 3.5+ 静态 template ref 和 `v-if`。

应使用 / 考虑 `useTemplateRef`，同时保留 null lifecycle；不得无条件 `!`。

### C-VTS-06 — TypeScript 7 tooling compatibility

给定 TS 7.0.2、旧 `vue-tsc@3.3.7` type-check 崩溃、Vite build PASS。

应把问题识别为 tooling compatibility / verification gap，不把 build 当替代证据，也不声称“TS7 一定不支持 Vue”；需要解析当前官方工具版本和 Consumer 约束。

### C-VTS-07 — Consumer Override

给定 Consumer Architecture 明确本阶段继续 Options API。

应服从项目规则，不因为 Profile Engineering Default 扩大迁移范围。

### C-VTS-08 — Element Plus 边界

给定问题依赖某个 Element Plus-specific component prop。

应承认当前 Profile 不拥有 Element Plus API 事实，只应用 Vue / TypeScript 通用规则并要求对应权威，而不是编造组件行为。

### C-VTS-09 — Verification 按风险扩展

给定 type-check PASS，但变更包含 watcher stale request + 可见 loading 状态。

应继续要求 current runtime behavior evidence，必要时 browser / component test，而不是仅凭静态检查完成。

## 10. Eval Harness 缺口

现有 `evals/run_codex_evals.py` 明确是 Skill Runtime Eval：

- Behavior corpus 通过 `$skill-name` 显式调用 Skill；
- 隔离 workspace 默认只复制 `.agents/skills/*`；
- 当前没有非 Skill Capability 的上下文注入模式。

Technology Profile 不是 Skill。如果为了评估 Profile 新建 `vue-skill`，会违反 Engineering Capability Architecture 与 Foundation v1 范围冻结。

因此 WI-05 需要一个**最小 Eval Harness 扩展**：

- 新增独立 `capability` corpus；
- 每个场景 Fresh Codex Runtime；
- 只复制场景声明的 Profile / Discipline / fixture context；
- 不使用 `$skill-name`；
- 不让 Runtime 读取 assertions / expected behavior / 历史结果；
- 继续人工逐 assertion 语义判分；
- 不把该扩展升级为新的 Runtime Adapter / benchmark framework。

该缺口属于完成 F3 Targeted Eval 的必要基础设施，不是 Post-v1 范围扩张。

## 11. Candidate 结论

当前研究支持形成 Draft Profile，且没有发现需要修改 Core Method 或 Engineering Capability Architecture 的 Blocking 缺口。

建议 Architecture Fit：

> **一个组合 Technology Profile + 内嵌 Verification Profile + 非 Skill Capability Targeted Eval。**

建议持久化位置：

`docs/technology-profiles/vue3-typescript.md`

建议状态顺序：

```text
Research
→ Candidate
→ Architecture Fit Review
→ Draft Profile
→ Capability Targeted Eval
→ AI Review
→ Ready to Integrate
→ Human / Repository Integration Decision
```

本研究文件保持 Research 权限，不因形成 Candidate 而成为规范性 Technology Profile。