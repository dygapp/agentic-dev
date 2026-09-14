---
id: repository:readme
type: repository
status: active
---

# agentic-dev

`agentic-dev` 是一个面向 AI Agent 驱动软件开发的 Method、可组合 Skill、分布式 Rule、Architecture 与 Consumer adoption 能力仓库。

## 两个入口

本仓库明确区分 **Agent View** 与 **Human View**：

- **Agent View**：从根 `AGENTS.md` 启动，通过 Method Selection、Skill discovery 与 Rule Discovery 进入规范资产；ordinary runtime 默认不依赖 Guide；
- **Human View**：从本 README 与 `docs/guides/using-agentic-dev.md` 开始，以适合人的方式理解项目、方法、流程和目录结构。

两种视窗共享同一套规范模型。Method / Architecture / Skill / Rule 是 canonical semantic owners；Guide / README 只负责解释和导航，不建立第二套 Authority。

## 当前核心模型

### Method

Method 是一类复杂工作的规范过程模型。当前正式 Method：

- `docs/methods/ai-development.md` — 普通软件 / 产品变更从意图澄清到收敛；
- `docs/methods/consumer-adoption.md` — Consumer 首次采用 `agentic-dev`；
- `docs/methods/consumer-upgrade.md` — Existing Consumer 显式升级 upstream baseline。

### Skill

Skill 是责任明确后可独立调用的稳定、有界、可复用执行能力。当前 Skills 见 `skills/README.md`。

### Rule

Rule 是按当前工作事实条件性适用的 policy / constraint / default / invariant / completion requirement。Rule 不要求依附 Skill，并允许 Consumer-local specialization。

普通 Agent 通过 `tools/rule-discovery/` 获取少量候选 locator；人类可通过 `docs/rules/README.md` 浏览当前 Rule 结构与 inventory。

### Architecture

Architecture 定义能力类型、ownership、组合关系和运行不变量。入口见 `docs/architecture/README.md`。

### Guide

Guide 只面向人类解释和使用。入口见 `docs/guides/README.md`。

## Agent Fresh Context

本仓库 Agent 工作从 `AGENTS.md` 恢复 Repository Authority、当前 Project Roadmap 和 GitHub current state，然后选择适用 Method；Rule 仍按 task signals 动态发现，Skill 通过 Agent Skills 原生机制发现。

## Consumer

Consumer 始终拥有自己的 Repository Authority。首次 adoption / 显式 baseline upgrade 才重新进入 upstream；adoption 完成后的 ordinary runtime 只使用 Consumer-local Method / Architecture / Skills / Rules / Discovery Tool，不在线依赖 `agentic-dev` current state。

## 当前结构

```text
AGENTS.md                     # Agent Bootstrap / Repository Authority
README.md                     # Human repository entry
skills/                       # reusable Agent execution capabilities
docs/
  methods/                    # Agent-facing normative process models
  architecture/               # capability boundaries / ownership / invariants
  rules/                      # discoverable Agent-facing conditional policies
  guides/                     # Human View / usage documentation
  project/                    # current project state
  research/                   # non-normative evidence / references
evals/
tools/
  rule-discovery/
```

当前项目阶段与下一演进只以 `docs/project/project-roadmap.md` 与 GitHub 当前事实为准。