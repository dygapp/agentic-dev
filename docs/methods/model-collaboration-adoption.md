---
id: method:model-collaboration-adoption
type: method
status: active
---

# Model Collaboration Adoption Method

## 1. 目标与适用范围

本 Method 用于一个 Repository 在**已经接受 Model Collaboration reusable semantics** 后，显式建立、配置、验证并首次启用自己的 Model Collaboration local capability instance。

它不替代 `method:ai-development`，也不拥有 upstream capability baseline 的评估 / 接受责任：

- Consumer 首次采用 `agentic-dev` 时，由 `method:consumer-adoption` 决定是否把 `architecture:model-collaboration`、本 Method 与其他相关 capability 接受 / 适配到 local Authority；
- Existing Consumer 因新的 upstream baseline 第一次获得或改变 Model Collaboration semantics 时，由 `method:consumer-upgrade` 评估 semantic delta 并决定 retain / adopt / adapt / replace / reject；
- 只有这些 reusable semantics 已经进入 Consumer-local canonical owner 后，才进入本 Method 建立 runtime instance。

两类工作可以在同一次整体变更中连续发生，但必须保持 Gate 与 semantic owner 清楚。本 Method 不得绕过 Consumer Adoption / Upgrade，从未评估的 upstream baseline 直接复制 Architecture、Method、Rule 或配置。

核心原则：**upstream semantic acceptance 与 local runtime activation 分离。** 前者由 Consumer Adoption / Upgrade 或目标 Repository 等价 Authority 负责；本 Method 只拥有后者。

## 2. 生命周期

```text
Restore Consumer Authority
→ Confirm Accepted Collaboration Semantics
→ Detect Runtime Capabilities
→ Select Collaboration Strategy
→ Local Capability Projection
→ Establish Local Collaboration Instance
→ Validate Collaboration
→ Enable / Fallback
→ Close Adoption
```

本 Method 的阶段表示 collaboration instance adoption 工作状态，不是普通软件开发阶段，也不自动授予产品 Execute、merge、release 或 deploy 权限。

## 3. Restore Consumer Authority

先恢复目标 Repository 自身当前事实、Project Knowledge、Repository Authority、当前 Method / Architecture / Skills / Rules、现有 Agent/runtime 配置、当前工作状态与允许修改范围。

必须确认：

- 谁拥有 current Project Capability Profile 或等价 local instance Authority；
- 是否已经存在 model / agent routing 配置；
- 是否有共享写入、外部操作、review 或安全 policy；
- 当前是否存在不允许被配置变更打断的 active lifecycle；
- 当前 local Authority 从哪里记录已接受的 Model Collaboration semantics 与 provenance。

不得从 upstream Project state、Guide、历史聊天或旧实验分支推断 Consumer 已经接受这项 capability。

退出条件：local canonical owners、允许变更边界与当前协作状态明确。

## 4. Confirm Accepted Collaboration Semantics

确认 Consumer-local Authority 已经拥有本次 runtime activation 所依赖的 reusable semantics，至少包括：

- Model Collaboration Architecture 或经 Consumer 明确适配后的等价 canonical owner；
- 本 Method 自身或 Consumer-local 等价 adoption process；
- 与当前 activation 直接相关、已被 Consumer 接受的 Rule / Tool contract（如有）；
- 可追溯的 upstream provenance 或 local-origin 说明。

如果缺少这些语义，或当前只有“upstream 有一个新 capability”的事实：

- 首次整体采用返回 `method:consumer-adoption`；
- Existing Consumer 的 upstream delta 返回 `method:consumer-upgrade`；
- 非 `agentic-dev` Consumer 使用其等价 Repository Authority 流程先完成 semantic acceptance。

本阶段不得为了继续运行而临时从 upstream 文件树复制未评估语义。

退出条件：runtime activation 的规范输入已经是 Consumer-local current Authority，而不是未决 upstream candidate。

## 5. Detect Runtime Capabilities

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

## 6. Select Collaboration Strategy

依据真实平台能力、任务类型、风险和成本目标选择 local strategy。至少允许：

- `disabled`：不启用协作；
- `basic`：deterministic tooling + bounded low-cost/read-only exploration + Primary Agent；
- `reviewed`：在 basic 之上增加独立 review；
- Consumer 自定义 strategy：只要不违反已接受的 Model Collaboration Architecture 不变量。

把抽象 capability tiers 映射到 Consumer 当前真实模型：

```text
low-cost capability → local model / effort
capable reasoning → local model / effort
high-capability reasoning → local model / effort
```

不得把 upstream 示例中的具体模型名当成必须复制的策略。

退出条件：strategy、tier mapping、触发条件、fallback 与预期优化目标明确。

## 7. Local Capability Projection

把**已经接受的** reusable collaboration semantics 投射到 Consumer-local runtime owners，而不是在本阶段重新决定 upstream capability 是否应 adopt / adapt。

根据本地策略建立或更新：

- runtime configuration 与 agent profiles；
- Consumer-local Rules：只为真实 conditional policy 建立或适配；
- Repository Authority / bootstrap：只在 ordinary runtime 需要稳定入口时增加 locator；
- Human Guide / runbook：按 Consumer 需要建立；
- Evidence / validation assets：放入 Consumer 自己的验证 owner。

特别区分：

- `single-writer`、Authority-preserving handoff 等已接受 reusable invariant 属于 Collaboration Architecture canonical owner；
- “本 Consumer 的 production external write 只能由 primary agent 执行”等局部 policy 可以成为 Consumer-local Rule；
- `fast_explorer = <concrete-model>` 之类映射只属于 local runtime configuration / capability instance。

如果 projection 过程中发现必须改变已接受的 reusable semantics，而不是单纯建立 local instance，则返回拥有 semantic acceptance 的 Consumer Adoption / Upgrade / local Authority，不在本阶段静默改写 Architecture。

退出条件：需要实例化的 local config / policy / evidence owners 明确，且没有第二套 capability semantic owner。

## 8. Establish Local Collaboration Instance

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

## 9. Validate Collaboration

验证必须与实际启用的 strategy 匹配。最低验证包含：

1. **configuration validation**：配置格式与当前 runtime 可接受；
2. **delegation smoke**：至少一个隔离的只读 child task 真实建立并产生可观察终态；
3. **authority fidelity**：child handoff 不把摘要替代 canonical Authority；
4. **single-writer**：启用写入协作时，共享写入面只有一个 active writer；
5. **review isolation**：启用独立 review 时，reviewer 不以实施者 completion claim 为事实前提；
6. **evidence claim**：requested model 与 observed runtime identity 分离，无法观察则明确 unknown；
7. **fallback**：禁用 collaboration 后普通单 Agent 路径仍可运行；
8. **upstream decoupling**：Consumer ordinary runtime 不读取 upstream current state。

如果要声称 efficiency / preferred-default value，应与相同目标和可比较上下文的单 Agent baseline 对照。质量不得低于 baseline；至少明确比较 high-capability token / context、total token、wall time、rework 与 residual findings 中实际可观察的指标。

一次 smoke 只能证明链路可用，不能证明长期成本收益。

退出条件：准备启用的每个 strategy / role path 所依赖的 runtime claims 都有当前 Evidence；失败或不可验证路径已经被排除、降级或进入 fallback。

## 10. Enable / Fallback

启用状态必须精确对应已经验证的范围：

- `enabled`：所选 strategy 的所有必需 runtime / Authority / writer / Evidence 检查均通过；
- `conditional`：只启用一个明确缩减且其自身必需检查全部通过的子策略；未验证 / 失败的 role path 必须保持 disabled，并记录触发条件与 fallback；
- `disabled`：不存在可安全启用的 child-based strategy，继续使用单 Agent ordinary runtime。

如果 delegation smoke 失败或无法确认 child thread 建立，则任何依赖 child Agent 的 path 都不能以 `conditional` 名义继续使用；只能禁用该 path 或退回已经独立验证的更小策略。

无论状态如何，都必须保持：

- single-agent fallback 可执行；
- collaboration failure 不改变产品目标或 Method Gate；
- 子 Agent 不自动获得 merge / release / deploy / destructive external-operation 权限；
- high-capability escalation 仍由 Evidence / local policy 触发，不成为默认路径。

退出条件：local instance status 与真实验证范围一致，没有把部分 / 失败 Evidence 扩张成完整 collaboration claim。

## 11. Close Adoption

记录：

- Consumer-local collaboration status；
- accepted collaboration semantics 的 local provenance；
- runtime / strategy / tier mapping 的 local owner；
- 本次新增 / 调整的 Consumer-local policy；
- 当前 validation Evidence；
- 已知 observability limitation；
- fallback path。

本阶段不重新关闭或改变 upstream evaluated baseline；baseline adoption / upgrade closure 仍由对应 Consumer Adoption / Upgrade Method 拥有。

完成条件：Consumer 可以在 Fresh Context 中仅依赖 local state 恢复协作能力，协作启用状态有当前 Evidence 支撑，不存在未声明的 upstream runtime dependency，也没有把 requested configuration 冒充 observed runtime fact。

完成本 Method 不产生未来自动升级义务。upstream capability 后续变化只有通过显式 Consumer Upgrade 或新的 local semantic decision 才能改变 Consumer accepted semantics；纯 local runtime mapping 维护则服从目标 Repository 自身 Authority。