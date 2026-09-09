# 规则检索与激活 A/B 评估

本目录保存“规则治理与知识激活 v1”阶段 C 的规则检索 / 激活评估资产。

这些文件属于 `evals/` 评估资产，**不是 Repository Authority**。删除它们不会删除任何规范性规则；所有行为判断仍必须回到当前仓库权威。

## 当前资产

- `rule-index.json`：B3 首轮派生规则索引；
- `targeted-evaluation-design.json`：C1 冻结的 9 个 A/B 场景与隐藏评分语料；
- `result-schema.json`：C2/C3 运行与人工评分结果结构；
- `fixtures/consumer-local-authority/`：C2 使用方本地权威最小夹具；
- `../query_rule_index.py`：B3/C1 派生索引查询器；
- `../run_rule_retrieval_ab.py`：C2 A/B 装配与静态校验 runner；
- `../run_rule_retrieval_c3.py`：C3 真实隔离运行与 provider model / reasoning effort 证据采集 runner。

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
7. A/B 使用同一个场景 prompt；
8. B 无回退时只物化查询返回源指针对应的当前规范性源章节 / 职责载体；回退时重新加载 C1 声明的当前完整权威基线。

`run_rule_retrieval_ab.py --run` 是 C2 实现阶段保留的早期诊断入口，**不得再作为 C3 可评分运行入口**，因为它不能为同一次实际 turn 提供足够的 provider model / reasoning effort 事实证据。

## C3 Readiness 静态校验

运行：

```bash
python3 evals/run_rule_retrieval_c3.py --validate-only
```

该命令不会调用 Codex。它在 C2 静态装配基础上继续确认：

- C3 结果 schema 已包含请求值、provider / turn 运行时事实与 A/B 配对公平性字段；
- runtime-facts 解析器能区分 `observed` / `ambiguous` / `unavailable`；
- provider model 与客户端 turn model 不会被混为同一个事实；
- 只有单一、可观察的 provider model 与主 turn reasoning effort 才允许进入比较。

## C3 真实运行入口

真正 C3 使用：

```bash
python3 evals/run_rule_retrieval_c3.py \
  --run \
  --model <model> \
  --reasoning-effort <effort>
```

可定向运行一个或多个场景：

```bash
python3 evals/run_rule_retrieval_c3.py \
  --run \
  --scenario RR-C1-02 \
  --model <model> \
  --reasoning-effort <effort>
```

C3 scored run 不提供单独 `--variant` 入口；每个选中场景都连续执行 A、B 两侧，避免把定向单侧诊断伪装成首次公平 A/B。

### 模型 / 推理强度证据

C1 要求 A/B 使用同一**实际模型与推理强度**。请求参数和客户端解析值本身都不能证明 provider 最终返回的模型，因此 C3 分层记录：

- `requested_model` / `requested_reasoning_effort`：传给 Codex 的共同请求值；
- `client_turn_model`：Codex 主 turn span 中的客户端解析模型，仅作诊断；
- `model`：Responses SSE `response.created` / `response.completed` 中 provider 返回的 `response.model`；
- `reasoning_effort`：同一主 turn span 的 `codex.turn.reasoning_effort`；
- `runtime_facts_status`：`observed` / `ambiguous` / `unavailable`；
- `pair_fairness_status`：`comparable` / `insufficient` / `mismatch`。

每次 Codex run 都设置独立 `log_dir`，并继续使用 `--ephemeral --json`。由于 `codex exec` 默认只启用 error 级日志，C3 只对该隔离子进程显式设置：

```text
RUST_LOG=error,codex_core=info,codex_api::sse::responses=trace
```

用途严格限定为运行时事实取证：

- stdout JSONL 保存行为轨迹与主 thread ID；
- SSE trace 提供 provider `response.model`；
- turn span 提供客户端 turn model 与 reasoning effort；
- trace 既可能出现在 stderr，也可能进入显式 `log_dir`，runner 会在同一次隔离进程的两处取并集；
- 临时工作目录和 log 目录名称都不包含 A/B 分组；
- 如果 provider model、reasoning effort 或客户端 turn 事实出现多值，标记 `ambiguous`；
- 如果 provider model 或 reasoning effort 无法取得，标记 `unavailable`；
- 若任一侧不是 `observed`，配对标记为 `insufficient`；
- 若 A/B 两侧观察到的 provider model / reasoning effort 不一致，标记为 `mismatch`；
- 只有 `comparable` 的配对才可进入效果比较。

这里的 provider `response.model` 仍是服务端返回的标识，不是模型权重的密码学证明；它满足本阶段“不能用请求值冒充实际服务模型”的证据边界。

当前做法属于阶段 C 的评估运行时证据适配，不改变长期 Method / Guide / Skill，也不把 Codex trace 格式固化为通用方法依赖。若 Codex 后续把 provider model 与 reasoning effort 作为正式结构化 `exec --json` / session API 暴露，应重新评估并优先迁移到正式接口。

### 隔离与隐藏答案

每个运行时工作区只包含该变体允许看到的上下文。Agent 不看到：

- `expected_behavior`；
- assertions；
- 预期规则键 / 回退；
- `metric_focus`；
- A / B 分组身份。

A/B 使用同一场景正文，差异只来自允许读取的规则上下文。C3 进一步固定：

- `--sandbox read-only`；
- `approval_policy="never"`；
- `web_search="disabled"`。

因此评估不依赖外部检索，也不会由 Agent 修改工作区。

运行结果写入：

`evals/results/rule-retrieval/`

每侧保留：

- `<scenario>-<variant>.jsonl`；
- `<scenario>-<variant>.stderr.txt`；
- `<scenario>-<variant>.runtime-facts.json`；
- `<scenario>-<variant>.result.json`。

`runtime-facts.json` 只保存线程 ID、事实来源类别和观察到的模型 / effort 值集合，不复制完整 trace。完整临时 log_dir 随隔离工作区销毁；这些结果目录继续属于本地 / 临时评估证据，不进入长期 Git 权威。

进程退出码只说明 Codex 进程是否正常结束；A/B fairness `comparable` 也只说明比较条件成立。最终必须按 `result-schema.json` 和 C1 隐藏断言人工评分，进程成功与公平性成立都不等于 Eval PASS。

## B 组章节物化边界

B 组查询器返回 `source_pointer` 后，运行器从当前规范性源实时读取内容：

- `§N` / `§N.M` 指针按 Markdown 数字标题提取对应章节；
- `§N.M～§N.K` 按范围展开；
- Skill 职责契约等无法继续用数字章节缩小的独立载体复制当前完整文件；
- 物化文件带来源路径、章节和 blob identity 注释，但该注释只是 provenance，不成为规则权威；
- 当前指针粒度若导致某个章节仍包含额外邻近规则，其上下文噪声应在 C3 如实计量，而不是为了美化 B 组偷偷重写规则或新增第二份摘要权威。
