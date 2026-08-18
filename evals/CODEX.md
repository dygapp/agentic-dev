# 使用 Codex CLI 执行第一轮 Runtime Eval

本指南只用于 B3 第一轮真实 Runtime 执行，不改变 `agentic-dev` 的通用 Skill 架构。

## 1. 使用隔离工作副本

不要在日常开发工作区直接跑会修改 fixture 的 Eval。使用当前 Eval 分支的临时 clone / worktree，并确保每条会修改文件的场景都从干净状态开始。

示例：

```bash
git clone <agentic-dev-repo> agentic-dev-eval
cd agentic-dev-eval
git checkout test/first-batch-skill-runtime-evals
```

## 2. 让 Codex 发现当前仓库的 Skills

本仓库的 Skill 源文件保存在 `skills/`，这是项目自身的源码组织，不等同于某个 Runtime 的安装目录。

Codex Repository Skill Eval 使用临时 `.agents/skills` symlink 暴露当前源文件：

```bash
mkdir -p .agents/skills
for d in skills/*; do
  if [ -f "$d/SKILL.md" ]; then
    ln -s "../../$d" ".agents/skills/$(basename "$d")"
  fi
done
```

Codex 支持扫描 repository `.agents/skills`，并支持 symlinked skill folders。该 `.agents/` 目录只用于临时 Eval，不作为本轮源码变更提交。

建议将临时内容加入本地 exclude，而不是修改仓库 `.gitignore`：

```bash
printf '\n.agents/\nevals/workspace/\nevals/results/\n' >> .git/info/exclude
```

## 3. 确认 Skill Discovery

启动一个新的 Codex CLI 会话，使用 `/skills` 检查 8 个 Skill 是否可见；或者输入 `$` 查看可提及的 Skill。

如果新 metadata 没有出现，重新启动 Codex 会话后再验证。

只有 8 个 Skill 都被 Runtime 发现，Activation Eval 才可开始。

## 4. 推荐：使用薄 Runner

仓库提供 `evals/run_codex_evals.py`，只负责启动独立 Fresh Codex 进程、保存 JSONL / stderr，并为 `B-EU-01` 重建干净 fixture；它**不会自动把进程退出码当成语义 PASS**。

先运行单个 Activation 场景验证环境：

```bash
python3 evals/run_codex_evals.py --activation --scenario A-CI-01
```

再运行单个可写 Behavior 场景：

```bash
python3 evals/run_codex_evals.py --behavior --scenario B-EU-01
```

环境确认后运行第一轮完整 corpus：

```bash
python3 evals/run_codex_evals.py --all
```

结果写入 `evals/results/`。每个 scenario 都由独立的 `codex exec --ephemeral --json` 执行，不使用 `resume`。

Runner 会自动创建 `.agents/skills` symlink；这些 Runtime 临时目录和结果不应提交到本轮源码 PR。

## 5. Activation Eval

输入：`evals/activation/core-first-pass.json`。

规则：

- 每个 query 使用一个全新的 `codex exec`；
- 不在 query 中附加目标 Skill 名；
- 不 resume 前一个 session；
- 默认使用 read-only sandbox；
- 使用 `--ephemeral` 避免把 Eval session rollout 持久化为后续上下文；
- 使用 `--json` 保存 JSONL Trace。

不用 Runner 时的单条示例：

```bash
mkdir -p evals/results/activation

codex exec --ephemeral --json \
  "<query from core-first-pass.json>" \
  > evals/results/activation/A-CI-01.jsonl
```

### Activation Evidence

优先从 JSONL Trace 判断目标 `SKILL.md` 是否实际被读取/加载。

可接受证据包括 Runtime 明确暴露的 Skill invocation / file-read / command trace，能够定位到目标 Skill 的 `SKILL.md`。

不要仅根据最终回答的文风推断“应该用了 Skill”。如果当前 Codex 版本的 JSONL 无法观察 Skill loading，记录：

```text
NOT_OBSERVABLE: activation trace unavailable
```

并将其视为 Eval Infrastructure Gap，而不是 PASS。

第一轮每个 query 先运行 1 次。只有结果不稳定、临界或失败时，才对该 query 重复 3 次并记录 trigger rate；本轮不默认制造 48 次以上重复调用。

## 6. Behavior Eval

输入：

- `evals/behavior/clarify-intent.json`
- `evals/behavior/readiness-check.json`
- `evals/behavior/execute-unit.json`
- `evals/behavior/converge.json`

Behavior Eval 的目的不是再次测试 activation，因此使用显式 Skill invocation，隔离“选错 Skill”和“Skill 执行错误”。

不用 Runner 时，例如：

```bash
codex exec --ephemeral --json \
  '$clarify-intent <prompt from B-CI-01>' \
  > evals/results/behavior/B-CI-01.jsonl
```

每个 scenario 都必须使用新的 `codex exec`，不能使用 `resume`。

### execute-unit 可运行场景

`B-EU-01` 会真实修改文件，因此为每次 Run 创建全新的 fixture 副本：

```bash
rm -rf evals/workspace/B-EU-01
mkdir -p evals/workspace
cp -R evals/fixtures/execute-unit-basic evals/workspace/B-EU-01
```

然后从该目录运行允许 workspace 写入的 Fresh Run：

```bash
mkdir -p evals/results/behavior

codex exec --ephemeral --json --sandbox workspace-write \
  -C evals/workspace/B-EU-01 \
  '$execute-unit 读取当前目录的 AGENTS.md 和 unit.md，只实现 greeting-01，并按仓库规则验证；完成后停止。' \
  > evals/results/behavior/B-EU-01.jsonl
```

注意：`-C` 改变的是 Codex 的工作目录，不改变启动 Codex 的 shell 对 `>` 重定向路径的解析，因此输出路径仍应从当前 shell 工作目录计算。

运行后保留：

- JSONL Trace；
- fixture 最终文件；
- `git diff --no-index` 或等价 diff（如需要）；
- 实际 verification output。

下一次重复 Run 前删除并重新复制 fixture，不能沿用已经修好的工作目录。

## 7. 结果判定

按 `evals/README.md` 的 PASS / FAIL / NOT_OBSERVABLE 规则逐项检查 assertion。

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
  - ...
evidence:
  - <trace / final output / test output reference>
notes:
  - <optional>
```

不要在发现失败后直接修改 Skill 并继续使用同一个 Context。失败先分类，再回到新的实现分支修正；修正后必须使用新的 Fresh Run 重新验证。

## 8. B3 不接受的替代证据

以下内容不计为 Runtime Eval PASS：

- 当前长聊天里对场景的文本推演；
- 开发 Skill 时做过的历史 context-isolated review；
- 没有 Runtime Trace 的“看起来触发了”；
- 在同一个 session 中连续跑多个 scenario；
- Skill 修改后继续沿用修改前的 session；
- `execute-unit` 只描述应该运行什么测试，但没有实际运行当前验证。
