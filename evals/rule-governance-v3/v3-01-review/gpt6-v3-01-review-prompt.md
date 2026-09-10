# V3-01 知识与能力所有权模型独立复核

这是一个 **Fresh Context、只读、独立一致性复核**。

目标仓库：`dygapp/agentic-dev`

正式候选提交：

`8504d1b2fcb5a834de75279f4ec7dfc81af70119`

对应 Draft PR：#100

当前 checkout 额外包含本评估目录中的只读评估资产；这些评估资产不是正式候选，也不是 Repository Authority。

## 1. 任务

判断 V3-01 候选是否已经形成足够清晰、互斥度合理且可实际应用的知识与能力所有权模型，使后续 V3-02 可以据此开展全仓语义审计。

本次不是重新设计 v3，也不是评审 Front Matter、Index、Manifest、Catalog 的具体实现。

必须重点验证：

1. “语义所有者”与“适用范围 / 来源状态”“运行 / 生命周期角色”“载体 / 权威形式”是否真正解耦；
2. 适用范围与来源状态是否被正确视为可以同时成立的正交字段；
3. 工程纪律、技术画像、验证画像是否能够稳定归入可复用工程能力，而不会被迫技能化或仓库本地化；
4. 仓库本地规范与上游可复用能力能否稳定区分；
5. Guide 是否已经退出“不属于核心方法 / 技能”的兜底角色；
6. 新技能准入是否足够严格，能够抑制 one-rule-one-Skill；
7. 混合文档是否能够被识别为需要按规范正文拆分，而不是被迫文件级单分类；
8. Architecture / Contract 等载体是否不会被误判为平行语义所有者；
9. Consumer 初始化、采用、升级和普通运行的所有权关系是否与 v2 的 Consumer-local ordinary runtime 相容；
10. v1 / v2 已验证的 Authority-first、渐进式披露、失败关闭、JIT Skill、单点正文、Consumer-local ordinary runtime 等行为是否被保留。

## 2. 必须读取

先确认当前 Git checkout 中可以解析正式候选提交，然后至少读取候选提交对应的：

- `AGENTS.md`
- `README.md`
- `docs/project/project-roadmap.md`
- `docs/project/rule-governance-knowledge-activation-v3.md`
- `docs/project/knowledge-capability-ownership-model-v3.md`
- `docs/method/ai-development-method.md`
- `docs/method/principles.md`
- `docs/architecture/engineering-capability-architecture.md`
- `docs/architecture/skill-architecture.md`
- `docs/architecture/skill-contracts.md`
- `docs/architecture/engineering-disciplines.md`
- `docs/architecture/technology-profile-contract.md`
- `docs/guides/using-agentic-dev.md`
- `docs/guides/git-commit-guidelines.md`
- `docs/guides/terminology-guidelines.md`
- `docs/guides/verification-evidence-rules.md`
- `docs/guides/external-operation-guidelines.md`
- `skills/technical-plan/SKILL.md`
- `skills/execute-unit/SKILL.md`

不要默认扫描整个仓库。

## 3. Holdout 一致性测试

以下资源没有作为 V3-01 候选文档中的主要代表判例给出最终答案。请使用 V3-01 的判断流程独立分类：

1. `AGENTS.md`
2. `README.md`
3. `docs/project/ai-review-guidelines.md`
4. `docs/architecture/engineering-capability-architecture.md`
5. `docs/decisions/method-decisions.md`
6. `skills/github-actions-verification/SKILL.md`
7. `tasks/README.md`
8. `docs/research/llm-wiki-rule-governance-fit-analysis.md`
9. `docs/project/project-roadmap.md`
10. `docs/project/rule-governance-knowledge-activation-v2.md`

对每个资源输出：

- 主要语义所有者；
- 适用范围；
- 来源状态；
- 生命周期角色；
- 载体 / 权威形式；
- 是否混合多个规范正文；
- 置信度；
- 简短理由；
- 如果模型本身无法稳定分类，明确指出歧义来自哪里。

允许一个文件被判定为“混合正文，需按语义拆分”。不要为了满足表格而强行指定单一所有者。

## 4. 严重程度

### Blocking

如果不修复，V3-01 不应成为 V3-02 的分类依据。例如：

- 语义所有者本身有结构性缺口；
- 两个核心类别无法在现实资源上稳定区分；
- 结果会形成第二套 Authority；
- 会破坏 Consumer-local ordinary runtime 或 v1/v2 关键安全边界。

### Medium

核心方向仍可成立，但在进入 V3-02 前必须修复。例如：

- 规则会系统性地产生两种同样合理的分类；
- scope / provenance / lifecycle / representation 仍被混为同一身份；
- Guide 或 Skill admission 仍有可重复的 ownership 漏洞；
- 代表资源能分类，但 holdout 出现可重复的中等级歧义。

### Low

不影响 V3-02 使用，可以后续优化的表达、示例或局部完整性问题。

每个 Blocking / Medium 必须给出：

- 标题；
- 被违反的设计目标；
- 现实失败场景；
- 受影响组件；
- 证据引用；
- 最小修复。

不能给出现实失败场景时，不得标为 Blocking / Medium。

## 5. 判定

只允许：

- `PASS`：Blocking=0 且 Medium=0，模型足以进入 V3-02 所有权审计；
- `REVISE`：存在可以有限修正解决的 Blocking / Medium；
- `REJECT`：所有权模型本身结构性不可用，需要重新设计。

即使 `PASS`，也不授权：

- V3-02 物理迁移；
- PR #100 合并；
- Skill 重构；
- discovery / metadata 实现；
- Consumer Repository 修改。

最终输出必须严格符合：

`evals/rule-governance-v3/v3-01-review/v3-01-review-output-schema.json`
