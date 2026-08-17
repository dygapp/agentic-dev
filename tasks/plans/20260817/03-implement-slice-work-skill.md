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
