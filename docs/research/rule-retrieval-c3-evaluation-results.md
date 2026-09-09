# C3 规则检索 A/B 运行与人工评分结果

记录日期：2026-09-09

阶段：**规则治理与知识激活 v1 / 阶段 C / C3 — 隔离运行时与人工评分**

文档性质：**Research / Evaluation Evidence，不是 Repository Authority**

集成起点：

`master@7130605453448993ce9ec08fc24309f5ff85510f`

## 1. 证据输入

人工回传归档：

`c3-rule-retrieval-eval-results.tar.gz`

- 大小：`510410` bytes
- SHA-256：`593192db13a07604c136895a77076833b3166c19b232f43a76ba81a6ea05b6e4`
- 结构：18 个 `.result.json`、18 个 `.runtime-facts.json`、18 个 `.jsonl`、18 个过滤后 `.stderr.txt`
- 归档未包含 `git-head.txt`

原始 `evals/results/` 继续属于临时评估证据，不提交为 Git 长期权威；本文件与
`evals/rule-retrieval/c3-human-scoring.json` 只保存可复核评分、指标和证据摘要。

## 2. 公平性 / 完整性

18 / 18 个 Codex 进程退出码为 `0`。

9 / 9 个 A/B pair 均满足：

- `runtime_facts_status = observed`
- `pair_fairness_status = comparable`
- provider model：`gpt-5.6-sol`
- reasoning effort：`high`

因此 9 个 pair 全部具备进入行为效果比较的公平性条件。

归档中所有持久化 `stderr.txt` 均未发现原始 `SSE event:` 或
`codex.turn.reasoning_effort=` trace，C3 Readiness 的 trace 最小化边界在本次真实运行中继续成立。

### 2.1 Git HEAD 追溯限制

归档未包含 `git-head.txt`，所以不能仅由该压缩包直接证明本地精确 Git HEAD。

这不使本次 A/B 失效，原因是：

1. A/B 由同一 C3 runner 批次顺序执行，使用同一工作区来源；
2. C3 Codex 子进程均为 read-only；
3. B 的 6 个直接命中场景只有在全部活动索引规范性来源 identity 校验通过后才会继续直接命中；
4. 6 个直接命中场景均未触发 stale fallback，说明 8 个活动索引规范性来源与冻结 identity 一致；
5. 三个控制 fallback reason 也与 C1 设计完全一致。

后续真实运行应把 `git rev-parse HEAD` 一并放入回传归档，关闭这一追溯缺口。

## 3. B 规则层结果

### 3.1 直接命中

6 个直接命中场景全部得到与 C1 冻结预期**完全一致**的规则键集合：

| 场景 | 结果 |
| --- | --- |
| RR-C1-02 | `UG-01, UG-02, UG-03, UG-07, UG-14, CON-SLICE` |
| RR-C1-03 | `UG-01, UG-02, UG-03, UG-14, UG-15, CON-READINESS` |
| RR-C1-04 | `UG-01, UG-02, UG-03, UG-19, CON-GHA` |
| RR-C1-05 | `UG-01, UG-02, UG-03, UG-21, EO-16, EO-17` |
| RR-C1-06 | `UG-01, UG-02, UG-03, UG-25` |
| RR-C1-07 | `EO-07, EO-09` |

派生指标：

- direct-hit exact expected set：`6 / 6`
- required rule hits：`29 / 29`
- `required_rule_recall = 100%`
- 在 C1 冻结 expected set 上没有额外规则键：`activation_precision = 100%`

这里的 precision 只描述首轮冻结 expected set，不代表全仓库所有可能规则已经得到完整人工相关性标注。

### 3.2 安全回退

3 个控制回退场景全部得到正确 reason：

| 场景 | 预期 / 实际 |
| --- | --- |
| RR-C1-01 | `no_indexed_rule_match` |
| RR-C1-08 | `indexed_source_stale_or_missing` |
| RR-C1-09 | `query_values_not_modeled` |

结果：`3 / 3` 回退类型正确。回退后 B 均给出正确语义结论，没有把回退误判为任务失败，也没有用近似规则伪装真实规则缺口。

## 4. 行为层人工评分

人工评分不把 B 内部查询 / fallback 机制作为 A 组必须回答的行为断言；B 的检索正确性已在第 3 节单独评分。
A/B 共同按最终任务行为、误停 / 误升级 / 误执行与权威边界评分。

| 场景 | A | B | 结论 |
| --- | --- | --- | --- |
| RR-C1-01 | PASS | PASS | 两侧都拒绝瞬时 PR 状态与机械尾部 PR |
| RR-C1-02 | **FAIL** | PASS | A 无证据把 `Return To` 固定为 `specify`；B 条件化检查上游 Ready 后进入 `slice-work` |
| RR-C1-03 | PASS | PASS | 两侧都要求实质 WHAT/HOW 修订后重新 `slice-work → readiness-check` |
| RR-C1-04 | PASS | PASS | 两侧都拒绝用祖先绿色 CI 冒充当前 trigger/gate 证据 |
| RR-C1-05 | PASS | PASS | 两侧都要求必要内容显式晋升、来源追溯与完整性 |
| RR-C1-06 | PASS | PASS | 两侧都保持 Consumer-local Authority 优先 |
| RR-C1-07 | PASS | PASS | 两侧都只要求写后重读，不扩张到未触发治理 |
| RR-C1-08 | PASS | PASS | 两侧都要求 stale index 回退当前规范性源 |
| RR-C1-09 | PASS | PASS | 两侧都拒绝从证据晋升规则推导 90 天保留许可 |

汇总：

- A semantic PASS：`8 / 9`
- B semantic PASS：`9 / 9`
- A wrong stop / escalation：`1`
- B wrong stop / escalation：`0`
- authority confusion：`0`
- wrong execution：`0`

### 4.1 RR-C1-02 A 的失败分类

A 正确完成了以下核心判断：

- EU 风格编号 / Roadmap 排序不授予 Execution Unit 身份；
- 不能直接 `execute-unit`；
- 必须形成真实切分产物；
- readiness PASS 前没有执行授权。

但 A 进一步把“当前输入没有看到可追溯 Execution Unit 切分产物”推导成：

> `Return To: specify`

题面没有证明 Specification 未 Ready，因此把 `specify` 固定为必须返回点属于额外误停 / 错误阶段选择。

失败分类：

`选择 / 冲突`

B 的处理更精确：先确认 Specification / 必要 Technical Planning 的当前 readiness；如果已 Ready，则进入
`slice-work`；只有上游确实未 Ready 时才返回 `clarify-intent` / `specify` / `technical-plan`。

因此本场景提供了阶段 C 所需的行为收益证据：较小、条件化上下文没有降低正确性，并避免了一次粗粒度上下文下的过度保守阶段选择。

## 5. 可取得成本指标

当前 runner 没有稳定提供 input token、output token、file read count 或 rule bytes / lines。
按 C1 规则，这些字段保持空值，不做推测估算。

本次只从 JSONL 已记录的 `command_execution.aggregated_output` 直接统计**实际命令输出字节**，并记录 runner 已提供的 wall-clock。
“命令输出字节”是可重复观察的上下文代理，不等同于模型 input token。

### 5.1 直接命中场景（RR-C1-02～07）

- A command output：`625,617` bytes
- B command output：`321,879` bytes
- B 相对 A：`-48.6%`

- A wall-clock：`1,011.585 s`
- B wall-clock：`507.753 s`
- B 相对 A：`-49.8%`

直接命中是当前原型收益最明确的区域：必要规则完整召回，同时显著缩小实际工具输出上下文与总耗时。

### 5.2 fallback 场景（RR-C1-01 / 08 / 09）

- A command output：`197,115` bytes
- B command output：`312,720` bytes
- B 相对 A：`+58.6%`

- A wall-clock：`295.391 s`
- B wall-clock：`681.017 s`
- B 相对 A：`+130.5%`

fallback 的额外查询、检测与完整 Authority 重读成本很明显。

**该结果不是删除 fallback 的证据。** C1 的优先级要求语义正确性、完整召回和 stale / unknown / no-match 安全性高于成本。
阶段 D 应减少不必要 fallback 或改善可发现性，但不得把未知 / stale 情况改成静默零结果或近似规则替代。

### 5.3 全部 9 场景

- A command output：`822,732` bytes
- B command output：`634,599` bytes
- B 相对 A：`-22.9%`

- A wall-clock：`1,306.976 s`
- B wall-clock：`1,188.770 s`
- B 相对 A：`-9.0%`

wall-clock 受服务端负载等外部因素影响，只作辅助观察，不作为单独优劣判据。

## 6. 阶段 C 结论

阶段 C 已形成足够证据判断：

> **“薄入口 + 条件检索 + 当前源指针 + 保守安全回退”在当前冻结高影响规则面上优于文件级粗粒度加载，具备进入阶段 D 的证据。**

证据链：

1. 9 / 9 pair 公平性可比较；
2. B 的 6 个直接命中场景 `29 / 29` 必需规则完整召回，且冻结 expected set 无额外键；
3. B 的 3 个回退场景 reason `3 / 3` 正确，回退后语义仍正确；
4. B 行为层 `9 / 9` PASS，没有 authority confusion、wrong execution 或 wrong stop；
5. A 为 `8 / 9`，RR-C1-02 出现一次可定位的 wrong stop；
6. 直接命中场景 B 的实际命令输出字节与 wall-clock 均约减半；
7. fallback 场景成本显著升高，说明长期设计必须保留“精确直接命中 + 保守回退”的双路径，而不是追求所有查询都强制命中。

该结论只适用于本轮审计和索引覆盖的高影响规则面。它不证明应该：

- 全仓库建立规则数据库；
- 全量拆分指南；
- 所有规则都进入索引；
- 删除 fallback；
- 引入图数据库 / MCP / Obsidian / CodeGraph 作为核心依赖；
- 把派生索引提升为 Repository Authority。

## 7. 下一门禁

阶段 C 的 C3 条件已经满足。下一实际步骤：

> **D1 — 基于证据实施指南 / 权威收敛**

D1 只实施本次证据能直接支持的动作：

- 保持薄常驻入口；
- 优先固化高价值直接命中规则的稳定激活指针 / 最小派生索引；
- 检查 RR-C1-02 暴露的粗粒度选择噪声是否能通过条件激活进一步收敛；
- 对当前已审计的实质重复做减法，但不复制新权威；
- 保留 stale / unknown / no-match 的 fail-closed 回退；
- 不为了降低 fallback 成本扩大到全仓库无证据索引化。

完成 D1 后必须进入 D2 回归，再进入至少一个真实使用方的新上下文验证。
