# 规则治理 v2 Guide + Metadata 对照实验

本文件冻结 G-min 实验。它只属于 `evals/` 评估资产，不是 Repository Authority，也不修改正式 Method / Guide / Skill。

## 1. 实验问题

E-min 已证明：当运行时已经正确解析当前职责并直接激活 `technical-plan` Skill 时，GPT-5.6 与 GPT-6 都能在保持关键技术规划语义的前提下显著减少规则上下文扩散。

G-min 进一步回答：

> 如果不预先告诉 Agent 当前职责，也不直接激活 `technical-plan` Skill，而是把大型 Guide 投影成带最小 metadata 的小规则模块，并提供一个薄 Catalog，Agent 能否自行选择正确模块与后续 Authority / Skill，同时获得与 E-min 接近的质量和上下文收益？

## 2. 三组定义

### A — 当前 v1 Pilot

复用既有 `01-technical-design` 结果，不重跑。

### B — E-min Skill-first

复用既有 `01-technical-design-emin` 结果，不重跑。运行时已把当前职责解析为 `technical-planning`，并直接激活 `technical-plan`。

### C — G-min Guide + Metadata

继续使用完全相同的 `01-technical-design.md` 场景、同一模型与同一 reasoning effort。

C 组不会预先声明当前职责，也不会直接调用 `$technical-plan`。runner 只创建一个评估专用发现层：

1. 从当前 `docs/guides/using-agentic-dev.md` 按现有章节边界动态提取原文；
2. 为每个小模块添加 eval-only metadata；
3. 生成一个不包含规则正文的薄 Catalog；
4. Agent 先读取 Catalog，自行选择最小适用模块；
5. 模块可以指向现有 Skill / Authority；
6. 完整 Repository 仍可访问，遇到缺口、冲突或高影响未知边界时允许 fail-closed 扩展读取。

模块正文必须来自当前 Guide 原文，不手工改写规则；metadata 只是派生发现信息，不成为第二套 Authority。

## 3. 主要区别

E-min 测试：

```text
任务 → 已解析 responsibility → 直接激活 Skill
```

G-min 测试：

```text
任务 → metadata Catalog → Agent 自行判断 responsibility
     → 选择 Guide 模块 → 按需读取 Skill / Authority
```

因此 G-min 不是 E-min 的叠加版本，而是并列候选。二者可以共享现有 Skill，但发现路径必须不同。

## 4. 明确不做

本实验不：

- 修改正式 `using-agentic-dev.md`；
- 给全仓库增加 Front Matter；
- 把派生 Catalog 变成 Authority；
- Runtime 化现有 `rule-index`；
- 新增正式 Skill；
- 测试 Consumer-local 投射；
- 扩大到 02～05 场景。

## 5. 公平性

进入比较前必须满足：

1. A / B / C 使用同一个 `01-technical-design.md`；
2. 同一模型的 provider model 与 reasoning effort 可比较；
3. 正式 Method / Guide / Skill / Repository Authority 未改变；
4. C 组只新增 `evals/` 实验资产；
5. C 组完整 Repository 仍可访问；
6. C 不读取 A / B 或其他模型结果；
7. web search disabled；
8. sandbox read-only；
9. 进程成功不等于语义 PASS。

## 6. 预注册语义标准

继续沿用 E-min 已冻结的 10 条技术规划语义检查：

1. 正确识别当前任务需要 `technical-plan`；
2. Specification 继续定义 WHAT / WHY；
3. 长期 Technical Plan 只保留跨 Execution Unit 有持续协调价值的 HOW；
4. Architecture Context 只在跨当前功能持续有效的架构状态变化时更新；
5. ADR 不因进入 Technical Planning 自动创建；
6. 只有长期保留重要选择理由、权衡、替代关系或高成本架构决定时评估 ADR；
7. 单 Unit、低影响、可逆的局部决定留给 Execute；
8. 不因单次迁移制造缺乏长期价值的公共抽象；
9. Consumer 当前 Architecture / ADR / Code 等事实缺失时不得伪造；
10. Product Intent / Specification、架构权威或高影响授权存在缺口时必须返回 / 升级。

任一重大语义回归都足以否定 G-min。

## 7. 效率指标

Primary metric 继续使用：

`repository_command_output_bytes`

G-min 相对 A 至少下降 40% 才认为存在明确收益。

Secondary metrics：

- command execution count；
- input / cached / non-cached input tokens；
- output tokens；
- wall clock；
- 实际读取 Repository 文件；
- 选择的 metadata modules；
- 是否仍读取完整大型 Guide / Method / Skill Contracts；
- 是否触发 fail-closed。

## 8. 与 E-min 的比较

G-min 不要求绝对超过 E-min 才有价值，因为它承担了 E-min 没有验证的“职责发现”步骤。

如果同时满足：

- 语义 10/10 无重大回归；
- 相对 A 的主指标下降至少 40%；
- Agent 没有从 prompt 获得预解析 responsibility；
- 能通过 metadata 自行选择 `technical-planning` 相关模块并取得所需 Skill / Authority；

则判为 `SUPPORTS G-min`。

进一步若 G-min 的主指标收益与 E-min 差距不超过 20 个百分点，且没有明显增加错误停止 / Authority 混淆，可认为它对“自动职责发现”具有竞争力。

若 G-min 明显落后于 E-min，但仍超过 A，则说明 metadata 更适合成为 Skill-first 的补充发现层，而不是主运行时载体。

## 9. 后续解释边界

- `SUPPORTS G-min` 只支持继续研究 Guide 模块化 / metadata discovery，不等于应该正式拆分所有 Guide。
- G-min 优于 A 但弱于 E-min，优先考虑“Skill-first 主体 + metadata 补充”。
- G-min 失败时，不因此否定 E-min；二者测试不同问题。
- 只有职责发现仍不能可靠解决时，才重新提高 Runtime Index 的优先级。
