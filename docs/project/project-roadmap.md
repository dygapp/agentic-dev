---
id: project:roadmap
type: project
status: active
---

# Project Roadmap

## Current Baseline

当前正式 capability baseline 以 **Review Governance vNext — Authority-chain Semantic Review & Current-owner Lifecycle** 为治理基础，并进一步集成 **Human Review Capability v1**、**Project Terminology Governance**、**Data Migration Governance**、**GitHub Agent Workflow Human View** 与外部操作 / 人工介入治理增强。

Integration provenance：Review Governance 来自 Issue #141 / PR #142；Human Review Capability v1 来自 Issue #144 / PR #145；Project Terminology Governance 来自 Issue #147 / PR #148；Data Migration Governance 来自 Issue #149 / PR #150；人工介入必要性治理来自 Issue #154 / PR #156；GitHub Agent Workflow Human Guide 与 external-write identity / idempotency 增强来自 Issue #157 / PR #158。精确 integration commit、merge 时间与 Actions 结果由 Git / GitHub 当前事实持有，不在 Roadmap 复制瞬时状态。

当前 baseline 建立在 Requirement Baseline Establishment & Architecture Clarification Split v1、V4 Rule Discovery、Capability Model v2、Project Knowledge Model、Rule granularity consolidation、Model Collaboration Capability & Adoption v1 与 Rule Discovery runtime activation hardening 之上，并完成以下收敛：

- `skill:review-change` 在原有 authority consistency、semantic regression、scope、evidence 与 artifact lifecycle 基础上增加有边界的 **Authority-chain semantic review**；
- 高影响 Authority restructuring 明确挑战 Current owner transition、single semantic ownership、Requirement / Domain → Observable Specification projection、declared replaceability seam、Authority / implementation / verification conflict classification 与 source role / evidence promotion boundary；
- bounded code-holdout / regenerability 只在 bulk Authority restructure、canonical owner migration、major Specification / Interface convergence、declared replaceability、heterogeneous reconstruction 或 high-impact semantic migration 等场景触发，不把普通 PR 自动升级为 full regenerability；
- `rule:authoritative-artifact-lifecycle-review` 扩展 Current-owner transition completeness：owner replace / retire / archive 或 lifecycle closure 后，Current locator、selector、verification consumer 与 durable current-state wording 必须同步迁移；
- Historical / archive / provenance 对 retired id/path 的明确非 Current 引用继续合法，旧字符串存在本身不是 stale dependency；deterministic targeted scan 只能辅助 semantic review，不建立中央 retired-owner catalog；
- C2 / C3 / C4 / C5 / C7 进入现有 Review procedure；C1 通过扩展既有 lifecycle Rule 而不是新增平行 Rule；C6 继续 HOLD，等待更多跨 Consumer / technology Evidence；
- 新增 `review-change` behavior eval 与 deterministic regression，用 Consumer failure-derived scenarios 锁定 currentness、conflict classification、replaceability seam 与 downstream projection semantics；
- `architecture:human-review` 与 `skill:human-review` 建立 Consumer 软件项目的人工评审能力：默认以结构化 Markdown Review Draft 作为非 Authority 的评审介质，按需生成临时视图，人工语义决定必须回写真正 owner；
- Human Review 按风险触发，不成为每个 Method stage 的固定审批；普通局部、低风险、可逆且 Authority 可唯一决定的工作不增加固定 Human Review 开销；
- HTML / DOCX 只在显式交付请求时作为可再生 projection 生成，不取得 Requirement / Specification / Architecture / Technical Authority；
- `human-review` 与 `review-change` 保持不同责任：前者帮助人理解和确认 Consumer 项目语义，后者独立复核 Repository change；任一 PASS 都不自动授予 merge / release / deploy 权限；
- Human Review v1 未新增 Human Review Method、持久 BPMN / Business Model 中间层、artifact-specific Review Skill 或中央 review catalog / owner registry，也没有把 Consumer-specific facts 上游化；
- `architecture:requirement-authority` 增加可选的 Project Terminology Authority：只有真实跨 Capability / Feature naming drift、alias mapping 或 shared business semantic root 需要时才建立，且继续保持 single semantic owner；
- `method:requirement-baseline-establishment` 在现有六阶段中完成 terminology detection、admission、classification、review 与 convergence，不新增 Method stage、mandatory glossary、central registry、Skill 或 Rule；
- terminology material ambiguity 继续服从既有 Human Blocking Question Gate；仅需 canonical naming coordination 的事项作为 non-blocking terminology decision 进入 Capability-level Review，不把命名统一扩大为产品 blocker；
- business terminology 只拥有 canonical business concept / semantic root 与必要 alias/source-role mapping，技术 identifier casing、package / filename style、DTO / Entity suffix 等仍属于 Technical / Code convention；
- terminology owner 通过 Requirement Authority Index 或等价 locator 按需发现，ordinary Fresh Context 不预加载整份 glossary，也不固定 `terminology.md` 或历史 Consumer 路径；
- `architecture:data-migration` 明确 durable migration invariant、Requirement / Specification / Technical ownership 与 canonical input / provenance 边界，同时保持 schema / initialization migration 的既有专项治理不被吞并；
- `rule:human-intervention-necessity` 要求在请求人工执行、提供输入、作出决定或充当系统中转前先验证其不可替代性，不能因为单一工具 surface 缺少接口就默认转给人工；
- `rule:safe-external-write` 在既有授权、最小变更与写后 reread 基础上增加有身份远程对象的 reuse / idempotency 防重责任，避免会话切换、重试或未知写入结果造成重复 Issue / PR 等对象。

稳定演进里程碑与原因见 `docs/project/project-evolution.md`。

## Current Evolution

Issue #143 — **Human-facing Guides 与 `jilinjobs` historical experience mining umbrella** 已完成主动 systematic mining：三轮历史扫描完成 retained / project-specific / failed-or-retired / uncertain 分类，高置信真实缺口中的 Project Terminology Governance 与 Data Migration Governance 已分别通过独立 bounded promotion lifecycle 集成。后续历史材料只按新的明确 Evidence 触发，不再把 Candidate B 维持为持续研究流。

Candidate A 已完成 Human Review Guide、Feature Development Guide 与 GitHub Agent Workflow Guide；Specification / Architecture / Technical Planning 等主题不机械拆成独立 Guide，其他 platform / operations Human View 继续按真实使用缺口逐个建立 bounded unit。

Issue #157 / PR #158 — **GitHub Agent Workflow** 已完成 semantic gap review、Human Guide、最小 runtime governance 增强、Independent Semantic Review 与真实 Consumer read-only applicability validation，并已集成到当前 baseline；不再作为 active bounded evolution。后续只按新的真实 platform / operations Evidence 继续演进，不从本次完成态自动启动新的 Method / Architecture / Skill / Consumer upgrade。

Issue #71 的 Consumer model-routing / blind independent review Evidence 已由 Issue #129 的 Model Collaboration Capability & Adoption v1 正式消费并关闭；历史证据继续由 GitHub 保留，不再作为独立待执行候选。

## Current Gate

**NONE — 当前没有 active bounded evolution / Gate。**

Roadmap 继续持有当前 evolution / Gate / next candidates 的稳定摘要；新的 bounded work 必须由新的明确 Evidence、Human Authority 或当前 Repository 事实重新激活，不能从已完成的 Issue #157 / PR #158 或下方候选列表自动继承 Execute / Integrate Authority。精确 PR、Review、Actions、commit 等 live state 继续以 GitHub current state 为准。

## Next Candidates

当前可见后续候选只在真实 Evidence 支持时推进：

- **Review Governance cross-Consumer validation**：观察 Authority-chain semantic review 在其他 Consumer / technology / repository structure 中是否稳定减少 stale owner、orphan projection、replaceability seam 与 source-promotion defect，同时关注 false-positive 与普通 PR 过度触发；
- **Human Review further validation / Human View evolution**：继续观察真实 Consumer 中“durable semantic correction → true owner writeback → reread → regenerate”的正向分支、不同正式文档环境兼容性以及是否出现新的稳定 Human Guide 需求；不得因为 v1 已存在就自动增加格式 Skill、审批 Gate 或持久模型层；
- **GitHub Agent Workflow / platform operations evidence evolution**：在真实 Consumer 与不同 execution topology 中继续观察 Local / Cloud runtime、GitHub-native API / Connector、Actions 与 Human escalation 的责任边界；不得把 GitHub-specific platform instance 晋升为 universal Git contract，也不得因为一个 surface 缺少能力就默认人工桥接；
- **C6 verification invariant / tooling evolution**：继续收集“verification 应验证 invariant 而不是 mutable implementation inventory”的跨案例 Evidence，再决定 Rule admission、tooling-only 或继续 Hold；不得只凭 `jilinjobs-cms` 单一主要样本晋升 universal Rule；
- **Current-owner deterministic tooling**：只有 targeted retired id/path、dead locator、selector/link integrity 检查在多个真实 migration 中证明价值且不需要中央同步 inventory 时，才评估正式 tooling；
- **Requirement Baseline Consumer validation**：继续在真实新项目 / 新的重大需求重建场景中观察 `Raw Inputs → docs/requirements → Requirement Baseline Ready → first Feature`，重点关注 Question Gate、Project Default、Capability Review、Fresh Context consumption、Requirement Authority Index 与按需 terminology ownership；
- **Architecture Clarification evidence evolution**：当前 v1 仍只有 bounded、conditional、anti-BDUF 的较低成熟度 contract；后续从真实 Consumer 的正向、负向和 Evolutionary Architecture case 中校正进入条件与责任细节；
- **Requirement execution capability / Skill admission**：只有真实 Consumer 证明 requirement extraction、elicitation、baseline review 或 terminology procedure 稳定、重复、可独立调用并能显著减少错误时，才评估新 Skill；
- **Consumer feedback evolution**：继续从 Issue #58 等长期 Consumer Evidence 判断是否需要新增 / 调整 reusable capability；
- **Method selection scaling**：只有 Method 数量、work-kind 歧义或 selector 维护成本真实增长时，才评估 metadata discovery / selector tool。

这些候选不因出现在 Roadmap 中自动获得 Planning / Execute Authority。

## Known Observations

- `jilinjobs-cms#155` 证明 Requirement Baseline / Documentation Authority 的 Authority-first、single semantic ownership 与 source-role separation 能支撑大型 Consumer 重建，但也证明局部文档自洽不足以替代跨层 projection、currentness、replaceability 与 regenerability challenge；
- G6 R4 / R5 只提供 replacement design / contract completeness dry-run Evidence，不证明 Node.js Backend 或 HTML-first Renderer 已经构建运行；该 Evidence 边界必须继续保持；
- Current-owner transition 同时包含 deterministic 与 semantic 两部分：dead locator / targeted retired reference 可自动化，Historical/provenance 引用角色与 Roadmap active-state wording仍需 semantic review；
- #143 systematic historical mining 已达到完成条件；后续不得为了寻找更多 candidate 无限扩大历史样本，新的 promotion 必须由新的明确 Evidence 与 current gap 重新触发；
- C6 当前保持 Held；未来不得因为其表述直觉上合理而绕过 cross-case Evidence；
- Requirement Baseline Establishment v1 的核心 Requirement 方法责任有真实大型 Consumer 的正向与负向 Evidence 支撑，但新的 default IA、Conversation Protocol 与 Project Terminology Governance 仍需要更多真实 Consumer adoption / project establishment 验证；
- Architecture Clarification 的 Evidence maturity 低于 Requirement Baseline Establishment，当前只允许按最小条件 contract 使用并持续演进；
- Human Review Capability v1 已通过 bounded independent semantic review 与真实 Consumer validation，但真实 Consumer 样本中的人工反馈为“无语义修改”，因此没有把未实际发生的正向 Authority writeback 分支夸大为已验证 runtime Evidence；
- Project Terminology Governance 的首轮 promotion Evidence 主要来自历史 Consumer corpus 与 current Requirement semantics 对照；当前只证明其职责边界足以进入 baseline，不证明所有 Consumer 都需要独立 terminology owner，也不证明 terminology Skill / Rule 已达到 admission；
- Data Migration Governance 的首轮 promotion Evidence 证明稳定 invariant 与 owner boundary 具有跨场景复用价值，但不意味着所有 migration 都需要 canonical dataset、独立 Method / Skill 或统一文件结构；
- GitHub Agent Workflow 的 A / B / C 只用于解释 execution topology / responsibility mode，不构成新的 Method lifecycle；具体平台能力、授权和 runtime availability 必须由当前环境重新验证；
- `Requirement Baseline Ready` 不等于 Architecture complete、Specification created、Execution Unit created 或 Execute / Integrate authority granted；
- 推荐 `docs/requirements` 目录是 Human IA / default projection，不是硬编码 runtime schema；Consumer 可以调整物理路径，但不能破坏 semantic ownership；
- Requirement Human Navigation、Requirement Authority Index、Requirement Fact Authority 与可选 Project Terminology Authority 必须保持清晰 ownership，避免 README / index / glossary / Capability 正文形成平行 Current truth；
- 问题数量不是 Requirement maturity 指标；连续没有真实 Blocking Ambiguity 时，应停止提问并完成当前 Capability / Review；canonical naming coordination 也不能为了“术语完整”被误升格为 Blocking Question；
- reusable Method / Skill 存在于 `agentic-dev` corpus 不等于当前 Repository 已自行采用；local selector / runtime instance 仍只描述本 Repository 实际采用的 work kind 与能力；
- Project Capability Profile 是 Repository-local instance owner，需要继续保持薄、稳定且不演变成 runtime catalog；
- V4 Rule / Skill Human inventory 继续由 deterministic tests 与真实 corpus 保持一致，不应迁入 Project Profile；
- Model Collaboration 的成本价值与具体平台支持度仍必须由 adoption / runtime Evidence 证明，不从 upstream self-integration 直接泛化。

## State Ownership

- 当前 Repository live state：GitHub branch / Issue / PR / Actions；
- 当前项目使命与核心要求：`project-charter.md`；
- 当前 capability instance：`project-capability-profile.md`；
- 当前 evolution / gate / next candidates：本 Roadmap；
- 当前 bounded unit 的 exact PR / Review / Actions / commit 等 live state：对应 GitHub current state；
- 稳定历史里程碑：`project-evolution.md`。

Roadmap 不保存完整 Architecture、实施日志、完整 Review 或 Closure Evidence；这些分别回到 capability owner 与 GitHub 历史。