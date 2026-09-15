---
id: project:roadmap
type: project
status: active
---

# Project Roadmap

## Current Baseline

当前正式 capability baseline 为 **Requirement Baseline Establishment & Architecture Clarification Split v1**。

Integration provenance：Issue #138 / PR #139；精确 integration commit、merge 时间与 Actions 结果由 Git / GitHub 当前事实持有，不在 Roadmap 复制瞬时状态。

该 baseline 建立在 Software Project Clarification v1、V4 Rule Discovery、Capability Model v2、Project Knowledge Model、Rule granularity consolidation、Model Collaboration Capability & Adoption v1 与 Rule Discovery runtime activation hardening 之上，并完成以下收敛：

- 新增 reusable `method:requirement-baseline-establishment`，把新项目 / 基线重建从 Raw Project Inputs 收敛到 `Requirement Baseline Ready`；
- Requirement 主路径正式定义为 `Establish Sources & Authority → Extract Requirement Facts → Structure Requirement Authority → Resolve Requirement Unknowns → Review Requirement Baseline → Requirement Convergence`；
- 固化 `Derive → Default → Ask → Review`：能由 Authority / 已确认事实唯一推导的结论不重复提问，没有 Evidence 支持的额外业务机制默认不创建，只有真实 material blocking ambiguity / conflict 才升级 Human Authority；
- 新增 reusable `architecture:requirement-authority`，定义 Requirement semantic ownership、推荐 `docs/requirements` Human IA、README / index / fact owner 边界、Aspect admission、Fresh Context consumption 与 artifact lifecycle；
- 新增独立、条件性的 `method:architecture-clarification`，只处理多个 Feature 共同依赖、长期、高成本难逆并阻塞可靠 Specification / Planning 的 systemic architecture driver；
- 删除 `method:software-project-clarification` super-method，不保留 compatibility layer；Method 之间通过 Return Contract 与 Repository-local selector 组合，不再建立只负责串联其他 Method 的上层流程；
- `method:ai-development` 继续只负责具体 Feature / change；系统性 Requirement Baseline gap 与 systemic Architecture gap 分别返回各自长期 owner / Method；
- Human Guide 新增 `establishing-requirement-baseline.md`，说明 Delta Conversation、Question Gate、Project Requirement Default、Capability Review 与 Clarification Depth Stop；
- `jilinjobs` 继续只作为带失败历史的混合 Evidence：吸收 Authority-first、single semantic ownership、确定性推导、高价值问题、独立语义复核等机制，不机械传播其 L1/L2/L3 编号、项目特定目录、历史 Task 流程或已经退出的持久 Business Model 中间层；
- 当前仍没有因为新增 Method 而建立 `requirements-analysis`、`requirement-elicitation` 或 `architecture-framing` Skill；Skill admission 继续要求新的跨 Consumer 真实 Evidence。

更早里程碑与原因见 `docs/project/project-evolution.md`；具体 capability contract 见真实 Method / Architecture / Skill / Rule owner。

## Current Evolution

当前没有获得 Planning / Execute Authority 的正式演进单元。

Issue #138 — **Requirement Baseline Establishment：新项目需求基线与 Architecture Clarification 拆分** 已作为本 baseline 的设计与实施 provenance；稳定语义已经进入 Method / Architecture / Guide owner。本 Roadmap 不复制 Issue / PR 的完整分析、review 和 Actions Evidence。

如果需要恢复 Issue #138 的设计理由，应读取 Issue #138 / PR #139，而不是在 Roadmap 建立第二份设计历史。

## Current Gate

**NONE — 当前没有 active Planning / Execute Gate。**

当前 Repository 可以从已集成 baseline 恢复 ordinary project state；任何下一演进都必须由新的真实 Evidence、明确问题或 Human Authority 建立独立工作入口，不能因为下列候选存在而自动开始。

## Next Candidates

当前可见后续候选只在真实 Evidence 支持时推进：

- **Requirement Baseline Consumer validation**：在真实新项目 / 新的重大需求重建场景中观察 `Raw Inputs → docs/requirements → Requirement Baseline Ready → first Feature` 是否能够稳定工作，重点观察 Question Gate、Project Default、Capability Review、Fresh Context consumption 与 Requirement Authority Index；
- **Architecture Clarification evidence evolution**：当前 v1 仍只有 bounded、conditional、anti-BDUF 的较低成熟度 contract；后续从真实 Consumer 的正向、负向和 Evolutionary Architecture case 中校正进入条件与责任细节；
- **Requirement execution capability / Skill admission**：只有真实 Consumer 证明 requirement extraction、elicitation 或 baseline review procedure 稳定、重复、可独立调用并能显著减少错误时，才评估新 Skill；
- **Consumer feedback evolution**：继续从 Issue #58 等长期 Consumer Evidence 判断是否需要新增 / 调整 reusable capability；
- **Method selection scaling**：只有 Method 数量、work-kind 歧义或 selector 维护成本真实增长时，才评估 metadata discovery / selector tool。

这些候选不因出现在 Roadmap 中自动获得 Planning / Execute Authority。

## Known Observations

- Requirement Baseline Establishment v1 的核心 Requirement 方法责任有真实大型 Consumer 的正向与负向历史 Evidence 支撑，但新的 default IA 与 Conversation Protocol 仍需要下一轮真实 Consumer adoption / project establishment 验证；
- Architecture Clarification 的 Evidence maturity 低于 Requirement Baseline Establishment，当前只允许按最小条件 contract 使用并持续演进；
- `Requirement Baseline Ready` 不等于 Architecture complete、Specification created、Execution Unit created 或 Execute / Integrate authority granted；
- 推荐 `docs/requirements` 目录是 Human IA / default projection，不是硬编码 runtime schema；Consumer 可以调整物理路径，但不能破坏 semantic ownership；
- Requirement Human Navigation、Requirement Authority Index 与 Requirement Fact Authority 必须保持不同 owner，避免 README / index /正文三份 inventory 与事实重复维护；
- 问题数量不是 Requirement maturity 指标；连续没有真实 Blocking Ambiguity 时，应停止提问并完成当前 Capability / Review；
- reusable Method 存在于 `agentic-dev` corpus 不等于当前 Repository 已自行采用；local selector 仍只描述本 Repository 实际采用的 work kind；
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