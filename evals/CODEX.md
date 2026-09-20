---
id: eval:codex-runtime
type: eval-guide
status: active
distribution: source-only
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

## 2. Skill / discovery 运行器

主运行器：

```text
evals/run_codex_evals.py
```

Skill regression：

```bash
python3 evals/run_codex_evals.py --activation --scenario A-CI-01
python3 evals/run_codex_evals.py --behavior --scenario B-EU-01
```

V4 Rule Discovery 判别评估：

```bash
python3 evals/run_codex_evals.py --discovery
python3 evals/run_codex_evals.py --discovery --scenario D-V4-GEN-01
```

`--discovery` 的 agentic-dev 场景复制当前 ordinary Bootstrap 的最小依赖闭包：`AGENTS.md`、Project Roadmap、Project Capability Profile；场景已经选择 Method 时再复制该 Method，并加 Rule Discovery Tool、current Rules、current Skills 与场景输入。首次 communication bootstrap 场景可以在 Method 选择前验证输出类 Rule 的激活，因此不强制伪造 selected Method。Human README 与 Method Architecture 不再固定复制；只有场景责任明确需要时才应作为额外输入。Consumer-local 场景仍只使用它自己的 local Authority。corpus、expected behavior、assertions 和历史结果不进入 workspace。

V4 已删除 monolithic Technology Profile runtime owner；旧 `--capability` / Profile eval 入口不属于 current baseline。技术行为通过 current technology Rules 与 V4 discovery corpus 验证。

## 3. 治理运行器

```text
evals/run_governance_evals.py
```

只保留仍有 current Rule / Authority owner 的治理回归场景。语料迁移前先检查其是否仍对应当前语义。

## 4. Execute 测试夹具

`B-EU-01` 使用：

`evals/fixtures/execute-unit-basic/`

每次运行必须复制到独立临时目录；不得沿用已经修改的 workspace。至少检查最终文件、实际验证输出、completion claim 与当前证据，并确认没有越过 Unit 边界执行 merge / release / deploy。

## 5. Rule Discovery / 扩展验证

Rule Discovery 的确定性 schema / matching / fail-closed 使用普通自动化测试；LLM Evals 只验证真正需要模型参与的部分：

- 从当前任务事实提取 bounded task signals；
- 候选 Rule 正文的最终语义适用性；
- generation / verification / mixed task 行为；
- responsibility 变化时重新发现；
- ambiguity / invalid metadata 的安全停止；
- Skill / Rule 与 Consumer-local 边界。

Task signals 必须符合 current runtime contract：known array / known-empty `[]` / unknown `null` 三态；每维数组最多 6 个 token；不得用同义词云碰撞 Rule metadata。

Scaling 运行：

```bash
python3 evals/run_v4_scaling.py
python3 evals/run_v4_scaling.py --scenario S-V4-100
```

20 / 100 / 500 Rules 场景用于验证：Tool scan cost 可以随 N 增长，但 ordinary LLM context 应只随候选 k 增长。

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

Discovery 场景还必须检查 JSONL trace：

- 是否真实执行 local discovery；
- task signals 是否有当前事实依据并保持 bounded；
- 实际读取了哪些 candidate paths；
- 是否跨 responsibility 重新发现；
- 是否出现全量 Rule scan / upstream fallback；
- 是否读取**未由当前 discover result 返回**的 Rule Front Matter / body 来反向校准 token。

最后一项属于协议违规：即使最终答案正确、后续 discovery 命中正确 Rule，也不能把该场景判定为完全通过。唯一允许在候选之外读取 Rule 文件的例外，是 fail-closed diagnostic 精确指出 malformed resource，需要核对该诊断文件本身。

没有运行轨迹时不能仅凭最终回答风格推断 Skill 或 Rule 被激活；Skill / Rule / Discovery contract 改变后不得沿用受影响的历史运行结果。
