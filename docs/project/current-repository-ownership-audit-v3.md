# V3-02 当前仓库所有权审计

**状态：** 已完成并集成  
**跟踪：** Issue #101  
**审计基线：** `master@c646e4182cb32344feb9e0872bb3828d4be01481`  
**分类权威：** `docs/project/knowledge-capability-ownership-model-v3.md`

## 1. 目的与边界

本文对 `agentic-dev` 当前长期知识、规则、工程能力、项目治理与历史证据执行语义所有权审计。

本轮只回答：

> 当前正文由谁拥有、适用于哪里、怎样进入当前仓库、何时被消费、当前位置是否匹配语义、是否存在重复 owner，以及后续应保留、重分类、拆分、合并、取代还是删除。

本文**不是迁移计划**，不执行文件移动、删除、Skill 重构、Front Matter 设计或发现机制实现。本文记录的 disposition 只有进入相应 V3-03～V3-06 设计并通过各自 Gate 后才能实施。

审计单位优先级：

```text
规范正文 / 规则族
→ 可独立演进的 section
→ 只有正文不可合理拆分时才按整文件判断
```

目录名、文件名、Markdown 形式和当前被谁读取都不能直接决定语义所有者。

## 2. 审计字段与判定约束

每个审计项至少记录：

- **当前位置 / section**；
- **语义所有者**：核心方法 / 原则、技能 / 过程型能力、可复用工程能力、仓库本地政策 / 规范 / 规则、项目 / 产品权威、Guide、研究 / 输入 / 证据；派生投影本身不获得独立规范正文所有权；
- **适用范围**：跨仓库可复用、仓库本地、外部输入、仅历史；
- **来源状态**：本仓原生、从上游采用、从外部输入提升、派生投影、外部未采用、历史来源；
- **运行 / 生命周期角色**：启动 / 初始化、首次采用、基线升级、普通运行、职责按需加载、验证 / 复核、仅历史 / 证据；
- **载体 / 权威形式**；
- **当前 ownership 适配度**：`fit`、`mixed`、`mislocated`、`transitional-current`、`historical`；
- **重叠 / duplicate owner**；
- **Disposition**：`keep`、`move`、`merge`、`split`、`supersede`、`delete`、`reclassify`；
- **目标 owner / target responsibility**，但不提前冻结最终文件路径；
- **理由与 downstream impact**；
- **V3-03 / V3-04 / V3-05 / V3-06 / V3-08 dependency**。

其中“适用范围”和“来源状态”必须分别判断。例如一个 Consumer 从 upstream 采用的资源，可以同时是“仓库本地”适用范围和“从上游采用”来源状态。

`move / split / supersede / delete` 在本文中只表示**后续候选**，不授予当前物理修改权限。

## 3. 总体结论

当前仓库并不存在“所有 Guide 都有问题”或“所有项目文档都只是历史”的简单结论。主要 ownership debt 集中在五类边界：

1. **Guide catch-all debt**：`docs/guides/*` 同时承载人类使用说明、仓库本地规范、跨项目工程纪律、Consumer 采用生命周期和普通运行发现架构；
2. **completed-project/current-contract debt**：v2 已完成，但若干 `docs/project/*-v2.md` 仍保存当前 Consumer-local discovery / adoption / runtime 的可复用契约；它们不能既被当成纯历史，又继续作为现行行为依据；
3. **repository-policy/project-path debt**：`repository-baseline.md`、`ai-review-guidelines.md` 虽位于 `docs/project/`，语义上主要是 `agentic-dev` 仓库本地政策，而不是项目 / 产品事实；
4. **derived-router debt**：`rule-activation-guide.md` 是手工维护的派生路由表，不拥有规则正文，却仍是当前上游入口；后续只能在新发现架构经验证后被显式取代，不能与新路由器长期并存；
5. **cross-owner duplication risk**：部分 Skill 为了执行便利复制了工程纪律 / 验证规则的详细表达，部分 Guide 又复制 Skill 路由或项目产物生命周期。当前尚不足以直接删除，V3-04 必须按规则族复核正文重叠。

同时，以下结构当前所有权基本健康：

- `docs/method/*` 作为核心方法 / 原则 owner；
- `docs/architecture/engineering-capability-architecture.md`、`engineering-disciplines.md`、`technology-profile-contract.md` 作为可复用工程能力架构 / 契约 owner；
- 当前 9 个 `SKILL.md` 作为过程型能力 owner；
- `docs/technology-profiles/vue3-typescript.md` 作为技术 / 验证画像 owner；
- `docs/research/*` 的研究正文与 Eval 的语料 / 结果保持研究 / 证据身份；但 Research / Eval 目录中的 README、执行说明与当前隔离 / 评分规则仍必须按自身 semantic body 单独判断，不能整目录降格为 Evidence；
- Roadmap 作为当前项目路线权威。

## 4. 根入口、方法、架构、决策与技术画像

| 当前位置 / 规则族 | 语义所有者 | 适用范围 | 来源状态 | 生命周期 | 载体 | 适配度 / 重叠 | disposition → 目标责任 | 理由与 downstream impact | 依赖 |
|---|---|---|---|---|---|---|---|---|---|
| `AGENTS.md` | 仓库本地政策 / 规范 | 仓库本地 | 本仓原生 | 启动 + 普通仓库治理 | Root Bootstrap | fit；仅保留薄摘要 / 指针 | keep → 稳定 Repository Governance | 当前职责合理；后续只更新被取代入口，不加入阶段状态 | V3-03、V3-06 |
| `README.md` | Guide | 仓库本地 | 派生投影 | 人类启动 / 恢复 | README | fit；不拥有 Method / Rule 正文 | keep → 人类导航 / 简短状态 | 当前可继续作为稳定导航；避免复制详细 Roadmap | V3-06 |
| `docs/method/ai-development-method.md` | 核心方法 / 原则 | 跨仓库可复用 | 本仓原生 | 普通运行 / 方法变更 | Method document | fit | keep → Core Method | 生命周期、阶段与 Authority 仍由此类 owner 承担 | V3-03、V3-04 |
| `docs/method/principles.md` | 核心方法 / 原则 | 跨仓库可复用 | 本仓原生 | 普通运行 / 条件读取 | Principle document | fit | keep → Core Principle | 证据先于声明等顶层不变量不能被 Guide / Skill 复制成第二 owner | V3-04 |
| `docs/architecture/engineering-capability-architecture.md` | 可复用工程能力 | 跨仓库可复用 | 本仓原生 | 能力设计 / 采用 / 复核 | Architecture document | fit | keep → Engineering Capability Architecture | 负责能力分层、证据准入与生命周期；后续吸收稳定 v3 ownership 关系 | V3-03、V3-04 |
| `docs/architecture/engineering-disciplines.md` | 可复用工程能力 | 跨仓库可复用 | 本仓原生 | 职责按需加载 | Discipline document | fit；与 `execute-unit` 有薄消费重叠风险 | keep → Engineering Discipline owner | 三项纪律无独立任务入口，不应 Skill 化；V3-04 检查 Skill 中是否复制过厚 | V3-04、V3-05 |
| `docs/architecture/technology-profile-contract.md` | 可复用工程能力 | 跨仓库可复用 | 本仓原生 | 技术画像设计 / 采用 | Contract document | fit | keep → Technology / Verification Profile contract | 画像是 reusable defaults，不是 Consumer facts | V3-05 |
| `docs/architecture/skill-architecture.md` | 可复用工程能力（Skill 架构 / 准入） | 跨仓库可复用 | 本仓原生 | Skill 设计 / 准入 / 复核 | Architecture document | fit | keep → Skill architecture | 定义何时可 Skill 化；不拥有具体 Skill procedure | V3-04 |
| `docs/architecture/skill-contracts.md` | 技能 / 过程型能力（契约层） | 跨仓库可复用 | 本仓原生 | Skill 设计 / 实现 / 复核 | Contract document | fit；与 `SKILL.md` 是 contract→implementation 关系 | keep → Skill contracts | 允许契约与实现分层，但不得出现两套冲突 procedure | V3-04 |
| `docs/architecture/first-batch-skill-design.md` | 研究 / 输入 / 证据（历史 Skill 实现设计） | 仅历史 | 历史来源 | 仅历史 / 设计追溯 | Historical design document | mislocated / transitional reference；`skills/README.md` 仍列作“权威设计参考” | supersede → historical design evidence | 当前 9 个 Skill 已有 Architecture、Contracts、SKILL.md；继续称其 current design authority 会制造多 owner | V3-04 |
| `docs/decisions/method-decisions.md` 当前有效决定 | 核心方法 / 原则或可复用工程能力的决策记录 | 跨仓库可复用 | 本仓原生 | 决策追溯 / 按需读取 | Decision log | fit；依靠每项状态区分 current / superseded | keep → 对应 Method / Architecture decision rationale | 不作为普通 runtime 全量 preload；稳定高影响决定可按 ADR Gate 单独提升 | ADR Gate |
| `docs/decisions/method-decisions.md` 已 superseded 决定 | 研究 / 输入 / 证据 | 仅历史 | 历史来源 | 仅历史 / 决策追溯 | Decision log section | fit | keep historical | 显式状态足以避免旧决定继续生效，无需因历史内容存在而拆文件 | 无 |
| `docs/technology-profiles/vue3-typescript.md` | 可复用工程能力 | 跨仓库可复用 | 本仓原生 | 技术命中时按需加载 | Technology / Verification Profile | fit | keep → profile owner | 当前代表性技术画像符合 Profile contract | V3-05 |
| `docs/technology-profiles/README.md` | Guide / 派生 inventory | 跨仓库可复用资源的导航 | 派生投影 | 人类导航 / 采用 | README | fit；不拥有画像正文 | keep → capability inventory | 后续 metadata / discovery 可以改进导航，但不需要先迁移 | V3-05、V3-06 |

### 4.1 `AGENTS.md` 后续只维护指针，不吸收迁移正文

根 Bootstrap 当前包含仓库职责、权威顺序、知识边界、外部操作、AI 复核、语言、研究采用和 Git 提交的薄规则与指针。其职责本身合理。

后续只需要：

- `rule-activation-guide.md` 若在 V3-06 被取代，更新 Consumer 使用入口；
- 外部操作、术语、Git、AI Review 等 owner 重分类后同步稳定指针；
- 保留必要的高层 repository-local invariants，但不把下游规范全文搬回根入口；
- 不把 v3 当前阶段、Issue、PR 或审计结果塞回 `AGENTS.md`。

## 5. 当前 9 个 Skill 与 supporting resources

本轮已重新检查当前 9 个 `SKILL.md` 的 `description`、Purpose、Use / Do Not Use、Authority Sources 和职责边界。它们均具有稳定 trigger、输入、procedure / output / exit 语义，当前 Skill 身份成立。

| 当前位置 | 语义所有者 | 适用范围 | 来源状态 | 生命周期 | 载体 | 适配度 / 重叠 | disposition → 目标责任 | 理由与 downstream impact | 依赖 |
|---|---|---|---|---|---|---|---|---|---|
| `skills/clarify-intent/SKILL.md` | 技能 / 过程型能力 | 跨仓库可复用 | 本仓原生 | 职责按需加载 | `SKILL.md` | fit | keep → clarify-intent procedure | 只处理高影响 Product Intent 歧义；长期领域事实仅识别候选 | V3-04 |
| `skills/specify/SKILL.md` | 技能 / 过程型能力 | 跨仓库可复用 | 本仓原生 | 职责按需加载 | `SKILL.md` | fit | keep → specify procedure | 负责 WHAT / WHY 形成过程；Domain Authority 写入仍服从 Consumer 权限 | V3-04 |
| `skills/technical-plan/SKILL.md` | 技能 / 过程型能力 | 跨仓库可复用 | 本仓原生 | 职责按需加载 | `SKILL.md` | fit | keep → technical-plan procedure | 拥有技术规划 HOW；Architecture / ADR 对象身份由更高 owner 定义 | V3-04 |
| `skills/slice-work/SKILL.md` | 技能 / 过程型能力 | 跨仓库可复用 | 本仓原生 | 职责按需加载 | `SKILL.md` | fit | keep → slice-work procedure | 形成候选 Execution Units，不把任务文件格式提升为方法事实 | V3-04 |
| `skills/readiness-check/SKILL.md` | 技能 / 过程型能力 | 跨仓库可复用 | 本仓原生 | 职责按需加载 | `SKILL.md` | fit；验证规则由其消费 | keep → readiness-check procedure | 只读 Gate 身份清晰；V3-04 检查跨职责验证正文是否重复 | V3-04 |
| `skills/execute-unit/SKILL.md` | 技能 / 过程型能力 | 跨仓库可复用 | 本仓原生 | 职责按需加载 | `SKILL.md` | fit with overlap risk；包含较详细工程纪律薄判断 | keep + overlap review → execute-unit procedure | Skill 需消费纪律，但不能成为 `engineering-disciplines.md` 第二规范正文 | V3-04 |
| `skills/systematic-debug/SKILL.md` | 技能 / 过程型能力 | 跨仓库可复用 | 本仓原生 | 职责按需加载 | `SKILL.md` | fit | keep → systematic-debug procedure | expected behavior 未定义时返回上游，未接管 Requirement | V3-04 |
| `skills/converge/SKILL.md` | 技能 / 过程型能力 | 跨仓库可复用 | 本仓原生 | 职责按需加载 | `SKILL.md` | fit with overlap risk；completion evidence 与验证纪律交叉 | keep + overlap review → converge procedure | 保持 feature-wide convergence owner；验证 rule family 需另有单点 owner | V3-04 |
| `skills/github-actions-verification/SKILL.md` | 技能 / 过程型能力（平台专项） | 跨仓库可复用、条件命中 | 本仓原生 | 职责按需加载 | `SKILL.md` | fit；与外部操作纪律存在通用/平台边界 | keep → GitHub Actions platform procedure | 明确服从 Consumer Policy，不拥有 Merge / Release / Deploy；平台细节继续单点拥有 | V3-04 |
| `skills/github-actions-verification/references/*` | 技能 / 过程型能力 supporting body | 跨仓库可复用、条件命中 | 本仓原生 | Skill 内按需加载 | Skill references | fit | keep → `github-actions-verification` supporting resources | 只要直接服务该 Skill procedure，不单独升级为平级 owner | V3-04、V3-05 |
| `skills/README.md` | Guide / inventory | 跨仓库可复用资源导航 | 派生投影 | 人类导航 / 采用 | README | fit with stale-reference risk | keep；修正 `first-batch-skill-design.md` current-reference 语义 | inventory 不拥有具体 procedure；后续去掉历史设计的“当前权威”暗示 | V3-04 |

当前没有证据支持批量新增、删除或重写 Skill。V3-04 的任务是**处理 overlap 与准入**，不是重新打开第一批核心 Skill 工程。

## 6. `docs/guides/*` 逐规则族审计

### 6.1 `using-agentic-dev.md`

**文件级结论：`mixed` → `split / reduce`，Guide 主身份保留。**

| 当前正文族 | 语义所有者 | 适用范围 | 来源状态 | 生命周期 | 载体 | 适配度 / overlap | disposition → 目标责任 | 理由 / downstream | 依赖 |
|---|---|---|---|---|---|---|---|---|---|
| 使用模型、知识边界、人类理解入口 | Guide | 跨仓库可复用说明 | 本仓原生 | 初始化 / 采用 / 人类阅读 | Guide section | fit | keep → Human/adoption Guide | 与 Guide 边界一致 | V3-03 |
| 外部需求来源如何进入 Consumer Authority | 可复用工程能力（Consumer lifecycle） | 跨仓库可复用 | 本仓原生 | 初始化 / 首次采用 | Guide section | mixed；规范语义只存在 Guide | extract / promote → Consumer lifecycle owner；Guide 留解释 | 否则普通规则依赖人类 Guide | V3-03 |
| 新项目最小 Bootstrap / 不预建空结构 | 可复用工程能力（Consumer initialization） | 跨仓库可复用 | 本仓原生 | 初始化 | Guide section | mixed | extract normative lifecycle；Guide 留例子 / 解释 | 初始化行为需可被 Agent 正确复用 | V3-03 |
| 主导语言的当前值 | 仓库本地政策形成规则 | 仓库本地（采用后） | 从上游 guidance 形成 / 本仓原生 | 初始化 + 普通运行 | Guide section | mixed | Guide 只解释“应本地建立”，真实值由 Consumer Policy owner | 不允许 upstream Guide 持续拥有 Consumer language | V3-03 |
| Skill inventory / responsibility routing 表 | 无独立规范 owner；派生自 Skill / Architecture | 跨仓库导航 | 派生投影 | adoption / routing | Manual table | transitional-current；可能与 Skill `description` 漂移 | reduce / supersede → native Skill discovery + minimal repository discovery | 避免维护第二职责表 | V3-04、V3-06 |
| 验证、工程纪律、外部操作入口 | Guide pointer | 跨仓库说明 | 派生投影 | adoption / 按需导航 | pointer sections | fit if thin | keep as pointers | 不复制规则正文即可 | V3-04、V3-06 |
| baseline adoption / upgrade | 可复用工程能力（Consumer lifecycle） | 跨仓库可复用 | 本仓原生 | 首次采用 / 基线升级 | Guide section | mixed；重要规范语义无独立 owner | extract / promote → Consumer lifecycle | 供 V3-03 建立正式 lifecycle | V3-03 |
| Roadmap lifecycle | 核心方法 / Project Authority lifecycle + repository governance | 跨仓库可复用原则 / 仓库本地实例 | 本仓原生 | 初始化 / 普通项目治理 | Guide section | overlap | move normative semantics to proper owner；Guide pointer-only | 避免 Guide 单点拥有长期 Project Authority 生命周期 | V3-03 |
| Fresh Context recovery | 可复用 discovery/bootstrap architecture | 跨仓库可复用 | 本仓原生 | 普通运行 | Guide section | mislocated | reclassify / pointer-only → discovery owner | ordinary runtime 不应依赖完整人类 Guide | V3-06 |
| agentic-dev experiment / feedback | 仓库本地治理 + 研究 / 证据 lifecycle | 仓库本地 | 本仓原生 | 实验 / 复核 | Guide section | mixed | split / pointer → repository policy + evidence process | 不属于 Consumer ordinary Guide 核心 | V3-03、V3-08 |
| 推荐启动提示与使用目标 | Guide | 跨仓库说明 | 本仓原生 | 初始化 / 人类使用 | Guide section | fit | keep | 低频说明合理 | 无 |

最终目标不是删除 `using-agentic-dev.md`，而是让它真正成为**人类 + 初始化 / 采用 / 升级说明 Guide**，不再承担 ordinary runtime procedure 或规范正文兜底。

### 6.2 `consumer-local-rule-activation.md`

**文件级结论：`mixed / mislocated` → `split + reclassify`，当前先保持 v2 兼容。**

| Section / 规则族 | 语义所有者 | 适用范围 | 来源状态 | 生命周期 | 载体 | 适配度 / overlap | disposition → 目标责任 | 理由 / downstream | 依赖 |
|---|---|---|---|---|---|---|---|---|---|
| §1～3 本地运行目标、薄 Bootstrap、发现对象 | 可复用工程能力（Consumer runtime/discovery） | 跨仓库可复用 | 本仓原生 | adoption + ordinary runtime | Guide sections | mislocated | extract / promote → lifecycle + discovery architecture | 当前是规范性运行语义 | V3-03、V3-06 |
| §4 Activation Manifest / Runtime Catalog | 可复用工程能力的 v2 representation contract | 跨仓库可复用候选 | 本仓原生 | ordinary runtime / transition | Guide section | transitional-current | keep transitional；V3-05/06 决定 promote 或 supersede | 不预设 v3 仍需要相同 Manifest/Catalog | V3-05、V3-06 |
| §5 来源时效性 | 可复用工程能力（discovery） | 跨仓库可复用 | 本仓原生 | ordinary runtime | Guide section | mislocated | reclassify → discovery architecture | fail-closed/currentness 属运行契约 | V3-06 |
| §6 主职责路由 | 可复用工程能力（discovery routing） | 跨仓库可复用 | 本仓原生 | ordinary runtime | Guide section | overlap with Skill discovery | reclassify；禁止形成 Stage Router super layer | 路由应依赖真实 owner，而非手工 Guide 复制 | V3-04、V3-06 |
| §7 routing-only vs Skill execution | Skill/discovery interface | 跨仓库可复用 | 本仓原生 | ordinary runtime / JIT | Guide section | mislocated | reclassify → discovery / Skill interface | 保留 v2 的 progressive disclosure 成果 | V3-04、V3-06 |
| §8 Stage Return | 核心方法 / Skill Contract + discovery consequence | 跨仓库可复用 | 本仓原生 | ordinary runtime | Guide section | duplicate-risk | 删除重复方法正文候选，只保留 discovery-specific re-routing consequence | 防止第二生命周期定义 | V3-04、V3-06 |
| §9 fail-closed | 可复用工程能力（discovery） | 跨仓库可复用 | 本仓原生 | ordinary runtime | Guide section | mislocated | reclassify → discovery architecture | 必须保持 v2 已验证行为 | V3-06 |
| §10～11 baseline state / local projection | 可复用工程能力（Consumer lifecycle） | 跨仓库可复用 | 本仓原生 | adoption / upgrade | Guide sections | mislocated | reclassify → Consumer lifecycle | origin ≠ current authority | V3-03 |
| §12 Runtime Adapter boundary | 可复用工程能力 | 跨仓库可复用 | 本仓原生 | runtime architecture | Guide section | mislocated | promote if retained → Runtime Adapter architecture | 不应由 Guide 定义工程能力身份 | V3-06 |
| §13 adoption acceptance | 可复用工程能力（Consumer lifecycle / adoption verification） | 跨仓库可复用 | 本仓原生 | adoption / verification | Guide section | mixed；验收责任与派生验证清单共置 | extract / promote → Consumer lifecycle / adoption verification；派生 acceptance checklist → V3-08 input | 当前采用完成必须验证；被检查的 runtime 规则继续由各自 owner 持有，验收清单不成为第二规则 owner | V3-03、V3-06、V3-08 |

`§13` 中“采用完成前必须验证”的责任进入 V3-03 Consumer lifecycle；各检查项的运行语义仍由对应 owner 持有，V3-08 只消费派生 acceptance checklist / validation input，不取得这些规则的 current ownership。

在新的 owner 经验证前，本文件继续作为 v2 兼容入口，不能提前删除或失效。

### 6.3 `rule-activation-guide.md`

| 字段 | 审计结论 |
|---|---|
| 当前正文 | “职责 / 风险 → 继续读取来源”的手工导航映射 |
| 语义所有者 | **无独立规范正文所有权**；语义来自被引用的 Method / Architecture / Skill / Policy / Guide |
| 适用范围 | 当前 upstream 使用 / adoption navigation |
| 来源状态 | 派生投影 |
| 生命周期 | transitional current discovery entry |
| 载体 | manually maintained navigation table |
| 适配度 | `transitional-current`；有 source-currentness 风险 |
| overlap | 与 future Resource Index / native Skill discovery 潜在重叠 |
| disposition | `supersede` candidate；若仍需导航，应变成可重建 / 可验证 derived projection |
| target responsibility | V3-06 Discovery Architecture |
| downstream | 替代完成前 README / AGENTS 仍引用它；不能提前删除，也不能与新 current router 长期并存 |
| dependency | V3-06、V3-07、V3-08 |

### 6.4 `verification-evidence-rules.md`

**文件级结论：`mislocated` → 主要 `reclassify` 为可复用验证工程能力；不应继续由 Guide 拥有规范正文。**

| 规则族 | 语义所有者 | 适用范围 | 来源状态 | 生命周期 | 载体 | overlap | disposition → target | downstream | 依赖 |
|---|---|---|---|---|---|---|---|---|---|
| Verification Contract Currentness | 可复用工程能力 / Verification Discipline | 跨仓库可复用 | 本仓原生 | verification / debug | Guide section | tests / workflow authority 规则与 Skills 相交 | reclassify → verification capability | Skills 只消费条件，不复制规则正文 | V3-04、V3-05 |
| Visual Evidence | 可复用工程能力 / conditional Verification Profile | 跨仓库可复用 | 本仓原生 | verification | Guide section | Consumer-specific tolerance 由项目权威决定 | reclassify → verification capability/profile | 保留“功能通过 ≠ 视觉通过”通用边界 | V3-04、V3-05 |
| Human Review Baseline Isolation | 可复用工程能力 / Verification Discipline | 跨仓库可复用 | 本仓原生 | verification/review | Guide section | 平台实现由 Consumer / platform policy 决定 | reclassify | 后续平台 Skill 只负责具体实现 | V3-04、V3-05 |
| Database Migration Completion Evidence | 可复用工程能力 / migration Verification Profile | 跨仓库可复用、条件命中 | 本仓原生 | verification | Guide section | 无独立 Skill 证据 | reclassify；representation 留 V3-05 | 不机械变成新 Skill | V3-05 |
| Evidence Claim Reuse Across Commits | 可复用工程能力 / Verification Discipline | 跨仓库可复用 | 本仓原生 | verification/review | Guide section | Consumer policy 决定是否允许 reuse | reclassify + local policy hook | 保留 ancestor/current claim mapping | V3-04、V3-05 |
| Evidence Type Must Match Claim | 可复用工程能力 / Verification Discipline | 跨仓库可复用 | 本仓原生 | verification | Guide section | 顶层 Evidence-before-claims 由 Principle owner | reclassify；删重复 Principle 正文候选 | 防止两个 normative owner | V3-04、V3-05 |
| Platform Boundary | Guide / capability pointer | 跨仓库导航 | 派生投影 | 按需导航 | pointer | GitHub Actions procedure 已有 Skill owner | keep as pointer in future inventory or capability doc | 不复制平台过程 | V3-04、V3-06 |

当前没有证据要求建立 `verify-evidence` 新 Skill；这些规则缺少统一独立任务入口与稳定独立输出。

### 6.5 `external-operation-guidelines.md`

**文件级结论：`mixed` → 主要 `reclassify` 为可复用外部操作工程能力，局部保留 Repository Policy hook。**

| 规则族 | 语义所有者 | 适用范围 | 来源状态 | 生命周期 | 载体 | overlap | disposition → target | downstream | 依赖 |
|---|---|---|---|---|---|---|---|---|---|
| 读取→判断→写入→重读验证闭环 | 可复用工程能力 / external-operation discipline | 跨仓库可复用 | 本仓原生 | external operation | Guide section | AGENTS 有薄摘要 | reclassify → reusable capability；AGENTS 留 bootstrap invariant | 外部操作不再依赖 Guide owner | V3-04、V3-05 |
| 工具能力 ≠ 授权 | 可复用工程能力 + Repository Policy hook | 跨仓库原则、本地值 | 本仓原生 | ordinary runtime | Guide section | AGENTS / Consumer policy | split：通用判断进入 capability；具体允许动作由 local policy | 不建立统一权限矩阵 | V3-03、V3-04 |
| 多仓库授权分别确认 | 可复用工程能力 | 跨仓库可复用 | 本仓原生 | external operation | Guide section | local policy 提供每仓权限值 | reclassify | 保持跨仓边界 | V3-04 |
| 人工介入边界 | 核心方法原则的操作化 + external capability | 跨仓库可复用 | 本仓原生 | external operation | Guide section | Method Human Escalation | 去重 Method identity，只保留操作领域应用 | 避免外部 Guide 改写顶层人工升级语义 | V3-04 |
| 二进制 / 媒体输入真实性验证 | 可复用工程能力 | 跨仓库可复用、条件命中 | 本仓原生 | execution / verification | Guide section | 无 | reclassify | 作为外部输入处理纪律 | V3-04、V3-05 |
| 异步操作有界观察 | 可复用工程能力 | 跨仓库可复用 | 本仓原生 | execution / verification | Guide section | GitHub Actions Skill 有平台实例 | reclassify；平台过程仍留 Skill | 通用闭环与平台细节解耦 | V3-04 |
| 共享资源 / lease / owner / cleanup | 可复用工程能力 | 跨仓库可复用、条件命中 | 本仓原生 | execution / verification | Guide section | platform policy / Skill | reclassify | Consumer 决定真实资源 / 优先级 | V3-04、V3-05 |
| 临时证据→持久输入晋升 | 可复用工程能力 + Project Authority promotion | 跨仓库可复用 | 本仓原生 | evidence lifecycle | Guide section | Method artifact lifecycle | reclassify；保留 owner promotion hook | 不让 artifact 自动变 Authority | V3-03、V3-04 |
| 依赖 PR / stacked topology | 可复用工程能力 / integration discipline | 跨仓库、平台条件命中 | 本仓原生 | integration planning | Guide section | repository integration policy | reclassify；具体 merge 策略由 local policy | 不把 GitHub topology 变通用 Method 阶段 | V3-04、V3-05 |

当前证据不足以直接把整套 external operation 变成新 Skill。V3-04 应先判断它是否只是多条跨职责纪律，还是存在稳定独立 procedure；V3-02 不提前做该决定。

### 6.6 `git-commit-guidelines.md`

| 字段 | 审计结论 |
|---|---|
| 语义所有者 | 仓库本地政策 / 规范 |
| 适用范围 | 仓库本地 |
| 来源状态 | 本仓原生 |
| 生命周期 | 普通仓库治理 |
| 载体 | 当前位于 Guide 目录的规范性文档 |
| 适配度 | `mislocated` |
| overlap | `AGENTS.md` 只有薄指针，无正文冲突 |
| disposition | `reclassify / move` candidate |
| target responsibility | Repository-local Git Standard；不提前冻结目录 |
| 理由 / downstream | 不同 Consumer 可以合理不同；upstream 可提供模板，但采用后本地值由 Consumer 自己拥有 |
| dependency | V3-03、V3-05、V3-07 |

### 6.7 `terminology-guidelines.md`

| 字段 | 审计结论 |
|---|---|
| 语义所有者 | 仓库本地政策 / 规范 |
| 适用范围 | 仓库本地 |
| 来源状态 | 本仓原生 |
| 生命周期 | 普通仓库治理 |
| 载体 | 当前位于 Guide 目录的术语 / 语言规范 |
| 适配度 | `mislocated` |
| overlap | Method / Architecture 定义概念职责；本文件只应拥有名称身份 / 表达规则 |
| disposition | `reclassify / move` candidate |
| target responsibility | Repository-local Language / Terminology Standard |
| 理由 / downstream | Consumer 主导语言与项目术语可不同；不能由 upstream 持续拥有 Consumer 当前值 |
| dependency | V3-03、V3-05、V3-07 |

## 7. `docs/project/*` 当前、仓库政策、过渡契约与历史边界

### 7.1 当前项目 / 产品权威

| 当前位置 | 语义所有者 | 适用范围 | 来源状态 | 生命周期 | 载体 | 适配度 / overlap | disposition → target | downstream | 依赖 |
|---|---|---|---|---|---|---|---|---|---|
| `project-roadmap.md` | 项目 / 产品权威 | 仓库本地 | 本仓原生 | 普通项目治理 / Fresh Context | Roadmap | fit | keep → Project Roadmap | 继续单点拥有当前阶段、路线、候选和 Gate | 各阶段 |
| `rule-governance-knowledge-activation-v3.md` | 项目 / 产品权威 | 仓库本地 | 本仓原生 | 当前有限里程碑 | Project milestone authority | fit | keep；里程碑完成后 historical | 当前 v3 范围 / Gate，不应进入通用 Method | V3-03～V3-08 |
| `knowledge-capability-ownership-model-v3.md` | 项目 / 产品权威（当前 v3 分类决策） | 仓库本地，目标语义可能跨仓复用 | 本仓原生 | 当前 v3 分析 / 审计 | Project design authority | transitional by design | keep now；最终评估 promote / supersede → Architecture / ADR | 当前是 V3-02 分类权威，但不预判最终长期载体 | V3-03、ADR Gate |

### 7.2 仓库本地政策当前误放在 `docs/project`

| 当前位置 | 语义所有者 | 适用范围 | 来源状态 | 生命周期 | 载体 | 适配度 / overlap | disposition → target | 理由 / downstream | 依赖 |
|---|---|---|---|---|---|---|---|---|---|
| `docs/project/ai-review-guidelines.md` | 仓库本地政策 / 规范 | 仓库本地 | 本仓原生 | 高影响变更复核 | Project-path governance doc | mislocated；AGENTS 有薄摘要 | reclassify / move → Repository-local AI Review Policy | 正文明示只约束 `agentic-dev`，不得自动投射 Consumer | V3-05、V3-07 |
| `docs/project/repository-baseline.md` | 仓库本地政策 / 规范 | 仓库本地 | 本仓原生 | 启动 + 普通仓库治理 | Project-path baseline doc | mislocated；与 AGENTS 的 source-of-truth / authority boundary 有摘要重叠 | reclassify / merge-or-move → Repository Baseline / Governance Standard | 正文定义 GitHub 唯一事实来源、协作模型、授权与工作基线，不是产品 / 项目事实；后续应避免与 AGENTS 双重规范 | V3-05、V3-07 |

`repository-baseline.md` 的发现是 V3-02 的代表性校验：**位于 `docs/project/` 不足以成为项目 / 产品权威。**

### 7.3 v2 仍支撑现行行为的过渡性可复用契约

这些文件物理上属于已完成 v2 项目记录，但部分正文仍支撑当前 Consumer-local discovery / adoption / runtime 语义。它们不能被普通 Fresh Context 当作完整历史过程加载，也不能在没有替代 owner 时直接归档。

| v2 资源 | 语义所有者 | 适用范围 | 来源状态 | 生命周期 | 载体 | 适配度 / overlap | disposition → target | downstream | 依赖 |
|---|---|---|---|---|---|---|---|---|---|
| `consumer-local-activation-metadata-contract-v2.md` | 可复用工程能力（discovery metadata contract） | 跨仓库可复用 | 本仓原生 | adoption + ordinary runtime transition | Completed-project contract | transitional-current | V3-05/06 决定 `promote` 或 `supersede` → resource/discovery contract | 替代前仍保护 v2 currentness / metadata 语义 | V3-05、V3-06 |
| `consumer-local-baseline-adoption-projection-v2.md` | 可复用工程能力（Consumer lifecycle） | 跨仓库可复用 | 本仓原生 | adoption / baseline upgrade | Completed-project design | transitional-current；与 using Guide 重叠 | extract / promote durable lifecycle；原文件 historical | V3-03 不再重新发明 adoption inventory | V3-03 |
| `consumer-local-rule-runtime-target-v2.md` | 可复用工程能力（Consumer runtime architecture） | 跨仓库可复用 | 本仓原生 | ordinary runtime | Completed-project target | transitional-current | extract durable runtime invariants；原文件随后 supersede historical | 保护 local-only / minimum context 等已验证行为 | V3-03、V3-06 |
| `consumer-local-runtime-routing-interface-v2.md` | 可复用工程能力（discovery/routing interface） | 跨仓库可复用 | 本仓原生 | adoption / ordinary runtime | Completed-project interface | transitional-current；与 activation Guide / routing table 重叠 | promote or supersede → Discovery Architecture | V3-06 必须保持 Stage Return / routing-only 等有效语义 | V3-06 |
| `consumer-local-rule-runtime-acceptance-v2.md` | 项目 / 产品权威（v2 acceptance contract） | 仓库本地于 v2 milestone；可复用结论作为输入 | 本仓原生 | validation / historical transition | Project acceptance contract | historical-with-reusable-input | retain evidence；durable reusable constraints 进入真实 owner，作为 V3-08 input | 不让旧 acceptance file 永久成为 runtime owner | V3-08 |

### 7.4 已完成项目记录 / Evidence

以下资源默认只保留历史、证据、决策来源或里程碑追溯职责，不进入 ordinary runtime：

| 资源 / 组 | 语义所有者 | 适用范围 | 来源状态 | 生命周期 | 载体 | 适配度 | disposition | downstream / 依赖 |
|---|---|---|---|---|---|---|---|---|
| `consumer-local-runtime-validation-plan-v2.md` | 研究 / 输入 / 证据 | 仅历史 | 历史来源 | 仅验证 / 历史 | Validation plan | historical | keep historical | V3-08 可参考但不继承为 current contract |
| `consumer-local-runtime-validation-result-v2.md`、`consumer-local-runtime-candidate-drift-review-v2.md` | 研究 / 输入 / 证据 | 仅历史 / 当前评估证据 | 历史来源 / 本仓原生 | Evidence only | Result / review | historical | keep historical | 证明 v2 行为，不定义 v3 runtime |
| `rule-governance-knowledge-activation-v1.md` / `v2.md` | 项目 / 产品权威（历史里程碑记录） | 仅历史 | 历史来源 | 历史 | Milestone docs | historical | keep historical | 不进入普通 Fresh Context |
| `rule-ownership-decomposition-audit-v2.md` | 研究 / 输入 / 证据 | 仅历史 | 历史来源 | historical analysis | Audit doc | historical | keep historical | V3-02 可参考但以 V3-01 分类为准 |
| `engineering-capability-foundation-v1*.md`、`engineering-discipline-expansion-v1*.md` | 项目 / 产品权威（历史里程碑） | 仅历史 | 历史来源 | 历史 | Project docs | historical | keep historical | 长期能力已经提升到 Architecture / Discipline / Profile |
| `engineering-discipline-scope.md` | 项目 / 产品权威（历史范围 / 优先级决策） | 仅历史 | 历史来源 | 历史规划 | Scope baseline | historical | keep historical | 现行纪律正文由 `engineering-disciplines.md` 单点拥有 |
| `chinese-interaction-context-cleanup-v1.md`、`terminology-semantic-safety-v1.md` | 项目 / 产品权威（历史治理里程碑） | 仅历史 | 历史来源 | 历史 | Project docs | historical | keep historical | 现行语言规则由 Repository-local terminology policy 拥有 |
| `stacked-pr-squash-topology-v1.md` | 项目 / 产品权威（历史治理里程碑） | 仅历史 | 历史来源 | 历史 | Project doc | historical | keep historical | durable operation rule family 已进入外部操作 / integration governance；V3-04 再去重 |

## 8. Research、Eval、Task 生命周期

本节继续遵守“目录不是身份”。Research / Eval 目录中的**研究正文、语料、结果与历史证据**不直接拥有现行规范正文；但 README、执行说明、隔离 / 评分规则等 current control body 仍可能属于仓库本地政策、Guide 或其他现行责任，必须分开判断。

### 8.1 `docs/research/README.md`

| 字段 | 审计结论 |
|---|---|
| 语义所有者 | 混合：仓库本地政策 / 规范 + Guide / 派生 inventory |
| 适用范围 | 仓库本地；其中目录清单用于人类 / Agent 导航 |
| 来源状态 | 本仓原生 + 派生投影 |
| 生命周期 | ordinary repository governance + research adoption / promotion + 按需导航 |
| 载体 | Research-area README |
| ownership 适配度 | mixed；目录位置合理，但正文不能整体按 Research Evidence 处理 |
| overlap | `AGENTS.md` 只有“研究不能覆盖 Authority”的薄摘要；长期准入、排除、promotion 与使用规则由本文件当前承担 |
| disposition | `keep`；V3-05 / V3-07 再判断 current policy body 与 derived inventory 是否需要结构化拆分或只保留稳定指针 |
| downstream | 后续资源模型不得把该 README 降格为 evidence；Research 正文的 promotion 仍必须进入真实 owner |
| dependency | V3-03、V3-05、V3-07 |

### 8.2 `docs/research/*` 研究正文（不含 `README.md`）

| 字段 | 审计结论 |
|---|---|
| 语义所有者 | 研究 / 输入 / 证据 |
| 适用范围 | 研究来源决定；对 current repository 默认不直接生效 |
| 来源状态 | 外部输入 / 本仓研究 / 历史来源 |
| 生命周期 | research / evidence only，除非显式 promotion |
| 载体 | Research documents |
| ownership 适配度 | fit |
| overlap | 被 Method / Architecture / Profile 吸收后仍可保留 provenance，但不继续拥有已提升结论 |
| disposition | `keep`；V3-02 不清理研究目录 |
| downstream | 后续候选能力可以引用证据，但不能从 Research 直接覆盖 current authority |
| dependency | 按未来 capability admission 需要 |

### 8.3 `evals/*` 当前控制正文、评估资产与历史证据

| 当前位置 / 规则族 | 语义所有者 | 适用范围 | 来源状态 | 生命周期 | 载体 | 适配度 / overlap | disposition → 目标责任 | downstream | 依赖 |
|---|---|---|---|---|---|---|---|---|---|
| `evals/README.md` 的隔离、污染判定、证据判定与当前 Eval 范围 | 仓库本地政策 / 规范（Evaluation Policy） | 仓库本地 | 本仓原生 | verification / evaluation ordinary governance | Eval-area README sections | mixed；与历史结果 / inventory 共文件 | keep；后续 split / reclassify candidate → Repository-local Evaluation Policy | 不得因为位于 `evals/` 就把当前隔离 / 评分规则降格为 evidence | V3-05、V3-07、V3-08 |
| `evals/README.md` 的历史运行结果与演进记录 | 研究 / 输入 / 证据 | 仅历史 / 当前评估证据 | 历史来源 / 本仓原生 | evidence / historical | Eval-area README sections | mixed | keep historical / evidence | 可以证明既有行为，但不单独定义 Method / Skill / Rule | V3-08 |
| `evals/CODEX.md`、`evals/governance/README.md` 的执行说明 / 使用入口 | Guide + 仓库本地 Evaluation Policy | 仓库本地 | 本仓原生 | evaluation execution / human operation / verification | Guide-like README / CODEX doc | mixed | keep；后续按 semantic body 决定 Guide pointer 与 current policy body 的边界 | 当前 runner、隔离、人工评分规则不能只靠历史 Evidence 反推 | V3-05、V3-07、V3-08 |
| `evals/run_*.py`、schema、fixture、corpus / assertions | 研究 / 输入 / 证据的评估实现 / representation；不新增“Evaluation tooling”平行 semantic owner | 仓库本地评估 | 本仓原生 | evaluation execution / verification | runner / schema / fixture / corpus | fit if subordinate to current evaluation contract；实现不能反向改写被测 Authority | keep | V3-05 只处理表示与发现；V3-08 可复用执行资产，不把实现代码提升为规则正文 | V3-05、V3-08 |
| `evals/results/*` 与冻结的历史 eval 资产 | 研究 / 输入 / 证据 | 仅历史 / 证据 | 历史来源 / 本仓原生 | evidence / historical | result / trace / frozen eval assets | fit | keep；`evals/rule-retrieval/*` 继续冻结为 v1 历史证据 | 旧 live index / runner 不得被 V3-06 误当 current implementation 复活 | V3-06、V3-08 |

### 8.4 `tasks/README.md` 与 `tasks/plans/*`

`tasks/README.md`：

- 语义所有者：仓库本地政策 / 协调规范；
- 适用范围：仓库本地；来源状态：本仓原生；
- 生命周期：复杂工作命中时 ordinary runtime；
- 载体：Task-area README；
- 适配度：fit；
- disposition：`keep`，不为了 taxonomy 机械移动；
- downstream：V3-05 可决定是否需要 metadata，但其规则正文继续由本地 policy owner 管理。

`tasks/plans/*`：

- 语义所有者：研究 / 输入 / 证据中的工作协调记录；
- 适用范围：当前工作；来源状态：本仓原生 / 历史来源；
- 生命周期：活动任务期间协调，结束后 historical；
- 载体：Plan document；
- disposition：`keep historical/coordination`；
- downstream：长期结论必须提升到真实 owner，不能通过 Plan 修改 Method / Architecture / Policy。

## 9. 跨 owner 重叠与后续检查清单

以下问题在 V3-02 中已识别，但当前不直接修改正文：

| 重叠 | 风险 | 当前 disposition 候选 | 后续阶段 |
|---|---|---|---|
| `using-agentic-dev.md` routing 表 vs Skill `description` / `Use When` | 手工路由漂移 | Guide routing reduce / supersede | V3-04、V3-06 |
| `consumer-local-rule-activation.md` Stage Return / routing vs Method / Skill Contract | 第二流程定义 | 只保留 discovery-specific consequence | V3-04、V3-06 |
| `verification-evidence-rules.md` vs Principle / `execute-unit` / `converge` | 证据规则重复 owner | verification capability 单点拥有具体跨职责规则；Principle 保留顶层不变量 | V3-04、V3-05 |
| `engineering-disciplines.md` vs `execute-unit` 长段薄规则 | 薄消费可能演化成复制正文 | semantic diff 后缩回 pointer / minimum execution judgment | V3-04 |
| `external-operation-guidelines.md` vs `github-actions-verification` | 通用操作纪律与平台 procedure 混淆 | reusable discipline vs platform Skill 分层 | V3-04 |
| `repository-baseline.md` vs `AGENTS.md` | source-of-truth / authority 边界双重规范 | 评估 merge / pointer 关系，AGENTS 保持薄 Bootstrap | V3-05、V3-07 |
| `docs/research/README.md` / `evals/{README.md,CODEX.md,governance/README.md}` current control body vs 同目录 Research / Eval evidence | 若按目录统一降格，会丢失当前 research lifecycle / evaluation isolation / scoring policy，并迫使后续重新 inventory | current policy / Guide body 与 evidence / tooling 分开建模；实现与结果不获得规范正文所有权 | V3-05、V3-07、V3-08 |
| `rule-activation-guide.md` vs future discovery mechanism | 多 current router | replacement 后显式 supersede | V3-06、V3-07 |
| v2 `docs/project/*` runtime contracts vs future V3-03/05/06 owners | completed-project 仍隐式 current | 新 owner 建立并验证后显式 supersede | V3-03、V3-05、V3-06 |
| `first-batch-skill-design.md` vs Skill contracts / current `SKILL.md` | 历史设计继续被当 current authority | Skills inventory 去除 current-authority 指向；保留历史 design evidence | V3-04 |

## 10. Disposition 依赖图

V3-02 不直接实施上述 disposition。推荐后续依赖：

```text
V3-02 审计矩阵
    ├─→ V3-03 Consumer lifecycle
    │     ├─ using-agentic-dev adoption / upgrade
    │     ├─ repository-local policy formation
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
    │     ├─ Repository baseline / AI Review representation
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

进入独立复核前必须确认：

- 七个 `docs/guides/*` 已按 semantic body / rule family 审计；
- Method、Architecture、Decision、Technology Profile、9 个 Skill、Project、Research、Eval、Task 的边界均有明确结论；
- `repository-baseline.md` / `ai-review-guidelines.md` 等目录与语义不一致项已被识别；
- v2 过渡性现行契约与纯历史项目记录已经分开；
- 每个主要审计项都记录语义所有者、适用范围、来源状态、生命周期、载体、适配度 / overlap、disposition、目标责任、影响与后续依赖；
- 所有 `move / split / supersede / delete` 都仍只是候选，没有发生物理迁移；
- V3-03～V3-06 可以直接使用本矩阵，而不需要再次做同义 inventory；
- 独立复核对高风险 ownership ambiguity 的 Blocking / Medium 为 0。

如果独立复核发现“某个当前规范正文没有明确 owner”“同一规则被两个 owner 同时声明 current”“历史资源仍被普通运行误认为 current”或“项目路径被错误等同于项目 / 产品权威”等问题，应先修订本审计矩阵，再进入后序阶段。
