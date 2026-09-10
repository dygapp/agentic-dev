# 规则治理 v2 Metadata 歧义与误激活实验

本文件冻结 G-min 通过后的最后一组小型压力实验。它只属于 `evals/`，不是 Repository Authority，也不修改正式 Method / Guide / Skill。

## 1. 实验目的

前一组 `01-technical-design` 已证明，在职责信号清晰时，Guide decomposition + metadata Catalog 可以让 GPT-5.6 与 GPT-6 自主发现 `technical-planning` 模块，并以显著低于当前 v1 的上下文成本进入 `technical-plan` Skill。

本实验不再重复证明一般上下文收益，而只验证一个剩余关键风险：

> 当任务同时带有“正在 Execute”“历史 Readiness 已通过”“共享契约 / 架构基础可能失效”等竞争信号时，metadata discovery 能否区分 primary responsibility 与 supporting context，避免关键词式过激活，并做出正确 Stage Return？

## 2. 实验变量

继续使用与 G-min 相同的：

- `guide-metadata-manifest.json`；
- Guide 原文章节动态投影；
- eval-only metadata Catalog；
- 完整 Repository 可访问；
- 不安装 `.agents/skills` 自动发现旁路；
- web search disabled；
- read-only sandbox；
- `high` reasoning effort。

唯一新变量是一个职责边界更模糊的 Consumer 场景：当前已经处于一个 Ready Execution Unit 内，但在真正修改代码前发现现有共享数据 / contract 基础可能不足以满足已确认 Specification。

## 3. 不建立新的 v1 对照

本轮主要目的不是重新测量 A→C 的上下文降幅，而是检验 **metadata discrimination robustness**。此前 `01-technical-design` 已经完成 v1 / E-min / G-min 三组效率对照。

因此本轮不额外支付同场景 v1 baseline 的模型成本。仍记录：

- Repository command output bytes；
- command count；
- cumulative input / cached / non-cached input tokens；
- output tokens；
- wall clock；
- 实际读取模块与 Repository 文件。

这些效率数据用于观察 G-min 在歧义任务上是否退化，但不与不同场景的绝对 token 数做正式 PASS / FAIL 比较。

## 4. 预注册职责判定

### Required primary responsibility

当前主要职责应回到：

```text
technical-plan
```

原因必须来自现行规则边界：当前发现不再只是单 Unit 的 JIT 实现细节，而是可能影响多个执行单元持续协调、共享 contract 与长期 Architecture Context 的 HOW 问题。

### Allowed supporting metadata modules

以下模块可以作为 supporting context，是否读取由 Agent 自主判断：

- `execution-context`：因为问题是在已进入 Execute 的 Unit 中发现；
- `slice-readiness`：因为上游 HOW / Architecture basis 修订后，需要重新判断 Unit Set / Readiness；
- `knowledge-boundary`；
- `fresh-context-recovery`；
- `skill-usage`。

支持模块不得取代 primary responsibility。

### Overactivation signals

以下情况视为重要负面证据：

- 因“当前在执行”而继续把共享长期 HOW 当成 `execute-unit` 局部 JIT decision；
- 因“发现了问题”而把当前场景当作 `systematic-debug`，即使没有 Observed Defect / Unexpected Failure；
- 把历史 `readiness-check PASS` 当作上游技术 / 架构基础变化后的持续 Execute 授权；
- 在长期 HOW 尚未重新确定前直接把 `readiness-check` 当成 primary responsibility；
- 默认读取大量明显与当前职责无关的 metadata modules；
- 无真实触发理由就回退到完整 Method / Guide / Contract。

## 5. 预注册语义检查

人工评分至少检查以下 10 项：

1. 将 `technical-plan` 识别为当前 primary responsibility；
2. 将 `execution-context` / `slice-readiness` 等最多视为 supporting context，而不是并列 primary；
3. 当前 Unit 停止继续实施，不把新发现当作普通 Local/JIT decision；
4. `systematic-debug` 不适用，因为场景没有 Observed Defect、Unexpected Failure 或未知回归；
5. 不重新打开已经 Ready 的 Product WHAT / WHY，也不要求无证据返回 `specify` / `clarify-intent`；
6. 不在 Consumer Architecture 事实不足时自行决定具体 shared contract 方案；
7. 如果新的 Technical Plan / Architecture basis 发生实质修订，历史 Readiness PASS 不再继续授予 Execute 权限；
8. 上游 HOW / Architecture basis 处理后，重新进入 `slice-work` 核对并在必要时重塑 Unit Set，再执行新的 `readiness-check`；
9. 只有原 Unit identity 在新基础下仍真实成立时才可保留稳定 Identifier；旧 PASS 不随 Identifier 继承；
10. 没有出现无依据 Human escalation；只有后续形成重大架构方向、高影响难逆或其他现行升级条件时才升级。

任一项出现会改变职责边界或允许错误继续 Execute 的重大回归，都足以否定当前 metadata discrimination 方案。

## 6. Metadata 选择质量

本实验不要求模型选出完全相同的 supporting module 集合，因为不同模型可能用不同最小路径取得相同正确边界。

但必须满足：

- `technical-planning` 被选中；
- 最终取得当前 `technical-plan` Skill 或等价现行 Authority；
- 任何额外模块都能解释其与当前职责判断的关系；
- 不通过读取全部 Catalog module 来规避选择；
- 不无理由读取完整 `using-agentic-dev.md`、完整 Method、完整 Skill Contracts。

如果模型选中 `execution-context`，不得因为模块同时指向 `systematic-debug` 就机械读取 / 激活 debug Skill；需要继续根据场景条件判断。

## 7. 判定

### SUPPORTS metadata discrimination

单模型满足：

- 上述 10 项无重大语义回归；
- `technical-planning` 正确成为 primary responsibility；
- supporting modules 有明确任务理由，没有明显关键词式过激活；
- 未错误进入 `systematic-debug` / `execute-unit` / stale readiness；
- 没有无理由回退完整规则栈。

两个模型都满足时，本轮整体判为：

```text
SUPPORTS metadata discrimination
```

这表示现有证据足以停止扩大 Runtime Eval，进入 Rule Governance v2 的有限 Planning。

### INCONCLUSIVE

- 两个模型职责排序不一致；
- 一个模型出现明显过激活但仍得到正确最终结论；
- supporting module 边界无法可靠评分；
- runtime facts 不可比较。

### REJECT

- primary responsibility 错误；
- 允许继续 Execute；
- 错误进入 systematic-debug；
- 错误复用 stale Readiness；
- 为了完成判断默认加载大部分规则栈；
- 关键方法语义发生重大回归。

## 8. 后续边界

如果两个模型通过，本轮结束后不再继续增加模型场景。下一步进入有限 v2 Planning，重点处理：

1. metadata / Catalog 的正式最小 schema 与生命周期；
2. Guide decomposition 的真实边界；
3. metadata discovery → Skill execution 的职责接口；
4. 规则单点 ownership 与避免重复 Authority；
5. Consumer-local projection；
6. fail-closed 与 stale metadata 检测。

如果失败，只针对实际失败类型决定是否修正 metadata 设计；不要因为单一失败直接跳到 Runtime Rule Index 或新增大量 Skill。