# 规则治理与知识激活 v2

## 状态

**活动有限里程碑 — 规划与设计阶段**

当前阶段：

> **Phase D — Discovery → Routing → Skill 接口**

人工决策日期：2026-09-10  
跟踪入口：Issue #92  
启动基线：`master@b6a20053a7a6f4f53915bea8218604720412c302`

长期阶段保持：

> **工程能力扩展与方法演进**

## 1. 核心目标

v1 已证明最小规则激活、来源追溯和 fail-closed 的价值；v2 要解决的是**真实 Consumer 长期独立运行**：

> 让 `agentic-dev` 的可复用方法 / 规则 / Skill 能被 Consumer 选择性采用并固化为 Consumer-local 可发现资产；完成 adoption 后，ordinary Consumer runtime 只依赖 Consumer Repository，不把 upstream 作为日常运行依赖。

Consumer 自己的 Repository Rules、Requirement / Specification、Domain / Architecture / ADR、Verification / Integration Rules 与 adopted reusable capability 必须能进入同一本地发现路径，同时始终保持 Consumer Repository Authority 优先。

## 2. 最高设计约束

### 2.1 Consumer-local-first

设计顺序固定为：

```text
Consumer-local Runtime Target
→ 需要的 Discovery / Routing / Skill / Authority 机制
→ agentic-dev 应提供的可复用能力与 Adoption Contract
```

不得先构建完整 upstream Runtime，再把 Consumer 适配留到最后。

### 2.2 单点 semantic owner

同一规范性规则只能有一个长期正文 owner。Metadata、Catalog、导航只保存发现所需的最小信息和 source pointer，不复制完整规则正文，也不形成第二套 Authority。

### 2.3 Adoption 后脱离日常 upstream

只有以下情况才重新读取 upstream：

- 显式 baseline upgrade；
- Consumer-local Authority 无法回答当前真正需要的方法 / Skill 问题；
- 当前任务明确属于 `agentic-dev` 实验 / 验证；
- Consumer Repository Authority 另有要求。

其他 ordinary work 应完全从 Consumer-local 入口恢复。

### 2.4 最小机制优先

当前不预设：

- Runtime Rule Index 服务；
- 向量数据库 / 图数据库；
- MCP 规则服务；
- 全仓统一 Front Matter；
- Rule Super Skill；
- 大量新专项 Skill；
- 机械拆分全部 Guide；
- 固定 Consumer 目录模板。

静态 Consumer-local metadata / Catalog 足够时，不增加更复杂基础设施。

## 3. 已接受证据边界

### 3.1 v1 基础

继续沿用：

- Consumer Repository Authority first；
- Progressive Disclosure；
- Evidence before claims；
- 详细规则单点 Authority；
- derived discovery 可删除 / 可重建；
- stale / missing / ambiguity / conflict / high-impact 时 fail-closed；
- 普通 Consumer 不要求运行 `evals/` 下的规则检索原型。

### 3.2 v2 临时 Runtime 证据

独立 `eval/*` 分支已经支持以下有限结论：

- Skill-first 在正确 responsibility 下能明显减少 context fan-out；
- Guide decomposition + metadata 可以帮助模型自主发现 `technical-planning`；
- ambiguity 场景中可以区分 primary responsibility、supporting context、Stage Return 与 stale Readiness。

这些证据只支持继续 v2 Planning，不授权原样产品化 eval manifest、全库 metadata 或 Runtime Rule Index。

### 3.3 Consumer 现实证据

Issue #58 已证明：只存在于 upstream、没有被 Consumer 显式采纳并本地固化的持续协作规则，在普通 Fresh Context 中不可靠。

因此 baseline adoption / upgrade 必须允许逐项：

```text
adopt
retain / override
reject / not applicable
```

并把需要长期约束后续工作的结果固化到 Consumer-local Authority / capability 中。

## 4. 已完成设计阶段

### Phase A — Consumer-local Runtime Target / Acceptance

**已完成。**

结果：

- `docs/project/consumer-local-rule-runtime-target-v2.md`
- `docs/project/consumer-local-rule-runtime-acceptance-v2.md`

确认 ordinary runtime 无 upstream；Consumer-native 与 adopted reusable asset 可以进入同一本地 discovery；routing-only 不机械加载 Skill；最终必须经过真实 Consumer L3 验证。

### Phase B — Rule Ownership / Guide Decomposition

**已完成。**

结果：

`docs/project/rule-ownership-decomposition-audit-v2.md`

确认：

- Principle 继续拥有顶层方法不变量；
- 8 个核心 Skill 继续拥有完整职责执行过程；
- Engineering Discipline 继续拥有跨技术栈阶段内工程约束；
- 只有真正跨 Skill / adoption / verification / external-operation 的条件语义才成为 reusable Guide Rule Module 候选；
- Consumer-native Authority 由 Consumer 自己拥有；
- Catalog / metadata 只承担 derived discovery。

Guide 不按文件大小或原章节机械拆分。

### Phase C — Minimal Metadata / Catalog Contract

**已完成。**

结果：

`docs/project/consumer-local-activation-metadata-contract-v2.md`

采用逻辑两层模型：

```text
Activation Manifest
→ optional derived Runtime Catalog
→ Consumer-local semantic owner
```

核心边界：

- Manifest / Catalog 不保存规则正文；
- `activation_role = bootstrap / routing / constraint / execution`；
- `semantic-reviewed` metadata 在 source 语义变化后必须重新复核；
- `current-locator` 只定位 Consumer Current Authority，不缓存易变化状态摘要；
- Consumer-native / adopted 来源身份必须保留；
- stale / missing / ambiguous discovery 必须 fail-closed 到 Consumer-local Current Authority。

## 5. 根入口职责收敛

2026-09-10 的 v2 复核发现：根 `AGENTS.md` 曾同时维护稳定仓库治理、当前里程碑 / 阶段、候选状态、方法摘要、AI 复核细则、中文表达细则和 Research 生命周期说明，造成职责混杂和 Fresh Context 常驻上下文膨胀。

已接受并实施以下长期边界：

- `AGENTS.md`：只维护稳定 Repository Governance、Authority Boundary 与 Agent 工作约束；
- `README.md`：维护面向人的简短当前状态和稳定导航；
- `docs/project/project-roadmap.md`：维护详细当前阶段、活动里程碑、候选库与下一 Gate；
- 具体 `docs/project/*`：维护里程碑设计 / 项目治理；
- Method / Principle / Architecture / Skill / Guide：继续各自单点拥有其规范性语义；
- Git / PR / Issue / Actions：保存精确外部状态和执行证据。

当前阶段、里程碑进展、候选路线、Issue / PR 状态、实验进展和下一工作项不得为了 Fresh Context 方便重新复制回 `AGENTS.md`。

该收敛同时修正了 v1 之后出现的一个结构性矛盾：一方面要求薄启动和 Progressive Disclosure，另一方面又把易变化状态持续堆入最高优先级 `AGENTS.md`。v2 后续 Consumer-local Bootstrap 设计必须避免复现这一模式。

## 6. 当前 Phase D — Discovery → Routing → Skill Interface

当前目标不是增加新的 Stage Router Skill，而是冻结一个最小运行接口。

必须回答：

1. task signal 如何产生候选 responsibility；
2. primary responsibility 与 supporting context 如何区分；
3. routing-only 什么时候可以停止而不加载 Skill；
4. 真正进入职责执行时何时加载 Skill；
5. constraint module 如何与 execution owner 组合；
6. Stage Return 后如何重新解析责任，并使旧 routing / Readiness 失效；
7. 多个规则命中时如何得到最小充分集合；
8. stale / missing / ambiguity / conflict / high-impact 时如何 fail-closed；
9. runtime adapter 如何只负责发现 / 交付 / 加载，不拥有 Method 语义。

Phase D 的结果必须直接受 Phase A Acceptance 和 Phase C metadata contract 约束。

## 7. 后续阶段

### Phase E — Baseline Adoption / Consumer-local Projection

需要冻结：

- exact upstream baseline；
- reusable vs `agentic-dev` project-only；
- adopt / retain-or-override / reject-not-applicable；
- adopted rule / module / Skill 的 Consumer-local persistence；
- provenance / source relation；
- Consumer-specific override 与 supersede；
- 再次升级时的 compare / update / retain / supersede；
- 不机械复制完整 upstream 文档体系。

### Phase F — 真实 Consumer 验证

**核心完成门禁。**

至少一个真实 Consumer 必须在新的 Fresh Context 中证明：

- ordinary runtime 不读取 upstream；
- 能从 Consumer Repository 自己恢复 Authority 与 local discovery；
- 能发现 Consumer-native 与 adopted reusable rules；
- primary / supporting responsibility 正确；
- 需要时才加载 Skill；
- Stage Return / fail-closed 正确；
- Consumer 更具体规则优先；
- baseline upgrade 仍显式、可审计；
- 没有第二套 Authority 或明显机械维护负担。

Consumer Repository 的实际修改必须在 Consumer 自己的授权上下文中执行；本仓库不得跨仓库静默修改。

### Phase G — 收敛与集成准备

完成 v1 回归、Authority / Method / Architecture / Guide / Skill 一致性检查、Consumer-local 证据复核、stale / fail-closed 回归、最终 AI Review 与稳定状态同步。

## 8. 完成定义

只有以下条件全部满足，v2 才可结束：

1. Consumer-local Runtime Target、discovery、semantic owner、routing 与 Skill activation 边界一致；
2. 同一规范性规则只有一个长期正文 owner；
3. stale / missing / ambiguity / conflict / high-impact 均有明确 fail-closed；
4. baseline adoption / upgrade 支持 adopt / retain-or-override / reject；
5. Consumer-native 与 adopted reusable asset 能被同一本地入口协调，同时保持 Consumer Authority 优先；
6. 至少一个真实 Consumer 在 ordinary Fresh Context 中不依赖 upstream 仍能正确发现、路由并按需执行 Skill；
7. Consumer 验证无未解决 Blocking / Medium 通用缺口；
8. 没有第二套 Authority、机械 metadata 维护、全库复制或超级能力；
9. 最终 AI Review 未解决 Blocking / Medium = `0 / 0`；
10. README、Roadmap、项目记录和必要 adoption / usage 入口能让新的上下文恢复最终有效状态，`AGENTS.md` 保持稳定治理入口而不重新承载项目状态。

达到以上条件只表示已具备进入人工集成决策的条件；合并仍由人工权威或仓库策略决定。