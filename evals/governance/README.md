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

## 正式概念语义安全评估

当前语料：

`formal-concept-semantic-safety.json`

目标是验证：Agent 在同时读取当前最高语言规则、正式概念身份映射，以及仍可能包含旧中文迁移别名的高优先级架构 / 契约文档时，能够稳定恢复正式工程概念身份，不因为中文化把能力层、方法对象或职责边界错误合并。

当前专项场景 `G-TERM-01` 直接覆盖：

- 技术画像 (`Technology Profile`)；
- 验证画像 (`Verification Profile`)；
- 任务型技能 (`Task-oriented Skill`)；
- 运行时适配器 (`Runtime Adapter`)。

它必须读取真实的 `engineering-capability-architecture.md` 与 `technology-profile-contract.md`，而不是只依赖题面描述旧别名。

## 运行边界

每个场景必须：

- 在独立临时工作目录运行；
- 只复制对应语料声明的 `context_paths`；
- 不向运行时暴露 `expected_behavior`、`assertions` 或历史结果；
- 不加载 Skill，也不虚构 Skill；
- 使用独立 `codex exec --ephemeral --json`；
- 进程退出码不作为语义通过依据；
- 由人工逐项读取最终输出并按断言评分。

运行全部项目治理场景：

```bash
python3 evals/run_governance_evals.py
```

运行指定场景：

```bash
python3 evals/run_governance_evals.py --scenario G-LANG-01
python3 evals/run_governance_evals.py --scenario G-TERM-01
```

结果写入：

`evals/results/governance/`

## 评分边界

“使用中文”不是简单统计汉字比例；“术语正确”也不是只检查是否出现某个英文词。人工评分至少检查：

1. 结论、动作、因果、状态和说明是否以自然中文完成；
2. 已有稳定中文表达的普通方法概念是否仍机械附带英文；
3. 代码标识、路径、命令、Git 引用、Skill 调用名和必须精确匹配的值是否被正确保留；
4. 输入中的英文、旧语风或历史偏好是否错误覆盖当前仓库规则；
5. 是否为了追求纯中文而错误翻译机器字段、代码或外部正式名称；
6. 正式概念是否保持正确对象类型、架构层级和职责边界；
7. 旧中文迁移别名是否被错误解释为新的正式能力层或新的概念；
8. 是否仍保持原任务要求的语义正确性，而不是只追求语言形式。

只有语言规则、正式概念身份和任务语义同时满足，场景才能判为通过。