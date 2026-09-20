---
id: method:model-collaboration-adoption
type: method
status: active
distribution: release-input
release-target: software-development
---

# Model Collaboration Adoption Method

## 1. 目标与适用范围

本 Method 用于一个 Repository 在**当前 installed Release 已经提供 Model Collaboration capability** 后，显式建立、配置、验证并首次启用自己的 local collaboration instance。

它不替代 `method:ai-development`，也不拥有 Release 安装 / 升级责任：

- 首次获得 collaboration capability 由 `method:consumer-adoption` 安装对应版本化 Release；
- Existing Consumer 获得新的 collaboration capability / breaking change，由 `method:consumer-upgrade` 更新 Release；
- 只有当前 installed release 已包含本 Method 所依赖的 collaboration semantics / Skills / references 后，才进入本 Method 做 local runtime activation。

本 Method **不得绕过 Consumer Release 安装 / 升级**，也不得为了继续执行而在线读取 upstream Source Architecture、Method、Rule 或配置。

核心原则：

> **Release installation 与 local runtime activation 分离。**

## 2. 生命周期

```text
Restore Consumer Authority
→ Confirm Installed Collaboration Capability
→ Detect Runtime Capabilities
→ Select Collaboration Strategy
→ Plan Local Runtime Integration
→ Establish Local Collaboration Instance
→ Validate Collaboration
→ Enable / Fallback
→ Close Adoption
```

本 Method 的阶段表示 collaboration instance adoption 工作状态，不是普通软件开发阶段，也不自动授予产品 Execute、merge、release 或 deploy 权限。

## 3. Restore Consumer Authority

先恢复目标 Repository：

- 当前 installed release identity；
- Consumer-owned `AGENTS.md`；
- 当前 Agent Skills / collaboration references；
- Project Knowledge / Repository Authority；
- runtime / provider 配置；
- 当前工作状态与允许修改范围。

必须确认：

- 谁拥有 local collaboration instance；
- 是否已经存在 model / agent routing 配置；
- 是否有共享写入、外部操作、review 或安全 policy；
- 当前是否存在不允许被配置变更打断的 active lifecycle。

不得从 upstream Project state、Guide、历史聊天或旧实验分支推断 Consumer 当前拥有或启用了这项 capability。

退出条件：installed release、local owners、允许变更边界与当前协作状态明确。

## 4. Confirm Installed Collaboration Capability

确认当前 installed release 已经提供 runtime activation 所需的 collaboration capability，至少可恢复：

- collaboration Skill / instruction entry；
- 必要 references；
- Runtime compatibility / execution requirement；
- 与当前 activation 相关的通用 invariant；
- release provenance / version。

如果当前 installed release 不包含所需 capability：

- 首次安装返回 `method:consumer-adoption`；
- Existing Consumer 返回 `method:consumer-upgrade`；
- 不得在线读取 upstream Source tree 临时补齐。

Consumer-local Product / authorization / technology policy 如果会约束 collaboration，继续由 Consumer 自己的 Authority 持有；它们不需要被复制到 Release。

退出条件：本次 activation 的通用输入来自 installed release，本地约束来自 Consumer Authority。

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

退出条件：当前 runtime capability matrix 有 Current Evidence 支持，unknown 项明确。

## 6. Select Collaboration Strategy

依据真实平台能力、任务类型、风险和成本目标选择 local strategy。至少允许：

- `disabled`；
- `basic`：deterministic tooling + bounded low-cost/read-only exploration + Primary Agent；
- `reviewed`：在 basic 之上增加独立 review；
- Consumer 自定义 strategy：只要不违反 installed capability 的稳定 invariant 与 Consumer Authority。

具体模型 / effort 映射始终属于 local runtime configuration，不属于通用 Release Authority。

退出条件：strategy、tier mapping、触发条件、fallback 与预期优化目标明确。

## 7. Plan Local Runtime Integration

只规划**本地 runtime instance**，不重新决定 upstream capability 是否采用。

根据本地策略建立或更新：

- runtime configuration / agent profiles；
- Consumer-local conditional policy；
- Consumer-owned Bootstrap 中必要的薄 locator；
- validation assets；
- local evidence / fallback entry。

区分：

- installed release 提供的通用 invariant；
- Consumer-specific authorization / technology / environment policy；
- local runtime config / concrete model mapping。

如果规划中发现必须改变 Release 提供的通用 capability，而不是单纯建立 local instance，则返回 Release upgrade / upstream evolution，不在本 Method 内静默改写发布能力。

退出条件：local config / policy / evidence owners 明确，没有第二套通用 capability owner。

## 8. Establish Local Collaboration Instance

在 Consumer 自己的 Project / Repository Authority 中建立薄 collaboration instance，至少记录：

- status：disabled / enabled / conditional；
- runtime / provider；
- local configuration locator；
- capability tier mapping locator；
- delegation / writer ownership locator；
- validation evidence locator；
- single-agent fallback locator。

Consumer local instance 不复制 upstream Source Architecture / Rule corpus，也不要求访问 `agentic-dev` 才能恢复。

退出条件：local instance 可从 Fresh Context 独立恢复。

## 9. Validate Collaboration

验证至少覆盖：

1. configuration validation；
2. delegation smoke；
3. authority fidelity；
4. single-writer；
5. review isolation；
6. requested / observed runtime claim separation；
7. single-agent fallback；
8. ordinary runtime `upstream access = 0`。

如果要声明 efficiency / preferred-default value，应与可比较的单 Agent baseline 对照；一次 smoke 只能证明链路可用，不能证明长期成本收益。

退出条件：准备启用的每个 strategy / role path 都有 Current Evidence；失败 / unknown path 已经被禁用、缩减或 fallback。

## 10. Enable / Fallback

启用状态必须精确对应已验证范围：

- `enabled`：所选 strategy 的全部必需检查通过；
- `conditional`：只启用已独立验证的缩减子策略；
- `disabled`：不存在可安全启用的 child-based strategy，继续单 Agent runtime。

无论状态如何：

- single-agent fallback 可执行；
- collaboration failure 不改变产品目标或 Method Gate；
- child Agent 不自动获得 merge / release / deploy / destructive external-operation 权限；
- high-capability escalation 仍由 Evidence / local policy 触发。

退出条件：local status 与 Current Evidence 一致。

## 11. Close Adoption

记录：

- installed release / collaboration capability provenance；
- Consumer-local collaboration status；
- runtime / strategy / tier mapping local owner；
- 本次新增 / 调整的 Consumer-local policy；
- validation Evidence；
- observability limitation；
- fallback path。

本阶段不改变 installed release identity；Release 安装 / 升级 closure 仍由对应 Consumer Method 拥有。

完成条件：Consumer 可以在 Fresh Context 中仅依赖 local state + installed release 恢复协作能力，不存在未声明的 upstream Source dependency，也没有把 requested configuration 冒充 observed runtime fact。

完成本 Method 不产生未来自动升级义务。Release 后续变化只有显式 Consumer Upgrade 才能改变 installed capability；纯 local runtime mapping 维护服从目标 Repository Authority。
