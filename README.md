# agentic-dev

`agentic-dev` 是一个面向 AI Agent 驱动软件开发的方法体系、工程能力架构与可组合技能仓库。

## 快速开始

使用 `agentic-dev` 启动或继续真实项目时，先读取：

`docs/guides/rule-activation-guide.md`

它只负责把当前任务路由到最小必要的 Guide / Skill / Repository Authority；不要默认把完整 `agentic-dev` 规则栈或完整历史加载进上下文。

目标项目始终拥有自己的仓库权威、需求、架构、代码、测试和集成策略。`agentic-dev` 提供“如何工作”的可复用方法与能力，不替使用方仓库决定项目事实。

一个足够薄的 Fresh Context 可以是：

```text
这是一个 Fresh Context。

继续：<目标仓库>

GitHub Repository 是唯一项目事实来源。

开始后先读取当前仓库 AGENTS.md / README.md，并读取 agentic-dev 的规则激活导航；随后按当前 Repository Authority 恢复当前阶段和直接相关 Authority，从下一实际步骤继续。

<必要的本轮特殊约束，如有>
```

项目目标、当前工作入口或必要特殊约束可以按实际任务补充；不要为了“完整”复制 Repository Authority、Development Method 或详细规则正文，它们应从仓库中的当前权威来源读取。

## 当前状态

- **基线版本：** v0.1
- **长期阶段：** 工程能力扩展与方法演进
- **最近完成并已集成的有限里程碑：** 规则治理与知识激活 v1
- **当前路线状态：** 待人工决策
- **下一有限里程碑：** 尚未选择

当前没有活动有限里程碑。WI-07 — 代码复核能力 v1 仍是优先后继候选，但未启动；其他候选也不会因当前维护工作自动进入实施。

当前路线、已完成里程碑、候选库与 Fresh Context 恢复顺序只在以下入口维护详细状态：

`docs/project/project-roadmap.md`

Issue #73、PR #89 以及规则治理 v1 的阶段计划属于已完成里程碑的历史证据，不再是普通 Fresh Context 的当前工作入口。需要研究技术依据时，从 `docs/research/README.md` 选择与当前 Authority 或技术问题直接相关的材料，而不是恢复已关闭里程碑的完整过程文档。

## 仓库事实与权威

GitHub Repository 是本项目长期事实来源。完整 Repository Authority、知识边界、当前项目阶段和 `agentic-dev` 自身治理规则见：

`AGENTS.md`

使用方项目的规则激活入口见：

`docs/guides/rule-activation-guide.md`

完整使用说明仍保存在：

`docs/guides/using-agentic-dev.md`

只有当前任务实际触发对应主题时，才按导航读取相关章节或 Skill。

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

外部官方资料、成熟开源实践、专项评估和使用方证据可以成为研究输入，但不能自动覆盖 Repository Authority。研究材料位于：

`docs/research/`

## 中文表达

`agentic-dev` 自身面向人的内容默认使用自然中文；正式概念身份、例外和精确表达规则见：

`docs/guides/terminology-guidelines.md`

使用方项目的主导语言由使用方自己的仓库权威决定，不从 `agentic-dev`、旧聊天或其他项目机械继承。

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
