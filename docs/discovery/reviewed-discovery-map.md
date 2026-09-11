# 已复核资源发现映射

**状态：** 基线 v0.1  
**性质：** 非规范性、需复核维护的派生发现映射  
**跟踪：** Issue #113

本文是 `agentic-dev` 自采用后的 **Reviewed Discovery Map**。它只保存跨资源发现所需的稳定 locator、职责 / 条件提示与 source binding；不拥有任何规范正文，也不维护第二份 `active/current` 真值。

真实语义始终由 Map 指向的 current semantic owner 持有。Map 与 source 冲突时，**source / Repository Authority 优先，Map 立即失去可信发现资格**。

## 1. Coverage scope

本 Map 只覆盖普通 `agentic-dev` 工作中需要跨资源发现的可复用能力与仓库本地条件规则：

- 当前 Skill inventory；
- 当前工程纪律；
- 当前技术画像 inventory；
- 使用方生命周期；
- 跨职责验证 / 证据规则；
- 外部操作规则；
- 仓库语言 / 术语、Git 提交、高影响 AI 复核规则；
- 与 Skill / 能力 / 资源发现本身相关的稳定架构入口。

当前项目状态、Issue / PR / Actions、Requirement / 当前工作正文**不进入 Map**，而由 `AGENTS.md → README.md → project-roadmap.md → current GitHub state` 直接恢复。

## 2. Coverage anchors 与 source binding

Map 区分三种绑定，避免把所有变化机械等同为 stale：

- **membership-reviewed**：只复核当前成员集合；inventory 普通说明文字变化不自动使 Map stale，但新增 / 删除 / 重分类成员会使对应范围 stale；
- **semantic-reviewed**：Map 从 source 提炼了职责 / 条件 / 风险提示；绑定的 source identity 变化后，对应提示先退出可信范围，必须重新判断语义影响；
- **current-locator**：只保存稳定定位 / authority role；正文正常变化不使 locator stale，但路径 / role / owner 被取代时必须更新。

当前 coverage：

| Coverage | Anchor / source | Binding | Reviewed identity / membership |
|---|---|---|---|
| Skill inventory | `skills/README.md` | membership-reviewed | `clarify-intent`, `specify`, `technical-plan`, `slice-work`, `readiness-check`, `execute-unit`, `systematic-debug`, `converge`, `github-actions-verification` |
| GitHub Actions Skill 触发语义 | `skills/github-actions-verification/SKILL.md` | semantic-reviewed | `5040e60a8a2274d8fead8375aaf66311392769ce` |
| 工程纪律 | `docs/architecture/engineering-disciplines.md` | semantic-reviewed | `d7512a776ea8473af2b4460afb3fbb11c80672c6`；3 个 current Discipline |
| 技术画像 inventory | `docs/technology-profiles/README.md` | membership-reviewed | `vue3-typescript` |
| Vue 3 + TypeScript 画像适用语义 | `docs/technology-profiles/vue3-typescript.md` | semantic-reviewed | `d6bc3e17d20153dcc0e777f1f044b65126e1a2a5` |
| 使用方生命周期 | `docs/architecture/consumer-lifecycle.md` | semantic-reviewed | `79849c46b37bb3707eb41ccad29405fef17c8c3b` |
| 验证规则族 | `docs/guides/verification-evidence-rules.md` | semantic-reviewed | `b18a1102a5f0ff637100984ab05f7144dcf192ba`；§1～§6 |
| 外部操作规则族 | `docs/guides/external-operation-guidelines.md` | semantic-reviewed | `f22de650351b89563a70653d4fdb96d4f24e6be3` |
| 中文 / 术语 | `docs/guides/terminology-guidelines.md` | semantic-reviewed | `f1aa6fad778125db37e1bd1da60589ae0f82dcf2` |
| Git 提交 | `docs/guides/git-commit-guidelines.md` | semantic-reviewed | `2f699b1f81ac52d9ff5244a7363d034e7840c9e9` |
| AI 复核 | `docs/project/ai-review-guidelines.md` | semantic-reviewed | `e832172c1d6ab5001fc75d204ece082906bb450e` |

### 2.1 Coverage drift

以下变化会让对应范围 stale：

- membership-reviewed inventory 的成员新增、删除、改名或重分类；
- semantic-reviewed source identity 改变；
- source / selector 不再存在；
- current-locator 的 path / authority role / owner 被取代；
- 当前仓库明确 supersede / disable 相关资源。

stale 范围在重新复核前不得用 no-match 证明“没有适用规则”。

semantic-reviewed source identity 改变后，不允许只刷新 identity；必须先判断变化是否影响本 Map 的派生提示。若不影响，可以更新 reviewed identity；若影响，先更新对应提示并完成必要复核。

## 3. Current Project / Authority locator

这些条目只承担稳定定位，不缓存项目状态：

| ID | Source | Role | Binding |
|---|---|---|---|
| `repository-governance` | `AGENTS.md` | bootstrap / authority | current-locator |
| `current-project-state` | `README.md` | bootstrap / current-state entry | current-locator |
| `current-roadmap` | `docs/project/project-roadmap.md` | routing / current-work entry | current-locator |

实际 Gate、Issue、PR、Actions 状态始终从 current source / GitHub 读取。

## 4. Core Skill discovery

核心职责 identity 与当前 Skill `name` 保持一致。Map 只提供 locator，不复制 Skill 的 Use When / Procedure。

| Primary responsibility | Skill source | Load rule |
|---|---|---|
| `clarify-intent` | `skills/clarify-intent/SKILL.md` | execute 时加载；routing-only 只返回 locator |
| `specify` | `skills/specify/SKILL.md` | execute 时加载；routing-only 只返回 locator |
| `technical-plan` | `skills/technical-plan/SKILL.md` | execute 时加载；routing-only 只返回 locator |
| `slice-work` | `skills/slice-work/SKILL.md` | execute 时加载；routing-only 只返回 locator |
| `readiness-check` | `skills/readiness-check/SKILL.md` | execute 时加载；routing-only 只返回 locator |
| `execute-unit` | `skills/execute-unit/SKILL.md` | execute 时加载；routing-only 只返回 locator |
| `systematic-debug` | `skills/systematic-debug/SKILL.md` | execute 时加载；是否适用由 current Method / Skill Contract 判断 |
| `converge` | `skills/converge/SKILL.md` | execute 时加载；routing-only 只返回 locator |

Skill membership 以 `skills/README.md` 的成员集合为 coverage anchor；Map 不通过自身表格宣布 Skill current，也不提炼核心 Skill 的完整 Use When。

## 5. Platform-specific Skill

| ID | Source | Derived trigger hint | Role |
|---|---|---|---|
| `github-actions-verification` | `skills/github-actions-verification/SKILL.md` | 当前工作真实涉及 GitHub Actions 的 completion evidence、trigger / gate、artifact / log、timeout / cancellation、reusable runtime、验证成本或可观察性 | supporting platform capability；只有专项过程本身成为当前目标时才可作为 primary |

该提示绑定 §2 中 `github-actions-verification/SKILL.md` 的 semantic-reviewed identity。是否加载完整 Skill 仍服从其 current `description` / Skill Contract。

## 6. Engineering Disciplines

这些条目是跨职责 supporting constraints，不夺取 primary responsibility。

| ID | Source / selector | Derived trigger hint |
|---|---|---|
| `implementation-minimality` | `docs/architecture/engineering-disciplines.md` §4 | 当前实施引入抽象、配置、扩展点、依赖或复杂度，需要判断其当前正当性 |
| `surgical-change` | `docs/architecture/engineering-disciplines.md` §5 | 当前变更需要检查最终差异范围、顺带修改或准备性重构是否属于当前责任 |
| `data-access-boundedness` | `docs/architecture/engineering-disciplines.md` §6 | 当前任务涉及集合型数据访问、分页 / 窗口、增长、有界性或生命周期边界 |

完整判断只读取对应 Discipline 正文。

## 7. Technology Profiles

| ID | Source | Derived trigger hint | Role |
|---|---|---|---|
| `vue3-typescript` | `docs/technology-profiles/vue3-typescript.md` | 当前任务真实涉及 Vue 3 / TypeScript，且技术默认、边界或验证画像会影响正确实施 | supporting technology profile |

画像 membership 以 `docs/technology-profiles/README.md` 的成员集合为 coverage anchor；当前提示同时绑定 `vue3-typescript.md` 的 semantic-reviewed identity。未来新增画像未完成 Map 复核前，不得因为本表无条目就判断“不存在适用画像”。

## 8. Consumer lifecycle / adoption

| ID | Source | Derived trigger hint |
|---|---|---|
| `consumer-lifecycle` | `docs/architecture/consumer-lifecycle.md` | 新 Consumer 初始化、首次采用、baseline upgrade、adoption verification、普通运行与显式重新进入 upstream |

面向人的说明与示例可以再读取 `docs/guides/using-agentic-dev.md`；长期规范语义只由 lifecycle architecture 持有。

## 9. Verification / Evidence rule units

每个条目只对应 `docs/guides/verification-evidence-rules.md` 中一个稳定资源单元；触发提示是派生发现语义，不替代规则正文。

| ID | Source / selector | Derived trigger hint |
|---|---|---|
| `verification-currentness` | `docs/guides/verification-evidence-rules.md` §1 | 测试 / Workflow / assertion 与当前 Requirement / Specification / Architecture 疑似不一致，或验证契约可能陈旧 |
| `visual-evidence` | `docs/guides/verification-evidence-rules.md` §2 | 视觉复刻、设计稿还原、品牌 / UI fidelity 属于当前验收义务 |
| `human-review-baseline-isolation` | `docs/guides/verification-evidence-rules.md` §3 | 自动验证修改共享状态，且同一环境随后用于 Human Review |
| `database-migration-completion` | `docs/guides/verification-evidence-rules.md` §4 | 当前变化包含数据库 schema / migration lifecycle，需要完整初始化完成证据 |
| `evidence-reuse-across-commits` | `docs/guides/verification-evidence-rules.md` §5 | 拟复用祖先提交证据支持当前提交的完成声明 |
| `evidence-type-matches-claim` | `docs/guides/verification-evidence-rules.md` §6 | 当前准备做 completion / pass / ready-to-integrate 声明 |

## 10. External-operation rule units

| ID | Source / selector | Derived trigger hint |
|---|---|---|
| `external-state-mutation` | `docs/guides/external-operation-guidelines.md` §1～§5 | 当前将修改 GitHub / Issue / PR / 仓库 / 外部 API 等外部状态，或存在明确外部副作用 / 授权边界；要求读 → 最小必要写 → 重读验证 |
| `external-binary-media` | `docs/guides/external-operation-guidelines.md` §4.1 | 外部二进制 / 图片 / 媒体资源将被版本化或运行环境消费，需要核对真实内容类型 |
| `async-external-operation` | `docs/guides/external-operation-guidelines.md` §5.1 | Workflow / deployment / remote task 等异步外部操作需要观察、诊断与闭环 |
| `shared-external-resource` | `docs/guides/external-operation-guidelines.md` §5.2 | 多运行争用固定域名、代理、端口、环境、数据库、账号等共享资源 |
| `artifact-promotion` | `docs/guides/external-operation-guidelines.md` §5.3 | 临时 Artifact / snapshot / output 将被接受为后续稳定输入 |
| `dependent-pr-topology` | `docs/guides/external-operation-guidelines.md` §5.4 | 依赖 PR / stacked PR / squash integration topology 会影响当前安全集成路径 |

纯只读的仓库状态恢复本身不要求为了形式完整性加载完整外部操作 Guide；只有写入、副作用、授权或其他具体风险命中时才加载对应正文。

## 11. Repository-local governance

| ID | Source | Derived trigger hint |
|---|---|---|
| `terminology-guidelines` | `docs/guides/terminology-guidelines.md` | 修改 `agentic-dev` 面向人的仓库正文、正式概念身份或中英文表达 |
| `git-commit-guidelines` | `docs/guides/git-commit-guidelines.md` | 准备创建 Git commit 或修改提交组织方式 |
| `ai-review-guidelines` | `docs/project/ai-review-guidelines.md` | 变更 Method / Principle / Architecture / Contract / 核心 Skill / Repository Authority / `docs/project/*` 或其他高影响 Agent 行为 |

这些规则只适用于 `agentic-dev` 自身；不得通过本 Map 自动投射给 Consumer。

## 12. Stable architecture locators

以下 entry 只承担稳定 locator，不复制架构正文：

| ID | Source | Authority role |
|---|---|---|
| `engineering-capability-architecture` | `docs/architecture/engineering-capability-architecture.md` | 可复用工程能力分类、生命周期与层次边界 |
| `skill-architecture` | `docs/architecture/skill-architecture.md` | Skill 身份、准入与支持资源边界 |
| `skill-contracts` | `docs/architecture/skill-contracts.md` | Skill 输入 / 输出 / 退出 / 返回契约 |
| `technology-profile-contract` | `docs/architecture/technology-profile-contract.md` | 技术画像长期契约 |
| `agent-resource-model` | `docs/architecture/agent-resource-model.md` | 资源身份、固有结构与派生发现边界 |
| `resource-discovery-architecture` | `docs/architecture/resource-discovery-architecture.md` | Local Discovery Entry / Map / Runtime View / discovery semantics |

这些 current-locator 的 applicability 由当前任务事实与更高 Repository Authority 判断；Map 不保存额外 Use When 摘要。

## 13. 使用边界

本 Map 只提供 **candidate discovery**。主职责解析、最小辅助集合、routing-only / execute、Stage Return、fail-closed 与 ordinary-runtime local-only 的完整语义统一由：

`docs/architecture/resource-discovery-architecture.md`

单点拥有。

使用 Map 时只额外保持：

- candidate 命中不等于最终适用；
- stale coverage 不允许用 no-match 证明“无规则”；
- Map 不创建 Authority priority；
- Map 不持久化一次任务的 discovery decision。

## 14. Map maintenance

### 14.1 更新触发

出现以下变化时重新检查受影响条目：

- coverage membership 改变；
- semantic-reviewed source identity 改变；
- source path / selector 改变；
- 新资源被证明需要独立跨资源发现；
- 真实 supersede / disable / override 关系改变。

### 14.2 更新方式

- 先读取真实 owner 当前内容；
- 判断变化是否影响派生职责 / 条件 / 风险提示；
- 只更新受影响条目；
- 重新记录 reviewed identity / membership；
- 对高影响发现语义变化按仓库 AI 复核规则处理。

不得仅刷新 source identity 就声称 semantic-reviewed 映射仍然有效。

### 14.3 删除

删除本 Map 不删除规范事实，但会失去已复核跨资源语义映射。安全恢复只能：

1. 从稳定 Local Discovery Entry + 真实 owner 直接工作；或
2. 重新执行必要的语义复核并建立新的 Map。

当前没有 Runtime View，因此不存在“从 generator 自动重建本 Map”的路径。