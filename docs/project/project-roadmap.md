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
V3-08 — Consumer 验证与持续有效性复核已完成；Issue #115 已以 `completed` 关闭，最终全轨高影响复核 Blocking=0 / Medium=0。  
V3-08 工作产物：`docs/project/rule-governance-v3-v3-08-consumer-validation.md`、`tasks/plans/20260911/06-rule-governance-v3-v3-08-consumer-validation.md`；最终精确 Evidence 以 Issue #115 为准。  
V3-08 启动基线：`master@2fe193035c629f6b8805fd473bd322f70fe6e172`。

当前活动子任务：

> **v3 Independent Review — Issue #118 / Gate A**

Independent Review 复核对象冻结基线：`agentic-dev@86fe96756c7b3678d7b0bac10f32358a9372e84c`。  
Independent Review 执行时必须重新读取届时 GitHub current `master`；冻结 subject baseline 不等于执行时 current repository state。  
协调计划：`tasks/plans/20260912/01-rule-governance-v3-independent-review.md`。

V3-07 已把 `agentic-dev` 自身 ordinary runtime 收敛为：

```text
Local Discovery Entry
+ Reviewed Discovery Map
```

Reviewed Discovery Map 是非规范性派生输入，不进入 Repository Authority；当前没有证据要求额外 Runtime View / Catalog / generator。

V3-08 已用成熟 Existing Consumer 与最小 first-adoption fixture 验证 V3-03～V3-07 的长期语义：

- Existing Consumer 可以显式完成 baseline upgrade 与逐项 adopt / retain-or-override / reject / supersede；
- ordinary Fresh Context 可以只依赖 Consumer-local current resources，普通运行 upstream access = 0；
- primary responsibility、最小 supporting context、Stage Return、source currentness 与失败关闭在真实运行中成立；
- Page Content Architecture → EU-55 的真实后续演进完整走过 Planning、Technical Planning、slice/readiness、Execute、verification/debug、Human Review、Integration 与 Post-Integration closure；
- 最小新 Consumer fixture 完成 first adoption，并在新的 ordinary-runtime Fresh Context 中保持 local-only；
- 成熟 Consumer 与最小 fixture 都没有真实证据要求 Reviewed Discovery Map / Runtime View，这只证明其 optionality，不推导为“任何 Consumer 都不需要”；
- 没有 V3-08 Evidence 要求回改 V3-03 / V3-05 / V3-06 / V3-07 的长期 reusable Architecture。

V3-08 已完成并退出活动执行权限。Independent Review 现在拥有独立 Planning Authority，但**真正复核执行必须在新的 Fresh Context 中完成**；既有 PASS、作者会话和历史聊天都不得成为复核结论前提。

当前门禁：

> **Issue #118 / Gate A — Independent Review Protocol Ready 候选。当前只授权冻结独立复核 subject baseline、execution-time current-state recovery、Finding schema、Fresh Context 独立性要求与恢复入口；不自动授予 ADR、正式 v3 设计、实现规划或其他候选工作权限。**

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
- `tasks/plans/20260912/01-rule-governance-v3-independent-review.md`

## 2. v3 当前路线

v3 严格按以下顺序推进：

1. V3-01 — 知识与能力所有权模型 — **已完成并集成**；
2. V3-02 — 当前仓库所有权审计 — **已完成并集成**；
3. V3-03 — 使用方初始化、采用、升级与普通运行生命周期 — **已完成并集成**；
4. V3-04 — 技能重分类与准入 — **已完成并集成**；
5. V3-05 — 面向 Agent 的结构化资源模型 — **已完成并集成**；
6. V3-06 — 资源发现架构 — **已完成并集成**；
7. V3-07 — `agentic-dev` 自采用与发现机制切换 — **已完成并集成**；
8. V3-08 — Consumer 验证与持续有效性复核 — **已完成 / Issue #115 closed as completed**；
9. 独立复核 — **已启动 Planning / Issue #118 / Gate A**；
10. 必要 ADR、正式 v3 设计与实现规划 — **未启动，取决于 Independent Review 最终 Gate**。

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

V3-08 通过真实 Existing Consumer、完整持续演进和最小 first-adoption fixture 验证上述 owner / lifecycle / discovery semantics 可以被局部采用、保持 Consumer Authority 优先，并在 ordinary runtime 中持续运转。

Independent Review 的任务不是继续扩建上述架构，而是从新的 Fresh Context 挑战 `86fe967…` 冻结 subject 上的 V3-01～V3-08 与 PR #117 后的一致性状态，判断是否存在 Blocking / Medium、Evidence 泛化越界或真实 ADR candidate。执行时仍必须恢复届时 current Repository State，以识别 subject baseline 之后的 planning / recovery-only 变化或任何需要显式刷新复核对象的实质语义变化。只有最终 Blocking=0 / Medium=0 后，才能决定直接进入 v3 Closure，或进入 finding 支持的必要 ADR。

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

V2 项目记录继续保留历史设计与验证证据价值；它们不因为被长期架构取代而删除。V3-08 已按 claim-level Evidence reuse 规则复用仍未被新语义改变的历史 Consumer evidence，并通过独立最小 fixture 补齐无法复用的 first-adoption 语义；“v2 总体通过”没有被用来替代当前 V3 claim 证明。

## 4. 当前范围边界

Independent Review 当前拥有 Planning Authority，但 Gate A 不等于 Independent Review 已经完成。当前允许：

- 冻结 subject baseline、review scope、Finding schema 与独立性要求；
- 固定 execution-time current-state recovery 与 subject refresh 条件；
- 更新 README / Roadmap / Issue #94 / #118 等必要 recovery surface；
- 建立供新的 Fresh Context 使用的最小协调计划；
- 对 Gate A planning diff 执行与风险相称的 AI Review 与集成收敛。

真正 Independent Review 必须在新的 Fresh Context 中重新恢复 Repository Authority、当前 GitHub State 与必要 V3 Authority，不得把冻结 subject SHA 当作 current master，也不得把作者会话、历史聊天、旧 AI Review PASS 或 Issue #118 中的总结性 claim 当作结论前提。

当前仍不自动：

- 重新设计 V3-01～V3-07；
- 修改 Consumer Repository；
- 把 `agentic-dev/docs/discovery/*` 实例复制给 Consumer；
- 强制 Consumer 建立 Reviewed Discovery Map / Runtime View / Manifest / Catalog；
- 用文件大小 / token 优化覆盖 correctness / Authority / fail-closed；
- 把单一 Consumer 或 fixture 事实泛化成所有 Consumer 的通用结论；
- 因 V3-08 PASS 或 Gate A 建立自动关闭 v3；
- 自动创建 ADR、正式 v3 设计或实现规划；
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
15. v3 / V3-08 — `docs/project/rule-governance-v3-v3-08-consumer-validation.md`、Issue #115

## 7. Root Bootstrap 与本地发现职责

为控制 Fresh Context 成本：

- `AGENTS.md`：稳定 Repository Governance、Authority Boundary 与 Agent 工作约束；不维护当前项目状态；
- `README.md`：简短当前状态与稳定导航；
- 本 Roadmap：详细项目路线、活动状态、候选与下一门禁；
- Git / PR / Issue / Actions：精确外部状态与执行证据；
- `docs/discovery/README.md`：只有需要跨资源判断职责 / 条件性能力时才进入的 Local Discovery Entry；
- `docs/discovery/reviewed-discovery-map.md`：非规范性派生发现映射，不保存项目状态或第二 current truth。

如果当前工作只是状态恢复、确认 Gate 或回答仓库事实，在读取 AGENTS / README / Roadmap / GitHub 当前状态后即可停止，不机械读取 Map 或所有 Skill。

Consumer 的采用与 ordinary runtime 始终遵守 Consumer 自己的 Repository Authority；`agentic-dev` 自身发现入口和 Map 不自动成为 Consumer runtime input。

## 8. Fresh Context 恢复顺序

新的 `agentic-dev` 上下文应：

1. 读取根 `AGENTS.md`，恢复稳定 Repository Governance 与 Authority Boundary；
2. 读取根 `README.md`，取得简短当前状态；
3. 读取本文，确认当前路线、门禁和候选边界；
4. 重新读取执行时当前 GitHub `master`、Open PR / Issue 和必要 Actions；
5. 当前 v3 规划期间读取 Issue #94；
6. Issue #115 已完成关闭，因此 V3-08 是已完成 Evidence，而不是活动 Gate；只有当前任务需要挑战 V3-08 claim 时才按需读取其项目记录与 Issue Evidence；
7. 当前 Independent Review 的 Planning / Evidence Authority 为 Issue #118；复核对象冻结在 `86fe967…`，但真正执行必须使用新的 Fresh Context 恢复届时 current Repository State，并确认 subject baseline 之后没有未处理的 V3 语义变化；
8. 只有当前 `agentic-dev` 任务需要跨资源发现时读取 `docs/discovery/README.md`，并按需进入 Reviewed Discovery Map / current semantic owner；
9. 只有具体 Finding 需要追溯时才按 Evidence locator 最小扩读已完成 V3-01～V3-08、v2 historical Evidence、Research 或 Eval；不重新做已完成阶段设计；
10. 不依赖其他聊天、历史会话或个人记忆补充未固化项目事实。

## 9. 更新触发

出现以下情况时更新本文：

- 当前有限里程碑或子任务门禁实质变化；
- 人工选择新的活动里程碑；
- 长期路线、候选优先级或完成定义改变；
- 新能力正式集成并改变 Fresh Context 恢复路径。

单次 Run ID、临时分支删除、PR 从 Draft 变为 Ready、PR 合并提交等纯 GitHub 原生状态不为了记录而机械写入 Roadmap；需要时直接从 Git / PR / Issue 恢复。