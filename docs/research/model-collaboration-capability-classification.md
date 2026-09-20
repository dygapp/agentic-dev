---
id: research:model-collaboration-capability-classification
type: research
status: active
distribution: source-only
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

## 4. 第二次修正：新增 Method 也不能偷走相邻 Method 的 Gate

确认 Model Collaboration 需要独立 Method 后，初版又出现了另一个边界问题：专用 Method 在 `Local Capability Projection` 中同时承担了 Collaboration Architecture 的 `adopt / adapt / reject` 判断。

这会与现有 `method:consumer-adoption` / `method:consumer-upgrade` 的 upstream capability assessment 重叠，并产生危险路径：Existing Consumer 可能绕过显式 baseline upgrade，直接从新 upstream 复制尚未评估的 Architecture / Method / Rule。

因此最终进一步拆分：

```text
Consumer Adoption / Upgrade
  → 接受 / 适配 reusable capability semantics

Model Collaboration Adoption
  → 对已经接受的 semantics 建立 local runtime / config / policy / validation instance

ordinary development Method
  → 在启用后的 local instance 上执行实际工作
```

这形成第二条重要经验：

> **识别出新 Method 后，还必须检查它的进入前提、退出结果和相邻 Method Gate，防止新增 Method 通过“方便”重新拥有已经存在的 semantic acceptance responsibility。**

多个 Method 可以在同一次整体变更中连续组合，但各自的 Gate 和 completion claim 必须保持可辨认，不能为了流程顺滑合并成隐式双 Authority。

## 5. 最终语义归属拆分

最终不是在 Method 与 Architecture 之间二选一，而是把不同问题交给不同 owner：

| 问题 | Semantic owner |
| --- | --- |
| 多模型协作的稳定结构、角色边界、single-writer、handoff、routing、fallback 是什么？ | Architecture |
| Consumer 是否接受新的 upstream collaboration semantics？ | Consumer Adoption / Upgrade 或目标 Repository 等价 Authority |
| 已接受 semantics 后，Consumer 怎样建立 / 首次启用 runtime instance？ | Model Collaboration Adoption Method |
| 当前 Repository 实际使用哪个 runtime、模型、配置路径、status？ | Project Capability Profile / local config |
| 哪些条件性局部 policy 只对当前 Consumer 成立？ | Consumer-local Rule |
| 人类怎样理解 / 配置 / 排错？ | Guide |
| 历史实验与为什么这样分类？ | Research / Git / Issue / PR |

这个拆分比“把所有内容放到一份多模型方法文档”更稳定，也避免把 `.codex/` 的物理配置结构误当成 capability semantic owner。

## 6. 可复用的分类分析流程

以后遇到“一个新能力应该是 Method / Architecture / Skill / Rule / Project 还是 Guide？”时，可以按以下顺序分析。

### 6.1 先识别真实问题，而不是先选文档类型

把需求拆成多个问句。例如本例实际同时包含：

1. 多模型协作的运行不变量是什么？
2. Consumer 是否已经接受相关 reusable semantics？
3. Consumer 怎样建立 runtime instance？
4. 当前项目怎样配置它？
5. 哪些 policy 需要条件性发现？
6. 人类怎样使用？

一个自然语言需求可能对应多个 semantic owner，不能强迫它只归入一个类型。

### 6.2 区分“使用能力”与“建立能力”

- **使用能力**：普通任务中如何执行协作，通常由 Architecture / Skill / Rule 约束；
- **建立能力**：Repository 如何从没有 runtime instance 进入“可恢复、可验证、可关闭”的 local state，可能形成独立 Method。

不要因为 ordinary runtime 没有新增生命周期，就否定 adoption / migration / bootstrap 类工作本身成为 Method 的可能。

### 6.3 再区分“接受语义”与“实例化语义”

这是本次第二次修正暴露出的关键检查：

- **semantic acceptance** 决定 upstream capability 是否进入 Consumer-local canonical owner；
- **instance activation** 决定已经接受的 capability 在当前 Repository 使用什么 runtime、配置、局部 policy 和验证证据。

如果现有 Method 已经拥有 semantic acceptance，新的 specialized Method 应把它作为前置 Gate，而不是重新实现一套 adopt / adapt / reject。

### 6.4 寻找相邻已存在能力作为语义对照

不是机械模仿文件结构，而是比较：

- work kind 是否类似；
- 是否同样存在 Restore / Assess / Apply / Validate / Close；
- 是否有 local canonical owner 建立问题；
- 是否需要跨 Fresh Context 保持 Gate 与 completion；
- 候选 Method 的输入 / 输出是否会覆盖相邻 Method 已有责任。

本次 `consumer-adoption` 是比 `ai-development` 更有解释力的相邻 Method；`consumer-upgrade` 则帮助发现了不能绕过 upstream delta assessment 的边界。

### 6.5 用 Method 准入门禁复核

候选 Method 至少要证明：

- work kind 稳定可识别；
- 有阶段 / 状态与责任转换；
- 有跨 context Gate / completion；
- 不能被一个有界 Skill 完整表达；
- 与现有 Method 不是纯命名差异；
- 有真实 Evidence 支持长期复用。

通过 admission gate 后，还要做 **Method composition review**：前置条件由谁拥有、失败返回哪里、完成结果交给谁、是否复制了其他 Method 的 Gate。

### 6.6 不按物理载体分类

`.codex/config.toml`、agent TOML、workflow、脚本都只是 implementation / instance asset。不能因为需求最后会产生配置文件，就把 capability 归类为“配置指南”；也不能因为有步骤就自动归类为 Method。

先确定 semantic owner，再决定物理文件放在哪里。

### 6.7 把证据与规范结论分开

历史实验失败仍然有价值：它证明静态 parse PASS 不等于 child runtime 成功，并形成了 future validation requirement。

但失败 Evidence 不能被改写成“多模型方案已经验证成功”。同理，Issue #71 支持 lower-cost-first / evidence-based escalation，但不能证明所有任务都应该启用 subagents。

Research 可以保存推理来源；只有进入真实 current owner 的结论才改变 capability 行为。

## 7. 对未来类似需求的启发

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
  semantic acceptance
  → local instance establishment / validation / enablement
  → ordinary use / later maintenance
```

Axis A 可能落到 Architecture / Skill / Rule；Axis B 的不同状态转换也可能分别属于 generic Adoption / Upgrade 与 specialized activation Method。不能因为都发生在“采用过程中”就让一个 Method 吞掉全部责任。

## 8. 当前证据限制

本次分类已经有历史实验与 Consumer Evidence 支撑，但当前平台 multi-agent runtime 的真实可靠性仍需由采用时的 runtime detection / smoke 重新证明。

因此本研究记录支持“capability / adoption semantic design”，不声称当前所有 Codex 环境已经通过 Model Collaboration runtime validation。