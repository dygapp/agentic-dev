# 规则治理与知识激活 v3 — 知识与能力所有权收敛

**状态：** 规划中  
**跟踪：** Issue #94  
**启动基线：** `master@3c31ae96683c4a653f001402b889b40e87df976b`

## 1. 目标

v3 的首要目标不是继续增加 Rule Index、Manifest、Catalog 或其他发现技术，而是先解决更上游的问题：

> `agentic-dev` 中的长期知识、规则和 Agent 能力是否被放在正确的 semantic owner 中？

v1 / v2 已证明最小上下文、Consumer-local ordinary runtime、source currentness 和渐进式披露的重要性，但当前进一步暴露出：如果 Method、Skill、Engineering Capability、Repository-local Rule、Project Authority 与 Guide 的边界本身不清楚，任何新的 discovery mechanism 都会继承并放大 ownership debt。

因此 v3 采用以下顺序：

```text
先确定 owner
→ 再审计现有内容
→ 再确定 Consumer lifecycle
→ 再判断 Skill / reusable capability 边界
→ 最后才设计 metadata / discovery
```

## 2. 启动依据

规则治理与知识激活 v2 已通过 PR #93 集成到当前 `master`。v2 的可复用结果继续作为 v3 必须保护的已验证基线。

在正式启动 v3 前，临时评估分支 `eval/rule-governance-v3-gpt6-review` 对候选治理方向进行了独立挑战：

- 首轮评审：`REVISE`，Blocking=0，Medium=1；
- 唯一 Medium 指出原候选没有为 Engineering Discipline、Technology Profile、Verification Profile 等“跨项目可复用、但不具有独立任务流程”的能力提供明确归属；
- 该 finding 经当前正式工程能力架构复核后接受；
- 候选修订为四维 ownership 判断，并增加 Reusable Engineering Capability / Discipline / Profile；
- 定向复评通过：Blocking=0，Medium=0，Low=0。

这些评估结果只作为启动前 Evidence，不自动获得 Repository Authority。正式长期结论必须重新进入当前规划与后续 Architecture / Contract / ADR 等真实 owner。

## 3. 当前规划主线

v3 按以下有限子任务顺序推进：

1. **V3-01 — Knowledge & Capability Ownership Model**  
   建立可执行的 ownership decision matrix，作为后续审计的唯一分类依据。
2. **V3-02 — Current Repository Ownership Audit**  
   对当前仓库按 semantic body / rule family 审计，形成 keep / move / merge / split / supersede / delete 候选，不先执行物理迁移。
3. **V3-03 — Consumer Initialization / Adoption / Upgrade / Runtime Lifecycle**  
   明确一次性 setup 与 ordinary runtime 的严格边界，以及 Consumer-local 资源如何形成并自行演进。
4. **V3-04 — Skill Reclassification & Admission**  
   判断现有 Guide / Rule 中哪些属于已有 Skill、Reusable Engineering Capability、Repository-local Rule 或真正的新 Skill 候选。
5. **V3-05 — AI-ready Resource Model**  
   在 owner 已确定后定义哪些长期资源需要结构化 metadata，以及普通 Markdown 与 `SKILL.md` 的兼容边界。
6. **V3-06 — Discovery Architecture**  
   判断 ownership 修正后还需要多复杂的 Repository Resource Discovery；不得预设一定需要统一 Index。
7. **V3-07 — agentic-dev Self-Adoption**  
   让 `agentic-dev` 自身使用与 Consumer 相同的核心模型，避免维护两套架构。
8. **V3-08 — Consumer Validation**  
   在真实 Consumer 上验证 initialization / upgrade / ordinary runtime 与 source-currentness、上下文成本和 fail-closed 行为。

只有前序 Gate 满足后才能进入后序任务；Roadmap 顺序不自动授予 Execute Authority。

## 4. 当前稳定方向

v3 当前至少区分以下 semantic owner role：

1. Method / Principle；
2. Skill / Procedural Capability；
3. Reusable Engineering Capability / Discipline / Profile；
4. Repository-local Policy / Standard / Rule；
5. Project / Product Authority Resource；
6. Guide；
7. Research / Input / Evidence。

同时必须把以下维度与 semantic owner 分开判断：

- applicability / provenance scope；
- runtime / lifecycle role；
- representation / authority form。

Architecture、Contract、Profile、`SKILL.md`、Guide、ADR、Requirement、generated index 等文件或载体形式不能直接替代 semantic ownership 判断。

## 5. Guide 当前边界

Guide 的候选边界收敛为：

> 面向人，以及 initialization / adoption / baseline upgrade 等低频 setup 场景，解释如何理解、选择和采用 `agentic-dev`。

因此 Guide 可以在初始化或升级时被 Agent 完整读取；这种一次性 token 成本本身不是问题。

Guide 不应继续承担：

- ordinary runtime 的核心 Agent procedure；
- Repository-local policy 的默认正文；
- Project Authority 的事实正文；
- Reusable Engineering Capability 的默认容器；
- “不属于 Method / Skill”内容的 catch-all bucket。

`using-agentic-dev.md`、`verification-evidence-rules.md`、`external-operation-guidelines.md`、`rule-activation-guide.md` 和 `consumer-local-rule-activation.md` 都必须在 V3-02 按正文语义重新审计，而不是按当前目录名决定身份。

## 6. Consumer 初始化与演进方向

Consumer 初始化不是简单复制 `agentic-dev` 文件，而是一次显式 Repository Bootstrap / Adoption。

初始化至少可能处理：

- 选择性采用 Method / Skill / Reusable Engineering Capability；
- 建立 Consumer-local `AGENTS.md`、Git 规范、术语 / 语言规范、验证 / 集成政策等 Repository-local Rules；
- 如果已经提供原始需求，分析并形成初始 Consumer authoritative requirements；
- 如果没有原始需求，不为了模板完整制造空 Requirement / Architecture / ADR，后续按 Consumer-local Method / Skill 逐步形成；
- 明确 Raw Input / Research / Evidence 与 Current Authority 的边界。

采用完成后：

```text
origin / upstream provenance
≠
current authority
```

Consumer-local 规则和项目权威由 Consumer 自己拥有、维护和演进。ordinary runtime 不因 `agentic-dev` upstream 出现新提交就自动改变行为。

baseline upgrade 是显式、低频操作；升级期间可以重新读取 upstream Guide / Method / Skill / reusable resources，完成逐项 adopt / retain-or-override / reject / supersede 后再次回到 local-only ordinary runtime。

## 7. v1 / v2 Preservation

v3 必须继续保护至少以下已经验证的长期成果：

- Thin Bootstrap；
- Repository / Consumer Authority first；
- Progressive Disclosure；
- Evidence before claims；
- semantic body 单点 owner；
- derived discovery 不拥有规范正文；
- stale / missing / ambiguity fail-closed；
- primary responsibility 与最小 supporting context 分离；
- routing-only 不机械加载完整 Skill；
- 真正进入职责时 JIT load Skill；
- Stage Return 后重新判断；
- Consumer ordinary runtime local-only；
- baseline adoption 逐项 adopt / retain-or-override / reject / supersede；
- 同一 Runtime scope / discovery responsibility 不并行维护多个 Current derived mechanism。

v3 不以“重新设计”为理由推翻这些已经通过真实 Consumer 验证的行为。

## 8. 当前非目标

V3-01 / V3-02 完成前，不：

- 实现新的 Rule Index / Manifest / Catalog；
- 实现 Front Matter generator；
- 冻结统一 metadata schema；
- 创建 Rule Super Skill / Stage Router Skill；
- 批量新增或改造 Skill；
- 物理移动 / 拆分 Guide；
- 修改 Consumer Repository；
- 启动 WI-06 / WI-07 / WI-09 或其他独立候选。

## 9. ADR Gate

v3 不用一个“大 ADR”承载全部探索。

只有专项分析形成以下条件时才创建或更新 ADR：

- 决定具有跨当前任务的长期约束；
- 存在多个合理替代方案且长期后果实质不同；
- 后续 Agent 不知道选择理由时容易重新打开已经关闭的架构选择；
- 决定已经稳定到可以作为长期 Architecture Context，而不是仍处于探索。

高概率 ADR 候选包括：

- Knowledge & Capability Ownership Architecture；
- Skill-centric procedural runtime 与 Guide / rule-centric runtime 的长期边界；
- AI-ready Resource Metadata / generated Resource Index（仅在 V3-05 / V3-06 证明需要后）。

目录名、字段名、文件拆分数量等局部实现选择不因为属于 v3 就自动 ADR 化。

## 10. 当前 Gate

当前正式工作入口：Issue #95 — V3-01。

当前只授权完成 V3-01 的规划、分析、候选文档和必要复核。V3-01 Gate 为：

> ownership decision matrix 足以让独立 reviewer 对代表性资源得到一致分类，且不存在未解决的阻塞或中等级 ownership ambiguity。

达到 Gate 后，只能进入“是否启动 V3-02”的下一规划判断，不自动获得物理迁移或实现权限。
