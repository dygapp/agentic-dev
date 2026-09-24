---
id: project:roadmap
type: project
status: active
---

# 项目路线图

## 当前基线

`agentic-dev` 当前稳定 baseline 是 `agentic-dev-v0.1.0`（integration commit `ae8ee8032e34c046d619c719dad408edda2d2d8a`）对应的极简 Provider 产品模型：

- `skills/**` 是唯一正式 Consumer-facing runtime product；
- `docs/guides/**` 只为人和 AI 提供按需 Bootstrap、方法理解与下一步导航；
- Consumer 自己拥有 Product / Requirement / Architecture / current work、技术政策、授权和本地约束；
- Provider ordinary bootstrap 只恢复 Repository Authority、Roadmap 与当前责任直接需要的少量治理 / 产品资产，不运行 Method selector、Project Capability Profile、Rule Discovery 或中央 Capability Runtime；
- Provider 自身只保留少量直接 governance，普通修改使用与声明匹配的最小 deterministic validation 与必要 Review，不恢复批量模型 grader、custom Release Builder 或多级 Gate；
- 历史复杂机制解决过的 bounded context、Consumer ownership、Evidence integrity、Fresh Context、human escalation 等长期语义已经进入 Skills、Guides、Provider governance 或 Consumer-local Authority。

当前允许的完成声明是：**Provider 极简切换完成，`agentic-dev-v0.1.0` 可供采用**。这不表示任何真实 Consumer 已完成采用验证，也不授予后续版本的 merge、release 或 deploy 权限。

稳定演进里程碑与历史原因由 `docs/project/project-evolution.md` 持有；精确 branch / Issue / PR / Actions / commit 状态始终从 GitHub 与当前 checkout 重新读取。

## 当前演进

**AI 驱动软件开发方法论产品边界重构已完成 S1～S3 Provider 收敛，并已集成 / 发布为 `agentic-dev-v0.1.0`。**

本轮目标模型先后完成 Specification、Repository-wide disposition、P1～P4 能力验证、S1 Authority Freeze、S2 Subtractive Cutover 与 S3 Final Fresh Independent Review。`methodology-product-boundary-specification.md` 与 `methodology-product-boundary-implementation-plan.md` 已完成本轮临时 Authority 职责，现作为本轮历史规范 / 实施计划保留，不再参与 ordinary Provider runtime。

S3 Final Fresh Independent Review 在 exact candidate `c84d5ec2a6616a79629879bd4ef24f6584ad45c6` 上重新核验当前 Authority、15 个 canonical Skill、26 个 legacy obligations、RC-only 语义、Consumer-owned file preservation、retired runtime / dead locator、最小验证基础设施与 P2→S3 Skill subject 差异，结果：

- `Blocking=0`
- `Medium=0`
- deterministic repository contracts：9 / 9 PASS
- `skills/*/SKILL.md` 相对 P2 exact subject `4918846e411b9797fb705fa0b6695891f190a51e` 无内容漂移
- 真实 Consumer adoption：未验证，且不属于本轮完成门槛
- 当前 exact candidate 的远端 PR / Actions：未作为本轮 PASS Evidence

当前进入 **v0.1.0 后 Consumer 反馈演进阶段**。当前演进计划由 [`post-v0.1.0-consumer-feedback-evolution-plan.md`](post-v0.1.0-consumer-feedback-evolution-plan.md) 持有：后续工作划分为独立演进事项，每次只推进一项，按证据重新分析 → 必要的外部研究 → 方案收敛 → 实施 → 聚焦验证与必要复核 → 收口逐项完成。

上一轮 Issue #172 Gate A～G、旧 Release Candidate 与相关 Runtime Evidence 继续只作为历史 Evidence；原 Gate H、custom Release Builder 与旧发布路线不恢复。前置状态收口已经完成：Issue #172 已明确 superseded / completed 并关闭，不再作为当前能力设计入口。

## 已完成阶段与当前收敛

Gate P1 — 标准 Skills Distribution 可行性验证已在 exact SHA `f5b1d90e8d3e642045f5ae57b6afb207f6cdbae3` 完成 Fresh Independent Review（`Blocking=0`、`Medium=0`）。Evidence：

- `../research/standard-skills-distribution-feasibility.md`

P1 已确认 GitHub exact tag + 标准 Skills CLI + `skills-lock.json` + Codex native discovery 可以承担普通安装路径；arbitrary commit SHA URL 不是标准 CLI 支持的安装 UX，无版本 generic `update` 也不作为已验证升级协议。

Gate P2 — Canonical Skills 重构已在 exact Skill subject `4918846e411b9797fb705fa0b6695891f190a51e` 完成 Fresh Independent Review（`Blocking=0`、`Medium=0`）。Evidence：

- `../research/canonical-skill-semantic-migration.md`

P2 已完成 15 个 canonical Skill 的语义迁移，移除旧 Release composition metadata 与 Provider docs runtime dependency；28/28 旧 release-input owner 已有明确投影 / disposition；标准安装、Codex native discovery 与 15/15 代表性 behavior semantic grading 均通过。

Gate P3 — Guides / Bootstrap / Navigation 已在 exact candidate `c104b58de4cb5ea78db8e408c8fe37480256a6ef` 完成 Fresh Independent Review（`Blocking=0`、`Medium=0`）。Evidence：

- `../research/methodology-guide-bootstrap-navigation-evidence.md`

P3 已完成 Guide 的 Human + AI 按需导航重构、greenfield Bootstrap、Existing Project 最小 adoption、exact-version Guide locator 和三类 next-step AI 行为验证。Greenfield 首次长任务存在一个非阻塞 Runtime limitation：目标工件已真实建立，但原 Agent process 未正常返回终态；独立只读收口与 Codex native discovery 已验证实际完成边界。该 limitation 不通过增加新的 Bootstrap Framework 解决。

Gate P4 — Consumer-local Constraints 最小方案已在 exact candidate `f7fc76396e50f8524873ba38121564e8031de125` 完成 Fresh Independent Review（`Blocking=0`、`Medium=0`）。Evidence：

- `../research/consumer-local-constraints-minimal-evidence.md`

P4 已冻结第一版最小约定：root `AGENTS.md` 承担极少量 repository-wide stable policy；nested `AGENTS.md` / 宿主原生 scoped instructions 承担 path / module policy；Consumer-local policy docs + 薄 locator 承担 activity / semantic policy；verified no-match 正常继续，broken / uncertain locator fail closed。Codex local 与 ChatGPT + WebCodex 均有验证路径，Skills 安装不覆盖 Consumer policy。

Disposable fixture 没有暴露前三种简单机制的缺口，因此按冻结前置条件没有触发真实软件 Consumer applicability challenge，也没有进入 metadata/filter 设计。旧 `rule-activation-guide.md` 与 `consumer-local-rule-activation.md` 已退出。

S1 Authority Freeze 已在 exact candidate `9a86785f613b50e48b868cdcec272a739011bb8e` 完成 Fresh Independent Semantic Review：`Blocking=0`、`Medium=0`。两项 Low 只作为 backlog；远端 PR / Actions 与真实 Consumer adoption 保持未验证，不阻塞本轮 Provider 收敛。

S2 已完成两步减法切换：

- `60bfa2a17e353bd888dbfafa9e1802fc14ae758e` — Provider governance 直接化，根 Bootstrap 不再执行 Method selector / Rule Discovery；
- `0c7f7f8483076eb5ae1410e09ff6a37705e0ce16` — 删除旧 Method / Rule / Capability / Release / Eval 基础设施，建立最小 deterministic tests 与单一 CI。

旧 Provider `rule-discovery lint`、Project Capability Profile、custom Release Builder / installer、authenticated batch model acceptance 与旧 workflows 已退出 Current tree，不保留兼容运行入口。

S3 — Minimal Validation / Final Fresh Independent Review 已在 exact candidate `c84d5ec2a6616a79629879bd4ef24f6584ad45c6` 完成：`Blocking=0`、`Medium=0`。本轮基础设施重构至此结束。

普通 Provider 修改不再要求 Method / Rule Discovery、批量模型自测或多级 Gate。WebCodex Runner 继续禁止直接或间接调用 `codex-cli`；只有未来 claim 明确依赖 Codex-specific Runtime Under Test 时，才在非 WebCodex 独立子任务中临时授权。

完成声明严格限定为：**Provider 极简切换完成，可供采用**。

## 后续演进事项

当前顺序暂定为：

1. **Skill 与项目权威的适配边界**：方案、实现与 focused validation 已完成，当前下一责任是最终 Fresh / Independent Review；
2. **小规模变更的执行粒度**；
3. **多仓库项目的工作区与权威边界**；
4. **本地验证环境的资源生命周期**。

该顺序不是永久 Roadmap。每个演进事项收口后必须基于届时最新 Repository / Consumer Evidence 重新判断后续事项，允许调整、拆分或删除，不为了“一次规划完整”同时展开多个事项的详细分析和设计。

## 已知约束

- P1～P4 的历史 Evidence 继续支持未变化的 exact Skill subject；跨 subject 复用必须证明差异不影响 claim；
- `skills/**` 是唯一正式 Consumer runtime product，Guides 只按需导航；
- Consumer-local Product / Requirement / Architecture / technology policy / authorization / current state 不得被通用 Skill 吸收；
- WebCodex 不调用 `codex-cli`；
- post-v0.1.0 演进一次只推进一个演进事项；Issue 中已有判断和候选方案只作为 Evidence，不直接成为 Current design；
- S3 review subject `c84d5ec2a6616a79629879bd4ef24f6584ad45c6` 的完成结论不依赖远端 PR / Actions；后续 integration / release 状态必须从 GitHub 当前事实重新核验；
- 真实 Consumer adoption 明确保留为未验证状态，不得从 Provider S3 PASS 外推。

## 状态归属

- Repository live state：GitHub 与当前 checkout 的 Git facts；
- 项目使命 / 核心要求：`project-charter.md`；
- Provider Bootstrap：根 `AGENTS.md`；
- Provider 直接治理：`../governance/**`；
- Consumer runtime product：`../../skills/**`；
- 人与 AI 的按需方法导航：`../guides/**`；
- 当前产品边界：`project-charter.md`、根 `AGENTS.md`、`../architecture/skill-architecture.md` 与本 Roadmap；
- 本轮已完成的产品边界规范 / 实施计划：`methodology-product-boundary-specification.md`、`methodology-product-boundary-implementation-plan.md`，仅作为历史收敛依据；
- Repository-wide disposition Evidence：`../research/methodology-product-boundary-asset-disposition.md`；
- 当前 evolution / next responsibility：本 Roadmap；
- post-v0.1.0 Consumer 反馈演进事项与逐项闭环协议：`post-v0.1.0-consumer-feedback-evolution-plan.md`；
- 演进事项 1 当前工作入口与详细方案 / Review Evidence：GitHub Issue #183；
- 稳定历史里程碑：`project-evolution.md`；
- 历史研究与旧模型 Evidence：`../research/**`；
- bounded change 的精确 commit / Review / Actions Evidence：Git / GitHub 对应对象。

Roadmap 不复制完整规范、Skill procedure、历史实施日志或完整 Review Evidence。
