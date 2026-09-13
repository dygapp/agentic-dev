---
id: eval:codex-runtime
type: eval-guide
status: active
---

# 使用 Codex CLI 执行运行时评估

本文只说明如何隔离执行 `agentic-dev` Evals；不改变 Method、Skill、Rule 或 Rule Discovery contract。

## 1. 隔离运行

不要在日常开发工作区直接运行会修改 fixture 的评估。使用临时 clone / worktree / isolated workspace，并保证每个会修改文件的场景从干净状态开始。

Runtime 不得读取：

- grading assertions / expected behavior；
- 历史 results；
- 与当前场景无关的仓库文件；
- 日常会话上下文。

如发生污染，该运行记为 infrastructure invalid，而不是 PASS / FAIL。

## 2. Skill / capability / discovery runner

主运行器：

```text
evals/run_codex_evals.py
```

历史 Skill / capability 命令：

```bash
python3 evals/run_codex_evals.py --activation --scenario A-CI-01
python3 evals/run_codex_evals.py --behavior --scenario B-EU-01
python3 evals/run_codex_evals.py --capability --scenario C-VTS-01
```

V4 Rule Discovery 判别评估：

```bash
python3 evals/run_codex_evals.py --discovery
python3 evals/run_codex_evals.py --discovery --scenario D-V4-GEN-01
```

`--discovery` 每个场景只复制当前 runtime entry、Rule Discovery Tool、current Rules、current Skills 与场景输入；corpus、expected behavior、assertions 和历史结果不进入 workspace。

## 3. Governance runner

```text
evals/run_governance_evals.py
```

只保留仍有 current Rule / Authority owner 的治理回归场景。语料迁移前先检查其是否仍对应 V4 current semantics。

## 4. Execute fixture

`B-EU-01` 使用：

`evals/fixtures/execute-unit-basic/`

每次运行必须复制到独立临时目录；不得沿用已经修改的 workspace。至少检查最终文件、实际验证输出、completion claim 与当前证据，并确认没有越过 Unit 边界执行 merge / release / deploy。

## 5. Rule Discovery / scaling

V4-04 以后，Rule Discovery 的确定性 schema / matching / fail-closed 优先使用普通自动化测试，不需要用 LLM 证明确定性代码行为。

V4-06 的 LLM 评估验证真正需要模型参与的部分：

- 从当前任务事实提取 task signals；
- 候选 Rule 正文的最终语义适用性；
- generation / verification / mixed task 行为；
- responsibility 变化时重新发现；
- ambiguity / invalid metadata 的安全停止；
- Skill / Rule 与 Consumer-local 边界。

V4-07 再使用 20 / 100 / 500 rules 的等价任务验证 discovery context scaling；不得在 V4-06 用场景数量代替 token-scaling 证据。

## 6. 结果判定

进程退出码 `0` 只表示 Codex 进程正常结束，不表示语义通过。

最小结果至少记录：

```text
runtime / model（可观察时）
target commit
scenario id
verdict
assertion verdicts
evidence references
infrastructure notes
```

Discovery 场景还应检查 JSONL trace 是否真实执行 local discovery、读取哪些 candidate paths、是否跨责任重新发现，以及是否出现全量 Rule scan / upstream fallback。

没有运行轨迹时不能仅凭最终回答风格推断 Skill 或 Rule 被激活；Skill / Rule / Discovery contract 改变后不得沿用受影响的历史运行结果。