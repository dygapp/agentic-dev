# 已复核资源发现映射

**状态：** V3-07 candidate  
**性质：** 非规范性、需复核维护的派生发现映射  
**跟踪：** Issue #113

本文是 `agentic-dev` 自采用的候选 **Reviewed Discovery Map**。它只保存跨资源发现所需的稳定 locator、职责 / 条件提示与 source binding；不拥有任何规范正文，也不维护第二份 `active/current` 真值。

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

## 2. Coverage anchors

只有以下 coverage anchors 与当前 source identity 一致时，Map 才可以声称对应范围已复核：

| Coverage | Anchor | Reviewed identity | 期望成员 / 语义单元 |
|---|---|---|---|
| Skill inventory | `skills/README.md` | `5ff2c65ec48e9899b6a1d4a4785aa0425de7c2c4` | 8 个核心 Skill + `github-actions-verification` |
| 工程纪律 | `docs/architecture/engineering-disciplines.md` | `d7512a776ea8473af2b4460afb3fbb11c80672c6` | 3 个 current Discipline |
| 技术画像 inventory | `docs/technology-profiles/README.md` | `ef6b4311364f876437186f0d702a48ad4d2b4e10` | `vue3-typescript.md` |
| 使用方生命周期 | `docs/architecture/consumer-lifecycle.md` | `79849c46b37bb3707eb41ccad29405fef17c8c3b` | 初始化 / 采用 / 升级 / 普通运行 / 上游重新进入 |
| 验证规则族 | `docs/guides/verification-evidence-rules.md` | `b18a1102a5f0ff637100984ab05f7144dcf192ba` | §1～§6 条件性规则族 |
| 外部操作规则族 | `docs/guides/external-operation-guidelines.md` | `f22de650351b89563a70653d4fdb96d4f24e6be3` | 外部写、媒体输入、异步、共享资源、持久输入、依赖 PR 等规则族 |
| 中文 / 术语 | `docs/guides/terminology-guidelines.md` | `f1aa6fad778125db37e1bd1da60589ae0f82dcf2` | `agentic-dev` 自身表达规则 |
| Git 提交 | `docs/guides/git-commit-guidelines.md` | `2f699b1f81ac52d9ff5244a7363d034e7840c9e9` | 当前提交规范 |
| AI 复核 | `docs/project/ai-review-guidelines.md` | `e832172c1d6ab5001fc75d204ece082906bb450e` | 当前高影响 AI 复核规则 |

### 2.1 Coverage drift

出现以下任一情况，对应 coverage 范围立即视为 **stale**：

- anchor identity 改变；
- inventory 新增 / 删除 / 重分类成员；
- selector / source path 不再存在；
- semantic owner 的条件语义发生变化；
- 当前仓库明确 supersede / disable 相关资源。

stale 范围在重新复核前不得用 no-match 证明“没有适用规则”。

纯 locator entry 如果不提炼 source 语义，可以只检查 path / authority role 是否仍 current；本文不会为了所有 locator 强制绑定正文 hash。

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

Skill membership 以 `skills/README.md` 为 coverage anchor；Map 不通过自身表格宣布 Skill current。

## 5. Platform-specific Skill

| ID | Source | Derived trigger hint | Role |
|---|---|---|---|
| `github-actions-verification` | `skills/github-actions-verification/SKILL.md` | 当前工作真实涉及 GitHub Actions 的 trigger / gate / artifact / log / timeout / cancellation / reusable runtime / 验证成本或可观察性 | supporting platform capability；只有专项过程成为当前目标时才可作为 primary |

是否加载完整 Skill 仍服从其当前 `description` / Skill Contract；本提示只用于 candidate discovery。

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

画像 membership 以 `docs/technology-profiles/README.md` 为 coverage anchor。未来新增画像未完成 Map 复核前，不得因为本表无条目就判断“不存在适用画像”。

## 8. Consumer lifecycle / adoption

| ID | Source | Derived trigger hint |
|---|---|---|
| `consumer-lifecycle` | `docs/architecture/consumer-lifecycle.md` | 新 Consumer 初始化、首次采用、baseline upgrade、adoption verification、普通运行与显式重新进入 upstream |

面向人的说明与示例可以再读取 `docs/guides/using-agentic-dev.md`；长期规范语义只由 lifecycle architecture 持有。

## 9. Verification / Evidence rule units

每个条目只对应 `verification-evidence-rules.md` 中一个稳定 section；触发提示是派生发现语义，不替代规则正文。

| ID | Selector | Derived trigger hint |
|---|---|---|
| `verification-currentness` | §1 | 测试 / Workflow / assertion 与当前 Requirement / Specification / Architecture 疑似不一致，或验证契约可能陈旧 |
| `visual-evidence` | §2 | 视觉复刻、设计稿还原、品牌 / UI fidelity 属于当前验收义务 |
| `human-review-baseline-isolation` | §3 | 自动验证修改共享状态，且同一环境随后用于 Human Review |
| `database-migration-completion` | §4 | 当前变化包含数据库 schema / migration lifecycle，需要完整初始化完成证据 |
| `evidence-reuse-across-commits` | §5 | 拟复用祖先提交证据支持当前提交的完成声明 |
| `evidence-type-matches-claim` | §6 | 当前准备做 completion / pass / ready-to-integrate 声明 |

Source：`docs/guides/verification-evidence-rules.md`。

## 10. External-operation rule units

| ID | Source / selector | Derived trigger hint |
|---|---|---|
| `external-state-write` | `docs/guides/external-operation-guidelines.md` §1～§5 | GitHub / Issue / PR / 仓库 / 外部 API 等状态读取或写入；要求读 → 最小写 → 重读验证 |
| `external-binary-media` | §4.1 | 外部二进制 / 图片 / 媒体资源将被版本化或运行环境消费，需要核对真实内容类型 |
| `async-external-operation` | §5.1 | Workflow / deployment / remote task 等异步外部操作需要观察、诊断与闭环 |
| `shared-external-resource` | §5.2 | 多运行争用固定域名、代理、端口、环境、数据库、账号等共享资源 |
| `artifact-promotion` | §5.3 | 临时 Artifact / snapshot / output 将被接受为后续稳定输入 |
| `dependent-pr-topology` | §5.4 | 依赖 PR / stacked PR / squash integration topology 会影响当前安全集成路径 |

这些条目是仓库本地操作治理 / supporting constraints；是否拥有当前 primary responsibility 由当前任务和 Repository Authority 决定。

## 11. Repository-local governance

| ID | Source | Derived trigger hint |
|---|---|---|
| `terminology-guidelines` | `docs/guides/terminology-guidelines.md` | 修改 `agentic-dev` 面向人的仓库正文、正式概念身份或中英文表达 |
| `git-commit-guidelines` | `docs/guides/git-commit-guidelines.md` | 准备创建 Git commit 或修改提交组织方式 |
| `ai-review-guidelines` | `docs/project/ai-review-guidelines.md` | 变更 Method / Principle / Architecture / Contract / 核心 Skill / Repository Authority / `docs/project/*` 或其他高影响 Agent 行为 |

这些规则只适用于 `agentic-dev` 自身；不得通过本 Map 自动投射给 Consumer。

## 12. Stable architecture locators

以下 entry 只帮助处理相关架构变更，不复制架构正文：

| ID | Source | Use when |
|---|---|---|
| `engineering-capability-architecture` | `docs/architecture/engineering-capability-architecture.md` | 新可复用工程能力分类、生命周期或层次边界 |
| `skill-architecture` | `docs/architecture/skill-architecture.md` | Skill 身份、准入、支持资源边界变化 |
| `skill-contracts` | `docs/architecture/skill-contracts.md` | Skill 输入 / 输出 / 退出 / 返回 / 契约变化 |
| `technology-profile-contract` | `docs/architecture/technology-profile-contract.md` | 新建 / 修改技术画像契约或画像结构 |
| `agent-resource-model` | `docs/architecture/agent-resource-model.md` | 资源身份、固有结构、派生发现边界变化 |
| `resource-discovery-architecture` | `docs/architecture/resource-discovery-architecture.md` | Local Discovery Entry / Reviewed Discovery Map / Runtime View / discovery semantics 变化 |

这些 locator 的 applicability 仍由当前任务事实与更高 Repository Authority 判断。

## 13. Discovery decision rules

使用本 Map 时：

1. 先从 `AGENTS.md`、README / Roadmap 与 current GitHub state 确认项目事实；
2. 只在需要跨资源发现时读取本 Map；
3. candidate 命中不等于最终适用；
4. 先形成一个 primary responsibility；
5. 只保留会改变当前正确执行 / 完成声明的最小 supporting set；
6. routing-only 不加载完整 Skill；
7. execute 才按需加载 primary Skill；
8. Stage Return 后旧 discovery decision 失效，重新读取受影响权威并重新发现；
9. 未知 condition / risk 不猜测；
10. 不使用固定 Top-K 或全局数值 priority；
11. no-match 但治理 / 风险事实仍存在时 fail-closed，不解释为无规则；
12. ordinary runtime 不访问 upstream。

具体 Method / Skill / Stage Return / Readiness / verification / authorization 语义继续由原 owner 单点拥有。

## 14. Map maintenance

### 14.1 更新触发

出现以下变化时重新检查受影响条目：

- coverage anchor identity 改变；
- Skill / Profile / Discipline membership 变化；
- source path / selector 改变；
- 条件性规则语义实质变化；
- 新资源被证明需要独立跨资源发现；
- 真实 supersede / disable / override 关系改变。

### 14.2 更新方式

- 先读取真实 owner 当前内容；
- 判断变化是否影响派生职责 / 条件 / 风险提示；
- 只更新受影响条目；
- 重新记录 reviewed identity；
- 对高影响发现语义变化按仓库 AI 复核规则处理。

不得仅刷新 hash 就声称 semantic-reviewed 映射仍然有效。

### 14.3 删除

删除本 Map 不删除规范事实，但会失去已复核跨资源语义映射。安全恢复只能：

1. 从稳定 Local Discovery Entry + 真实 owner 直接工作；或
2. 重新执行必要的语义复核并建立新的 Map。

当前没有 Runtime View，因此不存在“从 generator 自动重建本 Map”的路径。