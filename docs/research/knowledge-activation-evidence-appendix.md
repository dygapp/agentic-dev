# 知识激活关键证据附录

研究日期：2026-09-08

研究性质：**研究证据附录**

本文是 `knowledge-activation-and-code-intelligence-analysis.md` 的证据附录，专门保存后续新上下文最容易遗漏的数值、具体反例、外部项目实测和当前架构身份。本文不是规范性权威，不单独改变方法、指南、技能、工程纪律或技术画像。

## 1. 当前指南体量基线

2026-09-08 从 `dygapp/agentic-dev` 当前 `master` 读取 `docs/guides/`，共 4 个文件：

| 文件 | GitHub 报告大小 |
|---|---:|
| `docs/guides/using-agentic-dev.md` | 37,157 bytes |
| `docs/guides/external-operation-guidelines.md` | 18,733 bytes |
| `docs/guides/terminology-guidelines.md` | 14,578 bytes |
| `docs/guides/git-commit-guidelines.md` | 6,443 bytes |

合计约 76.9 KB，其中 `using-agentic-dev.md` 与 `external-operation-guidelines.md` 合计约 55.9 KB，占当前指南总体量约 73%。

这些数字只用于说明当前知识集中程度，不构成“超过某个大小就必须拆分”的规则。

真正重要的观察是：前两份指南内部都包含多个可以由不同任务 / 风险独立触发的主题，因此“整份文件加载”可能成为过粗的激活单位。

## 2. PR #72：规则已经存在，但没有可靠激活

PR #72：`docs(governance): 收敛里程碑集成状态闭环`

这是当前仓库最直接的规则激活失效证据之一。

PR #72 的正式说明明确记录：

- `docs/guides/using-agentic-dev.md` 已经存在“项目路线图与集成状态”边界；
- 该边界此前没有可靠进入 `agentic-dev` 自身高影响 AI 复核的必经路径；
- PR #70 合并后因此机械派生了尾部状态 PR；
- PR #72 的修复不是重新发明一套平行规则，而是把既有边界接入项目级 AI 复核；
- PR #39 是该规则原有固化入口；
- PR #63 是正确采用“拟集成后的稳定状态”的正向实例；
- PR #68 与 PR #72 构成既有规则未稳定执行的反例证据；
- PR #72 最终 AI Review `5130147829` 未解决阻塞 / 中等级问题为 `0 / 0`。

这组事实支持的最小结论不是“再增加一个状态闭环规则”，而是：

> **长期规则存在，不代表它会在当前任务中自动被发现和激活。**

它也是当前“先判断规则缺口还是激活失败”治理路径的直接仓库证据。

## 3. CodeGraph：极短激活提示对真实 Agent 行为的影响

CodeGraph 的 `src/installer/instructions-template.ts` 保存了一条对本里程碑非常关键的实测记录。

其背景是：

- 主 Agent 可以收到 MCP `initialize` 中的完整 CodeGraph 服务器指令；
- Task-tool 子代理会收到项目指令文件，但不会收到 MCP `initialize` 指令；
- 子代理即使拥有延迟加载的 CodeGraph 工具名称，也很少主动想到加载该能力。

CodeGraph 源码注释记录的强制委派流程测试：

- 测试对象：excalidraw；
- 模型：sonnet；
- effort：high；
- **没有短指令块时，子代理大约只有 1 / 9 次会主动加载并使用 CodeGraph；**
- **加入极短 marker-fenced CodeGraph 块后，子代理能稳定使用 CodeGraph，包括出现零 `Read` / `grep` 回退的运行。**

CodeGraph 因此没有重新把完整使用手册复制进 Agent 指令，而是在指令文件中只恢复一个非常短的条件性激活提示：

- 仓库存在 `.codegraph/` 时，理解 / 定位代码优先考虑 `codegraph_explore`；
- 没有 `.codegraph/` 时跳过；
- 详细行为继续由 MCP tool / server instructions 承担。

这条实测对 `agentic-dev` 的意义非常直接：

> **能力或规则已经存在、甚至工具已经可用，也不等于 Agent 会可靠激活它；一个小而精准的可发现入口可能比把完整说明常驻上下文更有效。**

该证据不能直接证明 `agentic-dev` 应采用同样实现，但强烈支持“激活入口本身需要专项评估”。

## 4. CodeGraph 的“单一强入口”不是偶然设计

CodeGraph 当前存在多个底层能力：

- node；
- search；
- callers；
- callees；
- impact；
- files；
- status；
- explore。

但 MCP 默认只暴露 `codegraph_explore`。

其官方文档说明这一选择来自实际 Agent 行为测量：一个强、覆盖面足够的入口比一组窄工具更容易把 Agent 引向直接答案，并减少错误工具选择。

这条设计经验与规则激活问题的关系是：

> 如果未来建立规则检索能力，不应先创建大量细粒度“规则工具”，把选择负担再次交给 Agent；应优先验证少量强入口能否更可靠地取得最小正确规则集。

## 5. CodeGraph 对常驻指令长度的明确约束

`src/mcp/server-instructions.ts` 的源码注释明确写出：

- 服务器指令会被 Agent 每个会话读取；
- 必须保持紧凑；
- 长指令会消耗令牌；
- 默认只围绕 `codegraph_explore` 这一暴露工具说明，不在常驻指令里列举默认不可见的其他工具。

`src/installer/instructions-template.ts` 同样说明：

- 早期曾把完整使用手册写进指令文件；
- 后来因为与 MCP `initialize` 指导重复、存在上下文成本而移除；
- 重新加入的只是为子代理 / 非 MCP 执行环境提供可发现性的极短块；
- 该块必须继续保持短小。

这与 `agentic-dev` 当前研究假设一致：

> 常驻上下文应只承担“必须一直知道什么”和“如何找到条件性知识”，不应默认承载全部长期规则正文。

## 6. CodeGraph 第一方基准测试：只作为外部参考

CodeGraph 当前文档公开了自身 Agent A/B 测试结果。

研究时读取的介绍页报告：

- 7 个真实开源代码库；
- 每个对照分组运行次数中位数为 4；
- 使用 CodeGraph 后约 **58% fewer tool calls**；
- 约 **22% faster**；
- file reads 降到接近零。

README 在后续重新测量说明中还报告过约 **44% lower cost / 62% fewer tokens on average** 的结果。

这些数字属于 CodeGraph 项目自己的第一方基准测试，不能直接推导：

- `agentic-dev` 的规则检索会获得同样比例收益；
- 任意使用方使用 CodeGraph 都会获得同样结果；
- 更少令牌 / 工具调用自动等于更高工程正确性。

可吸收的是它的验证方式：同模型 / 同任务下做有界 A/B，并把最终任务正确性与检索质量放在工具调用数量之前。

## 7. CodeGraph 索引不是权威

CodeGraph 的 `.codegraph/`：

- 保存本地派生 SQLite 索引；
- 默认由 `codegraph init` 建立；
- 通过 watcher 自动更新；
- 整个 `.codegraph/` 目录被自身 `.gitignore` 忽略；
- 发生陈旧时，对受影响文件回退到直接读取，而不是把旧索引当成事实。

这与当前仓库权威原则兼容：

```text
源码仓库
= 权威

.codegraph/
= 派生导航索引
```

如果未来 `agentic-dev` 自己建立规则索引，也应保持相同边界：可重建、可检测陈旧、不能成为第二事实来源。

## 8. CodeGraph 对普通使用方的交付边界

CodeGraph 仓库中确实存在 `.claude/skills/add-lang`、`.claude/skills/agent-eval` 等 Skill，但它们主要服务 CodeGraph 自身的语言支持开发与评估。

普通使用方的主要使用方式是：

- 本地 `.codegraph/` 索引；
- MCP `codegraph_explore`；
- CLI `codegraph explore`；
- 自动同步 / 陈旧处理；
- 极薄的 Agent 激活说明。

因此当前研究不建议：

- 把 CodeGraph 内部 Skill 复制进使用方；
- 在 `agentic-dev` 再包装一个 `codegraph` Skill 只是重复其现有能力；
- 让 CodeGraph 成为 `execute-unit`、`systematic-debug` 或未来 `code-review` 的强依赖。

更合理的是“能力存在时优先消费，能力不存在时可靠回退”。

## 9. Codex CLI 的当前 CodeGraph 项目级集成

CodeGraph 当前 `src/installer/targets/codex.ts` 明确支持 Codex CLI：

- 全局：`~/.codex/config.toml` + `~/.codex/AGENTS.md`；
- 项目级：`<cwd>/.codex/config.toml` + 仓库根目录 `AGENTS.md`；
- 项目配置写入 `[mcp_servers.codegraph]`；
- `AGENTS.md` 写入短 marker-fenced CodeGraph 块；
- 项目级 Codex config 在未信任项目中可能被加载但不启用，因此安装器会显式提醒 trust requirement。

这说明使用方无需由 `agentic-dev` 发明额外代码导航 Skill，即可在本地 Codex 环境接入成熟代码智能工具。

## 10. `code-review` 的当前正式架构身份

当前 `docs/architecture/skill-architecture.md` 已明确：

- 仓库当前实际维护 9 个 Skill：8 个核心 Skill + 1 个平台专项 Skill `github-actions-verification`；
- “第一批 8 个核心 Skill”是已经关闭的核心基线；
- `github-actions-verification` 是第 9 个已实现 Skill，但不是“第 9 个核心 Skill”；
- 第一批明确选择**不独立 Skill 化** `code-review`，让它继续作为内嵌纪律；
- 未来只有在出现稳定独立职责与足够证据时才重新评估。

因此，如果后续 WI-07 通过证据把 `code-review` 提升为独立任务型 Skill，正确身份应是：

> **第一批核心基线之后新增的任务型 Skill。**

不应描述为：

> “第 10 个核心 Skill”。

当前第一批 8 个核心 Skill 的闭合身份不需要因为代码复核候选重新打开。

## 11. 不新增“复核画像”架构层

本轮讨论没有发现建立新的“复核画像”能力层的必要证据。

未来代码复核更合理的组合仍是：

```text
通用代码复核职责
+ 当前仓库权威
+ 当前工程纪律
+ 当前差异 / 源码
+ 按风险激活的技术检查知识
+ 必要时当前官方资料
+ 可选代码智能
```

这已经可以通过现有能力层组合表达。

因此当前不建议：

- 新增复核画像；
- 为 Vue / Spring / Gradle 分别建立复核 Skill；
- 让技术画像复制一套专门复核版本。

只有后续评估证明现有层次无法表达稳定职责时，才重新评估架构层。

## 12. Issue #71 / AR-04 的精确价值

Issue #71 中 AR-04 使用缺陷发现前的 frozen candidate，隐藏后续答案、provenance 与 assertions，对一个真实发生过的架构 sequencing 缺口做独立新上下文盲测。

两组请求：

- `gpt-5.6-sol` / medium；
- `gpt-6-astra` / high。

两者都：

- 给出 `BLOCKING_CONCERN`；
- Human discovery grading 为 `DETECTED`；
- hidden assertions `8 / 8` 通过；
- 独立发现 `contentMigration -> main` 会把 migration tooling 绑定到 server-oriented Spring composition / main classpath；
- 要求先冻结 application / composition / shared-capability boundary，再决定 source set 或 multi-project。

该证据支持两个不同方向，不能混为一个超级复核能力：

1. 高返工技术规划的独立新上下文规划复核值得研究；
2. 独立复核者的确可能在实施前发现真实高代价结构缺陷。

它不证明所有规划都必须二次复核，也不证明昂贵模型必然更好；当前使用方结论仍是低成本且能力足够的复核优先，只有未解决 / 冲突 / 明确需要第二意见时升级。

## 13. 代码复核与现有工程纪律的关系

当前已有三项正式工程纪律：

1. 实现最小化与推测性复杂度控制；
2. 精准修改与差异范围控制；
3. 数据访问作用域与有界性控制。

其中前两项已经覆盖大量“AI 生成代码不应为了未来假想需求制造复杂度”和“变更应保持可解释范围”的问题。

因此本轮不应仅因为提出“AI 友好代码”就新增第四工程纪律。

更稳妥的验证路径是：

- 先把变更局部性、依赖方向、状态所有权、副作用、抽象必要性、间接层成本、契约清晰度、测试接缝等作为未来代码复核评估维度；
- 观察它们是否形成独立、稳定、跨任务的判断模式；
- 只有现有工程纪律无法合理承载且评估反复证明有增量价值时，再考虑第四工程纪律。

## 14. 新上下文必须保留的证据型判断

后续新上下文至少不要丢失以下事实：

1. 当前指南体量集中是事实，但“文件大”不是拆分规则；
2. PR #72 是当前最直接的“已有规则但未可靠激活”仓库证据；
3. CodeGraph 的子代理实测显示，没有短激活入口时能力可见性很差，约 1 / 9 主动加载；加入极短提示后稳定使用；
4. CodeGraph 默认一个强 MCP 入口，并严格控制常驻指令长度；
5. CodeGraph 第一方基准测试只能作为外部参考，不能套用收益比例；
6. `.codegraph/` 是派生索引，不是权威；
7. 使用方应直接消费 CodeGraph 的 MCP / CLI / 索引，而不是复制其内部 Skill；
8. `code-review` 早已存在于 Skill Architecture 的“第一批暂不独立 Skill 化”清单，不是本轮突然新增的想法；
9. 未来 `code-review` 即使成立，也不是“第 10 个核心 Skill”；
10. 当前没有证据新增复核画像架构层；
11. Issue #71 的独立规划复核价值与未来代码复核必须保持职责分离；
12. 当前路线依旧是：先规则治理与知识激活，再重新决策 WI-07 代码复核能力，再由真实评估决定 WI-06。

## 15. 证据来源

### agentic-dev

- `docs/guides/` 当前 GitHub directory metadata；
- PR #72；
- `docs/architecture/skill-architecture.md`；
- `docs/architecture/engineering-disciplines.md`；
- Issue #71。

### CodeGraph

研究基线：2026-09-08，研究时 `main@8df9ecac9ddf49925a6e80c32a89ec91e601ab23`。

重点来源：

- `site/src/content/docs/getting-started/introduction.md`；
- `site/src/content/docs/core-concepts/knowledge-graph.md`；
- `site/src/content/docs/reference/mcp-server.md`；
- `src/mcp/server-instructions.ts`；
- `src/installer/instructions-template.ts`；
- `src/installer/targets/codex.ts`；
- `.claude/skills/agent-eval/SKILL.md`；
- README benchmark / usage material。

这些外部来源只保存研究时可验证的当前事实。CodeGraph 后续变化不会自动改变 `agentic-dev` 当前权威。