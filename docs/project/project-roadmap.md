# 项目演进路线与当前状态

本文是 `agentic-dev` 仓库自身的 Project Roadmap，只维护**当前有效路线、活动状态、候选库、下一 Gate 与 Fresh Context 恢复入口**。

本文属于 `docs/project/*` 项目级 Authority，不覆盖更高优先级的方法、架构、契约、工程纪律或技术画像，也不得被 Consumer 自动继承。历史实施流水、精确 PR / Run / Review 证据由对应项目记录、Git、PR、Issue、Actions 与 `evals/` 保存；本文不重复维护完整历史证据。

## 1. 当前状态

长期阶段：

> **工程能力扩展与方法演进**

最近完成并已集成的有限里程碑：

> **规则治理与知识激活 v2 — Consumer-local 规则发现与激活**

当前活动有限规划里程碑：

> **规则治理与知识激活 v3 — 知识与能力所有权收敛**

v3 跟踪入口：Issue #94。  
V3-01 — 知识与能力所有权模型已完成并集成。  
V3-02 — 当前仓库所有权审计已完成并集成。  
当前活动 v3 子任务：**Issue #104 — V3-03 Consumer 初始化、采用、升级与普通运行生命周期**。  
当前候选：**PR #106（Draft）**。  
V3-03 启动基线：`master@ce7ab292f8ddf8b8512d406061a31a7db8ad9409`。

V3-03 直接消费 V3-02 已确认的 lifecycle rule families，不重复 Repository inventory。当前目标是建立单一 Consumer lifecycle owner，明确新 Consumer 首次采用、Existing Consumer baseline upgrade、逐项 adoption decision、adoption verification / baseline advance、ordinary-runtime local-only 与显式 upstream re-entry。

当前下一 Gate：

> **完成 V3-03 Consumer lifecycle 候选及其跨 owner 一致性复核；高影响 lifecycle ambiguity 的 Blocking / Medium 为 0 后，才进入人工集成决策，并在实际集成后判断是否启动 V3-04。**

V3-03 当前不执行 V3-02 的物理 disposition，也不修改 Consumer Repository、`SKILL.md`、metadata / Front Matter schema 或 discovery implementation。

详细当前规划 / 审计 / lifecycle：

- `docs/project/rule-governance-knowledge-activation-v3.md`
- `docs/project/knowledge-capability-ownership-model-v3.md`
- `docs/project/current-repository-ownership-audit-v3.md`
- `docs/architecture/consumer-lifecycle.md`
- `tasks/plans/20260911/01-rule-governance-v3-v3-03-consumer-lifecycle.md`

## 2. v3 当前路线

v3 严格按以下顺序推进：

1. V3-01 — 知识与能力所有权模型 — **已完成并集成**；
2. V3-02 — 当前仓库所有权审计 — **已完成并集成**；
3. V3-03 — Consumer 初始化、采用、升级与普通运行生命周期 — **当前**；
4. V3-04 — 技能重分类与准入；
5. V3-05 — 面向 Agent 的结构化资源模型；
6. V3-06 — 资源发现架构；
7. V3-07 — `agentic-dev` 自采用；
8. V3-08 — Consumer 验证；
9. 独立复核；
10. 必要 ADR、正式 v3 设计与实现规划。

顺序只定义规划依赖，不自动授予后序任务权限。

V3-01 已建立以下四维所有权判断：

```text
语义所有者
+ 适用范围 / 来源状态
+ 运行 / 生命周期角色
+ 载体 / 权威形式
```

至少区分：核心方法 / 原则、技能 / 过程型能力、可复用工程能力 / 工程纪律 / 画像、仓库本地政策 / 规范 / 规则、项目 / 产品权威资源、Guide、研究 / 输入 / 证据。

V3-02 已以规范正文 / 规则族为主要审计单位完成当前仓库审计，而不是按现有目录机械分类。其结果特别识别了 Guide catch-all、已完成项目记录中仍承担现行可复用语义的过渡契约、派生路由器与真实 semantic owner 的重叠，以及 Skill 与工程纪律 / 验证规则之间的正文复制风险。

V3-03 将 Consumer lifecycle 明确为可复用工程能力，而不是新的 Product Development Method Stage 或自动 Skill 候选。候选长期 owner 为 `docs/architecture/consumer-lifecycle.md`；`docs/architecture/engineering-capability-architecture.md` 负责其上层能力分类。

## 3. v2 已集成基线

规则治理与知识激活 v2 已通过 PR #93 集成。其 Phase A～G 已完成：

- Consumer-local 运行目标与验收；
- 规则所有权与 Guide 分解；
- 最小 metadata / Catalog 契约；
- 发现、路由与技能接口；
- 基线采用与 Consumer-local 投影；
- 真实 Consumer Phase F R1～R5；
- Phase G 候选漂移定向重验与最终 AI 复核；
- 根启动入口与 `AGENTS.md` 职责瘦身。

v2 已验证并继续受 v3 保护的行为至少包括：薄启动入口、仓库 / Consumer 权威优先、渐进式披露、证据先于结论、规范正文单点所有权、派生发现机制不拥有规范正文、陈旧 / 缺失 / 歧义时失败关闭、主职责与最小辅助上下文分离、只做路由判断时不机械加载完整技能、真正进入职责时按需加载技能、阶段返回后重新判断、Consumer 普通运行只依赖 Consumer-local 现行资源、逐项基线采用，以及同一运行范围 / 发现职责不并行维护多个现行派生机制。

V3-02 审计已明确：部分 v2 `docs/project/*` 虽属于已完成里程碑记录，仍承载当前 discovery / adoption / runtime 的过渡性可复用契约；在 V3-03～V3-06 建立并验证替代 owner 前不得提前归档、删除或失效。

V3-03 当前提炼其中的 durable Consumer lifecycle 语义；在 PR #106 实际集成并完成相应 replacement closure 前，v2 当前运行发现 / 激活机制和 transitional-current lifecycle 入口继续有效。

## 4. 当前范围边界

V3-03 当前只授权：

- 从 V3-02 审计矩阵消费 lifecycle rule families；
- 建立 Consumer lifecycle 长期 owner 候选；
- 明确 initialization / first adoption / baseline upgrade / local projection / adoption verification / baseline advance / ordinary runtime / upstream re-entry；
- 明确 evaluated baseline、active asset provenance 与 upgrade-only decision history 的职责分离；
- 明确 partial / failed upgrade 的 completion claim 与 current-state 边界；
- 明确与 Method、Guide、Skill、V3-05、V3-06、V3-08 的 owner 边界；
- 更新本阶段恢复入口并执行必要 AI 复核。

V3-03 当前不：

- 物理拆分、移动、重命名或删除 `docs/guides/*` 或其他现行 Authority；
- 修改当前 `SKILL.md` 或启动 V3-04；
- 新增或实现 Rule Index / Manifest / Catalog；
- 冻结全仓 Front Matter / metadata schema；
- 实现 Front Matter generator；
- 创建 Rule Super Skill / Stage Router Skill；
- 实现完整 discovery / routing architecture；
- 修改 Consumer Repository；
- 启动 WI-06、WI-07、WI-09、第四工程纪律或 Issue #71 候选实施。

临时 GPT-6 / 其他 AI 评估只作为挑战和复核证据，不自动提升为长期架构，也不授予后序执行权限。

## 5. 候选库

### WI-07 — 代码复核能力 v1

仍是独立候选，当前不启动。v3 活动规划不等于取消该候选，但在当前有限里程碑收口或人工重新排序前不并行进入实施。

### WI-06 — 第二及后续技术画像

未启动。Spring / Spring Boot / Gradle / Element Plus 等继续作为候选；是否进入下一有限里程碑仍需当前证据和人工路线决策。

### WI-09 — 运行时适配与分发

未启动。Marketplace、Plugin Bundle、Controller、统一安装 / 分发和 Codex 多模型协同采用适配继续作为候选。

### Issue #71 — 模型路由与盲测对照证据

继续作为独立规划 / 研究输入，不构成常规 Method Gate、新技能或默认模型策略。

Issue #58 继续承担长期 Consumer feedback 入口；其中新证据只有经过 `agentic-dev` 自身分类与准入后才能改变长期权威。

## 6. 已完成里程碑 / 子阶段索引

普通 Fresh Context 不默认读取以下已完成工作的完整过程记录：

1. 工程能力基础 v1 — `docs/project/engineering-capability-foundation-v1-closure.md`
2. 工程纪律扩展 v1 — `docs/project/engineering-discipline-expansion-v1*.md`
3. 中文交互与上下文清理 v1 — `docs/project/chinese-interaction-context-cleanup-v1.md`
4. 工程术语语义安全与现行文档收敛 v1 — `docs/project/terminology-semantic-safety-v1.md`
5. Squash Merge 下 Stacked PR 集成拓扑安全 v1 — `docs/project/stacked-pr-squash-topology-v1.md`
6. 规则治理与知识激活 v1 — `docs/project/rule-governance-knowledge-activation-v1.md`
7. 规则治理与知识激活 v2 — `docs/project/rule-governance-knowledge-activation-v2.md`
8. 规则治理与知识激活 v3 / V3-01 — `docs/project/knowledge-capability-ownership-model-v3.md`（其结果仍是当前后续阶段分类权威，不加载历史评估过程）
9. 规则治理与知识激活 v3 / V3-02 — `docs/project/current-repository-ownership-audit-v3.md`（其审计矩阵仍是 V3-03～V3-06 的直接分析输入，不加载历史评估过程）

## 7. Root Bootstrap 职责

为控制 Fresh Context 成本：

- `AGENTS.md`：稳定 Repository Governance、Authority Boundary 与 Agent 工作约束；**不维护当前项目状态**；
- `README.md`：简短当前状态与稳定导航；
- 本 Roadmap：详细项目路线、活动状态、候选与下一 Gate；
- `docs/project/*`：具体里程碑、项目治理、设计和验证记录；
- Git / PR / Issue / Actions：精确外部状态与执行证据。

当前阶段、里程碑进展、候选、Issue / PR / Run、基线历史与重复方法正文不得重新堆入 `AGENTS.md`。

## 8. Fresh Context 恢复顺序

新的 `agentic-dev` 上下文应：

1. 读取根 `AGENTS.md`，恢复稳定 Repository Governance 与 Authority Boundary；
2. 读取根 `README.md`，取得简短当前状态；
3. 读取本文，确认当前路线、Gate 和候选边界；
4. 重新读取当前 GitHub `master`、Open PR / Issue 和必要 Actions；
5. 当前 v3 规划期间读取 `docs/project/rule-governance-knowledge-activation-v3.md` 与 Issue #94；
6. 当前 V3-03 读取 Issue #104、`docs/architecture/consumer-lifecycle.md` 与 `tasks/plans/20260911/01-rule-governance-v3-v3-03-consumer-lifecycle.md`；
7. 只在 lifecycle 结论需要证据时按需读取 V3-02 审计矩阵、`using-agentic-dev.md`、`consumer-local-rule-activation.md` 和 v2 transitional-current lifecycle 文档；不重新做 Repository inventory；
8. 不依赖其他聊天、历史会话或个人记忆补充未固化项目事实。

## 9. 更新触发

出现以下情况时更新本文：

- 当前有限里程碑或子任务 Gate 实质变化；
- 人工选择新的活动里程碑；
- 长期路线、候选优先级或完成定义改变；
- 新能力正式集成并改变 Fresh Context 恢复路径。

单次 Run ID、临时分支删除、PR 从 Draft 变为 Ready、PR 合并提交等纯 GitHub 原生状态不为了记录而机械写入 Roadmap；需要时直接从 Git / PR / Issue 恢复。