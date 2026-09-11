# 项目演进路线与当前状态

本文是 `agentic-dev` 仓库自身的 Project Roadmap，只维护**当前有效路线、活动状态、候选库、下一门禁与 Fresh Context 恢复入口**。

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
V3-03 — 使用方初始化、采用、升级与普通运行生命周期已完成并集成。  
V3-04 — 技能重分类与准入已完成并集成。  
V3-05 — 面向 Agent 的结构化资源模型，跟踪入口为 Issue #109。  
V3-05 工作产物：`docs/architecture/agent-resource-model.md`。  
V3-05 启动基线：`master@cd61ab06c0194cc1cf0703aabc8aff5261529950`。

V3-05 直接消费 V3-01 四维所有权模型、V3-02 资源审计、V3-03 使用方生命周期和 V3-04 Skill / 支持资源边界。目标不是立即实现新的 Manifest / Catalog，而是先固定真实长期资源、资源固有结构与派生发现投影的边界，并逐项裁决 v2 metadata 契约。

V3-05 的精确审查、集成与完成状态由 Issue #109 和 GitHub 当前状态记录，不在 Roadmap 复制瞬时 PR 状态。Fresh Context 恢复时：

- 如果 Issue #109 仍开放，继续 V3-05 当前未完成门禁；
- 如果 Issue #109 已以完成原因关闭，V3-05 视为已收口，**V3-06 只成为下一规划候选**，仍需新的规划权威才能启动。

当前门禁：

> **V3-05 未完成时，先完成资源身份、结构化范围、固有 / 派生边界、物理表示兼容、当前有效性与 v2 metadata disposition 的收敛及 AI 复核；V3-05 完成后，只判断是否正式启动 V3-06，不继承 V3-05 权限。**

V3-05 不实现完整资源发现 / 路由，不冻结 Runtime Catalog / Activation Manifest，不全仓增加 Front Matter，不物理迁移全部 Guide / Policy / Project / Research-Eval 资源，也不修改使用方仓库。

详细当前规划 / 审计 / 架构：

- `docs/project/rule-governance-knowledge-activation-v3.md`
- `docs/project/knowledge-capability-ownership-model-v3.md`
- `docs/project/current-repository-ownership-audit-v3.md`
- `docs/architecture/consumer-lifecycle.md`
- `docs/project/skill-reclassification-admission-v3.md`
- `docs/architecture/agent-resource-model.md`
- `tasks/plans/20260911/03-rule-governance-v3-v3-05-structured-resource-model.md`

## 2. v3 当前路线

v3 严格按以下顺序推进：

1. V3-01 — 知识与能力所有权模型 — **已完成并集成**；
2. V3-02 — 当前仓库所有权审计 — **已完成并集成**；
3. V3-03 — 使用方初始化、采用、升级与普通运行生命周期 — **已完成并集成**；
4. V3-04 — 技能重分类与准入 — **已完成并集成**；
5. V3-05 — 面向 Agent 的结构化资源模型 — **状态见 Issue #109**；
6. V3-06 — 资源发现架构；
7. V3-07 — `agentic-dev` 自采用；
8. V3-08 — Consumer 验证；
9. 独立复核；
10. 必要 ADR、正式 v3 设计与实现规划。

顺序只定义规划依赖，不自动授予后序任务权限。

V3-01 已建立四维所有权判断：

```text
语义所有者
+ 适用范围 / 来源状态
+ 运行 / 生命周期角色
+ 载体 / 权威形式
```

目录、文件名、Front Matter、Markdown 形式或单一 `type` 都不能替代这些判断。

V3-02 已按规范正文 / 规则族完成当前仓库审计，识别 Guide catch-all、已完成项目记录中的现行过渡契约、派生路由与真实语义所有者重叠，以及 Skill / 工程能力复制风险。

V3-03 已把使用方生命周期收敛为单一可复用工程能力 owner：采用 / 升级与普通运行分离，普通运行默认只依赖使用方本地当前状态。

V3-04 已确认当前 9 个 Skill 身份继续成立，并把新增 Skill 准入与支持资源边界提升到 `docs/architecture/skill-architecture.md`；工程纪律 / Skill Contract / `execute-unit` 已收敛为单点正文 + 薄消费。

V3-05 当前建立三层资源模型：

```text
规范 / 事实正文
→ 资源固有结构
→ 派生发现投影
```

资源固有结构只表达真实长期身份 / 生命周期事实，派生发现投影服务 V3-06 的跨资源发现并可以删除 / 重建。V3-05 不把 Manifest record 等同于真实长期资源，也不新增独立于真实 owner 的统一 current-state 真值。

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

V3-02 已明确部分 v2 `docs/project/*` 仍承载现行过渡契约；在真实替代 owner / mechanism 集成前不得提前归档或删除。

V3-03 已提炼长期使用方生命周期；V3-04 已提炼 Skill / 工程能力边界；V3-05 正在重新裁决 v2 metadata / Manifest / Catalog。具体发现、查询、路由与对 `rule-activation-guide.md` 的显式取代仍等待 V3-06，因此当前 v2 discovery / activation 兼容入口继续有效。

## 4. 当前范围边界

V3-05 只授权：

- 定义哪些资源需要结构化及其最小长期资源身份；
- 让资源模型保持 V3-01 语义所有者、适用范围 / 来源状态、生命周期角色、载体形式正交；
- 明确资源原生结构、规范正文与派生发现提示的所有权关系；
- 明确普通 Markdown、`SKILL.md`、工程纪律、技术 / 验证画像、仓库本地规则、项目权威与 Skill supporting resource 的兼容方式；
- 固定当前有效性、来源、取代、派生关系的最小语义，但不建立第二 current-state truth；
- 逐项裁决 v2 `id / kind / source / activation_role / scope / responsibility / conditions / risks / origin / state / relations` 以及 `semantic-reviewed / current-locator`；
- 裁决 Activation Manifest / Runtime Catalog 属于资源固有模型还是 V3-06 派生层；
- 更新本阶段稳定恢复入口并执行必要 AI 复核。

V3-05 不：

- 实现或冻结 Runtime Catalog / Activation Manifest / Rule Index / generator；
- 设计完整资源发现、查询、排序、路由或 Stage Return 算法；
- 全仓批量增加 Front Matter 或统一 YAML / JSON schema；
- 建立数据库、向量库、图数据库、MCP 服务或后台 daemon；
- 物理迁移全部 Guide / Policy / Project / Research-Eval 文件；
- 修改任何使用方仓库；
- 重新设计 V3-03 生命周期或 V3-04 Skill 身份；
- 启动 V3-06～V3-08；
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
8. 规则治理与知识激活 v3 / V3-01 — `docs/project/knowledge-capability-ownership-model-v3.md`（其结果仍是当前后续阶段分类权威）
9. 规则治理与知识激活 v3 / V3-02 — `docs/project/current-repository-ownership-audit-v3.md`（其审计矩阵仍是 V3-05 / V3-06 直接分析输入）
10. 规则治理与知识激活 v3 / V3-03 — `docs/architecture/consumer-lifecycle.md`（当前长期使用方生命周期权威）
11. 规则治理与知识激活 v3 / V3-04 — `docs/project/skill-reclassification-admission-v3.md`（Skill 身份 / 重叠裁决记录；稳定准入规则已进入 Skill Architecture）

## 7. Root Bootstrap 职责

为控制 Fresh Context 成本：

- `AGENTS.md`：稳定 Repository Governance、Authority Boundary 与 Agent 工作约束；**不维护当前项目状态**；
- `README.md`：简短当前状态与稳定导航；
- 本 Roadmap：详细项目路线、活动状态、候选与下一门禁；
- `docs/project/*`：具体里程碑、项目治理、设计和验证记录；
- Git / PR / Issue / Actions：精确外部状态与执行证据。

当前阶段、里程碑进展、候选、Issue / PR / Run、基线历史与重复方法正文不得重新堆入 `AGENTS.md`。

## 8. Fresh Context 恢复顺序

新的 `agentic-dev` 上下文应：

1. 读取根 `AGENTS.md`，恢复稳定 Repository Governance 与 Authority Boundary；
2. 读取根 `README.md`，取得简短当前状态；
3. 读取本文，确认当前路线、门禁和候选边界；
4. 重新读取当前 GitHub `master`、Open PR / Issue 和必要 Actions；
5. 当前 v3 规划期间读取 `docs/project/rule-governance-knowledge-activation-v3.md` 与 Issue #94；
6. 读取 Issue #109 的当前状态和 `docs/architecture/agent-resource-model.md`：若 #109 仍开放，继续 V3-05；若已经完成关闭，则只把 V3-06 视为下一规划候选；
7. 只在资源模型结论需要证据时按需读取 V3-01 所有权模型、V3-02 审计矩阵、V3-03 生命周期、V3-04 技能重分类结果、代表性 `SKILL.md` / 技术画像 / 仓库本地规则，以及 `consumer-local-activation-metadata-contract-v2.md`；不重新做仓库盘点；
8. 不依赖其他聊天、历史会话或个人记忆补充未固化项目事实。

## 9. 更新触发

出现以下情况时更新本文：

- 当前有限里程碑或子任务门禁实质变化；
- 人工选择新的活动里程碑；
- 长期路线、候选优先级或完成定义改变；
- 新能力正式集成并改变 Fresh Context 恢复路径。

单次 Run ID、临时分支删除、PR 从 Draft 变为 Ready、PR 合并提交等纯 GitHub 原生状态不为了记录而机械写入 Roadmap；需要时直接从 Git / PR / Issue 恢复。
