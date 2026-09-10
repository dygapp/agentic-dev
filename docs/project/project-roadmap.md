# 项目演进路线与当前状态

本文是 `agentic-dev` 仓库自身的 Project Roadmap，只维护**当前有效路线、活动里程碑、候选库、下一 Gate 与 Fresh Context 恢复入口**。

本文属于 `docs/project/*` 项目级 Authority，不覆盖更高优先级的方法、架构、契约、工程纪律或技术画像，也不得被 Consumer 自动继承。历史实施流水、精确 PR / Run / Review 证据由对应项目记录、Git、PR、Issue、Actions 与 `evals/` 保存；本文不重复维护完整历史证据。

## 1. 当前状态

长期阶段：

> **工程能力扩展与方法演进**

最近完成并已集成的有限里程碑：

> **规则治理与知识激活 v1**

当前活动有限里程碑：

> **规则治理与知识激活 v2 — Consumer-local 规则发现与激活**

跟踪入口：Issue #92  
启动基线：`master@b6a20053a7a6f4f53915bea8218604720412c302`  
当前阶段：**Phase G — 收敛与集成准备**

Phase A～E 已完成设计与 reusable guidance 收敛。Phase F 已在真实 Consumer `dygapp/jilinjobs-cms` 上完成 R1～R5，并在冻结 Candidate `ec945368678715732fe729c331bd3bcdd919bbdd` 上 PASS。

Phase G Final AI Review 随后修复两项 Medium：

1. Consumer-local Guide 的 upstream 冲突措辞；
2. `using-agentic-dev.md` 对 Skill-owned 过程语义的重复维护，并将跨职责验证规则归位到 `verification-evidence-rules.md`。

这些修复改变了 reusable Guide 集合，因此旧 Phase F Evidence 不能直接覆盖最终 Candidate。当前已冻结 reusable candidate：

`29f88efd25232e57ccb4a82ffff039be047e4d1e`

当前下一 Gate：

> **在既有 Consumer 实验状态上执行 T1～T4 定向重验，而不是重跑完整 R1～R5。**

影响映射与重验边界：

`docs/project/consumer-local-runtime-candidate-drift-review-v2.md`

通过后继续 Final AI Review 的受影响维度复核与稳定状态收敛。

## 2. v2 阶段状态

| 阶段 | 状态 | 结果 / 当前边界 |
|---|---|---|
| Phase A — Runtime Target / Acceptance | 已完成 | Consumer-local Target + CL-01～CL-12 |
| Phase B — Rule Ownership / Guide Decomposition | 已完成 | 单点 semantic owner；Guide 不按章节机械拆分 |
| Phase C — Metadata / Catalog Contract | 已完成 | `Activation Manifest → optional Runtime Catalog → local owner` |
| Phase D — Discovery / Routing / Skill Interface | 已完成 | 一个 primary responsibility + 最小 supporting set；routing-only 与 Skill execution 分离 |
| Phase E — Baseline Adoption / Projection | 已完成 | per-item adopt / override / reject / supersede；ordinary runtime local-only |
| Phase F — Real Consumer Validation | 已完成 / PASS | `jilinjobs-cms` R1～R5 PASS；ordinary runtime upstream access = 0 |
| Phase G — Convergence / Integration Readiness | **当前** | Candidate Drift T1～T4 → Final AI Review → stable-state convergence |

主要 Authority / Evidence：

- `docs/project/rule-governance-knowledge-activation-v2.md`
- `docs/project/consumer-local-runtime-validation-result-v2.md`
- `docs/project/consumer-local-runtime-candidate-drift-review-v2.md`
- PR #93
- Issue #92

## 3. Root Bootstrap 职责

为控制 Fresh Context 成本：

- `AGENTS.md`：稳定 Repository Governance、Authority Boundary 与 Agent 工作约束；**不维护当前项目状态**；
- `README.md`：简短当前状态与稳定导航；
- 本 Roadmap：详细阶段、活动里程碑、候选和下一 Gate；
- `docs/project/*`：具体里程碑、项目治理、设计和验证记录；
- Git / PR / Issue / Actions：精确外部状态与执行证据。

当前阶段、里程碑进展、候选路线、Issue / PR / Run、实验进展或下一工作项不得为了恢复上下文重新复制到 `AGENTS.md`。

## 4. 当前范围边界

Phase G 只允许完成 v2 的证据与一致性收敛，不继续扩展设计。

当前不启动：

- WI-06 — 第二及后续技术画像；
- WI-07 — 代码复核能力 v1；
- WI-09 — 运行时适配与分发；
- 第四 Engineering Discipline；
- Issue #71 候选实施；
- Runtime Rule Index 服务；
- 向量 / 图数据库、MCP 规则服务；
- 全仓统一 Front Matter；
- Rule Super Skill / Stage Router Skill；
- 新的 Runtime Eval 场景。

Consumer Phase F / T1～T4 都只是验证，不自动授权 Consumer 实验分支合并或正式 adoption。

## 5. 候选库

### WI-07 — 代码复核能力 v1

**优先后继候选，未启动。** 只有 v2 完成、取消或被取代后，由新的人工路线决策重新选择才可启动。

### WI-06 — 第二及后续技术画像

未启动。Spring / Spring Boot / Gradle / Element Plus 等继续作为候选；必须先有稳定、跨项目、会实质影响工程决策的知识缺口证据。

### WI-09 — 运行时适配与分发

未启动。Marketplace、Plugin Bundle、Controller、统一安装 / 分发和 Codex 多模型协同采用适配继续作为候选，不由 v2 自动扩张得到。

### Issue #71 — 模型路由与盲测对照证据

继续作为独立规划 / 研究输入，不构成常规 Method Gate、新 Skill 或默认模型策略。

其他候选包括第四 Engineering Discipline、第二次基础型 Existing Consumer adoption gate、可执行架构边界证据模式，以及 Issue #58 后续形成的跨项目能力候选。

## 6. 已完成里程碑索引

以下里程碑均已完成；普通 Fresh Context 不默认读取其完整过程记录：

1. 工程能力基础 v1 — `docs/project/engineering-capability-foundation-v1-closure.md`
2. 工程纪律扩展 v1 — `docs/project/engineering-discipline-expansion-v1*.md`
3. 中文交互与上下文清理 v1 — `docs/project/chinese-interaction-context-cleanup-v1.md`
4. 工程术语语义安全与现行文档收敛 v1 — `docs/project/terminology-semantic-safety-v1.md`
5. Squash Merge 下 Stacked PR 集成拓扑安全 v1 — `docs/project/stacked-pr-squash-topology-v1.md`
6. 规则治理与知识激活 v1 — `docs/project/rule-governance-knowledge-activation-v1.md`；历史 Issue #73 / PR #89

Issue #58 继续承担长期 Consumer feedback 入口。

## 7. Fresh Context 恢复顺序

新的 `agentic-dev` 上下文应：

1. 读取根 `AGENTS.md`，恢复稳定仓库治理与 Authority Boundary；
2. 读取根 `README.md`，取得简短当前状态；
3. 读取本文，确认当前活动里程碑、阶段和下一 Gate；
4. 重新读取当前 GitHub `master`、Open PR / Issue 和必要 Actions；
5. 当前 Phase G 定向重验 Gate 时，读取 Issue #92、PR #93、`docs/project/rule-governance-knowledge-activation-v2.md`、`consumer-local-runtime-validation-result-v2.md` 与 `consumer-local-runtime-candidate-drift-review-v2.md`；
6. 只有具体一致性复核需要时才读取 Phase A～E Contract、Guide、Skill / Architecture；不默认恢复 v1 完整历史或全部 eval 输出；
7. 不依赖其他聊天、历史会话或个人记忆补充未固化项目事实。

## 8. 更新触发

出现活动里程碑完成 / 取消 / 被取代、人工选择新里程碑、当前阶段或下一 Gate 实质变化、新能力正式集成，或高质量证据改变长期边界时更新本文。

单次 Run ID、临时分支删除等纯执行证据不为了记录而机械更新 Roadmap。