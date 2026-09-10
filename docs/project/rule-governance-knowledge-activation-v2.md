# 规则治理与知识激活 v2

## 状态

**活动有限里程碑 — 规划与设计阶段**

当前阶段：

> **Phase B — Rule Ownership 与 Guide Decomposition 审计**

人工决策日期：2026-09-10

跟踪入口：Issue #92

启动基线：

`master@b6a20053a7a6f4f53915bea8218604720412c302`

长期阶段保持：

> **工程能力扩展与方法演进**

本里程碑承接“规则治理与知识激活 v1”已经验证的规则激活、渐进式披露、来源追溯和 fail-closed 基础，但不把 v1 的评估索引直接升级为正式运行时能力。

## 1. 核心问题

v1 已经证明：当前任务可以通过更小的规则集合获得可靠激活，并且派生索引可以在不成为第二套权威的前提下支持评估。但真实 Consumer 的长期问题仍未完全解决：

- 上游规则即使存在，如果没有在 baseline adoption 时被使用方显式采纳并固化为 Consumer-local 可发现权威，普通 Fresh Context 仍可能无法可靠发现；
- `agentic-dev` 不能成为已有 Consumer 日常开发必须持续读取的运行依赖；
- Consumer 自己的 Repository Rules、Domain / Architecture Authority、Verification / Integration Rules 与已采纳的可复用方法能力必须能在同一个本地发现路径中工作；
- 规则发现机制如果只在 `agentic-dev` 仓库内有效，就没有完成真实使用方闭环。

因此 v2 的主要目标不是继续优化 `agentic-dev` 自身的规则检索，而是：

> **形成并验证一个能够被 Consumer 选择性采用、固化并长期独立运行的 Consumer-local 规则发现与激活模型。**

成功标准必须以 Consumer-local 持续可用为最终依据，而不是以 `agentic-dev` 内部实验本身为完成条件。

## 2. 最高设计约束

### 2.1 Consumer-local-first

设计顺序必须从 Consumer 的长期运行目标反推上游能力：

```text
Consumer-local Runtime Target
        ↓
需要的发现 / 路由 / Skill / Authority 机制
        ↓
agentic-dev 应提供的可复用模型与采用方式
```

不得先把 `agentic-dev` 内部架构设计完整，再把 Consumer 适配作为最后一步。

### 2.2 Consumer Repository Authority 始终最高

`agentic-dev` 只提供可复用的方法、Skill、指南与采用模型，不替 Consumer 决定项目事实。

Consumer-local 发现路径必须能够同时处理：

- Consumer Repository Rules；
- Consumer Requirement / Specification；
- Consumer Domain / Architecture / ADR Authority；
- Consumer Verification / Integration Rules；
- Consumer 已采用的 `agentic-dev` 可复用规则与 Skill；
- 当前执行单元、运行状态和当前证据。

当使用方本地规则与上游可复用规则存在冲突时，先区分合理项目特化、陈旧 baseline 与上游通用缺口；不得由上游默认覆盖 Consumer Authority。

### 2.3 Adoption 后脱离日常上游依赖

已有 Consumer 完成 baseline adoption / upgrade 后，普通开发应恢复以 Consumer-local Authority 为主要入口。

只有明确执行 baseline upgrade、Consumer 本地权威无法回答当前真正需要的方法 / Skill 问题、当前工作被明确标记为 `agentic-dev` 实验，或 Consumer Authority 另有要求时，才重新读取 upstream。

### 2.4 单点语义所有权

同一规范性规则只能有一个长期语义 owner。

Metadata、Catalog、导航和派生索引只保存发现所需的最小信息与来源指针，不复制完整规则正文，也不形成第二套 Authority。

### 2.5 最小机制优先

当前证据只支持继续研究薄发现层、规则模块化与按需 Skill 激活，不支持预先引入：

- Runtime Rule Index 服务；
- 向量数据库或图数据库；
- MCP 规则服务；
- 全仓库统一 Front Matter；
- Rule Super Skill；
- 大量新的专项 Skill；
- 机械拆分全部 Guide。

如果静态 metadata / Catalog 与 Consumer-local 资产已经足以满足发现需求，不增加更复杂基础设施。

## 3. 当前证据与解释边界

### 3.1 v1 已确认基础

“规则治理与知识激活 v1”已经确认：

- 常驻核心规则应保持薄；
- 规则治理对象是激活单元，不是文件大小；
- 详细语义继续由现行 Authority / Guide / Skill 单点维护；
- 派生索引必须可删除、可重建并检测来源陈旧；
- 来源缺失、陈旧、冲突、无法分类或高影响边界不清时必须 fail-closed 回到当前 Repository Authority；
- 普通 Consumer 不要求运行 `evals/` 下的规则检索原型。

### 3.2 v2 临时运行实验

v2 Planning 前已在独立 `eval/*` 分支完成有限实验。这些实验不构成正式 Method / Guide / Skill Authority，只提供设计证据。

主要结论：

1. **E-min / Skill-first**：当当前 responsibility 已正确解析并激活 `technical-plan` 时，GPT-5.6 与 GPT-6 均在保持关键技术规划语义的前提下显著减少 Repository context fan-out。
2. **Guide decomposition + metadata**：在不预先声明 responsibility 的情况下，两个模型均可从多候选 metadata Catalog 自主发现 `technical-planning`，按需读取小 Guide 模块与 Skill，并进一步降低上下文扩散。
3. **Metadata 歧义压力场景**：当任务同时具有 Execute、历史 Readiness、共享 contract / Architecture basis 失效等竞争信号时，两个模型均能把 `technical-planning` 识别为 primary responsibility，将 execution / readiness 仅作为 supporting context，正确 Stage Return，未误进 `systematic-debug` 或复用陈旧 Readiness。

精确实验锚点：

- `eval/rule-governance-v2-research@e5f53198b157466c847d2cf62aeca902f1b79082`
- `eval/rule-governance-v2-guide-metadata@03ea11391ef1f1dbe101ebc723ef009a4d45592e`
- `eval/rule-governance-v2-metadata-ambiguity@7db9eaaa894c579cfe7695074a237aa1de8b3741`

这些结果支持进入 v2 Planning，但不证明：

- 当前 eval manifest 应原样产品化；
- 所有 Guide 都应拆分；
- 所有规则都需要 metadata；
- Runtime Rule Index 已有实施必要；
- `technical-plan` 单一职责上的结果可机械外推到全部 Skill；
- Consumer-local 投射已经完成。

### 3.3 Consumer 现实证据

Issue #58 已提供真实使用方样本：某些 repository-facing conventions 虽存在于上游 baseline，但未进入 Consumer-local Authority 时，普通 Fresh Context 难以可靠发现。

当前已经接受的泛化方向是：baseline upgrade 时逐项由 Consumer 判断：

```text
adopt
retain / override
reject / not applicable
```

只有需要长期约束后续工作的规则才固化为 Consumer-local 可发现权威；`agentic-dev` 自身项目规则不自动继承。

这项 Consumer 证据是 v2 的核心验收输入，而不是辅助案例。

## 4. 候选运行模型

当前证据支持继续设计以下最小候选链路，但本节仍是 v2 待验证目标模型，不直接成为通用方法强制规则：

```text
Thin Consumer-local Bootstrap
        ↓
Consumer-local Metadata / Catalog
        ↓
Small Rule / Guide Modules
        ↓
Responsibility / Condition / Risk / Stage Routing
        ↓
如果只需路由，停止
如果真正进入职责执行
        ↓
Load corresponding Skill
        ↓
Consumer Authority + Current Evidence
        ↓
Execute / Verify / Stage Return
```

职责边界候选：

- **Bootstrap**：只保留 Consumer Authority 优先、渐进式披露、当前证据等真正跨任务不变量与本地发现入口；
- **Metadata / Catalog**：帮助发现“当前应继续读取什么”，不拥有详细规范性语义；
- **Rule / Guide Module**：承载适用范围明确、需要独立激活的规则语义，并保留单点 owner；
- **Skill**：只在真正进入对应稳定职责执行时加载完整过程；
- **Consumer Authority / Current Evidence**：提供项目事实、当前状态和最终约束。

是否需要物理拆文件、metadata 的存储形式、Catalog 是静态文件还是可重建投影、以及哪些内容适合由 Skill 直接拥有，都必须由后续 ownership 与 Consumer-local 设计决定。

## 5. 分阶段路线

### 阶段 A — Consumer-local 目标模型与验收基线

状态：**已完成**。

A1 已形成 Consumer-local Runtime Target：

`docs/project/consumer-local-rule-runtime-target-v2.md`

A2 已形成 Consumer-local Acceptance Baseline：

`docs/project/consumer-local-rule-runtime-acceptance-v2.md`

阶段 A 已确认：

- ordinary Consumer runtime 不依赖 upstream；
- Consumer-native Authority 与 adopted reusable rule 必须能在同一本地发现路径中工作，同时保持来源身份与 Consumer Authority 优先；
- discovery layer 不拥有规则正文；
- routing-only 不机械加载 Skill；
- stale / missing / ambiguity / conflict 必须 fail-closed 到 Consumer-local Current Authority；
- 最终完成必须经过真实 Consumer L3 验证；
- token / context 降幅只能在语义正确和 Consumer-local 独立性通过后作为效率指标。

### 阶段 B — Rule Ownership 与 Guide Decomposition 审计

状态：**当前**。

目标：对当前可复用规则逐项确定长期 owner 和独立激活边界。

至少分类：

```text
always-on invariant
existing Skill-owned
cross-skill conditional rule
platform-specific rule
consumer adoption / bootstrap rule
agentic-dev project-only rule
duplicate / obsolete / explanatory content
```

阶段 B 不以“大文件”为拆分理由。每个候选激活单元必须说明 trigger、consumer、是否需要独立加载、语义 owner、Consumer-local 投射价值和取代关系。

Phase B 必须以 A1 / A2 为验收约束，不能从临时 G-min manifest 直接生成正式拆分。

### 阶段 C — 最小 Metadata / Catalog 契约

在 A / B 的结果上冻结最小 schema。

候选字段只在有真实发现价值时保留，例如：

- identity；
- scope；
- responsibility；
- conditions；
- risk；
- consumer；
- source pointer / source identity；
- supersede / applicability 等少量必要关系。

必须同时定义：

- Authority 与派生 metadata 的边界；
- stale source 检测；
- missing source；
- ambiguity / conflicting applicability；
- high-impact fail-closed；
- metadata 更新 / 重建 / 删除生命周期。

### 阶段 D — Discovery → Routing → Skill 接口

目标：冻结运行时职责接口，而不是建立新的超级控制器。

重点回答：

- 何时只需 module 完成 routing，不加载 Skill；
- 何时真正进入 Skill；
- primary responsibility 与 supporting context 如何区分；
- Stage Return 如何表达；
- 多个模块命中时如何保持最小充分集合；
- 何时 fail-closed 到 Consumer Authority；
- 运行时适配只负责交付 / 发现 / 加载，如何避免拥有方法语义。

### 阶段 E — Baseline Adoption / Consumer-local Projection

目标：定义上游能力如何低成本、可审计地成为 Consumer-local 持久能力。

必须覆盖：

- exact upstream baseline；
- reusable vs `agentic-dev` project-only；
- `adopt / retain-or-override / reject-not-applicable`；
- adopted rule / module / Skill 的本地 persistence；
- provenance 与 source relation；
- Consumer-local priority、scope、update trigger；
- upstream 新版本不能自动覆盖本地已采用规则；
- 再次升级时如何比较、更新、取代或保留；
- 不机械复制完整 `agentic-dev` 文档体系。

### 阶段 F — 真实 Consumer 验证

这是 v2 的核心完成门禁，而不是可选附加实验。

至少选择一个真实 Consumer，按其 Repository Authority 执行 adoption / projection，并在新的 Fresh Context 中验证：

- 日常运行不读取 `agentic-dev` upstream；
- 能从 Consumer Repository 自己恢复当前 Authority 和本地发现入口；
- 能发现代表性 Consumer-native 与 adopted reusable rules；
- 能正确区分 primary / supporting responsibility；
- 能在需要时激活 Skill；
- 能正确 Stage Return / fail-closed；
- Consumer 更具体规则优先；
- 没有第二套 Authority 或明显维护负担；
- baseline upgrade 仍保持显式、可审计。

Consumer Repository 的任何实际修改必须在 Consumer 自己的授权上下文中执行；本 `agentic-dev` 里程碑只定义能力、采用契约和验证要求，不跨仓库静默修改 Consumer。

### 阶段 G — 收敛、回归与集成准备

完成：

- 与 v1 核心规则回归；
- Authority / Method / Architecture / Guide / Skill 一致性检查；
- Consumer-local 验证证据复核；
- stale / fail-closed 回归；
- 最终 AI Review；
- Project Roadmap 与恢复入口同步；
- 达到“已具备进入人工集成决策的条件”。

## 6. 非目标

本里程碑当前不：

- 启动 WI-06、WI-07、WI-09、第四工程纪律或 Issue #71 的候选实施；
- 修改 Consumer 产品需求、架构或代码；
- 直接采用临时 eval manifest 作为正式 schema；
- 建立所有项目统一的固定目录模板；
- 要求 Consumer 保存全部 upstream 文档；
- 要求所有 Skill、Guide 或规则都存在于每个 Consumer；
- 将 `agentic-dev` 项目路线、提交语言等仓库自身规则自动投射给 Consumer；
- 用模型 token 降幅单独替代 Consumer 语义正确性与长期可维护性验收。

## 7. 完成定义

只有以下条件全部满足，v2 才可结束：

1. Consumer-local Runtime Target、发现层、规则 owner、路由与 Skill 激活边界形成一致设计；
2. 同一规范性规则只有一个长期语义 owner，Metadata / Catalog 只承担发现；
3. stale、missing、ambiguity、conflict 和 high-impact 边界均有明确 fail-closed 行为；
4. baseline adoption / upgrade 能选择性形成 Consumer-local 持久资产，并支持 adopt / retain-or-override / reject；
5. Consumer-native 项目规则与 adopted reusable rules 可以被同一本地发现入口协调，同时保持 Consumer Authority 优先；
6. 至少一个真实 Consumer 在 Fresh Context 中不依赖日常 upstream 读取，仍能正确发现规则、路由职责并按需执行 Skill；
7. Consumer 验证没有暴露需要回退设计阶段的 Blocking / Medium 通用缺口；
8. 当前方案没有引入第二套 Authority、机械 metadata 维护、全库复制或新的超级能力；
9. 最终 AI Review 未解决 Blocking / Medium Finding 为 `0 / 0`；
10. Project Roadmap、AGENTS、README 与必要的采用 / 使用入口能够让新的 `agentic-dev` 上下文恢复最终有效状态。

达到以上条件只表示本仓库变更具备进入人工集成决策的条件；合并仍由人工权威或仓库策略决定。
