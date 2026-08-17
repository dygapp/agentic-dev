# Implement slice-work Skill

## Goal

根据已复核的 Skill Contract 与第一批 Skill 设计基线，实现第二个核心 Skill：`slice-work`，将 Ready Specification 与可选 Technical Plan 转换为适合 Fresh Agent 独立执行和验证的纵向 Execution Units。

## Authority Inputs

实现时按仓库权威顺序使用以下输入：

1. `AGENTS.md`
2. `docs/method/ai-development-method.md`
3. `docs/architecture/skill-architecture.md`
4. `docs/architecture/skill-contracts.md`
5. `docs/architecture/first-batch-skill-design.md` 作为已冻结契约的实现设计说明，不得覆盖前四项权威。

若实现过程中发现权威输入存在冲突或 Contract 不足，不得通过 `SKILL.md` 静默修正；应停止实现并先回到对应权威层处理。

## Scope

- 创建 `skills/slice-work/SKILL.md`；
- 实现 reviewed contract 中规定的 Purpose、Use When、Do Not Use When、Inputs、Authority Sources、Procedure、Outputs、Exit Conditions、Escalation Conditions、Context Rules 与 Allowed Sub-skills / Disciplines；
- 建立 Specification Coverage 视图，并优先按 Observable Behavior / Verifiable Outcome 形成 Vertical Execution Units；
- 每个 Execution Unit 至少包含 `id`、`goal`、`spec_reference`、`completion_condition`、`dependencies`、`constraints`；
- 检查 Bounded、Context-fit、Independent Verification 与 Hidden Dependency；
- 调整过大、横向分层或高度耦合的 Unit；
- 输出可交给 `readiness-check` 的候选 Unit Set，但不承担最终 Readiness Verdict；
- 同步 `skills/README.md` 的实现状态。

## Out of Scope

- 不修改 Method；
- 不修改 Skill Architecture；
- 不修改 Skill Contract，除非实现暴露真实契约问题并先单独处理；
- 不实现 `readiness-check`、`execute-unit` 或其他 Skill 的职责；
- 不绑定 Jira、GitHub Issue、Markdown Task 或特定 Runtime Object；
- 不要求长期 Execution Unit 包含精确 Source File Paths；
- 不提前固化 Exact Test Commands、逐文件施工步骤或其他 JIT Execution Plan 内容；
- 不定义 Worker 分配、Queue 调度或 Controller Runtime 协议；
- 不强制一个 Feature 必须拆成多个 Unit；如果一个纵向 Unit 已满足契约，可以只产生一个 Unit。

## Validation

至少验证以下行为：

1. Ready Specification 可以形成至少一个可追溯、可验证的 Vertical Execution Unit；
2. 多个独立 Observable Behaviors 可以被合理拆为多个 Unit，并保持需求覆盖；
3. 过大的 Unit 会被继续拆分或塑形，而不是直接交给 Execute；
4. 纯横向技术层拆分会被识别并优先调整为 Vertical Outcome；
5. Hidden Dependency、错误依赖顺序或高度耦合能够被识别并显式化；
6. 每个 Unit 都包含最小逻辑字段，且 Completion Condition 可观察、可验证；
7. Unit 不新增 Specification 未授权的 Product Scope；
8. 长期 Unit 不依赖易过时的精确文件路径，也不包含 JIT 施工细节；
9. Product Intent 仍有阻塞歧义时停止并返回上游，而不是猜测拆分；
10. 必要 Major Design Decision 尚未解决时停止并返回 `technical-plan` / Human Authority；
11. 输出只声明 Unit Set 可进入 `readiness-check`，不自行给出最终 `PASS`。

验证应基于 Skill 文本契约进行 context-isolated 行为检查；如仓库已有适用验证机制，应优先复用现有机制。

## Acceptance Criteria

- `skills/slice-work/SKILL.md` 存在且职责单一；
- 实现内容与 `skill-contracts.md` 中 reviewed contract 一致；
- 未通过实现新增或改变方法语义；
- 形成的 Execution Unit 最小字段、Vertical、Traceable、Bounded、Context-fit 与 Independently Verifiable 语义明确；
- 明确区分 `slice-work` 与 `readiness-check`、`technical-plan`、Execute 内 JIT Planning 的职责边界；
- 至少完成一轮 current evidence 支持的契约验证；
- 实现变更与任何必要的 Contract Change 保持独立提交。

## Commit Guidance

如果权威 Contract 无需修改，本任务的 Skill Implementation 提交使用仓库既有 Commit 规范：

```text
feat(skills): 实现 slice-work Skill
```

配套文档同步可单独使用：

```text
docs(skills): 同步 slice-work 实现状态
```

如验证形成独立持久化用例，再使用：

```text
test(skills): 验证 slice-work Skill 契约行为
```

## Validation Evidence — 2026-08-17

### Static Contract Review

对照 `docs/architecture/skill-contracts.md` 与 `docs/architecture/first-batch-skill-design.md` 完成静态复核：

- `SKILL.md` 包含统一要求的全部职责章节；
- Inputs 保持为 Specification + Optional Technical Plan；
- Execution Unit 最小逻辑字段与 reviewed contract 一致；
- `slice-work` 只形成和塑形候选 Unit Set，不承担最终 Readiness Verdict；
- 未把 Coverage View 强制为长期 Artifact；
- 未绑定特定 Tracker、Runtime、Source File Paths 或 Exact Test Commands；
- 未修改 Method、Architecture 或 Skill Contract；
- 未发现需要回到权威层修订的 Contract Gap。

### Context-isolated Scenario Check

| # | 场景 | 预期行为 | 结果 |
|---|---|---|---|
| 1 | Ready Specification，单一可验证 Outcome | 允许形成一个 Vertical Unit | 符合 |
| 2 | 多个相对独立 Observable Behaviors | 按 Outcome 形成多个可追溯 Units 并保持 Coverage | 符合 |
| 3 | 单个 Unit 过大，不适合 Fresh Context | 继续拆分 / 重塑，不直接交给 Execute | 符合 |
| 4 | 候选按数据库层 / 服务层 / 接口层横向拆分 | 优先重塑为可独立验证的 Vertical Outcome | 符合 |
| 5 | Units 存在隐藏前置、错误顺序或高度耦合 | 显式化 Dependencies / Constraints 并调整边界 | 符合 |
| 6 | Unit 缺少 Trace、Completion Condition 或其他最小字段 | 继续塑形直到最小协议完整且 Completion 可验证 | 符合 |
| 7 | 候选 Unit 包含 Specification 未授权行为 | 移除或返回上游，不通过拆分新增 Scope | 符合 |
| 8 | 候选 Unit 固化精确文件路径、编辑顺序或 Test Commands | 不作为长期 Unit 要求，留给 Execute 内 JIT Plan | 符合 |
| 9 | Product Intent 仍有阻塞歧义 | 停止拆分并返回 `clarify-intent` / `specify` | 符合 |
| 10 | Unit Boundary 依赖尚未解决的 Major Durable Design | 返回 `technical-plan`，必要时升级 Human Authority | 符合 |
| 11 | Unit Set 已完成塑形 | 只声明可进入 `readiness-check`，不输出最终 `PASS` | 符合 |

### Validation Conclusion

首轮契约验证通过。当前实现未暴露 Method / Architecture / Skill Contract 问题，可以作为 `slice-work` 第一版实现进入 PR Review。
