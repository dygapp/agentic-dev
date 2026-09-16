---
id: project:roadmap
type: project
status: active
---

# Project Roadmap

## Current Baseline

当前正式 capability baseline 以 **Review Governance vNext — Authority-chain Semantic Review & Current-owner Lifecycle** 为治理基础，并进一步集成 **Human Review Capability v1** 与 **Project Terminology Governance**。

Integration provenance：Review Governance 来自 Issue #141 / PR #142；Human Review Capability v1 来自 Issue #144 / PR #145；Project Terminology Governance 来自 Issue #147 / PR #148。精确 integration commit、merge 时间与 Actions 结果由 Git / GitHub 当前事实持有，不在 Roadmap 复制瞬时状态。

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
- terminology owner 通过 Requirement Authority Index 或等价 locator 按需发现，ordinary Fresh Context 不预加载整份 glossary，也不固定 `terminology.md` 或历史 Consumer 路径。

稳定演进里程碑与原因见 `docs/project/project-evolution.md`。

## Current Evolution

Issue #143 Candidate A — **Human-facing Guides** 已完成 Human Review Guide 这一 bounded unit；其他 Specification / Architecture / Technical Planning / GitHub connector / GitHub Actions / Review Environment 等 Human View 继续保持 opportunity-driven，不因为主题列表存在而批量生成。

Issue #143 Candidate B — **`jilinjobs` historical experience mining** 当前保持 ACTIVE。历史 corpus 继续按 retained / project-specific / failed-or-retired / uncertain 分类，而不是把旧项目做法直接晋升为 current capability。首个高置信 promotion unit **Project Terminology Governance** 已通过独立 Issue #147 收敛并进入当前 Requirement Authority / Requirement Baseline / Human Guide baseline；它没有上游化 `jilinjobs` 具体术语、编号、固定路径或 Business Model 中间层。

Issue #71 的 Consumer model-routing / blind independent review Evidence 已由 Issue #129 的 Model Collaboration Capability & Adoption v1 正式消费并关闭；历史证据继续由 GitHub 保留，不再作为独立待执行候选。

## Current Gate

**ACTIVE — Issue #143 Candidate B Historical Experience Mining / Promotion Analysis。**

当前首个 promotion unit Project Terminology Governance 已完成 capability 集成；Candidate B 的剩余工作继续是系统扫描、分类、与 current capability baseline 对照，以及只对高置信真实缺口建立独立 promotion candidate。Candidate B 本身不授予 Consumer modification、Method modification 或批量 capability expansion authority。

## Next Candidates

当前可见后续候选只在真实 Evidence 支持时推进：

- **Candidate B remaining promotion analysis**：继续对 `jilinjobs` 历史经验做 retained / project-specific / failed-or-retired / uncertain 分类，并与 current `agentic-dev` baseline 去重；已经吸收的经验只作为 Evidence，只有职责稳定且存在真实 capability gap 的高置信项才建立独立 promotion candidate；
- **Review Governance cross-Consumer validation**：观察 Authority-chain semantic review 在其他 Consumer / technology / repository structure 中是否稳定减少 stale owner、orphan projection、replaceability seam 与 source-promotion defect，同时关注 false-positive 与普通 PR 过度触发；
- **Human Review further validation / Human View evolution**：继续观察真实 Consumer 中“durable semantic correction → true owner writeback → reread → regenerate”的正向分支、不同正式文档环境兼容性以及是否出现新的稳定 Human Guide 需求；不得因为 v1 已存在就自动增加格式 Skill、审批 Gate 或持久模型层；
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
- C6 当前保持 Held；未来不得因为其表述直觉上合理而绕过 cross-case Evidence；
- Requirement Baseline Establishment v1 的核心 Requirement 方法责任有真实大型 Consumer 的正向与负向 Evidence 支撑，但新的 default IA、Conversation Protocol 与 Project Terminology Governance 仍需要更多真实 Consumer adoption / project establishment 验证；
- Architecture Clarification 的 Evidence maturity 低于 Requirement Baseline Establishment，当前只允许按最小条件 contract 使用并持续演进；
- Human Review Capability v1 已通过 bounded independent semantic review 与真实 Consumer validation，但真实 Consumer 样本中的人工反馈为“无语义修改”，因此没有把未实际发生的正向 Authority writeback 分支夸大为已验证 runtime Evidence；
- Project Terminology Governance 的首轮 promotion Evidence 主要来自历史 Consumer corpus 与 current Requirement semantics 对照；当前只证明其职责边界足以进入 baseline，不证明所有 Consumer 都需要独立 terminology owner，也不证明 terminology Skill / Rule 已达到 admission；
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
- 稳定历史里程碑：`project-evolution.md`。

Roadmap 不保存完整 Architecture、实施日志、完整 Review 或 Closure Evidence；这些分别回到 capability owner 与 GitHub 历史。