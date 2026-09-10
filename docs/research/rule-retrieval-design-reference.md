# 规则检索设计参考

本文记录 `agentic-dev` 已验证过的**规则发现 / 激活技术设计**。它解释 v1 规则检索实验以及这些结果如何被后续 Consumer-local 机制吸收，不是 Repository Authority，也不定义当前项目状态。

当前规范性激活入口：

- `docs/guides/rule-activation-guide.md`
- `docs/guides/consumer-local-rule-activation.md`

当前 Consumer-local discovery 逻辑契约：

`docs/project/consumer-local-activation-metadata-contract-v2.md`

v1 JSON/Python rule-index 原型已经完成验证职责并退出当前可执行面；冻结设计与评分证据仍保留在 `evals/rule-retrieval/`。历史里程碑与精确实现可从 `docs/project/rule-governance-knowledge-activation-v1.md`、Git、PR #74～#89 和 Issue #73 恢复。

## 1. 设计目标

规则发现层只解决一个问题：**根据当前任务职责和已知风险，找到足以正确执行当前任务、又不引入大量无关上下文的最小规则入口。**

它必须可回到当前规范性来源、不复制第二份规则权威、保留项目 / 仓库作用域、来源陈旧或判断不可靠时安全回退、选择过程可解释，并且派生数据可删除、可重建。

## 2. 稀疏查询模型

最小发现语义使用两个主要维度：

```text
作用域 + 当前职责
```

只有候选集合会因此改变时，才增加：

```text
+ 当前阶段
+ 目标对象
+ 风险 / 状态条件
```

这些维度是逻辑输入，不要求用户填写固定表单。未知条件不得为了“命中更多规则”而猜测。

v2 将相同思想收敛为 Consumer-local `scope + responsibility candidate + only-known conditions / risks`，并由本地 Manifest / Catalog 负责发现，不要求继续使用 v1 JSON schema。

## 3. 作用域必须保真

跨仓库工作至少需要区分当前项目事实由哪个仓库权威主导、当前职责正在读取或改变哪个仓库 / 外部对象，以及其他仓库究竟是只读方法来源、使用方事实来源还是具有明确写入授权。

这可以避免把 `agentic-dev` 自身项目规则误带入 Consumer，也避免把对一个仓库的授权扩张为跨仓库授权。

## 4. 一个查询 / 路由只描述一个当前职责

职责从执行切换到验证、从验证切换到集成复核，或从普通开发进入显式 baseline upgrade 时，应重新解析规则入口。第一次得到的规则集不能被当成整个会话永久上下文。

v2 进一步区分 primary responsibility 与 supporting constraints；只做 routing / Stage Return 时不机械加载完整 execution Skill。

## 5. 最小正确规则集

“最小”不是固定条数、最低令牌数或最少文件数，而是：**没有遗漏任何当前必需规则，同时不装入当前职责不需要的规则。** 因此不能使用固定 Top-K 代替完整召回当前适用的必需规则。

通常应纳入当前作用域和职责成立的核心不变量、触发条件已经由事实满足的条件必需规则，以及当前职责独立执行需要的最小 Skill / 平台专项守卫。默认排除触发条件未满足的条件规则、其他项目作用域规则、纯历史证据、已被当前 Authority 取代的旧规则，以及当前职责无关的相邻指南内容。

## 6. v1 最小输出与 v2 收敛

v1 评估为了观察检索行为，派生结果包含：

- `source_pointer`；
- `activation_summary`；
- `applicability`；
- `required_checks`；
- 命中 / 回退解释。

这些字段帮助验证“检索是否正确”，但摘要始终不能脱离源指针成为长期权威。

v2 的 ordinary Consumer runtime 进一步做减法：Manifest / Catalog 只保存发现所需的最小 metadata 与 local source pointer，不保存完整 `activation_summary`、`required_checks` 或规则正文。Agent 在发现候选后读取 Consumer-local semantic owner，再执行规则。

因此 v1 的输出结构是**实验观察结构**，不是 v2 必须兼容的 Runtime schema。

## 7. 条目角色与关系的历史价值

v1 原型曾使用 `authority`、`pointer`、`consumer` 三类角色，以及 `equivalent`、`scope-variant`、`superseded-by` 等最小关系，用于证明作用域、来源身份和关系选择可以显式建模。

v2 没有原样继承这些枚举，而是将真正长期需要的身份收敛到 Consumer-local record：例如 `kind`、`activation_role`、`origin`、`state` 与必要的 `overrides / supersedes`。具体 schema 可以变化，但关系不能改变 Repository Authority 的原则保持不变。

## 8. Fail-closed

出现规范性来源缺失、来源 identity 已变化、源指针无法精确解析、必需维度未知、发现无命中但仍存在治理风险、作用域冲突，或高影响授权 / 架构 / 安全 / 隐私 / 不可逆边界无法可靠判断时，不应继续用派生信息声称规则召回完整。

通用回退原则：

```text
停止依赖当前派生发现结果
→ 回到当前 Repository Authority
→ 按当前职责读取真实 semantic owner
→ 重新判断
```

“不命中”不能被解释为“没有规则”。

v2 在 Consumer 中将该原则具体化为 fail-closed 到 Consumer-local Current Authority；ordinary runtime 不因为本地发现失败而自动跨仓访问 upstream。

## 9. v1 派生实现为何曾保持简单

v1 评估原型使用 `JSON 派生规则索引 + Python 标准库薄查询器`。JSON 足以表达当时需要的稀疏条件、源 identity 和最小关系，Python 标准库足以完成确定性过滤、来源校验和机器可读输出；因此不需要数据库、第三方检索包、MCP 服务或全仓统一 Front Matter。

该选择验证了“先用最小机制证明行为收益”的方向，而不是形成永久 JSON / Python 架构承诺。

## 10. v1 历史实现映射

v1 完成时的实现关系是：

| 技术职责 | v1 历史实现 |
|---|---|
| 派生规则条目与 source identity | `evals/rule-retrieval/rule-index.json` |
| 查询、过滤、来源陈旧检查 | `evals/query_rule_index.py` |
| A/B 工作区与静态回归 | `evals/run_rule_retrieval_ab.py` |
| C3 隔离运行 | `evals/run_rule_retrieval_c3.py` |
| fixture / 结果结构 | `evals/rule-retrieval/` 下相应运行资产 |

这些文件曾属于 Evaluation Asset，从未属于 Repository Authority。v2 确立 Consumer-local Manifest / optional Catalog 后，这套 runnable prototype 已被 supersede 并从当前树移除；需要复核代码时从 Git / PR #81、#82 及阶段 C 相关历史恢复。

当前树不再维护它们的 source identity，也不允许把冻结的 v1 预期 rule keys 重新解释为当前规则索引。

## 11. 已取得的验证信号

历史隔离 A/B 中，9 / 9 pair 可比较；按需检索组的直接命中场景召回冻结的 29 / 29 必需规则，3 / 3 安全回退 reason 正确，按需检索组行为语义 9 / 9 PASS，完整相关文档组为 8 / 9。直接命中场景观察到的命令输出字节约下降 48.6%，wall-clock 约下降 49.8%；fallback 成本更高，但 stale / unknown / no-match 的安全回退均正确，因此不能为了成本删除 fail-closed。

冻结的机器可读评分结果保存在：

`evals/rule-retrieval/c3-human-scoring.json`

冻结场景与隐藏断言保存在：

`evals/rule-retrieval/targeted-evaluation-design.json`

这些结果证明稀疏发现、source currentness 与 fail-closed 值得作为长期技术原则，也为 v2 的 Consumer-local 方案提供了前置证据；它们不证明所有仓库、模型或任务都能获得相同比例收益。

## 12. Discovery mechanism 生命周期

同一 Runtime scope 中，对于同一个 discovery responsibility，应只有一个被声明为 **current** 的机制。

如果新机制已经 supersede 旧的派生 index / catalog / retriever：

- 旧机制必须退出 Current Runtime / Eval surface，或被明确标记为 frozen historical evidence；
- 历史设计、评分和 Git 实现可以继续保留以支持审计，但不能继续伪装成当前可执行入口；
- 如果某个派生机制仍声明为 current runnable asset，就必须纳入 source-currentness 生命周期，保证 source pointer、identity、selector 和语义映射真实有效；
- 不允许保留“文件仍可执行、README 仍称 current，但 source 已经 stale”的第三种状态；
- 新机制替换旧机制时，应检查旧入口、脚本、fixture、文档引用和恢复导航是否一并退出 Current surface。

无论技术如何变化，长期边界仍是：当前 Authority 单点定义、派生层可重建、陈旧可检测、失败时安全回退。具体检索技术可以替换，历史原型不需要为了保持“看起来可运行”而永久同步。
