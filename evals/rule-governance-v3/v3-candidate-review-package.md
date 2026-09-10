---
id: eval-rule-governance-v3-candidate-review-package
title: 规则治理与知识激活 v3 候选评审包
type: evaluation-candidate
status: review-only
version: "V0.1"
classification:
  - rule-governance
  - knowledge-activation
  - repository-local-runtime
relations:
  upstream:
    - AGENTS.md
    - docs/project/rule-governance-knowledge-activation-v2.md
    - docs/project/consumer-local-activation-metadata-contract-v2.md
    - docs/project/rule-ownership-decomposition-audit-v2.md
    - docs/guides/rule-activation-guide.md
    - docs/guides/using-agentic-dev.md
    - docs/guides/consumer-local-rule-activation.md
  related:
    - evals/rule-governance-v3/gpt6-review-prompt.md
    - evals/rule-governance-v3/review-output-schema.json
---

# 规则治理与知识激活 v3 候选评审包

## 1. 文档性质

本文是临时评估分支上的 **v3 Candidate Design**，只用于独立模型评审，不是 `agentic-dev` 正式 Method、Architecture、Guide、Skill 或 Project Authority。

评审基线：

`agentic-dev@3c31ae96683c4a653f001402b889b40e87df976b`

本方案只有在评审结果返回、Blocking / Medium finding 被人工裁决并正式建立新的 Milestone / Authority 后，才可能进入实现。

本候选吸收一个历史 `jilinjobs` 需求分析规范中的 AI-ready Structured Markdown 经验作为外部设计输入：YAML Front Matter 只用于定位和路由，正文是业务 / 规范事实的唯一承载位置；Agent 先用 `type / classification / relations` 找到最小权威上下文，再读取正文。该外部规范本身不构成 `agentic-dev` Authority。

## 2. 为什么需要 v3

v2 已经证明以下长期方向有效：

- Thin Bootstrap；
- Consumer Repository Authority first；
- Progressive Disclosure；
- derived discovery 不拥有规则正文；
- source stale / missing / ambiguity 时 fail-closed；
- primary responsibility 与 supporting context 分离；
- routing-only 与 JIT Skill execution 分离；
- Consumer baseline adoption 使用逐项 `adopt / retain-or-override / reject-not-applicable / supersede-remove`；
- ordinary Consumer runtime 可以在完成 adoption 后完全 local-only；
- v1 JSON rule-index runnable surface 已被 v2 supersede，不再作为 Current Discovery Mechanism。

但 v2 仍存在四个结构性不足。

### 2.1 Activation metadata 与 semantic owner 双点维护

v2 的长期逻辑模型允许：

```text
semantic owner
+ manually maintained Activation Manifest
→ optional Runtime Catalog
```

Manifest 中的 `responsibility / conditions / risks / activation_role` 实际来自 semantic owner 的语义提炼。即使 source identity 能发现 stale，也仍要求维护者在修改 owner 后再次更新独立 Manifest。

这解决了“陈旧不能静默继续使用”，但没有解决“为什么需要维护第二份 activation semantics”。

### 2.2 `using-agentic-dev.md` 仍未完成真正的 semantic decomposition

v2 ownership audit 已明确判断 `using-agentic-dev.md` 同时承载：

1. Consumer bootstrap / adoption；
2. Skill 使用与职责路由；
3. 跨职责 verification / engineering coordination；
4. 解释性使用说明。

v2 已删除大量重复 Skill-owned procedure，并把验证规则迁到 `verification-evidence-rules.md`，但当前 `using-agentic-dev.md` 仍同时包含：

- 使用模型；
- 知识边界；
- requirement source adoption；
- 新项目初始化；
- 主导语言；
- 长期结构建立；
- Skill 使用；
- responsibility routing；
- baseline adoption；
- Roadmap lifecycle；
- Fresh Context recovery；
- experiment / feedback。

因此它仍是一份多责任、较大的运行时 Guide，而不是纯 landing / routing entry。

### 2.3 `rule-activation-guide.md` 仍是人工维护的导航索引

当前 `rule-activation-guide.md` 以人工表格维护：

```text
current responsibility / risk
→ exact Guide / Skill / section pointer
```

这实际上是一份手工 Runtime Index。Guide / Skill 结构变化时仍需要人工同步这些 pointer。

### 2.4 `agentic-dev` 自身尚未 self-host v2 discovery

当前 `agentic-dev` Fresh Context 仍主要依赖：

```text
AGENTS.md
→ README.md
→ Project Roadmap
→ Agent 自行判断需要打开哪个 Guide / Skill / Method
```

v2 的完整结构化 discovery 只在 Consumer 场景完成真实验证，`agentic-dev` 自身尚未通过同一模型发现和激活自己的规则。

## 3. v3 核心目标

建议 v3 名称：

> **规则治理与知识激活 v3 — Repository-local Structured Discovery & Self-Adoption**

v3 把 v2 的 Consumer-local 模型提升为 Repository-local 通用模型：

```text
Repository Task
→ Thin Bootstrap
→ Repository Activation Index
→ YAML Front Matter metadata
→ minimum applicable semantic owners
→ Primary Responsibility
→ routing-only OR JIT Skill
→ Execute / Verify / Stage Return
```

该模型同时适用于：

- `agentic-dev` 自身；
- 已采用 `agentic-dev` 的 Consumer。

Consumer 比 `agentic-dev` 多出的只是 upstream adoption / provenance lifecycle，而不是另一套 discovery architecture。

## 4. 核心架构原则

### 4.1 Front Matter 是 source-local Agent metadata

对于会被 Agent 长期、反复发现和消费的权威 / reusable resource，activation metadata 应尽量与 semantic owner 共址：

```text
Authoritative Resource
┌────────────────────────────┐
│ YAML Front Matter          │  Agent routing metadata
├────────────────────────────┤
│ Structured Markdown Body   │  normative semantics
└────────────────────────────┘
```

三条硬边界：

1. Front Matter 只回答“它是什么、何时可能需要读、与谁有关”；
2. Body 才能定义真实规则 / Requirement / Architecture / Skill procedure；
3. Agent 不得仅依据 Front Matter 执行正文规则。

### 4.2 Generated Activation Index 是唯一 Current Discovery Projection

建议 Current Runtime 采用：

```text
Authoritative / reusable resources + Front Matter
→ deterministic generator
→ Repository Activation Index
→ Agent discovery
```

Index 必须满足：

- generated；
- derived；
- non-authoritative；
- 可删除 / 可重建；
- 记录 source identity；
- 不保存规范性正文；
- 不人工维护 activation semantics；
- stale / invalid 时 fail-closed；
- 同一个 Runtime scope 内是唯一 Current Discovery Mechanism。

v3 如果正式采用该模型，应明确 supersede：

- v2 以人工维护 Activation Manifest 为默认 authoring source 的做法；
- `rule-activation-guide.md` 作为人工 Runtime mapping table 的职责。

### 4.3 一个独立 activation unit 尽量对应一个独立 semantic owner 文件

如果同一文件内存在多个拥有不同 `responsibility / conditions / lifecycle` 的长期规则族，一个文件级 Front Matter 很难准确激活。

因此：

> 只有当规则族具有独立长期 owner 与独立 activation semantics 时，才拆成独立文件；不得按 heading 数量机械拆分。

这也是 v3 需要真正拆分 `using-agentic-dev.md` 的原因。

## 5. 哪些资源需要统一 Front Matter

v3 不要求“所有 Markdown 统一模板”。应区分 **长期 Agent-consumed authoritative / reusable resource** 与普通输入 / 历史材料。

### 5.1 原则上必须

- Requirement Authority；
- Requirement Aspect；
- Specification；
- Architecture Authority；
- ADR；
- Method / Principle；
- reusable Guide Rule Module；
- Skill；
- Engineering Discipline；
- Verification Strategy / reusable verification rule。

### 5.2 原则上应有，但允许按 Repository 复杂度裁决

- durable Execution Unit / Work Authority；
- Project Roadmap；
- Domain Authority；
- Technology / Verification Profile。

### 5.3 默认不要求

- 原始需求输入；
- 外部政策 / 标准原文；
- Research 原始报告；
- 一次性分析；
- 临时 Task notes；
- 历史 Evidence；
- 普通 README；
- 纯解释性材料。

Root `AGENTS.md` 是稳定 Bootstrap 特殊入口，可以继续作为预先约定入口，而不要求通过 Index 才能发现。

## 6. 统一逻辑 Metadata Contract

v3 建议继承已验证的简单资源元数据风格，而不是发明复杂 ontology。

逻辑模型：

```yaml
id: stable-resource-id
title: human-readable-title
type: requirement | specification | architecture | adr | method | principle | guide | skill | discipline | verification | work | roadmap | profile
status: active | draft | superseded | archived
version: optional-human-version
classification:
  - stable-topic
activation:
  role:
    - bootstrap | routing | constraint | execution
  responsibility:
    - stable-responsibility
  scopes:
    - stable-scope
  conditions:
    - only-when-materially-useful
  risks:
    - only-when-materially-useful
relations:
  upstream:
    - stable-resource-id-or-path
  related:
    - stable-resource-id-or-path
  overrides:
    - stable-resource-id
  supersedes:
    - stable-resource-id
  stage_return:
    - stable-responsibility-or-resource
provenance:
  origin: consumer-native | adopted
  repository: optional-upstream-repository
  baseline: optional-exact-upstream-sha
  source: optional-upstream-source
```

不是所有字段都必须出现。只有真实改变 discovery candidate set 的 metadata 才应该持久化。

## 7. Serialization Profiles

统一的是**逻辑 metadata contract**，不是要求所有工具消费完全相同的 YAML 顶层键。

### 7.1 Generic authoritative Markdown profile

普通权威 Markdown 可以直接使用：

```yaml
---
id: architecture-public-renderer
title: Public Renderer Architecture
type: architecture
status: active
classification:
  - public-renderer
activation:
  role:
    - routing
    - constraint
  responsibility:
    - technical-plan
    - readiness-check
relations:
  upstream:
    - spec-public-renderer
---
```

正文保持完整 Architecture semantics。

### 7.2 Codex `SKILL.md` compatibility profile

当前 Codex Skill Runtime 对 `SKILL.md` 有自己的 Front Matter contract。`name` / `description` 是自动 Skill selection 读取的核心字段；当前官方 validator 允许的额外顶层字段有限，因此 v3 **不得**为了统一 schema 破坏原生 Skill 格式。

推荐：

```yaml
---
name: technical-plan
description: <Codex 原生 Skill activation description>
metadata:
  agentic-dev:
    id: skill-technical-plan
    type: skill
    status: active
    classification:
      - architecture
      - development-method
    activation:
      role:
        - routing
        - execution
      responsibility:
        - technical-plan
      scopes:
        - architecture
        - technical-planning
      conditions:
        - durable-cross-unit-how
        - shared-contract-change
    relations:
      upstream:
        - method-ai-development
---
```

这里要保持两个独立事实：

- Codex 原生 `name / description` 继续决定平台自身 Skill candidate selection；
- `metadata.agentic-dev` 只用于 Repository-local generated index，不替代 Codex Runtime 自身的 Skill metadata contract。

评审必须重点检查：这是否会形成“两套互相漂移的 Skill activation metadata”，以及是否需要进一步收敛到更薄的映射。

## 8. Source identity 与 stale 模型

### 8.1 Front Matter 不保存自己的 hash

禁止在 source 自己的 Front Matter 中写入自身 `source_identity`，避免自引用 hash。

### 8.2 Index 保存 Current source identity

生成器读取 source 后投射：

```yaml
- id: skill-technical-plan
  path: skills/technical-plan/SKILL.md
  source_identity:
    algorithm: git-blob-sha1
    value: <current-blob-sha>
  projected_activation: ...
```

### 8.3 重新定义 stale

因为 v3 的 activation semantics 与 source 共址，普通 source 修改后重新生成 Index 不再需要“人工先同步 Manifest”的双点维护。

但以下变更仍应阻止自动信任：

- `id / type / status` 非法；
- relations dangling / cyclic where forbidden；
- duplicate active owner identity；
- `supersedes / overrides` 矛盾；
- generator 无法解析 Front Matter；
- Current Index source identity 与仓库当前资源不一致；
- resource 被删除而 Index 仍声明 active。

对于影响高风险 routing contract 的 metadata 语义变更，是否要求额外 Human / AI Review，应由 v3 governance 明确定义，而不是重新建立一份手工 Manifest。

## 9. Activation Index 最小职责

建议 Index 只保存：

- resource id；
- local path；
- type / status；
- classification；
- activation role；
- responsibility；
- scopes；
- conditions / risks；
- relations；
- provenance 中 ordinary runtime 真正需要的最小部分；
- source identity。

禁止保存：

- Requirement / Architecture 摘要；
- Guide 规则摘要；
- Skill procedure；
- expected answer；
- Issue / PR / Run current state；
- recommendation；
- copied checklists。

Index 回答的是：

> 当前任务最应该继续读取哪些 Current semantic owners？

而不是：

> 当前规则正文是什么？

## 10. Index Generator / Validator

v3 应提供一个确定性、小型、Repository-local 工具，只承担 projection / validation，不承担 Method routing reasoning。

至少检查：

- YAML parse；
- duplicate id；
- required field profile；
- unsupported status；
- dangling relation；
- duplicate / contradictory active owner；
- source path existence；
- source identity freshness；
- generated Index 与 Current resources 一致；
- superseded resource 不进入 active routing set；
- optional policy: changed Front Matter that materially alters high-impact activation must have appropriate review evidence。

工具不得：

- 私下定义新的 Method Stage；
- 根据关键词自己决定 primary responsibility；
- 读取 upstream latest 改变 local runtime；
-复制正文；
-成为新的规则 Authority。

## 11. `using-agentic-dev.md` 物理拆分候选

v3 应把 `using-agentic-dev.md` 收敛成短 human landing page / scenario router，而不是继续作为多责任 Runtime Guide。

候选 owner 边界：

```text
docs/guides/
├── using-agentic-dev.md
│   └── landing page / 使用场景导航
├── consumer-bootstrap.md
│   └── Knowledge Boundary / 最小 Consumer Authority / 新项目启动
├── requirement-source-adoption.md
│   └── 外部需求来源进入 Consumer Authority
├── baseline-adoption.md
│   └── adopt / retain / override / reject / supersede
├── consumer-local-rule-activation.md
│   └── adopted capabilities 的 Consumer-local runtime 特殊规则
├── project-evolution-and-recovery.md
│   └── Roadmap lifecycle / Fresh Context recovery
├── agentic-dev-experiment-guidelines.md
│   └── Consumer experiment / upstream feedback
├── verification-evidence-rules.md
└── external-operation-guidelines.md
```

这只是 semantic decomposition candidate，不冻结最终文件名。

拆分准入：

> 一个规则族只有在具有独立长期语义 owner、独立 activation conditions / responsibility、且单独发现能降低误读或上下文成本时才独立成文件。

不得为了 Front Matter 一文件化而把每个 heading 机械拆成文件。

## 12. `rule-activation-guide.md` 的 v3 归位

当前手工 mapping table 不应继续承担 Current Runtime Index 职责。

v3 候选方向：

- Runtime mapping：由 Generated Activation Index 取代；
- human explanation：如果仍有价值，保留一个非常短的“如何理解 activation index”说明；
- 精确 responsibility / source mapping 不再由人工表格维护。

## 13. `agentic-dev` Self-Adoption

v3 必须让 `agentic-dev` 本身成为第一等使用方，而不是只让 Consumer 验证。

目标 Fresh Context：

```text
AGENTS.md
→ generated activation index
→ current project-routing resources
→ minimum Method / Guide / Skill / Discipline
→ routing-only OR JIT execution
```

self-adoption 必须覆盖真实场景，例如：

1. 下一 Roadmap Planning；
2. Requirement / Specification 语义问题；
3. durable architecture decision；
4. Ready Unit execution；
5. unexpected runtime failure；
6. GitHub Actions verification；
7. external operation；
8. convergence / evidence claim；
9. Fresh Context recovery。

至少验证：

- 正确 primary responsibility；
- 必需 supporting owner 不遗漏；
- 不加载明显无关 Guide / Skill；
- routing-only 不预加载完整 Skill；
- actual execution JIT Skill；
- Stage Return 后重新 discovery；
- stale / missing index fail-closed；
- Index 删除后能确定性重建；
- `AGENTS.md` 不重新膨胀。

## 14. Consumer v3 Projection

Consumer 不再以“复制 upstream Guide + 手写 Manifest”为默认 adoption 模型。

建议：

```text
upstream reusable capability
→ classify
→ adopt / retain-or-override / reject / supersede
→ establish/update Consumer-local semantic owner
→ persist local Front Matter + provenance
→ regenerate Consumer Activation Index
→ validate local-only runtime
```

仍然保持 v2 的重要区分：

- last evaluated upstream baseline；
- each active adopted asset `adopted_from`；
- upgrade-only decision history。

rejected decision 与 upstream project-only state 不进入 ordinary Runtime Index。

## 15. v1 / v2 成果保留要求

v3 不得回退以下成果：

### v1

- minimal correct rule set；
- derived discovery 不成为 Authority；
- source currentness；
- stale / missing / no-match fail-closed；
- effectiveness 由行为证据判断，不由工具可运行性判断。

### v2

- Thin Bootstrap；
- Consumer Authority first；
- semantic owner 单点正文；
- primary responsibility / supporting context；
- routing-only / Skill execution 分离；
- Stage Return 后重新 routing；
- Consumer local-only ordinary runtime；
- explicit baseline adoption lifecycle；
- adopted provenance 与 evaluated baseline 分离；
- superseded / rejected 不进入 active discovery；
- 一个 Runtime scope 只有一个 Current Discovery Mechanism。

## 16. 候选实施阶段

### Phase A — AI-ready Resource Metadata Contract

冻结：

- resource classes；
- Front Matter applicability；
- logical metadata contract；
- Generic Markdown / SKILL.md compatibility profile；
- Body / metadata Authority boundary。

### Phase B — Semantic Owner & Physical Decomposition

- 审计所有 current Method / Guide / Skill / Discipline；
- 真正拆分 `using-agentic-dev.md`；
- 识别其他“一文件多 activation owner”问题；
- 不按目录 / heading 机械拆分。

### Phase C — Generated Activation Index

- Index schema；
- generator / validator；
- source identity；
- relations validation；
- stale / fail-closed；
- supersede manual Runtime mapping。

### Phase D — `agentic-dev` Self-Adoption

- 给自身 Authority / Guide / Skill / Discipline 添加符合准入条件的 Front Matter；
- 生成唯一 Current Index；
- 用真实 Fresh Context 验证。

### Phase E — Consumer Projection v3

- 从 manual Manifest authoring 迁移为 source-local Front Matter + generated Index；
- 保持 v2 adoption lifecycle；
- 不要求原始 / research / history 全仓结构化。

### Phase F — Dual Runtime Validation

必须同时覆盖：

- `agentic-dev` self-runtime；
- 至少一个真实 Consumer runtime。

### Phase G — Convergence / Regression

- v1 / v2 preservation；
- current discovery uniqueness；
- Front Matter / Index currentness；
- Guide decomposition；
- context / token / file-read efficiency；
- Final AI Review；
- Human integration decision。

## 17. 明确非目标

v3 当前候选不预设：

- 向量数据库；
- 图数据库；
- MCP Rule Service；
- 全仓所有 Markdown 强制统一模板；
- 把 Front Matter 变成规范性事实正文；
- 让生成器做 LLM routing reasoning；
- 建立 Rule Super Skill / Stage Router Skill；
- 固定全局 condition / risk taxonomy；
- 将 Consumer upstream adoption 移回 ordinary runtime；
- 因为 self-adoption 就让 `agentic-dev/docs/project/*` 自动成为 Consumer Authority。

## 18. 评审必须挑战的问题

GPT-6 独立评审不得只判断“方案看起来合理”，必须重点挑战：

1. Front Matter + Generated Index 是否真的消除了双点维护，还是把重复转移到别处？
2. `SKILL.md` 的 Codex-native `name / description` 与 `metadata.agentic-dev.activation` 是否形成两套会漂移的 activation semantics？最小修正是什么？
3. 哪些 resource class 强制 Front Matter 的边界是否过宽 / 过窄？
4. 一文件一个 activation owner 是否会导致过度拆分？是否需要允许稳定 section-level activation unit？
5. Index generator / validator 是否真的能防止 v1 stale-index 类问题？
6. source identity 与 review lifecycle 是否充分，还是重新生成 Index 会让高风险 metadata 变化被静默接受？
7. `using-agentic-dev.md` 拆分是否有遗漏 / 重叠 owner？
8. `rule-activation-guide.md` 被 Index 取代后，人类和 Fresh Context 是否仍有足够入口？
9. `agentic-dev` self-hosting 与 Consumer adoption 是否真的共享一个 core model，还是只是表面统一？
10. v1 / v2 的哪些行为可能被 v3 破坏？
11. 是否存在明显更简单、长期维护成本更低、又能达到同样目标的方案？
12. 这个候选是否已经过度设计，哪些部分应该延后到证据出现后？

## 19. 候选完成定义

v3 只有在未来正式 Milestone 中满足以下条件才能视为完成：

- Agent 持续消费的权威 / reusable resources 具有一致、工具兼容的 Front Matter contract；
- Front Matter 只承担 discovery semantics，正文保持唯一 normative owner；
- Runtime Index 从 source metadata 确定性生成，不再人工维护第二份 activation semantics；
- Index stale / invalid 能 fail-closed，删除后可重建；
- `using-agentic-dev.md` 完成真正的 semantic decomposition；
- `rule-activation-guide.md` 不再人工维护 Current Runtime mapping；
- `agentic-dev` 自己通过同一 Repository-local discovery model 工作；
- Consumer 使用同一 core model，同时保留 upstream adoption / provenance 特殊生命周期；
- v1 / v2 所有长期有效行为不回退；
- self-runtime 与真实 Consumer runtime 均有 Fresh Context Evidence；
- 无未解决 Blocking / Medium finding；
- 再进入人工集成决策。
