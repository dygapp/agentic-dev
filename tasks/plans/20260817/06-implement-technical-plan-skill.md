# Implement technical-plan Skill

## Goal

根据已复核的 Skill Contract 与第一批 Skill 设计基线，实现第五个核心 Skill：`technical-plan`，仅在 Specification 无法直接、安全映射到当前技术系统时，解决跨 Execution Unit 有持续协调价值的长期 HOW 决策；如果不需要长期 Technical Planning，则明确返回并不制造持久 Artifact。

## Authority Inputs

实现时按仓库权威顺序使用以下输入：

1. `AGENTS.md`
2. `docs/method/ai-development-method.md`
3. `docs/architecture/skill-architecture.md`
4. `docs/architecture/skill-contracts.md`
5. `docs/architecture/first-batch-skill-design.md` 作为已冻结契约的实现设计说明，不得覆盖前四项权威。

若实现过程中发现权威输入存在冲突或 Contract 不足，不得通过 `SKILL.md` 静默修正；应停止实现并先回到对应权威层处理。

## Scope

- 创建 `skills/technical-plan/SKILL.md`；
- 实现 reviewed contract 中规定的 Purpose、Use When、Do Not Use When、Inputs、Authority Sources、Procedure、Outputs、Exit Conditions、Escalation Conditions、Context Rules 与 Allowed Sub-skills / Disciplines；
- 首先判断是否真的需要 Technical Planning；
- 仅处理跨 Execution Unit 有持续协调价值的 Durable Technical Decisions；
- 典型触发包括 Cross-module Behavior、New Data / Persistence Model、New External Integration、Migration、Shared / Public Contract Change、Deployment Topology Change、Significant Architecture Trade-off；
- 对 Technical Approach、Component Boundaries、Data / Contracts、Important Seams、Migration Strategy、Testing Strategy、Risks / Constraints 按需形成长期技术决策；
- 明确区分 Durable Technical Plan 与 Execute 内单 Unit 的 JIT Execution Plan；
- 检查并阻止 Silent Redefinition of Specification / Product Intent；
- 普通、低影响、可逆的局部实现选择不升级为长期 Technical Plan；
- 若无需长期 Technical Planning，明确返回“不需要 Technical Planning”，并不创建为创建而创建的长期 Artifact；
- 同步 `skills/README.md` 的实现状态。

## Out of Scope

- 不修改 Product Intent 或 Specification；
- 不创建 Execution Units；
- 不执行代码修改、测试或验证；
- 不提前固化当前 Unit 的精确 Source File Paths、逐文件施工顺序、Exact Test Commands 或其他 JIT Execution Plan 内容；
- 不要求固定 ADR、Architecture Diagram、Markdown / YAML 模板或特定持久化载体；
- 不把普通低影响可逆实现选择强制提升为 Architecture Decision；
- 不实现其他 Skill；
- 不自动推进到 `slice-work`、`readiness-check` 或 Execute。

## Validation

至少验证以下文本契约行为：

1. Specification 可以直接、安全映射到实现时，明确返回“不需要 Technical Planning”，且不制造长期 Artifact；
2. Cross-module Behavior 需要跨 Unit 协调时形成 Durable Technical Decisions；
3. New Data / Persistence Model 影响多个 Unit 时进入 Technical Planning；
4. New External Integration / Migration / Shared Contract Change 等触发项能被识别；
5. 普通、低影响、可逆的局部实现选择不会被错误提升为长期 Plan；
6. 文件级操作顺序、Exact Test Commands 和本地实现细节被明确留给 JIT Execution Plan；
7. Technical Plan 不会 Silent Redefinition Specification / Product Intent；
8. Major Architecture Direction、Destructive / Hard-to-reverse Data Operation、安全 / 隐私敏感决定或未授权 External Side Effect 会停止并升级；
9. Technical Approach、Boundaries、Data / Contracts、Important Seams、Migration、Testing Strategy、Risks / Constraints 只在有持续协调价值时记录；
10. Current Architecture / ADR / Codebase State 可以约束技术设计，但不能反向覆盖更高层 Product Authority；
11. Exit Condition 能明确判断实施前必须解决的技术不确定性是否已解决；
12. 输出不自动创建 Execution Units 或进入后续生命周期。

本轮验证属于基于 `SKILL.md` 文本的 context-isolated 行为检查，不表述为 Runtime / 自动化 harness 测试。

## Acceptance Criteria

- `skills/technical-plan/SKILL.md` 存在且职责单一；
- 实现内容与 `skill-contracts.md` 中 reviewed contract 一致；
- 未通过实现新增或改变方法语义；
- 能明确判断“需要 Technical Planning / 不需要 Technical Planning”；
- Durable Technical Plan 与 JIT Execution Plan 的职责边界明确；
- Silent Redefinition of Product Intent 被明确禁止；
- Human Escalation 与 Authority / Impact / Reversibility 边界一致；
- 至少完成一轮 current evidence 支持的文本契约行为验证；
- 实现变更与任何必要的 Contract Change 保持独立提交。

## Commit Guidance

如果权威 Contract 无需修改，本任务的 Skill Implementation 提交使用仓库既有 Commit 规范：

```text
feat(skills): 实现 technical-plan Skill
```

配套文档同步可单独使用：

```text
docs(skills): 同步 technical-plan 实现状态
```

如验证形成独立持久化用例，再使用：

```text
test(skills): 验证 technical-plan Skill 契约行为
```
