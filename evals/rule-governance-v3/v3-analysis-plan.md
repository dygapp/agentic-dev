---
id: eval-rule-governance-v3-analysis-plan
title: 规则治理与知识激活 v3 分阶段分析计划
type: evaluation-plan
status: review-only
version: "V0.1"
classification:
  - rule-governance
  - planning
relations:
  upstream:
    - evals/rule-governance-v3/v3-governance-convergence-summary.md
  related:
    - evals/rule-governance-v3/v3-candidate-review-package.md
    - evals/rule-governance-v3/gpt6-review-prompt.md
---

# 规则治理与知识激活 v3 分阶段分析计划

## 1. 目的

本计划把 v3 从一次“大设计”拆成顺序受控的分析任务。每个任务只回答一个主要架构问题，并以前序结果作为输入。

当前分支是临时评估分支；这些任务是后续正式 v3 Milestone 的候选分析结构，不等于已经获得 Execute Authority。

## 2. 总体顺序

```text
V3-01 Ownership Model
→ V3-02 Current Repository Audit
→ V3-03 Consumer Lifecycle
→ V3-04 Skill Reclassification
→ V3-05 AI-ready Resource Model
→ V3-06 Discovery Architecture
→ V3-07 agentic-dev Self-Adoption
→ V3-08 Consumer Validation
→ Independent Review
→ 必要 ADR / Formal v3 Design
```

不得跳过 ownership / audit，直接进入 Index、Manifest、Catalog、Front Matter generator 或新增 Skill 实现。

## 3. V3-01 — Knowledge & Capability Ownership Model

### 核心问题

建立 `agentic-dev` 长期内容的明确分类准则，至少区分：

- Method / Principle；
- Skill；
- Repository-local Policy / Standard / Rule；
- Project Authority Resource；
- Guide；
- Research / Input / Evidence。

### 必须回答

- 每类回答什么问题；
- 何时进入 / 不进入该类；
- 谁拥有正文语义；
- 是否进入 ordinary runtime；
- 是否可投射 / 采用到 Consumer；
- 是否存在 lifecycle / supersede 规则；
- “不属于 Method / Skill”为什么不能自动进入 Guide。

### 输出

一份可用于后续全仓分类的 ownership decision matrix。

### Gate

分类准则必须足够让两个独立 reviewer 对主要现有文档得出高度一致的 owner 判断；若仍大量依赖“看起来像”，不得进入 V3-02。

## 4. V3-02 — Current Repository Ownership Audit

### 核心问题

按 V3-01 对当前 `agentic-dev@master` 做 semantic ownership audit，重点不是移动文件，而是确认现有正文实际属于哪里。

### 优先对象

- `docs/guides/using-agentic-dev.md`
- `docs/guides/consumer-local-rule-activation.md`
- `docs/guides/rule-activation-guide.md`
- `docs/guides/verification-evidence-rules.md`
- `docs/guides/external-operation-guidelines.md`
- `docs/guides/git-commit-guidelines.md`
- `docs/guides/terminology-guidelines.md`
- `docs/architecture/engineering-disciplines.md`
- current Method / Principle / Skill overlap

### 输出

逐文档 / 逐 rule-family 分类矩阵：

```text
current location
current semantics
correct owner type
keep / move / merge / split / supersede / delete
ordinary-runtime role
consumer-adoption role
reason
```

### Gate

不能因为目录名推断 owner；所有拟迁移内容必须指向一个明确新 owner 或明确删除理由。

## 5. V3-03 — Consumer Initialization / Adoption / Upgrade / Runtime Lifecycle

### 核心问题

把 Consumer 生命周期正式拆开，避免一次性 setup guidance 进入 ordinary runtime。

### 必须覆盖

- new Consumer initialization；
- existing Consumer adoption；
- baseline upgrade；
- ordinary runtime；
- capability gap / explicit upstream re-entry；
- Consumer-local rule evolution；
- 原始需求存在 / 不存在两种初始化路径；
- origin / provenance 与 current Consumer Authority 的区别。

### 输出

Consumer lifecycle model + 每阶段允许读取的 resource class。

### Gate

ordinary runtime 必须能明确说明哪些 upstream 资产禁止默认读取；initialization / upgrade 必须能说明怎样把结果持久化为 Consumer-local Current Resource。

## 6. V3-04 — Skill Reclassification & Admission

### 核心问题

在 V3-02 审计结果基础上，判断哪些现有 Guide rule family 实际属于：

- existing Skill；
- Skill supporting reference；
- Engineering Discipline / Standard；
- Repository Policy；
- new Skill candidate；
- Human Guide；
- 不值得长期持久化。

### Skill admission

新 Skill 至少要满足：

- 独立稳定职责；
- 可跨项目复用；
- 明确 trigger；
- 明确输入 / Procedure / 输出；
- Exit / Stage Return / Escalation 可定义；
- 不是把若干无关规则打包；
- 不与现有 Skill 形成重复 owner。

### 输出

Skill migration / admission matrix。

### Gate

不得为了减少 Guide 数量机械新增 Skill；也不得因为历史上“不想改 Skill”而继续保留明显 procedural rule 在 Guide。

## 7. V3-05 — AI-ready Repository Resource Model

### 核心问题

对非 Skill 的长期 Agent-consumed resources 定义最小结构化元数据模型。

### 必须回答

- 哪些 resource 必须 / 应该 / 不需要 YAML Front Matter；
- identity / type / status / classification / relations 的最小字段；
- 是否需要 routing metadata；
- Front Matter 与正文 Authority 边界；
- 原始需求 / Research / Evidence 为什么默认不进入统一 Authority schema；
- `SKILL.md` 与普通 Markdown 的 metadata compatibility boundary。

### 输入原则

可以参考已经验证过的 Structured Markdown 实践：Front Matter 只做定位 / 路由，正文承载规范事实。

### 输出

AI-ready Resource Metadata Contract 候选。

### Gate

Contract 必须减少而不是增加双点维护；不得把事实摘要复制到 metadata。

## 8. V3-06 — Minimal Repository Discovery Architecture

### 核心问题

在 ownership 与 resource model 已确定后，重新判断还需要什么 discovery。

### 必须比较

- 仅目录 / Authority Map；
- generated Resource Index；
- generated Index + source identity；
- 是否有必要对 Skill 建第二份索引；
- 原生 Skill discovery 与 Repository Resource Discovery 的责任边界。

### 原则

优先最简单可验证结构；不能因为 v1/v2 有 Manifest / Catalog 历史就预设 v3 继续需要同等级机制。

### 输出

Discovery architecture + currentness / stale / rebuild / fail-closed contract。

### Gate

同一 responsibility 不允许并行保留多个看起来 current 的 derived discovery mechanism。

## 9. V3-07 — `agentic-dev` Self-Adoption

### 核心问题

让 `agentic-dev` 自身成为新 ownership / Skill / Resource Discovery 模型的一等使用方。

### 必须覆盖

- Thin `AGENTS.md`；
- README / Roadmap / current project Authority；
- Repository-local Standards；
- Method / Principle；
- native Skill discovery；
- Resource Discovery；
- Fresh Context；
- Stage Return；
- ordinary repository maintenance task；
- project planning task；
- platform / verification task。

### 输出

Self-adoption design + runtime scenarios。

### Gate

不能存在“Consumer 有结构化 discovery，但 agentic-dev 自己靠人工大 Guide 路由”的双重模型。

## 10. V3-08 — Consumer Projection & Validation

### 核心问题

验证 v3 对真实 Consumer 的 initialization / upgrade / ordinary runtime 是否可用。

### 验证至少覆盖

- 初始化时有原始需求；
- 初始化时无原始需求；
- Consumer-local terminology / git / repository rules 形成并可自行演进；
- adopted Method / Skills local-only；
- ordinary runtime 不读取 `using-agentic-dev.md` / upstream；
- explicit baseline upgrade 能重新进入 upstream 并更新 local resources；
- Consumer-specific override 优先；
- stale / missing / ambiguous resource discovery fail-closed；
- Skill JIT activation；
- v1/v2 已验证行为没有回归。

### 输出

Consumer validation plan / result。

### Gate

真实 Consumer PASS 前，不声明 v3 已完成。

## 11. ADR 决策点

ADR 不预建。只有对应分析形成明确长期架构取舍后再创建。

高概率检查点：

- V3-01 后：是否需要 `Repository Knowledge & Capability Ownership Architecture` ADR；
- V3-04 后：是否形成 `Skill-centric Runtime vs Guide/Rule-centric Runtime` 的长期取舍；
- V3-06 后：是否形成 `AI-ready Markdown + Generated Resource Index` 的长期取舍。

如果结论只是显然的文档重分类、字段命名或路径选择，则不创建 ADR。

## 12. 独立 AI Review 的位置

当前 GPT-6 Review 应评审：

1. Governance Summary 是否准确识别根因；
2. Ownership Model 是否缺少必要类别或存在重叠；
3. Guide / Skill / Repository Rule / Project Authority 边界是否稳定；
4. Consumer lifecycle 是否合理；
5. V3-01～V3-08 顺序是否避免过早实现；
6. 哪些既定判断已经足够稳定，哪些仍被过早冻结；
7. v1 / v2 哪些安全成果可能在重构中丢失。

评审不应现在要求确定最终 Index schema、最终 Skill 清单或最终文件目录。

## 13. 当前非目标

本计划阶段不：

- 修改 `master`；
- 创建正式 v3 Milestone / Issue / PR；
- 移动现有 Guide；
- 新增正式 Skill；
- 修改 Method / Principle；
- 实现 Front Matter validator / generator；
- 实现 Resource Index；
- 修改 Consumer Repository；
- 创建 ADR；
- 宣布 v2 invalid。

## 14. 当前自然 Gate

本临时评估分支的下一自然 Gate 是：

> 完成基于本治理总结与分析计划的 GPT-6 独立评审，回传结果后再决定哪些 Blocking / Medium 需要先修正，以及是否具备正式建立 v3 Milestone 的条件。