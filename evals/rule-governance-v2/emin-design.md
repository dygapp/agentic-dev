# 规则治理 v2 E-min 实验设计

本文件冻结下一步最小运行时激活实验。它只属于 `evals/` 评估资产，不是 Repository Authority，也不修改正式 Method / Guide / Skill。

## 1. 实验目的

当前 Pilot 已经取得两类证据：

1. GPT-6 Astra 与 GPT-5.6 Sol 对规则治理 v2 的独立架构评估均完成；
2. 两个模型都完成了当前 v1 下的 `01-technical-design` 生成阶段基线，并暴露出明显的仓库规则上下文扩散。

本实验不继续扩大 v1 场景覆盖，而只回答一个更有辨识力的问题：

> 如果运行时在复杂技术设计任务开始前，已经把当前职责精确解析为 `technical-plan`，并直接激活现有 `technical-plan` Skill，Agent 是否能在不降低技术规划语义质量的前提下，显著减少继续探索大型 Guide / Method / Contract 的上下文成本？

## 2. A / B 定义

### A — 当前 v1 Pilot 基线

复用已经完成的本地结果，不重跑：

```text
evals/results/rule-governance-v2/<model>/01-technical-design/
```

A 组使用原始 `01-technical-design.md` 场景，由 Agent 按当前正式 v1 使用方式自行恢复最小必要上下文。

### B — E-min Skill-first Runtime Activation

B 组仍使用同一个 `01-technical-design.md` 场景、同一模型、同一 reasoning effort、同一完整 Repository 内容。

唯一有意改变的是：在原始场景前增加一个**评估专用、非权威的运行时激活结果**：

```text
responsibility = technical-planning
primary activation unit = technical-plan
```

并显式调用：

```text
$technical-plan
```

B 组不会隐藏或删除任何 Guide / Method / Contract。完整 Repository 仍然可访问。

Agent 应先使用已经激活的 Skill 与任务中提供的 Consumer 事实；只有出现以下情况时才继续扩大规则读取：

- Skill 无法回答当前职责；
- 当前来源发生冲突；
- 当前任务暴露规范性缺口；
- 高影响、不可逆、重大架构、安全 / 隐私或授权边界无法确定。

如果扩大读取，必须在最终输出中说明触发了什么 fail-closed 原因。

因此，本实验测量的是“正确运行时激活是否减少无必要规则探索”，不是“通过把文件藏起来强制减少上下文”。

## 3. 本轮明确不验证

E-min **不**验证以下候选：

- Runtime Rule Index；
- Guide 全量拆分；
- metadata / Catalog；
- 新增专项 Skill；
- Consumer-local 投射；
- 正式修改 `rule-activation-guide.md`；
- 正式把 Guide 规则迁移到 Skill。

只有 Skill-first E-min 仍不足时，才有证据继续增加复杂机制。

## 4. 公平性约束

A / B 进入效果比较前必须满足：

1. `01-technical-design.md` 原始场景内容一致；
2. 同一比较对使用相同 provider model；
3. reasoning effort 均为 `high`；
4. A 与 B 之间正式 Method / Guide / Skill / Repository Authority 没有语义变化；
5. B 分支相对 A 运行 Head 的变化只能属于 `evals/` 实验资产；
6. B 不能读取 A 组结果或其他模型结果；
7. web search 禁用；
8. sandbox 为 `read-only`；
9. 进程成功不等于语义 PASS。

如果 provider model / reasoning effort 不一致，或 A→B 之间出现 `evals/` 以外的仓库变化，该模型对标记为不可比较。

## 5. 预注册语义检查

人工评分时，B 至少必须保持 A 已经表现出的以下关键语义：

1. 正确判断当前任务需要 `technical-plan`；
2. Specification 继续定义 WHAT / WHY，Technical Plan 不得重定义产品意图；
3. 长期 Technical Plan 只保留跨 Execution Unit 有持续协调价值的 HOW 决策；
4. Architecture Context 只在形成跨当前功能持续有效的架构状态变化时更新，不能把全部 Technical Plan 等同于 Architecture Context；
5. ADR 是条件性产物，不因进入 Technical Planning 自动创建；
6. 需要长期保留重要选择理由、权衡、替代关系或高成本长期架构决定时才评估 ADR；
7. 单 Unit、低影响、可逆的局部实现决定应留给后续执行，而不是提前冻结；
8. 不因为单次迁移创建缺乏长期价值的公共抽象；
9. Consumer 当前 Architecture / ADR / Code 等真实状态缺失时，不得伪造事实；需要时应保留条件或指出后续必须取得的本地 Authority；
10. 若发现 Product Intent / Specification、架构权威或高影响授权缺口，应按现有职责返回 / 升级，不得静默填补。

任一重大语义回归都足以否定当前 E-min，即使 token 明显下降。

## 6. 预注册效率指标

### Primary metric

`repository_command_output_bytes`

定义为 `codex exec --json` 中所有已完成 `command_execution` 的 `aggregated_output` UTF-8 字节总和。

该指标直接衡量 Agent 为恢复 / 搜索 Repository 规则而实际拉入运行轨迹的 shell 输出量，比累计 token 更接近本实验的“规则上下文扩散”问题。

E-min 的预注册目标：

> 在语义无重大回归的前提下，B 相对 A 的 `repository_command_output_bytes` 至少下降 **40%**。

### Secondary metrics

同时记录但不单独决定通过：

- `command_execution_count`；
- cumulative `input_tokens`；
- `cached_input_tokens`；
- non-cached input tokens；
- output tokens；
- wall-clock；
- 实际读取文件；
- 是否读取完整 `using-agentic-dev.md`、完整 Method、完整 Skill Contracts 等大型来源；
- 是否触发 fail-closed 扩展读取。

累计 token 会受 Codex 会话轮次、缓存和 provider 行为影响，因此只作为辅助指标，不与 shell 规则上下文输出等同。

## 7. 判定规则

### SUPPORTS E-min

只有同时满足：

- 两个模型 B 组关键语义均无重大回归；
- 两个模型 runtime facts 可比较；
- 两个模型 `repository_command_output_bytes` 均相对各自 A 组下降至少 40%；
- 未通过隐瞒 Repository 文件取得该下降；
- 没有因 Skill-first 产生新的 Authority 混淆或错误停止。

该结论只表示：

> “把正确的现有 Skill 作为生成阶段主要 Runtime Activation Unit”值得进入下一轮有限设计。

它**不**等于规则治理 v2 已经可以正式实施。

### INCONCLUSIVE

任一情况成立：

- 只有一个模型达到效率目标；
- provider / reasoning effort 无法公平比较；
- 语义质量难以可靠评分；
- B 频繁需要 fail-closed 回到完整规则栈，但原因尚不能分类。

### REJECT E-min

任一情况成立：

- B 出现重大语义回归；
- Authority / Stage Return / ADR / Architecture Context 边界明显错误；
- 上下文下降不足以抵消新增运行机制；
- 正确结果依赖评估 prompt 中人工塞入规则正文，而不是 Skill 自身与现有 Authority。

## 8. 后续分支条件

只有 E-min 获得支持后，才评估：

1. 如何让 Runtime 自动识别正确 Skill，而不是由实验 runner 预先指定；
2. 哪些 Guide 规则应真正迁移到现有 Skill；
3. 哪些跨职责 / 条件规则仍需要薄模块；
4. 是否需要 metadata / Catalog；
5. Consumer-local 如何获得同样的激活能力。

如果 E-min 被否定，不继续因为既有假设而强推 Skill-first，应回到候选方案 A～F 重新比较。
