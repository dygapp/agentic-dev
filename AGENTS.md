# AGENTS.md

## 仓库职责

`agentic-dev` 是 Software Development Agent Skills 的 Provider Repository。`skills/**` 是唯一正式的 Consumer-facing runtime product；`docs/guides/**` 为人和 AI 提供按需方法导航；Consumer 始终拥有自己的项目事实、架构、当前工作和本地约束。

GitHub Repository 是本仓库唯一长期项目事实来源。会话历史、个人记忆、其他仓库状态和未固化推理不构成本仓库事实。

## Fresh Context

新的本仓库上下文按以下顺序恢复：

1. 读取本文件；
2. 读取 `docs/project/project-roadmap.md`；
3. 重新核验当前 branch / HEAD / working tree，以及当前任务真正需要的 GitHub Issue / PR / Actions 状态；
4. 当前任务涉及项目使命或长期边界时，再读取 `docs/project/project-charter.md`；
5. 按当前责任直接读取必要的 Provider governance、Guide、Skill、设计文档和 Evidence，不执行 Method selector、Rule Discovery 或其他中央路由；
6. 只加载完成当前责任需要的最小上下文。

`README.md`、Guide inventory、Research、Project Evolution 和完整 Skill 清单都不是 ordinary bootstrap 的固定输入。

## Provider governance

Provider 自身只保留少量直接治理正文，不建立 Rule Engine 或动态发现层：

- Git / commit / history：`docs/governance/git-conventions.md`
- 中文表达与术语：`docs/governance/language-and-writing.md`
- 文档 Authority 与长期 owner 生命周期：`docs/governance/documentation-authority.md`
- 完成证据与高影响独立复核：`docs/governance/review-and-verification.md`
- Repository / GitHub / workflow / deployment 等外部写操作：`docs/governance/external-operations.md`

适用责任出现时直接读取对应正文；不得为了“发现规范”恢复 metadata、task signals、中央索引或扫描所有治理文档。

## Skills 与 Guides

`skills/**` 是 canonical Consumer runtime product。每个 Skill 必须能够在 Consumer Repository 中依赖自身 `SKILL.md`、Skill-local resources 与 Consumer-local Authority 完成通用责任，不在线回读 Provider `docs/**` 补执行语义。

`docs/guides/**` 同时服务人和 AI 的 Bootstrap、方法理解与导航，但不成为 ordinary task 的固定输入，也不复制 Skill procedure 或 Consumer project facts。

Skill 的 Provider 工程规范见 `docs/architecture/skill-architecture.md`。

## Consumer 边界

普通软件 Consumer：

- 自己拥有 `AGENTS.md`、Product / Requirement / Architecture / current work、代码、验证、授权和项目级约束；
- 通过标准 Agent Skills 兼容方式安装明确版本的 `skills/**`；
- 不要求复制 Provider 的治理、设计、Research 或项目状态；
- 普通 Skill execution 默认 `upstream access = 0`；
- Consumer-local policy 优先于通用 Skill 默认值。

## WebCodex 与 Codex CLI

ChatGPT + WebCodex 是本仓默认工作模式时，WebCodex Runner **不得直接或间接启动 `codex-cli`**，包括 `codex`、`codex exec`、`codex app-server` 以及 wrapper 间接调用。

Fresh Context、独立复核和普通语义判断不构成调用 `codex-cli` 的理由。只有声明本身必须观察 Codex-specific Runtime Under Test 时，才拆成独立子任务，由人工在单独会话显式临时授权，并在非 WebCodex 执行上下文运行。

## 复核与集成

会持续塑造 Agent 行为的高影响变更，例如 Repository Authority、canonical Skill contract、Provider governance 或产品边界变化，在进入最终集成决策前必须执行 Fresh / Independent Review。

Review PASS 不等于 merge、release 或 deploy 授权。merge、发布、部署、破坏性历史改写和其他不可逆外部操作始终服从当前 Repository / Human Authority。
