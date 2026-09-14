---
id: project:roadmap
type: project
status: active
---

# Project Roadmap

## Current Foundation

当前正式 Foundation 仍为 **V4 — 分布式规则发现与仓库基础重构**。

`master@3098f17b5661fbd4edbbaf1080ed4b4f5759e0d8` 是当前正式 V4 baseline。V4 已完成全部 Gate，不因后续 Capability Model 演进重新打开 Closure。

V4 稳定保留的核心运行约束包括：

```text
current task / repository facts
→ bounded task signals
→ Rule Discovery Tool
→ scan Rule YAML Front Matter
→ deterministic candidate filtering
→ {id, path} locators
→ LLM reads only candidate bodies
→ semantic applicability confirmation
```

- Rule metadata 与规范正文同文件维护；
- 不维护 Reviewed Discovery Map / Activation Manifest / Runtime Catalog / rule-index；
- Rule Discovery `candidates[]` 是 ordinary runtime 获得 Rule locator 的唯一入口；
- 未命中 Rule locator / metadata / body 不进入 ordinary LLM context；
- task signals 使用 known array / known-empty `[]` / unknown `null` 三态，每个非空维度最多 6 个 canonical token；
- Consumer ordinary runtime 默认只依赖 Consumer-local current state，不在线依赖 upstream current state。

## Current Evolution — Capability Model v2

当前增量演进入口为 **Issue #124 — Capability Model v2：重定义 Method / Skill / Rule / Guide 与双视窗架构**。

该演进来自 V4 完成后的真实可用性复核：Rule Discovery runtime 已稳定，但 Human View、Agent process entry、Method 扩展性以及 Skill / Rule 语义边界仍需长期收敛。

本轮不推翻 V4 Rule Discovery，而是在其上建立更完整的能力模型：

### Single Semantic Ownership, Multiple Views

- Method / Architecture / Skill / Rule 持有 canonical normative semantics；
- Guide / README 提供 Human View，不成为第二套 Authority；
- ordinary Agent runtime 默认不依赖 Guide；
- Agent 必须通过 Repository Bootstrap / Method Selection / Skill discovery / Rule Discovery 获得自己的规范入口。

### Capability boundaries

- **Method**：一类复杂工作的规范过程模型，可存在多个实例；
- **Architecture**：长期结构、ownership、组合关系和运行不变量；
- **Skill**：责任明确后的有界、稳定、可复用执行能力；
- **Rule**：按事实条件适用的 policy / constraint / default / invariant / completion requirement，可横切 Method、Skill 与 direct work；
- **Guide**：Human-facing explanation / usage / navigation；
- **Research**：非规范 Evidence / Reference。

Skill 与 Rule 是正交关系，不是固定 `Method → Skill → Rule` 流水线。Rule 是 Consumer-local policy specialization 的主要承载面之一。

## Current Candidate Structure

Issue #124 candidate 将当前长期结构收敛为：

```text
AGENTS.md                     # Agent Bootstrap / Repository Authority
README.md                     # Human repository entry
skills/                       # reusable Agent execution capabilities
docs/
  methods/                    # normative process models
  architecture/               # capability boundaries / ownership / invariants
  rules/                      # discoverable conditional policies
  guides/                     # Human View
  project/                    # current project state
  research/                   # non-normative evidence / references
evals/
tools/
  rule-discovery/
```

当前 candidate Methods：

- `method:ai-development`；
- `method:consumer-adoption`；
- `method:consumer-upgrade`。

大型项目前期 Requirements Analysis 仍只是未来 Method candidate；只有在历史实践与新 Evidence 足以提炼稳定适用边界、阶段、产物、Gate 和完成语义时才正式建立。

## Issue #124 Implementation Gates

当前实施顺序：

1. **Capability Architecture** — 定义能力类型、双视窗、single semantic ownership、Skill / Rule 正交关系；
2. **Agent Process Entry** — 建立 Method Selection，使 Agent 不依赖 Guide 进入规范流程；
3. **Method Restructuring** — Consumer Adoption / Upgrade 从混合 lifecycle 文档提升为正式 Method，Consumer Architecture 只保留长期不变量；
4. **Human View** — 扩展 Guides，并为 Architecture / Methods / Rules 提供 README 导航；
5. **Rule Infrastructure** — reserved `README.md` 退出 Rule Discovery、继续参加 repository lint；
6. **Asset / Granularity Audit** — 复核现有 Method / Skill / Rule / Guide / Architecture 归属及 Rule 粒度；
7. **Verification** — deterministic tests、repository lint、Rule smoke discovery、Method entry / Fresh Context 行为复核与 Human navigation review。

已完成的 Gate 必须由 branch / PR current Evidence 支持；在最终集成前，本节描述的是当前 candidate，不代表 `master` 已接受这些变化。

## V4 Closure Evidence

V4-00 ～ V4-09 全部 PASS。PR #123 已 squash merge，V4 initial integration commit 为 `0e7e45fa2a7aa9048d0f357b6b3be3befce921a4`；最终 Roadmap closure commit 为 `3098f17b5661fbd4edbbaf1080ed4b4f5759e0d8`。

最终 baseline Rule Discovery Run `34769662589` SUCCESS：38 / 38 deterministic tests PASS、lint 45 Rules / 11 Skills PASS，普通与 Vue unknown-risk smoke discovery 均 PASS。

V4-08 的 natural Rule Evolution observation 仍是 post-adoption future observation，不因本轮能力模型演进被虚构为已验证。

## Next Evolution

先完成 Issue #124 的能力模型与信息架构收敛，并通过独立验证证明 Agent View 与 Human View 都可恢复、Rule Discovery 没有回退为中心索引。其后继续从真实 `agentic-dev` / Consumer Evidence 演进；不因目录整齐、理论完备或历史做法自动新增 Method、Skill 或 Rule。