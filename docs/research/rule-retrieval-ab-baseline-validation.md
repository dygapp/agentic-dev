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
4. 来源陈旧、查询值未建模、必要维度未知或零可靠命中时，读取 C1 已声明的完整 Authority 基线；
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

A / B prompt 使用同一场景正文；差异只来自该变体允许读取的上下文，不使用“你是 A 组 / B 组”等实验提示影响 Agent 行为。

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

回退后若需要读取不属于首轮索引的 Authority，例如 `docs/project/ai-review-guidelines.md`，运行器从当前仓库读取，而不是错误要求临时 stale-root 包含全部 Repository Authority。

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

工作流权限只有 `contents: read`，未使用 secrets，也从未执行 `--run`。取得证据后均从候选分支删除，不进入长期仓库结构。

### 首轮实现验证

Run：`34291536760`

Job：`102278939797` (`validate`)

结果：**success**。

该轮验证了 runner、fixture、结果结构与最初 C2 输入能够执行。随后 C2 继续完成项目状态闭环并修正 AGENTS 派生来源 identity，因此该运行不再作为最终输入面的唯一验证依据。

### 最终输入面复跑

AGENTS 状态闭环完成后，其当前 blob identity 变为：

`0bd04757c64e6eda6a7ba00e04eca40e92651c29`

`rule-index.json` 的 `PTR-AGENTS-EXT` 已刷新到该 identity；61 项索引覆盖、关系与规则语义未改变。随后在 Head：

`698e3a8567c9618247c70dfefdbde0be112aea14`

重新执行相同静态验证。

Run：`34296037510`

Job：`102292773126` (`validate`)

结果：**success**。

日志明确记录：

```text
C2 静态校验通过：9 个场景的 A/B 工作区均可装配。
隐藏答案和 A/B 分组未进入 runtime-input；B 查询与 C1 冻结命中 / 回退一致。
未执行 Agent A/B；真正的新上下文运行与人工语义评分属于 C3。
```

该复跑覆盖最终 runner、query、索引、fixture、AGENTS identity 与 C1 设计输入。验证通过后只删除临时 workflow，并更新本研究证据 / PR 元数据；这些后继变化不被 `--validate-only` 消费，也不改变 runner、query、索引、fixture、AGENTS 或任何 A/B 场景输入，因此该祖先验证证据仍适用于最终 C2 集成候选。若这些被验证输入中的任一项再次变化，必须重新运行，不得机械复用当前 PASS。

## 8. 当前结论

C2 已满足：

- A / B 隔离装配可重复；
- 9 个 B query 的命中 / 回退预期可机器校验；
- Consumer-local 与 stale-source 控制可以生成；
- 隐藏答案、评分关注点和 A/B 分组不进入 Agent 可见运行时文件；
- A / B 使用相同任务正文，实验差异只来自允许读取的规则上下文；
- 查询回退、进程退出与人工语义评分分层；
- runner 默认不会执行 C3；
- 最终输入面 `py_compile` 与 `--validate-only` 已在真实 GitHub Actions 中成功执行；
- 临时静态验证 workflow 已删除，不建立新的长期自动化依赖。

本证据仍**不证明 B 比 A 更可靠或成本更低**。真正的行为效果、实际模型 / 推理强度一致性和人工断言评分必须在 C3 完成。
