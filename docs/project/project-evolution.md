---
id: project:evolution
type: project
status: active
distribution: source-only
---

# Project Evolution

## 1. 目的

本文件只保存对理解 `agentic-dev` 当前设计仍有长期价值的**稳定演进里程碑摘要**。

它不是实施日志，也不替代 Git / Issue / PR / Actions。每个阶段的完整实验、Gate、Review 和 commit 证据仍由 GitHub 历史保存。

## 2. 真实 Consumer 验证建立项目方向

早期 `agentic-dev` 通过真实 Consumer 验证，而不是只在方法仓库内部自洽：

- Issue #18：首个真实 Greenfield Consumer 实验，验证新的 Agent 能从 Consumer Repository Authority、需求、Method 与按需 Skill 启动真实项目；
- Issue #33：Existing Consumer 持续演进实验，验证已有项目能够从自身持久化 Authority 与 Roadmap 恢复，而不是重复 Greenfield bootstrap；
- 后续 Consumer Evidence 持续证明：Consumer 项目事实必须保留在 Consumer，自上游采用的能力必须本地固化，ordinary runtime 不能持续依赖 upstream。

这一阶段奠定了“reusable capability + Consumer-local Authority”的长期方向。

## 3. Engineering Capability Foundation

Consumer Evidence 逐步推动项目从“通用方法 + Skills”扩展为更明确的工程能力体系，重点验证了：

- implementation minimality；
- surgical diff scope；
- technology / verification profile；
- Consumer override / local Authority；
- exact-head Current Evidence。

Issue #52 等真实采用证据明确保留了一个重要边界：Consumer 选择性固化 reusable capability，但不复制 `agentic-dev` Project Roadmap、Foundation 状态、PR / Issue / Experiment 项目事实。

## 4. Rule Governance v2 — Consumer-local first

Issue #92 把规则治理的目标从“上游仓库内部如何更好发现规则”进一步收敛为：

> 规则治理、发现和激活必须能在真实 Consumer 中本地持续发挥作用，而不是形成 ordinary runtime 的上游依赖。

该阶段形成并验证了 Consumer-local-first 的设计方向、按职责加载、显式 baseline adoption / upgrade、local override 与 fail-closed 等关键思想。

## 5. V3 — 知识与能力所有权收敛

Issue #94 组织了 V3-01 ～ V3-08 的系统收敛：

- 知识与能力所有权模型；
- 当前仓库所有权审计；
- Consumer 初始化 / adoption / upgrade / ordinary runtime 生命周期；
- Skill 重分类与准入；
- 面向 Agent 的结构化资源模型；
- 资源发现架构；
- `agentic-dev` self-adoption；
- Consumer 验证与持续有效性。

随后 Issue #118 执行独立复核。V3 的价值在于明确了 semantic owner、Consumer-local lifecycle、发现失败关闭与 Evidence 泛化边界；它也暴露了 Reviewed Discovery Map / Catalog 等派生中心索引的同步和上下文成本。

V3 最终 Closure baseline 成为 V4 重构起点。

## 6. V4 — 分布式 Rule Discovery Foundation

Issue #122 启动减法优先的 Foundation Rebuild，主动放弃需要人工与规则正文同步的中央 Map / Manifest / Catalog。

V4 建立当前 Rule Discovery 基础：

```text
current task facts
→ bounded task signals
→ local deterministic Rule Discovery
→ small {id, path} candidates
→ read candidate bodies only
→ semantic applicability confirmation
```

核心结果包括：

- Rule metadata 与正文同文件；
- 全量 Rule metadata 不进入 ordinary LLM context；
- locator-only progressive disclosure；
- task signals 三态与 bounded token；
- deterministic / fail-closed discovery；
- Consumer ordinary runtime 使用 Consumer-local Rules / Discovery；
- 当前工作树删除被取代的 V1～V3 runtime 发现资产。

V4 closure baseline：`3098f17b5661fbd4edbbaf1080ed4b4f5759e0d8`。

## 7. Capability Model v2 — 能力类型与双视窗

V4 后的真实可用性复核发现：Rule Discovery 已稳定，但 Method / Skill / Rule / Guide 的长期边界、Agent process entry 与 Human View 仍不完整。

Issue #124 / PR #125 形成 Capability Model v2：

- `Single Semantic Ownership, Multiple Views`；
- Method 成为可扩展的一等复杂工作过程模型；
- Skill 成为责任明确后的有界执行能力；
- Rule 成为可独立于 Skill 存在的横切条件性 policy / constraint / invariant；
- Rule 明确支持 Consumer-local specialization；
- Consumer Adoption / Upgrade 提升为正式 Method；
- Guide / README 纯化为 Human View；
- Agent Bootstrap 建立 Method Selection、Skill discovery 与 Rule Discovery 的闭环。

PR #125 于 integration commit `e5488fd22a078ab59a427e36ef9a20af935fc63f` 合并，Issue #124 completed。

## 8. Project Knowledge Model — Project / Capability 分界

Capability Model v2 集成后继续复核发现：部分 Architecture 仍混入 `agentic-dev` 当前 Repository instance，例如 Method selector mapping、Skill inventory/count 与 AI Development-specific phase identity；同时 `docs/project/` 只剩 Roadmap，导致项目使命、当前 capability instance 和稳定演进历史缺乏明确长期 owner。

Issue #126 / PR #127 建立 Project Knowledge Model：

- `docs/project/**` 只拥有当前 Repository 自身的使命、核心项目需求、capability instance、Roadmap 与稳定演进摘要；
- `docs/architecture/**`、`docs/methods/**`、`skills/**`、`docs/rules/**` 与对应 tool contract 继续只拥有可复用 capability；
- 正式确立 **Project 不传播，Capability 传播**；
- Method selector instance 移入 Project Capability Profile；
- Skill inventory/count 退出 Skill Architecture；
- Method-specific phase identity 回归具体 Method；
- Rule Discovery exact runtime locator 只由 Project Capability Profile 持有；
- Consumer Adoption / Upgrade 明确不复制 upstream Project state，Consumer 必须建立自己的 local Project Knowledge / capability instance；
- deterministic contracts 防止实例信息重新漂回 Architecture / Bootstrap。

PR #127 以 exact candidate Head `5a2e59f5ae248fb2cf288c6521d8a9903ae8b68b` 通过 50 / 50 deterministic tests、Rule Discovery regression、高影响边界复核与 Convergence，并于 integration commit `10397cf00914fcfd6d71fd2ad6be6b89618dde8a` squash merge。

这一阶段没有改变 V4 Rule Discovery 核心运行语义，而是补齐 reusable capability 与 `agentic-dev` 自身 Project Knowledge 的长期 ownership 边界。

## 9. Model Collaboration Capability & Adoption v1

Issue #129 / PR #132 将历史 `experiment/codex-multi-model-collaboration`、Issue #71 Consumer model-routing Evidence，以及当前 Rule Discovery / Fresh Context / Project Capability Instance 架构重新收敛为正式、可选配的 Model Collaboration capability。

这一阶段形成的长期边界包括：

- `architecture:model-collaboration` 拥有 deterministic-first、能力层级、Primary responsibility、Authority-preserving handoff、single-writer、独立 review、Evidence-based escalation、requested-vs-observed runtime claim 与 single-agent fallback 等 reusable semantics；
- `method:model-collaboration-adoption` 只负责在 collaboration semantics 已经进入 Consumer-local Authority 后，探测 runtime、选择 strategy、投射 local config / policy、建立 instance、验证并启用或 fallback；
- `method:consumer-adoption` / `method:consumer-upgrade` 继续拥有 upstream reusable semantics 的首次接受与 baseline delta assessment，专用 collaboration Method 不得重新实现或绕过这一 Gate；
- `Project Capability Profile` 只记录 Repository-local selector / instance，不复制 reusable capability body；`agentic-dev` 自身当前 collaboration instance 仍为 `disabled`；
- Codex 配置与角色 profile 被保留为带核验日期的 Human Reference，不把平台专项 schema、模型名或 `.codex/` 物理结构提升为跨 Repository Authority；
- “协作链路可以安全启用”与“协作更省、更快或应成为默认策略”被拆成 functional enablement 与 efficiency / preferred-default 两类不同 claim；效率结论必须有可比单 Agent baseline 支撑；
- 旧实验中静态配置成功但 child collaboration smoke 失败的结果继续作为 Evidence，不能被改写为 runtime PASS；真实 child-thread、single-writer runtime behavior、observability 与 fallback 仍需每个 Consumer 在 adoption 时重新验证。

本轮还沉淀了一条通用 capability 分类经验：一个自然语言需求可能同时包含 reusable capability semantics、upstream semantic acceptance、local instance establishment、Consumer-local policy 与 Human View，不能先选文档类型再强行归类。新增 Method 通过 admission gate 后还需要做 **Method composition review**，检查它的前置条件、失败返回、完成结果以及是否侵占相邻 Method 已有 Gate。

PR #132 candidate exact Head `2d6b093696bbd97d5c43a265173afc9954a7008f` 通过 Rule Discovery Run #94 与独立复核（未解决 Blocking / Medium = 0 / 0），随后于 integration commit `385204c8605dd58584ec18456ab8a97d6282b515` squash merge；Post-Integration Rule Discovery Run #95 PASS，Issue #129 completed。

## 10. Software Project Clarification v1

Issue #133 / PR #134 补齐普通软件 Consumer 在多个 Feature 进入 Specification 之前，如何建立或重建长期 Requirement / Architecture Context 的项目级澄清能力。

这一阶段没有把 `jilinjobs` 历史流程当作成功模板，而是将其作为带失败历史的混合 Evidence，提炼可复用机制并显式保留失败教训。长期结果包括：

- 新增 `method:software-project-clarification`，生命周期为 `Establish Context → Requirement Clarification → Architecture Clarification? → Clarification Convergence`；
- Requirement Clarification 负责从原始、Legacy、冲突或碎片化输入中提取并确认长期 Product / Domain 事实，将确认结果提升并回写到真实 Requirement / Domain owner，而不是建立需要长期同步的派生中间层；
- 高风险 baseline 重建、批量语义变换与多 Authority 冲突合并在 Ready 声明前必须执行 independent semantic review，避免结构化迁移或实施者自证静默创造业务事实；
- Architecture Clarification 被限定为条件阶段：只有多个当前或预期 Feature 在可靠 Specification 前共同依赖尚未解决的长期 architecture driver 时进入；v1 只固化 bounded、conditional、anti-BDUF 的最小 contract；
- `method:ai-development` 明确保持 Feature / change 级职责；Feature-local ambiguity、Specification、Technical Planning 与项目级 Requirement / Architecture Clarification 通过真实长期 owner 组合，不形成平行 Authority；
- 新 Method 存在于 reusable Method corpus 不等于 `agentic-dev` 自身采用；`project-capability-profile.md` 未注册该 Method，Consumer 只有在显式 adoption / upgrade 后才建立 local selector mapping；
- 没有因为新增 Method 自动增加 Requirement / Architecture Skill、Clarification Rule、默认 Handoff Artifact 或固定 Consumer 文档 schema；
- `using-agentic-dev` Human Guide 同步解释两层 Clarification、适用边界、Consumer-local adoption 与当前 Architecture Clarification Evidence maturity，但不成为第二套规范 owner。

PR #134 在 Method Boundary Design、adversarial review、focused re-review、semantic consistency review、Human Guide alignment review 与语言规范检查后，于 integration commit `6fdcf628abfac3eb306fc9acfce303fd7aee245e` squash merge；Post-Integration Rule Discovery Run #106 PASS，Issue #133 completed。

这一阶段进一步确认了一条长期边界：**面向 Consumer 的 reusable Method 不应因为被 `agentic-dev` 定义，就自动反向成为 `agentic-dev` 自身 capability evolution 的默认流程。**

## 11. Requirement Baseline Establishment & Architecture Clarification Split v1

Issue #138 / PR #139 在 Software Project Clarification v1 的基础上识别出一个更具体的缺口：虽然 v1 已经拥有正确的 Authority-first 与 Clarification 原则，但仍没有完整回答一个新项目如何从 Raw Project Inputs 建立可持续使用的 `docs/requirements` Requirement Baseline。

这一阶段继续使用 `jilinjobs` 的多轮需求分析历史作为混合 Evidence，而不是成功模板，并把用户实际遇到的无限问答、确定性结果被重复确认、README / index 可能职责重叠等问题提升为可复用设计输入。

长期结果包括：

- 将 `method:software-project-clarification` 拆分为两个独立 work kind，并删除旧 super-method，不保留 compatibility layer；
- `method:requirement-baseline-establishment` 正式拥有 `Raw Project Inputs → Requirement Baseline Ready`，包括 source / Authority scope、Requirement fact extraction、Capability / ownership、Requirement Authority structure、Question Gate、Human Review 与 convergence；
- Requirement 会话采用 `Derive → Default → Ask → Review`：Authority 可回答或已确认事实可唯一推导时不问；缺少 Evidence 时不通过审核 / 通知 / 版本 / 归档 / 同步等否定式穷举让人工逐项证明不存在的功能；真正 material blocking ambiguity / conflict 才升级 Human Authority；
- Capability 完成后优先整体 Human Review，而不是把人工变成逐字段 Requirement Generator；Clarification Depth Stop 阻止 Requirement 问题下钻到字段、按钮、API、数据库、缓存、类 / package 等普通 Design 层；
- 新增 `architecture:requirement-authority`，把 Requirement Human Navigation、Requirement Authority Index 与 Requirement Fact Authority 明确拆开；推荐 `docs/requirements/{README,index,overview,business,aspects,non-functional,analysis}` 作为 Human IA，但不硬编码为跨 Consumer runtime schema；
- 横向 Aspect 只有在跨多个 Capability、具有独立业务 / Acceptance 意义且不能合理归属单一 owner 时才建立；`analysis/` 默认非 Authority，派生视图可再生时不形成第二套长期同步对象；
- `method:architecture-clarification` 成为独立、条件性 Method；简单项目或已有充分 Architecture Context 的项目可以在 `Requirement Baseline Ready` 后直接进入 `method:ai-development`；
- `method:ai-development` 分别把系统性 Requirement Baseline gap 与 systemic Architecture gap 返回各自长期 owner / Method，不再依赖模糊的“项目级澄清”责任；
- 当前没有因为新增 Method 自动创建 Requirement / Architecture Skill；是否 Skill 化继续等待真实 Consumer 中稳定、可独立调用、能显著减少重复错误的 procedure Evidence。

Issue #138 保存设计 Evidence 与边界决定，PR #139 是本次 capability 集成载体；精确 integration commit 与 Actions / Review Evidence 继续由 GitHub 历史保存，Project Evolution 不复制瞬时执行状态。

这一阶段进一步确认：**对于 AI 驱动的新软件项目，Requirement Baseline Establishment 是 Feature Development 的上游 Project Establishment work kind；Architecture Clarification 是条件性的独立 work kind，而不是新项目必须机械执行的固定阶段。**

## 12. Review Governance vNext — Failure-driven Authority-chain Review

Issue #140 的 Consumer Validation 与 `dygapp/jilinjobs-cms#155` G1～G7 提供了新的跨层 Review Evidence：Requirement / Documentation Authority 的 Authority-first、single semantic ownership 与 source-role separation 能支持大型 Consumer 的文档重建，但各层分别自洽并不能保证整条 Authority chain 已经可再生、可替换或保持 Current。

Consumer G1～G6 记录 25 个 primary Failure Evidence，G0 记录 7 个 supplemental governance / adoption Evidence。G5 在此前多个 Gate 已分别通过后仍发现 Requirement / Domain → Specification observable projection、Interface semantics、Historical Migration Specification orphan 与 responsibility split 等跨层缺口；G6 又发现 canonical migration workspace 把 mutable implementation inventory 混入 Current recovery surface。修复后，独立 Fresh Context 的 R1～R6 达到 PASS；其中 Backend / Public Renderer substitution 只属于 design / contract completeness dry-run，不是替代实现已经构建运行的证据。

Issue #141 / PR #142 将这些 Failure Evidence 转化为最小 upstream capability evolution：

- 不新增新的 Review Method 或 artifact-specific Review Skill，而是在现有 `skill:review-change` 内增加有边界的 Authority-chain semantic review；
- 高影响 Authority work 显式挑战 Current owner transition、single semantic ownership、downstream observable projection、declared replaceability seam、Authority / implementation / verification conflict classification 与 source role / evidence promotion boundary；
- 对 bulk Authority restructure、replaceability、major Specification / Interface convergence、heterogeneous reconstruction 与 high-impact semantic migration 增加 bounded code-holdout / regenerability challenge，普通 PR 不自动执行 full regenerability；
- C1 不建立平行 micro-rule，而是扩展既有 `rule:authoritative-artifact-lifecycle-review`，把 owner replace / retire / archive 或 lifecycle closure 后的 locator、selector、verification consumer 与 durable current-state wording 纳入 transition completeness；
- Historical / archive / provenance 中明确的非 Current retired reference 被保留为合法 Evidence，避免把全仓旧字符串扫描错误包装成 hard invariant；
- C2 / C3 / C4 / C5 / C7 首先进入 Review procedure；C6 “verification should validate invariants, not mutable inventories” 保持 Held，等待更多跨 Consumer / technology Evidence；
- deterministic tooling 只保留 targeted retired reference、dead locator、selector / link integrity 等候选方向，不恢复中央 owner registry、retired-owner catalog 或其他需要与 Authority corpus 同步的 runtime index。

这一阶段进一步确认：**Review Governance 的成熟方向不是不断增加细碎 Rules，而是用少量强 invariant、结构化 semantic review procedure 与 Evidence-supported deterministic checks组合；真实 Consumer failure 决定 Promotion / Hold / Reject，而不是从理论完整性反推 capability。**

## 13. Human Review Capability v1 — Authority-preserving Human Confirmation

Issue #144 / PR #145 在 Requirement Baseline、Feature Specification、Architecture Clarification 与 Technical Planning 之间补齐一个横向 Human Review capability，而没有新增强制 Human Review Method 或持久业务建模层。

这一阶段形成的长期边界包括：

- `architecture:human-review` 拥有 Review Draft、临时派生视图、反馈分类、Authority 回写、完成条件与显式交付投影的长期契约；
- `skill:human-review` 只负责执行该契约，不取得 Product / Requirement / Specification / Architecture / Technical 事实所有权；
- 默认评审介质是结构化 Markdown Review Draft；流程图、泳道图、状态图、关系图、矩阵、架构图等只在明显提升人工理解时按需生成，并保持可删除、可再生、非 Authority；
- Human feedback 区分展示反馈、语义修正、新增长期决定与未决问题；durable semantic change 必须进入真正 owner，完成真实写入、重新读取和 Review Draft 再生成后才能声明评审完成；
- 缺少写权限时允许返回待回写动作，但状态必须保持“待权威回写 / 评审未完成”，不能把“人工已经决定”误写成“Current Authority 已更新”；
- `delivery_target = none` 是默认；HTML / DOCX 只有显式请求时生成，交付投影不得反向拥有或修改业务语义；
- Human Review 按风险触发，普通局部、可逆、低风险工作不增加固定人工审批；
- `human-review` 与 `review-change` 明确分离：前者帮助人理解和确认 Consumer 项目语义，后者独立检查 Repository change；二者均不自动授予 merge / release / deploy。

Gate E 在真实 `jilinjobs-cms` Authority 上验证了 Requirement / Specification / Architecture review、跨模块生命周期视图、HTML / DOCX 显式投影和真实 Human confirmation；本次真实反馈为“确认，无语义修改”，因此没有把未实际发生的 durable semantic correction → true-owner writeback 正向分支夸大为已验证 runtime Evidence。

Issue #143 Candidate A 随后补齐 `docs/guides/human-review.md` Human View，使人类可以理解和使用该 capability，同时继续保持 Guide 不参与 ordinary Agent runtime、不复制 Architecture / Skill / Method 规范语义。

这一阶段进一步确认：**人工评审的价值来自让人能够理解、纠偏并把长期决定返回唯一 Authority，而不是增加一份需要长期同步的评审文档或把每个阶段变成人工审批。**

## 14. 当前演进原则

从当前阶段开始，项目演进遵守：

- 当前工作树表达当前有效 owner，不保留历史兼容层；
- Project Knowledge 保存稳定项目定义 / 实例 / Roadmap / 里程碑，不恢复阶段文档膨胀；
- reusable capability 继续以真实 Consumer Evidence 驱动，而不是理论扩张；
- 历史细节需要时从 GitHub Issue / PR / Git 恢复，不复制到 ordinary Fresh Context；
- Project Capability Profile 必须持续保持为薄的 Repository-local instance owner，不演变成新的 Runtime Catalog / Rule Index；
- 新 capability 的 semantic owner 分类应先区分 reusable semantics、semantic acceptance、local instance activation 与 ordinary use，再决定是否需要 Architecture / Method / Skill / Rule / Project / Guide；
- 新增 specialized Method 除了通过自身 admission gate，还必须复核与相邻 Method 的 Gate ownership 和组合关系；
- 多个 Method 可以通过 Return Contract 与 Repository-local selector 形成上下游关系，但不为串联过程额外建立 super-method；
- Consumer-oriented Method 是否适用于 `agentic-dev` 自身演进，必须由本 Repository 的真实 work kind 与 local selector 独立决定，不能从 reusable capability 的存在反推 self-adoption；
- 对新项目需求建立，问题数量不是成熟度指标；AI 应优先提取、推导、应用已确认默认并形成可 Review 的 Requirement Capability，只把真实需要 Authority 的决定升级给人；
- 面向人的 Guide 可以完整解释 current capability，但必须始终保持为 Human View，不成为 Agent runtime selector、第二套 Gate 或规范正文 owner。

## 15. Runtime closure、核心边界与验证可信度收敛

2026 年 9 月的连续演进进一步把 current runtime 与项目边界从历史探索状态收敛为可恢复、可验证的正式能力：

- Issue #143 的 systematic historical mining 完成后，Project Terminology Governance 与 Data Migration Governance 进入正确 canonical owners；历史材料退出持续主动扫描，不再作为普通 runtime 输入；
- Issue #157 / PR #158 建立 GitHub Agent Workflow Human View，并增强 external-write identity / idempotency 与人工介入必要性治理；
- Issue #162 / PR #163 建立 Chat Repository Bootstrap / execution transport closure，把旧 A / B / C execution-topology 假设替换为 Repository Authority / Rule Discovery、execution transport、verification 三层分离；
- Issue #164 R1 / PR #165 将 AI Development 核心边界明确收敛到 `Ready to Integrate`，退出 upstream Vue / TypeScript technology Rule family，同时保留 Consumer-local technology specialization；
- Issue #164 R2A / PR #166 修复 eval runner entry、behavior corpus registration、mode / scenario zero-execution success 与 Roadmap current-state drift；
- Issue #164 R2B / PR #167 修复 isolated discovery Bootstrap dependency closure、cross-Method completion-evidence applicability、Rule-root symlink incomplete scan，并把 PR / push deterministic verification 改为 exact-subject identity verification；
- Issue #164 R3 将 ordinary Agent 固定 Bootstrap 从 5 个固定文件收敛为 3 个：`AGENTS.md`、Project Roadmap、Project Capability Profile；Human README 与 Method Architecture 退出固定预读，按当前责任加载。Roadmap 同时退出已完成能力的长篇历史复述，把稳定演进说明归还本文件；
- Issue #164 R4 对 R1～R3 integrated baseline 执行独立最终语义复核，并从真实 Consumer `dygapp/jilinjobs-cms` 自身 Repository Authority 做 read-only applicability / upgrade-impact validation；最终 Blocking / Medium / Low = 0 / 0 / 0，Consumer compatibility PASS，当前 upstream upgrade 归类为 optional，本轮没有执行 Consumer mutation。

Issue #164 因此完成最终闭环。该轮继续遵守“减法优先”：没有新增 Method、Skill、technology Rule family、central registry 或 release / deploy / production-operations lifecycle。

