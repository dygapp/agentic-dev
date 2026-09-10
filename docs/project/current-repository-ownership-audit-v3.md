# V3-02 当前仓库所有权审计

**状态：** 审计候选  
**跟踪：** Issue #101  
**审计基线：** `master@c646e4182cb32344feb9e0872bb3828d4be01481`  
**分类权威：** `docs/project/knowledge-capability-ownership-model-v3.md`

## 1. 目的与边界

本文对 `agentic-dev` 当前长期知识、规则、工程能力、项目治理与历史证据执行语义所有权审计。

本轮只回答：

> 当前正文由谁拥有、当前位置是否匹配语义、是否存在重复 owner，以及后续应保留、重分类、拆分、合并、取代还是删除。

本文**不是迁移计划**，不执行文件移动、删除、Skill 重构、Front Matter 设计或发现机制实现。后续 disposition 只有进入相应 V3-03～V3-06 设计并通过各自 Gate 后才能实施。

审计单位优先级：

```text
规范正文 / 规则族
→ 可独立演进的 section
→ 只有正文不可合理拆分时才按整文件判断
```

目录名、文件名、Markdown 形式和当前被谁读取都不能直接决定语义所有者。

## 2. 审计字段

每项使用以下语义：

- **语义所有者**：核心方法 / 原则、技能 / 过程型能力、可复用工程能力、仓库本地政策 / 规范 / 规则、项目 / 产品权威、Guide、研究 / 输入 / 证据；
- **适用范围**：跨仓库可复用、仓库本地、外部输入、仅历史；
- **来源状态**：本仓原生、从上游采用、从外部输入提升、派生投影、外部未采用、历史来源；
- **生命周期**：启动 / 初始化、首次采用、基线升级、普通运行、职责按需加载、验证 / 复核、仅历史 / 证据；
- **适配度**：`fit`、`mixed`、`mislocated`、`transitional-current`、`historical`；
- **Disposition**：`keep`、`move`、`merge`、`split`、`supersede`、`delete`、`reclassify`。

`move / split / supersede / delete` 在本文中只表示**后续候选**，不授予当前物理修改权限。

## 3. 总体结论

当前仓库并不存在“所有 Guide 都有问题”或“所有项目文档都只是历史”的简单结论。主要 ownership debt 集中在四类边界：

1. **Guide catch-all debt**：`docs/guides/*` 同时承载人类使用说明、仓库本地规范、跨项目工程纪律、Consumer 采用生命周期和普通运行发现架构；
2. **completed-project/current-contract debt**：v2 已完成，但若干 `docs/project/*-v2.md` 仍保存当前 Consumer-local discovery / adoption / runtime 的可复用契约；它们不能既被当成纯历史，又继续作为现行行为依据；
3. **derived-router debt**：`rule-activation-guide.md` 是手工维护的派生路由表，不拥有规则正文，却仍是当前上游入口；后续只能在新发现架构经验证后被显式取代，不能与新路由器长期并存；
4. **cross-owner duplication risk**：部分 Skill 为了执行便利复制了工程纪律 / 验证规则的详细表达，部分 Guide 又复制 Skill 路由或项目产物生命周期。当前尚不足以直接删除，V3-04 必须按规则族复核正文重叠。

同时，以下结构当前所有权基本健康：

- `docs/method/*` 作为核心方法 / 原则 owner；
- `docs/architecture/engineering-capability-architecture.md`、`engineering-disciplines.md`、`technology-profile-contract.md` 作为可复用工程能力架构与契约 owner；
- 当前 9 个 `SKILL.md` 作为过程型能力 owner；
- `docs/technology-profiles/vue3-typescript.md` 作为技术 / 验证画像 owner；
- `docs/research/*` 与 Eval 作为研究 / 证据，不参与普通运行权威；
- Roadmap 作为当前项目路线权威。

## 4. 稳定核心资源审计

| 当前资源 | 语义所有者 | 适用范围 / 来源 | 生命周期 | 当前适配度 | disposition | 后续依赖 |
|---|---|---|---|---|---|---|
| `AGENTS.md` | 仓库本地政策 / Bootstrap | 仓库本地 / 本仓原生 | 启动、普通仓库治理 | fit | keep；后续只更新被取代的入口指针 | V3-03、V3-06 |
| `README.md` | Guide / 人类导航与状态投影 | 仓库本地 / 派生投影 | 启动、人类恢复 | fit | keep；不提升为规范正文 owner | V3-06 |
| `docs/method/ai-development-method.md` | 核心方法 | 跨仓库可复用 / 本仓原生 | 普通运行、方法变更 | fit | keep | V3-03、V3-04 |
| `docs/method/principles.md` | 核心原则 | 跨仓库可复用 / 本仓原生 | 普通运行、按条件读取 | fit | keep | V3-03、V3-04 |
| `docs/architecture/engineering-capability-architecture.md` | 可复用工程能力架构 | 跨仓库可复用 / 本仓原生 | 能力设计、采用 | fit | keep；后续吸收最终 v3 ownership 架构关系 | V3-03、V3-04 |
| `docs/architecture/engineering-disciplines.md` | 可复用工程能力 / 工程纪律 | 跨仓库可复用 / 本仓原生 | 职责按需加载 | fit | keep；V3-04 检查 Skill 内重复正文 | V3-04、V3-05 |
| `docs/architecture/technology-profile-contract.md` | 可复用工程能力契约 | 跨仓库可复用 / 本仓原生 | 技术画像设计、采用 | fit | keep | V3-05 |
| `docs/architecture/skill-architecture.md` | Skill 架构 / 准入边界 | 跨仓库可复用 / 本仓原生 | Skill 设计与复核 | fit | keep | V3-04 |
| `docs/architecture/skill-contracts.md` | Skill 契约 | 跨仓库可复用 / 本仓原生 | Skill 设计、实现、复核 | fit | keep | V3-04 |
| `docs/architecture/first-batch-skill-design.md` | 历史实现设计 / 过渡设计基线 | 仅历史 / 本仓原生 | 历史参考 | transitional-current | supersede 为历史设计参考；从 `skills/README.md` 的“当前权威设计参考”中退出候选 | V3-04 |
| `docs/decisions/method-decisions.md` | 方法 / 架构决策记录 | 跨仓库可复用语义 + 历史来源 | 决策追溯、按需读取 | fit | keep；依靠显式 superseded 状态区分当前与历史 | ADR Gate |
| `docs/technology-profiles/vue3-typescript.md` | 可复用工程能力 / 技术与验证画像 | 跨仓库可复用 / 本仓原生 | 技术命中时按需加载 | fit | keep | V3-05 |
| `docs/technology-profiles/README.md` | Guide / capability inventory | 跨仓库可复用资源的导航投影 | 人类导航、采用 | fit | keep；不拥有画像规则正文 | V3-05、V3-06 |
| `tasks/README.md` | 仓库本地政策 / 协调规范 | 仓库本地 / 本仓原生 | 复杂任务命中时普通运行 | fit | keep；路径无需为了分类而机械移动 | V3-05 |

### 4.1 `AGENTS.md` 的特殊说明

根 Bootstrap 当前包含仓库职责、权威顺序、知识边界、外部操作、AI 复核、语言、研究采用和 Git 提交的薄规则与指针。其职责本身合理。

需要后续维护的不是把这些内容全部移出，而是：

- 现有 `rule-activation-guide.md` 若在 V3-06 被取代，更新 Consumer 使用入口；
- `external-operation-guidelines.md`、`terminology-guidelines.md`、`git-commit-guidelines.md` 后续重分类时同步指针；
- 不把 v3 当前阶段、Issue、PR 或审计结果重新塞回 `AGENTS.md`。

## 5. 当前 9 个 Skill 审计

| Skill | 语义所有者 | 当前适配度 | disposition | 主要重叠复核点 |
|---|---|---|---|---|
| `clarify-intent` | 技能 / 过程型能力 | fit | keep | 长期领域事实只识别候选，不接管 Project Authority |
| `specify` | 技能 / 过程型能力 | fit | keep | Requirement / Domain Authority 的写入权仍由 Consumer Authority 决定 |
| `technical-plan` | 技能 / 过程型能力 | fit | keep | ADR / Architecture 身份由方法 / 架构定义，Skill 只拥有处理过程 |
| `slice-work` | 技能 / 过程型能力 | fit | keep | 不把任务文件格式提升为方法要求 |
| `readiness-check` | 技能 / 过程型能力 | fit | keep | 验证规则族只消费，不复制跨职责 owner |
| `execute-unit` | 技能 / 过程型能力 | fit with overlap risk | keep + V3-04 overlap review | 当前包含较详细工程纪律薄判断；检查是否仍是“薄消费”而非第二规范正文 |
| `systematic-debug` | 技能 / 过程型能力 | fit | keep | 只处理 expected behavior 已明确后的 unexpected failure |
| `converge` | 技能 / 过程型能力 | fit with overlap risk | keep + V3-04 overlap review | completion evidence / feature-wide acceptance 与验证纪律边界 |
| `github-actions-verification` | 平台专项技能 / 过程型能力 | fit | keep | 平台过程由本 Skill 单点拥有，外部操作能力只保留平台无关约束 |

`skills/github-actions-verification/references/*` 属于该 Skill 的 supporting resources，只要正文仍直接服务该 Skill 过程，应继续随 Skill owner 维护，不单独升级为平级语义所有者。

`skills/README.md` 是 Skill inventory / 人类导航，不拥有各 Skill procedure；应保留，但 V3-04 应移除对已经失去当前设计权威身份的 `first-batch-skill-design.md` 的“权威设计参考”表达。

## 6. `docs/guides/*` 逐项审计

### 6.1 `using-agentic-dev.md`

**文件级结论：mixed → split / reduce，Guide 主身份保留。**

| 当前正文族 | 正确语义所有者 | 当前问题 | disposition 候选 | 后续依赖 |
|---|---|---|---|---|
| 使用模型、知识边界、人类理解入口 | Guide | 与 Guide 边界一致 | keep | V3-03 |
| 外部需求来源如何进入 Consumer Authority | Consumer 生命周期 / Project Authority adoption 规则 | 低频采用语义，当前可留 Guide 解释，但规范边界不应只存在于 Guide | extract normative lifecycle + Guide pointer | V3-03 |
| 新项目最小 Bootstrap、语言、不要预建空结构 | Consumer 初始化 + Repository-local policy formation | 混合初始化过程与本地规则示例 | split：规范生命周期进入 V3-03，Guide 保留解释 | V3-03 |
| Skill inventory / responsibility routing 表 | Skill discovery / derived navigation | 手工复制职责映射，可能与 Skill 原生 discovery 漂移 | reduce / supersede manual routing after V3-06 | V3-04、V3-06 |
| 验证、工程纪律、外部操作入口 | 指针 | 当前仅导航可接受 | keep as thin pointers if Guide remains | V3-04 |
| baseline adoption / upgrade | Consumer 生命周期 | 当前是重要规范语义，不应长期只有 Guide owner | extract / promote | V3-03 |
| Roadmap 生命周期 | Project Authority lifecycle / Repository governance | Guide 不应单点拥有项目权威生命周期 | move normative semantics to proper owner，Guide 仅解释 | V3-03 |
| Fresh Context recovery | Bootstrap / discovery architecture | 普通运行语义混入 Guide | reclassify / pointer-only | V3-06 |
| agentic-dev experiment / feedback | agentic-dev 仓库治理 + Evidence lifecycle | 不属于 Consumer ordinary Guide 核心 | split or pointer | V3-03、V3-08 |
| 推荐启动提示与使用目标 | Guide | 人类说明合理 | keep | 无 |

结论不是删除 `using-agentic-dev.md`，而是让它最终真正成为**人类 + 初始化 / 采用 / 升级说明 Guide**，不再承担 ordinary runtime procedure 或规范正文兜底。

### 6.2 `consumer-local-rule-activation.md`

**文件级结论：mixed / mislocated → split + reclassify，当前先保持兼容。**

| Section / 规则族 | 正确语义所有者 | disposition 候选 | 后续依赖 |
|---|---|---|---|
| §1～3 本地运行目标、薄 Bootstrap、发现对象 | Consumer lifecycle + discovery architecture | extract / promote | V3-03、V3-06 |
| §4 Activation Manifest / Runtime Catalog | v2 过渡性 discovery representation | keep transitional until V3-05/06 decides need；随后 supersede 或 promote | V3-05、V3-06 |
| §5 来源时效性 | discovery architecture / reusable constraint | reclassify | V3-06 |
| §6 主职责路由 | discovery / responsibility routing | reclassify；不得形成平行 Stage Router | V3-04、V3-06 |
| §7 routing-only vs Skill execution | Skill/discovery interface | reclassify | V3-04、V3-06 |
| §8 Stage Return | Method + Skill contracts + discovery re-routing | 去除重复正文，保留 discovery-specific consequence | V3-04、V3-06 |
| §9 fail-closed | discovery architecture | reclassify | V3-06 |
| §10～11 baseline state / local projection | Consumer adoption / upgrade lifecycle | reclassify | V3-03 |
| §12 Runtime Adapter boundary | reusable engineering capability / Runtime Adapter architecture | promote to architecture if retained | V3-06 |
| §13 adoption acceptance | validation / evidence input | migrate to V3-08 acceptance model | V3-08 |

在新的 owner 经验证前，本文件继续作为 v2 兼容入口，不能提前删除或失效。

### 6.3 `rule-activation-guide.md`

**文件级结论：派生导航投影，不是规范性 Guide owner。**

它保存“职责 / 风险 → 继续读取来源”的手工映射，但明确不拥有规则正文。因此：

- 当前适配度：`transitional-current`；
- disposition：`supersede` candidate；
- 只有 V3-06 证明新的最小 discovery 足以替代，并完成 Consumer / self-adoption 验证后才退出；
- 若最终仍需导航产物，应成为**可重建、可验证、source-current 的 derived projection**，而不是第二规范正文；
- 不能与未来 Resource Index / Router 长期并列为多个 current discovery mechanism。

### 6.4 `verification-evidence-rules.md`

**文件级结论：mislocated → reclassify 为可复用验证工程能力；不应继续是 Guide。**

| 规则族 | 目标 owner | disposition 候选 |
|---|---|---|
| Verification Contract Currentness | 可复用验证纪律 | reclassify |
| Visual Evidence | 条件性验证画像 / 验证纪律 | reclassify |
| Human Review Baseline Isolation | 可复用验证纪律 | reclassify |
| Database Migration Completion Evidence | 迁移类 Verification Profile | reclassify；representation 留 V3-05 |
| Evidence Claim Reuse Across Commits | 可复用验证纪律 + Consumer policy hook | reclassify |
| Evidence Type Must Match Claim | 可复用验证纪律 | reclassify；顶层“证据先于声明”仍由 Principle owner |
| Platform Boundary | 指针 | keep pointer to platform Skill / external-operation owner |

当前没有证据要求建立 `verify-evidence` 新 Skill；这些规则缺少独立统一任务入口与稳定独立输出。

### 6.5 `external-operation-guidelines.md`

**文件级结论：mixed → 主要 reclassify 为可复用外部操作工程能力，局部 Repository Policy hook。**

主要规则族：

- 读取 → 判断 → 写入 → 重读验证的外部操作闭环；
- “工具能力不等于授权”与跨仓库授权分别确认；
- 人工介入边界；
- 外部二进制 / 媒体输入真实性验证；
- 异步外部操作的有界观察与结果闭环；
- 共享资源、锁、租约、所有者和清理边界；
- 临时执行证据向持久输入的显式晋升；
- 依赖 PR / stacked PR 的集成拓扑安全。

其中平台无关、跨项目成立的执行约束属于**可复用工程能力 / 外部操作纪律**；具体仓库“允许谁合并、发布、部署、清理什么”的值必须由 Consumer Repository-local Policy 决定。GitHub Actions trigger / runtime / artifact 等平台具体 procedure 继续由 `github-actions-verification` Skill 单点拥有。

当前 disposition：`split + reclassify`；V3-04 只评估是否存在值得 Skill 化的独立 procedure，不预设新增 Skill。

### 6.6 `git-commit-guidelines.md`

**文件级结论：mislocated → Repository-local Policy / Standard。**

当前内容明确规定 `agentic-dev` 自身 Commit Message 格式、scope、分层提交与正文规则。不同 Consumer 可以合理不同，因此：

- 适用范围：仓库本地；
- 来源：本仓原生；
- 生命周期：普通仓库治理；
- disposition：`reclassify / move` candidate；
- upstream 可以在初始化时提供参考或模板，但不能持续拥有 Consumer 的 Git 规范当前值；
- 不 Skill 化。

### 6.7 `terminology-guidelines.md`

**文件级结论：mislocated → Repository-local Policy / Standard。**

当前内容约束 `agentic-dev` 面向人的中文表达、术语身份与固定标识；并明确 Consumer 的主导语言由 Consumer 自己决定。

- disposition：`reclassify / move` candidate；
- 术语表只负责**名称身份映射**，Method / Architecture / Contract 仍拥有概念职责语义；
- Consumer 可在初始化中采用规则思想或模板，但本地术语和主导语言采用后由 Consumer 自己演进。

## 7. `docs/project/*` 当前与历史边界

`docs/project/*` 不能整体视为同一种生命周期。当前需要分成四组。

### 7.1 当前项目权威 — keep

| 资源 | 角色 | disposition |
|---|---|---|
| `project-roadmap.md` | 当前项目路线 / Gate / 候选权威 | keep；随当前 Gate 更新 |
| `rule-governance-knowledge-activation-v3.md` | 当前有限里程碑权威 | keep，里程碑结束后转历史项目记录 |
| `knowledge-capability-ownership-model-v3.md` | 当前 v3 分类权威 | keep；最终是否提升进 Architecture / ADR 由后续收敛判断 |
| `repository-baseline.md` | 仓库项目基线 / 恢复信息 | keep，若内容仍 current；V3-05 再检查 metadata 形式 |

### 7.2 仓库本地政策误放在 `docs/project` — reclassify candidate

`docs/project/ai-review-guidelines.md` 明确只约束 `agentic-dev` 自身高影响变更如何复核，不是通用方法或 Consumer Guide。因此：

- 语义所有者：Repository-local Policy / Standard；
- disposition：`reclassify / move` candidate；
- `AGENTS.md` 保持薄摘要与指针；
- 不把该规则自动投射给 Consumer。

### 7.3 v2 仍支撑现行行为的过渡契约

这些文件物理上属于已完成 v2 项目记录，但部分正文仍在支撑当前可复用 runtime/adoption 语义。它们不能被普通 Fresh Context 当作完整历史过程加载，也不能在没有替代 owner 时直接归档。

| v2 资源 | 当前真实角色 | disposition 候选 | 目标阶段 |
|---|---|---|---|
| `consumer-local-activation-metadata-contract-v2.md` | discovery metadata / Catalog 过渡契约 | transitional-current；由 V3-05/06 决定 promote 或 supersede | V3-05、V3-06 |
| `consumer-local-baseline-adoption-projection-v2.md` | Consumer 采用 / 升级 / 本地投影语义 | extract / promote durable lifecycle，原文件随后 historical | V3-03 |
| `consumer-local-rule-runtime-target-v2.md` | Consumer-local ordinary runtime 目标与不变量 | extract durable semantics，随后 supersede 为历史项目记录 | V3-03、V3-06 |
| `consumer-local-runtime-routing-interface-v2.md` | discovery / routing interface | transitional-current；由 V3-06 新架构取代或提升 | V3-06 |
| `consumer-local-rule-runtime-acceptance-v2.md` | v2 runtime acceptance contract | 作为 V3-08 验证输入；可复用长期约束先进入正确 owner | V3-08 |

### 7.4 已完成项目记录 / Evidence — historical

以下类型默认只保留历史、证据、决策来源或里程碑追溯职责，不进入 ordinary runtime：

- `consumer-local-runtime-validation-plan-v2.md`；
- `consumer-local-runtime-validation-result-v2.md`；
- `consumer-local-runtime-candidate-drift-review-v2.md`；
- `rule-governance-knowledge-activation-v1.md` / `v2.md`；
- `rule-ownership-decomposition-audit-v2.md`；
- `engineering-capability-foundation-v1*.md`；
- `engineering-discipline-expansion-v1*.md`；
- `chinese-interaction-context-cleanup-v1.md`；
- `terminology-semantic-safety-v1.md`；
- `stacked-pr-squash-topology-v1.md`；
- 已经完成且其长期结论已提升到 Method / Architecture / Skill / Policy 的其他项目记录。

`engineering-discipline-scope.md` 属于形成现行 `engineering-disciplines.md` 的历史设计 / scope evidence；现行纪律正文应以后者为 owner。若没有 Current Authority 明确继续消费前者，则候选降为 historical supporting evidence，而不是并列现行纪律权威。

## 8. Research / Eval / Task 生命周期审计

### 8.1 `docs/research/*`

整个目录的默认语义所有者是 Research / Input / Evidence：

- 可以支撑新能力候选；
- 不因研究结论看起来成熟就自动成为现行规则；
- 已被 Method / Architecture / Profile / Skill 吸收的结论，其研究原文继续保留 provenance / evidence 身份；
- ordinary Fresh Context 不默认加载完整 Research。

Disposition：整体 `keep`，除非以后发现重复、失效或无保留价值的具体研究；V3-02 不进行清理。

### 8.2 `evals/*`

Eval schema、fixture、runner、历史评分与运行产物属于 Evaluation tooling / Evidence，不拥有 Method / Skill / Rule 正文。

`evals/rule-retrieval/*` 当前只保留冻结的历史设计与评分证据；旧 live index / runner 已退出 Current surface。Disposition：`keep historical`，禁止被 V3-06 误当作 current discovery implementation 复活。

### 8.3 `tasks/plans/*`

计划文件只承担阶段协调与恢复现场。已完成任务默认转为历史协调记录，不进入普通运行权威；新的长期结论必须提升到真实 owner。

Disposition：`keep historical/coordination`；当前 V3-02 计划在本阶段有效，阶段结束后自然退出 Current Authority。

## 9. 跨 owner 重叠与后续检查清单

以下问题在 V3-02 中已识别，但当前不直接修改正文：

| 重叠 | 风险 | 后续动作 |
|---|---|---|
| `using-agentic-dev.md` routing 表 vs Skill `description` / `Use When` | 手工路由漂移 | V3-04/06 以 native Skill discovery 为基准复核 |
| `consumer-local-rule-activation.md` Stage Return / routing vs Method / Skill Contract | 第二流程定义 | V3-04/06 只保留 discovery-specific consequence |
| `verification-evidence-rules.md` vs Principle / execute-unit / converge | 证据规则重复 owner | V3-04 按 rule family 保留一个 normative owner |
| `engineering-disciplines.md` vs `execute-unit` 长段薄规则 | 薄消费可能演化成复制正文 | V3-04 做语义 diff，不机械把纪律全部塞进 Skill |
| `external-operation-guidelines.md` vs `github-actions-verification` | 通用操作纪律与平台 procedure 混淆 | V3-04 保持 platform-specific procedure 单点 owner |
| `rule-activation-guide.md` vs future discovery mechanism | 多 current router | V3-06 必须显式替代，不并存 |
| v2 `docs/project/*` runtime contracts vs future V3-03/05/06 owners | completed-project 仍隐式 current | 新 owner 建立并验证后显式 supersede |
| `first-batch-skill-design.md` vs Skill contracts / current SKILL.md | 历史设计继续被称为当前权威 | V3-04 收敛 inventory 指针 |

## 10. Disposition 依赖图

V3-02 不直接实施上述 disposition。推荐后续依赖如下：

```text
V3-02 审计矩阵
    ├─→ V3-03 Consumer lifecycle
    │     ├─ using-agentic-dev adoption / upgrade
    │     ├─ consumer-local baseline projection
    │     └─ v2 runtime target 中 lifecycle semantics
    │
    ├─→ V3-04 Skill reclassification
    │     ├─ Skill / discipline overlap
    │     ├─ verification rule families
    │     ├─ external-operation capability
    │     └─ first-batch-skill-design historical status
    │
    ├─→ V3-05 AI-ready resource model
    │     ├─ Policy / Standard representation
    │     ├─ Engineering Capability metadata
    │     └─ transitional v2 metadata contract
    │
    └─→ V3-06 discovery architecture
          ├─ rule-activation-guide replacement decision
          ├─ consumer-local routing / fail-closed
          ├─ Runtime Adapter boundary
          └─ Resource Index / Catalog necessity decision
```

V3-07 自采用负责执行最终被批准的 repository-local migration；V3-08 再证明 Consumer 初始化、升级与 ordinary runtime 没有因为重构发生行为回归。

## 11. V3-02 Gate 判断标准

进入 V3-02 独立复核前应确认：

- 七个 `docs/guides/*` 已按 semantic body / rule family 审计；
- Method、Architecture、Technology Profile、9 个 Skill、Project、Research、Eval、Task 的边界均有明确结论；
- v2 过渡性现行契约与纯历史项目记录已经分开；
- 所有 `move / split / supersede / delete` 都仍只是候选，没有发生物理迁移；
- V3-03～V3-06 可以直接使用本矩阵，而不需要再次做同义 inventory；
- 独立复核对高风险 ownership ambiguity 的 Blocking / Medium 为 0。

如果独立复核发现“某个当前规范正文没有明确 owner”“同一规则被两个 owner 同时声明 current”“历史资源仍被普通运行误认为 current”等问题，应先修订本审计矩阵，再进入后序阶段。