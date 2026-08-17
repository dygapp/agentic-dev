# Implement clarify-intent Skill

## Goal

根据已复核的 Skill Contract 与第一批 Skill 设计基线，实现第三个核心 Skill：`clarify-intent`，只解决定义正确 Product Intent 所必需的关键歧义，并形成可直接交给 `specify` 的 Clarified Intent 输出。

## Authority Inputs

实现时按仓库权威顺序使用以下输入：

1. `AGENTS.md`
2. `docs/method/ai-development-method.md`
3. `docs/architecture/skill-architecture.md`
4. `docs/architecture/skill-contracts.md`
5. `docs/architecture/first-batch-skill-design.md` 作为已冻结契约的实现设计说明，不得覆盖前四项权威。

若实现过程中发现权威输入存在冲突或 Contract 不足，不得通过 `SKILL.md` 静默修正；应停止实现并先回到对应权威层处理。

## Scope

- 创建 `skills/clarify-intent/SKILL.md`；
- 实现 reviewed contract 中规定的 Purpose、Use When、Do Not Use When、Inputs、Authority Sources、Procedure、Outputs、Exit Conditions、Escalation Conditions、Context Rules 与 Allowed Sub-skills / Disciplines；
- 只识别会 materially affect Goal、Scope、User-visible Behavior、Business Boundary、Acceptance Result 或 Significant Non-functional Obligation 的未决问题；
- 对普通、低影响、可逆的实现不确定性不升级给 Human；
- 对需要 Human Authority 的高影响歧义只提出最小必要问题；
- 输出 Goal、In Scope / Out of Scope、Key Observable Behaviors、Confirmed Product Decisions 与 Remaining Blocking Questions（如有）；
- 输出必须能够直接作为 `specify` 的输入；
- 如果没有阻塞问题，应快速退出，不制造额外讨论流程；
- 同步 `skills/README.md` 的实现状态。

## Out of Scope

- 不创建或更新正式 Specification；
- 不解决纯技术设计问题；
- 不生成 Technical Plan、Execution Units 或 JIT Plan；
- 不检查或修改代码；
- 不为了“更完整”而追问所有实现细节；
- 不把普通低影响可逆实现选择升级为 Human Decision；
- 不强制创建独立、永久的 Clarification Artifact；
- 不实现其他 Skill；
- 不绑定特定 Agent Runtime、Issue Tracker 或文档模板。

## Validation

至少验证以下行为：

1. Intent 已足够明确时快速形成 Clarified Intent，不制造多余问题；
2. 两种合理解释会产生 materially different User-visible Behavior 时识别为 Blocking Question；
3. Scope 边界不明确且会影响 Acceptance 时识别为 Blocking Question；
4. 普通、低影响、可逆实现细节不会被错误升级给 Human；
5. 纯技术设计选择不会被当作 Product Intent 问题处理；
6. 已确认的 Product Decision 能被保留并与 Remaining Blocking Questions 区分；
7. Authoritative Sources Conflict 时停止并升级，而不是自行选择解释；
8. Existing Intent 需要重新确认时可以增量收敛，不要求重建全部上下文；
9. Execute / Debug / Converge 回退的 Product Intent 歧义可以被重新澄清；
10. 输出不越权成为正式 Specification，但足以直接交给 `specify`；
11. Conversation History 不作为权威事实来源；
12. 没有阻塞 Intent 的关键歧义时满足 Exit Condition。

验证应基于 Skill 文本契约进行 context-isolated 行为检查；如仓库已有适用验证机制，应优先复用现有机制。

## Acceptance Criteria

- `skills/clarify-intent/SKILL.md` 存在且职责单一；
- 实现内容与 `skill-contracts.md` 中 reviewed contract 一致；
- 未通过实现新增或改变方法语义；
- 与 `specify`、`technical-plan` 的职责边界明确；
- 能明确区分 Product Intent Blocking Ambiguity 与普通实现不确定性；
- Human Escalation 只针对 Authority / Impact / Reversibility 要求升级的事项；
- 输出结构足以作为 `specify` 输入，但不替代 Specification；
- 至少完成一轮 current evidence 支持的契约验证；
- 实现变更与任何必要的 Contract Change 保持独立提交。

## Commit Guidance

如果权威 Contract 无需修改，本任务的 Skill Implementation 提交使用仓库既有 Commit 规范：

```text
feat(skills): 实现 clarify-intent Skill
```

配套文档同步可单独使用：

```text
docs(skills): 同步 clarify-intent 实现状态
```

如验证形成独立持久化用例，再使用：

```text
test(skills): 验证 clarify-intent Skill 契约行为
```
