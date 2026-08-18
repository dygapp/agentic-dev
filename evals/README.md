# Skill Runtime Evals

本目录用于第一批核心 Skill 的最小 Runtime 行为验证。

## 目标

Runtime Eval 只回答两个不同问题：

1. **Activation** — Agent 在只看到 Skill `name` / `description` 的情况下，是否会在正确场景加载对应 `SKILL.md`，并避免近似场景误触发；
2. **Behavior** — Skill 已正确加载后，Agent 是否遵守其职责边界、Stage Return、Escalation、Context 与 Evidence 规则。

这两类问题必须分开记录。Skill 没有激活与 Skill 激活后执行错误，不得合并成同一类失败。

## Fresh Context 与隔离规则

每次 Eval Run 必须从干净 Context 开始：

- 不继承上一次 Eval 的 Conversation History；
- 不把本仓库 Skill Engineering 讨论历史注入 Run；
- Activation Eval 只能依赖 Runtime 自动发现的 Skill metadata，不预先把目标 `SKILL.md` 正文塞入 Prompt；
- Behavior Eval 使用显式 `$skill-name`，验证 Skill 被选中后的行为契约；
- Activation 和 Behavior 都必须在仓库外隔离 workspace 中运行；
- Runtime 只可见当前 8 个 Skills，以及场景明确需要的 fixture；
- Runtime 不得读取 `evals/activation/*`、`evals/behavior/*`、历史 `evals/results/*` 或 grading assertions；
- Codex 子进程的实际 `cwd` / `PWD` 也必须指向隔离 workspace，不能只依赖 `-C`；
- Current Repository / Fixture Context 只按场景最小提供。

如果 Runtime 能读取 expected target、expected behavior、assertions 或历史回答，则该 Run 记为：

```text
INFRASTRUCTURE_INVALID / CONTAMINATED
```

它不是 PASS，也不是 Skill FAIL；必须先修 Eval 隔离，再使用新的 Fresh Run 重测。

没有 Fresh Context 的文本推演不计入 B3 Runtime Evidence。

## 第一轮范围

第一轮只覆盖 4 个关键 Skill：

- `clarify-intent`
- `readiness-check`
- `execute-unit`
- `converge`

它们分别覆盖入口歧义、Execute 前 Gate、单 Unit 实施与 Feature 最终收敛，是第一批调用链中最容易暴露 activation、职责边界、Stage Return 与 Evidence 问题的关键节点。

如果第一轮暴露跨 Skill 共性问题，修正后再决定是否扩展到其余 4 个；如果未暴露 Blocking Pattern，不为了形式完整机械扩大测试规模。

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

`activation/core-first-pass.json` 使用 realistic user queries，并显式包含 should-trigger 与 near-miss should-not-trigger 场景。

Runtime 必须能够观察 Skill 是否实际加载。仅根据最终回答“看起来像用了某个 Skill”不能作为 Activation Evidence。

第一轮每个 query 至少运行 1 次，用于发现明显边界问题。若结果不稳定、临界或与预期不符，再对该 query 运行 3 次并记录 trigger rate。

单次判定：

- `should_trigger=true`：目标 Skill 实际加载 → PASS；
- `should_trigger=false`：near-miss Skill 未加载，且正确相邻职责被选择 → PASS。

如果 Runtime 同时加载多个 Skill，应记录完整 activation set，并检查是否存在明显越界激活。

### 当前 Activation 结果

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

每个 Behavior 文件包含少量 Fresh-context 场景，每项包含：

- `prompt`
- `expected_behavior`
- `assertions`

Behavior Eval 不要求固定自然语言输出。Assertions 检查语义行为，不检查脆弱的固定措辞。

每条 assertion 必须根据实际 Run 输出或 Trace 给出：

- `PASS` — 存在明确证据支持；
- `FAIL` — 输出与 Contract 相反、缺少必要行为，或在无证据情况下声明完成；
- `NOT_OBSERVABLE` — Runtime 无法提供判断所需信息；
- `INFRASTRUCTURE_INVALID` — Run 被 expected answer / assertions / 历史结果污染，无法作为独立行为证据。

`NOT_OBSERVABLE` 或 `INFRASTRUCTURE_INVALID` 不能被当作 PASS。

### 首次全量 Behavior 结果

14 个 Behavior Codex 进程全部正常退出，最终输出表面上均符合场景 assertions；严格污染检查得到：

- `B-CI-03`：clean PASS
- `B-EU-01`：clean PASS
- 其余 12 个：`INFRASTRUCTURE_INVALID / CONTAMINATED`

污染来源是 Runtime 从仓库根目录运行时读取了 `evals/behavior/*` 或历史 `evals/results/*`。这属于 Eval Infrastructure Failure，不是 Skill Failure。

### 隔离 Behavior 重跑结果

第二次完整 Behavior rerun：

- 14 / 14 Codex 进程正常退出；
- 11 个场景没有访问本地仓库或 eval corpus；
- 其中 10 个 clean PASS；
- `B-EU-02` 为真实 Skill Behavior FAIL：面对两个独立 Ready Units，Runtime 计划在同一次 `execute-unit` invocation 中顺序执行 U-10、U-11，违反 one-unit / no queue traversal 边界；
- `B-CG-02`、`B-EU-03`、`B-RC-01` 仍通过 launcher 的进程环境线索回读本地仓库，因此继续判为 `INFRASTRUCTURE_INVALID / CONTAMINATED`。

已采取针对性修正：

- `execute-unit` 明确多 Unit 请求没有唯一 Current Unit 时必须停止并返回协调层；后续 Unit 必须由新的 invocation / Fresh Execution Context 执行；
- Runner 将 Codex 子进程自身 `cwd` 与 `PWD` 切到仓库外临时 workspace，并移除 `OLDPWD` 与常见 `GIT_*` 环境线索。

下一步只需重跑：

- `B-EU-02`
- `B-CG-02`
- `B-EU-03`
- `B-RC-01`

其他 Activation 与 clean Behavior evidence 不需要重复运行。

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

如 Runtime 能提供 token / duration，可附带记录，但它们不是本轮 B3 的关闭条件。

进程退出 `0` 只表示 Runtime 正常结束，不等于 Eval PASS。

## B3 关闭条件

B3 只有在以下条件同时满足时才可标记完成：

1. 4 个关键 Skill 都有实际 Fresh Runtime Run；
2. Activation 和 Behavior 分别有可观察、未污染结果；
3. 没有未解决的 Blocking Contract / Method Gap；
4. 失败已分类为 Metadata / Skill Implementation / Contract / Method / Runtime Infrastructure；
5. 对 Critical Evidence、Stage Return、Escalation 或职责边界的失败不能通过“模型大概理解了”豁免；
6. Eval 结果来自当前 Skill 版本，不使用 B2 之前的历史输出；
7. 用于 PASS 的 Runtime evidence 不包含 expected answer / assertions / 历史结果污染。

完成 B3 后再进行 Skill Engineering Closure Review。
