# Acceptance Verification Closure Hardening

## Goal

基于 Issue #18 最后两条 Consumer Evidence，补齐从 Specification Acceptance Obligation 到 Execution Unit ownership、planned evidence 与 executed current evidence 的生命周期闭环。

## Authority / Inputs

- `AGENTS.md`
- `docs/method/ai-development-method.md`
- `docs/architecture/skill-architecture.md`
- `docs/architecture/skill-contracts.md`
- Issue #18 Evidence：
  - `issuecomment-5389958865`
  - `issuecomment-5390031369`
- Consumer PR `dygapp/jilinjobs-cms#11`、PR `#12` 与关联 CI Evidence

## Scope

1. 先更新 Method / Decision / Architecture 中的 Acceptance-to-Verification closure 语义。
2. 对齐 `slice-work`、`readiness-check`、`execute-unit` Contract 与 Skill Implementation。
3. 保持 `converge` 的独立 Feature-wide safety-net 职责。
4. 更新 Operating Guide、状态说明与最小针对性 Behavior Evals。
5. 基于最终 PR 状态完成验证与 AI Review，并回写 Issue #18。

## Non-goals

- 不重新处理 EU-06。
- 不修改 Consumer 产品实现。
- 不新增核心 Skill 或独立 `verify-evidence` Skill。
- 不强制一条 Acceptance 对应一个测试。
- 不把 GitHub Actions、Playwright 或 E2E 提升为通用方法要求。
- 不自动执行 Merge。

## Completion Criteria

- Method、Architecture、Contract、Skill 与 Guide 对同一闭环语义保持一致。
- Unit-level 与显式 Feature-wide verification responsibility 均有合法表达。
- 缺少 planned verification coverage 时 Readiness 不得 `PASS`。
- Unit-owned obligations 缺少 executed current evidence 时不得声明 Unit `Completed`。
- `converge` 继续独立重新检查 Feature-wide Specification-to-Evidence coverage。
- 针对性 Eval 定义通过结构验证，并完成与风险相称的 Fresh Runtime 验证或明确记录不可执行原因。
- 最终 AI Review 不存在未解决 Blocking / Medium Finding。
