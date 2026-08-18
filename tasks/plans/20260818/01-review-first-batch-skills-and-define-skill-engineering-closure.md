# Review First-batch Skills and Define Skill Engineering Closure

## Goal

对第一批 8 个核心 Skill 进行整体收口复核，确认调用链、职责边界、Stage Return、Context、Escalation 与 Evidence 是否形成一致且可执行的体系，并定义关闭 Skill Engineering 前必须完成的最小 Hardening 工作。

本任务不预设 Skill Engineering 可以立即关闭。复核结论必须由当前 Method、Architecture、Contract 与已实现 Skill 状态支持。

## Authority Inputs

本轮语义判断严格按以下权威顺序进行：

1. `AGENTS.md`
2. `docs/method/ai-development-method.md`
3. `docs/architecture/skill-architecture.md`
4. `docs/architecture/skill-contracts.md`

`docs/architecture/first-batch-skill-design.md` 只作为已冻结契约的实现设计参考，不增加或覆盖前四项语义。

外部项目仅可作为实现成熟度与工程工艺参照，不作为本仓库 Method / Contract Authority。

## Review Scope

复核以下 8 个 Skill：

1. `clarify-intent`
2. `specify`
3. `technical-plan`
4. `slice-work`
5. `readiness-check`
6. `execute-unit`
7. `systematic-debug`
8. `converge`

重点检查：

- Feature 主调用链是否闭合；
- Workflow / Investigation 职责是否重叠或存在断层；
- Stage Return 是否能把 Requirement、Design、Execution、Defect 与 Convergence Gap 路由到正确职责层；
- Authority First、Progressive Disclosure、Fresh Context 与 Conversation History 非权威规则是否一致；
- Human Escalation 是否统一遵循 Authority / Impact / Reversibility；
- Verification-before-claim 与 Current Evidence 语义是否一致；
- `Ready to Integrate` 是否保持在 Integration 之前，并且没有被单个 Unit Completion、Ticket 状态或历史证据替代；
- 是否意外形成 Super-skill、Runtime / Tool / Framework 绑定或自动 Integration 行为。

## Review Result

### Overall Verdict

```text
Skill Engineering Closure Verdict:
HARDENING REQUIRED
```

第一批 8 个 Skill 的主体语义架构已经收敛：主调用链闭合，职责边界清楚，没有发现需要重新设计第一批 Skill 列表或新增 Super-skill 的结构性问题。

当前仍存在 3 个关闭前 Blocking Work Item，以及 2 个 Non-blocking Hardening Item。

## Blocking Work Items

### B1 — 统一 Ready-to-Integrate 终点语义

当前 Method 的普通 Feature 路径由 `converge` 进入 `Ready to Integrate`，但比例化流程中仍存在终点所有权不够明确的问题：

- Small Safe Change 当前表达为 `Execute → Verify → Ready to Integrate`；
- `execute-unit` 同时明确 Unit Completion 不等于 Feature Converged，也不等于 Ready to Integrate；
- Standalone Defect Workflow 以 Regression Verification / Review 结束，但没有显式定义何时进入 Ready to Integrate。

需要先在 Method 层明确：

- Convergence 是完成语义要求，但执行强度应与工作规模成比例；
- Small Safe Change 如何满足轻量 Convergence；
- Standalone Defect 在不进入完整 Feature Workflow 时，何种最终证据足以进入 Ready to Integrate；
- 不通过扩大 `execute-unit` 或 `systematic-debug` 职责来解决该问题。

如 Method 修改影响 Skill Contract，应单独同步 Contract；实现层修改不得先于权威语义修正。

### B2 — 标准化 Skill Packaging / Activation Metadata

第一批 8 个 `SKILL.md` 当前缺少通用 Skill discoverability 所需的最小 metadata。

目标：

- 为每个 Skill 增加最小 `name` + `description` metadata；
- `description` 同时表达核心职责与触发边界，支持可靠 activation；
- 不引入 vendor-specific tool permissions、slash commands 或 Runtime 私有协议；
- 不通过 metadata 改变既有 Contract 语义。

### B3 — 建立最小 Fresh-context Runtime Eval

当前首轮验证属于 Contract-level / context-isolated 文本行为检查，尚不能等同于真实 Runtime 行为验证。

目标：

- 先覆盖 `clarify-intent`、`readiness-check`、`execute-unit`、`converge` 四个关键 Skill；
- 每个 Skill 使用少量 Fresh-context 场景检查触发、拒绝触发、职责边界、Stage Return、Escalation 与 Evidence；
- 如果暴露共性问题，再扩展到其余 4 个 Skill；
- 不把本轮 Runtime Eval 扩张为大型测试平台建设。

## Non-blocking Hardening

### N1 — slice-work mechanical cross-cutting change

评估是否需要明确：Vertical 是默认优先方向而非教条；对无法合理独立纵切的 mechanical cross-cutting change，可采用可验证、可回滚、保持系统稳定的 staged slicing。

该项不得削弱 Vertical / Context-fit / Independently Verifiable 的默认原则。

### N2 — systematic-debug feedback-loop-first

评估是否需要强化：当可建立稳定 red-capable feedback loop 时，应在进入修复前优先建立能够持续复现问题的反馈循环。

该项属于 Debug 行为 hardening，不改变 Root-cause-first 主流程。

## Closure Criteria

只有同时满足以下条件，才能正式关闭 Skill Engineering：

1. B1 已解决，Small Safe Change、普通 Feature 与 Standalone Defect 的 Ready-to-Integrate 终点语义一致；
2. B2 已完成，8 个 Skill 具备最小标准 Packaging / Activation Metadata；
3. B3 已完成，最小 Fresh-context Runtime Eval 未暴露未解决的 Blocking Contract 问题；
4. 没有新的 Method / Architecture / Contract Blocking Gap；
5. 第一批 8 个 Skill 仍保持小型、可组合，不形成 Super-skill；
6. Integration 继续由 Human Authority / Repository Policy 控制。

满足后再更新阶段状态为 Skill Engineering Closed，并进入后续 Operationalization / Method Validation 工作。

## Work Order

按权威层级执行：

1. B1 — Method / 必要 Contract；
2. B2 — Skill Packaging / Implementation；
3. B3 — Runtime Eval；
4. Closure Review；
5. 只有 Closure Review 无 Blocking Finding 后才关闭 Skill Engineering。

不要在 B1 未稳定前通过 Skill Implementation 绕过语义问题。

## Commit Guidance

本任务记录：

```text
docs(tasks): 记录第一批 Skill 收口复核结论
```

B1 如修改 Method：

```text
docs(method): 统一 Ready to Integrate 收敛语义
```

若随后必须同步 Contract，保持独立提交：

```text
docs(contracts): 同步比例化收敛契约
```
