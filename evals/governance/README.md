# 项目治理定向评估

本目录保存 `agentic-dev` **仓库自身项目治理规则**的定向运行时评估。

它与现有两类评估保持边界：

- `evals/behavior/` 验证某个 Skill 已被选择后的行为契约；
- `evals/capability/` 验证不属于 Skill 的可复用工程能力，例如技术画像；
- `evals/governance/` 只验证 `agentic-dev` 自身会持续影响 Agent 行为的项目级治理规则。

这里的评估不会把项目治理提升为通用方法、工程纪律、技术画像或 Skill。

## 中文表达治理评估

当前语料：

`chinese-human-facing-output.json`

目标是验证：Agent 在只读取当前项目语言权威和题面输入的独立上下文中，能够稳定遵循“自然中文默认、必要原始标识例外”，而不会因为旧会话描述、英文状态、工具输出或大量英文术语重新恢复中英文混写。

每个场景必须：

- 在独立临时工作目录运行；
- 只复制语料声明的 `context_paths`；
- 不向运行时暴露 `expected_behavior`、`assertions` 或历史结果；
- 不加载 Skill，也不虚构 Skill；
- 使用独立 `codex exec --ephemeral --json`；
- 进程退出码不作为语义通过依据；
- 由人工逐项读取最终输出并按断言评分。

运行：

```bash
python3 evals/run_governance_evals.py
```

运行指定场景：

```bash
python3 evals/run_governance_evals.py --scenario G-LANG-01
```

结果写入：

`evals/results/governance/`

## 评分边界

“使用中文”不是简单统计汉字比例。人工评分至少检查：

1. 结论、动作、因果、状态和说明是否以自然中文完成；
2. 已有稳定中文表达的普通方法概念是否仍机械附带英文；
3. 代码标识、路径、命令、Git 引用、Skill 调用名和必须精确匹配的值是否被正确保留；
4. 输入中的英文、旧语风或历史偏好是否错误覆盖当前仓库规则；
5. 是否为了追求纯中文而错误翻译机器字段、代码或外部正式名称；
6. 是否仍保持原任务要求的语义正确性，而不是只追求语言形式。

只有语言规则与任务语义同时满足，场景才能判为通过。