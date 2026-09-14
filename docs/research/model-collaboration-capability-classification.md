---
id: research:model-collaboration-capability-classification
type: research
status: active
---

# Model Collaboration Capability 分类经验

## 1. 背景

本记录总结 Model Collaboration Capability & Adoption v1 形成过程中一段有复用价值的分析经验。它不是规范 Authority，不参与 ordinary runtime；正式结论已经分别进入 Architecture / Method / Project instance 等真实 owner。

历史输入包括：

- `experiment/codex-multi-model-collaboration` 分支：曾尝试 primary + fast explorer + implementation worker + quality reviewer + critical reviewer 的 Codex 多模型协作；
- 该实验的静态配置校验成功，但真实 child collaboration smoke 出现 `collab spawn failed: no thread with id`，因此没有把最终自述当作真实委派成功；
- Issue #71：Consumer 中对较低成本 capable model 与更高能力 model 的 paired / blind review Evidence，支持 lower-cost-first、evidence-based escalation，而不支持“高影响问题默认必须最高等级模型”的强假设；
- 当前 V4 Capability / Project / Method / Rule Discovery 架构已经明确 reusable capability 与 Repository-local instance 的 ownership 边界。

## 2. 初始判断为什么不完整

最初从“多模型协作是否改变软件开发生命周期”出发判断：

- 普通开发仍然是 Clarify / Specification / Technical Planning / Slice / Execute / Converge；
- 多模型只是同一责任在多个 Agent 之间分工；
- 因此更像 Architecture，而不是一个新的 Development Method。

这个判断对 **协作能力本身** 是正确的：single-writer、Authority-preserving handoff、model escalation、fallback 等确实属于 Architecture invariant。

但它遗漏了另一个不同的问题：

> 一个 Consumer Repository 如何把这项能力显式安装、配置、验证并建立为自己的 local capability instance？

只回答“capability 是什么”不足以回答“Consumer 怎样建立 capability”。

## 3. 关键转折：比较相邻已有 Method

重新对照 `method:consumer-adoption` 后发现，Method 并不等于“产品开发生命周期”。Consumer Adoption 本身管理的是一类独立复杂工作：

```text
Restore Consumer Authority
→ Select Upstream Baseline
→ Capability Assessment
→ Local Adoption / Adaptation
→ Establish Local Runtime Instance
→ Validate
→ Close
```

因此判断一个候选是否应该成为 Method，不能只问：

> 它是否改变 ordinary software development lifecycle？

还必须问：

> 它本身是否构成一个稳定、可识别、跨多个 action / context、具有阶段转换、Gate 和完成语义的复杂 work kind？

Model Collaboration Adoption 满足这个条件：即使 Consumer 已经采用 `agentic-dev` 很久，仍可能在之后单独执行“建立多模型协作能力”这类工作。

## 4. 最终 semantic-owner 拆分

最终不是在 Method 与 Architecture 之间二选一，而是把不同问题交给不同 owner：

| 问题 | Semantic owner |
| --- | --- |
| 多模型协作的稳定结构、角色边界、single-writer、handoff、routing、fallback 是什么？ | Architecture |
| Consumer 怎样第一次建立 / 启用这项 capability？ | Method |
| 当前 Repository 实际使用哪个 runtime、模型、配置路径、status？ | Project Capability Profile / local config |
| 哪些条件性局部 policy 只对当前 Consumer 成立？ | Consumer-local Rule |
| 人类怎样理解 / 配置 / 排错？ | Guide |
| 历史实验与为什么这样分类？ | Research / Git / Issue / PR |

这个拆分比“把所有内容放到一份多模型方法文档”更稳定，也避免把 `.codex/` 的物理配置结构误当成 capability semantic owner。

## 5. 可复用的分类分析流程

以后遇到“一个新能力应该是 Method / Architecture / Skill / Rule / Project 还是 Guide？”时，可以按以下顺序分析。

### 5.1 先识别真实问题，而不是先选文档类型

把需求拆成多个问句。例如本例实际同时包含：

1. 多模型协作的运行不变量是什么？
2. Consumer 怎样采用它？
3. 当前项目怎样配置它？
4. 哪些 policy 需要条件性发现？
5. 人类怎样使用？

一个自然语言需求可能对应多个 semantic owner，不能强迫它只归入一个类型。

### 5.2 区分“使用能力”与“建立能力”

这是本次最重要的经验。

- **使用能力**：普通任务中如何执行协作，通常由 Architecture / Skill / Rule 约束；
- **建立能力**：Repository 如何从没有该能力进入“可恢复、可验证、可关闭”的 local state，可能形成独立 Method。

不要因为 ordinary runtime 没有新增生命周期，就否定 adoption / migration / bootstrap 类工作本身成为 Method 的可能。

### 5.3 寻找相邻已存在 capability 作为语义对照

不是机械模仿文件结构，而是比较：

- work kind 是否类似；
- 是否同样存在 Restore / Assess / Apply / Validate / Close；
- 是否有 local canonical owner 建立问题；
- 是否需要跨 Fresh Context 保持 Gate 与 completion。

本次 `consumer-adoption` 是比 `ai-development` 更有解释力的相邻 Method。

### 5.4 用 Method admission gate 复核

候选 Method 至少要证明：

- work kind 稳定可识别；
- 有阶段 / 状态与责任转换；
- 有跨 context Gate / completion；
- 不能被一个有界 Skill 完整表达；
- 与现有 Method 不是纯命名差异；
- 有真实 Evidence 支持长期复用。

如果只满足“有很多步骤”，仍不足以成为 Method。

### 5.5 不按物理载体分类

`.codex/config.toml`、agent TOML、workflow、脚本都只是 implementation / instance asset。不能因为需求最后会产生配置文件，就把 capability 归类为“配置指南”；也不能因为有步骤就自动归类为 Method。

先确定 semantic owner，再决定物理文件放在哪里。

### 5.6 把 Evidence 与规范结论分开

历史实验失败仍然有价值：它证明静态 parse PASS 不等于 child runtime 成功，并形成了 future validation requirement。

但失败 Evidence 不能被改写成“多模型方案已经验证成功”。同理，Issue #71 支持 lower-cost-first / evidence-based escalation，但不能证明所有任务都应该启用 subagents。

Research 可以保存推理来源；只有进入真实 current owner 的结论才改变 capability 行为。

## 6. 对未来类似需求的启发

类似问题可能包括：

- 新的测试 / review orchestration 能力；
- Repository bootstrap / migration capability；
- 自动化发布或 deployment capability；
- 数据迁移 / external integration adoption；
- Agent runtime / provider capability；
- 新的 knowledge / context management runtime。

遇到这些需求时，不应先问“要不要新增一个 Method 文件”，而应先做两轴分析：

```text
Axis A — reusable capability semantics
  structure / invariant / procedure / conditional policy

Axis B — repository state transition
  how a Consumer establishes, validates, enables, upgrades or retires that capability
```

Axis A 可能落到 Architecture / Skill / Rule；Axis B 在满足 Method admission gate 时可以形成独立 Method。两者同时存在并不冲突。

## 7. 当前 Evidence 限制

本次分类已经有历史实验与 Consumer Evidence 支撑，但当前平台 multi-agent runtime 的真实可靠性仍需由采用时的 runtime detection / smoke 重新证明。

因此本研究记录支持“capability / adoption semantic design”，不声称当前所有 Codex 环境已经通过 Model Collaboration runtime validation。