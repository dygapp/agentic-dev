# GitHub Actions 验证能力落地计划

## Goal

基于 Consumer Experiment #18 的 EU-01 真实证据，将 GitHub / GitHub Actions 验证路径中的可观察性、分支与 PR 协作、验证成本控制和可诊断 Runtime 经验固化为可复用能力，同时保持 Method 的平台无关性。

## Authority / Inputs

- `AGENTS.md`
- `docs/architecture/skill-architecture.md`
- `docs/guides/external-operation-guidelines.md`
- `docs/guides/terminology-guidelines.md`
- `skills/execute-unit/SKILL.md`
- Experiment Issue #18 及其引用的 Consumer Evidence

## Scope

1. 明确平台专项非核心 Reusable Skill 的架构边界，并登记 `github-actions-verification`。
2. 在 External Operation Guide 中补充 Git / GitHub 执行隔离、PR 与 CI 可观察性路径选择原则。
3. 新增 `github-actions-verification` Skill，覆盖 GitHub Actions 验证路径选择、Fast Feedback / Completion Verification、预构建 Runtime、容器化 E2E、Artifact 复用、超时与取消、诊断证据等。
4. 小幅更新 `execute-unit`，在 GitHub Actions 验证场景按需组合该 Skill，并在选择验证机制时考虑证据可观察性与反馈成本。
5. 回写 Issue #18 Maintainer Review，记录本轮分类与落地范围。

## Non-goals

- 不把 GitHub、PR、GHCR、MCR 或容器拓扑写成 Method 通用强制规则。
- 不修改第一批 8 个核心 Skill 的 Contract。
- 不创建接管完整 GitHub 项目生命周期的超级 Skill。
- 不自动 Merge。
- 不进行与本轮范围无关的全仓术语重写。

## Work Order

1. Architecture / Guide authority alignment。
2. Skill implementation and references。
3. `execute-unit` composition alignment。
4. Touch-scoped terminology convergence。
5. Verify diff / repository state。
6. Update Experiment Issue #18。
7. Create one Ready PR and stop at Human Merge。

## Completion Criteria

- 变更保持 Method 平台无关，Contract 未变化。
- 新 Skill 具有明确 Purpose、Use When、Do Not Use When、Inputs、Procedure、Outputs、Exit / Escalation Conditions。
- GitHub Actions 具体经验以可条件触发 Pattern 固化，不覆盖 Consumer Repository Policy。
- 所有触及的旧文档在本次修改范围内符合 `terminology-guidelines.md`，遵循“旧内容按触达逐步收敛”。
- PR diff 仅包含本计划范围内文件；PR 为 Ready，最终由 Human Merge。
