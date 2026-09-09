# 规则治理 v2 独立架构评估命题

这是一个 Fresh Context。

研究 Repository：

`dygapp/agentic-dev`

GitHub Repository 是唯一项目事实来源。不要依赖其他聊天、历史会话、个人记忆或本命题之外未经 Repository 验证的项目状态。

本轮只进行分析、研究和方案评估：

**不得修改 Repository，不得创建 PR，不得直接实施方案。**

## 一、上下文恢复

先从当前工作区重新确认当前分支 / 提交和 Repository Authority，并完整读取：

- `AGENTS.md`
- `README.md`
- `docs/project/project-roadmap.md`
- `docs/method/ai-development-method.md`
- `docs/architecture/engineering-capability-architecture.md`
- `docs/architecture/skill-architecture.md`
- `docs/architecture/skill-contracts.md`
- `docs/guides/using-agentic-dev.md`
- `docs/guides/rule-activation-guide.md`
- `docs/guides/external-operation-guidelines.md`
- `docs/research/rule-retrieval-design-reference.md`
- `docs/project/rule-governance-knowledge-activation-v1.md`
- `evals/rule-retrieval/README.md`

并按 Repository 当前可发现入口读取规则治理 v1 的主要验证证据。只把当前 Repository 支持的内容当作事实。

当前分支只允许存在 `evals/` 研究资产差异；这些研究文件不是 Repository Authority，也不能被当成 v2 已经批准或正在实施的证据。

## 二、待验证的问题

不要把下列描述直接视为结论。请先判断它们是否真实存在、严重程度如何，以及 v1 已经解决到什么程度。

规则治理 v1 已经围绕规则发现、最小正确规则集、source identity、stale detection、fail-closed、A/B Eval 和薄激活导航形成了结果。

现在需要进一步判断：如果派生 `rule-index` / 查询器主要是 `evals/` 评估资产，而 Agent 在真实生成阶段——例如需求分析、Specification、技术方案设计、Execution Unit 切分、Readiness、代码生成、Debug、Converge、GitHub / CI 操作——仍然需要读取大型 Guide 或大量规则文档，是否仍然存在：

1. 上下文过长；
2. 无关规则污染当前推理；
3. 关键规则没有在生成前及时激活；
4. Agent 在生成阶段反复犯错，只能在后续验证阶段发现；
5. Consumer 将 `agentic-dev` 方法、规则和 Skill 本地固化后，正常开发不再持续依赖 `agentic-dev`，但 Consumer-local 是否仍拥有等价规则发现 / 激活能力并不清楚。

必须明确区分：

- Eval Verification；
- Runtime Rule Discovery / Activation；
- Repository Authority；
- Derived Index / Catalog；
- Skill Runtime Responsibility；
- Consumer-local Authority。

## 三、候选方案

请独立评估以下候选，不预设任何一个方案正确，也允许组合或全部否定。

### A — Runtime Rule Index

把当前经过验证的 rule-index / retrieval 能力从纯 Eval 资产扩展为日常 Agent 推理前的 Runtime Rule Discovery。

至少评估：

- 是否有必要；
- 是否会制造新的运行基础设施；
- Authority 与 Derived Index 如何区分；
- stale index 如何处理；
- Consumer-local 如何实现；
- 是否真正降低上下文并改善生成质量。

### B — Guide Decomposition + Metadata

把大型 Guide 拆成较小规则模块；只对规则激活单元增加最小可机器识别 metadata，例如：

- scope
- responsibility
- conditions
- risk
- consumers
- source identity

通过薄 Catalog / Manifest 或其他机制，让 Agent 在读取正文前先过滤。

至少评估：

- 是否真正降低上下文；
- 是否只是把一个大文件变成大量小文件；
- Agent 如何在不扫描全部正文的情况下发现正确文件；
- metadata 与正文如何避免漂移；
- Catalog 是否应该是 derived；
- 是否适合 Consumer-local。

### C — Guide Rule Reduction + Existing Skill Ownership

审计 Guide 规则，把主要消费者明确属于现有 Skill 的规则通过“迁移 / 收敛”归入对应 Skill，而不是在 Guide 与 Skill 中复制完整语义。

至少覆盖：

- `clarify-intent`
- `specify`
- `technical-plan`
- `slice-work`
- `readiness-check`
- `execute-unit`
- `systematic-debug`
- `converge`
- `github-actions-verification`

至少评估：

- Skill 是否适合作为主要 Runtime Activation Unit；
- 哪些规则应该属于 Skill；
- 哪些规则绝不能下沉到单一 Skill；
- 如何防止 Skill 膨胀；
- 如何做到“一条规范性规则只有一个完整语义所有者”；
- 如何避免 Method / Guide / Skill 冲突与冗余。

### D — 新增专项 Skill

对于不能合理归入现有 Skill、但具备稳定独立职责的规则集合，评估是否应形成专项 Skill。

候选例子仅用于分析，不代表推荐：

- external operations；
- Consumer adoption / baseline upgrade；
- project bootstrap；
- code review。

必须依据真实职责判断：

- Trigger 是否稳定；
- Inputs / Outputs 是否清晰；
- Exit / Escalation 是否可定义；
- 是否需要独立上下文；
- 是否会造成 Skill 数量失控。

### E — 混合方案

允许组合：

- 极薄 Always-on Invariants；
- Skill Runtime Activation；
- 小型条件规则模块；
- metadata；
- thin Catalog；
- derived index；
- eval verification。

如果推荐混合方案，必须明确每一层职责，不允许形成新的“万能 Rule Activation Super Skill”或第二套 Authority。

### F — KEEP V1

评估不实施 v2 的实际代价。如果当前机制已经足够，必须明确建议停止，而不是为了架构完整性继续建设。

## 四、Consumer-local 单独分析

当前方法要求 Existing Consumer adoption / baseline upgrade 后：

- 选择性采纳通用 Method / Rule / Skill；
- 固化到 Consumer 自己的 Repository Authority；
- 普通开发恢复以 Consumer-local Authority 为主要入口；
- `agentic-dev` 不应成为日常运行依赖。

请独立回答：

1. 新 Consumer 如何获得规则发现 / 激活能力？
2. Existing Consumer baseline upgrade 时如何升级该能力？
3. Consumer 自己的长期规则发生变化时，什么变化需要更新激活信息？
4. Consumer 是否需要自己的 rule-index / catalog / metadata？
5. 如何避免 Consumer 与 `agentic-dev` 双重 Authority？
6. 如何保证 Consumer 不依赖上游 Repository 仍可以 Fresh Context 恢复并正确工作？

## 五、必须遵守的架构约束

任何推荐方案都必须满足：

1. Repository Authority 仍是唯一规范性事实来源；
2. 派生索引、Catalog、Manifest 不得成为第二套 Authority；
3. Progressive Disclosure；
4. Fresh Context 可恢复；
5. Consumer-local 可独立运行；
6. 不要求所有任务加载完整 Guide；
7. 关键生成阶段应在重要推理前取得适用规则；
8. 不为了规则治理制造过大的新基础设施；
9. 不机械增加 Skill；
10. 不让已有 Skill 无限膨胀；
11. 不复制同一规则的完整语义到多个位置；
12. source stale / conflict / unknown scope 必须 fail-closed；
13. v1 已有效的机制不得无证据推翻。

## 六、输出要求

### A. v1 诊断

明确分成：

- 已解决；
- 部分解决；
- 未解决；
- 当前证据不足。

每项结论引用当前 Repository 中的具体证据路径。

### B. 候选方案评分

对 A～F 至少按以下维度给 1～5 分并解释：

- 生成阶段规则激活效果；
- 上下文成本；
- 规则召回可靠性；
- 过度激活风险；
- Authority 清晰度；
- 长期维护成本；
- Skill 膨胀风险；
- Consumer-local 适配；
- stale / conflict 安全性；
- 实现复杂度。

评分高低方向必须解释清楚，例如“5 = 最优 / 风险最低”还是相反。

### C. 推荐架构

如果推荐 v2，给出：

- Runtime Activation Architecture；
- Rule Ownership Model；
- Method / Guide / Skill / Rule Module / Catalog / Index 的职责边界；
- Consumer-local 模型。

不要直接给出文件级实施清单。

### D. 风险分析

重点检查：

- 双重 Authority；
- Rule Drift；
- Skill Overloading；
- Metadata Drift；
- Catalog Drift；
- Context Fragmentation；
- Hidden Dependency；
- Consumer baseline coupling；
- 过度工程化。

### E. v2 最小实验设计

在修改正式架构前，设计最小实验，至少覆盖：

1. 复杂技术设计；
2. 文档分析 / Specification；
3. 代码生成；
4. Debug / Verification；
5. Consumer Fresh Context。

说明怎样比较当前 v1 与候选 v2，包括：

- token / context 成本；
- 必需规则召回；
- 无关规则加载；
- 生成阶段错误；
- 最终验证错误；
- Fresh Context 恢复质量。

### F. 最终决策

只能选择一个：

- `GO — 可以进入有限 v2 Milestone`
- `NO-GO — 当前证据不足`
- `KEEP V1 — 当前没有足够收益支持 v2`

并说明进入实施前还必须满足什么条件。

## 七、评估原则

这是架构研究，不是实施任务。

不要因为已有候选方案看起来合理就尝试调和所有方案。

允许明确否定方案。

优先寻找最小、可验证、可逆的改变。

不要把两个模型意见一致当成事实；最终仍要回到 Repository Evidence 和后续真实运行实验。