---
id: repository:agents
type: repository
status: active
---

# AGENTS.md

## 仓库职责

`agentic-dev` 定义通用 AI Agent 驱动软件开发能力，并维护可复用的 Method、Skill、Rule、Architecture 与 Consumer adoption 能力。本文件只维护稳定 Repository Authority、Agent Bootstrap 和启动约束；`agentic-dev` 自身的使命、capability instance、Roadmap 与演进摘要由 `docs/project/**` 的真实 Project owner 分别持有。

GitHub Repository 是本仓库唯一长期项目事实来源。会话历史、其他聊天、个人记忆、其他仓库状态和未固化推理不构成本仓库事实。

## 权威与语义归属

发生冲突时先判断真实 semantic owner，不用目录层级覆盖正确责任：

1. `AGENTS.md` — Repository Authority / Agent Bootstrap；
2. `docs/project/project-charter.md` — `agentic-dev` 自身使命、目标、非目标与核心项目需求；
3. `docs/architecture/engineering-capability-architecture.md` — capability 类型、single semantic ownership 与双视窗；
4. `docs/architecture/project-knowledge-architecture.md` — Project Knowledge 与 reusable Capability 的长期边界；
5. `docs/project/project-capability-profile.md` — 当前 Repository 的 capability instance / Method selector / runtime locator；
6. `docs/architecture/method-architecture.md` — Method 类型与通用 selection contract；
7. 当前选定的 `docs/methods/*.md` — 当前工作过程模型；
8. 当前责任直接需要的其他 Architecture；
9. 当前责任适用的具体 `SKILL.md` 与 `docs/rules/**`；
10. `docs/project/project-roadmap.md` — 当前项目 baseline / evolution / gate / next candidates；
11. `docs/guides/**` — Human View；
12. `docs/research/**` — 非规范 Evidence / Reference。

Architecture、Method、Skill、Rule 各自只拥有其 capability 语义责任；Project owner 只拥有当前 Repository 的使命、实例、状态和稳定演进摘要；Guide / README 可以解释它们，但不得成为第二套规范 owner。Research 永远不是规范性 Authority。

## Fresh Context / Agent 启动

新的本仓库上下文按以下顺序恢复：

1. 读取本文件；
2. 读取 `docs/project/project-roadmap.md` 与 `docs/project/project-capability-profile.md`；`README.md` 属于 Human View，不作为 ordinary Agent 的固定启动输入；
3. 重新读取当前默认分支、Open Issue / PR 和当前任务需要的 GitHub 状态；
4. 若当前任务需要理解 `agentic-dev` 项目使命、目标或核心项目需求，再读取 `docs/project/project-charter.md`；
5. 直接使用 `project-capability-profile.md` 的 Repository-local selector instance 选择并读取当前 Method；只有当前任务修改 / 复核 Method 类型、selection contract、selector scaling 或 no-match 语义时，才按需读取 `docs/architecture/method-architecture.md`；若无映射匹配，不强行套用；
6. 从当前 Method stage / direct responsibility 与仓库事实提取最少量 task signals；Method-specific phase token 只能来自当前 Method canonical owner；
7. 按当前 Project Capability Profile 声明的 Rule Discovery instance 执行候选初筛，只读取返回的 Rule 正文；在开始当前 direct responsibility 的首个有副作用动作前必须完成本次 task-level discovery；direct responsibility 或其关键事实实质变化后，在下一次有副作用动作前重新发现；
8. 需要独立执行能力时，通过当前 Repository 声明的 Skill discovery 入口选择并读取相应 `SKILL.md`；
9. 只加载当前责任直接需要的其他 Architecture；Guide / Research / Project Evolution 仅在任务明确需要人类说明、研究证据或历史原因时读取。

不得为了恢复上下文读取全量 Rules、全量 metadata、全部 Skills、全部 Architecture、完整 Research 或完整 Project Evolution。ordinary runtime 不得通过目录遍历、Human README、IDE tree 或其他枚举机制把未命中 Rule locator / 文件名集合送入模型上下文；Rule Discovery 返回值是普通运行时获得 Rule locator 的唯一入口。

## Method 选择

`docs/architecture/method-architecture.md` 只定义通用 Method Selection Contract；当前 `agentic-dev` 的 `work kind → Method locator` 映射由 `docs/project/project-capability-profile.md` 单独拥有。

ordinary Bootstrap 直接消费 Project Capability Profile 的 local selector，不固定预读 Method Architecture。只有 selection contract 本身进入当前责任、selector 无法解释当前 work kind，或需要评估 selector scaling / no-match 行为时，才加载 Method Architecture。Bootstrap 不复制 selector mapping、Method stages 或 Gate；如果没有 local selector 匹配，继续按 Repository Authority 与当前 direct responsibility 工作，不得从 Guide、目录名或历史会话猜测流程。

## Rule Discovery

Rule metadata 与 Rule 正文必须同源、同文件维护。不得维护 Reviewed Discovery Map、Activation Manifest、Runtime Catalog、rule-index 或其他需要与规则正文同步的中心路由表。

当前 Repository 的 Rule root、Tool locator、ordinary invocation 与 Human inventory 由 `docs/project/project-capability-profile.md` 声明；通用信号、匹配、渐进披露与 fail-closed contract 由 `docs/architecture/rule-discovery-architecture.md` 持有。Bootstrap 不复制第二份 Tool path 或完整 invocation contract。

GitHub Actions 中名为 `Rule Discovery` 的 workflow 有两种职责，必须区分：

- `pull_request` / `push(master)` 继续只执行 repository lint、deterministic tests 与固定 smoke 场景；这些通过结果 **不能替代** 当前 task signals 的 task-level discovery；
- 参数化 task-level invocation 会 checkout 请求中的 exact commit SHA，并调用该 SHA 自身的 Rule Discovery Tool；当前 Repository 的具体云端入口与请求格式由 Project Capability Profile 持有。

调用 Rule Discovery 本身属于 **preflight infrastructure invocation**：它只计算候选、不得修改项目语义或授予后续动作权限，因此不要求先递归执行另一轮 Rule Discovery。得到候选后，任何真正的 Repository / Issue / PR / workflow / deploy / external state 副作用仍必须遵守当前责任的 discovery 结果与其他 Authority。

`task-signals-json` 必须显式包含 `phases`、`activities`、`technologies`、`artifacts`、`risks` 五个维度：

- 非空数组：当前事实可安全规范化出的少量已知 token；
- `[]`：当前事实明确没有该维度正向 signal；
- `null`：相关事实未知或无法安全规范化，不能伪装成空数组。

每个非空数组最多 6 个 lowercase kebab-case token。不得把目标 Rule 名、期望答案、Rule 文件名或历史候选写入 signals，也不得使用 synonym cloud 碰撞 metadata。

`phases` token 只能来自当前 selected Method 自己定义的 stable phase identity；当前 Method 未定义或无法安全判断时使用 `null`，不得由本 Bootstrap、Rule Discovery Architecture、其他 Method 或未命中 Rule metadata 猜测。

活动优先使用直接责任词，如 `implementation`、`verification`、`review`、`external-operation`、`design`。技术与工件使用当前 Repository 事实支持的稳定机器身份；具体技术 token 由目标 Repository 的代码、依赖、配置和 local Rule corpus 决定，本 Bootstrap 不维护跨项目技术词表。通用工件可使用 `code`、`database-migration`、`workflow-run` 等稳定身份；平台事实如 GitHub Actions 可使用 `github-actions`。

准备请求人工执行动作、提供输入、作出决定或充当系统 / 工具之间的中转时，视为新的 human escalation responsibility checkpoint。**发出人工请求前**，`activities` 至少包含 `human-escalation`，`risks` 至少包含 `human-intervention`，并重新执行 Rule Discovery；Bootstrap 只拥有这次 signal transition，不复制“是否确需人工、怎样缩减人工动作”的 Rule 正文。

成功结果只把 `candidates[].path` 作为待读取 Rule locator；候选不等于最终适用，必须读取正文后做语义确认。进入新的 direct responsibility，或当前 phase / activity / technology / artifact / risk facts 实质变化时，都必须在继续该责任的有副作用动作前重新发现；旧 candidate set 不跨职责永久有效。

Discovery `fail-closed` 时先修复 signals、metadata 或扫描完整性，不降级到全量 Rule、旧中心 Map 或 upstream discovery。`status=ok` 但候选为空，也不得读取未命中 Rule metadata 反向校准。

Rule root 中文件名恰为 `README.md` 的资源只作为 Human Navigation：不参与 Rule candidate scan，但仍参加 repository Markdown lint；其他 `.md` 不得借此逃逸 Rule contract。

Rule 的语义、粒度与 Consumer-local specialization 见 `docs/architecture/rule-architecture.md`；发现算法、reserved README 与 fail-closed contract 见 `docs/architecture/rule-discovery-architecture.md`。

## Skill / Rule / Guide 边界

- **Skill**：当前责任明确后具有稳定 Trigger / Inputs / Procedure / Outputs / Exit / Escalation 的有界执行能力；
- **Rule**：按当前事实条件性适用的 policy / constraint / default / invariant / completion requirement，可横切 Method、Skill 或 direct work；
- **Guide**：Human-facing explanation / usage / navigation，ordinary Agent runtime 默认不依赖。

Skill 与 Rule 是正交关系，不是上下游流水线。具体边界见 `docs/architecture/engineering-capability-architecture.md`、`skill-architecture.md` 与 `rule-architecture.md`。

## Project / Capability 边界

`docs/project/**` 描述 `agentic-dev` 这个具体 Repository：使命、核心项目需求、当前 capability instance、Roadmap 与稳定演进摘要。

`docs/architecture/**`、`docs/methods/**`、`skills/**`、`docs/rules/**` 与相应 tool contract 描述可被其他 Repository adopt / adapt 的 Capability。

核心原则：**Project 不传播，Capability 传播。** 具体 contract 见 `docs/architecture/project-knowledge-architecture.md`。

## Consumer 边界

Consumer Repository 始终拥有自己的项目事实、Project Knowledge、需求、架构、代码、验证与权限。`agentic-dev` 只提供可复用 capability。

长期 ownership / ordinary runtime 不变量见 `docs/architecture/consumer-architecture.md`。首次 adoption 与显式 upstream baseline upgrade 使用对应 Method，但 upstream `Project Charter / Capability Profile / Roadmap / Evolution` 只可作为 provenance / context，不自动成为 Consumer Authority。

Consumer 必须建立自己的 local Project Knowledge、Method selector、Rule Discovery instance 与 Skill entry。采用完成后的 ordinary runtime 只依赖 Consumer-local current state，发现失败不能自动回 upstream 补流程或规则。

Rule 是 Consumer-local policy specialization 的主要承载面之一；通用 Skill 不应吸收不同 Consumer 必然不同的 commit type / scope、术语、审批或局部技术 policy。

## 外部操作与复核

外部可变状态操作可使用 `external-operation` Skill，并通过 Rule Discovery 加载当前适用的授权、写后验证、异步观察、共享资源等 operation Rules。Rule 也可以在没有该 Skill 的其他 external work 中独立适用。

工具可写不等于已授权；merge、release、deploy、破坏性远程操作仍服从仓库策略和人工 Authority。

高影响仓库变更按当前 Rule Discovery 发现的 review requirement 判断是否必须执行 `review-change`。Review 通过不等于人工批准或集成授权。

## Human View / Research

人类从 `README.md` 与 `docs/guides/**` 理解 capability，从 `docs/project/README.md` 理解 `agentic-dev` 自身 Project Knowledge。Guide / README 可以完整解释 canonical owner，但不得保存第二套 runtime routing、Gate 或 Project current state。

`docs/research/**` 只保存外部规范、工程证据和设计参考，不参与 ordinary runtime discovery，也不自动改变规范能力。长期结论只有进入真实 current owner 后才成为规范。

## Project Knowledge

当前长期 Project owners：

- `docs/project/project-charter.md` — 使命、目标、非目标、核心项目需求与成功判据；
- `docs/project/project-capability-profile.md` — 当前 capability instance 与 Repository-local locator；
- `docs/project/project-roadmap.md` — 当前 baseline / evolution / gate / next candidates；
- `docs/project/project-evolution.md` — 稳定历史里程碑摘要。

Open PR / Issue、branch、Actions、review 与 commit 等 live state 始终重新从 GitHub 读取。临时计划、Gate 流水账、实验日志和阶段验证优先记录在 Issue / PR / Git / Actions，不为每次演进建立新的 Project Markdown owner。

## Git 与表达

Git commit、中文人类表达、精确机器标识符和正式概念身份等运行约束由当前 Rule Discovery 按 task signals 发现；本文件不复制 Rule path inventory 或第二份 Rule 正文。