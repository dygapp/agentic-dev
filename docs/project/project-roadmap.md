# 项目演进路线与当前状态

本文是 `agentic-dev` 仓库自身的 Project Roadmap，只维护**当前有效路线、活动状态、候选库、下一 Gate 与 Fresh Context 恢复入口**。

本文属于 `docs/project/*` 项目级 Authority，不覆盖更高优先级的方法、架构、契约、工程纪律或技术画像，也不得被 Consumer 自动继承。历史实施流水、精确 PR / Run / Review 证据由对应项目记录、Git、PR、Issue、Actions 与 `evals/` 保存；本文不重复维护完整历史证据。

## 1. 当前状态

长期阶段：

> **工程能力扩展与方法演进**

规则治理与知识激活 v2 当前状态：

> **内部完成定义已满足，已具备进入人工集成决策的条件。**

跟踪入口：Issue #92 / PR #93  
启动基线：`master@b6a20053a7a6f4f53915bea8218604720412c302`

v2 已完成 Phase A～G：

- Consumer-local Runtime Target / Acceptance；
- Rule Ownership / Guide Decomposition；
- Minimal Metadata / Catalog Contract；
- Discovery / Routing / Skill Interface；
- Baseline Adoption / Consumer-local Projection；
- 真实 Consumer Phase F R1～R5；
- Phase G Candidate Drift 定向重验与 Final AI Review 收敛；
- Root Bootstrap / `AGENTS.md` 职责瘦身。

最终冻结 reusable candidate：

`29f88efd25232e57ccb4a82ffff039be047e4d1e`

真实 Consumer `dygapp/jilinjobs-cms` 的 Phase F R1～R5 全部 PASS；随后针对 reusable Guide drift 完成 T1～T4 定向重验，最终 Head `c29da21b41ff3ddad023ecb64e3628dc3136a77e`，ordinary runtime upstream access = 0，Blocking / Medium reusable findings = `0 / 0`。

当前下一 Gate：

> **只剩人工集成决策。**

是否已经实际集成 v2，以 Git / PR #93 当前事实为准；Roadmap 不复制“PR 已打开 / 已合并”等瞬时状态。无论集成结果如何，当前都不会自动启动新的有限里程碑。

## 2. v2 阶段结果

| 阶段 | 状态 | 结果 |
|---|---|---|
| Phase A — Runtime Target / Acceptance | 已完成 | Consumer-local Target + CL-01～CL-12 |
| Phase B — Rule Ownership / Guide Decomposition | 已完成 | 单点 semantic owner；Guide 不按章节机械拆分 |
| Phase C — Metadata / Catalog Contract | 已完成 | `Activation Manifest → optional Runtime Catalog → local owner` |
| Phase D — Discovery / Routing / Skill Interface | 已完成 | 一个 primary responsibility + 最小 supporting set；routing-only 与 Skill execution 分离 |
| Phase E — Baseline Adoption / Projection | 已完成 | per-item adopt / override / reject / supersede；ordinary runtime local-only |
| Phase F — Real Consumer Validation | 已完成 / PASS | `jilinjobs-cms` R1～R5 PASS；ordinary runtime upstream access = 0 |
| Phase G — Convergence / Integration Readiness | 已完成 | T1～T4 PASS；Final AI Review 收敛；已具备人工集成决策条件 |

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
- 本 Roadmap：详细项目路线、当前 Gate 与候选库；
- `docs/project/*`：具体里程碑、项目治理、设计和验证记录；
- Git / PR / Issue / Actions：精确外部状态与执行证据。

当前阶段、里程碑进展、候选路线、Issue / PR / Run、实验进展或下一工作项不得为了恢复上下文重新复制到 `AGENTS.md`。

## 4. 当前范围边界

v2 已停止扩展设计。当前不因 v2 自动启动：

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

**优先后继候选，未启动。** 只能在 v2 集成决策完成后，由新的人工路线决策重新选择；候选优先级本身不授予启动权限。

### WI-06 — 第二及后续技术画像

未启动。Spring / Spring Boot / Gradle / Element Plus 等继续作为候选；必须先有稳定、跨项目、会实质影响工程决策的知识缺口证据。

### WI-09 — 运行时适配与分发

未启动。Marketplace、Plugin Bundle、Controller、统一安装 / 分发和 Codex 多模型协同采用适配继续作为候选，不由 v2 自动扩张得到。

### Issue #71 — 模型路由与盲测对照证据

继续作为独立规划 / 研究输入，不构成常规 Method Gate、新 Skill 或默认模型策略。

其他候选包括第四 Engineering Discipline、第二次基础型 Existing Consumer adoption gate、可执行架构边界证据模式，以及 Issue #58 后续形成的跨项目能力候选。

## 6. 已完成里程碑索引

普通 Fresh Context 不默认读取以下已完成工作的完整过程记录：

1. 工程能力基础 v1 — `docs/project/engineering-capability-foundation-v1-closure.md`
2. 工程纪律扩展 v1 — `docs/project/engineering-discipline-expansion-v1*.md`
3. 中文交互与上下文清理 v1 — `docs/project/chinese-interaction-context-cleanup-v1.md`
4. 工程术语语义安全与现行文档收敛 v1 — `docs/project/terminology-semantic-safety-v1.md`
5. Squash Merge 下 Stacked PR 集成拓扑安全 v1 — `docs/project/stacked-pr-squash-topology-v1.md`
6. 规则治理与知识激活 v1 — `docs/project/rule-governance-knowledge-activation-v1.md`
7. 规则治理与知识激活 v2 — `docs/project/rule-governance-knowledge-activation-v2.md`；其实际集成状态以 PR #93 / Git 为准

Issue #58 继续承担长期 Consumer feedback 入口。

## 7. Fresh Context 恢复顺序

新的 `agentic-dev` 上下文应：

1. 读取根 `AGENTS.md`，恢复稳定仓库治理与 Authority Boundary；
2. 读取根 `README.md`，取得简短当前状态；
3. 读取本文，确认当前路线、Gate 和候选边界；
4. 重新读取当前 GitHub `master`、Open PR / Issue 和必要 Actions；
5. 如果 PR #93 尚未集成，只在需要审查 v2 候选时读取 Issue #92、PR #93 与 v2 Evidence；如果已经集成，则把 v2 视为已完成能力基线；
6. 后续只有新的人工路线决策才能启动候选库中的下一有限里程碑；
7. 不依赖其他聊天、历史会话或个人记忆补充未固化项目事实。

## 8. 更新触发

出现人工选择新里程碑、当前路线或下一 Gate 实质变化、新能力正式集成且其集成事实会改变长期路线，或高质量证据改变长期边界时更新本文。

单次 Run ID、临时分支删除、PR 从 Draft 变为 Ready、PR 合并提交等纯 GitHub 原生状态，不为了记录而机械更新 Roadmap；需要时直接从 Git / PR / Issue 恢复。
