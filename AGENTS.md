---
id: repository:agents
type: repository
status: active
---

# AGENTS.md

## 仓库职责

`agentic-dev` 定义通用 AI Agent 驱动软件开发能力，并维护可复用的 Method、Skill、Rule、Architecture 与 Consumer adoption 能力。本文件只维护稳定 Repository Authority、Agent Bootstrap 和启动约束；当前阶段与下一工作入口只由 `docs/project/project-roadmap.md` 与 GitHub 当前事实维护。

GitHub Repository 是本仓库唯一长期项目事实来源。会话历史、其他聊天、个人记忆、其他仓库状态和未固化推理不构成本仓库事实。

## Authority 与 semantic ownership

发生冲突时先判断真实 semantic owner，不用目录层级覆盖正确责任：

1. `AGENTS.md` — Repository Authority / Agent Bootstrap；
2. `docs/architecture/engineering-capability-architecture.md` — 能力类型、single semantic ownership 与双视窗；
3. `docs/architecture/method-architecture.md` — Method 类型与 selection contract；
4. 当前选定的 `docs/methods/*.md` — 当前工作过程模型；
5. 当前责任直接需要的 Architecture；
6. 当前责任适用的具体 `SKILL.md` 与 `docs/rules/**`；
7. `docs/project/project-roadmap.md` — 当前项目阶段 / 下一演进；
8. `docs/guides/**` — Human View；
9. `docs/research/**` — 非规范 Evidence / Reference。

Architecture、Method、Skill、Rule 各自只拥有其语义责任；Guide / README 可以解释它们，但不得成为第二套规范 owner。Research 永远不是规范性 Authority。

## Fresh Context / Agent Bootstrap

新的本仓库上下文按以下顺序恢复：

1. 读取本文件；
2. 读取 `README.md` 与 `docs/project/project-roadmap.md`；
3. 重新读取当前默认分支、Open Issue / PR 和当前任务需要的 GitHub 状态；
4. 判断当前 work kind，并按 **Method Selection** 选择 Method；若无已定义 Method 匹配，不强行套用；
5. 从当前 Method stage / direct responsibility 与仓库事实提取最少量 task signals；
6. 使用 `tools/rule-discovery/` 对 `docs/rules/**` 做候选初筛，只读取返回的 Rule 正文；
7. 需要独立执行能力时，通过 Agent Skills 原生发现选择并读取相应 `SKILL.md`；
8. 只加载当前责任直接需要的 Architecture；Guide / Research 仅在任务明确需要人类说明或研究证据时读取。

不得为了恢复上下文读取全量 Rules、全量 metadata、全部 Skills、全部 Architecture 或完整 Research。ordinary runtime 不得通过目录遍历、Human README、IDE tree 或其他枚举机制把未命中 Rule locator / 文件名集合送入模型上下文；Rule Discovery 返回值是普通运行时获得 Rule locator 的唯一入口。

## Method Selection

当前 Method 数量较少，Bootstrap 只维护稳定 `work kind → Method locator`；Method 正文拥有全部阶段、Gate、返回与完成语义。

- 普通软件 / 产品变更从需求澄清到实现收敛：`docs/methods/ai-development.md`；
- Consumer 首次显式采用 `agentic-dev`：`docs/methods/consumer-adoption.md`；
- Existing Consumer 显式评估 / 升级 upstream baseline：`docs/methods/consumer-upgrade.md`。

如果任务不属于以上 work kind，按 Repository Authority 和当前直接责任工作，不得把最相近 Method 当作默认流程。Method selection 的长期边界见 `docs/architecture/method-architecture.md`。

当 Method 数量或选择歧义增长时，应先用 eval 证明需要更复杂 discovery；不得仅为形式统一复制 Rule Discovery 机制。

## Rule Discovery

Rule metadata 与 Rule 正文必须同源、同文件维护。不得维护 Reviewed Discovery Map、Activation Manifest、Runtime Catalog、rule-index 或其他需要与规则正文同步的中心路由表。

普通运行时使用：

```bash
python3 tools/rule-discovery/rule_discovery.py --repo-root . discover --signals-json '<task-signals-json>'
```

`task-signals-json` 必须显式包含 `phases`、`activities`、`technologies`、`artifacts`、`risks` 五个维度：

- 非空数组：当前事实可安全规范化出的少量已知 token；
- `[]`：当前事实明确没有该维度正向 signal；
- `null`：相关事实未知或无法安全规范化，不能伪装成空数组。

每个非空数组最多 6 个 lowercase kebab-case token。不得把目标 Rule 名、期望答案、Rule 文件名或历史候选写入 signals，也不得使用 synonym cloud 碰撞 metadata。

AI Development 当前 phase token：`clarify-intent`、`specification`、`technical-planning`、`slice-ready`、`execute`、`converge`。其他 Method 若需要 Method-specific Rule，必须先定义稳定 phase identity；未定义时使用 `null` 而不是猜测。

活动优先使用直接责任词，如 `implementation`、`verification`、`review`、`external-operation`、`design`。技术与工件使用当前事实支持的稳定机器身份；例如 Vue 3.x → `vue3`、TypeScript → `typescript`、`.vue` SFC → `vue-sfc`、普通源代码 → `code`、数据库 schema migration → `database-migration`、GitHub Actions → `github-actions`、workflow run → `workflow-run`。

成功结果只把 `candidates[].path` 作为待读取 Rule locator；候选不等于最终适用，必须读取正文后做语义确认。当前 phase / activity / technology / artifact / risk facts 实质变化时重新发现，不把旧 candidate set 当作整个会话永久上下文。

Discovery `fail-closed` 时先修复 signals、metadata 或扫描完整性，不降级到全量 Rule、旧中心 Map 或 upstream discovery。`status=ok` 但候选为空，也不得读取未命中 Rule metadata 反向校准。

Rule root 中文件名恰为 `README.md` 的资源只作为 Human Navigation：不参与 Rule candidate scan，但仍参加 repository Markdown lint；其他 `.md` 不得借此逃逸 Rule contract。

Rule 的语义、粒度与 Consumer-local specialization 见 `docs/architecture/rule-architecture.md`；发现算法、reserved README 与 fail-closed contract 见 `docs/architecture/rule-discovery-architecture.md`。

## Skill / Rule / Guide 边界

- **Skill**：当前责任明确后具有稳定 Trigger / Inputs / Procedure / Outputs / Exit / Escalation 的有界执行能力；
- **Rule**：按当前事实条件性适用的 policy / constraint / default / invariant / completion requirement，可横切 Method、Skill 或 direct work；
- **Guide**：Human-facing explanation / usage / navigation，ordinary Agent runtime 默认不依赖。

Skill 与 Rule 是正交关系，不是上下游流水线。具体边界见 `docs/architecture/engineering-capability-architecture.md`、`skill-architecture.md` 与 `rule-architecture.md`。

## Consumer 边界

Consumer Repository 始终拥有自己的项目事实、需求、架构、代码、验证与权限。`agentic-dev` 只提供可复用能力。

长期 ownership / ordinary runtime 不变量见 `docs/architecture/consumer-architecture.md`；首次 adoption 使用 `docs/methods/consumer-adoption.md`；显式 upstream baseline upgrade 使用 `docs/methods/consumer-upgrade.md`。采用完成后的 ordinary runtime 只依赖 Consumer-local current state，发现失败不能自动回 upstream 补流程或规则。

Rule 是 Consumer-local policy specialization 的主要承载面之一；通用 Skill 不应吸收不同 Consumer 必然不同的 commit type / scope、术语、审批或局部技术 policy。

## 外部操作与复核

外部可变状态操作可使用 `external-operation` Skill，并通过 Rule Discovery 加载当前适用的授权、写后验证、异步观察、共享资源等 operation Rules。Rule 也可以在没有该 Skill 的其他 external work 中独立适用。

工具可写不等于已授权；merge、release、deploy、破坏性远程操作仍服从仓库策略和人工 Authority。

高影响仓库变更按 `rule:high-impact-ai-review-required` 判断是否必须执行 `review-change`。Review 通过不等于人工批准或集成授权。

## Human View / Research

人类从 `README.md` 与 `docs/guides/**` 理解项目。Guide 可以完整解释 Method / Architecture / Skill / Rule，但不得保存 runtime routing、canonical Gate 或 current project state。

`docs/research/**` 只保存外部规范、工程证据和设计参考，不参与 ordinary runtime discovery，也不自动改变规范能力。长期结论只有进入真实 current owner 后才成为规范。

## Project State

`docs/project/` 只保留真正当前的 `project-roadmap.md`。临时计划、Gate 过程、资产分类、实验结果和阶段验证优先记录在 GitHub Issue / PR / Git / Actions，不为每次演进建立第二套 current state。

## Git 与表达

Git commit、中文人类表达、精确机器标识符和正式概念身份等运行约束由 `docs/rules/repository/**` 按 task signals 发现；本文件不复制第二份 Rule 正文。