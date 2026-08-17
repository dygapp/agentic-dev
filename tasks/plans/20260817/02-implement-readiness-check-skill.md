# Implement readiness-check Skill

## Goal

根据已复核的 Skill Contract 与第一批 Skill 设计基线，实现首个核心 Skill：`readiness-check`，并验证统一 `SKILL.md` 结构和只读 Gate 语义是否可执行。

## Authority Inputs

实现时按仓库权威顺序使用以下输入：

1. `AGENTS.md`
2. `docs/method/ai-development-method.md`
3. `docs/architecture/skill-architecture.md`
4. `docs/architecture/skill-contracts.md`
5. `docs/architecture/first-batch-skill-design.md` 作为已冻结契约的实现设计说明，不得覆盖前四项权威。

若实现过程中发现权威输入存在冲突或 Contract 不足，不得通过 `SKILL.md` 静默修正；应停止实现并先回到对应权威层处理。

## Scope

- 创建 `skills/readiness-check/SKILL.md`；
- 实现 reviewed contract 中规定的 Purpose、Use When、Do Not Use When、Inputs、Authority Sources、Procedure、Outputs、Exit Conditions、Escalation Conditions、Context Rules 与 Allowed Sub-skills / Disciplines；
- 保持 `readiness-check` 为只读 Checker；
- 实现 Specification / Design / Execution / Governance 四维 Gate；
- 区分 Blocking 与 Non-blocking Findings；
- Blocking Finding 必须指出应返回的职责层，不自行修改 Specification、Technical Plan 或 Execution Units；
- 允许 Controller / Runtime 自动调用，不要求 Human 手工触发；
- 在第一个 Skill 落地后同步修正 `skills/README.md` 的当前阶段说明。

## Out of Scope

- 不修改 Method；
- 不修改 Skill Architecture；
- 不修改 Skill Contract，除非实现暴露真实契约问题并先单独处理；
- 不实现其他 Skill；
- 不引入独立 Reviewer Agent；
- 不自动 Rewrite Specification / Technical Plan / Execution Units；
- 不绑定 GitHub、Jira 或其他 Runtime-specific 调度协议；
- 不新增通用 Skill Runtime 元数据规范。

## Validation

至少验证以下行为：

1. 完整且一致的输入可以得到 `PASS`；
2. Specification 存在阻塞缺口时形成 Blocking Finding；
3. 必要 Technical Planning 未解决时形成 Blocking Finding；
4. Execution Unit 不可执行、不可验证或覆盖不足时形成 Blocking Finding；
5. Governance / Authority 冲突时停止并升级；
6. 非阻塞问题不会被错误当作 Blocking Finding；
7. Checker 不会静默修改任何权威 Artifact；
8. Blocking Finding 能明确指出返回的职责层；
9. 结果可以明确判断是否允许进入 Execute。

验证应基于 Skill 文本契约进行 fresh-context 行为检查；如果仓库已有适用验证机制，应优先复用现有机制。

## Acceptance Criteria

- `skills/readiness-check/SKILL.md` 存在且职责单一；
- 实现内容与 `skill-contracts.md` 中 reviewed contract 一致；
- 未通过实现新增或改变方法语义；
- Authority、Exit、Escalation、Context Rule 均明确；
- Blocking / Non-blocking Finding 及返回职责层语义明确；
- 至少完成一轮 current evidence 支持的契约验证；
- 实现变更与任何必要的 Contract Change 保持独立提交。

## Commit Guidance

如果权威 Contract 无需修改，本任务的 Skill Implementation 提交使用仓库既有 Commit 规范：

```text
feat(skills): 实现 readiness-check Skill
```

配套文档同步可单独使用：

```text
docs(skills): 同步首个 Skill 实现状态
```

如验证形成独立持久化用例，再使用：

```text
test(skills): 验证 readiness-check Skill 契约行为
```

## Validation Result — 2026-08-17

### Method

采用 context-isolated scenario review：判断时只使用当前 `skills/readiness-check/SKILL.md` 的行为定义和每个场景显式给出的模拟输入，不依赖 Conversation History 中的项目事实。当前仓库尚未建立独立 Skill Runtime / Test Harness，因此本轮验证不新增 Runtime-specific 测试框架。

同时将当前实现逐节对照 reviewed Contract，检查必需章节、四维 Gate、只读边界、Exit 与 Escalation 语义。

### Static Contract Check

结果：**PASS**。

已确认当前实现包含并对齐：

- Purpose
- Use When
- Do Not Use When
- Inputs
- Authority Sources
- Procedure
- Outputs
- Exit Conditions
- Escalation Conditions
- Context Rules
- Allowed Sub-skills / Disciplines

实现覆盖 Specification / Design / Execution / Governance 四维 Gate；没有新增超级 Skill、自动 Artifact Rewrite、自动 Execute / Integration 或 Runtime-specific 调度协议。

静态检查过程中发现一项实现偏差：初版曾把“输出 Blocking Findings 后停止检查”也写成 Exit Condition，而 reviewed Contract 的 Exit Condition 是“不存在 Blocking Finding”。该问题已在实现层修正，无需修改 Contract。

### Scenario Checks

| Case | Minimal Input Condition | Expected Result | Result |
|---|---|---|---|
| 1 | Specification 清楚、Acceptance 可验证、无必要长期 Technical Plan、Units 覆盖完整且可独立验证、Governance 无冲突 | `PASS` | PASS |
| 2 | Acceptance Criteria 只有模糊目标，无法观察完成状态 | Blocking / Specification / Return To `specify` | PASS |
| 3 | 输入表明存在跨 Unit 的重大持久技术决定，但尚未完成必要 Technical Planning | Blocking / Design / Return To `technical-plan` | PASS |
| 4 | Unit 缺少可验证 Completion Condition，或 Requirement Coverage 明显缺失 | Blocking / Execution / Return To `slice-work` | PASS |
| 5 | Repository Authority 与当前工作要求冲突，Agent 无权自行裁决 | Blocking / Governance + Human / Explicit Policy Escalation | PASS |
| 6 | 只有普通命名偏好、低影响可逆实现建议 | `PASS`，可附 Non-blocking Finding | PASS |
| 7 | 调用者要求 Checker 顺便修改 Specification / Plan / Units 使其通过 | 拒绝静默修改；输出对应 Finding / Return To | PASS |
| 8 | 存在 Blocking Finding | 不输出 `PASS`，明确 Dimension / Evidence / Return To / Escalation | PASS |

### Acceptance Review

- `skills/readiness-check/SKILL.md` 已存在且职责单一：PASS
- 与 reviewed Contract 一致：PASS
- 未修改 Method / Architecture / Contract：PASS
- Authority / Exit / Escalation / Context 明确：PASS
- Blocking / Non-blocking 与返回职责层明确：PASS
- 已有 current evidence 支持的首轮契约验证：PASS

结论：`readiness-check` 首版实现已达到当前任务 Acceptance Criteria，可进入 PR Review；不代表第一批其他 Skills 已完成。
