# Implement systematic-debug Skill

## Goal

根据已复核的 Skill Contract 与第一批 Skill 设计基线，实现第六个核心 Skill：`systematic-debug`，为 Observed Defect / Unexpected Failure 提供 Reproduce → Expected vs Actual → Root Cause → Falsifiable Hypothesis → Minimal Fix → Regression Evidence 的调查与修复路径。

## Authority Inputs

实现时按仓库权威顺序使用以下输入：

1. `AGENTS.md`
2. `docs/method/ai-development-method.md`
3. `docs/architecture/skill-architecture.md`
4. `docs/architecture/skill-contracts.md`
5. `docs/architecture/first-batch-skill-design.md` 仅作为已冻结契约的实现设计说明，不得覆盖前四项权威。

若实现暴露权威输入冲突或 Contract 不足，不得通过 `SKILL.md` 静默修正，应先回到对应权威层处理。

## Scope

- 创建 `skills/systematic-debug/SKILL.md`；
- 仅用于 Observed Defect 或 Unexpected Failure；
- 先建立可重复或足够稳定的 Failure Evidence，再进入 Root-cause Investigation；
- 明确 Expected Behavior 必须来自 Applicable Authority，Current Code / Runtime Evidence 只解释 Actual Behavior；
- 明确 Expected vs Actual；
- 基于证据形成可证伪 Hypothesis，并通过针对性观察、检查或实验验证；
- 修复 Root Cause，而不是通过连续 Patch 尝试绕过症状；
- 优先应用满足权威行为所需的 Minimal Root-cause Fix；
- 完成当前 Regression Verification 后才声明 Debug 完成；
- Expected Behavior 未定义或冲突时返回 `clarify-intent` / `specify`；
- 修复要求 Major Architecture Direction 时返回 `technical-plan` / Human Authority；
- 同步 `skills/README.md` 实现状态。

## Out of Scope

- 不替代普通 TDD 中预期的初始 Failing Evidence；
- 不猜测未定义的 Expected Behavior；
- 不把连续随机 Patch 当作 Debug Strategy；
- 不强制特定 Debugger、Profiler、Tracing 或 Observability 工具；
- 不绑定 Bug Tracker；
- 不扩大为整个 Feature 的 Convergence Review；
- 不自动修改 Product Intent / Major Technical Design；
- 不自动 Merge / Push / Release / Deploy；
- 不实现其他 Skill。

## Validation

至少验证以下文本契约行为：

1. 存在可观察 Unexpected Failure 时进入系统化 Debug 路径；
2. 普通 TDD 的预期初始失败不会被误判为 Defect；
3. Debug 首先尝试 Reproduce / 建立稳定 Failure Evidence；
4. Expected Behavior 必须来自权威，不能由 Current Code 自行定义；
5. Expected Behavior 未定义时停止并返回 `clarify-intent` / `specify`；
6. Expected vs Actual 被明确区分；
7. Hypothesis 必须可证伪，并通过针对性证据验证，而不是凭直觉接受；
8. 修复针对 Root Cause，避免连续猜 Patch；
9. Minimal Fix 不扩大 Product Scope；
10. Regression Evidence 必须来自修复后的当前状态；
11. 修复要求 Major Architecture、Product Intent Change 或未授权不可逆动作时停止并升级 / 回上游；
12. 输出包含 Root-cause Statement、Minimal Fix、Regression Evidence，以及必要的 Stage Return / Escalation。

本轮验证属于基于 `SKILL.md` 文本的 context-isolated 行为检查，不表述为 Runtime / 自动化 harness 测试。

## Validation Result

首轮文本契约行为验证完成，12 个场景均通过：

1. Observed Unexpected Failure 会进入 Reproduce-first 调查路径；
2. TDD 预期初始失败被明确排除；
3. 在修复前要求建立可重复或足够稳定的 Failure Evidence；
4. Expected Behavior 只能来自 Applicable Authority；
5. Expected Behavior 未定义或冲突时返回 `clarify-intent` / `specify`；
6. Expected 与 Actual 在调查中独立表达；
7. Hypothesis 必须说明可支持证据和可否定条件，并通过针对性证据验证；
8. 连续猜 Patch 被明确禁止，修复目标是已验证 Root Cause；
9. Minimal Fix 被限制为恢复既有 Expected Behavior，不扩张 Product Scope；
10. Regression Evidence 必须来自修复后的当前状态；
11. Major Architecture、Product Intent Change、不可逆 Data Action、安全 / 隐私或未授权 External Effect 会回上游或升级；
12. 输出结构覆盖 Root-cause Statement、Minimal Fix、Regression Evidence 与必要 Stage Return / Escalation。

静态 Contract 对照与场景检查均未发现需要修改 Method、Skill Architecture 或 Skill Contract 的问题。

## Acceptance Criteria

- `skills/systematic-debug/SKILL.md` 存在且职责单一；
- 实现内容与 reviewed contract 一致；
- 未通过实现新增或改变方法语义；
- Reproduce、Expected vs Actual、Falsifiable Hypothesis、Root-cause Fix、Regression Evidence 的顺序与边界明确；
- 与 TDD 预期失败、`execute-unit`、`specify` / `clarify-intent`、`technical-plan` 的职责边界明确；
- 完成状态必须由当前 Regression Evidence 支持；
- 至少完成一轮 current evidence 支持的文本契约行为验证；
- 实现变更与任何必要 Contract Change 保持独立提交。

## Commit Guidance

如果权威 Contract 无需修改：

```text
feat(skills): 实现 systematic-debug Skill
```

配套状态同步：

```text
docs(skills): 同步 systematic-debug 实现状态
```

如未来形成独立持久化自动化验证，再使用：

```text
test(skills): 验证 systematic-debug Skill 契约行为
```
