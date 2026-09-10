# 项目演进路线与当前状态

本文是 `agentic-dev` 仓库自身的 Project Roadmap，只维护**当前有效路线、活动里程碑、候选库、下一 Gate 与 Fresh Context 恢复入口**。

本文属于 `docs/project/*` 项目级 Authority，不覆盖更高优先级的方法、架构、契约、工程纪律或技术画像，也不得被 Consumer 自动继承。

历史实施流水、精确 PR / Run / Review 证据由对应项目记录、Git、PR、Issue、Actions 与 `evals/` 保存；本文不重复维护完整历史证据。

## 1. 当前长期阶段

当前长期阶段：

> **工程能力扩展与方法演进**

最近完成并已集成的有限里程碑：

> **规则治理与知识激活 v1**

当前活动有限里程碑：

> **规则治理与知识激活 v2 — Consumer-local 规则发现与激活**

人工选择日期：2026-09-10  
跟踪入口：Issue #92  
启动基线：`master@b6a20053a7a6f4f53915bea8218604720412c302`

当前阶段：

> **Phase D — Discovery → Routing → Skill 接口**

Phase A～C 已完成设计基线：

- Phase A：Consumer-local Runtime Target 与验收基线；
- Phase B：Rule Ownership / Guide Decomposition 审计；
- Phase C：最小 Activation Manifest / Runtime Catalog 契约。

当前下一实际 Gate：冻结 discovery → responsibility routing → routing-only / Skill execution → Stage Return / fail-closed 的最小运行接口，然后进入 Phase E baseline adoption / Consumer-local projection。

v2 项目级 Authority：

`docs/project/rule-governance-knowledge-activation-v2.md`

当前设计输入：

- `docs/project/consumer-local-rule-runtime-target-v2.md`
- `docs/project/consumer-local-rule-runtime-acceptance-v2.md`
- `docs/project/rule-ownership-decomposition-audit-v2.md`
- `docs/project/consumer-local-activation-metadata-contract-v2.md`

协调计划：

`tasks/plans/20260910/01-rule-governance-knowledge-activation-v2.md`

## 2. 当前路线状态

| 路线 | 状态 | 当前边界 |
|---|---|---|
| 核心方法 | 稳定维护 | 只有高质量通用证据揭示生命周期或 Authority 缺口时才定向修改 |
| 规则治理与知识激活 | **v2 当前** | Consumer-local-first；当前 Phase D，不直接产品化临时 eval 方案 |
| 使用方采用 | **v2 核心完成门禁** | 必须证明 adopted capability 可在 Consumer-local Repository 中持续发现和激活，ordinary runtime 不依赖 upstream |
| 工程纪律 | 已完成基础建设，可条件扩展 | 当前三项正式 Engineering Discipline；第四项未启动 |
| 技术画像 | 候选库 | 当前代表性画像为 Vue 3 + TypeScript；WI-06 未启动 |
| 任务型 Skill | 候选库 | WI-07 代码复核能力 v1 为优先后继候选，但不得在 v2 内提前启动 |
| 运行时与分发 | 候选库 | WI-09 未启动；v2 不扩张为通用分发平台 |
| 模型路由 / 盲测 | 研究候选 | Issue #71 继续独立，不与 v2 或代码复核合并为超级能力 |
| Consumer 长期反馈 | 持续开放 | Issue #58 继续作为跨项目泛化证据入口，不承担活动里程碑总控 |

## 3. 规则治理与知识激活 v2

### 3.1 核心目标

形成并验证一个能够被 Consumer **选择性采用、固化并长期独立运行**的 Consumer-local 规则发现与激活模型。

最终 ordinary Consumer runtime 应满足：

```text
Thin Consumer-local Bootstrap
→ Local Discovery
→ Applicable Rule / Responsibility Routing
→ 按需 Skill / Current Authority
→ Execute / Verify / Stage Return
```

其中不包含日常访问 `agentic-dev` upstream。

### 3.2 已完成设计阶段

#### Phase A — Consumer-local 目标模型与验收基线

已完成。

结果：

- `docs/project/consumer-local-rule-runtime-target-v2.md`
- `docs/project/consumer-local-rule-runtime-acceptance-v2.md`

确认 Consumer-native Authority 与 adopted reusable capability 可以进入同一本地发现路径，但必须保持来源身份和 Consumer Authority 优先；最终必须由真实 Consumer Fresh Context 验证。

#### Phase B — Rule Ownership / Guide Decomposition

已完成。

结果：

`docs/project/rule-ownership-decomposition-audit-v2.md`

确认 Principle、Skill、Engineering Discipline、Guide Rule Module、Platform-specific capability 与 Consumer-native Authority 必须保持单点 semantic owner；Guide 不能按章节机械拆分，Catalog 也不能复制规则正文。

#### Phase C — Minimal Metadata / Catalog Contract

已完成。

结果：

`docs/project/consumer-local-activation-metadata-contract-v2.md`

当前采用逻辑两层模型：

```text
Activation Manifest
→ optional derived Runtime Catalog
→ Consumer-local semantic owner
```

Manifest / Catalog 只承担发现，不成为第二套 Authority；semantic-reviewed source 变化必须重新复核 metadata，current-locator 只定位当前 Authority、不缓存其当前状态正文。

### 3.3 当前 Phase D

目标：冻结最小 Runtime Responsibility Interface，而不是创建新的 Stage Router / Rule Super Skill。

必须回答：

- task signal 如何映射到 primary responsibility；
- supporting context 如何参与但不夺取 primary responsibility；
- routing-only 何时可以不加载 Skill；
- 真正进入职责执行时何时加载 Skill；
- Stage Return 如何重新解析责任并使旧 routing / readiness 失效；
- 多个规则命中时如何得到最小充分集合；
- stale / missing / ambiguity / conflict / high-impact 情况如何 fail-closed；
- runtime adapter 如何只负责交付 / 发现 / 加载，而不拥有 Method 语义。

Phase D 完成后进入 Phase E。

### 3.4 后续阶段

```text
Phase D  Discovery / Routing / Skill Interface
→ Phase E Baseline Adoption / Consumer-local Projection
→ Phase F 真实 Consumer 验证
→ Phase G 收敛、回归、最终 AI Review 与集成准备
```

Phase F 是核心完成门禁，不是可选附加实验。Consumer Repository 的实际修改必须在 Consumer 自己的授权上下文中执行；`agentic-dev` 会话不得跨仓库静默修改 Consumer。

## 4. 根入口职责

为控制 Fresh Context 成本，当前根入口职责固定如下：

- `AGENTS.md`：稳定 Repository Governance、Authority Boundary 与 Agent 工作约束；不维护当前项目状态；
- `README.md`：简短当前状态与稳定导航；
- 本 Roadmap：详细当前阶段、活动里程碑、候选和下一 Gate；
- 具体 `docs/project/*`：里程碑设计与治理记录；
- Git / PR / Issue / Actions：精确外部状态和证据。

当前阶段、里程碑、候选、Issue / PR 状态或下一工作项不得为了 Fresh Context 方便重新复制到 `AGENTS.md`。

## 5. 已完成里程碑索引

以下项目均已完成；普通 Fresh Context 不默认读取其完整过程记录。

1. **工程能力基础 v1**  
   收尾：`docs/project/engineering-capability-foundation-v1-closure.md`
2. **工程纪律扩展 v1**  
   记录：`docs/project/engineering-discipline-expansion-v1.md`、`docs/project/engineering-discipline-expansion-v1-closure.md`
3. **中文交互与上下文清理 v1**  
   记录：`docs/project/chinese-interaction-context-cleanup-v1.md`
4. **工程术语语义安全与现行文档收敛 v1**  
   记录：`docs/project/terminology-semantic-safety-v1.md`
5. **Squash Merge 下 Stacked PR 集成拓扑安全 v1**  
   记录：`docs/project/stacked-pr-squash-topology-v1.md`
6. **规则治理与知识激活 v1**  
   记录：`docs/project/rule-governance-knowledge-activation-v1.md`；历史跟踪 Issue #73 / PR #89

Issue #33 的既有 Consumer 实验已关闭；Issue #58 继承长期 Consumer feedback 职责。

## 6. 候选库

以下均为候选，不因排序、编号或当前 v2 工作自动获得实施授权。

### WI-07 — 代码复核能力 v1

状态：**优先后继候选，未启动**。

只有在 v2 完成、取消或被取代后，由新的人工路线决策重新选择才可启动。候选职责仍是独立、高信噪比、受控上下文的代码复核；不得变成通用方法阶段或“复核一切”的超级 Skill。

### WI-06 — 第二及后续技术画像

未启动。Spring / Spring Boot / Gradle / Element Plus 等只保留为候选；必须先有跨项目、稳定、会实质影响工程决策的知识缺口证据。

### WI-09 — 运行时适配与分发

未启动。Marketplace、Plugin Bundle、Controller、统一安装 / 分发以及 Codex 多模型协同采用适配都继续保留为候选；不得由 v2 的 Consumer-local discovery 自动扩张得到。

### Issue #71 — 模型路由与盲测对照证据

继续作为独立规划 / 研究候选。当前不构成常规 Method Gate、新 Skill、模型路由框架或默认模型策略。

### 其他候选

- 第四 Engineering Discipline；
- 第二次基础型既有项目采用门禁；
- 可执行架构边界证据模式；
- Issue #58 后续形成的其他跨项目通用能力候选。

## 7. 当前边界

当前只推进 Issue #92 的 v2 范围。

不得因本里程碑静默启动：

- WI-06 / WI-07 / WI-09；
- 第四 Engineering Discipline；
- Issue #71 候选实施；
- Runtime Rule Index 服务；
- 向量 / 图数据库、MCP 规则服务；
- 全仓统一 Front Matter；
- Rule Super Skill；
- 机械拆分全部 Guide。

临时 `eval/*` 分支只保存设计证据，不是当前 Repository Authority。

## 8. Fresh Context 恢复顺序

新的 `agentic-dev` 工作上下文应：

1. 读取根 `AGENTS.md`，恢复稳定仓库治理与 Authority Boundary；
2. 读取根 `README.md`，取得简短当前状态；
3. 读取本文，确认当前活动里程碑、阶段和下一 Gate；
4. 读取当前 GitHub `master`、Open PR / Issue 和必要 Actions，确认是否存在更新的集成事实或人工路线决定；
5. 当前为 v2 时，读取 Issue #92 与 `docs/project/rule-governance-knowledge-activation-v2.md`；
6. 再按当前 Phase 只读取对应设计结果、Guide / Skill / Research / Consumer Evidence；
7. 已关闭里程碑、完整历史评估和全部 Research 不作为默认恢复输入；
8. 不依赖其他聊天、历史会话或个人记忆补充未固化项目事实。

## 9. 更新触发

出现以下情况时更新本文：

- 活动有限里程碑完成、取消或被取代；
- 人工选择新的有限里程碑；
- 当前阶段或下一 Gate 实质变化；
- 新能力正式集成并改变当前路线；
- 高质量证据改变候选优先级或现有长期边界。

精确合并提交、临时分支删除、单次 Run ID 等仅属于外部执行证据时，不为了记录它们机械更新 Roadmap。