# GPT-6 v3 Architecture Review Prompt

这是一个 **Fresh Context 独立架构评审**。

目标仓库：`dygapp/agentic-dev`

评审对象不是当前正式 Authority，而是临时评估分支中的候选：

`evals/rule-governance-v3/v3-candidate-review-package.md`

## 评审边界

1. Git Repository 当前 checkout 是唯一项目事实来源；不要使用其他聊天、个人记忆或未在仓库中出现的项目状态。
2. 不修改任何文件、Git 状态、Issue、PR 或外部资源；本次只读评审。
3. 候选文档是 review target，不是 Authority。判断冲突时，以当前仓库 `AGENTS.md` 及其 Authority hierarchy 为准。
4. 不重新设计一套全新的方法论。你的任务是识别候选中的真实结构缺陷、遗漏、兼容性风险、复杂度风险和 v1/v2 回归风险，并给出最小修正。
5. 不因为某种技术“可能更先进”就提出替换。只有能指出具体失败场景或长期维护风险时，才形成 finding。
6. 不把 Low / optional improvement 升级成阻塞项。

## 必须读取

至少读取：

- `AGENTS.md`
- `README.md`
- `docs/project/project-roadmap.md`
- `docs/project/rule-governance-knowledge-activation-v1.md`
- `docs/project/rule-governance-knowledge-activation-v2.md`
- `docs/project/consumer-local-activation-metadata-contract-v2.md`
- `docs/project/rule-ownership-decomposition-audit-v2.md`
- `docs/guides/rule-activation-guide.md`
- `docs/guides/using-agentic-dev.md`
- `docs/guides/consumer-local-rule-activation.md`
- `docs/guides/verification-evidence-rules.md`
- `docs/architecture/skill-architecture.md`
- `docs/architecture/skill-contracts.md`
- `skills/README.md`
- 至少两个当前核心 `SKILL.md`，其中必须包含 `skills/technical-plan/SKILL.md`
- `evals/rule-governance-v3/v3-candidate-review-package.md`

可以按需继续读取直接相关文件，但不要为了“保险”扫描整个仓库。

## 重点评审问题

必须逐项判断：

1. Front Matter → Generated Activation Index → semantic body 的三层边界是否真正保持单点 Authority？
2. source-local Front Matter 是否确实减少 manual Manifest 的双点维护，还是把重复转移到其他字段 / 文件？
3. Generic Markdown 与 Codex `SKILL.md` compatibility profile 是否可共存？特别检查 `name / description` 与 `metadata.agentic-dev.activation` 是否会形成两套漂移的 Skill activation semantics。
4. “哪些长期资源必须 / 应该有 Front Matter”的准入边界是否合理，是否会造成过度结构化或遗漏关键 Runtime resource？
5. “独立 activation unit 尽量对应独立文件”的规则是否会导致过度拆分；什么情况下需要 section-level selector，什么情况下必须拆文件？
6. Generated Index 的 source identity / stale / generator / validator 模型是否足以防止 v1 stale-index 类故障？
7. 自动重新生成 Index 是否可能让高风险 activation metadata 变化被静默接受？如果是，最小 review gate 应放在哪里？
8. `using-agentic-dev.md` 候选拆分是否完整、互斥、可发现；是否仍存在语义 owner 重叠或新 Mega-Guide？
9. `rule-activation-guide.md` 退出手工 Runtime mapping 后，human landing / Fresh Context discovery 是否仍足够？
10. `agentic-dev` self-adoption 是否真正复用了同一个 Repository-local core model，还是与 Consumer 仍有两套架构？
11. Consumer upstream adoption / provenance 应位于 source Front Matter、独立 adoption state、还是二者组合？候选是否清楚地区分了 ordinary runtime 与 upgrade-only history？
12. v1 / v2 已验证成果是否全部被保留；列出任何可能的行为回归。
13. Index 作为唯一 Current Discovery Mechanism 是否与 Codex 原生 Skill discovery 产生职责冲突？如果二者天然必须并存，应该怎样界定“一个 responsibility 一个 current mechanism”？
14. 是否存在比候选更简单的最小结构，能达到相同目标并显著降低长期维护成本？只在有具体依据时提出。
15. 候选哪些部分属于当前 v3 必须解决，哪些应该延后到真实证据出现后，避免过度设计？

## Severity 定义

### Blocking

如果不修复，则候选不能安全进入正式 v3 Milestone，例如：

- 会形成第二套 Authority；
- 核心 discovery 无法保持 current；
- 会破坏 Codex Skill 兼容性；
- 会导致 Consumer / agentic-dev 的关键 Authority precedence 错误；
- v1/v2 关键安全行为明显回退。

### Medium

不一定阻止概念成立，但在正式实施前必须解决，例如：

- 明确的双点维护；
- ownership 重叠；
- 可重复出现的 stale / missing failure；
- 迁移边界缺失；
- 会显著增加长期上下文或维护成本；
- self-adoption 与 Consumer model 表面统一、实际分叉。

### Low

不影响 v3 核心成立，可以在后续实现或证据驱动迭代中处理。

## Finding 要求

每个 Blocking / Medium 必须同时包含：

- `title`
- `design_goal_violated`
- `failure_scenario`
- `affected_components`
- `evidence_refs`
- `minimal_fix`

如果不能给出具体失败场景，不应标为 Blocking / Medium。

## 最终判定

只允许：

- `PASS`：没有 Blocking / Medium；候选可以进入正式 v3 Milestone 决策。
- `REVISE`：存在至少一个可通过有限修改解决的 Blocking / Medium。
- `REJECT`：核心模型本身存在结构性问题，有限修正不足以解决。

同时对以下维度分别给出结论：

- `front_matter_authoring_model`
- `generated_index_model`
- `guide_decomposition`
- `agentic_dev_self_adoption`
- `consumer_projection`
- `v1_v2_preservation`
- `complexity_control`

最终输出必须严格符合：

`evals/rule-governance-v3/review-output-schema.json`

不要输出 schema 之外的额外说明。