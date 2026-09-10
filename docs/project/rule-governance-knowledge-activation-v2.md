# 规则治理与知识激活 v2

## 状态

**活动有限里程碑 — Consumer 验证阶段**

当前阶段：

> **Phase F — 真实 Consumer 验证**

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

```text
Consumer-local Runtime Target
→ Discovery / Routing / Skill / Authority 机制
→ agentic-dev reusable capability / adoption model
```

Consumer 验证不是设计完成后的附加项，而是 v2 最终完成门禁。

### 2.2 单点 semantic owner

同一规范性规则只能有一个长期正文 owner。Metadata、Catalog、导航只保存发现所需的最小信息和 source pointer，不复制规则正文，也不形成第二套 Authority。

### 2.3 Adoption 后脱离日常 upstream

只有显式 baseline upgrade、Consumer 本地确实缺少必要方法 / Skill、明确 `agentic-dev` 实验，或 Consumer Authority 要求时才重新读取 upstream。

### 2.4 最小机制优先

当前没有证据要求 Runtime Rule Index 服务、向量 / 图数据库、MCP 规则服务、全仓统一 Front Matter、Rule Super Skill、大量专项 Skill 或固定 Consumer 目录模板。

## 3. 已接受证据边界

### 3.1 v1 基础

继续沿用 Consumer Repository Authority first、Progressive Disclosure、Evidence before claims、单点 Authority、derived discovery 可删除 / 可重建和 stale / ambiguity / high-impact fail-closed。

### 3.2 v2 临时 Runtime 证据

独立 `eval/*` 证据支持 Skill-first、metadata discovery 与 ambiguity routing 的可行性，但不授权原样产品化 eval manifest 或 Runtime Rule Index。

### 3.3 Consumer 现实证据

Issue #58 已证明：只存在 upstream、没有进入 Consumer-local Authority 的持续规则在普通 Fresh Context 中不可靠。因此 adoption 必须逐项 `adopt / retain-or-override / reject-not-applicable / supersede-remove`，并让 ordinary runtime 回到 local-only。

## 4. 已完成设计阶段

### Phase A — Consumer-local Runtime Target / Acceptance

**已完成。**

- `docs/project/consumer-local-rule-runtime-target-v2.md`
- `docs/project/consumer-local-rule-runtime-acceptance-v2.md`

### Phase B — Rule Ownership / Guide Decomposition

**已完成。**

- `docs/project/rule-ownership-decomposition-audit-v2.md`

Principle、核心 Skill、Engineering Discipline、Guide Rule Module、Platform capability 与 Consumer-native Authority 保持各自 semantic owner；Guide 不按章节机械拆分。

### Phase C — Minimal Metadata / Catalog Contract

**已完成。**

- `docs/project/consumer-local-activation-metadata-contract-v2.md`

采用 `Activation Manifest → optional Runtime Catalog → Consumer-local semantic owner`，并区分 `semantic-reviewed` 与 `current-locator` source binding。

### Phase D — Discovery → Routing → Skill Interface

**已完成。**

- `docs/project/consumer-local-runtime-routing-interface-v2.md`

冻结：一个 current primary responsibility + 最小 supporting constraints；`routing-only` 与 Skill execution 分离；Stage Return 后重新 routing；Runtime Adapter 不拥有 Method 语义。

### Phase E — Baseline Adoption / Consumer-local Projection

**已完成。**

- `docs/project/consumer-local-baseline-adoption-projection-v2.md`
- reusable Guide：`docs/guides/consumer-local-rule-activation.md`
- 薄导航：`docs/guides/rule-activation-guide.md`

冻结：

- `last evaluated upstream baseline` 与 active local asset 的 `adopted_from` 分离；
- adoption decision history 只在显式升级时使用；
- partial adoption / override / reject / supersede 可审计；
- adopted change 必须成为 Consumer-local current asset；
- ordinary runtime 不读取 upstream 或 upgrade history。

## 5. Root Bootstrap / AGENTS 职责收敛

v2 期间发现根 `AGENTS.md` 曾同时承载稳定仓库治理、当前里程碑 / 阶段、候选状态、方法摘要、复核细则、表达细则与 Research 生命周期，违背薄启动与 Progressive Disclosure。

已经实施：

- `AGENTS.md` 只保留稳定 Repository Governance、Authority Boundary 与 Agent 工作约束；
- `README.md` 承载简短当前状态；
- Project Roadmap 承载详细当前阶段、活动里程碑、候选和下一 Gate；
- Method / Principle / Architecture / Skill / Guide 恢复各自单点 semantic ownership；
- Git / PR / Issue / Actions 保存精确外部状态与证据；
- 当前阶段、里程碑进展、候选路线、Issue / PR 状态、实验进展和下一工作项不得重新堆入 `AGENTS.md`。

相对 v2 启动基线，`AGENTS.md` 已实现实质减法；Roadmap 也删除了大量默认恢复不需要的历史流水，只保留索引和当前路线。

这项结果同时成为 Phase F Consumer Bootstrap 的真实验证要求：Consumer-local adoption 不能通过不断把状态和 baseline 历史塞进 AGENTS / Bootstrap 来获得“可发现性”。

## 6. 当前 Phase F — 真实 Consumer 验证

验证 Authority：

`docs/project/consumer-local-runtime-validation-plan-v2.md`

首个真实 Consumer：

`dygapp/jilinjobs-cms`

其实际 Current State 必须在独立 Consumer Fresh Context 中重新从 GitHub 恢复；本文不维护 Consumer 当前阶段或提交状态。

Phase F 必须覆盖：

- **R1 Ordinary Fresh Context**：Consumer-native Authority + adopted reusable capability + 实际按需 Skill；
- **R2 Stage Return / Ambiguity / Routing-only**：正确 primary responsibility、无批量 Skill、local fail-closed；
- **R3 Consumer Override**：真实 Consumer-specific rule 优先于 reusable default；
- **R4 Baseline Upgrade Lifecycle**：adopt / retain-or-override / reject + evaluated baseline / adopted provenance 分离；
- **R5 Stale / Rebuild**：stale metadata fail-closed + derived Catalog 可删除 / 重建。

Consumer 验证还必须审计 AGENTS / Bootstrap 是否重复存在本项目刚刚修复的状态与 baseline-history 膨胀模式；如果存在，只能按 Consumer 自己的 Authority 做职责归位，不能机械套用 `agentic-dev` 文件结构。

Consumer Repository 的实际修改必须在 Consumer 自己授权的会话 / 分支中执行。本 `agentic-dev` 会话只提供候选 reusable baseline、验证要求和后续证据复核。

Phase F 完成条件：R1～R5 均取得可审计证据，且无未解决 Blocking / Medium reusable finding。否则结果必须是 INCONCLUSIVE / REJECT 或返回相应设计阶段，不能直接进入 Phase G。

## 7. Phase G — 收敛与集成准备

只有 Phase F PASS 后进入。

完成：

- v1 核心行为回归；
- Authority / Method / Architecture / Guide / Skill 一致性检查；
- Consumer-local validation evidence review；
- stale / fail-closed 回归；
- Root Bootstrap 职责回归；
- 最终 AI Review；
- README / Roadmap / 项目记录稳定状态收敛；
- 达到“已具备进入人工集成决策的条件”。

## 8. 完成定义

只有以下条件全部满足，v2 才可结束：

1. Consumer-local Runtime Target、discovery、semantic owner、routing 与 Skill activation 边界一致；
2. 同一规范性规则只有一个长期正文 owner；
3. stale / missing / ambiguity / conflict / high-impact 均有明确 fail-closed；
4. baseline adoption / upgrade 支持 adopt / retain-or-override / reject / supersede；
5. Consumer-native 与 adopted reusable asset 能由同一本地入口协调，同时保持 Consumer Authority 优先；
6. 至少一个真实 Consumer 在 ordinary Fresh Context 中不依赖 upstream 仍能正确发现、路由并按需执行 Skill；
7. Consumer 验证无未解决 Blocking / Medium reusable finding；
8. 没有第二套 Authority、机械 metadata 维护、全库复制或超级能力；
9. Root AGENTS / Bootstrap 保持稳定治理入口，不重新累积项目状态、baseline history 或重复方法正文；
10. 最终 AI Review 未解决 Blocking / Medium = `0 / 0`；
11. README、Roadmap、项目记录和 adoption / usage 入口能让新上下文恢复最终有效状态。

达到以上条件只表示已具备进入人工集成决策的条件；合并仍由人工权威或仓库策略决定。