# agentic-dev

`agentic-dev` 是一个面向 AI Agent 驱动软件开发的方法体系、工程能力架构与可组合 Skill 仓库。

## 快速开始

使用 `agentic-dev` 启动、采用或升级真实 Consumer 项目时，先读取：

`docs/guides/rule-activation-guide.md`

它只负责把低频初始化 / 首次采用 / 基线升级 / 实验 / Consumer-local 普通运行带到正确入口，不再承担 ordinary runtime 的手工职责路由。

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
- **已完成并集成：** V3-01 — 知识与能力所有权模型；V3-02 — 当前仓库所有权审计；V3-03 — 使用方初始化、采用、升级与普通运行生命周期；V3-04 — 技能重分类与准入；V3-05 — 面向 Agent 的结构化资源模型；V3-06 — 资源发现架构
- **V3-07 跟踪入口：** Issue #113 — `agentic-dev` 自采用与发现机制切换
- **V3-07 工作产物：** `docs/discovery/README.md`、`docs/discovery/reviewed-discovery-map.md`、`docs/project/rule-governance-v3-v3-07-self-adoption.md`

V3-07 把已集成的使用方生命周期、资源模型与资源发现架构投射到 `agentic-dev` 自身真实仓库状态。当前 self-runtime 采用：

```text
Local Discovery Entry
+ Reviewed Discovery Map
```

当前没有真实证据要求额外 Runtime View / Catalog / generator。

V3-07 的精确审查、集成与完成状态以 Issue #113 和当前 GitHub 状态为准，不在 README 复制瞬时 PR 状态。Issue #113 完成后，V3-08 只成为下一规划候选，不自动启动。

V3-07 不修改 Consumer Repository，不创建 Rule Super Skill / Stage Router / Runtime Controller，也不把 `agentic-dev` 自身 `docs/discovery/*` 自动投射给 Consumer。

详细当前路线、候选与下一门禁统一维护在：

`docs/project/project-roadmap.md`

v3 当前规划 / 审计 / 架构 / 自采用入口：

- `docs/project/rule-governance-knowledge-activation-v3.md`
- `docs/project/knowledge-capability-ownership-model-v3.md`
- `docs/project/current-repository-ownership-audit-v3.md`
- `docs/architecture/consumer-lifecycle.md`
- `docs/project/skill-reclassification-admission-v3.md`
- `docs/architecture/agent-resource-model.md`
- `docs/architecture/resource-discovery-architecture.md`
- `docs/project/rule-governance-v3-v3-07-self-adoption.md`
- `docs/discovery/README.md`

## 入口职责

为避免启动上下文膨胀，根入口职责明确分离：

- `AGENTS.md`：只维护稳定 Repository Governance、Authority Boundary 与 Agent 工作约束；**不维护当前阶段、里程碑进展、候选路线、Issue / PR 状态或下一工作项**；
- `README.md`：维护面向人的简短当前状态与稳定导航；
- `docs/project/project-roadmap.md`：维护详细项目路线、活动状态、候选库和下一 Gate；
- `docs/discovery/README.md`：`agentic-dev` 自身普通运行的 Local Discovery Entry；
- `docs/discovery/reviewed-discovery-map.md`：非规范性、需复核维护的跨资源发现映射；
- `docs/project/*`：维护具体里程碑、项目治理、设计与验证记录；
- Git / PR / Issue / Actions：维护精确外部状态与执行证据。

发生当前状态变化时优先更新 README / Roadmap / 对应项目记录，不把状态性正文复制回 `AGENTS.md`，也不把当前项目状态复制进 Reviewed Discovery Map。

## 仓库事实与权威

GitHub Repository 是本项目长期事实来源。

稳定 Repository Authority、知识边界和仓库级 Agent 约束见：

`AGENTS.md`

当前项目路线和恢复顺序见：

`docs/project/project-roadmap.md`

`agentic-dev` 自身普通运行的本地发现入口见：

`docs/discovery/README.md`

其 Reviewed Discovery Map 见：

`docs/discovery/reviewed-discovery-map.md`

该 Map 是派生发现输入，不是新的 Authority；冲突时真实 semantic owner 优先。

Consumer 初始化 / 采用 / 升级导航见：

`docs/guides/rule-activation-guide.md`

完成采用后的 Consumer-local 落地说明见：

`docs/guides/consumer-local-rule-activation.md`

使用方初始化、首次采用、基线升级、采用验证、普通运行与重新进入上游的长期生命周期见：

`docs/architecture/consumer-lifecycle.md`

当前长期资源语义与最小结构契约见：

`docs/architecture/agent-resource-model.md`

当前长期本地资源发现与职责路由架构见：

`docs/architecture/resource-discovery-architecture.md`

跨职责验证与证据条件规则见：

`docs/guides/verification-evidence-rules.md`

完整使用说明见：

`docs/guides/using-agentic-dev.md`

`docs/discovery/*` 只属于 `agentic-dev` 自身本地运行状态，不自动成为 Consumer 资源。Consumer 完成采用后必须建立或复用自己的 Local Discovery Entry，并按自身复杂度判断是否需要 Reviewed Discovery Map / Runtime View。

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

使用方生命周期见：

`docs/architecture/consumer-lifecycle.md`

Agent 资源模型见：

`docs/architecture/agent-resource-model.md`

资源发现架构见：

`docs/architecture/resource-discovery-architecture.md`

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
│   ├── architecture/
│   ├── decisions/
│   ├── discovery/
│   ├── guides/
│   ├── method/
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
