---
id: repository:agents
type: repository
status: active
---

# AGENTS.md

## 仓库职责

`agentic-dev` 定义通用 AI Agent 驱动软件开发方法，并维护可复用的 Method、Skill、Rule、架构与 Consumer adoption 能力。本文件只维护稳定的 Repository Authority、Agent Bootstrap 和启动约束；当前阶段与下一工作入口只由 `docs/project/project-roadmap.md` 与 GitHub 当前事实维护。

GitHub Repository 是本仓库唯一长期项目事实来源。会话历史、其他聊天、个人记忆、其他仓库状态和未固化推理不构成本仓库事实。

## Authority

发生冲突时先按 semantic owner 判断，不以目录层级覆盖真实 owner。稳定 Authority / capability contracts 包括：

1. `AGENTS.md` — Repository Authority / Agent Bootstrap；
2. `docs/architecture/engineering-capability-architecture.md` — 能力类型与双视窗；
3. `docs/architecture/method-architecture.md` — Method 类型与 selection contract；
4. 当前选定的 `docs/methods/*.md` — 当前工作过程模型；
5. `docs/methods/principles.md` — 跨 Method 顶层方法原则；
6. 当前责任直接需要的 Architecture；
7. 当前责任适用的具体 `SKILL.md` 与 `docs/rules/**`；
8. `docs/project/project-roadmap.md` — 当前项目阶段 / 下一演进；
9. `docs/guides/**` — Human View；
10. `docs/research/**` — 非规范 Evidence / Reference。

Architecture、Method、Skill、Rule 各自只拥有其语义责任；Guide / README 可以解释它们，但不得成为第二套规范 owner。Research 永远不是规范性 Authority。

## Fresh Context / Agent Bootstrap

新的本仓库上下文按以下顺序恢复：

1. 读取本文件；
2. 读取 `README.md` 与 `docs/project/project-roadmap.md`；
3. 重新读取当前默认分支、Open Issue / PR 和当前任务需要的 GitHub 状态；
4. 判断当前 work kind，并按 **Method Selection** 选择 Method；若无已定义 Method 匹配，不强行套用；
5. 从当前 Method stage / direct responsibility 与仓库事实提取最少量 task signals；
6. 使用 `tools/rule-discovery/` 对 `docs/rules/**` 的 YAML Front Matter 做候选初筛，只读取返回的候选 Rule 正文；
7. 需要独立执行能力时，通过 Agent Skills 原生发现选择并读取相应 `SKILL.md`；
8. 只加载当前责任直接需要的 Architecture；Guide / Research 仅在任务明确需要人类说明或研究证据时读取。

不得为了恢复上下文读取全量 Rules、全量 metadata、全部 Skills、全部 Architecture 或完整 Research。ordinary runtime 不得通过 `rg --files`、`find`、目录遍历、IDE tree、脚本或其他方式预先枚举 `docs/rules/**` 的完整 locator / 文件名集合；Rule Discovery 的返回值是普通运行时获得 Rule locator 的唯一入口。

## Method Selection

当前 Method 数量较少，Bootstrap 只维护稳定 `work kind → Method locator`；Method 正文拥有全部阶段、Gate、返回与完成语义。

- 普通软件 / 产品变更从需求澄清到实现收敛：`docs/methods/ai-development.md`；
- Consumer 首次显式采用 `agentic-dev`：`docs/methods/consumer-adoption.md`；
- Existing Consumer 显式评估 / 升级 upstream baseline：`docs/methods/consumer-upgrade.md`。

如果任务不属于以上 work kind，按 Repository Authority 和当前直接责任工作，不得把最相近 Method 当作默认流程。Method selection 的长期边界见 `docs/architecture/method-architecture.md`。

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

AI Development 的阶段 token 继续使用：`clarify-intent`、`specification`、`technical-planning`、`slice-ready`、`execute`、`converge`。其他 Method 如需新的稳定 phase token，必须由对应 Method / Rule Discovery contract 明确定义后才能使用；不得把自然语言阶段名直接猜成 token。

活动优先使用直接责任词，如 `implementation`、`verification`、`review`、`external-operation`、`design`。技术与工件使用当前事实的稳定机器身份；常见规范化示例：Vue 3.x → `vue3`、TypeScript → `typescript`、`.vue` SFC → `vue-sfc`、普通源代码 → `code`、数据库 schema migration → `database-migration`、GitHub Actions → `github-actions`、workflow run → `workflow-run`。这些只是 token 规范化，不构成 Rule→token 路由表。

成功结果只把 `candidates[].path` 作为待读取 Rule locator；候选本身不等于最终适用，必须读取候选正文后做语义确认。若某个维度的 canonical token 不确定，优先用 `null` 保留未知语义，而不是读取未命中 Rule 的 Front Matter 反向推断 token。除 Discovery 返回的 `candidates[].path` 外，ordinary runtime 不得提前枚举、读取或把其他 Rule locator 送入模型上下文。

当当前 phase、activity、technology、artifact 或 risk facts 发生会改变候选集合的实质变化时，重新执行 discovery，不把旧 candidate set 当作整个会话永久上下文。Discovery 返回 `fail-closed` 时停止依赖其结果，修复当前 signals、metadata 或扫描完整性后重试；不得降级到全量 Rule 加载、旧中心 Map 或 upstream discovery。`status=ok` 但候选为空也不得通过读取未命中 Rule metadata 进行校准；只能基于新的当前事实重新发现，或明确保留规则发现缺口。

Rule Discovery Tool 只返回少量 `{id, path}` locator；LLM 读取候选正文后完成最终语义适用性判断。目录路径不得成为隐藏匹配条件。schema、重复 id 或扫描完整性异常必须失败关闭。

Rule 的语义、粒度与 Consumer-local specialization 见 `docs/architecture/rule-architecture.md`；发现算法见 `docs/architecture/rule-discovery-architecture.md`。

## Skill / Rule / Guide 边界

- Skill：当前责任明确后具有稳定 Trigger / Inputs / Procedure / Outputs / Exit / Escalation 的有界执行能力；
- Rule：按当前事实条件性适用的 policy / constraint / default / invariant / completion requirement，可横切 Method、Skill 或 direct work；
- Guide：Human-facing explanation / usage / navigation，ordinary Agent runtime 默认不依赖。

Skill 与 Rule 不是上下游关系。具体边界见 `docs/architecture/engineering-capability-architecture.md`、`skill-architecture.md` 与 `rule-architecture.md`。

## Consumer 边界

Consumer Repository 始终拥有自己的项目事实、需求、架构、代码、验证与权限。`agentic-dev` 只提供可复用方法和能力。

长期 ownership / ordinary runtime 不变量见 `docs/architecture/consumer-architecture.md`；首次 adoption 使用 `docs/methods/consumer-adoption.md`；显式 upstream baseline upgrade 使用 `docs/methods/consumer-upgrade.md`。采用完成后的 ordinary runtime 只依赖 Consumer-local current state，发现失败不能自动回到 upstream 补流程或规则。

## 外部操作与复核

外部可变状态操作使用 `external-operation` Skill，并通过 Rule Discovery 加载当前适用的授权、写后验证、异步观察、共享资源等 operation Rules。工具可写不等于已授权；merge、release、deploy、破坏性远程操作仍服从仓库策略和人工权威。

高影响仓库变更按 `rule:high-impact-ai-review-required` 判断是否必须执行 `review-change`。Review 通过不等于人工批准或集成授权。

## 研究

`docs/research/**` 只保存外部规范、工程证据和设计参考，不参与 ordinary runtime discovery，也不自动改变 Method / Architecture / Rule / Skill。长期结论只有进入真实 current owner 后才成为规范。

## Project State

`docs/project/` 只保留真正当前的 `project-roadmap.md`。临时计划、Gate 过程、资产分类、实验结果和阶段验证优先记录在 GitHub Issue / PR / Git / Actions，不为每次演进建立第二套 current state。

## Git 与表达

Git commit、中文人类表达、精确机器标识符和正式概念身份等运行约束由 `docs/rules/repository/**` 按 task signals 发现；本文件不复制第二份规则正文。