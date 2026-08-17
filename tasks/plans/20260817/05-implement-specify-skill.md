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

## Validation Evidence

**状态：** PASS  
**验证对象：** `skills/specify/SKILL.md` 当前分支版本  
**验证性质：** 静态 Contract 对照 + context-isolated 文本行为检查；当前仓库尚无独立 Skill Runtime / 自动化 harness，因此不将本轮结果表述为 Runtime 执行测试。

### Static Contract Review

- 统一 11 个 `SKILL.md` 契约章节均已实现；
- Purpose 与 reviewed contract 一致，限定为创建或更新 WHAT / WHY Authority；
- Inputs、Authority Sources、Exit Conditions、Escalation Conditions 与 Context Rules 均有显式定义；
- 未引入固定文件名、目录、Markdown / YAML 模板、Front Matter 或 Runtime-specific 协议；
- 未修改 Method、Skill Architecture 或 reviewed Skill Contract；
- 未把 `technical-plan`、`slice-work`、Execute / JIT Planning 的职责并入本 Skill。

### Context-isolated Scenario Checks

1. **Clarified Intent → Specification：PASS** — Procedure 3–8 可以形成 Goal、Scope、Behaviors、Rules、Boundary、Acceptance 与相关 NFR，Procedure 11 检查 Fresh-Agent 可理解性。
2. **Existing Specification 增量更新：PASS** — Procedure 2 明确只修改受影响 WHAT / WHY，并保留未受影响 Existing Authority，同时要求最终自洽。
3. **Product Decision 未解决：PASS** — Procedure 1 / 10 / 11 均要求返回 `clarify-intent`，不猜测补齐 Requirement。
4. **Requirement / Authority Conflict：PASS** — Authority Sources 与 Escalation Conditions 要求停止并升级，不选择方便实现的解释。
5. **HOW 泄漏：PASS** — Procedure 9 显式过滤 Source Paths、Classes、Framework、Persistence、Exact Commands 与 JIT Plan。
6. **Observable Behaviors / Business Rules：PASS** — Procedure 4 / 5 分别定义可观察 Product Outcome 与有权威依据的业务规则。
7. **Boundary / Failure Behavior：PASS** — Procedure 6 只纳入会改变 Product Semantics / Acceptance 的关键边界与失败行为。
8. **Observable Acceptance：PASS** — Procedure 7 要求可观察、可区分完成状态，并禁止用内部实现方式定义 Product Acceptance。
9. **Relevant NFR：PASS** — Procedure 8 只记录已有权威要求的 NFR，不因模板完整性发明约束。
10. **Fresh-Agent Spec Ready：PASS** — Procedure 11 明确检查 What / Not What / Completion / Ambiguity 四项。
11. **Current System 不反向覆盖 Product Authority：PASS** — Authority Sources 明确 Current Code / Tests / Database 只能反映 Current System State，不能单独成为新 Product Requirement。
12. **职责终点：PASS** — Procedure 12 与 Context Rules 明确输出 Specification 后退出，不自动 Technical Planning、Slice、Readiness 或 Execute。

### Review Conclusion

本轮未发现实现层偏差，也未发现必须修改 Method / Architecture / Skill Contract 才能解决的问题。当前 `specify` 实现满足 task 05 的 Acceptance Criteria，可以进入 PR Review。

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
