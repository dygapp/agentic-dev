# 收敛项目治理与复用边界

## 状态

实施完成，待 Review / Integration。

## Goal

消除 `agentic-dev` 当前运行中仍可能依赖 Conversation History、其他项目经验或未固化工作习惯的隐含知识，并明确 Reusable Skill、Project Rule 与 Bootstrap / Setup Capability 的最小边界。

本工作只做 Repository Self-containment 收敛，不扩展方法生命周期，不新增 Skill，不建设新的 Runtime / Distribution / Controller Framework。

## Authority Inputs

按仓库权威顺序使用：

1. `AGENTS.md`
2. `docs/method/ai-development-method.md`
3. `docs/method/principles.md`
4. `docs/architecture/skill-architecture.md`
5. `docs/architecture/skill-contracts.md`
6. `docs/decisions/method-decisions.md`
7. `docs/guides/git-commit-guidelines.md`
8. `docs/research/*`
9. Tasks / 临时工作记录

GitHub `master` 是本轮工作的基线。

## Targeted External Review

只复核既有研究范围：

- `mattpocock/skills`
- `github/spec-kit`
- `obra/superpowers`

针对性结论：

- 外部项目普遍区分可复用能力与项目实例规则；
- Setup / Constitution / Initial Instructions 等机制证明“通用流程 → 项目级规则”的分层有实际价值；
- 不同项目采用 Skill、Command、Template、Instruction 等不同实现，因此“跨项目可复用”不能直接推出“必须 Skill 化”。

不增加新的研究样本。

## Scope

### `AGENTS.md`

- 明确其他会话、其他项目和个人记忆不能直接成为当前项目事实；
- 明确外部经验必须先在当前 Repository Authority 中固化；
- 增加到 `tasks/README.md` 的工作协调 Context Pointer；
- 将当前阶段执行重点收敛为 Repository Self-containment + 真实 Repository 验证。

### `docs/architecture/skill-architecture.md`

- 区分 Reusable Skill、Project Rule、Bootstrap / Setup Capability；
- 明确 Project Rule 可以选择或限制 Skill，但 Skill 不得覆盖 Repository Authority；
- 明确 Project Bootstrap 不预设必须实现为 Skill；
- 明确新增 Skill 继续要求真实职责缺口与复用证据。

### `tasks/README.md`

- 移除过期的 `First Skill Implementation` 阶段说明；
- 固化当前项目实际使用的 `tasks/plans/YYYYMMDD/NN-name.md` 协调约定；
- 明确简单工作不创建 Plan；
- 明确 Plan 不是 Method Authority，也不等同于 Execution Unit。

### `docs/research/README.md`

- 只记录本轮针对性外部复核结论；
- 不重写既有三个研究分析；
- 不把 Research 升级为 Method Authority。

## Non-goals

本轮不做：

- 新增第九个核心 Skill；
- 创建 `project-governance` / `project-foundation` 等新 Skill；
- 创建新的 Template / Preset / Bundle / Marketplace；
- 创建完整 Task Governance Framework；
- 创建 Controller / Worker Runtime；
- 扩展 Runtime Eval / Benchmark；
- 引入第四个方法论研究项目；
- 修改第一批 8 个 `SKILL.md`。

## Completion Criteria

- 当前 Repository 可以独立说明本项目知识边界；
- Skill / Project Rule / Bootstrap 边界有单一架构权威；
- `tasks/plans` 的当前项目使用规则不再依赖其他会话记忆；
- 没有新增 Skill、Method Stage、Runtime Layer 或重复 Governance Artifact；
- Research 仅作为增量证据，不覆盖 Method / Contract；
- 下一步可以直接进入 First Real Repository Validation。

## Next Step

本 Plan 完成并集成后，不再为上述治理边界单独增加 Eval。

下一项工作应进入：

> **First Real Repository Validation**

使用当前 8 个核心 Skills 和当前 Repository Rules 完成真实 Feature / Defect 工作，再根据真实证据决定是否需要 Runtime、Skill、Contract 或 Method hardening。
