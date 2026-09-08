# 规则激活审计基线

审计日期：2026-09-08

审计阶段：**规则治理与知识激活 v1 / 阶段 A / A1 — 建立审计基线**

文档性质：**研究证据 / 审计基线**

本文只冻结阶段 A 后续审计所需的当前仓库基线、高影响交叉入口和历史失效场景候选。本文不是规范性权威，不修改方法、架构、技能契约、指南行为或项目路线；规则单元的正式切分、重复 / 冲突判断和失效类型分类分别留给 A2～A5。

## 1. 当前仓库基线

当前 `master`：

`c5ac53a7e5d6dbbb9d585c824bcd76c16bb0299c`

该提交是 PR #74 `docs(governance): 启动规则治理与知识激活 v1` 的 squash merge 提交。

当前活动有限里程碑：

> **规则治理与知识激活 v1**

跟踪入口：Issue #73。

当前下一实际门禁：

> **阶段 A — 激活审计**

A1 建立本基线时：

- 开放 PR：`0`；
- 开放 Issue：#73、#71、#58；
- #73 是当前活动里程碑跟踪入口；
- #71 继续作为独立高风险规划复核 / 模型路由研究输入；
- #58 继续作为长期使用方经验反馈入口；
- WI-06、WI-07、WI-09、第四工程纪律和 `code-review` 实现均未启动。

本状态只用于冻结 A1 审计起点；后续阶段恢复时仍应重新读取 GitHub 当前状态。

## 2. 当前审计输入身份

### 2.1 两份高影响指南

| 文件 | 当前 blob SHA | A1 角色 |
|---|---|---|
| `docs/guides/using-agentic-dev.md` | `b8ccf80a5e8c14560a7bfd77450045e55ccbfaf1` | 使用方权威、项目恢复、执行职责、验证、路线图与基线升级等使用规则的主要指南 |
| `docs/guides/external-operation-guidelines.md` | `f22de650351b89563a70653d4fdb96d4f24e6be3` | 外部写操作、权限、人工介入、异步闭环、共享资源、临时证据与 GitHub 协作的主要指南 |

两份指南都位于 `master@c5ac53a7e5d6dbbb9d585c824bcd76c16bb0299c`。

研究附录记录的体量基线为：

- `using-agentic-dev.md`：37,157 bytes；
- `external-operation-guidelines.md`：18,733 bytes；
- 两者合计约 55.9 KB，占当前 `docs/guides/` 总体量约 73%。

这些数字只说明知识集中程度，不构成拆分条件。

### 2.2 直接交叉的仓库入口

| 入口 | 当前 blob SHA | 与后续激活审计的关系 |
|---|---|---|
| `AGENTS.md` | `708dd8819f7dc6160655ea0f39472be0b14e55aa` | 常驻仓库权威、知识边界、渐进式披露、当前证据、人工 / 集成边界、外部操作摘要、AI 复核入口 |
| `README.md` | `d3e14f55092f298936d482b25dca36e5276f954f` | 稳定启动入口、当前路线指针、核心原则摘要、使用指南入口 |
| `docs/project/project-roadmap.md` | `d4d1d9f05c205964b9cb87b6258ab34ac863f4eb` | 当前里程碑、下一门禁、新上下文恢复顺序 |
| `skills/slice-work/SKILL.md` | `ffebf73f0b1f9213fe1334b94d2a360b10678d63` | 规划候选与候选执行单元身份、最小上下文、规格追踪 |
| `skills/readiness-check/SKILL.md` | `6745eb0af71f6cf920479ecc5fe47db7bbd59e80` | 就绪门禁、上游返回、旧候选 / 旧就绪证据失效与重新进入 |
| `skills/execute-unit/SKILL.md` | `c71ddd23d20b3a14c9cb19a38f6e8d6cbedcf46e` | 单执行单元新上下文、当前仓库状态、当前验证证据、按需 GitHub Actions 验证 |
| `skills/converge/SKILL.md` | `363d9b21744cb5a04d16102dd7243446d2d19b83` | 整体证据重建、长期产物闭环、项目路线图状态检查、集成决策边界 |
| `skills/github-actions-verification/SKILL.md` | `5040e60a8a2274d8fead8375aaf66311392769ce` | 声明 / 风险到实际触发拓扑、异步运行、共享资源、临时证据和可观察性 |

A1 只登记这些高影响交叉入口，不把“出现相同主题”直接判定为重复错误。部分重复可能是必要的常驻摘要、激活提示或职责实现；A4 再区分合理摘要 / 指针与实质重复权威。

## 3. 高影响交叉主题清单

以下主题已经能从当前仓库观察到跨指南、常驻入口、技能或项目入口重复出现。这里只冻结后续审计对象，不在 A1 决定规则单元边界或删除 / 合并动作。

| 编号 | 高影响主题 | 当前主要入口 | A1 观察 | 后续主要处理 |
|---|---|---|---|---|
| X-01 | 仓库权威与知识边界 | `AGENTS.md`、README、`using-agentic-dev.md`、多个技能 `Authority Sources` / `Context Rules` | 同一不变量既作为常驻原则出现，也作为使用方 / 技能局部约束出现 | A2 / A4 |
| X-02 | 渐进式披露与新上下文恢复 | `AGENTS.md`、Roadmap、`using-agentic-dev.md`、`slice-work`、`readiness-check`、`execute-unit`、`converge` | “只加载当前必要上下文”和“不依赖会话历史”具有跨任务常驻价值，同时存在任务专项展开 | A2 / A4 |
| X-03 | 项目路线图生命周期与集成后稳定状态 | `using-agentic-dev.md`、`AGENTS.md` AI 复核入口、Roadmap、`converge` | 这是已知出现过“规则存在但未可靠进入正确复核路径”的高风险主题 | A2 / A4 / A5 |
| X-04 | 规划候选、候选执行单元与就绪执行单元身份 | `using-agentic-dev.md`、`slice-work`、`readiness-check`、README 流程摘要 | 使用指南和两个技能都表达身份晋升边界；需要确认哪些是职责实现、哪些只是激活提示 | A2 / A4 / A5 |
| X-05 | 上游语义修订后的就绪回退与重新切分 | `using-agentic-dev.md`、`readiness-check` | 规则既存在于使用指南，也进入门禁技能；历史上出现过旧候选 / 旧 Gate basis 被误认为可继续使用的风险 | A2 / A4 / A5 |
| X-06 | 当前证据与完成声明 | `AGENTS.md`、README、`using-agentic-dev.md`、`execute-unit`、`converge`、`external-operation-guidelines.md` | “没有当前证据不得声明完成”是常驻不变量，但不同职责需要不同声明粒度 | A2 / A3 / A4 |
| X-07 | 验证声明 / 风险与实际触发拓扑 | `using-agentic-dev.md`、`execute-unit`、`github-actions-verification` | 通用使用规则与平台专项技能均表达验证触发责任，需要确认最小激活入口 | A2 / A4 / A5 |
| X-08 | 外部写操作的读取 → 写入 → 重新读取闭环 | `AGENTS.md`、`external-operation-guidelines.md`、`github-actions-verification` | AGENTS 保存薄摘要，指南展开完整规则，平台技能再次具体化；属于典型“常驻核心 + 条件规则”候选结构 | A3 / A4 |
| X-09 | 异步运行、共享资源、所有者 / 租约与有界观察 | `external-operation-guidelines.md`、`github-actions-verification` | 通用外部操作语义与 GitHub Actions 平台实现交叉，不能因同题出现就判定重复 | A3 / A4 / A5 |
| X-10 | 临时执行证据晋升为已接受持久输入 | `using-agentic-dev.md` 验证段落、`external-operation-guidelines.md` §5.3、`github-actions-verification` | 当前存在较完整的跨层重复表达，是 A4 应重点判断“必要职责消费还是实质重复”的对象 | A2 / A3 / A4 |
| X-11 | 人工介入与集成授权 | `AGENTS.md`、README、`using-agentic-dev.md`、`external-operation-guidelines.md`、`converge`、`github-actions-verification` | 人工 / 集成边界既是常驻安全不变量，也是外部操作与收敛职责的退出条件 | A2 / A3 / A4 |
| X-12 | 既有使用方基线升级与本地规则可发现性 | `using-agentic-dev.md` §6.1、README 启动入口、Issue #33 / #52 使用方证据 | 需要区分上游可复用规则、`agentic-dev` 项目规则与使用方本地权威；历史上有真实新上下文可发现性摩擦 | A2 / A4 / A5 |
| X-13 | 中文表达与外部协作语言 | `AGENTS.md`、README、`external-operation-guidelines.md`、术语指南 | 已有明确最高层语言规则，同时外部协作指南保留条件性入口；后续需确认其是否只是合理激活摘要 | A3 / A4 |

该清单只用于保证后续审计不遗漏高影响交叉面。A2 / A3 仍必须按语义重新枚举规则激活单元，不能把本表编号直接当成最终规则 ID。

## 4. 历史失效场景候选

A1 冻结以下真实历史场景，作为 A5 分类和阶段 C 检索 / 激活评估的候选输入。这里保存的是“必须重新研究的场景”，不提前把全部场景定性为激活失败；正式失效类型由 A5 依据当时已存在规则、实际上下文和修订内容重新判定。

### S-01 — 项目路线图 / 里程碑集成后状态闭环

证据锚点：PR #72；研究附录 §2。

已确认历史事实：

- `using-agentic-dev.md` 已经存在“项目路线图与集成状态”边界；
- 该边界此前没有可靠进入 `agentic-dev` 自身高影响 AI 复核路径；
- PR #70 合并后因此机械派生尾部状态 PR；
- PR #72 的修复重点是把既有边界接入项目级 AI 复核，而不是重新发明平行规则；
- PR #63 是“拟集成后的稳定状态”的正向参考。

该场景是当前仓库最直接的“已有长期规则与实际激活路径脱节”候选。

### S-02 — 规划候选被提前赋予执行单元语义

证据锚点：Issue #58 Finding 3；PR #60。

已确认历史事实：

- 使用方曾把尚未完成规格说明 / 必要技术规划 / 切分 / 就绪检查的未来工作预编号为后续 `EU-xx`；
- 新上下文容易把编号和 Roadmap 顺序误读成已经获得执行单元身份；
- 最终通用边界收敛为：规划 / 需求候选 → 候选执行单元（可有稳定标识）→ 就绪检查 → 已就绪执行单元；
- PR #60 最终全新运行时结果为 `5 / 5` 场景、`27 / 27` 断言通过。

A5 需要判断该历史摩擦中哪些规则当时已经存在、哪些属于使用层可发现性不足。

### S-03 — 就绪检查发现上游基础失效后的重新进入

证据锚点：Issue #58 Finding B；PR #61。

已确认历史事实：

- 使用方在就绪审计中发现当前实现与原规格说明 / 技术计划基础冲突；
- 正确路径是返回规格说明 / 技术规划，完成实质修订后重新 `slice-work → readiness-check`；
- 已有候选标识、工作产物或历史就绪结果不能跨语义修订继续授权执行；
- PR #61 最终新场景与直接回归合计 `6 / 6` 场景、`37 / 37` 断言通过。

### S-04 — 验证声明 / 风险与 GitHub Actions 实际触发拓扑错配

证据锚点：Issue #58 Finding A；PR #61。

已确认历史事实：

- 使用方的专项高成本工作流已经开始按真实责任路径收窄，但普通文档 / 权威 PR 仍机械触发完整 CI 与评审环境；
- 修订后要求显式对账 `Change / Authority Impact → Evidence Claim / Risk → Verification Layer → Actual Trigger / Gate → Current Evidence`；
- `paths`、label、`workflow_dispatch` 等只作为平台适配器，不能代替声明 / 风险语义。

该场景适合检验“只加载通用证据规则”与“按 GitHub Actions 风险激活平台专项规则”的差异。

### S-05 — 异步外部操作中的临时证据与单实例评审环境生命周期

证据锚点：Issue #58 Findings 1～2；PR #59。

已确认历史事实：

- 临时工作流产物被接受为长期输入时，需要显式晋升并保留来源关系，而不能继续把会过期的 Artifact 当作唯一长期输入；
- 单实例评审环境需要可观察所有者、租约取得 / 续期 / 到期 / 释放和过期运行判定；
- 自动验证与人工评审可以具有不同生命周期，不能机械 `latest-head-wins`；
- PR #59 定向维护最终为 `5 / 5` 场景、`34 / 34` 断言通过。

该场景同时覆盖 `external-operation-guidelines.md` 与 `github-actions-verification` 的职责交叉。

### S-06 — 既有使用方新上下文的本地权威发现与上游基线边界

证据锚点：Issue #33 Finding 1～2；Issue #52 F4 Existing Consumer Adoption。

已确认历史事实：

- Issue #33 的既有使用方实验目标就是证明已有项目可以从自身持久化仓库权威、项目路线图、本地开发规则、代码和当前证据恢复，而不依赖旧会话；
- 实验中出现过真实摩擦：使用方对精确 `agentic-dev` 基线的引用容易被后续 Agent 误解为普通开发仍需持续跨仓库读取上游；
- 使用方通过本地开发方法 / AGENTS / README / Roadmap 固化已采纳规则，并把普通开发恢复入口收回使用方仓库；
- Issue #52 的正式 F4 采用进一步记录了选择性固化工程纪律、技术画像、验证画像与使用方覆盖边界，同时明确没有复制 `agentic-dev` 项目路线图、Foundation 状态、PR / Issue / Experiment 项目事实。

该场景适合验证新的激活方式是否能让使用方只取得当前任务需要的 `agentic-dev` 可复用规则，同时保持使用方仓库权威优先。

## 5. 正向对照候选

后续评估不应只有失败样本。A1 同时登记以下正向对照：

- **PR #63**：项目状态在集成前已经表达拟集成后的稳定路线，可作为 S-01 的正向对照；
- **Issue #52 / Consumer PR #49**：既有使用方采用精确基线并选择性固化本地规则，可作为 S-06 的正向对照；
- **PR #59 / #60 / #61 的最终运行时结果**：可用于验证后续检索模型没有把已经收敛的行为重新退化。

正向对照只用于后续评估设计，不表示必须复制当时的文档结构或运行流程。

## 6. A1 结论与后续边界

A1 已取得以下可审查基线：

1. 当前 GitHub / 活动里程碑状态已经冻结；
2. 两份高影响指南的精确 blob 身份已经冻结；
3. 当前直接交叉的 AGENTS、README、Roadmap 与五个技能入口已经记录；
4. 13 个高影响交叉主题已经登记为后续审计对象；
5. 6 个真实历史失效场景候选和必要正向对照已经冻结。

A1 **没有**完成以下工作：

- 没有把 13 个交叉主题当成最终规则激活单元；
- 没有判断任何指南必须拆分；
- 没有删除、合并或新增长期规则；
- 没有建立规则索引、YAML、图数据库或 MCP；
- 没有修改技能、方法、工程纪律或技术画像；
- 没有完成 A5 的规则缺口 / 激活失败分类。

下一工作项仍按协调计划进入：

> **A2 — `using-agentic-dev.md` 激活映射**

A2 应从本基线重新按语义枚举 `using-agentic-dev.md` 的规则激活单元，并记录触发条件、消费者、强度、权威指针、上下文层级、重复 / 重叠 / 陈旧候选及相关历史证据；不得直接把本文件的 X-xx 编号当作最终映射结果。
