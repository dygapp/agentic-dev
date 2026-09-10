# Consumer-local 激活元数据契约 v2

## 状态

**Phase C 结果 — Minimal Metadata / Catalog Contract**

上层输入：

- `docs/project/consumer-local-rule-runtime-target-v2.md`
- `docs/project/consumer-local-rule-runtime-acceptance-v2.md`
- `docs/project/rule-ownership-decomposition-audit-v2.md`

本文冻结 v2 的**逻辑 metadata / Catalog 契约与生命周期**。它不要求所有 Consumer 使用固定目录，也不把当前示例序列化格式提升为核心方法要求。

## 1. 设计目标

Consumer-local discovery 需要同时满足：

1. ordinary runtime 只依赖 Consumer-local 资产；
2. metadata 足以找到最小 semantic owner；
3. Consumer-native Authority 与 adopted reusable capability 可进入同一发现入口；
4. metadata 不复制规则正文；
5. source 变化后旧 discovery 不被静默继续使用；
6. rejected / superseded rule 不参与 Current routing；
7. Catalog 可以删除 / 重建，不损失任何规范性事实；
8. Consumer 不需要把全部文档改造成统一模板或 Front Matter。

## 2. 两层发现模型

### 2.1 Activation Manifest

**Activation Manifest** 是 Consumer-local、版本化的发现元数据集合。

它保存：

- local discovery identity；
- semantic owner 的本地 source pointer；
- 最小 activation dimensions；
- adopted reusable capability 的 provenance；
- current / superseded 等发现生命周期；
- source identity policy。

它不保存：

- 规则完整正文；
- Requirement / Architecture 内容摘要；
- Skill procedure；
- 当前执行状态副本；
- upstream Project Roadmap / Issue / PR 状态。

Manifest 是**维护输入**，但不是规范性规则 Authority。删除 Manifest 会损失快速发现能力，但不会损失任何规范性项目事实；可以从当前 semantic owners、Consumer adoption 状态与 Repository Authority 重新审计建立。

### 2.2 Runtime Catalog

**Runtime Catalog** 是 Manifest 与当前 Consumer-local source identities 的可删除运行时投影。

它的目标是让 Fresh Context 只需先读取一个很小的本地入口即可完成候选选择。

Catalog 可以：

- 直接采用 Manifest 的 compact projection；
- 或由一个确定性本地工具生成。

无论具体实现为何，都必须满足：

- 不含规范性规则正文；
- 记录 Manifest identity / source identity；
- source stale 时不能继续声称当前规则集合完整；
- 删除后可以从 Manifest 重建；
- Runtime 不需要访问 upstream 才能验证 Catalog 当前性。

对于很小的 Consumer，可以直接读取 Manifest 而不生成第二个 Catalog 文件；“两层”是职责模型，不要求物理上一定存在两个文件。

## 3. 最小逻辑 Record

一个 active activation record 最多由以下字段族组成。

### 3.1 必需字段

#### `id`

Consumer-local 稳定发现 identity。

要求：

- 在当前 Consumer discovery scope 内唯一；
- 不要求与 upstream id 相同；
- semantic owner 被替换时，按真实 identity 决定保留或 supersede，不能只凭名称自动复用。

#### `kind`

用于判断加载方式，而不是定义 Authority 优先级。

最小枚举：

```text
authority
rule-module
skill
engineering-discipline
platform-skill
```

不为每个具体文档类型增加 schema enum。

#### `source`

必须指向 Consumer-local 可读取对象。

逻辑内容：

```text
path
optional selector
```

`selector` 用于当前 semantic owner 仍位于较大文件中的情况，例如稳定 heading / section identity；不使用易漂移的行号作为唯一 selector。

#### `activation_role`

最小枚举：

```text
bootstrap
routing
constraint
execution
```

语义：

- `bootstrap`：Fresh Context / Consumer Authority / discovery entry；
- `routing`：帮助判断 responsibility / Stage Return；
- `constraint`：对一个或多个职责施加条件性约束；
- `execution`：只有真正进入该职责时才加载完整 owner，例如 Skill。

该字段避免“发现了 Skill 就机械加载 Skill”。

#### `scope`

至少一个逻辑作用域，用于排除明显无关对象。

v2 不规定全球统一完整词表。Consumer 可以在保留稳定 method responsibility identity 的同时使用自己的 domain / subsystem scope。

### 3.2 条件字段

只有会改变候选集合时才填写。

#### `responsibility`

一个或多个稳定职责 identity，例如：

```text
clarify-intent
specify
technical-plan
slice-work
readiness-check
execute-unit
systematic-debug
converge
```

跨职责规则可以列出多个消费者，或在只依赖 condition/risk 时省略。

#### `conditions`

只有触发条件成立时才激活的稳定条件标签。

例如：

```text
external-requirement-source
baseline-upgrade
visual-fidelity
observed-unexpected-failure
database-migration
shared-external-resource
```

条件标签只用于发现，不代替 owner 中的完整判断规则。

#### `risks`

只有风险维度会改变所需规则时使用，例如：

```text
major-architecture
irreversible
security-privacy
authority-conflict
external-side-effect
```

不得为了“更智能”预先建立大而全的风险 taxonomy。

### 3.3 生命周期 / provenance 字段

#### `origin`

最小区分：

```text
consumer
adopted
```

`consumer` 表示 Consumer-native owner。

`adopted` 需要保留最少 provenance：

```text
upstream repository
exact baseline
upstream source identity/path
```

这些信息只用于来源追溯与 future baseline comparison，不要求 ordinary runtime 打开 upstream。

#### `state`

最小枚举：

```text
active
superseded
disabled
```

普通 Runtime Catalog 只投射 `active`。

`reject / not applicable` 属于 adoption decision history，不需要制造 active/discoverable runtime record。

#### `relations`

只在需要时使用：

```text
overrides
supersedes
```

- `overrides`：Consumer-specific current owner 覆盖一个更通用 adopted default；
- `supersedes`：当前 owner 取代旧 current owner。

关系帮助选择与审计，不改变 Consumer Repository Authority hierarchy。

## 4. Source binding：两种模式

一个统一的整文件 hash 策略会给高频变化的 Consumer Roadmap / Current Authority 带来不必要维护成本；完全不检查 source identity 又会让语义 metadata 变陈旧。

因此定义两种最小 source binding。

### 4.1 `semantic-reviewed`

适用：metadata 的 `responsibility / conditions / risks` 是从 source 规则语义中提炼出来的对象，例如 reusable Guide rule module、Skill、Engineering Discipline。

要求：

- Manifest 记录 `reviewed_source_identity`；
- identity 应绑定 source selector 对应的实际内容，而不是无关整仓库状态；
- source / selected content identity 改变时，旧 record 立即视为 stale；
- 不允许生成器仅重算 hash 就自动恢复 `active`；
- 必须先复核 source 变化是否影响 activation metadata，再更新 reviewed identity。

这继承 v1 的保守 stale-source 原则。

### 4.2 `current-locator`

适用：metadata 只负责定位一个 Consumer-native Current Authority seam，而**没有复制该 Authority 的当前规则摘要**，例如：

- Documentation Authority Map；
- Current Project Roadmap；
- Current Requirement index；
- Architecture index；
- Verification Strategy entry。

要求：

- Runtime 始终读取该 local source 的当前内容；
- metadata 不缓存其中的 Current Gate、业务值、状态、架构决定或验收正文；
- 至少验证 source 存在、仍由 Consumer Repository Authority 声明为当前入口；
- source path / authority role 被取代时，必须同步更新 Manifest；
- 不因文件正文的正常状态更新而让 locator 自动失效。

`current-locator` 不能用于把详细规则摘要藏进 metadata；一旦 metadata 自身开始表达源规则的适用语义，应切回 `semantic-reviewed`。

## 5. Catalog 中明确禁止的内容

Runtime Catalog 不应包含：

- `required_checks` 的完整列表；
- 规则正文摘要段落；
- Technical Plan / Requirement / Architecture 内容摘要；
- Skill Procedure；
- 当前 Issue / PR / Actions 状态副本；
- “推荐解决方案”；
- 根据历史模型结果写死的 expected answer。

允许一个极短的非规范性 label / title 供人理解，但它不能成为 Agent 在不读 source 的情况下执行规则的依据。

这比 v1 评估索引进一步收窄：v1 的 `activation_summary` / `required_checks` 对评估很有用，但 Consumer ordinary runtime 的当前证据表明，更安全的正式长期设计是让 Catalog 只负责发现，让 Agent 读取 local semantic owner 后再执行。

## 6. 查询 / 选择契约

Runtime discovery 继续采用稀疏模型：

```text
Consumer scope
+ current responsibility candidate
+ only-known conditions / risks
```

### 6.1 不要求用户填写表单

这些维度可以由 Agent 从：

- 当前任务；
- Thin Bootstrap；
- Consumer Current Authority；
- 当前运行状态；

中解析。

未知值不得猜测。

### 6.2 不使用固定 Top-K

目标仍是最小正确集合：

> 不遗漏当前必需 owner，同时不加载明显无关 owner。

固定 Top-K 不能代替完整召回已知适用的必需规则。

### 6.3 primary 与 supporting

发现结果应区分：

- **primary responsibility**：当前真正需要进入 / 返回的职责；
- **supporting constraints / routing context**：帮助正确判断或约束 primary 的规则。

多个 supporting records 可以同时成立，但不能因此把多个 execution Skill 全部加载。

### 6.4 Skill activation

`kind=skill/platform-skill` 且 `activation_role=execution` 时：

- 只做 routing / Stage Return：只需识别 owner；
- 真正进入该职责：加载 Skill；
- supporting responsibility 不自动加载完整 Skill；
- 当前任务切换 responsibility 后重新解析，不把第一次 Skill 集合作为整段会话永久上下文。

## 7. Consumer Authority precedence

Catalog 不拥有独立 priority 系统来覆盖 Repository Authority。

如果多个记录同时命中：

1. 先遵守 Consumer 自己声明的 Repository Authority hierarchy；
2. Consumer-native specific rule 可以合法 override 更通用 adopted default；
3. `overrides` 只帮助发现这种关系，不创造覆盖权；
4. adopted Skill / reusable rule 永远不能改写 Consumer Requirement / Specification / Architecture fact；
5. 无法确认 current local override 身份时 fail-closed 到 Consumer Authority。

不引入一个全局 `priority: 100` 之类的分数来替代 Authority 语义。

## 8. Stale / missing / ambiguity fail-closed

### 8.1 semantic-reviewed stale

```text
current selected source identity
!= reviewed_source_identity
```

则：

```text
该 record = stale
→ 不进入可信 active set
→ 回到 Consumer-local Current Authority / semantic owner
→ 复核 activation metadata
→ 更新 Manifest
→ 再生成 Catalog
```

### 8.2 source missing / selector missing

直接 fail-closed；不通过相似文件名、旧路径或 upstream online search 自动补齐。

### 8.3 zero match

如果任务风险明显存在而 Catalog 无命中：

- 不解释为“没有规则”；
- 读取 Consumer-local Authority Map / relevant local Guide / Skill inventory；
- 必要时形成本地 discovery gap；
- ordinary runtime 不自动访问 upstream。

### 8.4 ambiguous primary responsibility

允许加载少量 routing / constraint owner 来消歧。

如果仍不能安全区分：

- 停止高影响动作；
- 回到 Consumer-local Current Authority；
- 只有当前 Consumer Authority 本身无法回答必要方法 / Skill 问题时，才触发已经存在的“upstream baseline / method gap”边界，而不是由 Catalog 自动跨仓检索。

## 9. Manifest / Catalog lifecycle

### 9.1 新增

只有满足以下条件之一才新增 discovery record：

- 新 Consumer-native Authority seam 会被独立任务反复发现；
- Consumer adoption 接受一个 reusable rule / Skill / Discipline；
- 已有大规则文档中的某个语义单元被证明需要独立激活；
- 新平台专项能力被当前 Consumer 采用。

不得因为新增一个 Markdown 文件就机械新增 record。

### 9.2 更新

触发：

- semantic owner 的 activation semantics 变化；
- source path / selector 改变；
- scope / responsibility / condition / risk 发生实际变化；
- Consumer override / supersede 决策变化；
- exact upstream baseline adoption 发生变化。

### 9.3 删除 / supersede

旧 record 失效时必须从 ordinary active Catalog 移除。

历史 provenance 可以保存在 Git / adoption record / archived metadata，但不能继续参与 Current routing。

### 9.4 重建

Runtime Catalog 应从 Manifest + Current Consumer source 状态确定性重建。

如果 Manifest 本身丢失，规范性事实仍完整存在；可以通过当前 Authority / adopted capability inventory 重新做 discovery audit，但在重建完成前应进入安全回退，而不是猜测旧 Catalog。

## 10. 最小示例（逻辑示例，不规定路径）

### 10.1 Adopted Skill

```json
{
  "id": "method.technical-plan",
  "kind": "skill",
  "activation_role": "execution",
  "scope": ["project"],
  "responsibility": ["technical-plan"],
  "conditions": ["cross-unit-how", "architecture-change"],
  "source": {
    "path": "<consumer-local-skill-path>",
    "binding": "semantic-reviewed",
    "reviewed_source_identity": "sha256:<selected-content>"
  },
  "origin": {
    "type": "adopted",
    "repository": "dygapp/agentic-dev",
    "baseline": "<exact-commit>",
    "source": "skills/technical-plan/SKILL.md"
  },
  "state": "active"
}
```

### 10.2 Consumer-native Authority Locator

```json
{
  "id": "consumer.architecture.current",
  "kind": "authority",
  "activation_role": "constraint",
  "scope": ["architecture"],
  "source": {
    "path": "<consumer-architecture-entry>",
    "binding": "current-locator"
  },
  "origin": {
    "type": "consumer"
  },
  "state": "active"
}
```

### 10.3 Consumer override

```json
{
  "id": "consumer.verification.project-specific",
  "kind": "authority",
  "activation_role": "constraint",
  "scope": ["verification"],
  "responsibility": ["execute-unit", "converge"],
  "source": {
    "path": "<consumer-verification-owner>",
    "binding": "current-locator"
  },
  "origin": {
    "type": "consumer"
  },
  "relations": {
    "overrides": ["<adopted-generic-default-id>"]
  },
  "state": "active"
}
```

## 11. 物理实现约束

v2 允许 Consumer 根据规模选择：

### 小型 Consumer

一个小的本地 Manifest 可以同时作为 Runtime Catalog，不引入生成器。

### 中大型 Consumer

可以维护少量 Activation Manifest / descriptor 输入，并生成一个 compact Runtime Catalog；生成器只做：

- schema validation；
- source / selector resolution；
- source identity validation；
- active filtering；
- deterministic projection。

生成器不得自动发明 conditions、修正规则语义或通过 LLM 静默更新 reviewed identity。

### 明确不要求

- 全仓文件 Front Matter；
- 数据库；
- 向量 embedding；
- 图数据库；
- MCP service；
- 后台 daemon；
- 中央 hosted registry。

## 12. Phase C 决定

1. 正式采用 **Activation Manifest + optional derived Runtime Catalog** 的职责模型。
2. Metadata 只保存发现分类、local source pointer、lifecycle 与 provenance，不保存规则正文 / required checks。
3. 使用 `activation_role` 区分 bootstrap / routing / constraint / execution，支持 routing-only 不机械加载 Skill。
4. 使用 `semantic-reviewed` 与 `current-locator` 两种 source binding，分别处理语义 metadata stale 风险和高频 Consumer Current Authority。
5. Consumer Authority precedence 不转换为全局数值 priority。
6. adopted reusable 与 Consumer-native records 可以共存，但 `origin` 身份必须保留。
7. rejected candidate 不进入 runtime record；superseded / disabled 不进入 active Catalog。
8. Runtime Catalog 可删除 / 重建，任何 source stale / missing / ambiguous 情况 fail-closed 到 Consumer-local Authority。
9. JSON 仅作为逻辑示例；具体 Consumer 可以使用 JSON / YAML / 等价结构化载体，只要满足本契约。
10. 当前仍无证据需要 Runtime Rule Index 服务或更复杂检索基础设施。

## 13. 进入 Phase D 的约束

Phase D 必须基于本契约定义运行时接口：

- task facts 如何形成；
- discovery 如何返回 primary / supporting；
- module / Authority / Skill 何时读取；
- Stage Return 如何重新触发 discovery；
- fail-closed 如何回到 Consumer-local Authority；
- runtime adapter / generator 如何保持无方法语义；
- ordinary runtime 如何证明没有访问 upstream。
