# Implement specify Skill

## Goal

根据已复核的 Skill Contract 与第一批 Skill 设计基线，实现第四个核心 Skill：`specify`，将已经澄清的 Product Intent 形成或增量更新为 WHAT / WHY Specification，使 Fresh Agent 能独立理解 Required Behavior、Boundary 与 Completion。

## Authority Inputs

实现时按仓库权威顺序使用以下输入：

1. `AGENTS.md`
2. `docs/method/ai-development-method.md`
3. `docs/architecture/skill-architecture.md`
4. `docs/architecture/skill-contracts.md`
5. `docs/architecture/first-batch-skill-design.md` 作为已冻结契约的实现设计说明，不得覆盖前四项权威。

若实现过程中发现权威输入存在冲突或 Contract 不足，不得通过 `SKILL.md` 静默修正；应停止实现并先回到对应权威层处理。

## Scope

- 创建 `skills/specify/SKILL.md`；
- 实现 reviewed contract 中规定的 Purpose、Use When、Do Not Use When、Inputs、Authority Sources、Procedure、Outputs、Exit Conditions、Escalation Conditions、Context Rules 与 Allowed Sub-skills / Disciplines；
- 形成或增量更新 WHAT / WHY Specification；
- 组织 Goal、Scope、Observable Behaviors、Business Rules、Boundary / Failure Behavior、Acceptance Criteria 与 Relevant Non-functional Constraints；
- 强制区分 Product / Domain Requirement 与技术实现 HOW；
- 默认排除 Source File Paths、Class / Function Names、Framework-specific Construction Details、Database Implementation Choices 与 Step-by-step Edit Instructions；
- 对 Existing Specification 支持增量更新，保留未受已确认 Product Decision 影响的既有权威内容；
- 执行 Fresh-Agent Spec Ready 自检，确认 Fresh Agent 能判断要做什么、不做什么、何时完成以及是否仍有关键歧义；
- Requirement / Authority Conflict、Product Decision 缺失或必须 materially change 已确认 Scope / Intent 时停止并升级或返回 `clarify-intent`；
- 同步 `skills/README.md` 的实现状态。

## Out of Scope

- 不重新承担 `clarify-intent` 的 Product Intent 决策职责；
- 不创建 Technical Plan；
- 不生成 Execution Units、JIT Plan、代码或测试；
- 不通过 Current Code 或实现便利性反向发明 Product Requirement；
- 不固定 Specification 文件名、目录或持久化载体；
- 不强制特定 Markdown / YAML 模板或 Front Matter；
- 不加入 Framework、Persistence、Source Path 等 HOW 字段作为通用 Specification 要求；
- 不实现其他 Skill；
- 不自动推进到 `technical-plan`、`slice-work` 或后续生命周期。

## Validation

至少验证以下行为：

1. 已澄清 Intent 可以形成让 Fresh Agent 独立理解 Required Behavior 与 Completion 的 Specification；
2. Existing Specification 可以根据已确认 Product Decision 增量更新，而不无谓重写未受影响内容；
3. Product Decision 尚未解决时停止并返回 `clarify-intent`，不猜测补齐需求；
4. Requirement / Authority Conflict 时停止并升级，不自行选择方便实现的解释；
5. Source Paths、Classes、Framework、Persistence 与逐步施工指令等 HOW 细节不会被错误固化为通用 Specification 内容；
6. Observable Behaviors 与 Business Rules 能明确说明系统必须呈现的产品行为；
7. Boundary / Failure Behavior 足以说明关键边界与失败时应呈现的产品语义；
8. Acceptance Criteria 可观察、可验证，但不通过指定实现方式来定义完成；
9. Relevant Non-functional Constraints 只在确有权威要求时记录，不凭常见实践发明；
10. Fresh-Agent Spec Ready 自检能明确回答“做什么、不做什么、何时完成、是否仍有关键歧义”；
11. Current System / Existing Authoritative Behavior 可作为输入，但不能反向覆盖更高层 Product Authority；
12. 输出保持 WHAT / WHY，并且不自动进入 Technical Planning、Slice 或 Execute。

验证应基于 Skill 文本契约进行 context-isolated 行为检查；如仓库已有适用验证机制，应优先复用现有机制。

## Acceptance Criteria

- `skills/specify/SKILL.md` 存在且职责单一；
- 实现内容与 `skill-contracts.md` 中 reviewed contract 一致；
- 未通过实现新增或改变方法语义；
- 与 `clarify-intent`、`technical-plan`、Execute 内 JIT Planning 的职责边界明确；
- WHAT / WHY 与 HOW 的边界可由 Fresh Agent 明确执行；
- Existing Specification 增量更新语义明确；
- Spec Ready Gate 的四个判断问题明确且有可执行检查步骤；
- 至少完成一轮 current evidence 支持的契约验证；
- 实现变更与任何必要的 Contract Change 保持独立提交。

## Commit Guidance

如果权威 Contract 无需修改，本任务的 Skill Implementation 提交使用仓库既有 Commit 规范：

```text
feat(skills): 实现 specify Skill
```

配套文档同步可单独使用：

```text
docs(skills): 同步 specify 实现状态
```

如验证形成独立持久化用例，再使用：

```text
test(skills): 验证 specify Skill 契约行为
```
