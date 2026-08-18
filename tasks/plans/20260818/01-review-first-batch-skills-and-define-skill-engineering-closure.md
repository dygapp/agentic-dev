# Review First-batch Skills and Define Skill Engineering Closure

## Goal

对第一批 8 个核心 Skill 进行整体收口复核，确认调用链、职责边界、Stage Return、Context、Escalation 与 Evidence 是否形成一致且可执行的体系，并定义关闭 Skill Engineering 前必须完成的最小 Hardening 工作。

本任务不预设 Skill Engineering 可以立即关闭。复核结论必须由当前 Method、Architecture、Contract、Skill Implementation 与 Runtime Evidence 支持。

## Authority Inputs

本轮语义判断严格按以下权威顺序进行：

1. `AGENTS.md`
2. `docs/method/ai-development-method.md`
3. `docs/architecture/skill-architecture.md`
4. `docs/architecture/skill-contracts.md`

`docs/architecture/first-batch-skill-design.md` 只作为已冻结契约的实现设计参考，不增加或覆盖前四项语义。

外部项目与外部 Skill Specification 只能作为实现成熟度、Packaging 与工程工艺参照，不作为本仓库 Method / Contract Authority。

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
- Stage Return 是否把 Requirement、Design、Execution、Defect 与 Convergence Gap 路由到正确职责层；
- Authority First、Progressive Disclosure、Fresh Context 与 Conversation History 非权威规则是否一致；
- Human Escalation 是否统一遵循 Authority / Impact / Reversibility；
- Verification-before-claim 与 Current Evidence 语义是否一致；
- `Ready to Integrate` 是否保持在 Integration 之前，并且没有被单个 Unit Completion、Ticket 状态或历史证据替代；
- 是否意外形成 Super-skill、Runtime / Tool / Framework 绑定或自动 Integration 行为。

## Review Result

### Current Verdict

```text
Skill Engineering Closure Verdict:
READY FOR FINAL CLOSURE REVIEW
```

第一批 8 个 Skill 的主体语义架构已经收敛：主调用链闭合、职责边界清楚，没有发现需要重新设计第一批 Skill 列表或新增 Super-skill 的结构性问题。

关闭前 Blocking Work Item B1 / B2 / B3 已全部解决。当前不再存在已知 Blocking Metadata / Skill Implementation / Contract / Method Gap。

正式关闭 Skill Engineering 前，只剩最后一步：将本 PR 的 B3 evidence 与 hardening 集成到 `master` 后，基于最终权威状态执行一次 Closure Review。

## Blocking Work Items

### B1 — 统一 Ready-to-Integrate 终点语义

状态：**RESOLVED**。

Method 已明确：

- 普通与复杂 Feature 通过 `converge` 进入 Ready to Integrate；
- Small Safe Change 使用比例化 Lightweight Convergence；
- Standalone Defect 使用 Defect Closure Check；
- Unit Completion 本身不等于 Ready to Integrate；
- 不扩大 `execute-unit`、`systematic-debug` 或 Integration 权限。

重新对照 Architecture / Contract 后，不需要同步修改 Skill Contract。

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

状态：**RESOLVED / COMPLETE**。

第一轮 Runtime Eval 建立并实际执行：

- 16 个 Activation 场景；
- 14 个 Behavior 场景；
- 覆盖 `clarify-intent`、`readiness-check`、`execute-unit`、`converge`；
- `B-EU-01` 使用真实可修改 Python fixture 与当前 unittest evidence；
- 每个 scenario 使用独立 `codex exec --ephemeral --json`。

#### Activation Result

最终结果：**16 / 16 PASS**。

4 个 near-miss 正确路由：

- `clarify-intent` near-miss → `specify`
- `readiness-check` near-miss → `slice-work`
- `execute-unit` near-miss → `converge`
- `converge` near-miss → `systematic-debug`

未发现 Activation metadata Blocking Finding。

#### Behavior Result

最终有效 Fresh Runtime evidence：**14 / 14 PASS**。

Runtime hardening 过程中曾发现两类问题：

1. **Eval Infrastructure contamination** — 初始 Behavior Run 可以读取仓库内 eval corpus；后续还发现 launcher `cwd/PWD` 与文件系统搜索可能泄漏仓库或其他项目上下文。Runner 已逐步改为仓库外隔离 workspace、真实子进程 `cwd/PWD` 隔离、移除 launcher 环境路径线索，并对最终必要场景显式限制只使用当前工作目录与 prompt。
2. **真实 Skill Implementation Finding** — `B-EU-02` 暴露 `execute-unit` 面对两个独立 Ready Units 时可能计划在同一次 invocation 中顺序执行。Skill 已强化既有 one-unit Contract：没有唯一 Current Unit 时停止并返回协调层；后续 Unit 必须使用新的 invocation / Fresh Execution Context。

受影响场景均使用修改后的当前 Skill / Runner 重新执行并通过。

最终关键证据包括：

- `B-EU-01`：真实 inspect → minimal fix → 当前 unittest verification → 3 tests PASS → evidence-backed Completed → stop；
- `B-EU-02`：拒绝在同一次 invocation 中顺序执行两个 Units；
- `B-EU-03`：跨 6 Units、难回滚的公共 API contract 正确返回 `technical-plan`；
- `B-EU-04`：历史绿色 CI 截图不能替代当前 Completion Evidence，返回 Not Completed；
- `B-RC-01`：Specification / Design / Execution / Governance 均满足时只读 PASS；
- `B-CG-02`：Specification 继续作为 Product Authority，矛盾实现与测试不能反向修改 Requirement。

最终 PASS evidence 没有读取 expected behavior / assertions / 历史 eval 结果、其他项目内容或额外 `find-skills` Skill。

B3 最终矩阵：

```text
Activation: 16 / 16 PASS
Behavior:   14 / 14 PASS
Blocking Metadata Gap: 0
Blocking Skill Implementation Gap: 0
Blocking Contract Gap: 0
Blocking Method Gap: 0
```

## Non-blocking Hardening

### N1 — slice-work mechanical cross-cutting change

评估是否需要明确：Vertical 是默认优先方向而非教条；对无法合理独立纵切的 mechanical cross-cutting change，可采用可验证、可回滚、保持系统稳定的 staged slicing。

该项不得削弱 Vertical / Context-fit / Independently Verifiable 的默认原则。

### N2 — systematic-debug feedback-loop-first

评估是否需要强化：当可建立稳定 red-capable feedback loop 时，应在进入修复前优先建立能够持续复现问题的反馈循环。

该项属于 Debug 行为 hardening，不改变 Root-cause-first 主流程。

N1 / N2 当前均为 Non-blocking，不阻止 Skill Engineering Closure；只有后续真实使用证据表明需要时再进入独立变更。

## Closure Criteria

关闭 Skill Engineering 需要同时满足：

1. B1 已解决；**SATISFIED**
2. B2 已完成；**SATISFIED**
3. B3 已完成，Fresh-context Runtime Eval 无未解决 Blocking Contract 问题；**SATISFIED**
4. 没有新的 Method / Architecture / Contract Blocking Gap；**SATISFIED**
5. 第一批 8 个 Skill 保持小型、可组合，不形成 Super-skill；**SATISFIED**
6. Integration 继续由 Human Authority / Repository Policy 控制；**SATISFIED**

当前所有实质 Closure Criteria 已满足。为保证最终判定基于 `master` 权威状态，正式 `Skill Engineering = CLOSED` 在 PR #12 集成后执行一次 Final Closure Review 再落地。

## Work Order

1. B1 — Method / 必要 Contract；**DONE**
2. B2 — Skill Packaging / Implementation；**DONE**
3. B3 — Runtime Eval；**DONE**
4. PR #12 Review / Integration；**READY**
5. Final Skill Engineering Closure Review；**PENDING AFTER INTEGRATION**
6. 无 Blocking Finding 后进入 `Skill Operationalization & Method Validation`。

## Commit Guidance

PR #12 建议最终 squash commit：

```text
test(skills): 建立第一批 Skill Fresh Runtime Eval
```

Runtime Eval 暴露的 Skill Implementation hardening 已在本 PR 内显式记录，没有静默修改 Method / Contract。