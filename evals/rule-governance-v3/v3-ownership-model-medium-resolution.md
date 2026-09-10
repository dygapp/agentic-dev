---
id: eval-rule-governance-v3-ownership-medium-resolution
title: 规则治理 v3 Ownership Medium Finding 修订说明
type: evaluation-resolution
status: review-only
version: "V0.2"
classification:
  - rule-governance
  - knowledge-ownership
  - engineering-capability
relations:
  upstream:
    - evals/rule-governance-v3/v3-governance-convergence-summary.md
    - evals/rule-governance-v3/v3-analysis-plan.md
    - evals/rule-governance-v3/v3-candidate-review-package.md
    - docs/architecture/engineering-capability-architecture.md
    - docs/architecture/engineering-disciplines.md
    - docs/architecture/technology-profile-contract.md
  related:
    - evals/rule-governance-v3/gpt6-medium-rereview-prompt.md
---

# 规则治理 v3 Ownership Medium Finding 修订说明

## 1. 性质

本文只用于临时评估分支中的定向复评，不是 `agentic-dev` 正式 Authority，也不授权实施 v3。

首轮 GPT-6 治理评审结论为 `REVISE`，唯一 Medium finding 是：

> 六类 ownership 模型没有为 Engineering Discipline、Technology Profile、Verification Profile 这类“跨项目可复用、但不具备独立任务流程”的长期工程能力明确归属。

该 finding 经当前 Repository Authority 复核后成立。

本文件是该 finding 的最小修订层。在定向复评中，如果它与 V0.1 的三份候选文档冲突，以本文为准；正式 v3 Milestone 如获批准，应把通过后的结论重新合并进正式候选 / Architecture，而不是长期依赖本 addendum。

Frozen Repository base：

`agentic-dev@3c31ae96683c4a653f001402b889b40e87df976b`

## 2. Repository evidence

当前正式架构已经明确区分以下能力：

- Core Method：定义跨技术栈生命周期、阶段职责、Authority 与完成语义；
- Engineering Discipline：描述阶段内部如何高质量工作，通常跨技术栈成立，但不因为重要就自动成为 Skill；
- Technology Profile：描述特定技术体系下的可复用默认知识、边界、惯例和验证关注点；
- Verification Profile：描述某类技术变更通常需要的验证层级、证据类型和风险判断；
- Skill：只有在能力形成稳定、独立、可组合流程，并具有明确输入、步骤、输出和退出条件时才适合 Skill 化。

`engineering-disciplines.md` 进一步明确，当前工程纪律没有独立任务入口、阶段返回、稳定独立输出或单独调度价值，因此不满足任务型 Skill 条件；同时又会被多个 Skill、工程质量复核和技术画像共同消费，因此也不应只写死在某一个 Skill 内。

`technology-profile-contract.md` 明确 Technology Profile 是可复用默认基线，不是某个 Consumer 的最终项目事实；Consumer 可以选择、局部覆盖或拒绝，但不能因为本地偏好改写客观技术语义。

因此，V0.1 将长期资源主要压缩为 Method / Skill / Repository-local Policy / Project Authority / Guide / Research/Input/Evidence 六类，确实不足以覆盖当前正式 Engineering Capability Architecture。

## 3. 修订后的 ownership 判断模型

v3 后续不再把“资源类型、适用范围、运行场景、物理载体”混成单一分类维度。

至少分开判断四个维度。

### 3.1 Semantic owner role

当前候选采用七类 semantic owner role：

1. **Method / Principle**  
   拥有跨项目成立的开发生命周期、阶段职责、Authority 边界和顶层不变量。

2. **Skill / Procedural Capability**  
   拥有稳定、独立、可组合的 Agent procedure；具有明确 trigger、输入、步骤、输出、退出 / Stage Return / Escalation。

3. **Reusable Engineering Capability / Discipline / Profile**  
   拥有跨项目可复用、但不一定形成独立任务流程的工程知识与约束，包括 Engineering Discipline、Technology Profile、Verification Profile，以及经 Architecture / Contract 明确准入的同类 capability。它可以被多个 Skill 和 Consumer 选择性采用，不因为 Agent 会读取就自动 Skill 化，也不因为存在于 `agentic-dev` 仓库就退化成 repository-only policy。

4. **Repository-local Policy / Standard / Rule**  
   拥有当前 Repository 自己持续适用的本地治理约束，例如 Git Commit、语言 / 术语、授权、集成、本地验证政策。它通常不是跨项目 reusable capability，也通常没有独立 procedure。

5. **Project / Product Authority Resource**  
   拥有当前项目的 Requirement、Domain、Specification、Architecture state、ADR、Roadmap、Verification Strategy、durable Work Authority 等项目事实或长期项目决定。它回答 `What is true for this project?`。

6. **Guide**  
   主要服务人类理解、选择、采用、初始化和 baseline upgrade 等低频 setup 场景；不拥有 ordinary runtime 的核心 procedure、repository-local policy 或项目事实。

7. **Research / Input / Evidence**  
   包括原始需求、政策原文、研究、实验、历史 evidence、一次性分析等非 Current Authority 输入；只有经过明确 promotion / adoption 才可能形成前六类资源。

七类仍只是 V3-01 的候选 decision matrix，不是已经冻结的正式 Architecture；V3-01 必须用当前代表资源验证分类是否足够，并允许发现反例后修订。

### 3.2 Applicability / provenance scope

Semantic owner role 与适用范围分开判断。至少区分：

- `reusable-upstream`：由 `agentic-dev` 维护，可跨 Consumer 选择性采用；
- `repository-local`：只对当前仓库持续生效；
- `consumer-native`：由 Consumer 自己形成和演进；
- `adopted-local`：来源于 upstream，但采用后由 Consumer-local Authority 管理。

同一种 semantic owner role 可以存在于不同 scope。

例如：

- `agentic-dev` 的 Technology Profile：Reusable Engineering Capability + reusable-upstream；
- Consumer 自己的 Git 规范：Repository-local Policy + consumer-native；
- Consumer 采用并局部覆盖的验证画像：Reusable Engineering Capability 的 adopted-local projection；
- Consumer Requirement：Project Authority + consumer-native。

`origin` / provenance 不授予 current authority，也不要求 ordinary runtime 访问 upstream。

### 3.3 Runtime / lifecycle role

另行判断资源在生命周期中的消费方式：

- bootstrap / initialization；
- adoption / baseline upgrade；
- ordinary runtime；
- verification / review；
- historical / evidence only。

同一 semantic owner 不因为只在某个生命周期阶段消费就改变资源类型。

例如 `using-agentic-dev.md` 可以是 Guide，并在 initialization / upgrade 中完整读取；这不让它成为 ordinary runtime Authority。

### 3.4 Representation / authority form

Architecture、Contract、Standard、Profile、`SKILL.md`、Guide、ADR、Requirement 等物理 / 文档形式，不直接等于 semantic owner role。

特别是：

- `engineering-capability-architecture.md` / `skill-contracts.md` 等 Architecture / Contract 文档可以定义 reusable capability 的身份、职责和准入边界；
- `SKILL.md` 是 Skill 的平台兼容执行载体；
- Profile 文档可以承载 Reusable Engineering Capability；
- Repository Standard 文档承载 repository-local policy；
- Architecture Authority / ADR 在 Consumer 中可以承载 Project Authority；
- derived discovery / index 不获得 semantic body ownership。

因此 V3-01 不应试图把每一种文件名或文档类型都变成新的 ownership category。

## 4. 代表资源映射

V3-01 必须至少使用以下当前资源试分类，而不是只在抽象层判断。

| 当前资源 | Semantic owner role | Scope / lifecycle 说明 |
|---|---|---|
| `docs/method/ai-development-method.md` | Method / Principle | reusable-upstream；普通方法权威 |
| `skills/execute-unit/SKILL.md` | Skill / Procedural Capability | reusable-upstream；JIT procedure |
| `docs/architecture/engineering-disciplines.md` | Reusable Engineering Capability / Discipline / Profile | reusable-upstream；跨 Skill 消费，不要求独立 task entry |
| `docs/technology-profiles/vue3-typescript.md` | Reusable Engineering Capability / Discipline / Profile | reusable-upstream；Consumer 可选择 / 覆盖 / 拒绝 |
| `docs/guides/git-commit-guidelines.md` | Repository-local Policy / Standard / Rule | 当前内容主要约束 `agentic-dev` 自身；若 Consumer 采用，应形成 Consumer-local 自有规则 |
| `docs/guides/terminology-guidelines.md` | Repository-local Policy / Standard / Rule | 当前 `agentic-dev` 表达 / 术语治理；概念定义继续由 Method / Architecture / Contract owner 持有 |
| Consumer Requirement / Specification | Project / Product Authority Resource | consumer-native；ordinary runtime project facts |
| `docs/guides/using-agentic-dev.md` | Guide（候选主身份） | human + initialization / adoption / upgrade；其中非 Guide rule family 必须 V3-02 分流 |
| `docs/guides/verification-evidence-rules.md` | **文件级不得直接单类化** | 需在 V3-02 按 rule family 判断 Reusable Engineering Capability / existing Skill / Principle / platform capability；重复正文应回到单一 owner |
| `docs/guides/external-operation-guidelines.md` | **文件级不得直接单类化** | 需区分 reusable external-operation constraint、repository authorization、平台 procedure、human explanation |

## 5. 对 V3-01～V3-04 的修订

### V3-01

输出不再只是“六类文件分类”，而是四维 decision matrix：

```text
semantic owner role
+ applicability / provenance scope
+ runtime / lifecycle role
+ representation / authority form
```

Gate：至少用上一节代表资源完成一致分类；如果两个 reviewer 对 Engineering Discipline / Technology Profile / Repository-local Policy 等仍频繁混淆，则不能进入 V3-02。

### V3-02

全仓 audit 仍按 rule family / semantic body 判断，不按目录名判断。Architecture / Contract 作为正式定义权威必须保留，其正文不能因为文件位于 `docs/architecture` 就自动归为 Consumer-style Project Authority。

V3-02 与 V3-04 可以共享同一份审计矩阵，避免重复维护迁移事实。

### V3-03

Consumer lifecycle 不变：initialization / adoption / explicit upgrade 可以读取 upstream；完成本地采用后 ordinary runtime local-only。Reusable Engineering Capability 必须通过逐项 adoption / local projection 进入 Consumer，不因 upstream 可复用就成为运行时外部依赖。

### V3-04

Skill admission 继续保持严格：

- 有独立稳定 procedure 才考虑 Skill；
- Engineering Discipline / Profile 不因为跨项目复用就自动 Skill 化；
- supporting reference 只承载 Skill-owned procedure 的细节，不用于隐藏另一类独立 semantic owner；
- Repository-local policy 不因为 Agent 需要遵守就 Skill 化；
- Guide 中发现的 reusable non-procedural rule family 优先判断是否属于现有 Engineering Capability / Discipline / Profile，而不是直接创建新 Skill。

## 6. 对 Front Matter / Discovery 的影响

本修订不提前决定 V3-05 / V3-06 的实现。

它只增加一个约束：如果后续需要 Resource Metadata / Index，metadata 必须能够表达“semantic owner role 与 scope / lifecycle / representation 分离”，不能用一个 `type` 字段把四个维度重新混在一起。

同样，不预设所有 Skill、Profile、Policy、Authority 都必须进入一个统一 Index。Native Skill discovery 与最小 Repository Resource discovery 的职责边界仍留给 V3-06 比较。

## 7. ADR 影响

本修订不立即创建 ADR。

如果 V3-01～V3-03 最终验证并正式采用上述 ownership 模型，则可以评估一个长期 ADR 记录：

- 为什么区分 procedural Skill、reusable non-procedural Engineering Capability、repository-local Policy 与 Project Authority；
- 为什么 scope / lifecycle / representation 不与 semantic owner role 混为单一分类；
- 为什么 Guide 退出 ordinary runtime semantic ownership。

具体目录、字段名或文件拆分仍不属于 ADR 级决定。

## 8. Medium resolution claim

当前修订声称解决的只有首轮唯一 Medium：

> “六类 ownership 模型缺少可复用非流程能力的明确归属。”

本修订不声称 v3 已完成设计，也不证明 Front Matter、Resource Index、自采用或 Consumer runtime 已经通过。

定向复评只应判断：

1. 该 Medium 是否已经被充分解决；
2. 是否因修订引入新的 Blocking / Medium；
3. 如果通过，是否可以进入“正式建立 v3 Milestone”的人工路线决策，而不是直接实施。
