# GPT-6 v3 Governance / Architecture Review Prompt

这是一个 **Fresh Context 独立治理与架构评审**。

目标仓库：`dygapp/agentic-dev`

Frozen base：

`3c31ae96683c4a653f001402b889b40e87df976b`

评审对象不是当前正式 Authority，而是临时评估分支中的三个候选输入：

- `evals/rule-governance-v3/v3-governance-convergence-summary.md`
- `evals/rule-governance-v3/v3-analysis-plan.md`
- `evals/rule-governance-v3/v3-candidate-review-package.md`

## 1. 评审边界

1. Git Repository 当前 checkout 是唯一项目事实来源；不要使用其他聊天、个人记忆或未在仓库中出现的项目状态。
2. 不修改任何文件、Git 状态、Issue、PR 或外部资源；本次只读评审。
3. 三份 v3 文档都是 review-only candidate，不是 Authority。冲突时以当前 `AGENTS.md` 及其 Authority hierarchy 为准。
4. 本轮首先评审 **knowledge / capability ownership 与 Consumer lifecycle**，不是先优化 Manifest / Index / Front Matter 技术实现。
5. 不重新设计完整方法论。只有能指出真实失败场景、ownership conflict、生命周期污染、回归或明显过度设计时才形成 Blocking / Medium。
6. 不因为某种架构“更先进”就建议采用；Low / optional improvement 不升级成阻塞项。
7. 不把“Guide 应减少”机械推导成“新增更多 Skill”；新 Skill 必须满足当前 Skill Architecture 的 admission 边界。
8. 不把目录名当 semantic owner。`docs/guides/*` 中的文件可能实际属于 Standard、Skill support、Guide 或其他类型。

## 2. 必须读取

至少读取：

- `AGENTS.md`
- `README.md`
- `docs/project/project-roadmap.md`
- `docs/method/ai-development-method.md`
- `docs/method/principles.md`
- `docs/architecture/skill-architecture.md`
- `docs/architecture/skill-contracts.md`
- `docs/project/rule-governance-knowledge-activation-v1.md`
- `docs/project/rule-governance-knowledge-activation-v2.md`
- `docs/project/rule-ownership-decomposition-audit-v2.md`
- `docs/project/consumer-local-activation-metadata-contract-v2.md`
- `docs/guides/using-agentic-dev.md`
- `docs/guides/consumer-local-rule-activation.md`
- `docs/guides/rule-activation-guide.md`
- `docs/guides/verification-evidence-rules.md`
- `docs/guides/external-operation-guidelines.md`
- `docs/guides/git-commit-guidelines.md`
- `docs/guides/terminology-guidelines.md`
- `skills/README.md`
- 至少两个当前核心 `SKILL.md`，其中必须包含 `skills/technical-plan/SKILL.md`
- `evals/rule-governance-v3/v3-governance-convergence-summary.md`
- `evals/rule-governance-v3/v3-analysis-plan.md`
- `evals/rule-governance-v3/v3-candidate-review-package.md`

可以按需继续读取直接相关文件，但不要为了“保险”扫描整个仓库。

## 3. 第一优先级：Ownership Model

逐项判断以下候选类别是否必要、互斥、可操作：

1. Method / Principle；
2. Skill；
3. Repository-local Policy / Standard / Rule；
4. Project Authority Resource；
5. Guide；
6. Research / Input / Evidence。

必须回答：

- 是否缺少必要类别；
- 是否有两个类别仍会竞争同一 semantic body owner；
- 是否存在无法稳定分类的大量现实内容；
- Repository-local Standard 是否真有必要独立于 Guide / Skill；
- “不属于 Method / Skill”是否还可能继续自动滑入 Guide；
- 当前分类是否能解释 `git-commit-guidelines.md`、`terminology-guidelines.md`、`verification-evidence-rules.md`、`external-operation-guidelines.md` 的真实身份。

## 4. 第二优先级：Guide / Skill 边界

重点挑战：

### Guide 候选边界

Guide 主要服务：

- 人类理解；
- Consumer initialization；
- adoption；
- baseline upgrade；
- 其他低频 setup / orientation。

Guide 不应默认成为 Consumer ordinary runtime procedural owner。

判断这个边界是否过窄或过宽。

### Skill 候选边界

Skill 拥有稳定 Agent procedure，并应有明确：trigger、input、procedure、output、exit / return / escalation。

判断：

- 当前 Guide 中是否有明显应该回到 existing Skill 的内容；
- 是否有真实 new Skill candidate；
- 是否更适合 Skill supporting reference 而不是新 Skill；
- 怎样避免 Guide catch-all 与 Skill explosion 两个极端。

不要仅给抽象建议。Blocking / Medium 必须引用当前文件的具体语义。

## 5. 第三优先级：Consumer Lifecycle

逐项评审：

```text
new Consumer initialization
existing Consumer adoption
explicit baseline upgrade
ordinary runtime
explicit upstream re-entry / capability gap
```

必须检查：

- `using-agentic-dev.md` 在 initialization / upgrade 时完整读取是否合理；
- adoption 后 ordinary runtime 是否应完全退出 upstream Guide；
- Consumer-local terminology / git / repository policies 是否应由 Consumer 自己拥有和演进；
- upstream origin / provenance 是否会错误地继续承担 Current Authority；
- initialization 时有原始需求，先分析形成 Consumer authoritative requirements 是否合理；
- initialization 时没有原始需求，不创建空 Requirement / Architecture 是否合理；
- 后续需求是否能通过 Consumer-local Method / Skill 逐步形成；
- baseline upgrade 是否能在完成后重新回到 local-only ordinary runtime。

## 6. 第四优先级：分析顺序与 ADR Gate

评审 V3-01～V3-08：

```text
V3-01 Ownership Model
→ V3-02 Current Repository Audit
→ V3-03 Consumer Lifecycle
→ V3-04 Skill Reclassification
→ V3-05 AI-ready Resource Model
→ V3-06 Minimal Discovery Architecture
→ V3-07 agentic-dev Self-Adoption
→ V3-08 Consumer Validation
```

判断：

- 顺序是否存在错误依赖；
- 是否应该合并 / 拆分某个分析任务；
- 是否还有必须先于 metadata / discovery 的分析；
- 当前是否过早要求 GPT-6 决定最终技术方案；
- ADR 应在哪些分析结果形成后再创建；
- 哪些候选 ADR 实际不值得单独记录。

## 7. 第五优先级：v1 / v2 Preservation

必须明确列出重构过程中最容易丢失的有效成果，至少检查：

- Thin Bootstrap；
- Repository / Consumer Authority first；
- Progressive Disclosure；
- Evidence before claims；
- single semantic body owner；
- derived discovery non-authoritative；
- stale / missing / ambiguity fail-closed；
- primary responsibility + supporting context；
- routing-only 不机械加载完整 Skill；
- JIT Skill activation；
- Stage Return 后重新路由；
- Consumer ordinary runtime local-only；
- per-item baseline adoption；
- superseded / rejected content 不继续进入 Current Runtime；
- 一个 discovery responsibility 不并行保留多个 current derived mechanisms。

如果某个 v3 候选判断会破坏这些成果，应形成 finding。

## 8. 只有前述判断成立后，才评审 Metadata / Discovery Hypothesis

当前只把以下内容视为**后续候选方向**，不是已经决定：

- Authority / Repository Standard 等长期 Agent-consumed Markdown 可使用 YAML Front Matter；
- Front Matter 只承载 identity / classification / relations / routing，正文承载真实语义；
- `SKILL.md` 保持平台原生 metadata compatibility；
- ownership 修正后再判断是否需要 generated Resource Index；
- native Skill discovery 与 Resource Discovery 可以分责；
- `rule-activation-guide.md` / v2 Manifest 是否退出 Current Runtime，要等 V3-06 决定。

重点回答：

- 这些假设是否仍然被过早冻结；
- ownership 修正后是否可能只需要更简单的目录 / Authority Map；
- 是否存在必须提前解决的 metadata compatibility risk；
- 是否有理由现在就要求统一 Index 管理 Skill + Authority + Guide（默认答案不应是假定“是”）。

## 9. `agentic-dev` Self-Adoption

必须判断 v3 把 self-adoption 放在 V3-07 是否合理。

检查：

- 是否应该先完成 ownership / skill / resource model 再 self-host；
- 是否能避免 `agentic-dev` 与 Consumer 两套 runtime model；
- 是否存在 `agentic-dev` 特有 Repository-local policy 导致 Consumer 模型不能直接复用；
- self-adoption 验证应覆盖哪些代表性任务。

## 10. Severity

### Blocking

如果不修复，治理 / 分析路线不能安全进入正式 v3 Milestone。例如：

- ownership model 会制造新的双 Authority；
- Guide / Skill 边界结构性错误；
- Consumer ordinary runtime 会重新依赖 upstream；
- 分析顺序会在关键前提未完成前冻结实现；
- 明显破坏 v1 / v2 已验证安全行为。

### Medium

正式立项前必须解决的有限问题，例如：

- 类别存在可重复 ownership overlap；
- Guide 边界仍让大量 procedural rule 无家可归；
- Consumer lifecycle 有明确污染路径；
- V3 子任务依赖顺序不正确；
- ADR Gate 或 preservation contract 缺失；
- 当前候选仍提前冻结了不必要的 metadata / discovery 决策。

### Low

不影响 v3 治理与分析路线成立，可留待对应 V3 子任务处理。

## 11. Finding 要求

每个 Blocking / Medium 必须同时包含：

- `title`
- `design_goal_violated`
- `failure_scenario`
- `affected_components`
- `evidence_refs`
- `minimal_fix`

如果不能给出具体失败场景，不应标为 Blocking / Medium。

## 12. 最终判定

只允许：

- `PASS`：当前治理总结与分阶段分析路线不存在未解决 Blocking / Medium，可以进入是否正式建立 v3 Milestone 的人工决策；这不等于最终 v3 Architecture PASS。
- `REVISE`：存在可通过有限修改解决的 Blocking / Medium。
- `REJECT`：ownership / lifecycle / planning 核心模型本身存在结构性问题，有限修正不足以解决。

最终输出必须严格符合：

`evals/rule-governance-v3/review-output-schema.json`

不要输出 schema 之外的额外说明。