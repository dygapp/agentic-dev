---
id: eval-rule-governance-v3-governance-convergence-summary
title: 规则治理与知识激活 v3 治理收敛总结
type: evaluation-summary
status: review-only
version: "V0.1"
classification:
  - rule-governance
  - knowledge-ownership
  - consumer-lifecycle
relations:
  upstream:
    - AGENTS.md
    - docs/project/rule-governance-knowledge-activation-v2.md
    - docs/project/rule-ownership-decomposition-audit-v2.md
    - docs/architecture/skill-architecture.md
  related:
    - evals/rule-governance-v3/v3-analysis-plan.md
    - evals/rule-governance-v3/v3-candidate-review-package.md
---

# 规则治理与知识激活 v3 治理收敛总结

## 1. 文档性质

本文只在临时评估分支中固化当前已经形成的治理判断，用于防止继续讨论导致上下文增长后丢失关键结论。

本文不是 `agentic-dev` 正式 Method、Architecture、Guide、Skill、ADR 或 Project Authority；不授权修改 `master`，也不代表 v3 已正式立项。

Frozen base：

`agentic-dev@3c31ae96683c4a653f001402b889b40e87df976b`

## 2. 当前问题重新定义

v1 / v2 主要从“如何让 Agent 更高效发现和激活规则”出发。当前复核认为，在继续设计 Manifest、Catalog 或 Index 之前，必须先处理更上游的问题：

> `agentic-dev` 演进中新增的长期内容是否被放在了正确的 semantic owner 中？

当前风险不是单纯缺少更好的检索技术，而是多类不同性质内容被集中到 Guide，导致：

- Guide 逐渐成为不能修改 Method / Skill 后的默认接收桶；
- Agent procedural capability 与人类说明混在一起；
- Repository-local 规范与 reusable capability 混在一起；
- Consumer initialization / baseline upgrade / ordinary runtime 生命周期混在一起；
- 为了从混杂 Guide 中发现规则，又逐步引入 rule-index、Manifest、Catalog 或人工导航表；
- discovery complexity 被 ownership debt 放大。

因此 v3 的第一原则是：

> **先纠正知识与能力的归属，再决定需要什么发现机制。**

## 3. 当前稳定的内容所有权模型

当前候选采用六类资源，其中前五类可能成为长期 Current Resource，最后一类主要作为输入 / 证据。

### 3.1 Method / Principle

回答：

> 通用 AI 驱动开发生命周期、阶段、顶层不变量是什么？

特征：

- 跨项目成立；
- 定义稳定方法语义；
- 高于 Skill 实现；
- 不因单个 Consumer 或平台特殊情况扩张。

### 3.2 Skill

回答：

> Agent 在一个稳定、可复用职责中应该怎样工作？

典型特征：

- 有明确 trigger / Use When / Do Not Use；
- 有输入；
- 有稳定 Procedure；
- 有输出；
- 有 Exit / Stage Return / Escalation；
- 可被多个项目复用；
- 适合按需加载，而不是普通上下文常驻。

不是每条规则都应成为 Skill。只有形成独立可复用流程的能力才 Skill 化。

### 3.3 Repository-local Policy / Standard / Rule

回答：

> 当前 Repository 中，所有相关工作持续必须遵守什么本地约束？

典型例子：

- Git Commit Standard；
- 术语 / 中文表达 Standard；
- 主导语言规则；
- Repository Operation / Integration Policy；
- Consumer-specific coding / review / validation policy。

这类资源通常：

- 不是一个独立执行流程，因此不适合 Skill；
- 不是项目业务事实，因此不属于 Requirement / Architecture；
- 应由当前 Repository 自己拥有并演进；
- 可以由 `AGENTS.md` 保留极薄指针或通过稳定 Resource Discovery 发现，但正文不应复制进 `AGENTS.md`。

当前 `docs/guides/git-commit-guidelines.md`、`docs/guides/terminology-guidelines.md` 虽然物理上位于 `guides/`，语义上更接近这一类，需要在 V3-02 中重新分类，而不是先按目录名决定身份。

### 3.4 Project Authority Resource

回答：

> 当前项目事实是什么？

包括但不限于：

- Requirement；
- Domain Authority；
- Specification；
- Architecture Authority；
- ADR；
- Project Roadmap；
- Verification Strategy；
- durable Work / Execution Authority。

这些事实属于 Consumer / 当前 Repository，不属于 reusable Skill，也不能被 upstream Guide 或 Skill 覆盖。

### 3.5 Guide

Guide 的候选新边界：

> **面向人，以及 initialization / adoption / baseline upgrade 等低频 setup 场景，解释如何理解、选择和采用 `agentic-dev`。**

Guide 可以比 ordinary runtime resource 更详细，因为其完整读取通常只发生在低频初始化或升级过程中。

Guide 不应成为：

- Agent ordinary runtime 的主要 procedural owner；
- Repository-local policy 的默认载体；
- Project Authority 的事实载体；
- 不愿修改 Method / Skill 时新增规则的默认接收桶。

`using-agentic-dev.md` 应重点按这个边界重新审计。当前结论不是机械拆成更多 Guide，而是先把不属于 Guide 的内容迁回正确 owner。

### 3.6 Research / Input / Evidence

包括：

- 原始需求；
- 政策 / 标准原文；
- 客户附件；
- 研究报告；
- 一次性分析；
- 历史 Eval / Evidence；
- 会议或调查输入。

它们可以进入 Repository，但不会因为存在、被读取或带 metadata 就自动成为 Authority。只有经过当前 Repository 的采用 / 提升流程，才可能形成前述 Current Resource。

## 4. Guide 边界的当前判断

### 4.1 `using-agentic-dev.md`

当前候选定位应收敛为：

- Human-facing landing / usage guide；
- new Consumer initialization entry；
- existing Consumer baseline upgrade entry；
- adoption / setup 场景的解释性说明。

它不应作为 Consumer ordinary runtime dependency，也不应该因为 Consumer 已完成 adoption 就继续被 Consumer `AGENTS.md` 日常引用。

其中如果存在稳定 Agent procedure，应迁移到既有 Skill、Engineering Discipline、Repository Standard，或在满足 Skill admission 时形成新的 setup/adoption Skill；如果只是解释采用关系，则继续留在 Guide。

### 4.2 其他 Guide

当前 `docs/guides/*` 不能再按“文件在 guides 目录，所以就是 Guide”处理。V3-02 必须逐项做 semantic ownership audit。

特别需要重新审计：

- `verification-evidence-rules.md`：其中各 rule family 可能分别属于现有 Skill、Engineering Discipline / Standard、平台 Skill 或真正的跨职责 reusable constraint；
- `external-operation-guidelines.md`：需要区分 reusable external-operation procedure、Repository-specific authorization policy、平台专项 Skill；
- `rule-activation-guide.md`：当前人工职责→文档映射可能只是 v2 的过渡 discovery surface；ownership 修正后是否仍需要必须重新论证；
- `consumer-local-rule-activation.md`：其中 adoption-time、runtime procedure、Consumer-local policy / discovery contract 应重新分流。

## 5. Consumer 生命周期边界

### 5.1 Initialization

初始化 Consumer 不是简单复制文件，而是一次 Repository Bootstrap / Adoption。

输入可以包括：

- candidate `agentic-dev` baseline；
- 用户提供的原始需求 / 项目资料；
- 当前 Consumer Repository 事实；
- 当前运行环境能力。

初始化可能形成：

1. Consumer-local Method / adopted Skills / Engineering Capability；
2. Consumer-local Repository Rules：AGENTS、术语、Git、语言、集成 / 验证等；
3. Consumer Project Authority：Requirement、Specification、Architecture、Roadmap 等；
4. 输入 / Research / Evidence 的明确非 Authority 边界。

初始化后，Consumer-local rules 与 Authority 由 Consumer 自己拥有和继续演进。`origin` 不等于 current authority。

### 5.2 原始需求存在时

如果初始化时用户提供原始需求：

```text
Raw Requirement / Input
→ requirements analysis / clarify / specify
→ Consumer authoritative requirements
```

不直接把原始文件视为 Requirement Authority。

权威需求应面向 Agent 持续消费，采用结构化正文与适当的资源 metadata；Front Matter 只负责定位 / 路由，正文承载真实需求事实。

### 5.3 原始需求不存在时

不为了模板完整创建空 Requirement / Architecture / ADR。

先建立足够继续工作的 Consumer-local governance / Method / Skill foundation；后续真实需求出现时，再通过 Consumer-local Method / Skill 逐步形成并完善权威需求和其他 Project Authority。

### 5.4 Ordinary runtime

完成 initialization / adoption 后：

- Consumer ordinary runtime 只依赖 Consumer-local Current Resources；
- 不日常读取 `agentic-dev` Guide；
- upstream 新提交不会自动改变 Consumer 当前行为；
- Skill / local policy / Project Authority 按 Consumer Repository Authority 工作。

### 5.5 Baseline upgrade

baseline upgrade 是显式、低频操作：

```text
Current Consumer local state
+ previous evaluated upstream baseline
+ candidate upstream baseline
→ 读取必要 upstream Method / Skill / Guide / reusable resources
→ classify adopt / retain / override / reject / supersede
→ 更新 Consumer-local Current Resources
→ 验证
→ ordinary runtime 再次 local-only
```

upgrade history 与 rejected decision 不进入普通 Fresh Context。

## 6. AI-ready Markdown 的当前稳定判断

当前只冻结原则，不冻结具体 schema：

1. 长期由 Agent 反复定位和消费的 Authority / Repository Rule 等 Markdown，应考虑统一 YAML Front Matter；
2. Front Matter 只承载 identity、classification、relations、routing 等 metadata，不承载规范事实正文；
3. Body 是 Requirement / Architecture / Policy 等真实语义的唯一正文 owner；
4. 原始需求、Research、历史 Evidence 等默认不要求统一模板；
5. `SKILL.md` 必须保持平台原生 Skill metadata compatibility，不能为了统一普通文档 schema 破坏 Skill Runtime；
6. 是否采用统一逻辑 metadata contract、何种 Resource Index、是否需要 source identity projection，留到 V3-05 / V3-06 细化。

## 7. Discovery 的当前稳定判断

现在不再预设 v3 必须采用“大而统一的 Activation Index”。

候选分工是：

```text
How Agent works?
→ native Skill discovery / Skill

What is true / what constrains this Repository?
→ AI-ready Repository Resources
→ minimum Resource Discovery
```

需要多少 Index、是否 YAML/JSON、是否生成、是否需要对 Skill 做二次索引，都必须在 ownership audit 完成后再决定。

当前禁止先实现：

- 新 Manifest；
- 新 Catalog；
- 新 Rule Index；
- Front Matter generator；
- Rule Super Skill / Stage Router Skill；
- 因讨论而机械新增一批 Skill。

## 8. ADR 使用边界

当前不把整个 v3 讨论写成一个大 ADR。

ADR 只在后续专项分析形成具有长期后果、存在真实替代方案、需要保留选择理由与权衡的决定后创建。

当前高概率 ADR 候选：

- Repository Knowledge & Capability Ownership Architecture；
- Skill-centric Runtime vs Guide/Rule-centric Runtime（若 V3-04 最终形成明确架构取舍）；
- AI-ready Markdown + Generated Resource Index（仅当 V3-05 / V3-06 最终证明需要并形成替代方案取舍）。

不应因目录命名、字段名、Guide 文件数量等局部实现选择创建 ADR。

## 9. v1 / v2 需要保留的成果

v3 不应把前两轮有效结论全部推翻。至少继续保护：

- Thin Bootstrap；
- Repository / Consumer Authority first；
- Progressive Disclosure；
- Evidence before claims；
- semantic owner 单点正文；
- derived discovery 不拥有规范正文；
- stale / missing / ambiguity fail-closed；
- primary responsibility 与 supporting context 分离；
- routing-only 不机械加载完整 Skill；
- Skill 在真正进入职责时 JIT load；
- Stage Return 后重新判断；
- Consumer ordinary runtime local-only；
- baseline adoption 逐项 adopt / retain-or-override / reject / supersede；
- 一个 discovery responsibility 不并行保留多个 Current derived mechanisms。

## 10. 当前未决问题

以下问题刻意不在本总结中提前决定：

- 哪些现有 Guide 内容具体迁往哪个 owner；
- 是否需要新增 setup / adoption / verification Skill；
- `using-agentic-dev.md` 最终保留哪些 section；
- Repository Rule / Standard 的目录和命名；
- 哪些长期资源必须 Front Matter；
- Front Matter 最终 schema；
- Skill metadata 是否需要额外 `agentic-dev` extension；
- 是否需要 Resource Index；
- Index 是否 generated、采用 YAML 还是 JSON；
- source currentness 应由哪些检查负责；
- `agentic-dev` self-adoption 的最终 bootstrap path。

这些问题必须按 `v3-analysis-plan.md` 分阶段处理，不能在同一轮大设计中一次性冻结。

## 11. 当前 Gate

在进入任何正式 v3 实施前，至少应完成：

```text
Governance Summary
→ Ownership Model
→ Current Repository Audit
→ Consumer Lifecycle
→ Skill Reclassification
→ AI-ready Resource Model
→ Minimal Discovery Architecture
→ agentic-dev Self-Adoption Design
→ Consumer Validation Design
→ Independent AI Review
→ 必要 ADR / Formal v3 Authority
```

当前评估分支只允许推进到独立评审准备与结果收敛，不授权修改 `master` 或建立正式 v3 实现。