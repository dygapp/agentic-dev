---
id: project:distribution-rebuild-specification
type: project
status: active
---

# 发布模型重构规范与验收合同

## 1. 文档职责

本文是 Issue #172 — **发布模型重构：从能力仓库直接投影转向 Skills 发布产物** 的项目级规范与验收 Authority。

本文只拥有本轮重构的：

- 问题定义；
- 冻结目标；
- Source / Distribution 边界；
- Consumer 发布目标；
- 资产分类要求；
- 运行时兼容要求；
- 验证策略；
- Legacy Consumer 能力覆盖要求；
- Acceptance Criteria；
- 由 Acceptance Criteria 派生的实施 Gate。

Issue #172 只承担实施协调、Gate、Review、Actions 与 Evidence timeline，不得通过 comment 静默改变本文的目标或验收条件。

本文不是新的 reusable Capability。重构完成后，最终稳定语义必须分别回写真实 Project / Architecture / Skill / Tool / Release owner；本文届时退出 Current Authority，由 Git / Issue / PR 保存实施历史。

## 2. 背景与问题

当前 `agentic-dev` 同时承担：

1. 通用 AI Agent 软件开发能力的设计与演进；
2. Method / Architecture / Skill / Rule / Tool 等内部语义所有权；
3. Consumer adoption / upgrade；
4. Consumer-local runtime projection。

现行模型已经证明“Project 不传播、Capability 传播”和 Consumer ordinary runtime `upstream access = 0` 等原则具有价值，但真实 Consumer 也暴露出新的结构问题：

- provider-side 的 Method / Architecture / Rule / Tool 形态被较大程度投影到 Consumer；
- Consumer 的 `docs/**` 同时出现业务 / 产品 / 系统知识与 AI 开发元能力文档；
- Consumer 根目录出现 `skills/`、`tools/` 等主要服务 Agent runtime 的资产；
- upstream authoring layout 与 Consumer runtime layout 被过度绑定；
- adoption / upgrade 需要理解和比较较多 upstream 内部能力类型；
- Agent Skills 已支持 `SKILL.md + references/ + scripts/ + assets/` 的复杂包装，但当前发布模型没有充分利用 Skill 作为 Distribution Unit；
- 当前复杂内部语义模型是否需要以同样复杂度暴露给普通软件 Consumer，尚未经过严格的 Distribution Boundary 审计。

因此，本轮不把问题定义为简单目录迁移，而定义为：

> **将 `agentic-dev` 的内部 Authoring / Source Model 与对普通软件 Consumer 的 Distribution / Runtime Model 正式分离。**

## 3. 目标定位

重构后的 `agentic-dev` 应被理解为：

> **开发、验证、构建并发布 Software Development Agent Skills 的源码项目。**

这不意味着 `agentic-dev` 内部必须只保留 Skills。

内部 Source Model 可以继续维护有真实语义所有权价值的：

- Project Knowledge；
- Method；
- Architecture；
- Rule；
- Skill；
- Tool；
- Eval；
- Research；
- Human Guide；
- Build / Release infrastructure。

但：

> **Source Model 中存在的资产类型，不自动成为 Consumer Distribution Model 中的一等资产类型。**

Consumer 面向普通软件开发，只应安装经过构建、验证和版本化的发布产物，而不是把 upstream 源码仓库的信息架构缩小后复制到本地。

## 4. 冻结原则

### 4.1 Source Model 与 Distribution Model 分离

`agentic-dev` 内部使用什么语义 owner，与最终 Consumer 安装什么文件是两个独立问题。

不得再使用：

```text
upstream path / type
→ Consumer 同名 path / type
```

作为默认 projection 规则。

正确方向是：

```text
source semantics
→ distribution classification
→ release build / transformation
→ versioned release artifact
→ Consumer installation
```

### 4.2 Skill 是主要 Distribution Unit

首版 Consumer Release 以 Agent Skill 为主要能力分发单元。

Skill 可以按 Agent Skills 规范包含：

```text
<skill>/
├── SKILL.md
├── references/
├── scripts/
└── assets/
```

这些 supporting resources 可以承载：

- 详细规范；
- 生命周期说明；
- 条件性决策资料；
- 模板；
- 确定性脚本；
- 运行所需静态资源。

不得继续因为“内容复杂”就自动要求 Consumer 建立平级 Method / Architecture / Rule / Tool namespace。

同时，Skill 仍必须具有有界 Trigger / Purpose，不能为了减少文件类型退化为接管完整开发生命周期的单一超级 Skill。复杂发布物可以由多个可组合 Skill 共同形成。

### 4.3 adopt semantics，不镜像文件

Source 中的 Method / Architecture / Rule / Skill / Tool 等内容进入发布物前，必须先回答：

1. Consumer ordinary runtime 是否真的需要这项语义？
2. 它应由哪个发布 Skill 持有或引用？
3. 是否需要 transformation / compilation？
4. 是否本质属于 Consumer-local policy？
5. 是否只是 provider-side design / evidence / guide？

不得因为文件当前存在于 `docs/architecture/**`、`docs/methods/**`、`docs/rules/**` 就在 Consumer 中建立对应目录。

### 4.4 Guide 默认不是发布对象

`docs/guides/**` 默认属于 provider Human View，只服务理解、维护与采用判断，不进入 Consumer Release。

Consumer 确有长期人类说明需求时，应形成 Consumer-owned Human View，而不是复制 upstream Guide。

### 4.5 Architecture 默认不是发布对象

provider-side Architecture 主要用于定义 `agentic-dev` 自身能力类型、ownership、组合关系和设计不变量。

Architecture 不能按目录整体发布，也不建立默认的：

```text
.agents/architecture/
```

如果某项 Architecture 语义是 Consumer runtime 的必要前提，应经过显式裁决后：

- 编译进对应 Skill 的 `SKILL.md`；
- 放入对应 Skill 的 `references/**`；
- 或由 Consumer 自身真实 Project / System Architecture owner 持有。

### 4.6 Method / Rule 不建立默认 Consumer 一级 namespace

首版发布目标不预设：

```text
.agents/methods/
.agents/rules/
.agents/contracts/
.agents/tools/
.agents/evals/
```

必须存在。

Source 中的 Method / Rule 可以继续是 provider-side canonical owner，但进入发布物时应优先成为一个或多个 Skill 的运行说明、reference、script input 或生成内容。

只有新的跨 Runtime Evidence 证明某个一级 namespace 是不可替代的独立运行所有者时，才允许修改本文重新引入。

### 4.7 Consumer-local policy 保持 Consumer-local

以下内容不得为了“发布完整”被自动吸收到通用 Release：

- Consumer 产品 / 业务事实；
- Consumer Requirement / Specification / System Architecture；
- Consumer 当前 Roadmap / Current Work；
- Consumer GitHub 操作授权矩阵；
- Consumer 技术栈专项 policy；
- Consumer 本地术语、审批、迁移、环境与组织约束；
- 其他只有目标 Repository Authority 才能决定的规则。

通用 Release 必须保留扩展 / 特化边界，而不是把一个真实 Consumer 的本地治理反向泛化。

### 4.8 Consumer ordinary runtime 不依赖 upstream Repository

安装完成后，普通 Consumer 工作不得要求：

- 在线读取 `dygapp/agentic-dev` current branch；
- 读取 upstream Roadmap / Issue / PR；
- 解析“latest baseline”；
- 在 Skill 发现失败时回退 upstream；
- 为正常任务重新执行 upstream adoption analysis。

发布版本、来源 SHA 与必要 provenance 可以记录，但 ordinary runtime 必须依赖 Consumer-local installed release。

### 4.9 repository-local 默认安装结果

首版 repository-local deployment target 的目标形态为：

```text
AGENTS.md

.agents/
  README.md
  skills/
    <skill>/
      SKILL.md
      references/
      scripts/
      assets/
```

其中：

- `AGENTS.md` 继续是 Repository-native Bootstrap / Authority surface；
- `.agents/README.md` 是 Human View，解释安装内容、边界和使用方式；
- `.agents/skills/**` 是主要发布能力面；
- supporting directories 按 Skill 实际需要存在，不要求每个 Skill 都创建；
- Consumer 的 `docs/**` 继续优先承载产品、业务、系统、技术与项目知识。

平台强制路径继续留在平台原生位置，例如：

```text
.github/workflows/**
```

不得为了目录统一把平台 adapter 强搬入 `.agents/**`。

### 4.10 `.agents/README.md` 只承担 Human View

`.agents/README.md` 必须说明：

- `.agents/**` 是什么；
- 已安装资产类型是什么；
- Skill / supporting resource 的基本关系；
- 哪些内容不属于 `.agents/**`；
- 如何理解版本 / provenance；
- 非原生 Skill Runtime 如何进入兼容发现路径。

它不得成为第二套 Skill selector、Rule Map、Current Gate、Roadmap 或 manually synchronized inventory Authority。

### 4.11 一个 Source，多种未来 Distribution Target

首版必须交付 repository-local `.agents/skills/**` 发布目标。

但 Source / Distribution Architecture 不得把 Skill 绑定为只适用于这一种物理发布方式。未来可以从同一 canonical Skill source 生成其他 Runtime / Plugin / package target。

本轮不要求实现 Plugin 发布。

## 5. 资产分类模型

### 5.1 全仓扫描是重构前置 Gate

在大规模结构修改前，必须对当前 Repository 的 Current assets 做 Repository-wide Distribution Classification。

每个具有独立语义所有权或独立发布责任的 Current asset 必须明确：

- 当前路径；
- 当前 `type` / semantic owner；
- 为什么存在；
- 是否属于 provider Project / authoring / runtime / build / eval / research / guide；
- Consumer runtime 是否需要；
- distribution disposition；
- release target；
- 是否需要 transformation；
- 是否被其他 owner 替代；
- 是否应退出 Current tree。

### 5.2 稳定 distribution disposition

首版至少支持以下分发状态：

- `source-only`：只属于 `agentic-dev` 源码 / 项目 /研究 /验证，不进入发布物；
- `release-input`：作为发布构建的语义输入，但不能原样投影；
- `release-direct`：自身就是发布运行资产，可按声明直接进入 release；
- `retired`：经重构确认退出 Current model。

不再用“文件位于 reusable 目录”隐式推断 distribution status。

### 5.3 分类应同源、可机械读取

对已经使用 YAML Front Matter 的 Markdown owner，应在文件自身增加 distribution metadata，而不是维护长期手工中央表。

对 `SKILL.md`，自定义信息必须通过 Agent Skills Specification 允许的 `metadata` string map 表达，不新增非法顶层字段。

Skill 内部的 `references/**`、`scripts/**`、`assets/**` 默认继承所属 Skill 的发布生命周期；只有它形成独立 semantic owner / release responsibility 时才单独分类。

其他独立文本 / script owner 可以使用其原生 header comment 或等价机器可读 metadata。不得为了“每个文件都打标签”给普通 fixture、生成物或 Skill 内部附件制造重复 metadata。

### 5.4 不建立第二套手工 Registry

可以通过脚本从同源 metadata 生成：

- asset audit report；
- release inventory；
- unclassified list；
- release target mapping；
- provenance manifest；
- integrity / checksum manifest。

这些生成结果不是第二套 Authority，不允许人工同步维护。

## 6. Release Build

### 6.1 发布物必须由显式 Build 生成

发布过程必须具有确定性的 build / package step，而不是人工复制目录。

至少满足：

```text
exact source SHA
+ current classified source
+ release build logic
→ release artifact
```

### 6.2 Build 可以进行 Transformation

允许并预期：

- 把多个 source semantic owner 汇编为一个 Skill package；
- 把 Method lifecycle 转换成 Skill instructions / references；
- 把通用 Rule 语义编译进一个或多个 Skill；
- 把 Tool 代码移动 / 复制进需要它的 Skill `scripts/**`；
- 生成兼容 discovery metadata；
- 生成 provenance / checksum manifest。

因此：

> **release artifact 不要求与 source tree 1:1 对应。**

### 6.3 发布物不得泄漏 provider Project state

Release 中不得包含作为 ordinary runtime Authority 的：

- `agentic-dev` Project Roadmap；
- upstream current Gate；
- Open Issue / PR；
- provider Capability Profile current instance；
- Research history；
- historical Eval result；
- provider-only Human Guide；
- self-adoption state。

必要 provenance 只记录版本和来源，不获得 Consumer current Authority。

### 6.4 Release provenance

每个 Release Candidate 至少可恢复：

- release version / candidate id；
- exact source commit SHA；
- included Skill identities；
- generated artifact integrity / checksums；
- Runtime compatibility declaration；
- build result / verification evidence locator。

provenance 可以由生成 manifest 承载，但 manifest 不是 Runtime selector 的第二 Authority。

## 7. Runtime 兼容要求

### 7.1 Codex repository-local Skill discovery

必须验证安装后的：

```text
.agents/skills/**
```

能够被支持 repository Skills 的 Codex Runtime 正确发现、选择和按需加载。

验证不能只证明文件存在，至少应包含 activation / behavior evidence。

### 7.2 ChatGPT + GitHub Connector 兼容

不得假设 ChatGPT + GitHub Connector 与 Codex 具有完全相同的 repository-native Skill scan 行为。

Release 必须提供一个足够薄、可审计、不复制 Skill 正文的兼容路径，使 ChatGPT 会话能够通过 GitHub Repository：

```text
AGENTS.md
→ repository-defined Skill discovery entry
→ matching SKILL.md
→ required references / resources
→ task execution
```

兼容发现可以使用由 `SKILL.md` metadata 自动生成的少量 index / manifest；如果使用，必须满足：

- 机械生成；
- 只保存必要 locator / metadata；
- 不复制 Skill Procedure；
- 不成为第二套手工 selector；
- 与 Skill corpus 可以 deterministic validate。

### 7.3 scripts / external execution capability

Skill 包含 script 不等于每个 Runtime 都能直接执行 script。

每个依赖可执行能力的发布 Skill 必须声明或可确定：

- 当前 Runtime 是否能 direct execute；
- 是否有 GitHub Actions / connector / external tool 等 automated alternate path；
- Evidence 如何恢复；
- 所有声明路径不可用时如何 fail closed。

不得出现“ChatGPT 可以读懂 Skill，但核心 Procedure 只能调用一个当前 Runtime 无法执行的本地 script，且没有替代路径”的隐式失效。

### 7.4 Progressive Disclosure

新的发布模型仍必须保持上下文有界：

- 未激活时只暴露低成本 Skill metadata；
- Skill 命中后加载 `SKILL.md`；
- reference / script / asset 只按需要加载；
- 不为了替代 Rule Discovery 而在 Bootstrap 全量枚举所有规范正文。

## 8. 重构期间验证策略

### 8.1 真实 Consumer mutation 不作为中间 Gate

Gate A～G 期间，默认不要求人工切换到真实 Consumer 执行 adoption / upgrade / mutation。

不得因为每个中间 Source refactor 都要求人工 Consumer 验证而中断连续重构。

### 8.2 保留 repository-native 当前验证

重构期间继续使用当前 Repository Authority 要求的：

- deterministic lint / tests；
- current affected evals；
- Fresh / isolated runtime eval；
- exact-subject Current Evidence；
- 高影响 `review-change`；
- release build / package integrity checks；
- necessary negative controls。

不得以“最终还会做 Consumer Validation”为理由降低当前仓库验证。

### 8.3 自动 Consumer-like validation 可以保留

如果可以完全自动化，可以建立 isolated fixture / temporary workspace：

```text
build release
→ install release into fixture
→ bootstrap
→ discover Skill
→ execute representative responsibility
→ verify upstream dependency = 0
→ negative / fail-closed controls
```

这类验证属于 Release Integration Test，可以进入持续 CI。

它不等于最终真实 Consumer Validation。

## 9. Legacy Consumer Capability Coverage Audit

### 9.1 Gate 位置

完整 Source / Distribution 重构、Release Build 和 Automated Runtime Acceptance 完成后，在真实 Consumer migration 之前，必须对现有 Consumer 的 AI development capability 做一次只读覆盖审计。

本轮至少以 `dygapp/jilinjobs-cms` 当前 Repository 为真实样本。

Gate F 只进行读取、比较、分类和补齐 upstream Release 缺口，不在 Consumer 中实施迁移。

### 9.2 比较对象

比较的不是旧路径与新路径，而是：

```text
legacy Consumer AI development obligations
vs
new Release + Consumer-local retained obligations
```

至少覆盖：

- Repository Authority / Knowledge Boundary；
- Fresh Context / Bootstrap；
- Requirement Baseline Establishment；
- Architecture Clarification；
- ordinary Feature / change lifecycle；
- Specification；
- Technical Planning；
- work slicing；
- readiness；
- implementation；
- systematic debugging；
- convergence；
- verification / evidence discipline；
- independent change review；
- human review；
- human escalation；
- external operation safety；
- GitHub Actions verification；
- conditional policy / rule activation；
- language / terminology governance；
- technology-specific policy；
- current work / Roadmap ownership；
- upstream decoupling；
- adoption / upgrade / release update；
- executable capability / alternate path / fail-closed；
- Current Evidence / exact-subject verification。

### 9.3 每项只能得到显式 disposition

允许的最终状态：

- `release-covered`：由一个发布 Skill 完整覆盖；
- `release-composed`：由多个发布 Skill / references 共同覆盖；
- `consumer-local`：应继续由 Consumer Repository Authority 持有；
- `bootstrap-covered`：由根 `AGENTS.md` 或 Repository Bootstrap 承担；
- `platform-covered`：由 GitHub / Runtime / Plugin / native mechanism 承担；
- `intentionally-retired`：有明确理由确认退出；
- `gap`：新模型遗漏，阻塞真实迁移。

进入真实 Consumer migration 前：

```text
unclassified = 0
gap = 0
```

### 9.4 不得用“Skill 数量差不多”替代能力覆盖

覆盖审计必须以 obligation / behavior 为粒度，不以旧文件数量、新 Skill 数量或目录映射作为充分证据。

## 10. 真实 Consumer Validation

真实 Consumer Validation 只在 Release Candidate Freeze 后开始。

它至少验证：

- 安装 / 升级发布物；
- Consumer 业务 / 项目 `docs/**` 不再承载不必要的通用 AI 开发元能力副本；
- Consumer-local policy / technology specialization 未丢失；
- `.agents/README.md` 人类入口可理解；
- Codex repository-local Skill discovery / activation；
- ChatGPT + GitHub Connector compatibility path；
- supporting references / scripts / alternate execution；
- ordinary runtime `upstream access = 0`；
- Fresh Context 从 Consumer Repository 独立恢复；
- representative ordinary Feature / change 可继续推进；
- legacy coverage audit 中的所有 retained obligations 实际可恢复；
- 未出现隐藏的 provider Project state 依赖。

真实 Consumer migration / validation 可以需要人工参与，但不得回溯成 Gate A～G 每个中间阶段的强制人工步骤。

## 11. Acceptance Criteria

以下 Acceptance ID 是本轮重构的冻结验收合同。

### 11.1 Source / Distribution 边界

| ID | 验收条件 |
|---|---|
| `DR-AC-01` | Current Architecture 明确区分 Source / Authoring Model 与 Consumer Distribution / Runtime Model，不再把二者视为同一目录模型。 |
| `DR-AC-02` | `agentic-dev` 被明确定位为开发、验证、构建并发布 Software Development Agent Skills 的源码项目；内部仍可保留必要的 Method / Architecture / Rule 等 authoring owner。 |
| `DR-AC-03` | Skill 成为首版主要 Distribution Unit，并允许按规范使用 `references/`、`scripts/`、`assets/` 承载复杂 supporting content。 |
| `DR-AC-04` | 新发布模型没有通过一个无边界超级 Skill 接管完整开发生命周期；发布 Skill 保持可发现、可组合和有界触发。 |
| `DR-AC-05` | Guide 默认明确为 provider Human View，不作为 Consumer release object。 |
| `DR-AC-06` | Architecture 不再按目录直接投影到 Consumer；需要的 runtime semantics 已被显式编译 / 投影到真实发布 owner。 |
| `DR-AC-07` | 首版 Consumer Release 不默认要求 `.agents/methods`、`.agents/architecture`、`.agents/rules`、`.agents/contracts`、`.agents/tools`、`.agents/evals`。 |
| `DR-AC-08` | Consumer-specific Product / Requirement / System Architecture / technology policy / authorization / current state 保持 Consumer-local，不被通用 Release 吸收。 |

### 11.2 Asset Classification / Build

| ID | 验收条件 |
|---|---|
| `DR-AC-09` | 对当前 Current tree 完成 Repository-wide Distribution Classification；所有独立语义 / 发布责任资产都有 disposition。 |
| `DR-AC-10` | 分类可由同源 metadata 或明确继承关系机械恢复；不存在需要人工同步的中央分类 Registry。 |
| `DR-AC-11` | 发布相关审计结果满足 `unclassified = 0`、`orphan-release-input = 0`、`ambiguous-release-owner = 0`。 |
| `DR-AC-12` | Release 由 exact source SHA 的显式 deterministic build / package step 生成，不依赖人工复制。 |
| `DR-AC-13` | Build 支持 source semantics → Skill package transformation，不要求 source tree 与 release tree 1:1。 |
| `DR-AC-14` | Release artifact 不携带 provider Project current state、Research history、historical Eval result 或 provider-only Guide 作为 Consumer runtime Authority。 |
| `DR-AC-15` | 每个 Release Candidate 可恢复 release identity、exact source SHA、Skill inventory、integrity/checksum、compatibility 与 verification evidence locator。 |
| `DR-AC-16` | 生成的 inventory / manifest 全部来自 canonical metadata / build，不形成第二套人工维护 Authority。 |

### 11.3 Consumer Repository Layout

| ID | 验收条件 |
|---|---|
| `DR-AC-17` | repository-local 安装结果以根 `AGENTS.md` + `.agents/README.md` + `.agents/skills/**` 为核心，Consumer `docs/**` 恢复为产品 / 业务 / 系统 / 技术 / 项目知识空间。 |
| `DR-AC-18` | `.agents/README.md` 解释 installed capability，但不复制 Skill selector、Skill Procedure、Current Gate、Roadmap 或手工 inventory Authority。 |
| `DR-AC-19` | 平台必须固定位置的 adapter 继续位于平台原生路径，不为了目录统一强制进入 `.agents/**`。 |
| `DR-AC-20` | Consumer ordinary runtime 不访问 upstream current state，且 discovery / runtime failure 不回退 `agentic-dev` Repository。 |

### 11.4 Runtime Compatibility

| ID | 验收条件 |
|---|---|
| `DR-AC-21` | Codex 对安装后的 `.agents/skills/**` 完成真实 native discovery / activation / representative behavior 验证。 |
| `DR-AC-22` | ChatGPT + GitHub Connector 存在明确、薄、可审计的 Repository-defined Skill discovery compatibility path；实现不依赖“ChatGPT 一定原生扫描 `.agents/skills`”的未经验证假设。 |
| `DR-AC-23` | 若 compatibility path 使用 index / manifest，则该资产完全由 Skill metadata 机械生成并通过 deterministic consistency check。 |
| `DR-AC-24` | 依赖 scripts / external execution 的 Skill 对 direct path、automated alternate、Evidence recovery 与 fail-closed 有明确可验证行为。 |
| `DR-AC-25` | 新发布模型保持 Progressive Disclosure；普通 Bootstrap 不全量加载所有 Skill references / rules / supporting content。 |

### 11.5 Verification / Governance

| ID | 验收条件 |
|---|---|
| `DR-AC-26` | Gate A～G 不把真实 Consumer mutation / 人工 Consumer validation 作为每个中间阶段的 blocking Gate；可自动化 Consumer-like validation 可保留。 |
| `DR-AC-27` | 每个重构 PR 都显式声明 Covered Acceptance IDs、Not Covered IDs 与当前 Evidence。 |
| `DR-AC-28` | 如果实施需要改变冻结目标，必须先修改本文并完成相应独立复核；不得通过实现便利静默缩减 Acceptance。 |
| `DR-AC-29` | 所有受影响的 repository-native deterministic tests / evals / Fresh Runtime / negative controls 在最终 exact subject 上取得 Current Evidence。 |
| `DR-AC-30` | 高影响变更按当前 Rule 使用 `review-change` 完成独立复核；Review PASS 不替代集成授权。 |

### 11.6 Legacy Coverage / Final Acceptance

| ID | 验收条件 |
|---|---|
| `DR-AC-31` | 在真实 Consumer migration 前完成 Legacy Consumer Capability Coverage Audit，并对最低覆盖清单逐项给出合法 disposition。 |
| `DR-AC-32` | Coverage Audit 满足 `unclassified = 0`、`gap = 0`；`consumer-local` 项有明确本地 owner，不因 Release 简化而丢失。 |
| `DR-AC-33` | Gate G 对所有 `DR-AC-01`～`DR-AC-32` 执行 Specification Conformance Review，最终 `Blocking = 0`、`Medium = 0`、`Unverified = 0`，否则不得 Freeze Release Candidate。 |
| `DR-AC-34` | 只有 Gate G PASS 后才进入真实 Consumer migration / validation；真实验证覆盖 Codex、ChatGPT + GitHub Connector、upstream decoupling、Consumer-local Authority 与 representative software-development behavior。 |

## 12. 实施 Gate

### Gate A — Specification & Acceptance Freeze

目标：

- 固化本文；
- 建立 Issue #172；
- 把 Roadmap 切换到本轮 active evolution；
- 执行独立 `review-change`；
- 在集成后冻结 `DR-AC-01`～`DR-AC-34`。

Gate A 不修改 Source / Distribution implementation。

### Gate B — Repository-wide Asset / Distribution Classification

目标：

- 扫描 Current tree；
- 建立 distribution metadata contract；
- 为 Current semantic owners 分类；
- 建立 deterministic classification / audit tooling；
- 得到完整 asset audit；
- 满足 `DR-AC-09`～`DR-AC-11`。

不得在分类未闭环时大规模移动目录。

### Gate C — Source / Distribution Model Rebuild

目标：

- 重构 Architecture / Project / Consumer model；
- 明确哪些现有 Method / Rule / Architecture 只属于 provider authoring；
- 调整 Consumer adoption / upgrade 语义为 release install / update 边界；
- 清除“upstream type → Consumer 同名 type”的默认假设；
- 满足 `DR-AC-01`～`DR-AC-08`、`DR-AC-20`。

### Gate D — Skill Packaging & Release Build

目标：

- 设计首版 release skill set；
- 将必要 Source semantics 编译 / 包装进 Skill；
- 引入 `references/`、`scripts/`、`assets/`；
- 建立 deterministic release builder；
- 生成 repository-local install artifact；
- 建立 provenance / integrity；
- 满足 `DR-AC-12`～`DR-AC-19`。

首版 Skill set 的精确拆分由 Gate B / C Evidence 决定，不在 Gate A 凭讨论预设全部 Skill 名单。

### Gate E — Automated Runtime Acceptance

目标：

- Agent Skills 格式 / metadata 验证；
- isolated install fixture；
- Codex native discovery / activation；
- ChatGPT + GitHub Connector compatibility path 的自动化可验证部分；
- script / external path / fail-closed；
- upstream dependency negative control；
- Progressive Disclosure；
- 满足 `DR-AC-21`～`DR-AC-30` 中可自动取得的 Evidence。

### Gate F — Legacy Consumer Capability Coverage Audit

目标：

- 只读恢复 `dygapp/jilinjobs-cms` 当前 AI governance；
- 建立 obligation-level coverage matrix；
- 对每项给出合法 disposition；
- 所有 `gap` 返回 Gate C / D / E 修复；
- 最终满足 `DR-AC-31`、`DR-AC-32`。

本 Gate 不修改 Consumer。

### Gate G — Final Specification Conformance Review & Release Candidate Freeze

目标：

- 以本文为唯一 acceptance checklist；
- 逐项核验 `DR-AC-01`～`DR-AC-32`；
- 重新执行 exact-head required validation；
- 独立 Final Review；
- 满足 `DR-AC-33` 后冻结 Release Candidate。

### Gate H — Real Consumer Migration & Validation

Gate H 不属于“重构中间验证”，而是 Release Candidate 完整形成后的真实采用验证。

目标：

- 在独立 Consumer 工作上下文中迁移 / 安装新 Release；
- 删除被新 Release 正式替代的旧 AI development copies；
- 保留 Coverage Audit 判定的 Consumer-local obligations；
- 验证 `DR-AC-34`；
- 将真实 Evidence 反馈给 `agentic-dev`。

## 13. 实施顺序与连续执行原则

默认顺序：

```text
Gate A
→ Gate B
→ Gate C
→ Gate D
→ Gate E
→ Gate F
→ Gate G
→ Gate H
```

Gate A～G 应尽量在 `agentic-dev` 内连续推进。

只有以下情况允许阻塞：

- 当前 Authority 无法恢复；
- 必要 Repository / external permission 缺失；
- Acceptance 本身发生真实冲突；
- 需要改变本文冻结的重大目标；
- 必须由人工作出的 Product / Scope / Major Architecture decision。

普通实现细节、目录命名、脚本组织、fixture 结构、测试组织等可逆事项由当前 Agent 按本文与 Repository Authority 自主处理。

## 14. Scope Change Control

本文集成后，任何会改变 `DR-AC-01`～`DR-AC-34` 实质含义的修改都属于 Specification Change。

修改顺序必须是：

```text
new evidence / conflict
→ update this specification
→ independent review
→ integrate specification change
→ adjust implementation
```

禁止：

```text
implementation convenience
→ silently skip requirement
→ explain after the fact
```

如果某个 Acceptance 最终确认不再适用，应在本文中显式删除 / 替代并记录理由，不使用隐式 waiver。

## 15. 本轮明确暂缓事项

以下问题留到独立讨论，不在本规范中提前定案：

- 是否新增独立 `code-review` Skill；
- 是否把 setup / install / upgrade orchestration 封装为 Skill；
- 是否发布 Plugin 版本；
- 是否需要除首版 repository-local target 之外的其他 distribution target。

这些事项不得阻塞当前 Source / Distribution Rebuild，除非 Gate B～F Evidence 证明它们已经成为满足冻结 Acceptance 的必要条件。
