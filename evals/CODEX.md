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

Runner 对两类 Eval 都使用仓库外临时 workspace：

- **Activation Eval**：只复制当前 8 个 Skill 到临时 `.agents/skills/`，Runtime 看不到 `evals/activation/core-first-pass.json`、Behavior assertions 或其他答案文件；
- **Behavior Eval**：同样只复制当前 8 个 Skill，并使用显式 `$skill-name`。`B-EU-01` 额外复制真实 fixture，运行结束后再保存最终 fixture 快照。

此外，Runner 启动 Codex 子进程时，会把进程级 `cwd` 与 `PWD` 一并切到临时 workspace，并移除 `OLDPWD` 与常见 `GIT_*` 环境线索。只使用 `-C` 而让 launcher 自身仍停留在仓库根目录，会留下反向定位本地仓库的环境线索，不满足本轮严格隔离要求。

这些 Runtime 临时内容不提交到源码 PR。

如果希望人工确认 Skill Discovery，可以启动一个新的 Codex CLI 会话，使用 `/skills` 或 `$` 检查 8 个 Skill 是否可见。

## 3. 推荐：使用薄 Runner

仓库提供：

```text
evals/run_codex_evals.py
```

Runner 只负责：

- 每个 scenario 启动独立 `codex exec --ephemeral --json`；
- Activation / Behavior 使用仓库外隔离 workspace；
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

Behavior trace 如果读取了仓库中的 `evals/behavior/*`、`evals/results/*`、expected behavior 或 assertions，应判为 **INFRASTRUCTURE_INVALID / CONTAMINATED**，不能因为最终回答正确就算 PASS。

## 6. execute-unit 可运行 Fixture

`B-EU-01` 会真实修改：

```text
evals/fixtures/execute-unit-basic/
```

Runner 每次都从源 fixture 复制到独立临时 workspace，运行后把最终快照保存到：

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

## 7. Pilot 与隔离发现

第一轮 Pilot 证明：

- Codex JSONL 可以直接观察 implicit Skill activation；
- `execute-unit` 可以在 Fresh Runtime 中真实修改 fixture、执行当前验证并基于证据停止。

后续全量运行又暴露两个 Eval Infrastructure 风险：

1. 从仓库根目录运行 Activation 时，Agent 可能读到 `target_skill` / expected reason；
2. 即使 `-C` 指向仓库外临时目录，如果启动 Codex 的父进程仍以仓库根目录作为 `cwd/PWD`，少数 Run 仍可能沿环境线索反向搜索本地仓库。

因此当前 Runner 同时隔离：

- Runtime workspace 内容；
- Codex 子进程实际 `cwd`；
- `PWD` / `OLDPWD`；
- 常见 `GIT_*` 环境线索。

## 8. 结果判定

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

## 9. B3 不接受的替代证据

以下内容不能替代 Runtime Eval PASS：

- 当前长聊天中的文本推演；
- Skill 开发阶段的历史 context-isolated review；
- 没有 Runtime Trace 的“看起来触发了”；
- Runtime 可以读取包含 `target_skill` / expected answer 的 eval corpus；
- Runtime 通过 launcher 的 `cwd/PWD` 等环境线索回读到本地仓库中的 eval corpus；
- 同一 session 连续跑多个 scenario；
- Skill 修改后继续沿用旧 session；
- `execute-unit` 只描述应运行测试，但没有实际运行 Current Verification。
