# agentic-dev

`agentic-dev` 是一个面向 AI Agent 驱动软件开发的方法体系、工程能力架构与可组合 Skill 仓库。

## 快速开始

使用 `agentic-dev` 启动或继续真实项目时，先读取：

`docs/guides/rule-activation-guide.md`

它只负责把当前任务路由到最小必要的 Guide / Skill / Repository Authority；不要默认把完整 `agentic-dev` 规则栈或完整历史加载进上下文。

目标项目始终拥有自己的仓库权威、需求、架构、代码、测试和集成策略。`agentic-dev` 提供“如何工作”的可复用方法与能力，不替 Consumer 决定项目事实。

一个足够薄的 Fresh Context 可以是：

```text
这是一个 Fresh Context。

继续：<目标仓库>

GitHub Repository 是唯一项目事实来源。

开始后先读取当前仓库 AGENTS.md / README.md；随后按当前 Repository Authority 恢复当前阶段和直接相关 Authority，从下一实际步骤继续。

<必要的本轮特殊约束，如有>
```

项目目标、当前工作入口或必要特殊约束可以按实际任务补充；不要为了“完整”复制 Repository Authority、Development Method 或详细规则正文，它们应从仓库中的当前权威来源读取。

## 当前状态

- **基线版本：** v0.1
- **长期阶段：** 工程能力扩展与方法演进
- **规则治理与知识激活 v2：** 内部完成定义已满足，已具备进入人工集成决策的条件
- **跟踪入口：** Issue #92 / PR #93

v2 已完成 Consumer-local Runtime Target、Rule Ownership / Guide Decomposition、Activation Manifest / Runtime Catalog 契约、Discovery / Routing / Skill Interface、Baseline Adoption / Projection、真实 Consumer Phase F R1～R5 以及 Phase G Candidate Drift 定向重验。

真实 Consumer `dygapp/jilinjobs-cms` 的 ordinary runtime upstream access 保持为 0；最终定向重验 T1～T4 全部 PASS，Blocking / Medium reusable findings 为 `0 / 0`。冻结 reusable candidate：

`29f88efd25232e57ccb4a82ffff039be047e4d1e`

详细证据：

- `docs/project/consumer-local-runtime-validation-result-v2.md`
- `docs/project/consumer-local-runtime-candidate-drift-review-v2.md`
- `docs/project/rule-governance-knowledge-activation-v2.md`

是否已经实际集成 v2，不由 README 复制瞬时 PR 状态；以 Git / PR #93 的当前事实为准。无论 PR 是否已经集成，v2 都不会自动启动 WI-06、WI-07、WI-09、Issue #71 或其他候选，后续仍需要新的人工路线决策。

详细当前路线、候选与下一 Gate 统一维护在：

`docs/project/project-roadmap.md`

## 入口职责

为避免启动上下文膨胀，根入口职责明确分离：

- `AGENTS.md`：只维护稳定 Repository Governance、Authority Boundary 与 Agent 工作约束；**不维护当前阶段、里程碑进展、候选路线、Issue / PR 状态或下一工作项**；
- `README.md`：维护面向人的简短当前状态与稳定导航；
- `docs/project/project-roadmap.md`：维护详细项目路线、活动状态、候选库和下一 Gate；
- `docs/project/*`：维护具体里程碑、项目治理、设计与验证记录；
- Git / PR / Issue / Actions：维护精确外部状态与执行证据。

发生当前状态变化时优先更新 README / Roadmap / 对应项目记录，不把状态性正文复制回 `AGENTS.md`。

## 仓库事实与权威

GitHub Repository 是本项目长期事实来源。

稳定 Repository Authority、知识边界和仓库级 Agent 约束见：

`AGENTS.md`

当前项目路线和恢复顺序见：

`docs/project/project-roadmap.md`

Consumer 规则激活入口见：

`docs/guides/rule-activation-guide.md`

完成 baseline adoption 后的 Consumer-local 规则发现与激活见：

`docs/guides/consumer-local-rule-activation.md`

跨职责验证与证据条件规则见：

`docs/guides/verification-evidence-rules.md`

完整使用说明见：

`docs/guides/using-agentic-dev.md`

只有当前任务实际触发对应主题时，才按导航读取相关 Guide、Authority 或 Skill。

## 核心开发路径

常规功能工作通常沿以下职责推进：

```text
治理与领域上下文
→ 澄清意图
→ 规格说明
→ 按需技术规划
→ 工作切分
→ 就绪检查
→ 新上下文执行
→ 整体收敛
→ 已具备进入集成决策的条件
→ 人工权威或仓库策略
```

独立缺陷使用更轻的复现、根因、最小修复与回归路径。

完整方法以 `docs/method/ai-development-method.md` 和当前架构 / 契约权威为准；README 不维护第二份方法定义。

## 工程能力

Skill 清单、身份和职责边界统一维护在：

`skills/README.md`

工程能力分层、证据进入方式和长期生命周期统一维护在：

`docs/architecture/engineering-capability-architecture.md`

外部官方资料、成熟开源实践、专项评估和 Consumer 证据可以成为研究输入，但不能自动覆盖 Repository Authority。研究入口：

`docs/research/README.md`

## 中文表达

`agentic-dev` 自身面向人的内容默认使用自然中文；正式概念身份、例外和精确表达规则见：

`docs/guides/terminology-guidelines.md`

Consumer 的主导语言由其自己的 Repository Authority 决定，不从 `agentic-dev`、旧聊天或其他项目机械继承。

## 仓库结构

```text
.
├── AGENTS.md
├── README.md
├── docs/
│   ├── method/
│   ├── architecture/
│   ├── decisions/
│   ├── guides/
│   ├── project/
│   ├── research/
│   └── technology-profiles/
├── skills/
├── evals/
└── tasks/
```

## Git 提交

提交信息遵循：

`docs/guides/git-commit-guidelines.md`
