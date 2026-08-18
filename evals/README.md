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
- Activation 和 Behavior 都在仓库外隔离 workspace 中运行；
- Runtime 只可见当前 8 个 Skills，以及场景明确需要的 fixture；
- Runtime 不得读取 `evals/activation/*`、`evals/behavior/*`、历史 `evals/results/*` 或 grading assertions；
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
│   ├── readiness-check.json
│   ├── execute-unit.json
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