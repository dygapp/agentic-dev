# 使用 Codex CLI 执行第一轮 Runtime Eval

本指南只用于 B3 第一轮真实 Runtime 执行，不改变 `agentic-dev` 的通用 Skill 架构。

## 1. 使用隔离工作副本

不要在日常开发工作区直接跑会修改 fixture 的 Eval。使用当前 Eval 分支的临时 clone / worktree，并确保每条会修改文件的场景都从干净状态开始。

```bash
git clone <agentic-dev-repo> agentic-dev-eval
cd agentic-dev-eval
git checkout test/first-batch-skill-runtime-evals
```

建议将 Runtime 临时内容加入本地 exclude，而不是修改仓库 `.gitignore`：

```bash
printf '\n.agents/\nevals/workspace/\nevals/results/\n' >> .git/info/exclude
```

## 2. Skill Discovery

本仓库的 Skill 源文件保存在 `skills/`，这只是项目源码组织，不等同于 Runtime 安装目录。

Runner 对两类 Eval 使用不同隔离方式：

- **Activation Eval**：在仓库外创建临时目录，只复制当前 8 个 Skill 到该目录的 `.agents/skills/`。Runtime 看不到 `evals/activation/core-first-pass.json`、Behavior assertions 或其他答案文件。
- **Behavior Eval**：在仓库 / fixture 内通过临时 `.agents/skills` symlink 暴露源码 Skill，因为 Behavior 场景使用显式 `$skill-name`，目标不是再次测试 activation。

这些 `.agents/` 内容只用于 Runtime Eval，不提交到源码 PR。

如果希望人工确认 Skill Discovery，可以启动一个新的 Codex CLI 会话，使用 `/skills` 或 `$` 检查 8 个 Skill 是否可见。

## 3. 推荐：使用薄 Runner

仓库提供：

```text
evals/run_codex_evals.py
```

Runner 只负责：

- 每个 scenario 启动独立 `codex exec --ephemeral --json`；
- Activation 使用仓库外隔离 workspace；
- Behavior 使用显式 Skill invocation；
- 为 `B-EU-01` 重建干净 fixture；
- 保存 raw JSONL / stderr / run metadata。

Runner **不会**把进程退出码自动当成语义 PASS。

先运行隔离 Activation smoke test：

```bash
python3 evals/run_codex_evals.py --activation --scenario A-CI-01
```

再运行单个可写 Behavior pilot：

```bash
python3 evals/run_codex_evals.py --behavior --scenario B-EU-01
```

Pilot 与环境确认后运行第一轮完整 corpus：

```bash
python3 evals/run_codex_evals.py --all
```

结果写入：

```text
evals/results/
```

每个 scenario 都是 Fresh `codex exec`，不使用 `resume`。

## 4. Activation Eval

输入：

```text
evals/activation/core-first-pass.json
```

规则：

- query 不显式附加目标 Skill 名；
- 每个 query 使用独立 Fresh Run；
- 使用 `--ephemeral`；
- 保存 `--json` Trace；
- Runtime 工作目录中不得存在 activation corpus、expected target 或 grading assertions；
- 默认只需要 read-only 行为。

### Activation Evidence

优先从 JSONL Trace 判断目标 `SKILL.md` 是否实际被读取 / 加载。

可接受证据例如：

- Runtime 明确输出 Skill invocation；
- file-read / command trace 指向目标 `SKILL.md`；
- 其他能够明确证明目标 Skill 被加载的 Runtime trace。

不要只根据最终回答风格推断“应该用了 Skill”。

如果当前 Codex 版本无法观察 Skill loading，记录：

```text
NOT_OBSERVABLE: activation trace unavailable
```

它属于 Eval Infrastructure Gap，不是 PASS。

第一轮每个 query 先运行 1 次。只有失败、临界或不稳定时，再对该 query 重复 3 次判断 trigger rate。

## 5. Behavior Eval

输入：

- `evals/behavior/clarify-intent.json`
- `evals/behavior/readiness-check.json`
- `evals/behavior/execute-unit.json`
- `evals/behavior/converge.json`

Behavior Eval 使用显式 `$skill-name`，目的是隔离验证：

> Skill 已经被选中后，是否真正遵守职责边界、Stage Return、Escalation 与 Evidence Contract。

每个 scenario 必须使用新的 `codex exec`，不能 `resume`。

## 6. execute-unit 可运行 Fixture

`B-EU-01` 会真实修改：

```text
evals/fixtures/execute-unit-basic/
```

Runner 每次都先重建：

```text
evals/workspace/B-EU-01/
```

fixture 的 Repository verification command 为：

```bash
python3 -m unittest discover -s tests -v
```

运行后至少检查：

- JSONL Trace；
- fixture 最终文件；
- 实际 verification output；
- Completion Claim 是否引用本次 Current Evidence；
- 是否只处理 `greeting-01`；
- 是否停止在 Unit Completion，没有 Merge / Push / Release / Deploy。

下一次 Run 必须重新复制干净 fixture，不能沿用已经修好的工作目录。

## 7. 结果判定

按 `evals/README.md` 的 PASS / FAIL / NOT_OBSERVABLE 规则逐项检查 assertions。

最小结果记录：

```text
runtime: Codex CLI
model: <actual model>
skill_version: <commit SHA>
scenario_id: <id>
activated_skills: <observed set or NOT_OBSERVABLE>
verdict: PASS | FAIL | NOT_OBSERVABLE
assertion_results:
  - <assertion>: PASS | FAIL | NOT_OBSERVABLE
evidence:
  - <trace / final output / test output reference>
notes:
  - <optional>
```

进程退出 `0` 只表示 Codex 进程正常结束，不表示 Eval PASS。

发现失败后不要在同一个 Context 中修改 Skill 并继续测试。先分类失败，修正后使用新的 Fresh Run 重新验证。

## 8. B3 不接受的替代证据

以下内容不能替代 Runtime Eval PASS：

- 当前长聊天中的文本推演；
- Skill 开发阶段的历史 context-isolated review；
- 没有 Runtime Trace 的“看起来触发了”；
- Runtime 可以读取包含 `target_skill` / expected answer 的 eval corpus；
- 同一 session 连续跑多个 scenario；
- Skill 修改后继续沿用旧 session；
- `execute-unit` 只描述应运行测试，但没有实际运行 Current Verification。
