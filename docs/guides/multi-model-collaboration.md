---
id: guide:multi-model-collaboration
type: guide
status: active
distribution: source-only
---

# 多模型协作使用指南

本 Guide 面向人类说明如何理解和采用 Model Collaboration capability。规范语义以 `docs/architecture/model-collaboration-architecture.md` 与 `docs/methods/model-collaboration-adoption.md` 为准；本文件不拥有新的 Gate、routing 或 policy。

## 1. 什么时候值得启用

Model Collaboration 适合下列情况：

- 大量只读搜索、依赖定位、Rule / Authority / Evidence 收集占据主模型上下文；
- 实施与独立 review 可以清晰隔离；
- 某些高影响决策只在有未决冲突时需要更高能力 second opinion；
- Consumer 希望把高能力模型预算集中到真正需要推理的工作，而不是信息搬运。

它不适合为了“多 Agent”本身增加复杂度。一个模型已经能稳定完成、上下文很小、协调成本高于收益时，保持单 Agent 更合理。

## 2. 推荐职责模型

```text
Deterministic tools
  ↓
Low-cost explorer / context worker
  ↓
Primary / capable reasoning worker
  ↓
Independent reviewer（按需要）
  ↓
High-capability second opinion（只在触发条件成立时）
```

Primary Agent 始终保留 Goal、Authority、委派边界与最终 completion claim。子 Agent 返回的是证据、观察或有界工作结果，不自动成为最终事实。

## 3. 不要让低成本模型成为 Authority 代理

推荐 handoff：

```text
task facts
canonical authority locators
Rule Discovery candidate locators + exact bodies when needed
code / test locators
observed evidence
unknown / unresolved questions
```

不推荐：

```text
canonical Rule / Requirement
→ cheap model summary
→ original source discarded
→ reasoning model only sees summary
```

低成本模型可以帮助“找什么、读什么、整理什么”，但后续真正依赖规范语义时仍应能读取 canonical owner。

## 4. Consumer Release 与运行时启用

这里需要区分两件事：

1. **获得 collaboration capability**：首次整体安装由 `method:consumer-adoption` 负责；Existing Consumer 通过 `method:consumer-upgrade` 更新到包含相关能力的 candidate Release；
2. **把 installed collaboration capability 实例化为本项目 runtime**：由 `method:model-collaboration-adoption` 负责。

因此 Consumer 不能因为想启用多模型协作，就在线读取最新 upstream Source Architecture / Method / Rule 临时补能力。先确保当前 installed release 已包含 collaboration capability，再进入专用 Method 建立 local config、policy 与验证。

`method:model-collaboration-adoption` 的生命周期为：

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

## 5. Consumer 中应该固化什么

典型 Consumer 可以包含：

```text
<consumer>/
├─ Project Capability Profile 或等价 Authority
│  └─ collaboration status / runtime / config locator / fallback locator
├─ platform-local config
│  └─ 例如 .codex/config.toml + agent profiles
├─ Consumer-local Rules
│  └─ 只保存本项目真正条件性 policy
└─ validation evidence / tests
```

不要把 upstream Project Profile 复制到 Consumer；不要因为示例使用某个模型就把该模型写成通用规范。

这里的 platform config、tier mapping 与 local Rules 是 **runtime instance projection**，不是第二次决定 upstream Architecture 是否被采用。若 projection 迫使你改变 reusable semantics，应返回 Consumer Adoption / Upgrade 或目标仓库等价 Authority。

## 6. Codex 参考实现

历史 `experiment/codex-multi-model-collaboration` 曾使用 read-only explorer、single implementation worker、independent quality reviewer、high-impact critical reviewer 与一个保存 Goal / Authority / Decision / Final Verification 的 Primary Agent。这个职责拆分仍可作为 Codex 参考，但旧实验中的具体模型、reasoning effort、并发数和 `.codex/` 文件不是当前规范。

当前完整 Codex 参考配置、角色 profile 与 runtime smoke 结构见：

[`codex-model-collaboration-reference.md`](codex-model-collaboration-reference.md)

该 Reference 是带核验日期的 Human View：它可以展示 `.codex/config.toml`、`.codex/agents/*.toml` 的安全起点，但 Consumer 仍必须在 `method:model-collaboration-adoption` 中重新探测当前 Codex schema、模型可用性、sandbox、thread、observability 与 effective config。

新的 Consumer 应把抽象能力层映射到当前真实可用模型，而不是复制历史型号：

```text
low-cost capability       → 当前可用模型 / effort
capable reasoning         → 当前可用模型 / effort
high-capability reasoning → 当前可用模型 / effort
```

## 7. 运行时冒烟验证必须验证真实委派

旧实验曾发生：静态配置解析成功，但真实轨迹出现 `collab spawn failed: no thread with id`；主线程最终回答仍声称委派成功。

因此 adoption 不能只看：

- TOML 可以解析；
- CLI exit code = 0；
- 主 Agent 说“子 Agent 已完成”。

必须观察至少一个真实 child thread / child run / child terminal result。若当前平台无法提供足够证据，应把该项标记为不可观察，并按 Method 决定保持 disabled / conditional 或 fallback。

## 8. 成本怎么看

不要把“总 token 一定下降”当作目标。多 Agent 可能增加总 token。

更有意义的是分别看：

- 高能力模型 token 是否下降；
- Primary Agent context 是否变小；
- 总 token 是否可接受；
- wall time 是否改善；
- 返工轮次是否下降；
- 最终质量 / residual findings 是否不低于单 Agent baseline。

一个合理的成功案例可以是“总 token 略升，但高能力模型输入大幅下降、质量不降、返工减少”。

应区分两个 claim：

- functional enablement：证明选定协作链路安全可用并可 fallback；
- efficiency / preferred-default：只有可比单 Agent baseline 支持时才能声称更省、更快或更适合作为默认策略。

## 9. 升级

默认：

```text
deterministic first
→ lowest sufficient capability
→ escalate only with evidence
```

高能力 second opinion 更适合：

- 高返工成本 architecture；
- migration / irreversible data；
- security / privacy；
- conflicting review evidence；
- ordinary capable model 留下重大未决问题。

Issue #71 的 Consumer Evidence 已表明，高端模型并不天然拥有只有它才能发现的 blocking issue，因此模型身份本身不能成为升级理由。

## 10. 最小启用检查表

进入专用 activation Method 前：

- Consumer Authority 已恢复；
- 当前 installed release 已包含 collaboration capability；
- 如果当前 Release 不包含，需要先执行 Consumer Adoption / Upgrade；
- 没有通过 upstream Source tree 临时补齐 capability。

启用前：

- current runtime capabilities 已探测；
- strategy 与 capability tiers 已选定；
- local config / policy / evidence owners 已区分；
- single-agent fallback 已设计；
- 静态配置通过；
- 子模型委派冒烟验证通过；
- 保持 Authority 的交接验证通过；
- 单写入者边界验证通过（如启用写入）；
- requested / observed model claim 边界明确；
- 回退验证通过；
- ordinary runtime `upstream access = 0`。

如果这些条件不能成立，不要为了追求“多模型协作”而强行启用。
