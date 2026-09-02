# Non-Skill Capability Targeted Evals

本目录保存 **不属于 Skill** 的 Engineering Capability Targeted Eval，例如 Technology Profile。

它解决的问题是：某项规范性工程能力已经形成 Draft，但没有也不应该存在对应 `$skill-name` 时，如何在 Fresh Runtime 中验证 Agent 是否能够正确应用该能力。

## 与 Skill Runtime Eval 的区别

Skill Activation / Behavior Eval 继续验证 Skill discovery 与 Skill contract。

Capability Eval：

- 不创建或激活虚构 Skill；
- 不使用 `$skill-name`；
- 每个 corpus 明确声明 `context_paths`；
- runner 只把这些当前能力文件复制到仓库外的隔离临时工作区；
- prompt 要求 Runtime 先读取声明的 Capability Context；
- Runtime 不得到 `expected_behavior`、`assertions` 或历史结果；
- 每个场景仍使用独立 `codex exec --ephemeral --json`；
- 进程退出码只表示进程状态，不等于 Eval PASS；
- PASS / FAIL 继续由人工读取最终输出与必要命令轨迹后逐 assertion 语义判分。

## 当前范围

Foundation v1 只增加：

`vue3-typescript-profile.json`

用于验证首个 Vue 3 + TypeScript Technology Profile。

这不是新的 Benchmark Framework、Runtime Adapter 或 Distribution 层。后续只有新的非 Skill Capability 真正需要独立 Targeted Eval 时，才评估是否增加 corpus。

## 运行

```bash
python3 evals/run_codex_evals.py --capability
```

按场景运行：

```bash
python3 evals/run_codex_evals.py --capability --scenario C-VTS-01
```

运行结果写入：

`evals/results/capability/`

结果目录继续属于临时 Eval evidence，不自动成为 Repository Authority。