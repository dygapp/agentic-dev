---
id: method:model-collaboration-adoption
type: method
status: active
---

# Model Collaboration Adoption Method

## 1. 目标与适用范围

本 Method 用于一个 Repository **显式建立或首次启用 Model Collaboration local capability instance**。

它不替代 `method:ai-development`，也不要求 Consumer 必须首次采用整个 `agentic-dev`。一个已经长期运行的 Consumer 也可以独立进入本 Method，为当前 Repository 增加可选多模型协作能力。

它也不同于 `method:consumer-upgrade`：如果只是因为新的 upstream baseline 改变了已经采用的协作 capability，先按 Consumer Upgrade 评估 semantic delta；如果目标是第一次建立 / 启用 collaboration instance，则使用本 Method。

核心原则：**能力语义来自 reusable Architecture，运行实例属于 Consumer local Authority。**

## 2. 生命周期

```text
Restore Consumer Authority
→ Detect Runtime Capabilities
→ Select Collaboration Strategy
→ Project Collaboration Capability
→ Establish Local Collaboration Instance
→ Validate Collaboration
→ Enable / Fallback
→ Close Adoption
```

本 Method 的阶段表示 adoption 工作状态，不是普通软件开发阶段，也不自动授予产品 Execute、merge、release 或 deploy 权限。

## 3. Restore Consumer Authority

先恢复目标 Repository 自身当前事实、Project Knowledge、Repository Authority、当前 Method / Architecture / Skills / Rules、现有 Agent/runtime 配置、当前工作状态与允许修改范围。

如果当前 Repository 已采用 `agentic-dev`，读取其 recorded evaluated / adopted baseline 与 local adaptations；如果尚未采用，不得为了启用协作而顺带复制整个 upstream capability tree。

必须确认：

- 谁拥有 current Project Capability Profile 或等价 local instance Authority；
- 是否已经存在 model / agent routing 配置；
- 是否有共享写入、外部操作、review 或安全 policy；
- 当前是否存在不允许被配置变更打断的 active lifecycle。

退出条件：local canonical owners、允许变更边界与当前协作状态明确。

## 4. Detect Runtime Capabilities

对实际运行平台执行当前能力探测，而不是仅根据文档或静态配置假设支持。

至少判断：

- 是否支持子 Agent / subagent / thread；
- 是否允许每个 Agent 选择独立 model / reasoning effort；
- read-only / workspace-write / external-operation 等权限是否可隔离；
- concurrency / thread 上限；
- project-scoped configuration 是否真实加载；
- requested model 是否当前可用；
- child thread / child result 是否可观察；
- actual runtime model / reasoning effort 是否可观察；
- usage / token / time 等指标可观察到什么程度。

静态配置 parse PASS 不能替代真实 runtime smoke。若平台在关键 capability 上不可观察，必须记录限制；若协作线程本身无法验证建立，本 Method 不得继续把多模型状态标记为 enabled。

退出条件：当前 runtime capability matrix 有当前证据支持，unknown 项明确。

## 5. Select Collaboration Strategy

依据真实平台能力、任务类型、风险和成本目标选择 local strategy。至少允许：

- `disabled`：不启用协作；
- `basic`：deterministic tooling + bounded low-cost/read-only exploration + Primary Agent；
- `reviewed`：在 basic 之上增加独立 review；
- Consumer 自定义 strategy：只要不违反 `architecture:model-collaboration` 的不变量。

把抽象 capability tiers 映射到 Consumer 当前真实模型：

```text
low-cost capability → local model / effort
capable reasoning → local model / effort
high-capability reasoning → local model / effort
```

不得把 upstream 示例中的具体模型名当成必须复制的策略。

退出条件：strategy、tier mapping、触发条件、fallback 与预期优化目标明确。

## 6. Project Collaboration Capability

把已选择的 reusable capability 投射到 Consumer-local canonical owners，而不是复制 upstream Project state。

逐项判断：

- Collaboration Architecture：adopt / adapt / reject；
- runtime configuration：建立 Consumer-local instance；
- Consumer-local Rules：只为真实 conditional policy 建立或适配；
- Repository Authority / bootstrap：只在 ordinary runtime 需要稳定入口时增加 locator；
- Human Guide / runbook：按 Consumer 需要建立；
- Evidence / validation assets：放入 Consumer 自己的验证 owner。

特别区分：

- `single-writer`、Authority-preserving handoff 等 reusable invariant 属于 Collaboration Architecture；
- “本 Consumer 的 production external write 只能由 primary agent 执行”等局部 policy 可以成为 Consumer-local Rule；
- `fast_explorer = <concrete-model>` 之类映射只属于 local runtime configuration / capability instance。

不得把同一语义复制到 Architecture、Rule、Project Profile 和配置说明中形成多份 current owner。

退出条件：所有 accepted capability 都有明确 local owner，未采用内容有明确 disposition。

## 7. Establish Local Collaboration Instance

在 Consumer Project Capability Profile 或等价 Authority 中建立薄的 collaboration instance。至少记录：

- status：disabled / enabled / conditional；
- runtime / provider；
- local configuration locator；
- capability tier mapping locator；
- delegation / writer ownership locator；
- validation evidence locator；
- single-agent fallback locator。

Project Profile 只保存当前 instance pointer / selection，不复制 `architecture:model-collaboration` 正文、完整模型说明或 Rule inventory。

ordinary runtime 必须能够只依赖 Consumer Repository 恢复这项能力；不得要求在线访问 `agentic-dev` 才知道当前模型、配置或协作策略。

退出条件：local instance 可从 Fresh Context 独立恢复。

## 8. Validate Collaboration

验证必须与实际启用的 strategy 匹配。最低验证包含：

1. **configuration validation**：配置格式与当前 runtime 可接受；
2. **delegation smoke**：至少一个隔离的只读 child task 真实建立并产生可观察终态；
3. **authority fidelity**：child handoff 不把摘要替代 canonical Authority；
4. **single-writer**：启用写入协作时，共享写入面只有一个 active writer；
5. **review isolation**：启用独立 review 时，reviewer 不以实施者 completion claim 为事实前提；
6. **evidence claim**：requested model 与 observed runtime identity 分离，无法观察则明确 unknown；
7. **fallback**：禁用 collaboration 后普通单 Agent 路径仍可运行；
8. **upstream decoupling**：Consumer ordinary runtime 不读取 upstream current state。

如果要声称效率收益，应与相同目标和可比较上下文的单 Agent baseline 对照。质量不得低于 baseline；至少明确比较 high-capability token / context、total token、wall time、rework 与 residual findings 中实际可观察的指标。

一次 smoke 只能证明链路可用，不能证明长期成本收益。

退出条件：启用所依赖的 runtime claims 有当前 Evidence；失败或不可验证项已经触发 fallback 或显式限制。

## 9. Enable / Fallback

只有 Validate Collaboration 通过后，才能把 Consumer local instance 标记为 enabled / conditional。

启用必须保持：

- single-agent fallback 可执行；
- collaboration failure 不改变产品目标或 Method Gate；
- 子 Agent 不自动获得 merge / release / deploy / destructive external-operation 权限；
- high-capability escalation 仍由 Evidence / local policy 触发，不成为默认路径。

如果关键 smoke 失败、线程不可观察或 Authority / writer ownership 无法保证，保持 disabled 或 conditional，并继续使用单 Agent ordinary runtime。不得为了完成 adoption 而把失败证据解释成成功。

退出条件：启用状态与 fallback 状态准确反映真实 runtime。

## 10. Close Adoption

记录：

- exact evaluated upstream capability baseline（如适用）；
- Consumer-local collaboration status；
- runtime / strategy / tier mapping 的 local owner；
- adopted / adapted / rejected collaboration semantics；
- 当前 validation Evidence；
- 已知 observability limitation；
- fallback path。

完成条件：Consumer 可以在 Fresh Context 中仅依赖 local state 恢复协作能力，协作启用状态有当前 Evidence 支撑，不存在未声明的 upstream runtime dependency，也没有把 requested configuration 冒充 observed runtime fact。

完成本 Method 不产生未来自动升级义务。upstream capability 后续变化只有通过显式 Consumer Upgrade 或新的 local adoption decision 才改变 Consumer state。