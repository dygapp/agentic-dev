# 非 Skill 工程能力定向评估

本目录保存**不属于 Skill** 的工程能力定向评估，例如技术画像。

它解决的问题是：某项规范性工程能力已经形成草案，但没有也不应该存在对应 `$skill-name` 时，如何在独立运行环境中验证 Agent 是否能够正确应用该能力。

## 与 Skill 运行时评估的区别

Skill 激活 / 行为评估继续验证 Skill 发现与 Skill 契约。

工程能力评估：

- 不创建或激活虚构 Skill；
- 不使用 `$skill-name`；
- 每个语料明确声明 `context_paths`；
- 运行器只把这些当前能力文件复制到仓库外的隔离临时工作区；
- 提示要求运行环境先读取声明的能力上下文；
- 运行环境不得到 `expected_behavior`、`assertions` 或历史结果；
- 每个场景仍使用独立 `codex exec --ephemeral --json`；
- 进程退出码只表示进程状态，不等于评估通过；
- `PASS` / `FAIL` 继续由人工读取最终输出与必要命令轨迹后逐项断言进行语义判分。

## 当前范围

工程能力基础 v1 只增加：

`vue3-typescript-profile.json`

用于验证首个 Vue 3 + TypeScript 技术画像。

这不是新的评估框架、运行时适配器或分发层。后续只有新的非 Skill 工程能力真正需要独立定向评估时，才评估是否增加语料。

## 当前结果

2026-09-02，针对 PR #50 冻结的 Vue 3 + TypeScript 技术画像语义 Blob：

`999911e83b23389d16f9cbbadeb4d5c29f56de75`

在仓库外独立临时工作区完成运行时定向评估：

```text
场景： 9 / 9 PASS
断言：41 / 41 PASS
```

覆盖 `C-VTS-01`～`C-VTS-09`。九次运行均只读取语料声明的 `docs/technology-profiles/vue3-typescript.md` 与场景提示，没有读取工程能力语料、`expected_behavior`、`assertions`、研究材料、历史结果或工作区外路径；所有进程均以状态码 `0` 正常结束，且标准错误为空。进程退出码没有被当作通过依据，结论来自逐项断言语义判分。

结果压缩包 SHA-256：

`abf788b5e51db9fdc145d73dd6eafc16a99a6d3417dbd81b0aa00e538e22a088`

本轮结果证明当前草案画像能正确处理 build / type-check 边界、响应式与 watcher 职责、props / v-model、template ref 生命周期、TypeScript 7 工具兼容、使用方覆盖边界、Element Plus 权威边界与风险驱动验证扩展。

上述 API / 工具名称在涉及实际技术对象时保持原样。

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

结果目录继续属于临时评估证据，不自动成为仓库权威。长期有效的技术画像状态与规范规则仍由 `docs/technology-profiles/` 中的当前实例入口承载。
