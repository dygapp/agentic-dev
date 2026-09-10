---
id: eval-rule-governance-v3-candidate-review-package
title: 规则治理与知识激活 v3 候选评审包
type: evaluation-candidate
status: review-only
version: "V0.2"
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
    - evals/rule-governance-v3/v3-governance-convergence-summary.md
    - evals/rule-governance-v3/v3-analysis-plan.md
    - evals/rule-governance-v3/gpt6-review-prompt.md
---

# 规则治理与知识激活 v3 候选评审包

## 1. 评审对象已重新定义

本文不是 v3 Final Design，而是对当前**治理方向与分析路线**的 Candidate Review Package。

Frozen base：

`agentic-dev@3c31ae96683c4a653f001402b889b40e87df976b`

当前评审不要求决定最终：

- Front Matter schema；
- Resource Index 格式；
- Manifest / Catalog 是否存在；
- 新 Skill 清单；
- Guide 最终文件数量；
- 目录命名；
- ADR 数量。

这些都必须建立在更上游的 ownership / lifecycle 结论上。

## 2. 为什么需要重新规划 v3

v1 证明结构化 discovery、最小规则集合与 fail-closed 有价值；v2 进一步证明 Consumer-local discovery、primary/supporting、routing-only/JIT Skill、baseline adoption 与 ordinary runtime local-only 可以成立。

但继续复核发现：当前真正的根因可能不在 discovery 技术，而在**知识与能力 ownership 被错误分类**。

典型演进路径曾逐渐变成：

```text
发现新的长期规则
→ 不应该扩大 Core Method
→ 不应该随意新增 / 修改 Skill
→ 进入 Guide
```

这个保护 Method / Skill 稳定性的动机合理，但最后一步把 Guide 变成了 catch-all bucket。

后果包括：

- `using-agentic-dev.md` 同时承担 human explanation、Consumer bootstrap、baseline adoption、ordinary runtime routing、Fresh Context recovery、project evolution 等不同职责；
- Repository-local Git / terminology 等规则物理位于 Guide，但语义上更像 Repository Standard；
- verification / external operation 等跨职责规则进入 Guide 后，可能与 existing Skill / Engineering Discipline / Repository Policy 重叠；
- 为了从大 Guide 中发现规则，又需要人工导航、rule-index、Manifest / Catalog 等派生机制；
- `agentic-dev` 自身还没有形成与 Consumer 一致的结构化 local discovery / Skill-centric runtime 模型。

因此 v3 需要先解决：

> **什么内容应该在哪里，由谁作为 semantic owner？**

而不是先回答：

> Manifest / Index 应该怎样实现？

## 3. 当前候选 Ownership Model

### 3.1 Method / Principle

拥有跨项目成立的开发生命周期、阶段和顶层不变量。

判断重点：

- 是否属于通用 lifecycle invariant；
- 是否必须约束 Skill architecture；
- 是否高于具体执行 capability。

不承担 Consumer-specific policy、平台细节或项目事实。

### 3.2 Skill

拥有稳定的 Agent procedural capability。

一个候选 Skill 应能够回答：

```text
何时进入？
输入是什么？
怎么做？
输出是什么？
什么时候退出？
何时 Stage Return？
何时 Escalate？
```

必须避免两个极端：

- Guide 中继续埋藏明显的 Agent workflow；
- 为了减少 Guide 数量，把每条规则都变成微型 Skill。

### 3.3 Repository-local Policy / Standard / Rule

拥有当前 Repository 持续适用的本地约束。

典型候选：

- Git Commit Standard；
- terminology / language Standard；
- Repository Operation / Integration Policy；
- Consumer-specific validation / review policy。

这类内容通常没有独立 Procedure，不应仅因为 Agent 需要遵守就 Skill 化。

它们也不应被当作人类 Guide 的普通说明；应成为 Repository-local Current Resource，由该 Repository 自行演进。

### 3.4 Project Authority Resource

拥有当前项目事实，例如：

- Requirement / Domain Authority；
- Specification；
- Architecture / ADR；
- Project Roadmap；
- Verification Strategy；
- durable Work Authority。

这些资源回答 `What is true?`，不能被 Skill / upstream Guide / generic reusable rule 覆盖。

### 3.5 Guide

候选边界：

> 面向人，以及 initialization / adoption / baseline upgrade 等低频 setup 场景，解释如何理解、选择、采用和升级 `agentic-dev`。

Guide 可以在低频 adoption 时完整读取，因此“Guide 较长”本身不是核心问题；核心问题是它是否错误进入 ordinary runtime，或承载了本应属于 Skill / Standard / Authority 的正文。

### 3.6 Research / Input / Evidence

原始需求、政策原文、研究报告、一次性分析、历史 Evidence 等不因为进入 Repository 就自动成为 Authority。

只有通过明确 adoption / promotion 才能形成前五类 Current Resource。

## 4. 当前 Guide 重分类假设

以下只是 V3-02 的待审计假设，不是最终迁移决定。

### `using-agentic-dev.md`

应主要保留：

- human-facing usage entry；
- new Consumer initialization orientation；
- existing Consumer baseline upgrade orientation；
- adoption / setup explanation。

应退出 Consumer ordinary runtime。

其中真实 Agent procedure 应回到 Skill / setup capability；Repository-local rule 应进入 Consumer-local Standard；Project fact 不应存在于 Guide。

### `git-commit-guidelines.md` / `terminology-guidelines.md`

虽然当前位于 `docs/guides/`，语义上更像 `Repository Standard / Rule`。是否移动路径、是否改名是后续实施问题；首先需要确认 semantic owner 类型。

### `verification-evidence-rules.md`

必须逐 rule-family 审计，不能继续假设“跨多个 Skill，所以统一放 Guide”。可能的 owner 包括：

- existing Skill；
- Skill supporting reference；
- Engineering Discipline / Verification Standard；
- platform-specific Skill；
- 真正的 reusable constraint。

### `external-operation-guidelines.md`

必须区分：

- reusable external operation procedure；
- Repository-specific authorization policy；
- platform-specific behavior。

### `rule-activation-guide.md`

当前职责→Guide/Skill/section 的人工映射表可能只是 ownership debt 下的过渡 Runtime Index。如果 native Skill discovery + structured Repository Resource discovery 足够，它可能应退出 Current Runtime；是否保留 human navigation 需后续判断。

### `consumer-local-rule-activation.md`

必须把 adoption-time explanation、ordinary runtime procedure、Consumer-local discovery / policy 分开判断，而不是默认整份 Guide local projection。

## 5. Consumer 生命周期候选

### 5.1 New Consumer initialization

初始化是一次 Repository Bootstrap / Adoption，不是整仓复制。

可能输入：

- candidate `agentic-dev` baseline；
- Consumer 当前 Repository 状态；
- 用户提供的原始需求 / 项目资料；
- runtime capabilities。

可能输出：

```text
Consumer-local Method / Skills
+ Consumer-local Repository Rules
+ Consumer Project Authority
+ explicit non-Authority inputs / research / evidence
```

### 5.2 Consumer-local Rules

初始化时可以基于 `agentic-dev` guidance 建立：

- `AGENTS.md`；
- terminology / language rules；
- Git rules；
- repository operation / integration rules；
- verification / review policy。

一旦形成，这些内容由 Consumer 自己拥有和演进。Upstream origin / provenance 不能取代 Consumer current authority。

### 5.3 初始化时存在原始需求

候选路径：

```text
Raw Requirement / Input
→ requirements analysis / clarify / specify
→ Consumer authoritative requirements
```

原始需求不会因被复制、带 metadata 或被 Agent 读取就自动成为 Requirement Authority。

### 5.4 初始化时没有原始需求

不预建空 Requirement / Architecture / ADR。

先建立足够继续工作的 Consumer-local governance / Method / Skill foundation；后续真实输入出现后，再用 Consumer-local method / Skill 逐步形成和完善 Requirement / Specification / Architecture 等 Authority。

### 5.5 Ordinary runtime

完成 adoption 后：

- local-only；
- 不默认读取 upstream `using-agentic-dev.md`；
- 不因 upstream latest 变化自动修改当前行为；
- 使用 Consumer-local Skill / Rule / Authority；
- upstream 只在显式 baseline upgrade、真实 capability gap、实验或 Consumer Authority 明确要求时重新进入。

### 5.6 Baseline upgrade

显式低频流程：

```text
Current Consumer state
+ previous evaluated baseline
+ candidate upstream baseline
→ read necessary upstream Method / Skill / Guide / reusable resources
→ adopt / retain / override / reject / supersede
→ persist Consumer-local Current Resources
→ validate
→ ordinary runtime local-only
```

upgrade-only history 不应成为 ordinary Fresh Context 输入。

## 6. Skill-centric Runtime 假设

当前需要 GPT-6 重点挑战的候选是：

```text
How Agent works?
→ Skill / native Skill discovery

What is true?
→ Project Authority Resource

What locally constrains work?
→ Repository Policy / Standard

How humans adopt / understand?
→ Guide
```

如果这个划分成立，v3 可能不再需要一个统一 Rule Activation System 管理所有对象。

可能的更简单结构：

```text
Task
├── procedural need
│   → native Skill discovery
│   → Skill
│
└── repository knowledge / constraints
    → structured local resources
    → minimal Resource Discovery
```

评审必须判断：

- 这是否真正减少 duplication；
- Repository-local policy 是否仍能可靠进入相关任务；
- native Skill discovery 是否足以承担 Skill routing；
- 是否需要额外 supporting-skill / cross-cutting constraint discovery；
- 如何保留 primary responsibility / supporting context / Stage Return 等 v2 成果。

## 7. AI-ready Resource Metadata：只冻结方向

当前不冻结 Front Matter schema，只保留以下候选原则：

- 长期由 Agent 反复定位的 Requirement / Architecture / Repository Standard 等资源适合 AI-ready Structured Markdown；
- YAML Front Matter 只用于 identity / classification / relations / routing，不承载正文事实；
- body 是 semantic owner；
- 原始需求 / Research / historical Evidence 默认不要求统一 schema；
- `SKILL.md` 保持平台原生 metadata compatibility；
- 是否需要统一 logical resource metadata contract 留到 V3-05；
- 是否需要 generated Resource Index 留到 V3-06。

因此下列原 v3 假设被明确降级，不再视为已决定：

```text
manual Manifest 必然由 generated Index 替代
所有长期资源必须统一 activation fields
Index 必须统一索引 Skill + Authority + Guide
Index 必须保存 source_identity
Guide 必须按独立 activation unit 拆文件
```

它们只能在后续分析证据支持时采用。

## 8. `agentic-dev` self-adoption

v3 最终必须解决 `agentic-dev` 自身的规则发现与激活，而不能只优化 Consumer。

但 self-adoption 的具体实现不能提前固定。

必须先回答：

- `agentic-dev` 自己有哪些 Repository-local Standards；
- Method / Principle 什么时候需要加载；
- native Skill discovery 能解决多少 procedural activation；
- README / Roadmap / Project Authority 如何进入 Fresh Context；
- 是否仍需要 Resource Index；
- `AGENTS.md` 需要保留哪些 always-on pointers；
- 如何避免再创建一个人工大导航 Guide。

## 9. ADR 边界

当前不创建正式 ADR。

只有当专项分析形成以下特征时才记录 ADR：

- 长期影响 Repository architecture；
- 有真实替代方案；
- 需要保存为什么选择 / 放弃某方案；
- 后续 Agent 不知道该决定容易重新打开已关闭选择。

高概率候选：

1. Repository Knowledge & Capability Ownership Architecture；
2. Skill-centric Runtime vs Guide/Rule-centric Runtime；
3. AI-ready Markdown + Resource Discovery architecture。

目录、文件名、字段名、Guide 数量等通常不值得 ADR。

## 10. v1 / v2 必须保留的安全成果

无论 v3 最终采用什么实现，都必须保护：

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

## 11. 分阶段分析路线

正式细化前采用：

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

完整任务边界见：

`evals/rule-governance-v3/v3-analysis-plan.md`

## 12. GPT-6 本轮真正需要回答的问题

本轮独立评审优先判断：

1. 当前是否正确识别了根因：ownership debt 是否比 discovery implementation 更上游；
2. 六类 ownership 是否足够且互斥，是否存在错误分类；
3. Guide 新边界是否合理；
4. Skill admission 是否能同时避免 Guide catch-all 与 Skill explosion；
5. Repository-local Standard 是否是必要独立类别；
6. Consumer initialization / baseline upgrade / ordinary runtime 的生命周期是否划分正确；
7. 原始需求存在 / 不存在的初始化路径是否合理；
8. ordinary runtime local-only 是否被正确保留；
9. `agentic-dev` self-adoption 是否被放在正确位置；
10. V3-01～V3-08 顺序是否避免 premature design；
11. 哪些当前“稳定判断”其实仍被过早冻结；
12. v1 / v2 哪些有效成果最容易在 ownership 重构中回退。

只有在这些问题成立后，才讨论：

- Front Matter；
- Resource Index；
- source identity；
- generator / validator；
- 新 Skill；
- physical Guide split。

## 13. 本轮非目标

GPT-6 不应在本轮：

- 给出完整最终目录树并要求立即采用；
- 决定最终 metadata schema；
- 决定最终 Index 格式；
- 要求立即实现 generator；
- 因某规则重要就要求新增 Skill；
- 把所有 Guide 删除；
- 修改 v2 历史 evidence；
- 修改 Consumer；
- 创建正式 ADR / Milestone。

## 14. 评审后 Gate

如果 GPT-6 返回 Blocking / Medium：

```text
finding
→ current model 二次核验 Repository evidence
→ 只修正成立的治理 / planning 缺陷
→ 必要时再次独立评审
```

如果不存在未解决 Blocking / Medium：

> 才进入是否正式建立 v3 Milestone 的人工路线决策；仍不直接进入具体实现。