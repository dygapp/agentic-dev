# 规则检索 A/B 基线实现与静态校验

记录日期：2026-09-09

阶段：**规则治理与知识激活 v1 / 阶段 C / C2 — A/B 基线实现与静态校验**

文档性质：**研究 / 评估证据**

基线：

`master@364d23bee5f3505c46e29a13d353de954c216a56`

本文记录 C2 对 C1 已冻结 A/B 设计的可重复执行基线与静态验证，不执行真正的 Agent A/B，也不形成“B 优于 A”的效果结论。

## 1. C2 实现

C2 新增：

- `evals/run_rule_retrieval_ab.py`：A/B 基线运行器；
- `evals/rule-retrieval/result-schema.json`：进程、检索与人工评分结果结构；
- `evals/rule-retrieval/fixtures/consumer-local-authority/`：最小 Consumer-local Authority fixture；
- `evals/rule-retrieval/README.md`：运行、评分和来源物化边界。

运行器默认只执行静态校验：

```bash
python3 evals/run_rule_retrieval_ab.py --validate-only
```

只有显式使用：

```bash
python3 evals/run_rule_retrieval_ab.py --run
```

才进入 C3 Codex 新上下文运行。因此 C2 不会因为普通验证命令意外提前执行 Agent A/B。

## 2. A / B 上下文装配

### A — 文件级粗粒度基线

A 直接复制 C1 `a_context_paths` 声明的当前职责相关整份规范性文档 / fixture。

它不是“全仓库上下文”，也没有为了让 B 更容易胜出而故意弱化。

### B — 条件检索与安全回退

B 首先使用当前 `rule-index.json` 与 `query_rule_index.py`：

1. 校验当前 8 个规范性来源 identity；
2. 执行 C1 冻结的稀疏 query；
3. 无回退时，根据返回 `source_pointer` 从**当前规范性源**实时物化匹配章节 / 独立职责载体；
4. 来源陈旧、查询值未建模、必要维度未知或零可靠命中时，停止信任派生索引和临时来源视图，重新从**当前 Repository Authority**装配 C1 已声明的完整基线；
5. Consumer-local fixture 始终作为 Consumer 项目事实保留，不由上游规则索引替代。

物化文件只增加来源路径、章节和 blob identity provenance 注释；派生内容仍不是新的规则权威。

当前源指针若只能定位到较宽的整个章节，C2 不为了降低 B 的上下文成本重新发明更细摘要。该噪声属于 C3 应如实测量的原型结果。

## 3. 隐藏答案与实验提示隔离

C2 最终实现不会向 Agent 暴露：

- `expected_behavior`；
- `assertions`；
- `b_expected_rule_keys`；
- `b_expected_fallback` / `b_expected_fallback_reason`；
- `metric_focus`；
- A / B 分组身份。

`runtime-input.json` 只包含场景 ID 与允许读取的上下文列表。

A / B prompt 使用同一场景正文；差异只来自该变体允许读取的上下文，不使用“你是 A 组 / B 组”等实验提示影响 Agent 行为。实际 `--run` 使用的临时目录前缀也不包含 A / B 标识，避免 Codex 从当前工作目录侧信道观察到分组身份；分组只保留在运行器外部控制和运行后的结果记录中。

## 4. 控制 fixture

### Consumer-local Authority

`fixtures/consumer-local-authority/` 明确：

- Consumer Repository 是项目事实与本地方法权威；
- 精确 `agentic-dev` baseline 只供明确 baseline upgrade 使用；
- 当前工作是普通功能开发，不执行 baseline upgrade；
- 不把 `agentic-dev` 自身项目状态复制成 Consumer 项目事实。

该 fixture 是评估输入，不代表任何真实 Consumer Repository。

### 无语义来源漂移

`RR-C1-08` 不持久化第二份规范性源。运行器在临时目录复制当前索引的活动来源，并只给 `using-agentic-dev.md` 追加一个换行，制造内容 identity 漂移；查询必须在筛选前返回：

```text
fallback_required = true
fallback_reason = indexed_source_stale_or_missing
```

最终实现进一步保证：一旦发生 fallback，Agent 可见的所有声明规则上下文必须重新从当前 Repository Authority 装配。静态校验会把 fallback 后的工作区文件逐项与当前 Authority / 当前 fixture 做字节级比较，避免临时 stale-root 中的同名陈旧文件继续被消费。

## 5. 结果结构

`result-schema.json` 固定区分：

- Agent 进程退出；
- B 查询命中 / 回退；
- 人工语义断言评分；
- 权威混淆、误停 / 误升级、误执行；
- 可取得的文件 / 工具 / token / 时间指标；
- 失败分类。

运行器在 C3 进程结束后只生成 `grading_status=pending` 的结果骨架，不自动把退出码 0 解释成语义 PASS。

## 6. 模型与推理强度公平性

C1 要求 A / B 使用同一实际模型与推理强度。

当前仓库没有可由本 runner 可靠强制并证明的统一 Codex 模型配置契约。因此 C2 只保证：

- 同一 runner；
- 同一 Codex 可执行文件；
- 同一进程环境；
- 同一场景任务正文；
- 同类隔离工作区和外部权限边界。

这些事实**不自动证明**实际模型 / reasoning effort 相同。

C3 必须从可取得的真实运行证据记录两侧实际模型与推理强度；无法证明一致的 A/B 对不得进入效果比较。结果骨架中的 `model` / `reasoning_effort` 因此默认保持 `null`，不会用环境变量或请求配置冒充实际执行事实。

## 7. 真实静态执行证据

为满足 C2“验证 runner 命令可执行”门禁，PR #84 使用一次性、只读 GitHub Actions workflow 执行：

```bash
python3 -m py_compile evals/query_rule_index.py evals/run_rule_retrieval_ab.py evals/run_codex_evals.py
python3 evals/run_rule_retrieval_ab.py --validate-only
```

工作流权限只有 `contents: read`，未使用 secrets，也从未执行 `--run`。每次取得证据后均从候选分支删除，不进入长期仓库结构。

### 7.1 首轮实现验证

Run：`34291536760`

Job：`102278939797` (`validate`)

结果：**success**。

该轮验证了 runner、fixture、结果结构与最初 C2 输入能够执行。随后 C2 继续完成项目状态闭环并修正 AGENTS 派生来源 identity，因此该运行不作为最终输入面的验证依据。

### 7.2 状态闭环后的复跑

Head：`698e3a8567c9618247c70dfefdbde0be112aea14`

Run：`34296037510`

Job：`102292773126` (`validate`)

结果：**success**。

该轮已经覆盖更新后的 AGENTS identity 和当时的 C2 输入，但最终差异级 AI 复核发现一个中等级缺口：`RR-C1-08` 检测到来源陈旧后虽然正确返回 fallback，fallback 工作区对 stale-root 中已经存在的同名规范性源仍会优先复制陈旧副本。也就是说，旧静态校验验证了“需要回退”，却没有验证“回退后的 Agent 上下文确实来自当前 Authority”。

因此该运行被后续修订取代为祖先诊断证据，不作为最终 C2 PASS。

### 7.3 fallback 来源修正复跑

修订内容：

- fallback 后所有规则上下文显式从 `ROOT` 当前 Repository Authority 装配；
- 新增静态断言：B fallback 后每个声明上下文文件必须与当前 Authority / 当前 fixture 字节一致；
- 不改变 C1 场景、61 项索引覆盖、规则关系或 Guide / Skill 语义。

验证输入 Head：

`96eb5f356383bfb54ec5bd99e76f48f74d7ec01c`

Run：`34296395675`

Job：`102293842203` (`validate`)

结果：**success**。

该轮确认 fallback 来源修正和 9 场景静态装配有效。随后最终差异复核又识别到运行环境侧的实验身份泄漏风险：实际 `--run` 临时目录前缀仍包含 `-A-` / `-B-`，Codex 可能通过当前工作目录观察到分组。因此该 Head 继续作为 fallback 修正证据，但不作为最终 runner 的完整静态基线。

### 7.4 最终 runner 静态复跑

运行目录已改为中性前缀：只包含场景 ID，不包含 A / B 分组；分组仍保留在运行器外部结果标识中。

最终验证输入 Head：

`3adb250cdfb3fe904c6a601aedb9d14017f22ab8`

Run：`34297156461`

Job：`102296153284` (`validate`)

结果：**success**。

日志明确记录：

```text
C2 静态校验通过：9 个场景的 A/B 工作区均可装配。
隐藏答案和 A/B 分组未进入 runtime-input；B 查询与 C1 冻结命中 / 回退一致。
未执行 Agent A/B；真正的新上下文运行与人工语义评分属于 C3。
```

该运行覆盖当前最终 runner 的 Python 编译、C1 设计 / 索引校验、9 场景 A/B 工作区装配和 fallback Authority 字节一致性断言。A/B 运行目录中性由最终 runner 差异直接复核；C2 没有为了验证该路径而提前执行真实 Agent A/B。

该运行之后只删除一次性 workflow，并更新本研究证据 / PR 元数据；如果 runner、query、索引、fixture、AGENTS 或 C1 A/B 场景输入中的任一项再次变化，必须重新验证，不得机械复用当前 PASS。

## 8. 当前结论

C2 已满足：

- A / B 隔离装配可重复；
- 9 个 B query 的命中 / 回退预期可机器校验；
- Consumer-local 与 stale-source 控制可以生成；
- stale / unknown / no-match fallback 后重新从当前 Repository Authority 装配规则上下文；
- 静态校验直接验证 fallback 工作区内容与当前 Authority / fixture 一致；
- 隐藏答案、评分关注点和 A/B 分组不进入 Agent 可见运行时文件；
- 实际 Codex 工作目录不包含 A / B 分组标识；
- A / B 使用相同任务正文，实验差异只来自允许读取的规则上下文；
- 查询回退、进程退出与人工语义评分分层；
- runner 默认不会执行 C3；
- 最终 runner 的 `py_compile` 与 `--validate-only` 已在真实 GitHub Actions 中成功执行；
- 临时静态验证 workflow 已删除，不建立新的长期自动化依赖。

本证据仍**不证明 B 比 A 更可靠或成本更低**。真正的行为效果、实际模型 / 推理强度一致性和人工断言评分必须在 C3 完成。
