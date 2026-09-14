---
id: guide:multi-model-collaboration
type: guide
status: active
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

## 3. 不要让低成本模型成为 Authority proxy

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

## 4. Consumer adoption 与 runtime activation

这里需要区分两件事：

1. **接受 upstream capability semantics**：首次整体采用由 `method:consumer-adoption` 负责；Existing Consumer 的新 baseline delta 由 `method:consumer-upgrade` 负责；
2. **把已经接受的 Model Collaboration semantics 实例化为本项目 runtime capability**：由 `method:model-collaboration-adoption` 负责。

因此 Existing Consumer 不能因为想启用多模型协作，就绕过 baseline upgrade 直接从最新 upstream 复制 Architecture / Method / Rule。先让 reusable semantics 进入 Consumer-local canonical owner，再进入专用 adoption Method 建立配置、local policy 与验证。

`method:model-collaboration-adoption` 的生命周期为：

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

如果 Consumer 在同一次整体升级中刚刚接受这项新 capability，可以在 Consumer Adoption / Upgrade 完成 semantic acceptance 后连续进入本 Method；两段过程可以相邻，但 Gate 与 owner 不能合并成一份隐式流程。

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

## 6. Codex 参考映射

历史 `experiment/codex-multi-model-collaboration` 曾使用：

- read-only fast explorer；
- single implementation worker；
- independent quality reviewer；
- high-impact critical reviewer；
- primary agent 保存目标、Authority、决策与最终验证责任。

这个角色拆分仍可作为 Codex 的参考，但旧实验中的具体模型名称、reasoning effort 与并发数只属于当时实验实例。

新的 Consumer 应先探测当前 Codex 实际能力，再映射：

```text
low-cost capability      → 当前可用模型 / effort
capable reasoning        → 当前可用模型 / effort
high-capability reasoning→ 当前可用模型 / effort
```

### 示例配置形态

下面只展示形态，不是 normative config：

```toml
[agents]
enabled = true
# 具体 thread / concurrency / default model 按当前 runtime 与 Consumer policy 设置
```

子 Agent profile 应分别声明自己的只读 / 写入权限和有界职责。写入角色应保持 single-writer；explorer / reviewer 默认只读。

## 7. Runtime smoke 必须验证真实委派

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

## 9. Escalation

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

## 10. 最小采用检查表

进入专用 adoption 前：

- Consumer Authority 已恢复；
- Model Collaboration reusable semantics 已经被 Consumer 正式接受；
- 未决 upstream semantic delta 已经通过 Consumer Adoption / Upgrade 处理。

启用前：

- current runtime capabilities 已探测；
- strategy 与 capability tiers 已选定；
- local config / Rules / profile owners 已区分；
- single-agent fallback 已设计；
- static config PASS；
- child delegation smoke PASS；
- Authority-preserving handoff PASS；
- single-writer boundary PASS（如启用写入）；
- requested / observed model claim 边界明确；
- fallback PASS；
- ordinary runtime upstream access = 0。

如果这些条件不能成立，不要为了追求“多模型协作”而强行启用。