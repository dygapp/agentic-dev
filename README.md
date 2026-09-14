---
id: repository:readme
type: repository
status: active
---

# agentic-dev

`agentic-dev` 是一个面向 AI Agent 驱动软件开发的 Method、可组合 Skill、分布式 Rule、Architecture 与 Consumer adoption 能力仓库。

## 两个入口，一套 canonical knowledge

本仓库明确区分 **Agent View** 与 **Human View**：

- **Agent View**：从根 `AGENTS.md` 启动，恢复 Project current state / capability instance，再通过 Method Selection、Skill discovery 与 Rule Discovery 进入规范资产；ordinary runtime 默认不依赖 Guide；
- **Human View**：从本 README 与 `docs/guides/using-agentic-dev.md` 开始，以适合人的方式理解项目、方法、流程和目录结构。

两种视窗共享同一套 canonical knowledge。Method / Architecture / Skill / Rule 是 reusable capability 的 semantic owners；Project Knowledge 持有 `agentic-dev` 自身使命、能力实例、Roadmap 与演进摘要；Guide / README 只负责解释和导航，不建立第二套 Authority。

## Project 与 Capability

当前信息架构遵守：

> **Project 不传播，Capability 传播。**

- `docs/project/**` 回答“`agentic-dev` 这个项目是什么、当前怎样实例化能力、走到哪里、为什么演进成今天这样”；
- `docs/architecture/**`、`docs/methods/**`、`skills/**`、`docs/rules/**` 与相应 tool contract 回答“哪些工程能力可以被其他 Repository adopt / adapt”。

Project Knowledge 的边界见 `docs/architecture/project-knowledge-architecture.md`，当前 Project owners 见 `docs/project/README.md`。

## 当前核心能力模型

### Method

Method 是一类复杂工作的规范过程模型。通用 Method 类型和 selection contract 由 `docs/architecture/method-architecture.md` 定义；`agentic-dev` 当前采用哪些 Method、怎样从 work kind 进入它们，由 `docs/project/project-capability-profile.md` 持有。

Human inventory 见 `docs/methods/README.md`。

### Skill

Skill 是责任明确后可独立调用的稳定、有界、可复用执行能力。当前 Skill 资源与 Human inventory 见 `skills/README.md`；通用 Skill identity / admission 见 `docs/architecture/skill-architecture.md`。

### Rule

Rule 是按当前工作事实条件性适用的 policy / constraint / default / invariant / completion requirement。Rule 不要求依附 Skill，并允许 Consumer-local specialization。

普通 Agent 使用当前 Project Capability Profile 声明的 Rule Discovery instance 获取少量候选 locator；人类可通过 `docs/rules/README.md` 浏览当前 Rule 结构与 inventory。

### Architecture

Architecture 定义可复用能力的类型、ownership、组合关系和运行不变量。入口见 `docs/architecture/README.md`。

### Guide

Guide 面向人类解释和使用。入口见 `docs/guides/README.md`。

## Agent Fresh Context

本仓库 Agent 工作从 `AGENTS.md` 恢复：

```text
Repository Authority
→ Project Roadmap + Project Capability Profile + GitHub current facts
→ Method Selection（若适用）
→ current responsibility
    ├─ Architecture
    ├─ Skill discovery
    └─ Rule Discovery
→ execute / verify
```

项目使命 / 核心项目需求只在当前任务需要时从 `project-charter.md` 加载；稳定历史原因只在需要时从 `project-evolution.md` 加载，不进入 ordinary runtime 固定上下文。

## Consumer

Consumer 始终拥有自己的 Repository Authority 与 Project Knowledge。显式 adoption / baseline upgrade 可以读取 upstream Project Knowledge 作为 provenance / context，但真正传播的是可复用 Capability：Method / Architecture / Skill / Rule / Tool contract。

采用完成后，Consumer 必须形成自己的 local capability instance、Method selector、Skill / Rule discovery 与 Roadmap；ordinary runtime 不在线依赖 `agentic-dev` current state。

## 当前结构

```text
AGENTS.md                     # Agent Bootstrap / Repository Authority
README.md                     # Human repository entry
skills/                       # reusable Agent execution capabilities
docs/
  methods/                    # reusable normative process models
  architecture/               # reusable capability boundaries / invariants
  rules/                      # discoverable conditional policies
  guides/                     # Human View / usage documentation
  project/                    # agentic-dev-local charter / profile / roadmap / evolution
  research/                   # non-normative evidence / references
evals/
tools/
  rule-discovery/
```

当前项目 baseline、evolution、Gate 与下一候选只以 `docs/project/project-roadmap.md` 和 GitHub 当前事实为准。