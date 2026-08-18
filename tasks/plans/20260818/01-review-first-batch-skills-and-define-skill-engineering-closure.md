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

当前关闭前 Blocking Work Item 为 B1 / B2 / B3，其中 B1、B2 已解决，B3 正在 Runtime Eval。

## Blocking Work Items

### B1 — 统一 Ready-to-Integrate 终点语义

状态：**RESOLVED**。

Method 已明确：

- 普通与复杂 Feature 通过 `converge` 进入 Ready to Integrate；
- Small Safe Change 使用比例化 Lightweight Convergence；
- Standalone Defect 使用 Defect Closure Check；
- Unit Completion 本身不等于 Ready to Integrate；
- 不扩大 `execute-unit`、`systematic-debug` 或 Integration 权限。

重新对照 Architecture / Contract 后，不需要同步修改 Skill Contract 或 Skill Implementation。

### B2 — 标准化 Skill Packaging / Activation Metadata

状态：**RESOLVED**。

第一批 8 个 `SKILL.md` 已增加最小通用 metadata：

- `name`
- `description`

并满足：

- `name` 与目录名一致；
- `description` 同时表达核心职责与触发边界；
- 未引入 vendor-specific tool permissions、slash commands 或 Runtime 私有协议；
- 未通过 metadata 改变既有 Contract 语义。

### B3 — 建立最小 Fresh-context Runtime Eval

状态：**IN PROGRESS — ACTIVATION PASSED / BEHAVIOR ISOLATION RERUN REQUIRED**。

第一轮 Runtime Eval 已建立：

- 16 个 Activation 场景；
- 14 个 Behavior 场景；
- 覆盖 `clarify-intent`、`readiness-check`、`execute-unit`、`converge`；
- `B-EU-01` 使用真实可修改 Python fixture 与当前 unittest evidence；
- 每个 scenario 使用独立 `codex exec --ephemeral --json`。

#### Activation Result

隔离后的 Activation corpus 结果：**16 / 16 PASS**。

每个场景都只加载预期 primary Skill；4 个 near-miss 也全部正确路由：

- `clarify-intent` near-miss → `specify`
- `readiness-check` near-miss → `slice-work`
- `execute-unit` near-miss → `converge`
- `converge` near-miss → `systematic-debug`

未发现 Activation metadata Blocking Finding。

#### Behavior First Full-run Finding

14 个 Behavior 场景全部进程正常退出，输出语义表面上均与 assertions 一致；其中：

- `B-CI-03`：干净有效 PASS；
- `B-EU-01`：干净有效 PASS，实际完成 inspect → failing/current evidence → minimal fix → `python3 -m unittest discover -s tests -v` → 3 tests PASS → evidence-backed Completed → stop；
- 其余 12 个场景在运行中读取了 `evals/behavior/*` 或既有 `evals/results/*`，能够接触 expected behavior、assertions 或历史回答，因此属于 **INFRASTRUCTURE_INVALID / CONTAMINATED**，不能作为 Runtime PASS，也不算 Skill FAIL。

由此暴露的是 Behavior Eval 隔离问题，而不是 Method / Contract / Skill 语义缺陷。

Runner 已修正：

- Activation 和 Behavior 均在仓库外临时 workspace 中执行；
- Runtime 只可见当前 8 个 Skills；
- Behavior 仍使用显式 `$skill-name`；
- `B-EU-01` 额外复制源 fixture，运行后只保存最终 fixture 快照；
- Runtime 不再可读取 `evals/activation/*`、`evals/behavior/*`、历史 `evals/results/*` 或 grading assertions。

B3 下一 Gate：重新运行完整 `--behavior` corpus，并对 14 个隔离 Behavior 结果重新 grading。Activation 不需要重跑。

## Non-blocking Hardening

### N1 — slice-work mechanical cross-cutting change

评估是否需要明确：Vertical 是默认优先方向而非教条；对无法合理独立纵切的 mechanical cross-cutting change，可采用可验证、可回滚、保持系统稳定的 staged slicing。

该项不得削弱 Vertical / Context-fit / Independently Verifiable 的默认原则。

### N2 — systematic-debug feedback-loop-first

评估是否需要强化：当可建立稳定 red-capable feedback loop 时，应在进入修复前优先建立能够持续复现问题的反馈循环。

该项属于 Debug 行为 hardening，不改变 Root-cause-first 主流程。

## Closure Criteria

只有同时满足以下条件，才能正式关闭 Skill Engineering：

1. B1 已解决；
2. B2 已完成；
3. B3 已完成，最小 Fresh-context Runtime Eval 未暴露未解决的 Blocking Contract 问题；
4. 没有新的 Method / Architecture / Contract Blocking Gap；
5. 第一批 8 个 Skill 仍保持小型、可组合，不形成 Super-skill；
6. Integration 继续由 Human Authority / Repository Policy 控制。

满足后再更新阶段状态为 Skill Engineering Closed，并进入后续 Operationalization / Method Validation 工作。

## Work Order

1. B1 — Method / 必要 Contract；**DONE**
2. B2 — Skill Packaging / Implementation；**DONE**
3. B3 — Runtime Eval；**IN PROGRESS**
4. Closure Review；
5. 只有 Closure Review 无 Blocking Finding 后才关闭 Skill Engineering。

## Commit Guidance

B3 Eval 基础设施与结果：

```text
test(skills): 建立第一批 Skill Fresh Runtime Eval
```

如 Runtime Eval 暴露 Skill Implementation 问题，应单独修订对应 Skill，不在 Eval 结果中静默修改 Method / Contract。
