# Implement execute-unit Skill

## Goal

根据已复核的 Skill Contract 与第一批 Skill 设计基线，实现第七个核心 Skill：`execute-unit`，使用最小 Fresh Execution Context 实现并证明一个 Execution Unit，且 Completion 必须由当前证据支持。

## Authority Inputs

实现时按仓库权威顺序使用以下输入：

1. `AGENTS.md`
2. `docs/method/ai-development-method.md`
3. `docs/architecture/skill-architecture.md`
4. `docs/architecture/skill-contracts.md`
5. `docs/architecture/first-batch-skill-design.md` 仅作为已冻结契约的实现设计说明，不得覆盖前四项权威。

若实现暴露权威输入冲突或 Contract 不足，不得通过 `SKILL.md` 静默修正，应先回到对应权威层处理。

## Scope

- 创建 `skills/execute-unit/SKILL.md`；
- 一次只执行一个 Current Execution Unit，不遍历整个 Feature / Queue；
- 使用 Fresh Execution Context，只加载 Repository Rules、Current Unit、Relevant Specification、Relevant Technical Plan、Relevant ADR / Domain Context、Relevant Current Code / Tests；
- 先 Inspect Actual Repository State，再决定施工方式；
- 从 Repository Rules 与实际仓库状态发现可用 Build / Test / Lint / Verification 方式，不硬编码通用命令，也不把未经验证的命令当作事实；
- JIT Execution Plan 仅在当前 Unit 有帮助时创建，并默认随当前 Execution Context 结束；
- 有稳定 Behavior Seam 时建立 Expected / Failing Evidence；
- 只实现当前 Unit 所需最小变更；
- 运行 Targeted Verification；
- Unexpected Failure 转入 `systematic-debug`；
- 根据风险执行 Review，并逻辑区分 Specification Compliance 与 Engineering Quality；
- 记录当前 Verification Evidence 与 Result State；
- 只有当前证据支持 Unit Observable Completion Condition 时才满足 Exit Condition；
- 如果执行中发现 Product Intent / Major Design 必须改变，输出 Stage Return / Authoritative Update Required，而不是静默修改上游权威；
- 同步 `skills/README.md` 实现状态。

## Out of Scope

- 不自动执行多个 Execution Units；
- 不自动遍历 Queue；
- 不自动进入 `converge`；
- 不自动 Merge / Push / Release / Deploy；
- 不把 JIT Plan 强制持久化；
- 不硬编码某语言、框架或仓库的 Build / Test / Lint Commands；
- 不通过 Current Code 反向覆盖 Product Authority；
- 不静默修改 Product Intent / Scope 或 Major Technical Design；
- 不把普通低影响可逆实现选择升级为 Human Decision；
- 不实现其他 Skill。

## Validation

至少验证以下文本契约行为：

1. 一次只执行一个 Execution Unit，不自动继续下一个 Unit；
2. 默认使用最小 Fresh Execution Context，不依赖完整 Conversation History；
3. 在实施前先 Inspect Actual Repository State；
4. Repository-specific Build / Test / Lint / Verification 方式从仓库规则和实际状态发现，而不是硬编码或猜测；
5. JIT Execution Plan 仅服务当前 Unit，默认不进入长期知识库；
6. 有稳定 Behavior Seam 时可以采用 Expected / Failing Evidence 或 TDD，但不机械强制所有场景；
7. 实现范围保持在 Current Unit，避免无授权 Scope Expansion；
8. Unexpected Failure 进入 `systematic-debug`，而不是连续猜 Patch；
9. Risk-based Review 能逻辑区分 Specification Compliance 与 Engineering Quality；
10. Completion 必须由当前 Verification Evidence 支持，不能仅凭“代码已改”声明完成；
11. Product Intent / Major Design / Authority Conflict / Destructive / Security / Privacy / 未授权 External Side Effect 会停止并返回上游或升级；
12. 输出包含 Implementation、Tests / Verification Evidence、Result State，以及必要的 Stage Return / Authoritative Update Required；
13. `execute-unit` 不自动调用 `converge` 或 Integration；
14. Current Code / Tests 可以说明 Current System State，但不能反向定义 Product Requirement。

本轮验证属于基于 `SKILL.md` 文本的 context-isolated 行为检查，不表述为 Runtime / 自动化 harness 测试。

## Acceptance Criteria

- `skills/execute-unit/SKILL.md` 存在且职责单一；
- 实现内容与 reviewed contract 一致；
- 未通过实现新增或改变方法语义；
- Fresh Context、One Unit、Actual Repository Inspection、Runtime Command Discovery、JIT Planning、Verification-before-claim 的边界明确；
- 与 `systematic-debug`、`technical-plan`、`slice-work`、`converge` 的职责边界明确；
- Completion 只能由当前证据支持；
- Human Escalation 与 Authority / Impact / Reversibility 边界一致；
- 至少完成一轮 current evidence 支持的文本契约行为验证；
- 实现变更与任何必要 Contract Change 保持独立提交。

## Commit Guidance

如果权威 Contract 无需修改：

```text
feat(skills): 实现 execute-unit Skill
```

配套状态同步：

```text
docs(skills): 同步 execute-unit 实现状态
```

如未来形成独立持久化自动化验证，再使用：

```text
test(skills): 验证 execute-unit Skill 契约行为
```
