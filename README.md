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
- **最近已集成里程碑：** 规则治理与知识激活 v2
- **当前活动规划里程碑：** 规则治理与知识激活 v3 — 知识与能力所有权收敛
- **总体跟踪：** Issue #94
- **已完成并集成：** V3-01 — 知识与能力所有权模型；V3-02 — 当前仓库所有权审计
- **当前活动子任务：** Issue #104 — V3-03 Consumer 初始化、采用、升级与普通运行生命周期
- **当前候选：** PR #106（Draft）— `docs/architecture/consumer-lifecycle.md`

V3-03 正在把 V3-02 已识别的 Consumer lifecycle 规则族收敛到单一长期 owner，重点区分新 Consumer 首次采用、Existing Consumer baseline upgrade、逐项 adoption decision、采用验收 / baseline advance、ordinary-runtime local-only 与显式 upstream re-entry。

V3-02 的其他 disposition 仍只是后续设计输入。V3-03 不执行 Guide 物理迁移、Skill 重构、Front Matter / Index 实现、完整 discovery architecture 或 Consumer 修改。

详细当前路线、候选与下一 Gate 统一维护在：

`docs/project/project-roadmap.md`

v3 当前规划 / 审计 / lifecycle 入口：

- `docs/project/rule-governance-knowledge-activation-v3.md`
- `docs/project/knowledge-capability-ownership-model-v3.md`
- `docs/project/current-repository-ownership-audit-v3.md`
- `docs/architecture/consumer-lifecycle.md`

v3 规划期间，v2 已验证的 Consumer-local 普通运行和当前 discovery / activation 入口继续有效；不因为 v3 正在演进就提前替换现行运行行为。

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

Consumer 初始化、首次采用、baseline upgrade、采用验收、ordinary runtime 与 upstream re-entry 的长期 lifecycle 候选见：

`docs/architecture/consumer-lifecycle.md`

跨职责验证与证据条件规则见：

`docs/guides/verification-evidence-rules.md`

完整使用说明见：

`docs/guides/using-agentic-dev.md`

V3-02 已完成对上述现有入口的语义所有权审计；在后续真实 owner / replacement 经设计、验证并正式集成前，v2 Guide / activation 入口继续保持现行兼容，不提前删除或改写其运行语义。

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

Consumer lifecycle 的当前 V3-03 规范候选见：

`docs/architecture/consumer-lifecycle.md`

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
