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

- `formal-concept-semantic-safety.json`
- `method-object-semantic-safety.json`

目标是验证：Agent 在读取当前最高语言规则、正式概念身份映射与对应定义权威时，能够稳定恢复正式工程概念身份，不因为中文化把能力层、方法阶段、产物、门禁或 Skill 调用名错误合并。

阶段 B 已经把现行定义权威中的“技术配置档”“验证配置档”“运行时适配层”等冲突中文名称收敛为唯一首选名称。因此最终 `G-TERM-01` 不再假设现行定义权威仍包含这些旧别名，而是把旧别名作为题面中的历史 / 迁移输入，验证 Agent 不会因为看到旧材料而把它们重新提升为当前正式名称或新的能力层。

`G-TERM-01` 直接覆盖：

- 技术画像 (`Technology Profile`)；
- 验证画像 (`Verification Profile`)；
- 任务型技能 (`Task-oriented Skill`)；
- 运行时适配器 (`Runtime Adapter`)。

它必须读取真实的 `engineering-capability-architecture.md` 与 `technology-profile-contract.md`，从当前已收敛定义恢复概念身份，而不是依赖题面里的旧别名定义概念。

`G-TERM-02` 直接覆盖：

- 技术规划阶段 (`Technical Planning`) 与技术计划产物 (`Technical Plan`)；
- 整体收敛阶段 / 职责 (`Converge`) 与 `converge` Skill 调用名；
- 就绪门禁 (`Readiness Gate`) 与 `readiness-check` Skill 调用名；
- 执行阶段 (`Execute`) 与 `execute-unit` Skill 调用名。

它必须读取真实的核心方法、Skill 架构与 Skill 契约，验证中文化不会抹平对象类型和职责边界。

## 依赖 PR 集成拓扑评估

当前语料：

`stacked-pr-integration-topology.json`

目标是验证：Agent 在 GitHub + squash merge 的依赖式 PR 场景中，能够先判断当前依赖链是否由平台原生 stack 生命周期管理，再建立与实际平台状态一致的集成拓扑和当前证据，而不会把历史审查 ancestry、旧 Head 或工具动作成功直接当成“已具备进入集成决策的条件”。

三个场景分别覆盖：

- `G-PR-TOPO-01`：普通手工依赖 PR 链在父层 squash merge 后的 child normalization 与当前证据；
- `G-PR-TOPO-02`：GitHub 原生 stack 在平台级联 rebase / retarget 后的状态核验与证据边界；
- `G-PR-TOPO-03`：依赖模式、PR 快照或 Head 身份不明确时的安全退出与恢复路径。

该评估不得导出“禁止 stacked PR”“强制 GitHub 原生 stack”“强制某种分支策略 / 合并策略”或修改核心方法 / 技能契约的结论。

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
python3 evals/run_governance_evals.py --scenario G-TERM-02
python3 evals/run_governance_evals.py --scenario G-PR-TOPO-01
python3 evals/run_governance_evals.py --scenario G-PR-TOPO-02
python3 evals/run_governance_evals.py --scenario G-PR-TOPO-03
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
7. 旧中文迁移别名是否被错误解释为当前正式名称或新的能力层；
8. 方法阶段、产物、门禁和 Skill 调用名是否被错误合并；
9. 是否仍保持原任务要求的语义正确性，而不是只追求语言形式；
10. 依赖 PR 场景是否先确认实际平台管理模式，而不是根据 `stacked` 名称或历史 base 猜测；
11. PR Head、base、diff、checks 或集成基线改变后，是否重新判断当前证据适用范围；
12. 是否避免把平台预览期细节错误提升为永久方法契约或统一仓库策略。

只有对应治理规则、正式概念身份和任务语义同时满足，场景才能判为通过。
