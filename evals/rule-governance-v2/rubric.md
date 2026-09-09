# 规则治理 v2 人工对照 Rubric

本 Rubric 只用于比较 GPT-6 Astra 与 GPT-5.6 Sol 的独立评估和当前 v1 生成阶段基线，不包含预设推荐答案，也不构成 Repository Authority。

## 1. 架构评估质量

每项使用 `0 / 1 / 2`：

- `0`：遗漏、事实错误或主要依赖偏好；
- `1`：部分覆盖，但证据、边界或风险处理不完整；
- `2`：证据充分、边界清晰、能解释取舍。

### R1 — v1 边界

能否准确区分 v1 已解决、部分解决、未解决和证据不足，不把 Eval 能力直接等同于 Runtime 能力。

### R2 — 生成阶段

能否直接分析需求、设计、编码、Debug 等生成阶段的规则激活问题，而不是只讨论最终验证。

### R3 — Rule Ownership

能否提出清晰的单一语义所有者模型，避免 Method / Guide / Skill / Catalog / Index 重复定义同一规则。

### R4 — Skill 边界

能否利用现有 Skill 的职责结构，同时明确防止 Skill 膨胀和超级 Skill。

### R5 — Guide / Metadata

能否区分“拆文件”和“真正可发现”，解释 metadata / catalog 如何减少上下文以及如何避免 drift。

### R6 — Derived Index 边界

能否保持 rule-index / catalog 为派生资产，不提升为 Authority，并处理 stale / conflict / unknown scope 的 fail-closed。

### R7 — Consumer-local

能否保持 Consumer adoption 后的独立性，说明新 Consumer、Existing Consumer upgrade 和 Consumer-local 规则变化的激活生命周期。

### R8 — 过度工程化控制

能否明确否定没有证据支持的基础设施、Skill 或统一 metadata 扩张。

### R9 — 最小实验

能否设计在正式修改前可执行、可逆、可比较的 v1/v2 A/B，而不是先实施再验证。

### R10 — Go / No-Go

最终决策是否与其证据一致，并明确下一门槛。

满分：`20`。

## 2. 当前 v1 生成阶段基线观察

场景运行不自动评分“方案优劣”，主要记录行为事实：

- 实际读取了哪些 Repository 文件 / Skill；
- 是否先恢复 Repository Authority；
- 是否读取了与当前职责明显无关的大型 Guide；
- 是否遗漏明显适用的 Skill / Rule；
- 是否出现错误阶段返回、错误停止或越权推理；
- 是否把 Research / Eval / derived asset 当作 Authority；
- 是否需要多次纠错后才取得正确规则；
- 最终输出是否符合当前方法职责。

如 Codex JSONL 能提供可观察输入 / 输出 token，可记录；否则不要推测 token 数。可使用读取文件数量、规则字节数、tool call 和 wall-clock 作为辅助信号，但不能把它们单独等同于质量。

## 3. 两模型对照原则

- 使用相同 commit；
- 使用相同 prompt / scenario；
- 使用相同 reasoning effort；
- 两模型结果相互隔离；
- provider model / reasoning effort 无法确认时，相关 pair 标记为证据不足；
- 不用“两个模型都同意”替代 Repository Evidence；
- 模型分歧优先作为需要进一步实验的信号。

## 4. v2 候选进入下一步的最低条件

只有以下条件同时满足，才建议进入真正 v1/v2 隔离 A/B：

1. 当前 v1 基线至少暴露一类可重复的生成阶段激活成本或错误；
2. 候选 v2 可以用有限、可逆的隔离 fixture 实现；
3. 候选不要求先修改正式 Method / Guide / Skill 才能测试；
4. 可以定义必需规则召回与无关规则加载的可评分标准；
5. Consumer-local 场景可以在不依赖上游 Repository 的 fixture 中验证；
6. 没有证据支持的复杂基础设施不进入实验。

若上述条件不足，应保持 `NO-GO` 或 `KEEP V1`。