# Skill Runtime Evals

本目录用于第一批核心 Skill 的最小 Fresh Runtime 行为验证。

## 目标

Runtime Eval 分开回答两个问题：

1. **Activation** — Agent 在只看到 Skill `name` / `description` 的情况下，是否在正确场景加载对应 `SKILL.md`，并避免近似场景误触发；
2. **Behavior** — Skill 已被正确加载后，Agent 是否遵守职责边界、Stage Return、Escalation、Context 与 Evidence 规则。

Skill 没有激活与 Skill 激活后执行错误必须分别分类。

## Fresh Context 与隔离规则

每次 Eval Run 必须从干净 Context 开始：

- 不继承上一条 Eval 的 Conversation History；
- 不注入本仓库 Skill Engineering 讨论历史；
- Activation 只能依赖 Runtime 自动发现的 Skill metadata，不预加载目标 `SKILL.md` 正文；
- Behavior 使用显式 `$skill-name`，验证 Skill 被选中后的行为契约；
- Activation 和 Behavior 都在仓库外隔离工作目录中运行；
- Runtime 只可见当前 8 个 Skills，以及场景明确需要的 fixture；
- Runtime 不得读取 `evals/activation/*`、`evals/behavior/*`、历史 `evals/results/*` 或 分级断言；
- Codex 子进程实际 `cwd` / `PWD` 指向隔离 workspace；
- Behavior 场景在需要时显式声明当前工作目录与 prompt 构成本场景全部可用上下文，不允许搜索目录外路径；
- Current Repository / Fixture Context 只按场景最小提供。

如果 Runtime 能读取 expected target、expected behavior、assertions 或历史回答，则该 Run 记为：

```text
INFRASTRUCTURE_INVALID / CONTAMINATED
```

它不是 PASS，也不是 Skill FAIL；必须先修 Eval 隔离，再用新的 Fresh Run 重测。

## 第一轮范围

第一轮覆盖 4 个关键 Skill：

- `clarify-intent`
- `readiness-check`
- `execute-unit`
- `converge`

它们分别覆盖入口歧义、Execute 前 Gate、单 Unit 实施和 Feature 最终收敛。

如果第一轮没有暴露跨 Skill 的 Blocking Pattern，不为了形式完整机械扩展到其余 4 个 Skill。

## Artifact Lifecycle 针对性扩展

PR #28 将 Domain Context、Architecture Context 与 Artifact Lifecycle Closure 提升为 Method / Skill Architecture 职责后，恢复任务确认 Contract / Skill 尚未完整 operationalize。为验证本次受影响行为，只增加 7 个针对性 Behavior 场景：

- `B-CI-04`：Clarify 识别 Domain Authority Candidate，但不自行提升长期权威；
- `B-SP-01`：Specify 验证候选，并在无写入授权时输出 Required Domain Authority Action；
- `B-TP-01`：Architecture Context 需要更新、但不满足 ADR 条件时仍持久化架构状态；
- `B-RC-04`：未闭环的 Domain / Artifact Lifecycle Gap 阻止 `PASS`；
- `B-EU-05`：Execute 发现 Domain Authority 冲突时返回上游；
- `B-SD-01`：Debug 不根据代码 / 测试发明长期领域事实；
- `B-CG-05`：Artifact Lifecycle Gap 阻止 `READY`。

该扩展不改变第一轮历史结果，也不机械扩展 Activation corpus 或为所有 Skill 建设大型 benchmark。

### 针对性扩展结果

2026-08-20 在仓库外隔离 workspace 中完成有效 Fresh Runtime 重跑：

```text
Artifact Lifecycle Behavior: 7 / 7 PASS
```

- `B-CI-04` 正确标记 Domain Authority Candidate，交给 `specify` 验证，未自行持久化长期权威；
- `B-SP-01` 在 Product Owner-only 写入策略下形成 Required Domain Authority Action，未把 Feature Specification 冒充为已闭环的长期权威；
- `B-TP-01` 要求更新现有 `architecture-overview`，同时因不存在需要保留的替代方案或权衡而不创建 ADR，也未把架构状态只留在 Technical Plan；
- `B-RC-04` 将未确定 Producer、Persistence、Update 与 Supersede 的长期客户分级规则判为 Blocking Finding，未输出 `PASS`；
- `B-EU-05` 面对 Specification 与 Domain Authority 冲突时停止实施，不使用代码或测试裁决 14 / 30 天业务事实；
- `B-SD-01` 识别跨功能“活跃客户”定义缺少领域权威，在 Expected Behavior 未确定时不宣称 Debug 完成；
- `B-CG-05` 在实现和测试通过的情况下仍因 Domain Authority / Artifact Lifecycle Gap 输出 `GAPS`，未输出 `READY`。

所有场景均由人工按 assertion 逐项语义分级；进程退出码没有被当作 PASS。Trace 只读取隔离 workspace 中提供的 Skill 与场景材料，未读取本仓库 Eval 定义、历史结果或当前工作目录之外的上下文。

## 验收到验证的闭环针对性扩展

Issue #18 的 Consumer 实验在 `agentic-dev@3e0b99d85d968f138e6eae9bc51ea1b7a710748e` 上证明：执行单元可以具有实现覆盖并完成主路径，但部分验收义务仍缺少计划验证证据和已执行的当前证据；功能整体 `converge` 能正确阻止 `READY`，但发现时机偏晚。

为验证本次受影响行为，只增加 4 个针对性行为场景：

- `B-SW-01`：`slice-work` 为分页、竞争排序和分区导航建立验收责任归属与计划验证证据；
- `B-RC-05`：宽泛完成条件与主路径验证计划不足以通过验证覆盖就绪检查；
- `B-EU-06`：实现存在与单页主路径不能代替分页义务的已执行的当前证据；
- `B-CG-06`：即使执行单元均已完成且存在功能整体计划验证，未执行的证据仍由 `converge` 判为 `GAPS`。

该扩展不新增独立 `verify-evidence` Skill，不要求一条验收义务对应一个测试，也不把 E2E、CI 或特定平台提升为通用方法要求。

### 针对性扩展结果

2026-08-24，使用 `codex-cli 0.148.0` 在仓库外隔离 workspace 中完成有效全新运行时重跑。Skill 内容与 PR #30 的语义基线 `5a894d28bddc4b427af0d3822ae3e2541e730512` 一致。

```text
验收到验证的闭环行为评估：4 / 4 PASS
断言：                          21 / 21 PASS
```

- `B-SW-01`（`6 / 6`）建立同时包含实现覆盖与验证覆盖的规格覆盖视图，为分页、竞争排序和分区导航分别分配执行单元级验证责任，并给出能够证明关键差异的计划验证证据；
- `B-RC-05`（`5 / 5`）拒绝进入执行，明确把验收责任未归属和计划验证覆盖不足列为阻塞性发现，并返回 `slice-work`；
- `B-EU-06`（`5 / 5`）没有把 `LIMIT/OFFSET`、翻页按钮或三条数据的主路径视为分页已验证，在缺少 11 条数据、第二页、`page` 参数和数据切片证据时输出 `Not Completed`；
- `B-CG-06`（`5 / 5`）没有把所有执行单元均已完成、计划验证或排序代码视为当前证据，输出 `GAPS` 并把纯验证缺口返回正常执行路径。

所有断言均由人工读取最终输出与命令轨迹后逐项语义分级。四次运行都从独立临时 workspace 启动，只读取当前场景提供的 Skill 与目录内容，没有读取 Eval 定义、grading assertions、历史结果或仓库外上下文。

`stderr` 中存在 Codex 模型列表刷新超时，但四个进程均以状态码 `0` 完成、JSONL 均包含 `turn.completed` 和完整最终输出，因此该诊断噪声没有影响本轮语义观察。精确模型名没有由当前 JSONL / 运行元数据 暴露，记录为非阻塞运行时观察；本轮行为结论不依赖进程退出码。

## 文件结构

```text
evals/
├── README.md
├── CODEX.md
├── run_codex_evals.py
├── activation/
│   └── core-first-pass.json
├── behavior/
│   ├── clarify-intent.json
│   ├── specify.json
│   ├── technical-plan.json
│   ├── readiness-check.json
│   ├── execute-unit.json
│   ├── systematic-debug.json
│   └── converge.json
└── fixtures/
    └── execute-unit-basic/
```

## Activation Eval

`activation/core-first-pass.json` 使用 realistic user queries，并包含 should-trigger 与 near-miss should-not-trigger 场景。

Runtime 必须能够观察 Skill 是否实际加载。仅根据最终回答风格推断“像是用了某个 Skill”不能作为 Activation Evidence。

单次判定：

- `should_trigger=true`：目标 Skill 实际加载 → PASS；
- `should_trigger=false`：目标 Skill 未误触发，且正确相邻职责被选择 → PASS。

### 最终 Activation 结果

隔离后的第一轮 Activation corpus：

```text
16 / 16 PASS
```

4 个 near-miss 均正确路由：

- `clarify-intent` → `specify`
- `readiness-check` → `slice-work`
- `execute-unit` → `converge`
- `converge` → `systematic-debug`

未发现 Activation metadata Blocking Finding。

## Behavior Eval

Behavior assertion 只检查语义，不要求固定自然语言输出。

每条 assertion 根据实际 Run 输出或 Trace 判定：

- `PASS` — 存在明确证据支持；
- `FAIL` — 输出违反 Contract、缺少必要行为，或在无证据情况下声明完成；
- `NOT_OBSERVABLE` — Runtime 无法提供判断所需信息；
- `INFRASTRUCTURE_INVALID` — Run 被 expected answer、assertions、历史结果或其他越界上下文污染。

`NOT_OBSERVABLE` 与 `INFRASTRUCTURE_INVALID` 都不能算 PASS。

### Runtime hardening 过程

首次 Behavior 全量运行暴露了仓库根目录答案污染；隔离后第二轮又暴露了 launcher 环境路径泄漏。两者都属于 Eval Infrastructure Failure，不算 Skill Failure。

隔离重跑同时发现一个真实 Skill Implementation 问题：

- `B-EU-02` 中 `execute-unit` 面对两个独立 Ready Units 时计划在同一次 invocation 中顺序执行，违反 one-unit / no queue traversal 既有 Contract。

针对性修正：

- `execute-unit` 明确：多 Unit 请求没有唯一 Current Unit 时停止并返回协调层；后续 Unit 必须由新的 invocation / Fresh Execution Context 执行；
- Runner 将 Codex 子进程自身 `cwd` / `PWD` 切到仓库外临时 workspace，并移除可反向定位仓库的 launcher 环境线索；
- 最后针对需要的 Behavior 场景增加中性的上下文边界声明，禁止搜索当前隔离目录之外的路径。

这些修正没有改变 Method / Architecture / Contract。

### 最终 Behavior 结果

当前 Skill 版本的有效 Fresh Runtime evidence：

```text
14 / 14 PASS
```

其中：

- `B-EU-01` 真实修改 fixture，读取 `AGENTS.md` / `unit.md` / 当前实现与测试，执行仓库声明的 unittest verification，3 tests PASS，并基于当前证据停止在 Unit Completion；
- `B-EU-02` 在 hardening 后明确拒绝在同一 `execute-unit` invocation 中顺序执行两个 Units；
- `B-EU-03` 正确将跨 6 个 Units、难回滚的新公共 API contract 返回 `technical-plan`，不自行冻结局部设计；
- `B-EU-04` 不把上周绿色 CI 截图当作当前 Completion Evidence，返回 Not Completed；
- `B-RC-01` 在 Specification / Design / Execution / Governance 均无阻塞时给出只读 PASS；
- `B-CG-02` 以 Specification 为 Product Authority，对实现与测试中的矛盾行为给出 GAPS。

最终有效证据没有读取本仓库 eval corpus、历史结果、其他项目内容或额外 `find-skills` Skill。

## Result 记录

每次 Run 至少记录：

```text
runtime:
model:
skill_version:
scenario_id:
activated_skills:
verdict:
assertion_results:
evidence:
notes:
```

进程退出 `0` 只表示 Runtime 正常结束，不等于 Eval PASS。

## B3 结果

```text
Activation: 16 / 16 PASS
Behavior:   14 / 14 PASS
Blocking Metadata Gap: 0
Blocking Skill Implementation Gap: 0
Blocking Contract Gap: 0
Blocking Method Gap: 0

B3 = COMPLETE
```

第一轮 Runtime Eval 曾发现的一个 `execute-unit` Skill Implementation 缺陷和多轮 Eval Infrastructure 缺陷均已修正，并通过受影响场景的 Fresh Runtime 重测。

B3 完成后进入最终 Skill Engineering Closure Review。
