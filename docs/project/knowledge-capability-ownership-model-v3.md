# Knowledge & Capability Ownership Model v3

**状态：** V3-01 候选基线  
**跟踪：** Issue #95  
**上游规划：** `docs/project/rule-governance-knowledge-activation-v3.md`

## 1. 目的

本文为 V3-01 提供可执行的 ownership decision matrix，用于判断一段长期内容应该由谁拥有，而不是根据它当前位于哪个目录、使用什么文件名或被哪个 Agent 读取来推断身份。

核心原则：

> **先判断 semantic owner，再判断 scope、lifecycle 和 representation。**

以下四个维度必须分开：

```text
semantic owner role
+ applicability / provenance scope
+ runtime / lifecycle role
+ representation / authority form
```

任何单一 `type`、目录名、Front Matter 字段或文件扩展名都不能替代这四个判断。

## 2. 第一维：Semantic Owner Role

### 2.1 Method / Principle

回答：

> 通用开发生命周期、阶段职责、Authority 边界和顶层不变量是什么？

进入条件：

- 跨多个项目成立；
- 会约束多个 Skill / capability；
- 改变后会影响生命周期、阶段、完成语义、Authority precedence 或顶层工作原则。

不进入：

- 单一技术栈规则；
- 单一 Repository 的 Git / 语言 /集成政策；
- 某个稳定 Agent procedure 的具体步骤；
- 项目业务事实。

典型 owner：`docs/method/*`。

### 2.2 Skill / Procedural Capability

回答：

> Agent 在一个稳定、可独立组合的职责中应该怎样执行？

进入条件通常同时包括：

- 有明确 trigger / Use When / Do Not Use；
- 有稳定输入；
- 有可重复 procedure；
- 有明确输出；
- 有 Exit / Stage Return / Escalation；
- 可以作为独立职责被调用或组合；
- 过程复杂度足以值得 JIT 加载和独立维护。

不进入：

- 只有若干约束，没有独立任务入口；
- 只是“Agent 应遵守”的一条规则；
- 单一 Repository 本地规范；
- 仅供人理解的说明。

“可复用”或“Agent 会读取”都不足以构成 Skill admission。

### 2.3 Reusable Engineering Capability / Discipline / Profile

回答：

> 跨项目复用的工程约束、默认知识、技术 / 验证边界是什么？

适用于：

- Engineering Discipline；
- Technology Profile；
- Verification Profile；
- 经当前工程能力架构准入的同类 reusable non-procedural capability。

典型特征：

- 可以被多个 Skill 消费；
- 通常跨多个 Consumer 复用；
- 可以有 trigger / condition，但不一定有独立任务流程；
- 没有必要为了被 Agent 激活而 Skill 化；
- Consumer 可以选择性采用、覆盖或拒绝其默认值，但不能用本地偏好改写客观技术事实。

如果一项 Engineering Discipline 后续形成稳定独立流程、明确输入输出和独立调度价值，再按 Skill admission 重新评估；不能提前升级。

### 2.4 Repository-local Policy / Standard / Rule

回答：

> 当前 Repository 中相关工作持续必须遵守什么本地约束？

典型内容：

- Git Commit / Branch / Integration policy；
- 主导语言和术语规则；
- 仓库授权边界；
- 本地验证与 Review policy；
- 当前 Repository 的目录 / 协作 /运行约束。

典型特征：

- 预期不同 Repository 可以合理不同；
- 由当前 Repository 自己拥有和演进；
- 通常没有独立可调用 procedure；
- 可以从 upstream 模板 / Guide 初始化，但 adoption 后 current authority 属于本地。

Repository-local Rule 不因为可以被多个项目参考就自动成为 reusable upstream capability；关键是其语义是否允许 / 预期由各 Repository 自行决定。

### 2.5 Project / Product Authority Resource

回答：

> 对当前项目而言，什么是真的、必须实现、已经决定或当前有效？

包括但不限于：

- Requirement / Domain Authority；
- Specification；
- Architecture state；
- ADR；
- Roadmap；
- Verification Strategy；
- durable Work / Execution Authority。

典型特征：

- 由当前项目事实和决策产生；
- 高于 Skill 对项目事实的推测；
- upstream reusable capability 不得覆盖；
- 原始需求 / 外部资料必须经过当前项目 adoption / confirmation 才能成为 Authority。

### 2.6 Guide

回答：

> 人或低频 setup 场景中的 Agent，应该怎样理解、选择、采用或升级这些能力？

Guide 的主要适用场景：

- Human-facing explanation；
- new Consumer initialization；
- existing Consumer adoption；
- baseline upgrade；
- 能力清单、入口与解释性导航。

Guide 可以较详细；在 initialization / upgrade 中完整读取属于可接受的一次性 token 成本。

Guide 不拥有：

- ordinary runtime 的核心 Agent procedure；
- Repository-local policy 的规范正文；
- Project Authority 的事实正文；
- Reusable Engineering Capability 的规范正文。

因此：

```text
not Method / not Skill
≠
Guide
```

### 2.7 Research / Input / Evidence

回答：

> 哪些材料支持后续判断，但当前还不是 Current Authority？

包括：

- raw requirement / customer material；
- 外部政策 / 标准原文；
- Research；
- Experiment / Eval；
- historical evidence；
- 一次性 analysis；
- 会议 / 调查输入。

这些资源只有经过明确 adoption / promotion 后，才可能形成前六类 Current Resource。

## 3. 第二维：Applicability / Provenance Scope

semantic owner 与来源 / 适用范围分开。至少使用以下 scope：

| Scope | 含义 |
|---|---|
| `reusable-upstream` | 由 `agentic-dev` 维护，供多个 Consumer 选择性采用 |
| `repository-local` | 只对当前 Repository 持续生效 |
| `consumer-native` | Consumer 自己形成并自行演进 |
| `adopted-local` | 起源于 upstream，采用后成为 Consumer-local 当前资产 |
| `external-input` | 外部原始输入，尚未成为当前 Authority |
| `historical-evidence` | 只承担历史 / Evidence 职责 |

规则：

```text
origin / provenance
≠
current authority
```

例如：

- `agentic-dev` Technology Profile = Reusable Engineering Capability + `reusable-upstream`；
- Consumer 自己的 Git 规范 = Repository-local Policy + `consumer-native`；
- Consumer 采用并调整的验证画像 = Reusable Engineering Capability 的 `adopted-local` projection；
- Consumer Requirement = Project Authority + `consumer-native`。

adopted-local 资产进入普通运行后，不要求继续访问 upstream 才能成立。

## 4. 第三维：Runtime / Lifecycle Role

同一 semantic owner 可以在不同阶段被消费，生命周期不能反向定义 owner。

至少区分：

| Lifecycle role | 说明 |
|---|---|
| bootstrap / initialization | 建立最小 Consumer Repository Authority 和 local capability |
| adoption | 首次采用 reusable baseline |
| baseline upgrade | 显式比较 upstream candidate 与 current local state |
| ordinary runtime | 常规项目工作时的当前资源 |
| JIT execution | 进入某个真实职责时按需加载 |
| verification / review | 只在验证 / 复核条件命中时读取 |
| historical / evidence only | 不参与 Current Runtime Authority |

关键边界：

- `using-agentic-dev.md` 可以在 initialization / upgrade 中完整读取，但不因此成为 ordinary runtime Authority；
- Skill 通常在真实职责命中时 JIT load；
- Consumer-local Repository Rules 和 Project Authority 可以是 ordinary runtime Current Resource；
- rejected upgrade decision 和历史 eval 默认不进入普通 Fresh Context。

## 5. 第四维：Representation / Authority Form

物理形式描述“如何承载”，不直接说明“谁拥有语义”。

可能形式包括：

- Method / Principle document；
- Architecture / Contract document；
- `SKILL.md` + references / scripts / templates；
- Engineering Discipline / Profile document；
- Repository Policy / Standard document；
- Requirement / Specification / Architecture / ADR / Roadmap；
- Guide / README；
- configuration / manifest；
- generated projection / index；
- Research / Evidence artifact。

特别规则：

- `engineering-capability-architecture.md` / `skill-contracts.md` 等 Architecture / Contract 可以定义 capability 的身份、边界和准入，但“Architecture / Contract”本身不是一个必须新增的 semantic owner 分类；
- `SKILL.md` 是 Skill 的平台兼容执行载体，不代表普通 Markdown 应强制使用相同 schema；
- generated index / catalog 只能投射 metadata，不取得 semantic body ownership；
- 文件位于 `docs/guides/` 不足以证明它语义上是 Guide。

## 6. Ownership Decision Flow

对任意长期内容按以下顺序判断。

### Step 1 — 这是 Current Authority 还是输入 / Evidence？

如果只是 raw source、Research、历史 Evidence 或一次性分析，归入 Research / Input / Evidence；只有明确 promotion 后继续分类。

### Step 2 — 它是否改变顶层方法？

如果它定义或改变跨项目生命周期、阶段、Authority precedence、完成语义或顶层不变量，进入 Method / Principle。

### Step 3 — 它是否是当前项目事实或长期项目决定？

如果回答“当前项目到底是什么 / 必须做什么 / 已决定什么”，进入 Project / Product Authority。

### Step 4 — 它是否是独立 Agent procedure？

如果具有稳定 trigger、输入、过程、输出、退出 / return / escalation，并可独立组合，先判断是否已由 existing Skill 拥有；只有现有 Skill 无法合理拥有且独立职责成立时才考虑 new Skill。

### Step 5 — 它是否是跨项目 reusable engineering constraint / default / profile？

如果跨项目成立、可被多个 Skill 消费，但缺少独立 task entry / output /调度价值，进入 Reusable Engineering Capability / Discipline / Profile。

### Step 6 — 它是否由当前 Repository 自己决定并预期本地演进？

如果是 Git、语言、术语、授权、集成、本地验证等仓库约束，进入 Repository-local Policy / Standard / Rule。

### Step 7 — 它是否只是解释如何理解 /采用？

如果主要服务人类或 setup / adoption / upgrade explanation，进入 Guide。

如果一个文件同时命中多个 owner，说明文件可能混合多个 semantic body；应在 V3-02 记录 split / move / merge 候选，不为了保留当前文件完整性强行指定单一 owner。

## 7. Existing Skill / New Skill / Discipline / Repository Standard 判定

### 7.1 优先进入 existing Skill 的条件

当规则：

- 只在某个既有 Skill 的职责内有意义；
- 是该 Skill procedure / exit / return / escalation 的必要组成；
- 不需要被多个独立职责作为平级规范消费；

则优先回到 existing Skill 或其 supporting resource，避免创建第二 owner。

### 7.2 New Skill admission

只有同时满足以下核心条件时才进入 new Skill 候选：

1. 独立职责真实存在；
2. 多次 / 多项目复用有证据；
3. trigger 与 Do Not Use 可以稳定描述；
4. 输入、procedure、输出、退出条件明确；
5. 不能被现有 Skill 以薄扩展合理拥有；
6. 独立维护与 JIT load 的收益高于新增 Skill 的 discovery / ambiguity 成本。

否则不得因为“这条规则很重要”“跨职责”“Agent 经常用”而新增 Skill。

### 7.3 Engineering Discipline / Profile 条件

当内容：

- 跨项目成立；
- 描述阶段内部质量约束、技术默认知识或验证关注点；
- 被多个 Skill / Consumer 复用；
- 没有独立 task entry、稳定独立输出或单独调度价值；

则优先作为 Engineering Discipline / Technology Profile / Verification Profile 等 reusable capability。

### 7.4 Repository Standard 条件

当内容的正确值由 Repository 自己决定，且不同 Consumer 可以合理不同，例如：

- Git message / branch convention；
- 语言 / 术语偏好；
- 集成 / review policy；
- 本地授权与验证规则；

则应由 Repository-local Standard / Policy 拥有。upstream 可以提供 bootstrap guidance 或 candidate template，但不持续拥有 Consumer 的 current value。

## 8. Guide Admission Boundary

一段内容只有在主要目标是以下之一时才应保留在 Guide：

- 解释 `agentic-dev` 的能力和边界；
- 帮助人选择采用哪些能力；
- 说明 initialization / adoption / baseline upgrade 的入口；
- 提供不拥有规范语义的 human-facing navigation。

以下内容一旦稳定，不应继续留在 Guide 作为唯一 owner：

- 可执行的 Agent procedure；
- reusable engineering constraint；
- repository-local normative rule；
- product / project fact；
- architecture / contract semantics。

Guide 可以引用这些 owner，但不得复制第二份完整规则正文。

## 9. Consumer Lifecycle 与 Ownership

### 9.1 初始化

初始化 Consumer 时可以完整读取 adoption Guide，并基于当前输入：

- 选择性采用 Method / Skill / Reusable Engineering Capability；
- 生成 Consumer-local Repository Rules，例如 Git、术语 /语言、验证、集成政策；
- 如果存在 raw requirement，分析并形成 Consumer Project Authority；
- 如果没有需求，不制造空权威产物。

### 9.2 采用后

完成 adoption 后：

- Consumer-local rules 和 Authority 由 Consumer 自己演进；
- ordinary runtime 只依赖 Consumer-local Current Resource；
- upstream baseline 更新不会自动改变 Consumer 行为。

### 9.3 Baseline upgrade

显式 upgrade 可以临时重新读取 upstream Guide / Method / Skill / reusable capability；完成逐项 adopt / retain-or-override / reject / supersede 后，再次退出 upstream ordinary dependency。

## 10. Semantic Body 单点 Ownership

对同一个规范语义，只允许一个 Current semantic body owner。

其他资源只能：

- 引用 owner；
- 保存最小 routing metadata；
- 保存 provenance；
- 保存必要的 trigger / locator；
- 作为 generated projection。

不得通过 Guide、Index、Skill reference、README、AGENTS 或 Manifest 再复制第二份会独立演进的正文规则。

如果当前存在重复正文，V3-02 必须选择：

```text
keep one owner
+ replace duplicates with pointer / projection
+ mark superseded / historical state
```

## 11. Supersede / Migration / Deletion 最小语义

任何 ownership 迁移至少记录：

- old owner / location；
- new owner / location；
- semantic body 是否迁移、合并或删除；
- old resource 是 superseded、historical 还是仍保留 human explanation；
- ordinary runtime 是否仍能发现唯一 Current owner；
- 是否有 derived index / catalog / pointer 需要同步或淘汰。

不允许仅复制新文件后保留旧规范正文继续被当作 Current。

## 12. 代表资源判例

| 当前资源 | Semantic owner 判断 | Scope / Lifecycle | V3-02 候选动作 |
|---|---|---|---|
| `docs/method/ai-development-method.md` | Method / Principle | reusable-upstream；方法权威 | 保留 |
| `skills/technical-plan/SKILL.md` | Skill / Procedural Capability | reusable-upstream；JIT | 保留；不把 ADR / architecture procedure复制到 Guide |
| `skills/execute-unit/SKILL.md` | Skill / Procedural Capability | reusable-upstream；JIT | 保留；工程纪律只保留薄消费边界 |
| `docs/architecture/engineering-disciplines.md` | Reusable Engineering Capability / Discipline / Profile | reusable-upstream；按条件 ordinary runtime | 保留为 reusable capability owner |
| `docs/technology-profiles/vue3-typescript.md` | Reusable Engineering Capability / Discipline / Profile | reusable-upstream；选择性 adoption | 保留为 Technology Profile |
| `docs/architecture/technology-profile-contract.md` | 定义 reusable capability 的 Architecture / Contract form | reusable-upstream；能力治理 | 保留为 Profile contract；不误判为 Consumer Project Authority |
| `docs/guides/git-commit-guidelines.md` | Repository-local Policy / Standard / Rule | 当前主要约束 `agentic-dev`；Consumer 应本地化 | 从 Guide 身份迁出候选；Consumer 初始化后形成 local rule |
| `docs/guides/terminology-guidelines.md` | Repository-local Policy / Standard / Rule | `agentic-dev` 本地表达治理；Consumer 可选择采用 | 从 Guide 身份迁出候选；概念职责仍由 Method / Architecture / Contract 定义 |
| `docs/guides/using-agentic-dev.md` | Guide 为主，但当前文件含混合正文 | human + initialization / adoption / upgrade | 保留 adoption / explanation；runtime procedure / local rule 分流 |
| `docs/guides/verification-evidence-rules.md` | 文件级不可单类化 | reusable verification constraints；按 condition 激活 | V3-02 按 rule family 判断 existing Skill / reusable capability / principle / platform owner |
| `docs/guides/external-operation-guidelines.md` | 文件级不可单类化 | 同时包含 reusable constraint、repository authorization、platform operation 与 explanation | V3-02 按 semantic body 拆分 owner；不直接整体改名即结束 |
| Consumer Requirement / Specification | Project / Product Authority | consumer-native；ordinary runtime | 保持 Consumer-local Authority |
| v3 GPT-6 raw result | Research / Input / Evidence | historical-evidence | 不进入 ordinary runtime；只把通过治理流程后的结论提升到正式 owner |

这些判例只验证 ownership decision matrix 的可用性，不在 V3-01 执行物理迁移。

## 13. 反例检查

以下推理全部判定为错误：

```text
Agent 会读 → 应该是 Skill
跨项目可复用 → 应该是 Skill
不属于 Method → 应该放 Guide
位于 docs/guides → 语义上就是 Guide
需要按条件激活 → 必须有独立 Skill
来自 agentic-dev → Consumer ordinary runtime 应持续读取 upstream
来自外部资料 → 自动成为 Requirement Authority
有 YAML Front Matter → 自动成为 Current Authority
```

## 14. V3-01 Gate

V3-01 只有在以下条件同时成立时完成：

1. 独立 reviewer 可以基于本文对代表资源做出基本一致的 owner 判断；
2. Engineering Discipline / Profile 不再被误判成 Skill 或 Repository-local Rule；
3. Repository-local Rule 与 reusable upstream capability 的边界可解释；
4. Guide admission 不再承担 catch-all 作用；
5. mixed document 能够被识别为“按 semantic body 拆分”，而不是被迫文件级单分类；
6. 不存在未解决的阻塞或中等级 ownership ambiguity。

达到 Gate 只允许开始 V3-02 的 ownership audit；不自动授权物理迁移、Skill 重构或 discovery implementation。
