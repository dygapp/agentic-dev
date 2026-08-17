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
