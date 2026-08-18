# Skill Runtime Evals

本目录用于第一批核心 Skill 的最小 Runtime 行为验证。

## 目标

Runtime Eval 只回答两个不同问题：

1. **Activation** — Agent 在只看到 Skill `name` / `description` 的情况下，是否会在正确场景加载对应 `SKILL.md`，并避免近似场景误触发；
2. **Behavior** — Skill 已正确加载后，Agent 是否遵守其职责边界、Stage Return、Escalation、Context 与 Evidence 规则。

这两类问题必须分开记录。Skill 没有激活与 Skill 激活后执行错误，不得合并成同一类失败。

## Fresh Context 规则

每次 Eval Run 必须从干净 Context 开始：

- 不继承上一次 Eval 的 Conversation History；
- 不把本仓库 Skill Engineering 讨论历史注入 Run；
- Activation Eval 只能依赖 Runtime 自动发现的 Skill metadata，不应预先把目标 `SKILL.md` 正文塞入 Prompt；
- Behavior Eval 应让 Runtime 使用目标 Skill，并加载该 Skill 正文，但不加载无关 Skill 正文；
- Current Repository / Fixture Context 只按场景最小提供。

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
├── activation/
│   └── core-first-pass.json
└── behavior/
    ├── clarify-intent.json
    ├── readiness-check.json
    ├── execute-unit.json
    └── converge.json
```

## Activation Eval

`activation/core-first-pass.json` 使用 realistic user queries，并显式包含 should-trigger 与 near-miss should-not-trigger 场景。

Runtime 必须能够观察 Skill 是否实际加载。仅根据最终回答“看起来像用了某个 Skill”不能作为 Activation Evidence。

第一轮每个 query 至少运行 1 次，用于发现明显边界问题。若结果不稳定、临界或与预期不符，再对该 query 运行 3 次并记录 trigger rate。

单次判定：

- `should_trigger=true`：目标 Skill 实际加载 → PASS；
- `should_trigger=false`：near-miss Skill 未加载 → PASS。

如果 Runtime 同时加载多个 Skill，应记录完整 activation set，并检查是否存在明显越界激活。

## Behavior Eval

每个 Behavior 文件只包含少量 Fresh-context 场景，每项包含：

- `prompt`
- `expected_behavior`
- `assertions`

Behavior Eval 不要求固定自然语言输出。Assertions 检查语义行为，不检查脆弱的固定措辞。

每条 assertion 必须根据实际 Run 输出或 Trace 给出：

- `PASS` — 存在明确证据支持；
- `FAIL` — 输出与 Contract 相反、缺少必要行为，或在无证据情况下声明完成；
- `NOT_OBSERVABLE` — Runtime 无法提供判断所需信息。

`NOT_OBSERVABLE` 不能被当作 PASS；如果它阻碍关键 Contract 验证，应记录为 Eval Infrastructure Gap。

## Result 记录

第一轮不建设复杂 benchmark harness。每次 Run 至少记录：

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

## B3 关闭条件

B3 只有在以下条件同时满足时才可标记完成：

1. 4 个关键 Skill 都有至少一个实际 Fresh Runtime Run；
2. Activation 和 Behavior 分别有可观察结果；
3. 没有未解决的 Blocking Contract / Method Gap；
4. 失败已分类为 Metadata / Skill Implementation / Contract / Method / Runtime Infrastructure；
5. 对 Critical Evidence、Stage Return、Escalation 或职责边界的失败不能通过“模型大概理解了”豁免；
6. Eval 结果来自当前 Skill 版本，不使用 B2 之前的历史输出。

完成 B3 后再进行 Skill Engineering Closure Review。
