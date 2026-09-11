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
V3-05 — 面向 Agent 的结构化资源模型已完成并集成。  
V3-06 — 资源发现架构，跟踪入口为 Issue #111。  
V3-06 工作产物：`docs/architecture/resource-discovery-architecture.md`。  
V3-06 启动基线：`master@640f1e3a8e7b5a6e67ad9ea028e51ba621e37964`。

V3-06 直接消费 V3-05 的资源模型和 v2 已验证的发现 / 路由行为。当前目标不是机械保留 Manifest + Catalog 两层，而是收敛：真实本地当前资源、可选已复核发现映射、可选纯生成运行视图和临时发现决策之间的边界，并固定一个主职责、最小辅助上下文、routing-only / 按需 Skill、Stage Return 与失败关闭接口。

V3-06 的精确审查、集成与完成状态由 Issue #111 和 GitHub 当前状态记录，不在 Roadmap 复制瞬时 PR 状态。Fresh Context 恢复时：

- 如果 Issue #111 仍开放，继续 V3-06 当前未完成门禁；
- 如果 Issue #111 已以完成原因关闭，V3-06 视为已收口，**V3-07 只成为下一规划候选**，仍需新的规划权威才能启动。

当前门禁：

> **V3-06 未完成时，先完成最小发现架构、current-set、任务事实、主职责 / 辅助上下文、按需 Skill、Stage Return、fail-closed、派生表示生命周期和 v2 replacement / compatibility 的收敛及 AI 复核；V3-06 完成后，只判断是否正式启动 V3-07，不继承 V3-06 权限。**

V3-06 不修改使用方仓库，不创建规则超级 Skill / 阶段路由 Skill / Runtime Controller，不全仓增加 Front Matter，也不在 V3-07 自采用前删除当前 v2 discovery / activation 兼容入口。

详细当前规划 / 审计 / 架构：

- `docs/project/rule-governance-knowledge-activation-v3.md`
- `docs/project/knowledge-capability-ownership-model-v3.md`
- `docs/project/current-repository-ownership-audit-v3.md`
- `docs/architecture/consumer-lifecycle.md`
- `docs/project/skill-reclassification-admission-v3.md`
- `docs/architecture/agent-resource-model.md`
- `docs/architecture/resource-discovery-architecture.md`
- `tasks/plans/20260911/04-rule-governance-v3-v3-06-resource-discovery.md`

## 2. v3 当前路线

v3 严格按以下顺序推进：

1. V3-01 — 知识与能力所有权模型 — **已完成并集成**；
2. V3-02 — 当前仓库所有权审计 — **已完成并集成**；
3. V3-03 — 使用方初始化、采用、升级与普通运行生命周期 — **已完成并集成**；
4. V3-04 — 技能重分类与准入 — **已完成并集成**；
5. V3-05 — 面向 Agent 的结构化资源模型 — **已完成并集成**；
6. V3-06 — 资源发现架构 — **状态见 Issue #111**；
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

V3-02 已按规范正文 / 规则族完成当前仓库审计，识别指南兜底、已完成项目记录中的现行过渡契约、派生路由与真实语义所有者重叠，以及技能 / 工程能力复制风险。

V3-03 已把使用方生命周期收敛为单一可复用工程能力语义所有者：采用 / 升级与普通运行分离，普通运行默认只依赖使用方本地当前状态。

V3-04 已确认当前 9 个技能身份继续成立，并把新增技能准入与支持资源边界提升到 `docs/architecture/skill-architecture.md`；工程纪律 / 技能契约 / `execute-unit` 已收敛为单点正文 + 薄消费。

V3-05 已建立三层资源模型：

```text
规范 / 事实正文
→ 资源固有结构
→ 派生发现投影
```

资源固有结构表达真实长期身份 / 生命周期事实；跨资源正规化职责 / 条件 / 风险等属于派生发现提示；V3-05 不把 Manifest record 等同于真实长期资源，也不新增独立于真实语义所有者的统一当前状态真值。现有 Activation Manifest 被判定为混合过渡载体，长期 provenance / locator / supersede 等固有事实迁出前不得整体删除。

V3-06 当前进一步把长期发现架构收敛为：

```text
本地当前资源与稳定入口
→ 可选 Reviewed Discovery Map
→ 可选纯生成 Runtime View
→ 临时发现决策
```

小型仓库可以不维护派生映射；需要跨资源语义正规化时，只维护一个 current 已复核发现映射。纯生成运行视图只能由真实资源 + current 映射确定性生成，不独立维护语义。

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

V3-02 已明确部分 v2 `docs/project/*` 仍承载现行过渡契约；在真实替代语义所有者 / 机制集成前不得提前归档或删除。

V3-03 已提炼长期使用方生命周期；V3-04 已提炼技能 / 工程能力边界；V3-05 已提炼长期资源模型；V3-06 当前接管长期 discovery / routing 语义并设计 replacement。当前 v2 发现 / 激活入口在 V3-07 自采用完成切换和验证前继续有效，不能因 V3-06 设计已形成就提前删除。

## 4. 当前范围边界

V3-06 只授权：

- 裁决最小发现架构是否需要 Manifest / Catalog / Index / generator；
- 定义 current resource set 如何从真实仓库权威、V3-01 维度、原生状态和 supersede / disable 关系形成；
- 区分当前任务事实、资源原生结构、已复核派生映射和纯生成运行视图；
- 定义候选发现、一个主职责、最小辅助上下文；
- 定义 routing-only / 按需 Skill、Stage Return 和旧状态失效；
- 定义 stale / missing / ambiguity 的本地 fail-closed；
- 定义 Reviewed Discovery Map 与纯生成 Runtime View 的更新、source binding、语义复核和重建边界；
- 完成 v2 `rule-activation-guide.md`、`consumer-local-rule-activation.md`、metadata contract、routing interface、Activation Manifest、Runtime Catalog 与手工路由表的逐项处置；
- 定义 V3-07 自采用所需 replacement / compatibility 输入契约；
- 更新本阶段稳定恢复入口并执行必要 AI 复核。

V3-06 不：

- 重新定义 V3-01～V3-05；
- 创建规则超级 Skill、阶段路由 Skill 或 Runtime Controller；
- 把完整开发生命周期塞入 Adapter / generator；
- 全仓批量增加 Front Matter 或统一 YAML / JSON schema；
- 修改任何使用方仓库；
- 直接执行 V3-07 / V3-08；
- 在 replacement 验证并集成前删除当前 v2 discovery / activation 入口；
- 建立数据库、向量库、图数据库、MCP 服务或后台 daemon；
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
9. 规则治理与知识激活 v3 / V3-02 — `docs/project/current-repository-ownership-audit-v3.md`（其审计矩阵仍是 V3-06 直接分析输入）
10. 规则治理与知识激活 v3 / V3-03 — `docs/architecture/consumer-lifecycle.md`（当前长期使用方生命周期权威）
11. 规则治理与知识激活 v3 / V3-04 — `docs/project/skill-reclassification-admission-v3.md`（技能身份 / 重叠裁决记录；稳定准入规则已进入技能架构）
12. 规则治理与知识激活 v3 / V3-05 — `docs/architecture/agent-resource-model.md`（当前长期资源语义与最小结构契约）

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
6. 读取 Issue #111 的当前状态和 `docs/architecture/resource-discovery-architecture.md`：若 #111 仍开放，继续 V3-06；若已经完成关闭，则只把 V3-07 视为下一规划候选；
7. 只在发现架构结论需要证据时按需读取 `docs/architecture/agent-resource-model.md`、V3-02 审计矩阵、V3-03 生命周期、V3-04 技能边界、`rule-activation-guide.md`、`consumer-local-rule-activation.md`、v2 metadata / routing contract 与对应 Skill / 工程能力；不重新做 V3-01～V3-05 分类工作；
8. 不依赖其他聊天、历史会话或个人记忆补充未固化项目事实。

## 9. 更新触发

出现以下情况时更新本文：

- 当前有限里程碑或子任务门禁实质变化；
- 人工选择新的活动里程碑；
- 长期路线、候选优先级或完成定义改变；
- 新能力正式集成并改变 Fresh Context 恢复路径。

单次 Run ID、临时分支删除、PR 从 Draft 变为 Ready、PR 合并提交等纯 GitHub 原生状态不为了记录而机械写入 Roadmap；需要时直接从 Git / PR / Issue 恢复。