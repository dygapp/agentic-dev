# 使用 Codex CLI 执行运行时评估

本指南说明如何执行 `agentic-dev` 当前维护的隔离运行时评估。它只定义评估操作方式，不改变通用方法、Skill 架构或工程能力分层。

## 1. 使用隔离工作副本

不要在日常开发工作区直接运行会修改 fixture 的评估。使用当前评估分支的临时 clone / worktree，并确保每条会修改文件的场景都从干净状态开始。

```bash
git clone <agentic-dev-repo> agentic-dev-eval
cd agentic-dev-eval
git checkout <current-eval-branch-or-commit>
```

建议把运行时临时内容加入本地 exclude，而不是修改仓库 `.gitignore`：

```bash
printf '\n.agents/\nevals/workspace/\nevals/results/\n' >> .git/info/exclude
```

## 2. 隔离原则

评估运行时不得读取评分答案、历史结果或日常开发会话上下文。

现有评估分为：

- Skill 激活评估：只复制当前仓库实际维护的 Skill package，不预加载目标 `SKILL.md`；
- Skill 行为评估：复制当前 Skill package，并显式调用目标 Skill；
- 非 Skill 工程能力评估：只复制语料声明的 `context_paths`；
- 项目治理评估：只复制项目治理语料声明的 `context_paths`，不加载 Skill，也不把项目规则包装成工程能力。

所有场景都应在仓库外临时工作目录运行。Codex 子进程的实际 `cwd` 和 `PWD` 必须指向该隔离目录，并移除常见的 Git 环境线索，防止运行时反向定位日常仓库。

如果运行时能够读取 `expected_behavior`、`assertions`、历史结果或其他评分答案，该次运行判为评估基础设施污染，不能作为通过证据。

## 3. Skill 与工程能力评估运行器

现有主运行器：

```text
evals/run_codex_evals.py
```

它负责：

- 每个场景启动独立 `codex exec --ephemeral --json`；
- 激活和行为评估使用仓库外 Skill 副本；
- 非 Skill 工程能力评估只复制显式声明的上下文；
- `B-EU-01` 使用干净、可写的 fixture；
- 保存 JSONL、stderr 和运行元数据；
- 不自动进行语义评分。

常用命令：

```bash
python3 evals/run_codex_evals.py --activation --scenario A-CI-01
python3 evals/run_codex_evals.py --behavior --scenario B-EU-01
python3 evals/run_codex_evals.py --capability --scenario C-VTS-01
```

运行历史的 Skill 激活与行为全集：

```bash
python3 evals/run_codex_evals.py --all
```

`--all` 保留现有历史语义，只运行 Skill 激活与 Skill 行为语料，不自动包含非 Skill 工程能力或项目治理评估。

## 4. 项目治理评估运行器

项目治理定向评估使用：

```text
evals/run_governance_evals.py
```

当前中文表达治理全集：

```bash
python3 evals/run_governance_evals.py
```

运行单个场景：

```bash
python3 evals/run_governance_evals.py --scenario G-LANG-01
```

项目治理运行器复用主运行器已有的隔离上下文复制、Codex 调用和结果保存能力，但不把项目治理登记成 Skill 或工程能力。

结果写入：

```text
evals/results/governance/
```

具体语料和人工评分边界见：

`evals/governance/README.md`

## 5. Skill 激活评估

输入：

```text
evals/activation/core-first-pass.json
```

规则：

- query 不显式附加目标 Skill 名；
- 每个 query 使用独立新运行；
- 使用 `--ephemeral`；
- 保存 JSON Trace；
- 运行目录中不得存在激活语料、目标答案或评分断言；
- 默认只需要只读行为。

应优先从 JSONL Trace 判断目标 `SKILL.md` 是否实际被读取或加载，不要只根据最终回答风格推测 Skill 已被使用。

如果当前 Codex 版本无法观察 Skill 加载，应记录为不可观察的评估基础设施缺口，而不是判为通过。

## 6. Skill 行为评估

行为评估输入来自已经登记到主运行器的：

```text
evals/behavior/*.json
```

行为评估显式调用目标 Skill，目的是隔离验证：Skill 已经被选择后，是否真正遵守其职责边界、阶段返回、人工升级、上下文和证据契约。

每个场景必须使用新的 `codex exec`，不能 `resume`。

如果 Trace 读取了仓库中的 `evals/behavior/*`、`evals/results/*`、预期行为或评分断言，该次运行属于基础设施污染，不能因为最终回答看起来正确就判为通过。

## 7. `execute-unit` 可运行 fixture

`B-EU-01` 会真实修改：

```text
evals/fixtures/execute-unit-basic/
```

运行器每次都从源 fixture 复制到独立临时工作目录，运行后把最终快照保存到：

```text
evals/workspace/B-EU-01/
```

fixture 的仓库验证命令：

```bash
python3 -m unittest discover -s tests -v
```

运行后至少检查：

- JSONL Trace；
- fixture 最终文件；
- 实际验证输出；
- 完成声明是否引用本次当前证据；
- 是否只处理 `greeting-01`；
- 是否停止在执行单元完成边界，没有执行 merge、push、release 或 deploy。

下一次运行必须重新复制干净 fixture，不能沿用已经修好的工作目录。

## 8. 结果判定

进程退出码只表示 Codex 进程是否正常结束，不表示语义评估通过。

每个场景必须由人工读取最终输出和必要命令轨迹，并逐项检查语料中的 `assertions`。

最小结果记录可以包含：

```text
运行环境：Codex CLI
模型：<实际模型或未观察到>
对应提交：<commit SHA>
场景：<id>
结论：通过 / 失败 / 不可观察
断言结果：
  - <断言>: 通过 / 失败 / 不可观察
证据：
  - <Trace / 最终输出 / 测试输出引用>
备注：
  - <可选>
```

必须保持以下边界：

- 退出码 `0` 不能替代人工语义评分；
- 当前长聊天中的文本推演不能替代隔离运行时评估；
- 没有 Trace 的“看起来触发了”不能证明 Skill 激活；
- 同一会话连续跑多个场景不满足独立运行要求；
- Skill 或治理规则修改后不得沿用旧会话结果；
- 运行时读取评分答案或历史结果后得到的答案属于污染结果；
- 当前完成声明必须由与当前目标状态匹配的证据支持。

## 9. 语言与评估结果

当前仓库的评估指南、人工评分记录和结果汇报遵循 `docs/guides/terminology-guidelines.md`。

历史评估材料中已有的英文状态、场景说明和原始运行输出可以作为历史证据保留，但**不构成当前仓库面向人的表达示范**。新的人工汇报应使用自然中文，只在命令、场景编号、机器字段、路径、日志或必须精确匹配的对象中保留原始英文。