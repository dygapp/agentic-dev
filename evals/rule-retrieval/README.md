# 规则检索与激活 A/B 评估

本目录保存“规则治理与知识激活 v1”阶段 C 的规则检索 / 激活评估资产。

这些文件属于 `evals/` 评估资产，**不是 Repository Authority**。删除它们不会删除任何规范性规则；所有行为判断仍必须回到当前仓库权威。

## 当前资产

- `rule-index.json`：B3 首轮派生规则索引；
- `targeted-evaluation-design.json`：C1 冻结的 9 个 A/B 场景与隐藏评分语料；
- `result-schema.json`：C2 固定的运行 / 人工评分结果结构；
- `fixtures/consumer-local-authority/`：C2 使用方本地权威最小夹具；
- `../query_rule_index.py`：B3/C1 派生索引查询器；
- `../run_rule_retrieval_ab.py`：C2 A/B 基线运行器。

## C2 静态校验

C2 不执行真正的 Agent A/B。运行：

```bash
python3 evals/run_rule_retrieval_ab.py --validate-only
```

静态校验至少确认：

1. C1 设计、61 项索引与当前 8 个规范性来源结构有效；
2. 所有 A 组声明的上下文文件和 Consumer fixture 均可解析；
3. 9 个 B query 的实际命中键 / 回退结果与 C1 冻结预期一致；
4. `RR-C1-08` 在临时副本中制造无语义内容身份漂移，并必须触发 `indexed_source_stale_or_missing`；
5. `RR-C1-01` 的项目级零命中必须触发 `no_indexed_rule_match`；
6. 运行时工作区不复制 `expected_behavior`、assertions、预期规则键或预期回退；
7. A/B 使用同一个场景 prompt，运行器只有显式 `--run` 才调用 Codex；
8. B 无回退时只物化查询返回源指针对应的当前规范性源章节 / 职责载体；回退时才加载 C1 声明的完整权威基线。

## C3 运行入口

只有进入 C3 后才执行：

```bash
python3 evals/run_rule_retrieval_ab.py --run
```

可定向运行场景：

```bash
python3 evals/run_rule_retrieval_ab.py --run --scenario RR-C1-02
```

默认同一次运行按相同 Codex 可执行文件、相同进程环境与相同题面依次执行 A / B；`--variant` 只用于诊断或经记录的定向重跑，不应被拿来伪装首次公平 A/B。

C1 要求 A/B 使用同一**实际模型与推理强度**。当前仓库没有可由本 runner 可靠强制的统一 Codex 模型配置契约，因此不得把“同一可执行文件 / 同一环境”自动等同于“实际模型已证明相同”。C3 必须从可取得的运行证据记录实际模型与推理强度；只有两侧能够证明一致的 A/B 对才可以进入效果比较。若当前运行时无法取得这些字段，应把该对记录为公平性证据不足，而不是推断相同。

每个运行时工作区都只包含该变体允许看到的上下文。隐藏答案只保留在仓库外部评分侧的 C1 设计语料中，不复制到 Agent 工作目录。

运行结果写入：

`evals/results/rule-retrieval/`

进程退出码只说明 Codex 进程是否正常结束。最终必须按 `result-schema.json` 和 C1 隐藏断言人工评分；查询器退出码 `2` 代表“需要回退”，也不等于 Agent 语义失败。

## B 组章节物化边界

B 组查询器返回 `source_pointer` 后，运行器从当前规范性源实时读取内容：

- `§N` / `§N.M` 指针按 Markdown 数字标题提取对应章节；
- `§N.M～§N.K` 按范围展开；
- Skill 职责契约等无法继续用数字章节缩小的独立载体复制当前完整文件；
- 物化文件带来源路径、章节和 blob identity 注释，但该注释只是 provenance，不成为规则权威；
- 当前指针粒度若导致某个章节仍包含额外邻近规则，其上下文噪声应在 C3 如实计量，而不是在 C2 为了美化 B 组偷偷重写规则或新增第二份摘要权威。
