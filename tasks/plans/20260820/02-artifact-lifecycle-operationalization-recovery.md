# Artifact 生命周期跨层对齐恢复计划

**状态：** COMPLETE（Draft PR #29，等待 Human Review）

**当前分支：** `codex/artifact-lifecycle-operationalization`

**恢复基线：** `master@8882c98`（PR #28 已合并）

**前序计划：** `tasks/plans/20260820/01-artifact-lifecycle-closure-method-revision.md`

## 1. Goal

在 PR #28 已完成 Method / Skill Architecture / AI Review Governance 修订的基础上，补齐 Artifact Lifecycle Closure 在 Skill Contract、核心 Skill 实现、Consumer Operating Guide 与针对性 Eval 中的跨层映射，并留下可供 Fresh Context 直接恢复的当前状态与证据。

本计划只 operationalize 已经进入上游权威的语义，不重新设计方法，不新增核心 Skill、方法阶段、固定 Artifact 目录或完整生命周期 Super-skill。

## 2. Authority / Inputs

按仓库权威顺序使用：

1. `AGENTS.md`
2. `docs/method/ai-development-method.md`
3. `docs/method/principles.md`
4. `docs/architecture/skill-architecture.md`
5. `docs/architecture/skill-contracts.md`
6. `docs/decisions/method-decisions.md`
7. `docs/project/ai-review-guidelines.md`
8. `docs/guides/using-agentic-dev.md`
9. 前序计划与 PR #28 当前证据

GitHub `master@8882c98` 是本轮唯一集成基线。Conversation History 只用于定位恢复入口，不作为项目事实。

## 3. Recovery State

已由当前 Repository / GitHub 状态确认：

- PR #28 已合并，Squash Commit 为 `8882c98`；
- PR #28 已在 PR 讨论中记录 `AI Review: PASS`；
- `master` 与 `origin/master` 一致，恢复时工作树干净；
- 前序计划的 Method、Skill Inventory 与 AI Review Governance 范围已经进入 `master`；
- 前序计划没有追加合并后 Closure Record；
- PR #28 之后没有完成 Contract / Skill / Operating Guide / Eval 对齐的 `master` 提交。

## 4. Confirmed Findings

### F1 — Domain Context 生命周期尚未进入 Contract / Skill

Method 与 Skill Architecture 已要求：

- `clarify-intent` 识别长期领域事实候选；
- `specify` 验证候选，并按 Consumer Repository Authority 处理确认、持久化、更新与取代；
- Execute / Debug / Converge 发现长期领域事实缺失、冲突或失效时返回上游职责；
- Converge 在 `READY` 前检查相关长期权威产物已完成生命周期闭环。

当前 Contract 与相关 `SKILL.md` 仍主要按旧 Product Intent / ADR 语义运行。

### F2 — Architecture Context 与 ADR 在低层仍被混同

Method 已区分：

- 跨功能持续有效的架构状态进入 Architecture Authority；
- 只有需要保留决定背景、主要权衡或替代关系的重要决定才形成 ADR。

当前 `technical-plan` Contract / Skill 仍写为“不满足 ADR 条件则继续留在 Technical Plan”，会漏掉不需要 ADR、但必须更新 Architecture Context 的架构状态。

### F3 — Converge Exit Condition 尚未对齐

Method 已要求 `READY` 前同时满足领域、架构 / ADR 权威与 Artifact Lifecycle Closure；Contract / Skill / Consumer Guide 尚未完整表达。

### F4 — Method Decision 与恢复记录缺口

`docs/decisions/method-decisions.md` 尚未轻量记录本轮已经确定的产物生命周期责任分配及“不新增 Super-skill / 固定目录”的方法选择。前序计划也缺少最终状态与后继工作指针。

### F5 — 缺少针对性 Runtime Evidence

现有 Behavior Eval 没有覆盖 Domain Authority 候选、非 ADR Architecture Context 更新、下游阶段回流与 Artifact Lifecycle Gap 阻止 `READY` 的场景。

## 5. Scope

### Included

- `docs/decisions/method-decisions.md`
- `docs/architecture/skill-contracts.md`
- `docs/architecture/first-batch-skill-design.md`
- `skills/clarify-intent/SKILL.md`
- `skills/specify/SKILL.md`
- `skills/technical-plan/SKILL.md`
- `skills/execute-unit/SKILL.md`
- `skills/systematic-debug/SKILL.md`
- `skills/converge/SKILL.md`
- `skills/readiness-check/SKILL.md`（仅当 Contract 对齐确认确有影响）
- `docs/guides/using-agentic-dev.md`
- 最小必要 Behavior Eval 与 Eval 说明
- 本计划与前序计划的最小 Closure / Successor 回写

### Non-goals

- 修改 PR #28 已确定的 Method 语义；
- 新增核心 Skill、方法阶段或 Controller；
- 创建 Domain Context Skill、Architecture Management Skill 或 Artifact Management Super-skill；
- 强制 Consumer 使用固定目录、模板、文件名或审批流；
- 把 `agentic-dev` 的项目级 AI Review Governance 自动传播给 Consumer；
- 为形式覆盖机械扩展全部 Skill Eval。

## 6. Work Items / Status

| ID | Work Item | Status | Current Evidence / Result |
|---|---|---|---|
| W1 | 建立恢复 Plan 与隔离分支 | COMPLETE | 分支与可恢复 Plan 已创建，初始证据已记录 |
| W2 | 补充轻量 Method Decision | COMPLETE | 已新增 D-019，记录生命周期责任分配与不采用的集中式方案 |
| W3 | 对齐 Skill Contract 与第一批 Skill Design | COMPLETE | 已区分 Domain candidate、Architecture Context、ADR 与 Artifact Lifecycle Gap |
| W4 | 对齐受影响核心 Skills | COMPLETE | 7 个核心 Skill 已完成 Domain / Architecture / Lifecycle 职责对齐 |
| W5 | 对齐 Consumer Operating Guide | COMPLETE | 已补充 Domain Authority、Architecture Context / ADR 分离与收敛路由 |
| W6 | 增加并运行针对性 Eval / Skill Validation | COMPLETE | 7 个 Skill validation PASS；Artifact Lifecycle Fresh Runtime Behavior 7 / 7 PASS |
| W7 | 重新读取最终状态并执行 AI Review | COMPLETE | 修复 1 个 Medium Finding 后 targeted re-review PASS；无未解决 Blocking / Medium Finding |
| W8 | Commit / Push / PR / Verify | COMPLETE | 6 个分层提交已推送；Draft PR #29 已创建并完成元数据、评论、文件与 compare 写后验证 |
| W9 | 回写前序计划 Closure 与本计划最终结果 | COMPLETE | 前序计划 Closure / Successor 与本计划最终发布结果均已固化 |

## 7. Required Semantic Mapping

实现与复核时至少确认：

1. Domain candidate：识别、验证、授权确认、持久化、更新、取代、升级边界完整；
2. Architecture state：Architecture Context 更新与 ADR 条件产生分离；
3. Stage Return：Execute / Debug / Converge 不在下游静默提升长期权威；
4. Gate / Closure：Readiness 按其职责阻止未解决的权威缺口，Converge 阻止未闭环 Artifact 的 `READY`；
5. Consumer boundary：载体和写入权限由 Consumer Repository Authority 决定；
6. Skill boundary：不新增全生命周期管理 Skill，不扩大单个 Skill 职责；
7. Evidence：关键行为至少有静态一致性检查和风险相称的 Fresh Runtime Eval。

## 8. Resumption Protocol

Fresh Context 恢复时只需：

1. 读取 `AGENTS.md` 与 `tasks/README.md`；
2. 读取本计划的 `Recovery State`、`Confirmed Findings`、`Work Items / Status` 与 `Evidence Log`；
3. 确认当前分支、`git status` 与 `HEAD`；
4. 只重新读取当前 `IN PROGRESS` Work Item 所需的上游 Authority 和目标文件；
5. 完成一个 Work Item 后立即更新状态与证据，不依赖聊天记忆；
6. 如果发现 Method Gap，停止低层实现并先修改更高层权威；如果只是 Contract / Skill 对齐，保持本计划范围继续。

## 9. Completion Criteria

- Method Decision、Contract、Skill Design、Skill Implementation 与 Operating Guide 对 Artifact Lifecycle 语义一致；
- Architecture Context 与 ADR 在所有受影响层保持明确区分；
- Domain Authority 候选与阶段回流职责可由 Fresh Agent 直接执行；
- `converge` 不会在存在 Artifact Lifecycle Gap 时输出 `READY`；
- 没有新增核心 Skill、方法阶段、固定 Consumer Artifact 结构或 Super-skill；
- 受影响 Skill 通过 `skill-creator` validator；
- 针对性 Eval 产生当前可复核证据；
- 最终 AI Review 不存在未解决的 Blocking / Medium Finding；
- PR 中记录最终 AI Review 摘要，且集成仍由 Human Authority 决定；
- 前序计划和本计划都留下足以跨 Fresh Context 恢复的最终状态指针。

## 10. Evidence Log

### 2026-08-20 — Recovery Initialization

- `master == origin/master == 8882c98`；
- PR #28：`https://github.com/dygapp/agentic-dev/pull/28`，状态 `merged`；
- 当前实际 Skill 目录 9 个，带 `name` front matter 的 manifest 9 个；
- `git diff --check` 在恢复前基线通过；
- 已创建分支 `codex/artifact-lifecycle-operationalization`；
- 已确认 F1–F5，开始 W1。

### 2026-08-20 — Authority / Contract Alignment

- 新增 D-019，未修改 PR #28 已确定的 Method 正文；
- Contract Matrix 与各 Skill Contract 已补充 Domain Authority、Architecture Context / ADR 分离、Stage Return 与 Converge Closure；
- 第一批 Skill Design 已同步实现重点；
- `git diff --check`：PASS；
- W2、W3 完成，进入 W4。

### 2026-08-20 — Skill / Operating Guide Alignment

- 已更新 `clarify-intent`、`specify`、`technical-plan`、`readiness-check`、`execute-unit`、`systematic-debug`、`converge`；
- 已同步 Consumer Guide 中的 Domain candidate、Architecture Context / ADR、Readiness 与 Converge 路由；
- 未新增 Skill、方法阶段、固定 Artifact 目录或模板；
- W4、W5 完成，进入 W6。

### 2026-08-20 — Validation / Fresh Runtime Evidence

- 7 个受影响 Skill 均通过 `skill-creator/scripts/quick_validate.py`；环境没有 PyYAML，验证时通过 `/tmp/agentic-dev-skill-validator-shim/yaml.py` 调用本机 Node `yaml` parser，没有修改项目依赖或用户环境；
- 新增 7 个最小 Artifact Lifecycle Behavior 场景：`B-CI-04`、`B-SP-01`、`B-TP-01`、`B-RC-04`、`B-EU-05`、`B-SD-01`、`B-CG-05`；
- 在仓库外隔离 workspace 中完成 Fresh Runtime 重跑，进程均正常结束；人工按 assertion 逐项分级结果为 `7 / 7 PASS`；
- Trace 未读取本仓库 Eval 定义、历史结果或隔离 workspace 外上下文；场景内无 Git repository 时的 `git status` 失败没有影响语义结果；
- JSON 语法、Eval runner Python 编译与 `git diff --check` 均通过；
- W6 完成，进入 W7 最终 AI Review。

### 2026-08-20 — Final AI Review / Targeted Re-review

- Review 输入：`master@8882c98` 权威基线、当前最终 diff、受影响 Method / Architecture / Contract / Skill / Operating Guide、术语规范与 Runtime evidence；
- Review 维度：Authority Alignment、Semantic Regression、Cross-layer Consistency、Scope Control、Terminology、Human / Integration Boundary、Evidence Alignment、Artifact Lifecycle Closure；
- 初次 Review 发现 1 个 Medium Finding：`technical-plan` 已要求非 ADR 的 Architecture Context 更新，但旧的“无需长期 Technical Plan”输出仍可能被理解为不产生任何长期 Artifact 并直接进入 Slice；
- 已修复为：无需 Technical Plan Artifact 不豁免必要的 Architecture Authority 更新；同时精确区分 Clarify Intent 识别候选与 Specification 验证候选，并移除 `converge` 重复输入表述；
- 修复后重新运行 `B-TP-01` Fresh Runtime Eval，人工语义分级 PASS：不创建 Technical Plan Artifact，要求更新现有 `architecture-overview`，不机械创建 ADR；
- 7 个受影响 Skill validator、7 个相关 Behavior JSON、Eval runner Python 编译与 `git diff --check` 全部 PASS；
- Targeted re-review 未发现未解决的 Blocking / Medium Finding；本地结论为 `AI Review: PASS`。该结论不等于 Human Approval 或 Merge Authorization；采用 PR 后仍必须把摘要记录到 PR 讨论或正式 Review。
- 前序计划已追加 PR #28 Closure / Successor 指针；W7 完成，W9 已完成前序指针部分。

### 2026-08-20 — Publish / Closure

- 按 Authority 层级形成 6 个分层提交：Method Decision、Contract / Architecture、Skill Implementation、Consumer Guide、Eval、Task Recovery Record；
- 分支 `codex/artifact-lifecycle-operationalization` 已推送到 `origin`；
- 创建 Draft PR #29：`https://github.com/dygapp/agentic-dev/pull/29`，目标为 `master@8882c98`；
- 写后重新读取确认：PR 为 `open`、`draft`、`mergeable`，head 正确；22 个预期文件完整，分支相对 `master` 为 ahead 6 / behind 0；
- 最终 AI Review 摘要已记录到 PR 讨论：`https://github.com/dygapp/agentic-dev/pull/29#issuecomment-5354842030`；
- W8、W9 完成；本计划关闭于 Draft PR / Human Review 边界，不授予 Merge 权限。

## 11. Blockers

当前无 Blocking External Dependency。后续 Human Review / Merge 不属于本计划授权范围。

如果后续 GitHub 写操作因权限、网络或授权失败，应保留本地已验证状态和精确失败证据，不把工具调用失败误报为已发布。
