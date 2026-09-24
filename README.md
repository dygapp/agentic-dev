# agentic-dev

`agentic-dev` 为普通软件项目提供一组可直接安装的 Software Development Agent Skills，以及供人和 AI 按需阅读的方法导航。

长期产品模型只有三部分：

```text
agentic-dev Guides
→ 帮助理解怎么开始、下一步做什么

agentic-dev skills/**
→ 唯一正式 Consumer runtime product

Consumer Repository
→ 自己拥有项目事实、架构、当前工作和项目级约束
```

## 从哪里开始

- 第一次了解：[`docs/guides/getting-started.md`](docs/guides/getting-started.md)
- 新项目 Bootstrap：[`docs/guides/bootstrap-new-project.md`](docs/guides/bootstrap-new-project.md)
- 已有项目采用：[`docs/guides/adopting-agentic-dev.md`](docs/guides/adopting-agentic-dev.md)
- 不知道下一步：[`docs/guides/choosing-next-step.md`](docs/guides/choosing-next-step.md)
- Skill 清单：[`skills/README.md`](skills/README.md)

Guide 只在需要方法理解、Bootstrap 或导航时按需读取。进入明确执行责任后，由 installed Skill 承担 procedure。

## Consumer 边界

Consumer 始终拥有自己的 `AGENTS.md`、Product / Requirement / Architecture / current work、technology policy、术语、审批、授权、代码、测试与运行环境。

普通安装只安装 `skills/**`，不复制 Provider 的 Project、governance、Research 或设计目录。普通 Skill execution 不依赖在线读取 `agentic-dev` 当前 Source。

## Provider 维护

本仓自身维护采用薄治理模型：

```text
AGENTS.md
→ docs/project/project-roadmap.md
→ 当前责任直接需要的 docs/governance/**
→ skills/** / docs/guides/** / 必要设计与 Evidence
```

不使用 Method selector、五维 Rule Discovery、custom Release Builder 或批量模型自测作为 ordinary Provider work 的前置。

Provider 规则入口见 [`AGENTS.md`](AGENTS.md) 与 [`docs/governance/README.md`](docs/governance/README.md)。

## 当前结构

```text
AGENTS.md
README.md
skills/                         # canonical Consumer runtime product
docs/
  guides/                       # 人和 AI 按需方法导航
  governance/                   # Provider 自身少量直接治理
  architecture/                 # 必要 Provider 产品工程设计
  project/                      # agentic-dev 项目使命、路线与演进
  research/                     # 非规范历史 Evidence / Reference
tests/                          # 少量 deterministic / isolated smoke
```

当前项目阶段与下一责任以 [`docs/project/project-roadmap.md`](docs/project/project-roadmap.md) 和 GitHub 当前事实为准。
