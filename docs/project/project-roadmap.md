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

> **Phase G — 收敛与集成准备**

Phase A～E 已完成设计与 reusable guidance 收敛；Phase F 已在真实 Consumer `dygapp/jilinjobs-cms` 完成 R1～R5 验证并 PASS。当前下一实际 Gate 是执行 v1 核心行为、Authority / Method / Architecture / Guide / Skill、stale / fail-closed、Root Bootstrap 回归与 Final AI Review；全部通过后达到“已具备进入人工集成决策的条件”。

v2 项目级 Authority：

`docs/project/rule-governance-knowledge-activation-v2.md`

Phase F 结果：

`docs/project/consumer-local-runtime-validation-result-v2.md`

协调计划：

`tasks/plans/20260910/01-rule-governance-knowledge-activation-v2.md`

## 2. 当前路线状态

| 路线 | 状态 | 当前边界 |
|---|---|---|
| 核心方法 | 稳定维护 | 只有高质量通用证据揭示生命周期或 Authority 缺口时才定向修改 |
| 规则治理与知识激活 | **v2 当前 / Phase G** | A～F 已完成；当前只做最终回归、AI Review 与稳定状态收敛，不继续扩展设计范围 |
| 使用方采用 | **核心完成门禁已通过** | `jilinjobs-cms` Phase F R1～R5 PASS，ordinary runtime upstream access = 0；实验不等于正式 Consumer adoption |
| 工程纪律 | 已完成基础建设，可条件扩展 | 当前三项正式 Engineering Discipline；第四项未启动 |
| 技术画像 | 候选库 | 当前代表性画像为 Vue 3 + TypeScript；WI-06 未启动 |
| 任务型 Skill | 候选库 | WI-07 代码复核能力 v1 为优先后继候选，但不得在 v2 内提前启动 |
| 运行时与分发 | 候选库 | WI-09 未启动；v2 不扩张为通用分发平台 |
| 模型路由 / 盲测 | 研究候选 | Issue #71 继续独立，不与 v2 或代码复核合并为超级能力 |
| Consumer 长期反馈 | 持续开放 | Issue #58 继续作为跨项目泛化证据入口，不承担活动里程碑总控 |

## 3. 规则治理与知识激活 v2

### 3.1 核心目标

形成并验证一个能够被 Consumer **选择性采用、固化并长期独立运行**的 Consumer-local 规则发现与激活模型。

目标 ordinary Consumer runtime：

```text
Thin Consumer-local Bootstrap
→ Local Discovery
→ Applicable Rule / Responsibility Routing
→ 按需 Skill / Current Authority
→ Execute / Verify / Stage Return
```

其中不包含日常访问 `agentic-dev` upstream。

### 3.2 Phase A — Consumer-local Target / Acceptance

**已完成。**

- `docs/project/consumer-local-rule-runtime-target-v2.md`
- `docs/project/consumer-local-rule-runtime-acceptance-v2.md`

确认 Consumer-native Authority 与 adopted reusable capability 可以进入同一本地发现路径，但必须保持来源身份和 Consumer Authority 优先。

### 3.3 Phase B — Rule Ownership / Guide Decomposition

**已完成。**

`docs/project/rule-ownership-decomposition-audit-v2.md`

确认 Principle、Skill、Engineering Discipline、Guide Rule Module、Platform-specific capability 与 Consumer-native Authority 保持单点 semantic owner；Guide 不按章节机械拆分，Catalog 不复制规则正文。

### 3.4 Phase C — Minimal Metadata / Catalog Contract

**已完成。**

`docs/project/consumer-local-activation-metadata-contract-v2.md`

采用：

```text
Activation Manifest
→ optional derived Runtime Catalog
→ Consumer-local semantic owner
```

`semantic-reviewed` metadata 在 source 语义变化后必须重新复核；`current-locator` 只定位 Current Authority，不缓存易变化状态正文。

### 3.5 Phase D — Discovery → Routing → Skill Interface

**已完成。**

`docs/project/consumer-local-runtime-routing-interface-v2.md`

最小模型：一个 current primary responsibility + 最小 supporting constraints。`routing-only` 与 Skill execution 分离；Stage Return 后重新 routing；Runtime Adapter 只负责 discovery / delivery / loading，不拥有 Method 语义。

### 3.6 Phase E — Baseline Adoption / Consumer-local Projection

**已完成。**

- `docs/project/consumer-local-baseline-adoption-projection-v2.md`
- reusable Guide：`docs/guides/consumer-local-rule-activation.md`
- 上游薄导航：`docs/guides/rule-activation-guide.md`

关键边界：

- `last evaluated upstream baseline` 与每个 active local asset 的 `adopted_from` 分离；
- adoption decision history 只在显式升级时读取，不进入 ordinary Fresh Context；
- `adopt / retain-or-override / reject-not-applicable / supersede-remove` 逐项决定；
- adopted change 必须落成 Consumer-local current asset；
- upstream `docs/project/*`、Roadmap、Issue / PR 状态和 Research / Eval 过程不投射为 Consumer runtime Authority。

### 3.7 Phase F — 真实 Consumer 验证

**已完成，PASS。**

结果：

`docs/project/consumer-local-runtime-validation-result-v2.md`

真实 Consumer：`dygapp/jilinjobs-cms`。

R1～R5 全部 PASS；ordinary runtime upstream access = 0；Base Drift = NO IMPACT；Blocking / Medium reusable Rule Governance v2 finding = NONE。实验同时验证了 Consumer Bootstrap 职责归位、Consumer-native locator、adopted Guide、按需 local Skill、Consumer override、baseline lifecycle 和 stale / Catalog rebuild。

Phase F 只是验证证据，不授权 Consumer 实验分支合并或正式 adoption。

### 3.8 当前 Phase G — 收敛与集成准备

当前只执行：

1. v1 核心不变量与 fail-closed 边界回归；
2. Authority / Method / Architecture / Guide / Skill 一致性检查；
3. Consumer Phase F Current Evidence 复核；
4. Root Bootstrap / `AGENTS.md` 职责回归；
5. Final AI Review；
6. README / Roadmap / Issue / PR 稳定状态收敛。

不得在 Phase G 再引入新的 Runtime Index、metadata taxonomy、Guide 拆分、Skill 或 Consumer 产品变更。

## 4. 根入口职责

为控制 Fresh Context 成本，根入口职责固定如下：

- `AGENTS.md`：稳定 Repository Governance、Authority Boundary 与 Agent 工作约束；不维护当前项目状态；
- `README.md`：简短当前状态与稳定导航；
- 本 Roadmap：详细当前阶段、活动里程碑、候选和下一 Gate；
- 具体 `docs/project/*`：里程碑设计与治理记录；
- Git / PR / Issue / Actions：精确外部状态和证据。

当前阶段、里程碑、候选、Issue / PR 状态、实验进展或下一工作项不得为了 Fresh Context 方便重新复制到 `AGENTS.md`。

## 5. 已完成里程碑索引

以下项目均已完成；普通 Fresh Context 不默认读取其完整过程记录。

1. **工程能力基础 v1** — `docs/project/engineering-capability-foundation-v1-closure.md`
2. **工程纪律扩展 v1** — `docs/project/engineering-discipline-expansion-v1.md`、`docs/project/engineering-discipline-expansion-v1-closure.md`
3. **中文交互与上下文清理 v1** — `docs/project/chinese-interaction-context-cleanup-v1.md`
4. **工程术语语义安全与现行文档收敛 v1** — `docs/project/terminology-semantic-safety-v1.md`
5. **Squash Merge 下 Stacked PR 集成拓扑安全 v1** — `docs/project/stacked-pr-squash-topology-v1.md`
6. **规则治理与知识激活 v1** — `docs/project/rule-governance-knowledge-activation-v1.md`；历史跟踪 Issue #73 / PR #89

Issue #33 的既有 Consumer 实验已关闭；Issue #58 继承长期 Consumer feedback 职责。

## 6. 候选库

以下均为候选，不因排序、编号或当前 v2 工作自动获得实施授权。

### WI-07 — 代码复核能力 v1

状态：**优先后继候选，未启动**。只有在 v2 完成、取消或被取代后，由新的人工路线决策重新选择才可启动。

### WI-06 — 第二及后续技术画像

未启动。Spring / Spring Boot / Gradle / Element Plus 等只保留为候选；必须先有跨项目、稳定、会实质影响工程决策的知识缺口证据。

### WI-09 — 运行时适配与分发

未启动。Marketplace、Plugin Bundle、Controller、统一安装 / 分发以及 Codex 多模型协同采用适配继续保留为候选；不得由 v2 的 Consumer-local discovery 自动扩张得到。

### Issue #71 — 模型路由与盲测对照证据

继续作为独立规划 / 研究候选。当前不构成常规 Method Gate、新 Skill、模型路由框架或默认模型策略。

其他候选包括第四 Engineering Discipline、第二次基础型既有项目采用门禁、可执行架构边界证据模式，以及 Issue #58 后续形成的其他跨项目通用能力候选。

## 7. 当前边界

当前只推进 Issue #92 的 Phase G 收敛。

不得因本里程碑静默启动 WI-06 / WI-07 / WI-09、第四 Engineering Discipline、Issue #71 候选实施、Runtime Rule Index 服务、向量 / 图数据库、MCP 规则服务、全仓统一 Front Matter、Rule Super Skill 或机械拆分全部 Guide。

临时 `eval/*` 分支只保存设计证据，不是 Current Repository Authority。

## 8. Fresh Context 恢复顺序

新的 `agentic-dev` 工作上下文应：

1. 读取根 `AGENTS.md`，恢复稳定仓库治理与 Authority Boundary；
2. 读取根 `README.md`，取得简短当前状态；
3. 读取本文，确认当前活动里程碑、阶段和下一 Gate；
4. 读取当前 GitHub `master`、Open PR / Issue 和必要 Actions，确认是否存在更新的集成事实或人工路线决定；
5. 当前为 v2 Phase G 时，读取 Issue #92、PR #93、`docs/project/rule-governance-knowledge-activation-v2.md` 与 `docs/project/consumer-local-runtime-validation-result-v2.md`；
6. 只在 Final Review 的具体维度需要时读取对应 Design Contract、Guide、Skill / Architecture；不默认恢复 v1 完整历史或全部 eval 输出；
7. 不依赖其他聊天、历史会话或个人记忆补充未固化项目事实。

## 9. 更新触发

出现以下情况时更新本文：活动有限里程碑完成、取消或被取代；人工选择新的有限里程碑；当前阶段或下一 Gate 实质变化；新能力正式集成并改变当前路线；高质量证据改变候选优先级或现有长期边界。

精确单次 Run ID、临时分支删除等只属于外部执行证据时，不为了记录它们机械更新 Roadmap。