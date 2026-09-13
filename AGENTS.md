---
id: repository:agents
type: repository
status: active
---

# AGENTS.md

## 仓库职责

`agentic-dev` 定义通用 AI Agent 驱动软件开发方法，并维护可复用的 Skill、Rule、架构与 Consumer adoption 能力。本文件只维护稳定的 Repository Authority、知识边界和启动约束；当前阶段与下一工作入口只由 `docs/project/project-roadmap.md` 与 GitHub 当前事实维护。

GitHub Repository 是本仓库唯一长期项目事实来源。会话历史、其他聊天、个人记忆、其他仓库状态和未固化推理不构成本仓库事实。

## Authority

发生冲突时，先按语义 owner 判断，再服从以下层级：

1. `AGENTS.md`；
2. `docs/method/ai-development-method.md`；
3. `docs/method/principles.md`；
4. `docs/architecture/engineering-capability-architecture.md`；
5. `docs/architecture/consumer-lifecycle.md`；
6. `docs/architecture/skill-architecture.md`；
7. `docs/architecture/rule-discovery-architecture.md`；
8. 当前任务适用的 `docs/rules/**` 与具体 `SKILL.md`；
9. `docs/project/project-roadmap.md`；
10. `docs/guides/**`；
11. `docs/research/**`。

Rule 可以约束 Skill 的阶段内执行，但不得重定义 Method / Architecture；Skill 拥有自己的 Procedure，但不得通过实现暗中修改更高层 Authority。Guide 只面向人类初始化、采用、升级和低频说明，不拥有 ordinary runtime 规则。Research 永远不是规范性 Authority。

## Fresh Context

新的本仓库上下文按以下顺序恢复：

1. 读取本文件；
2. 读取 `README.md` 与 `docs/project/project-roadmap.md`；
3. 重新读取当前默认分支、Open Issue / PR 和当前任务需要的 GitHub 状态；
4. 从当前任务与仓库事实提取最少量 task signals；
5. 使用 `tools/rule-discovery/` 对 `docs/rules/**` 的 YAML Front Matter 做候选初筛，只读取返回的候选 Rule 正文；
6. 需要独立执行能力时，通过 Agent Skills 原生发现选择并读取相应 `SKILL.md`；
7. 只加载当前任务直接需要的 Method / Architecture / Guide / Research。

不得为了恢复上下文读取全量 Rules、全量 metadata、全部 Skills 或完整 Research。

## Rule Discovery

Rule metadata 与 Rule 正文必须同源、同文件维护。不得维护 Reviewed Discovery Map、Activation Manifest、Runtime Catalog、rule-index 或其他需要与规则正文同步的中心路由表。

普通运行时使用以下稳定入口：

```bash
python3 tools/rule-discovery/rule_discovery.py --repo-root . discover --signals-json '<task-signals-json>'
```

`task-signals-json` 必须显式包含 `phases`、`activities`、`technologies`、`artifacts`、`risks` 五个维度。每个维度使用以下三态语义：

- 非空数组：当前事实能够安全规范化出的少量已知 token；
- `[]`：当前事实明确没有该维度的正向 signal；
- `null`：该维度相关事实未知，或无法在不猜测的情况下确定 canonical token；未知不得伪装成空数组，也不得通过同义词堆叠碰撞 metadata。

每个非空数组最多 6 个 lowercase kebab-case token。不得把目标 Rule 名、期望答案、Rule 文件名或会话历史写入 signals，也不得为了让候选出现而批量添加同义词、推测风险或近义技术名。

阶段 token 使用 Method 的稳定阶段身份：`clarify-intent`、`specification`、`technical-planning`、`slice-ready`、`execute`、`converge`。活动优先使用直接责任词，如 `implementation`、`verification`、`review`、`external-operation`、`design`。技术与工件使用当前事实的稳定机器身份；常见规范化示例：Vue 3.x → `vue3`、TypeScript → `typescript`、`.vue` SFC → `vue-sfc`、普通源代码 → `code`、数据库 schema migration → `database-migration`、GitHub Actions → `github-actions`、workflow run → `workflow-run`。这些只是 token 规范化，不构成 Rule→token 路由表。

成功结果只把 `candidates[].path` 作为待读取 Rule locator；候选本身不等于最终适用，必须读取候选正文后做语义确认。若某个维度的 canonical token 不确定，优先用 `null` 保留未知语义，而不是读取未命中 Rule 的 Front Matter 反向推断 token。

当当前 phase、activity、technology、artifact 或 risk facts 发生会改变候选集合的实质变化时，重新执行 discovery，不把旧 candidate set 当作整个会话永久上下文。Discovery 返回 `fail-closed` 时停止依赖其结果，修复当前 signals、metadata 或扫描完整性后重试；不得降级到全量 Rule 加载、旧中心 Map 或 upstream discovery。`status=ok` 但候选为空也不得通过读取未命中 Rule metadata 进行校准；只能基于新的当前事实重新发现，或明确保留规则发现缺口。

Rule Discovery Tool 只返回少量 `{id, path}` locator；LLM 读取候选正文后完成最终语义适用性判断。目录路径不得成为隐藏匹配条件。schema、重复 id 或扫描完整性异常必须失败关闭。

## Skill / Rule / Guide 边界

- Skill：具有稳定 Trigger / Inputs / Procedure / Outputs / Exit / Escalation 的独立执行闭环；
- Rule：执行工作时必须遵守的条件、约束、默认值、不变量或完成声明要求，但本身不是完整任务流程；
- Guide：面向人的初始化、adoption、upgrade、恢复和低频说明。

具体架构见 `docs/architecture/skill-architecture.md` 与 `docs/architecture/rule-discovery-architecture.md`。

## Consumer 边界

Consumer Repository 始终拥有自己的项目事实、需求、架构、代码、验证与权限。`agentic-dev` 只提供可复用方法和能力。

首次采用或显式升级时可以读取上游；采用完成后的 ordinary runtime 只依赖 Consumer-local current Method / Skills / Rules / Repository Authority。发现失败不能自动回到 upstream 补规则。长期生命周期见 `docs/architecture/consumer-lifecycle.md`。

## 外部操作与复核

外部可变状态操作使用 `external-operation` Skill，并通过 Rule Discovery 加载当前适用的授权、写后验证、异步观察、共享资源等 operation Rules。工具可写不等于已授权；merge、release、deploy、破坏性远程操作仍服从仓库策略和人工权威。

高影响仓库变更按 `rule:high-impact-ai-review-required` 判断是否必须执行 `review-change`。Review 通过不等于人工批准或集成授权。

## 研究

`docs/research/**` 只保存外部规范、工程证据和设计参考，不参与 ordinary runtime discovery，也不自动改变 Method / Architecture / Rule / Skill。长期结论只有进入真实 current owner 后才成为规范。

## Project State

`docs/project/` 只保留真正当前的 `project-roadmap.md`。临时计划、Gate 过程、资产分类、实验结果和阶段验证优先记录在 Issue #122、PR、Git commit 与 Actions，不为 V4 再建立一组过程 Markdown。

## Git 与表达

Git commit、中文人类表达、精确机器标识符和正式概念身份等运行约束由 `docs/rules/repository/**` 按 task signals 发现；本文件不复制第二份规则正文。