---
id: architecture:model-collaboration
type: architecture
status: active
distribution: release-input
release-target: software-development
---

# 模型协作架构

## 1. 目标与边界

本 Architecture 是 `agentic-dev` Source / Authoring Model 中的 **Model Collaboration capability** canonical owner：在不改变当前 Method 责任、Repository Authority 与 semantic ownership 的前提下，把确定性工具、不同能力层级的模型与独立 Agent 组合为可选运行能力。其 Consumer runtime 所需语义通过 Distribution Build 进入版本化 Release，而不是要求 Consumer 复制本 Architecture。

Model Collaboration 不是 `method:ai-development` 的替代品，也不自动增加新的产品开发阶段。普通软件开发仍由当前选定 Method 决定生命周期；本能力只回答“同一责任可以怎样在多个工具 / Agent / Model 之间分配，同时保持 Authority、Evidence 与最终责任不漂移”。

本 Architecture 不拥有任何具体模型名、价格、供应商、CLI 配置路径、并发数或 Consumer 当前启用状态。具体 runtime mapping 与配置属于 Repository-local capability instance。

## 2. 能力分层

协作优先按责任与认知复杂度分层，而不是按产品型号路由：

```text
Tier 0 — deterministic tooling
  search / lint / tests / Rule Discovery / structured extraction

Tier 1 — low-cost capability
  bounded exploration / context preparation / evidence collection / classification

Tier 2 — capable reasoning
  ordinary specification / implementation / debugging / semantic confirmation / normal review

Tier 3 — high-capability reasoning
  high-impact architecture / unresolved conflicts / irreversible decisions / independent challenge
```

能由 deterministic tooling 可靠完成的工作不得为了“使用多模型”而升级为 LLM 工作。高能力模型也不得仅因为身份更强而默认接管普通任务。

## 3. 主要责任

每次协作必须存在一个明确的 **Primary Agent / current responsibility owner**。它保留：

- 当前 Goal、Scope 与 Repository Authority 的解释责任；
- 当前 Method stage / direct responsibility；
- 委派边界与允许副作用；
- 对子结果的接受、拒绝或升级判断；
- 最终状态重新读取与 completion claim；
- 需要人工授权的外部操作升级。

子 Agent 的成功返回、退出码 `0`、自述“已完成”或 requested model 配置都不能替代 Primary Agent 对最终事实和 Evidence 的重新核验。

## 4. 保持权威的交接

低成本 Agent 可以作为 **context / evidence worker**，但不得成为 Authority proxy。

推荐 handoff 传递：

- current task facts；
- canonical Authority locator；
- Rule Discovery 返回的 candidate locator 与需要时的 exact Rule body；
- code / test / Evidence locator；
- 已观察事实；
- unknown / unresolved questions。

不得把 canonical Requirement、Method、Architecture、Rule 或其他 Authority 先压缩为低成本模型的二手总结，然后只把总结提供给后续推理模型。摘要可以帮助导航，但后续需要依赖规范语义时必须能够回到真实 owner。

跨 Agent 传递的 observation 与 normative source 必须可区分，避免把探索者推断升级成事实。

## 5. 委派边界

协作默认遵守：

1. **bounded delegation**：每个子任务目标、输入、允许操作和返回内容清晰；
2. **read-only by default**：探索、资料定位、独立 review 默认只读；
3. **single-writer**：同一共享写入面同一时刻只有一个明确 writer；
4. **no recursive fan-out by default**：子 Agent 不继续无界委派；只有 local Authority 明确允许并能保持责任可追溯时才扩展；
5. **fresh / isolated review**：需要独立 challenge 时，reviewer 不继承实施者的完成结论作为前提；
6. **minimum necessary context**：每个 Agent 只获得完成当前责任所需的 Authority、Rules、代码与 Evidence。

并行化只适用于真正独立的只读探索、分类、测试观察或复核。共享写入、共享外部资源和顺序依赖任务不得为了吞吐量而并行。

## 6. 条件性 policy 与模型协作

`agentic-dev` 自身 provider runtime 继续通过 Rule Discovery 激活本仓条件性 policy；模型协作不得绕过当前 Repository 的 policy / authorization。

但普通软件 Consumer Release 不默认安装 upstream Rule Discovery。发布到 Consumer 的 collaboration Skill 必须携带其通用 procedure / invariant 所需的 instructions / references，同时把 repository-specific authorization、technology policy、writer ownership 和 escalation 继续交给 Consumer-local Authority。

不得让低成本模型通过枚举任意 Rule tree、Guide 或历史聊天取得隐式权限，也不得把 exploration summary 当成 Repository Authority。

## 7. 模型路由与升级

Reusable capability 只定义能力层级，不硬编码模型型号。

默认路由原则：

```text
deterministic first
→ lowest sufficient capability
→ escalate when evidence justifies
```

升级高能力模型的典型条件包括：

- 当前 capable model 留下重大未决歧义；
- 多份 Evidence 或 reviewer 结论发生实质冲突；
- 涉及高返工成本架构、不可逆数据操作、安全 / 隐私或长期共享 contract；
- 明确需要独立 second opinion；
- Consumer-local policy 要求特定风险等级必须独立 challenge。

不得把模型等级本身当作结论权威。高能力模型的长期使用价值应由增量发现、决策质量、返工下降或其他当前 Evidence 证明。

## 8. 证据与模型身份

配置中的 model / reasoning effort 只表示 **requested runtime target**。只有运行轨迹或平台证据能够独立确认时，才能声明 observed / actual runtime model。

不可观察时必须明确写为 unknown / not observable，不得从输出风格、最终自述或配置文件反推实际模型身份。

同理，协作线程是否真实建立必须由可观察 thread / child run / event / result 证据支持；主 Agent 声称“已委派”不能单独证明委派发生。

## 9. 成本、启用与效率声明

Model Collaboration 不承诺减少总 token。多 Agent 工作可能增加总输入与协调开销。

评估重点应区分：

- high-capability / premium-model token；
- Primary Agent context size；
- total token；
- wall time；
- rework / correction rounds；
- completion quality 与 residual findings。

必须区分两个 claim level：

1. **functional enablement claim**：只证明选定 collaboration strategy 在当前 runtime 中真实可用、Authority / writer / Evidence 边界成立、失败可回退。达到该 claim 可以把通过验证的 strategy 标记为 enabled / conditional，但不能声称它比单 Agent 更省 token、更快或质量更高；
2. **efficiency / preferred-default claim**：若要声称 collaboration 是成本优化或应成为默认优选策略，必须与可比较的单 Agent baseline 对照，证明质量不低于 baseline，并且在 high-capability budget、Primary context、rework、wall time 等至少一个目标上存在当前 Evidence 支持的实际改善。

因此“链路能工作”与“值得默认使用”不是同一个结论。不能只根据“用了更便宜模型”或“并发更多”推断效率收益。

## 10. Consumer Release 与本地实例

普通软件 Consumer 可以选择不启用、部分启用或完整启用本能力。

两类责任明确分离：

1. **Release installation / update**：由 `method:consumer-adoption` / `method:consumer-upgrade` 确保当前 installed release 已包含 collaboration capability；
2. **local runtime activation**：由 `method:model-collaboration-adoption` 在 installed release 基础上探测 runtime、选择策略、建立 local instance 并验证。

启用后，Consumer local instance 至少明确：

- runtime / provider 与当前能力支持；
- capability tier → concrete model / effort mapping；
- Primary Agent 与 delegation policy；
- writer ownership 与并发边界；
- local config locator；
- Consumer-local collaboration policy；
- validation evidence locator；
- single-agent fallback / disable path。

具体 `.codex/`、其他 Agent 平台配置、模型名与并发数只属于 local instance 或 Human example，不属于本 Architecture。

Consumer ordinary runtime 不得依赖在线读取 `agentic-dev` current Source state。通用 collaboration semantics 的变化只有通过新的 versioned Release 才能进入 Consumer；纯本地 runtime mapping 维护服从目标 Repository 自己的 Authority。

## 11. 安装与普通运行时

`method:model-collaboration-adoption` 只在当前 installed release 已经提供 collaboration capability 后执行。

如果 Consumer 当前 Release 不包含所需 capability：

- 首次获得能力 → `method:consumer-adoption` 安装合适 Release；
- Existing Consumer → `method:consumer-upgrade` 更新到 candidate Release；
- 不得通过读取 upstream Source Architecture / Method / Rule 临时补齐。

启用后的 ordinary software work 仍由原有软件开发 Method / installed Skills 控制。Model Collaboration 只是运行方式，不自动改变产品目标、Requirement、当前 work kind、Integration Authority 或外部操作权限。

## 12. 回退

任何 Consumer runtime activation 都必须定义可验证的 single-agent fallback。出现以下情况时应 fail closed 到单 Agent 或停止协作，而不是假装多模型链路有效：

- 子 Agent runtime / thread 无法建立；
- requested capability 不可用；
- shared writer ownership 无法保证；
- handoff 丢失 Authority / Evidence；
- actual runtime identity 对当前 claim 至关重要但不可观察；
- collaboration failure 会使 completion claim 无法被当前 Evidence 支撑。

Fallback 只改变协作策略，不自动改变产品目标、Method Gate 或外部操作授权。