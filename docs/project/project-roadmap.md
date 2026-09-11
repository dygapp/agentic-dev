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
V3-06 — 资源发现架构已完成并集成。  
V3-07 — `agentic-dev` 自采用与发现机制切换已完成并集成。  
V3-08 — Consumer 验证与持续有效性复核，跟踪入口为 Issue #115。  
V3-08 工作产物：`docs/project/rule-governance-v3-v3-08-consumer-validation.md`、`tasks/plans/20260911/06-rule-governance-v3-v3-08-consumer-validation.md`。  
V3-08 启动基线：`master@2fe193035c629f6b8805fd473bd322f70fe6e172`。

V3-07 已把 `agentic-dev` 自身 ordinary runtime 收敛为：

```text
Local Discovery Entry
+ Reviewed Discovery Map
```

Reviewed Discovery Map 是非规范性派生输入，不进入 Repository Authority；当前没有证据要求额外 Runtime View / Catalog / generator。

V3-08 不继续设计新的 discovery 容器，而是用真实 Consumer 验证 V3-03～V3-07 的生命周期、资源与发现语义是否能够：

- 被 Existing Consumer 显式 baseline upgrade 采用；
- 在 ordinary Fresh Context 中只依赖 Consumer-local current state；
- 正确处理职责、supporting capability、Stage Return、source currentness、coverage drift 与失败关闭；
- 降低不必要的默认上下文成本而不牺牲 correctness；
- 在真实后续项目演进中持续有效；
- 对 first-adoption 语义取得可审计 Evidence。

Primary real Consumer 为 `dygapp/jilinjobs-cms`。当前 `agentic-dev` 工作只允许读取该 Consumer、设计验证并接收 Evidence；Consumer 写实验必须在其自身 Repository Authority 下独立执行。

V3-08 当前 Gate：**Gate A — Validation Design**。

Gate A 已恢复到 Consumer 当前真实状态，并明确：

- Consumer 当前 evaluated `agentic-dev` baseline 为 `d9fad0da83dbdb61cac5eb9778b0258c6861eef1`；
- V3-08 candidate baseline 为 `2fe193035c629f6b8805fd473bd322f70fe6e172`；
- exact upstream delta 为 34 commits ahead / 0 behind，必须逐项分类，不允许复制完整 upstream；
- Consumer 当前 EU-54 已进入独立 Execute 生命周期，V3-08 在其自然收口前只做旁路只读观察；
- Consumer `docs/work/current/*` 与 Issue / PR Current Evidence 当前存在真实状态冲突，V3-08 要验证 conflict detection / fail-closed，而不是预设某一载体天然优先；
- Existing Consumer baseline upgrade、post-adoption runtime、持续有效性和 first-adoption claim coverage 分轨验证；
- `docs/README.md` 只是 Consumer Local Discovery Entry 的候选，不是预设物理答案；Reviewed Discovery Map 同样必须由 Consumer local inventory 决定是否需要。

V3-08 的精确 Gate、Consumer Evidence、PR / Actions 与完成状态由 Issue #115 和当前 GitHub 状态记录，不在 Roadmap 复制瞬时 Consumer PR Head 或 workflow 状态。Fresh Context 恢复时：

- 如果 Issue #115 仍开放，继续 V3-08 当前未完成 Gate；
- 如果 Issue #115 已以完成原因关闭，V3-08 视为已收口，**独立复核只成为下一规划候选**，仍需独立授权才能启动。

当前门禁：

> **先完成 Gate A 验证设计、风险 / AI 复核和 Consumer handoff；EU-54 未自然收口前不得进入 Consumer baseline-upgrade 写实验。后续必须取得真实 Consumer Gate B～D Evidence，不能用设计推演代替 V3-08 完成。**

详细当前规划 / 审计 / 架构 / 自采用 / Consumer 验证：

- `docs/project/rule-governance-knowledge-activation-v3.md`
- `docs/project/knowledge-capability-ownership-model-v3.md`
- `docs/project/current-repository-ownership-audit-v3.md`
- `docs/architecture/consumer-lifecycle.md`
- `docs/project/skill-reclassification-admission-v3.md`
- `docs/architecture/agent-resource-model.md`
- `docs/architecture/resource-discovery-architecture.md`
- `docs/project/rule-governance-v3-v3-07-self-adoption.md`
- `docs/project/rule-governance-v3-v3-08-consumer-validation.md`
- `docs/discovery/README.md`
- `tasks/plans/20260911/06-rule-governance-v3-v3-08-consumer-validation.md`

## 2. v3 当前路线

v3 严格按以下顺序推进：

1. V3-01 — 知识与能力所有权模型 — **已完成并集成**；
2. V3-02 — 当前仓库所有权审计 — **已完成并集成**；
3. V3-03 — 使用方初始化、采用、升级与普通运行生命周期 — **已完成并集成**；
4. V3-04 — 技能重分类与准入 — **已完成并集成**；
5. V3-05 — 面向 Agent 的结构化资源模型 — **已完成并集成**；
6. V3-06 — 资源发现架构 — **已完成并集成**；
7. V3-07 — `agentic-dev` 自采用与发现机制切换 — **已完成并集成**；
8. V3-08 — Consumer 验证与持续有效性复核 — **状态见 Issue #115**；
9. 独立复核；
10. 必要 ADR、正式 v3 设计与实现规划。

顺序只定义规划依赖，不自动授予后序任务权限。

V3-01 建立四维所有权判断：

```text
语义所有者
+ 适用范围 / 来源状态
+ 运行 / 生命周期角色
+ 载体 / 权威形式
```

V3-02 完成当前仓库语义所有权审计。V3-03 将使用方生命周期提升为长期可复用工程能力。V3-04 确认当前 9 个 Skill 身份并固定 Skill 准入 / 支持资源边界。V3-05 建立：

```text
规范 / 事实正文
→ 资源固有结构
→ 派生发现投影
```

V3-06 建立长期发现架构：

```text
本地当前资源与稳定入口
→ 可选 Reviewed Discovery Map
→ 可选纯生成 Runtime View
→ 临时发现决策
```

V3-07 根据本仓库真实复杂度选择**一个 Reviewed Discovery Map、无 Runtime View**，并把 `agentic-dev` 自身 ordinary runtime 入口切换到 `docs/discovery/README.md`。旧手工 Guide routing 已显式退出 current discovery responsibility。

V3-08 当前不改变上述架构，而通过真实 Consumer 回答：这些 owner / lifecycle / discovery semantics 是否真的可以被局部采用、保持 Consumer Authority 优先，并在长期 ordinary runtime 中持续运转。

## 3. v2 已集成基线与兼容退出

规则治理与知识激活 v2 已通过 PR #93 集成。其 Phase A～G 已验证并继续受 v3 保护的行为至少包括：

- 薄启动入口；
- 仓库 / Consumer 权威优先；
- 渐进式披露；
- 证据先于结论；
- 规范正文单点所有权；
- 派生发现机制不拥有规范正文；
- 陈旧 / 缺失 / 歧义时失败关闭；
- 主职责与最小辅助上下文分离；
- routing-only 不机械加载完整 Skill；
- 真正进入职责时按需加载 Skill；
- Stage Return 后重新判断；
- Consumer 普通运行只依赖 Consumer-local current resources；
- 基线逐项采用；
- 同一运行范围 / 发现职责不并行维护多个 current 派生机制。

V3-03～V3-06 已把这些长期语义分别提升到使用方生命周期、资源模型和资源发现架构。V3-07 已把 `agentic-dev` 自身仍 current 的 v2 手工发现 surface 降级为 Guide / historical / compatibility 角色，并建立唯一 current self-runtime discovery mechanism。

V2 项目记录继续保留历史设计与验证证据价值；它们不因为被长期架构取代而删除。V3-08 可以按 claim-level Evidence reuse 规则复用仍未被新语义改变的历史 Consumer evidence，但不能用“v2 总体通过”替代当前 V3 claim 证明。

## 4. 当前范围边界

V3-08 当前授权 `agentic-dev`：

- 读取真实 Consumer 当前 Repository Authority / GitHub Evidence；
- 建立 Gate A～D 验证矩阵、Evidence Contract、context-cost 口径与 finding classification；
- 记录 Existing Consumer previous / candidate upstream baseline；
- 设计 Consumer baseline upgrade 的逐项 adopt / retain-or-override / reject-not-applicable / supersede-remove 判定；
- 验证 local-only ordinary runtime、primary + supporting、currentness、coverage drift、fail-closed；
- 设计受控 negative tests，但不在本仓库会话直接执行 Consumer 写操作；
- 以真实后续 Consumer 工作验证 sustained validity；
- 关闭 first-adoption claim：优先 claim-level Evidence reuse，不足时用最小隔离 Consumer fixture；
- 对 Consumer findings 进行 reusable / Consumer-only / defect / efficiency 分类；
- 必要时修订 `agentic-dev` 当前长期 owner 并重新验证。

V3-08 当前不：

- 重新设计 V3-01～V3-07 作为默认起点；
- 在 `agentic-dev` 会话直接修改 `jilinjobs-cms`；
- 打断或扩大 Consumer 当前 EU-54 Execute scope；
- 把 `agentic-dev/docs/discovery/*` 实例复制给 Consumer；
- 强制 Consumer 建立 Reviewed Discovery Map / Runtime View / Manifest / Catalog；
- 用文件大小 / token 优化覆盖 correctness / Authority / fail-closed；
- 把 Consumer 产品事实提升为通用规则；
- 因一次 Consumer PASS 自动关闭 v3；
- 自动进入独立复核、ADR 或正式 v3 实现规划；
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

继续作为独立规划 / 研究输入，不构成常规 Method Gate、新 Skill 或默认模型策略。

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
8. v3 / V3-01 — `docs/project/knowledge-capability-ownership-model-v3.md`
9. v3 / V3-02 — `docs/project/current-repository-ownership-audit-v3.md`
10. v3 / V3-03 — `docs/architecture/consumer-lifecycle.md`
11. v3 / V3-04 — `docs/project/skill-reclassification-admission-v3.md`
12. v3 / V3-05 — `docs/architecture/agent-resource-model.md`
13. v3 / V3-06 — `docs/architecture/resource-discovery-architecture.md`
14. v3 / V3-07 — `docs/project/rule-governance-v3-v3-07-self-adoption.md`、`docs/discovery/README.md`

## 7. Root Bootstrap 与本地发现职责

为控制 Fresh Context 成本：

- `AGENTS.md`：稳定 Repository Governance、Authority Boundary 与 Agent 工作约束；不维护当前项目状态；
- `README.md`：简短当前状态与稳定导航；
- 本 Roadmap：详细项目路线、活动状态、候选与下一门禁；
- Git / PR / Issue / Actions：精确外部状态与执行证据；
- `docs/discovery/README.md`：只有需要跨资源判断职责 / 条件性能力时才进入的 Local Discovery Entry；
- `docs/discovery/reviewed-discovery-map.md`：非规范性派生发现映射，不保存项目状态或第二 current truth。

如果当前工作只是状态恢复、确认 Gate 或回答仓库事实，在读取 AGENTS / README / Roadmap / GitHub 当前状态后即可停止，不机械读取 Map 或所有 Skill。

V3-08 读取 Consumer 时同样遵守 Consumer Repository Authority；`agentic-dev` 自身发现入口和 Map 不自动成为 Consumer runtime input。

## 8. Fresh Context 恢复顺序

新的 `agentic-dev` 上下文应：

1. 读取根 `AGENTS.md`，恢复稳定 Repository Governance 与 Authority Boundary；
2. 读取根 `README.md`，取得简短当前状态；
3. 读取本文，确认当前路线、门禁和候选边界；
4. 重新读取当前 GitHub `master`、Open PR / Issue 和必要 Actions；
5. 当前 v3 规划期间读取 Issue #94；
6. 读取 Issue #115 与 `docs/project/rule-governance-v3-v3-08-consumer-validation.md`：若 #115 仍开放，继续 V3-08 当前 Gate；若已经完成关闭，则只把独立复核视为下一规划候选；
7. V3-08 Gate A / Consumer handoff 只读恢复 `dygapp/jilinjobs-cms` 当前 GitHub / Repository Authority；不得从本文复制某个历史 Consumer PR Head 作为当前事实；
8. 只有当前 `agentic-dev` 任务需要跨资源发现时读取 `docs/discovery/README.md`，并按需进入 Reviewed Discovery Map / current semantic owner；
9. 只在 V3-08 结论需要证据时按需读取 V3-03～V3-07 架构 / 项目记录与 v2 historical Evidence；不重新做已完成阶段设计；
10. 不依赖其他聊天、历史会话或个人记忆补充未固化项目事实。

## 9. 更新触发

出现以下情况时更新本文：

- 当前有限里程碑或子任务门禁实质变化；
- 人工选择新的活动里程碑；
- 长期路线、候选优先级或完成定义改变；
- 新能力正式集成并改变 Fresh Context 恢复路径。

单次 Run ID、临时分支删除、PR 从 Draft 变为 Ready、PR 合并提交等纯 GitHub 原生状态不为了记录而机械写入 Roadmap；需要时直接从 Git / PR / Issue 恢复。