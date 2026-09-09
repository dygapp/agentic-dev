# 规则激活导航

本文是 `agentic-dev` 面向使用方的**薄规则导航入口**。它只负责告诉 Agent 当前任务应继续读取哪些现行来源，不复制详细规则正文，也不成为第二套规则权威。

详细语义继续由现有 Repository Authority、`docs/guides/using-agentic-dev.md`、`docs/guides/external-operation-guidelines.md` 和对应 Skill 承担。发生冲突、来源陈旧或适用范围不明确时，必须回到当前仓库权威重新读取。

## 1. 常驻最小不变量

使用 `agentic-dev` 推进任何使用方项目时，只需要持续保持以下三个薄不变量：

1. **使用方仓库权威优先。** `agentic-dev` 提供方法、Skill 与使用指导，不替使用方仓库定义项目事实。详细来源：`using-agentic-dev.md` §1、§2。
2. **渐进式披露。** 只加载当前任务真正需要的最小权威上下文，不把旧聊天、个人记忆或完整历史作为项目事实。详细来源：`using-agentic-dev.md` §2、§5.5、§7。
3. **证据先于完成声明。** 完成、通过或可集成结论必须由与当前目标和验收义务匹配的当前证据支持。详细来源：`using-agentic-dev.md` §5.7、§5.8。

“重要”不等于“每次都加载完整正文”。其余规则按当前职责和风险条件继续发现。

## 2. 按职责 / 风险继续读取

先识别当前工作的 `scope + responsibility`；只有确实有辨识需要时，再补充阶段、对象或条件。不要为了保险默认读取全部指南。

| 当前职责或风险 | 继续读取的最小来源 |
|---|---|
| 新项目初始化、外部需求来源采纳 | `using-agentic-dev.md` §2.1、§3、§3.1、§3.2 |
| 规划候选、执行单元身份、工作切分 | `using-agentic-dev.md` §3、§5.4；`skills/slice-work/SKILL.md` |
| 就绪门禁、上游 WHAT / HOW / 架构基础失效后的重新进入 | `skills/readiness-check/SKILL.md`，必要时补读 `using-agentic-dev.md` §5.4 |
| 单个已就绪执行单元的实施 | `skills/execute-unit/SKILL.md`；`using-agentic-dev.md` §5.5 |
| 验证证据类型、证据与完成声明匹配 | `using-agentic-dev.md` §5.7；当前执行 / 收敛 Skill |
| GitHub Actions 的验证层、trigger / gate、可观察性或成本边界 | `skills/github-actions-verification/SKILL.md`，重点 §4、§4.1；不要先加载整份外部操作指南 |
| 临时执行证据被接受为长期稳定输入 | `external-operation-guidelines.md` §5.3；如果载体是 GitHub Actions Artifact，再补读 `github-actions-verification` §10.1 |
| 异步外部操作 | `external-operation-guidelines.md` §5.1；GitHub Actions 场景再补读 `github-actions-verification` §11 |
| 共享资源、单实例 owner / lease / stale run | `external-operation-guidelines.md` §5.2；GitHub Actions 场景再补读 `github-actions-verification` §8 |
| 普通外部写操作、PR / Issue / 仓库状态修改 | `external-operation-guidelines.md` §1、§2、§5；只在实际出现更具体风险时继续读取对应小节 |
| 依赖 PR / stacked PR 的当前集成拓扑 | `external-operation-guidelines.md` §5.4 |
| 项目路线图、长期产物、集成后的稳定路线 | `using-agentic-dev.md` §6.2 |
| 既有使用方升级 `agentic-dev` baseline | `using-agentic-dev.md` §6.1 |
| 中断恢复、新聊天或新执行者 | `using-agentic-dev.md` §7，并从使用方项目路线图或等价入口继续按需读取 |
| 明确的 `agentic-dev` 使用方实验 | `using-agentic-dev.md` §8 |
| 项目主导语言 | 使用方仓库本地规则优先；需要通用边界时读 `using-agentic-dev.md` §3.1、§7 |

Skill 的完整执行过程由该 Skill 自己拥有。使用指南承担发现、协调和跨职责边界，不要求同时加载多个 Skill 的完整正文。

## 3. 激活规则

使用上述导航时遵守：

```text
当前任务
→ 确认使用方仓库权威
→ 识别当前职责 / 风险
→ 读取最小来源指针
→ 只激活当前适用规则
→ 执行 / 验证
```

具体要求：

- 不使用固定 Top-K 代替完整召回当前适用的必需规则；
- 不因为某个关键词出现，就无条件激活同名主题的全部规则；
- 相似规则适用范围不同时，保留仓库、职责、阶段和风险条件，不把它们合并成无范围规则；
- 详细规则只在其现行来源维护一次；本导航只保存足以发现来源的短指针；
- 项目自己的 `AGENTS.md`、Roadmap、Requirement、Specification、Architecture 等事实始终优先于 `agentic-dev` 对使用方事实的推测。

## 4. 安全回退

如果出现以下任一情况，不继续使用可能陈旧或不完整的导航结果：

- 指向的来源不存在或已明显改变；
- 当前任务无法用现有职责 / 条件可靠分类；
- 查询或导航没有命中规则，但当前风险显然仍需要治理判断；
- 多个规则适用范围冲突；
- 涉及高影响授权、重大架构、安全 / 隐私或不可逆操作而边界不明确。

此时执行保守回退：

```text
停止依赖派生导航
→ 重新读取当前 Repository Authority
→ 按当前任务补读完整相关 Guide / Skill
→ 再做判断
```

回退是安全路径，不是任务失败。不得用近似规则、旧索引或历史聊天填补未知边界。

## 5. 派生规则索引的边界

`evals/rule-retrieval/rule-index.json` 与 `evals/query_rule_index.py` 当前仍是规则治理里程碑形成的**可删除、可重建评估资产**：

- 不是 Repository Authority；
- 不要求普通使用方安装或运行；
- 不要求所有规则进入索引；
- 来源陈旧、未知或无匹配时必须回退当前仓库权威；
- 后续是否形成长期运行时检索能力，必须继续由实际验证证据决定。

正常使用 `agentic-dev` 时，以本导航中的稳定来源指针和当前仓库权威工作即可。

## 6. 当前不采用的做法

当前证据不要求：

- 每次启动都读取完整 `using-agentic-dev.md` 与完整 `external-operation-guidelines.md`；
- 把完整规则复制进 Fresh Context 启动提示；
- 把所有指南拆成大量小文件；
- 给全仓库统一增加 Front Matter / trust taxonomy；
- 建立新的 LLM-maintained Wiki 作为第二事实来源；
- 引入 BM25、向量数据库、图数据库、MCP knowledge server 或 Obsidian 核心依赖；
- 把规则检索包装成新的超级 Skill。

如果后续 D2 回归或真实使用方验证证明当前导航仍会漏掉必要规则，再基于具体失败补充最小来源指针或重新评估结构；不要预先扩张知识基础设施。
