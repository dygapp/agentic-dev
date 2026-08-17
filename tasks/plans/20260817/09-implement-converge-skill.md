# Implement converge Skill

## Goal

根据已复核的 Skill Contract 与第一批 Skill 设计基线，实现第八个核心 Skill：`converge`，从 Feature-wide 视角判断 Current System、Current Verification Evidence 与权威 Specification 是否真正收敛，并形成 `READY` 或 `GAPS`。

## Authority Inputs

实现时按仓库权威顺序使用以下输入：

1. `AGENTS.md`
2. `docs/method/ai-development-method.md`
3. `docs/architecture/skill-architecture.md`
4. `docs/architecture/skill-contracts.md`
5. `docs/architecture/first-batch-skill-design.md` 仅作为已冻结契约的实现设计说明，不得覆盖前四项权威。

若实现暴露权威输入冲突或 Contract 不足，不得通过 `SKILL.md` 静默修正，应先回到对应权威层处理。

## Scope

- 创建 `skills/converge/SKILL.md`；
- 只做 Feature-wide 收敛检查，不替代单 Unit 的 `execute-unit`；
- 使用 Specification 作为 Feature Intent 主要权威，Technical Plan（如存在）不得覆盖 Product Intent；
- 检查 Missing Behavior、Partial Implementation、Contradiction with Specification、Unrequested Behavior、Obsolete Technical Plan、Unverified Critical Behavior、Cross-unit Integration Gap；
- 基于 Current Implemented System 与 Current Verification Evidence 形成主结果 `READY` 或 `GAPS`；
- 不因 Execution Unit / Ticket 状态为 Done 就声明 `READY`；
- `GAPS` 必须包含 Gap Description、Authority / Evidence Reference、Required Stage Return 或 Execution-work Direction；
- 可在现有 Intent / Design 下修正的 Gap，描述补充或修正 Execution Work，并交回 `slice-work` 塑形为 Units；
- 需要改变 Product Intent / Major Design 的 Gap，返回相应上游阶段或升级 Human Authority；
- 只有 Feature Behavior、Implementation State 与 Current Verification Evidence 和 Specification 收敛一致时，才能进入 `Ready to Integrate`；
- 同步 `skills/README.md` 实现状态。

## Out of Scope

- 不验证或执行单个 Execution Unit；
- 不自动修改 Specification、Technical Plan 或 Execution Units 来消除 Gap；
- 不把 Unit / Ticket 状态聚合当作 Feature Completion Evidence；
- 不自动创建或执行新的 Units；
- 不自动 Merge / Push / Release / Deploy；
- 不把 `Ready to Integrate` 等同于已经完成 Integration；
- 不绑定特定语言、框架、Issue Tracker、Agent Runtime 或 CI 系统；
- 不实现其他 Skill。

## Validation

至少验证以下文本契约行为：

1. `converge` 只在 Feature-wide 收敛检查时使用，不替代单 Unit 验证；
2. Specification 是 Feature Intent 主要权威，Technical Plan 不能覆盖 Product Intent；
3. Missing Behavior 能形成 Gap；
4. Partial Implementation 能形成 Gap；
5. Contradiction with Specification 能形成 Gap；
6. Unrequested Behavior 能形成 Gap；
7. Obsolete Technical Plan 能被识别，而不是机械要求实现继续服从过时 Plan；
8. Unverified Critical Behavior 在缺少当前证据时阻止 `READY`；
9. Cross-unit Integration Gap 能形成 Gap；
10. 所有 Unit / Ticket 都 Done 但当前系统或证据不收敛时，仍不能输出 `READY`；
11. 可在现有 Intent / Design 下修复的 Gap 被描述为 Execution Work Direction 并返回 `slice-work`；
12. 需要改变 Product Intent / Major Design 的 Gap 返回相应上游阶段或 Human Authority；
13. `GAPS` 输出包含 Gap Description、Authority / Evidence Reference、Required Stage Return / Execution-work Direction；
14. 只有 Current System + Current Evidence 与 Specification 收敛一致时输出 `READY`；
15. `READY` 的含义是 `Ready to Integrate`，不自动执行 Integration；
16. Authoritative Sources Conflict 或未授权 External / Production Side Effect 会停止并升级。

本轮验证属于基于 `SKILL.md` 文本的 context-isolated 行为检查，不表述为 Runtime / 自动化 harness 测试。

## Acceptance Criteria

- `skills/converge/SKILL.md` 存在且职责单一；
- 实现内容与 reviewed contract 一致；
- 未通过实现新增或改变方法语义；
- Feature-wide、`READY` / `GAPS`、Current Evidence、Stage Return 的边界明确；
- 与 `execute-unit`、`slice-work`、`specify` / `clarify-intent`、`technical-plan` 的职责边界明确；
- `READY` 只能由当前系统和当前证据支持；
- `Ready to Integrate` 与 Integration 行为明确分离；
- 至少完成一轮 current evidence 支持的文本契约行为验证；
- 实现变更与任何必要 Contract Change 保持独立提交。

## Validation Result

本轮已完成静态 Contract 对照与 16 个 context-isolated 文本行为场景检查。

结果：

1. PASS — Feature-wide 职责与单 Unit `execute-unit` 边界明确；
2. PASS — Specification 保持 Feature Intent 主要权威，Technical Plan 不覆盖 Product Intent；
3. PASS — Missing Behavior 形成 Gap；
4. PASS — Partial Implementation 形成 Gap；
5. PASS — Contradiction with Specification 形成 Gap，且不静默改写 Specification；
6. PASS — 具有收敛意义的 Unrequested Behavior 形成 Gap；
7. PASS — Obsolete Technical Plan 被识别并路由，不要求实现机械服从过时 Plan；
8. PASS — Unverified Critical Behavior 阻止 `READY`；
9. PASS — Cross-unit Integration Gap 形成 Gap；
10. PASS — Unit / Ticket 全部 Done 但 Current System / Evidence 不收敛时仍不得 `READY`；
11. PASS — Existing Intent / Design 下的 Execution Gap 返回 `slice-work` 塑形；
12. PASS — Product Intent / Major Design Gap 返回相应上游职责或 Human Authority；
13. PASS — `GAPS` 包含 Gap Description、Authority / Evidence Reference、Required Stage Return / Execution-work Direction；
14. PASS — 只有 Current System + Current Evidence 与 Specification 收敛时输出 `READY`；
15. PASS — `READY` 只表示 `Ready to Integrate`，不执行 Integration；
16. PASS — Authority Conflict 或未授权 Shared / Production / External Side Effect 会停止并升级。

静态 Review 中发现并修正一处实现偏差：首版曾允许在“明显存在必要 Unit 未执行”时以阶段性理由继续 `converge`；冻结 Contract 的 `Do Not Use When` 不允许该例外，已修正为直接返回执行路径并停止本 Skill。

未发现需要修改 `AGENTS.md`、Method、Skill Architecture 或 Skill Contract 的问题。

## Commit Guidance

如果权威 Contract 无需修改：

```text
feat(skills): 实现 converge Skill
```

配套状态同步：

```text
docs(skills): 同步 converge 实现状态
```

如未来形成独立持久化自动化验证，再使用：

```text
test(skills): 验证 converge Skill 契约行为
```
