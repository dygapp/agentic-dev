# 规则激活导航

本文是 `agentic-dev` 面向使用方的**薄规则导航入口**。它只负责告诉 Agent 当前任务应继续读取哪些现行来源，不复制详细规则正文，也不成为第二套规则权威。

详细语义继续由现有 Repository Authority、对应 Guide / Skill / Engineering Capability 承担。发生冲突、来源陈旧或适用范围不明确时，必须回到当前仓库权威重新读取。

## 1. 常驻最小不变量

使用 `agentic-dev` 推进任何 Consumer 时，只持续保持三个薄不变量：

1. **Consumer Repository Authority 优先。** `agentic-dev` 提供方法、Skill 与使用指导，不替 Consumer 定义项目事实。
2. **渐进式披露。** 只加载当前任务真正需要的最小 Authority Context，不把旧聊天、个人记忆或完整历史作为项目事实。
3. **证据先于完成声明。** 完成、通过或可集成结论必须由与当前目标和验收义务匹配的 Current Evidence 支持。

“重要”不等于“每次都加载完整正文”。其余规则按当前职责和风险条件继续发现。

## 2. 按职责 / 风险继续读取

先识别当前工作的 `scope + responsibility`；只有确实有辨识需要时，再补充阶段、对象或条件。不要为了保险默认读取全部指南。

| 当前职责或风险 | 继续读取的最小来源 |
|---|---|
| 新项目初始化、外部需求来源采纳 | `using-agentic-dev.md` §2.1、§3、§3.1、§3.2 |
| 已有 Consumer baseline upgrade | `using-agentic-dev.md` §6.1；需要把 adopted capability 变成 ordinary runtime 本地发现能力时再读 `consumer-local-rule-activation.md` |
| 已完成 adoption 的 Consumer 普通工作 | **回到 Consumer-local Bootstrap / Discovery Entry**；普通 Runtime 不继续把本指南或 upstream 当作日常依赖 |
| 规划候选、执行单元身份、工作切分 | `using-agentic-dev.md` §3、§5.4；`skills/slice-work/SKILL.md` |
| 就绪门禁、上游 WHAT / HOW / Architecture basis 失效后的重新进入 | `skills/readiness-check/SKILL.md`，必要时补读 `using-agentic-dev.md` §5.4 |
| 单个已就绪执行单元的实施 | `skills/execute-unit/SKILL.md`；`using-agentic-dev.md` §5.5 |
| 验证证据类型、证据与完成声明匹配 | `using-agentic-dev.md` §5.7；当前执行 / 收敛 Skill |
| GitHub Actions 验证层、trigger / gate、可观察性或成本 | `skills/github-actions-verification/SKILL.md`，不要先加载整份外部操作指南 |
| 临时执行证据被接受为长期稳定输入 | `external-operation-guidelines.md` §5.3；GitHub Actions Artifact 再补 `github-actions-verification` 对应部分 |
| 异步外部操作 | `external-operation-guidelines.md` §5.1；GitHub Actions 场景再补平台 Skill |
| 共享资源、单实例 owner / lease / stale run | `external-operation-guidelines.md` §5.2；GitHub Actions 场景再补平台 Skill |
| 普通外部写操作、PR / Issue / 仓库状态修改 | `external-operation-guidelines.md` §1、§2、§5；只在实际出现更具体风险时继续读取对应小节 |
| 依赖 PR / stacked PR 的当前集成拓扑 | `external-operation-guidelines.md` §5.4 |
| 项目路线图、长期产物、集成后的稳定路线 | `using-agentic-dev.md` §6.2 |
| 中断恢复、新聊天或新执行者 | `using-agentic-dev.md` §7，并从 Consumer 项目路线图或等价入口继续按需读取 |
| 明确的 `agentic-dev` Consumer 实验 | `using-agentic-dev.md` §8 |
| 项目主导语言 | Consumer Repository 本地规则优先；需要通用边界时读 `using-agentic-dev.md` §3.1、§7 |

Skill 的完整执行过程由该 Skill 自己拥有。使用指南承担发现、协调和跨职责边界，不要求同时加载多个 Skill 的完整正文。

## 3. Consumer-local adoption 后的边界

`consumer-local-rule-activation.md` 定义采用完成后的本地发现与激活方式，包括：

- Thin Bootstrap；
- Consumer-local Activation Manifest / optional Runtime Catalog；
- Consumer-native 与 adopted reusable assets 的同路发现；
- primary responsibility / supporting context；
- routing-only 与 Skill execution 分离；
- Stage Return 后重新 routing；
- stale / missing / ambiguity fail-closed；
- last evaluated upstream baseline 与 active asset provenance 分离。

这项 Guide Module 用于 adoption / projection 设计和 Consumer 本地化，不意味着普通 Consumer 工作每次都读取 upstream Guide。完成本地化后，ordinary runtime 应从 Consumer-local discovery entry 开始。

## 4. 激活规则

使用上述导航时遵守：

```text
当前任务
→ 确认 Consumer Repository Authority
→ 识别当前职责 / 风险
→ 读取最小来源指针
→ 只激活当前适用规则
→ 执行 / 验证
```

具体要求：

- 不得为了控制数量而截断仍然适用的必需规则；
- 不因为某个关键词出现，就无条件激活同名主题的全部规则；
- 相似规则适用范围不同时，保留仓库、职责、阶段和风险条件；
- 详细规则只在其 current semantic owner 维护一次；导航只保存足以发现来源的短指针；
- Consumer 自己的 `AGENTS.md`、Roadmap、Requirement、Specification、Architecture 等事实始终优先于 reusable default。

本导航不要求普通 Consumer 运行 `evals/` 下的规则检索原型；是否需要额外 discovery tooling 由 Consumer 自己的实际需要和证据决定。

## 5. 安全回退

如果出现以下任一情况，不继续依赖当前导航 / discovery result：

- 指向来源不存在；
- source identity / selector 陈旧或无法解析；
- 当前任务无法用现有职责 / 条件可靠分类；
- no-match 但当前风险显然仍需要治理判断；
- 多个规则适用范围冲突；
- high-impact authorization、重大 Architecture、安全 / 隐私或不可逆边界不明确。

此时：

```text
停止依赖当前 derived discovery
→ 重新读取当前 Repository Authority
→ 按当前问题补读必要 Guide / Skill / local Authority
→ 再做判断
```

对于已经完成 adoption 的 Consumer，ordinary runtime 的回退优先回到 **Consumer-local Current Authority**，不自动访问 upstream。

回退是安全路径，不是任务失败。不得用近似规则、旧索引或历史聊天填补未知边界。