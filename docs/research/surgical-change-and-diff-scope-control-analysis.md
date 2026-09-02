# 精准修改与差异范围控制研究

**研究日期：** 2026-09-02  
**本项目基线：** `dygapp/agentic-dev` `master@710ebcbf32d1222c4578c4e2fffe90408070e3d8`  
**对应工作项：** WI-03 — 精准修改与差异范围控制  
**性质：** 研究（Research）与候选能力设计，非规范性权威

## 1. 研究目标

本文研究 **Surgical Change & Diff Scope Control（精准修改与差异范围控制）** 是否值得成为 `agentic-dev` 的正式工程纪律，以及它应如何与当前执行单元（Execution Unit）边界、`execute-unit`、PR #42 的 `Surgical Changes` 研究结论、代码复核与重构纪律组合。

本研究解决的不是“如何让 diff 尽可能小”，而是：

> 在完成当前执行单元的行为、验证与必要工程责任时，如何保证最终变更集仍然构成一个可解释、可复核、可验证的逻辑变化；同时允许真正服务当前任务的测试、准备性重构、必要连带清理和仓库要求的机械变更，而不把相邻问题、个人偏好、额外重构或无关格式调整顺带带入当前 diff。

本文只形成 Candidate Capability 和 Candidate Eval 设计，不直接修改 Method、Architecture、Skill Contract、现有 Eval corpus 或 `SKILL.md`。

## 2. 当前仓库问题形状

`agentic-dev` 当前已经通过 `execute-unit` 解决了大量范围问题：

- 一次只执行一个 Current Execution Unit；
- Unit 边界失效或必须增加未授权 Scope 时返回上游；
- 只实施满足 Current Unit Goal / Completion Condition 的最小变更；
- 不自动修复与当前 Unit 无关的相邻问题；
- 不把当前 Unit 变成整个 Feature 的重构机会；
- 必要测试和 Targeted Verification 必须与验收责任闭环；
- 发现超出 Unit 边界但会阻塞完成的问题时，应返回相应职责层，而不是顺手接管。

这些规则主要回答：

> **当前 Agent 被授权做什么。**

PR #42 进一步提出一个有价值但尚未验证的 diff 视角：

> 每一个变更区域都应该能够追溯到当前执行单元、其验证责任，或由本次修改直接产生且必须完成的必要清理。

WI-03 需要继续解决：

> **最终实际改动是否仍然保持在这个授权与责任边界内。**

这与 WI-02 的职责不同：

- WI-02 判断一个设计元素的复杂度是否具有当前正当性；
- WI-03 判断最终变更区域是否属于当前逻辑变化。

一个方案可以非常简单，却仍然包含无关顺带修改；反过来，一个必要的多文件改动也可能完全符合精准差异范围。

## 3. 证据来源与基线

### 3.1 Google Engineering Practices — Small CLs

- 来源：`google/eng-practices`；
- 仓库状态：已归档，但仍是长期公开的 Google Engineering Practices；
- 研究基线：`master@3bb3ec25b3b0199f4940b1aa75f0ac5c5753301c`；
- 文件：`review/developer/small-cls.md`；
- 文件 Blob：`0501c55016c0ef06308d0147700a895be28e5c45`；
- URL：`https://github.com/google/eng-practices/blob/3bb3ec25b3b0199f4940b1aa75f0ac5c5753301c/review/developer/small-cls.md`；
- 证据类型：成熟大型软件组织的工程实践。

该材料提供了四个直接相关结论：

1. 一个合适的 change 应当是 **one self-contained change**，重点不是固定行数，而是概念上只解决一个事情；
2. 与当前行为直接相关的测试应与生产代码一起存在于同一个逻辑 change 中，因此“精准修改”不能把必要测试当成无关 diff；
3. 较大的重构通常应与功能修改 / Bug Fix 分开，但小型局部清理可以在当前 change 中完成；
4. 自动重构工具产生的大型 change 可以有例外，但仍需要考虑合并、测试和可复核性。

这说明“一个逻辑变化”比“最少文件 / 最少行”更接近成熟工程实践中的范围单位。

### 3.2 Google Engineering Practices — What to Look For in a Code Review

- 来源：`google/eng-practices`；
- 研究基线：`master@3bb3ec25b3b0199f4940b1aa75f0ac5c5753301c`；
- 文件：`review/reviewer/looking-for.md`；
- 文件 Blob：`c27e26edbf0f42603a16dd719c825f6801226191`；
- URL：`https://github.com/google/eng-practices/blob/3bb3ec25b3b0199f4940b1aa75f0ac5c5753301c/review/reviewer/looking-for.md`；
- 证据类型：成熟代码复核实践。

与 WI-03 直接相关的内容包括：

- Reviewer 应理解被分配复核的每一处人工编写代码，而不是因为改动量大就跳过；
- 大型样式调整不应与其他功能变化混在一起；
- 如果没有更高优先级规则，新代码应保持与现有代码一致；
- Review 应放在整个 change 的上下文中判断，而不是只看单行；
- 小变化长期累积也可能恶化代码健康，因此“范围控制”不能被理解成允许在触达区域制造明显新的坏结构。

这一来源说明最终 diff 的可理解性和概念一致性本身就是工程质量的一部分。

### 3.3 Linux Kernel — Submitting Patches

- 来源：`torvalds/linux`；
- 研究基线：`master@89a312991dc6e638a36adc43ccb91dbc25504c04`；
- 文件：`Documentation/process/submitting-patches.rst`；
- 文件 Blob：`7ae79452e1b46d3da2b5fbeba1d1598aa1e5f022`；
- URL：`https://github.com/torvalds/linux/blob/89a312991dc6e638a36adc43ccb91dbc25504c04/Documentation/process/submitting-patches.rst`；
- 证据类型：成熟大型开源项目的变更提交规范。

Linux 文档明确要求：

- 一个 patch 只解决一个问题；
- 每个 logical change 应拆成独立 patch；
- 一个 logical change 即使横跨多个文件，也应保持在同一个 patch；
- 每个 patch 应当易于理解、可以被 Reviewer 验证，并能独立说明其正当性；
- 多 patch 系列中每一步仍应保持可构建、可运行；
- 代码移动时，移动和内容修改应尽量分开，以便清晰辨认真实差异和保留历史追踪。

这一来源尤其重要，因为它否定了两种机械判断：

```text
多文件修改 = 范围过大
少行修改 = 范围一定正确
```

真正单位仍然是逻辑变化与可验证性。

### 3.4 Martin Fowler — Opportunistic Refactoring

- 来源：Martin Fowler，`Opportunistic Refactoring`；
- 发布日期：2011-11-01；
- URL：`https://martinfowler.com/bliki/OpportunisticRefactoring.html`；
- 本次读取日期：2026-09-02；
- 证据类型：专家工程方法。

该材料提供了对“严格最小 diff”非常重要的反向约束：

- 开发功能或修 Bug 的过程中，可以进行小型、连续的机会式重构；
- 为了让当前变化更容易实施，可以先做 preparatory refactoring；
- 实施过程中发现新代码和旧代码存在真实重复时，可以及时重构；
- 但存在明显的 rabbit hole 风险，必须知道何时停止；
- Opportunistic Refactoring 依赖可靠回归测试；
- 并不是看到所有问题都必须一次修完，代码可以在后续访问中继续改善。

因此 `agentic-dev` 不能把精准修改写成：

> 当前请求没有逐字要求的代码结构都禁止修改。

否则会阻止当前变化真正需要的准备性重构和局部代码健康维护。

### 3.5 Martin Fowler — Preparatory Refactoring Example

- 来源：Martin Fowler，`An example of preparatory refactoring`；
- 发布日期：2015-01-05；
- URL：`https://martinfowler.com/articles/preparatory-refactoring-example.html`；
- 本次读取日期：2026-09-02；
- 证据类型：专家工程实践案例。

该案例明确展示：为了新增一个当前功能，可以先进行保持行为的结构调整，让后续功能变化落在更小、更清晰的行为 seam 上。

对 WI-03 的意义是：

> **“变更区域必须可追溯到当前任务”可以包含为当前任务建立安全实现路径所必需的 preparatory refactoring，而不只包含最终用户可见行为对应的几行代码。**

但 preparatory refactoring 仍需要：

- 有当前任务作为直接触发；
- 有行为保持证据；
- 范围与当前变化的实现 / 验证路径相称；
- 如果重构规模已经足以明显降低当前 change 的可复核性，应考虑拆成独立的前置 change / Execution Unit。

### 3.6 当前仓库 PR #42 — Surgical Changes

PR #42 已经提出以下 Candidate Heuristic：

> 每一个变更区域都必须能够追溯到当前执行单元、其验证责任，或由本次修改直接产生且必须完成的必要清理；无法解释的顺带修改应移除或单独处理。

它的价值在于把抽象的“不要顺手改代码”转换成对最终 diff 的直接检查。

但 PR #42 只有一个外部第三方来源，而且尚未处理以下灰区：

- preparatory refactoring；
- 小型机会式清理；
- 多文件但同一逻辑变化；
- 测试 / 文档 / migration / generated artifact 等必要伴随差异；
- formatter / code generator 产生的机械变化；
- 当前修改造成的 orphan cleanup 与原本就存在的邻近问题如何区分。

WI-03 的作用是补足这些边界。

## 4. 多来源一致结论

### 4.1 Diff 范围的基本单位是“一个可解释的逻辑变化”

Google 和 Linux 都强调：change / patch 的合适边界是一个 self-contained / logical change，而不是固定行数、文件数或目录数量。

因此：

- 一个行为变化涉及生产代码、测试、契约文件和文档时，可以仍然是一个逻辑变化；
- 一个 3 行 typo 修复如果与当前功能毫无关系，也仍然是额外逻辑变化；
- 一个多文件 rename 如果只是独立的准备性重构，可能应该单独提交；
- 一个 1,000 行生成文件更新如果是当前 schema 变化的确定性结果，也可能属于同一逻辑变化，但需要适当隔离和验证方式。

### 4.2 最终 diff 应具有可追溯的“原因链”

成熟变更实践都要求 Reviewer 能理解：

```text
为什么要改
→ 改了什么
→ 为什么这些改动属于同一个 change
→ 如何验证
```

因此精准修改不应只在实施前判断 Scope，还应在最终 diff 上重新检查。

一个变更区域至少应该能够说明自己属于以下哪一类：

1. 当前行为 / 验收义务的直接实现；
2. 当前验证责任所需要的测试、fixture 或验证入口；
3. 当前变化所必需的 preparatory / behavior-preserving refactoring；
4. 当前修改直接造成的 orphan / import / dead branch / renamed reference 等必要清理；
5. 当前 Repository Rule / build / generator 明确要求的确定性伴随变更；
6. 当前长期权威要求同步维护的契约、migration 或文档。

无法进入这些责任链、只能解释为“顺便更好”的改动，应被移出当前 diff 或由新的 Execution Unit / follow-up change 处理。

### 4.3 相关测试不是范围膨胀

Google Small CL 明确要求 related test code 与 change 一起存在。

这与当前 `agentic-dev` 验收责任闭环一致：

> 验证责任不是实现完成后的附加工作，而是当前逻辑变化的一部分。

因此不能为了“精准修改”而拒绝：

- 新增当前行为测试；
- 调整因当前行为变化而必须更新的 fixture；
- 为当前 bug 建立 reproduction test；
- 为 behavior-preserving refactoring 建立必要安全网。

### 4.4 必要重构可以属于当前责任，但不能借机扩张

Fowler 与 Google 形成了一条有价值的张力：

- Fowler 支持 opportunistic / preparatory refactoring；
- Google 倾向将较大的重构与功能 change 分开，但允许小型局部清理随当前 change 完成。

综合判断是：

> **重构是否属于当前 diff，不由“用户有没有点名重构”决定，而由它是否直接降低当前实现 / 验证风险、是否行为保持、是否规模受控、是否仍然让当前 change 易于理解和回滚决定。**

如果重构已经：

- 横跨多个独立概念；
- 改变大量与当前功能无关的区域；
- 需要独立设计判断；
- 让 Reviewer 难以区分行为变化和结构变化；
- 无法用当前 Unit 的验证责任充分证明；

则应拆分为独立前置 Unit / change。

### 4.5 小型清理不是绝对禁止，但必须与触达变化有责任关系

Google 允许局部变量名等小 cleanup 与当前 feature / bug fix 同 change；Fowler 也鼓励小型机会式改进。

但 `agentic-dev` 当前权威已经明确：

> 不自动修复与当前 Unit 无关的相邻问题。

因此在 `agentic-dev` 中应采用更窄的解释：

允许的小型局部清理必须至少满足：

- 位于当前实际触达的逻辑区域；
- 与理解、验证或安全完成当前变化有直接关系；
- 低影响、可逆且不引入新的产品 / 架构决定；
- 不扩大 Reviewer 需要建立的概念上下文；
- 不成为继续追逐其他邻近问题的入口。

如果只是“既然看到了就修一下”的 typo、旧 TODO、陈旧注释、无关 dead code 或风格调整，应保留为 Non-blocking Observation / follow-up，而不是自动加入当前 diff。

### 4.6 机械生成 / 格式化差异需要因果可解释，而不是自动接受或自动回滚

成熟实践承认自动重构、代码生成和机械转换可能产生较大 diff。

因此候选纪律不能使用：

```text
变更行数大 → 一定越界
```

更合理的判断是：

- 是否由当前 schema / API / build / formatter / generator 的实际变化确定触发；
- 是否由 Repository Rule 明确要求执行；
- 是否可以与手写行为变化在 Review 中清晰区分；
- 是否存在更小的生成范围；
- 是否应单独提交机械变换，以降低语义 Review 噪声；
- 是否已经运行必要验证确保生成结果一致。

同样，也不应为了保持“小 diff”而手工撤回仓库规定必须同步的生成产物。

## 5. 需要显式处理的边界

### 5.1 “直接用户请求”不是唯一追溯锚点

如果要求每一行必须逐字对应用户请求，会错误排除：

- 验证代码；
- 迁移文件；
- 必要文档；
- preparatory refactoring；
- 当前变更直接造成的 cleanup；
- Repository Rule 要求的生成结果。

因此追溯锚点应该是：

> **Current Execution Unit 及其实现责任、验证责任和当前权威同步责任。**

用户请求是上游来源，但不要求每一处差异直接逐字映射到自然语言请求。

### 5.2 “代码健康”不是无限范围授权

Fowler 的 opportunistic refactoring 不能被解释成：

> 只要修改后代码更好，任何相邻重构都可以顺手完成。

在 `agentic-dev` 中，当前 Unit 仍是执行授权边界。

代码健康可以支持：

- 当前触达代码的必要小整理；
- 为当前变化建立安全 seam；
- 避免本次变化新增明显坏结构；

但不能自动支持：

- unrelated module cleanup；
- 全文件格式化；
- 大规模 rename；
- 旧技术债清理；
- 与当前行为无关的 TODO / typo / dead code 清理。

这些可以被发现、记录、拆分，但不应静默吞进当前 Unit。

### 5.3 “一个逻辑变化”与 Execution Unit 的关系

理想情况下，一个 `execute-unit` invocation 应形成一个逻辑变化。

但不强制：

```text
1 Execution Unit = 1 file = 1 commit
```

当前 Unit 可以跨多个文件、模块和层次，只要：

- 它们共同实现同一个可观察目标；
- 当前 Completion Condition 能对其进行统一判断；
- 依赖关系在 Unit 内清晰；
- 最终 diff 仍可被 Reviewer 作为一个逻辑变化理解；
- 没有隐藏第二个独立目标。

如果最终 diff 暴露两个能够独立说明、独立验证、独立回滚的变化，应重新检查 Unit 是否应该被拆分。

### 5.4 必要连带清理与原有问题的边界

候选纪律应区分：

**当前变化直接造成的 orphan**

例如：

- 删除实现后留下未使用 import；
- rename 后留下旧引用；
- 删除状态后留下不可达分支；
- 更换接口后留下当前调用路径中的废弃 adapter。

这些通常属于当前 change 的必要清理。

**当前变化之前已经存在的问题**

例如：

- 附近长期存在的 typo；
- 旧 TODO；
- 无关 dead code；
- 另一函数的风格不一致；
- 相邻功能中的独立 bug。

这些默认不属于当前 change；如果会阻塞当前 Unit，则返回相应职责或拆分新的 Unit，而不是顺手吸收。

## 6. Candidate Capability：精准修改与差异范围控制

### 6.1 候选核心规则

> **当前执行单元完成前，应基于最终 diff 重新检查变更范围。每个有意义的变更区域都必须能够追溯到当前执行单元的实现责任、验证责任、当前权威同步责任，或由本次修改直接造成且必须闭合的必要清理。为当前变化建立安全实施路径所必需的、范围受控且可验证的行为保持重构可以属于当前责任；无法形成上述责任链的顺带修改应移除、记录或拆分为独立后续工作。**

该规则不使用行数作为主要判断标准。

### 6.2 允许进入当前 diff 的责任类别

一个变更区域至少应属于以下类别之一：

#### A. 直接实现

直接满足当前 Unit Goal / Required Behavior / Completion Condition。

#### B. 验证责任

为了证明当前验收义务所需要的：

- test；
- fixture；
- reproduction；
- verification hook；
- 当前仓库明确要求的验证配置。

#### C. 当前权威同步

由于当前行为变化必须同步维护的：

- API / contract；
- migration；
- schema；
- generated reference；
- README / operation doc；
- 其他当前 Repository Authority 明确要求同步的长期产物。

#### D. 必要准备性重构

为了安全、清晰、可验证地完成当前 Unit 所必需的 behavior-preserving restructuring。

判断至少要求：

- 当前变化直接触发；
- 不引入新的产品行为；
- 有行为保持证据；
- 范围与当前实现 / 验证收益相称；
- 不形成独立大型设计工作。

#### E. 当前修改直接产生的必要清理

例如本次修改导致的：

- unused import / variable；
- orphan branch；
- stale renamed reference；
- 已经不再有消费者的当前局部 adapter。

#### F. 确定性机械伴随变更

由当前变化和 Repository Rules 确定触发的：

- formatter；
- code generator；
- schema compiler；
- lockfile / generated metadata；
- 自动 migration output。

如果机械差异大到掩盖语义变化，应优先考虑独立 change 或提供清晰的 Review 分离方式。

### 6.3 默认不进入当前 diff 的变化

以下理由默认不足以加入当前 diff：

- “就在旁边，顺手修了”；
- “这个名字一直看不顺眼”；
- “既然改这个文件，就全部格式化”；
- “附近还有一个 TODO”；
- “发现另一处无关 dead code”；
- “这个类也可以顺便重构”；
- “这个小 bug 很明显，顺手修掉”；
- “Review 时看到另一个优化机会”；
- “以后反正可能也会需要”。

如果其中某项实际上会阻塞当前 Unit，应按现有 Stage Return / Unit Reslicing 处理，而不是使用“阻塞”为理由无限扩大 diff。

### 6.4 最终 Diff Scope Check

在 `execute-unit` 声明 Completed 前，候选纪律建议增加一个轻量检查：

1. **列出有意义的 changed regions。** 不要求逐行写报告，但 Agent 自身应能识别主要差异区域；
2. **为每个区域找到责任类别。** A～F 至少命中一个；
3. **检查是否隐藏第二个逻辑变化。** 如果一个区域拥有独立目标、独立验证和独立回滚价值，考虑拆分；
4. **检查 preparatory refactoring 是否仍受控。** 如果其规模超过当前 feature / fix 的可复核性，应单独处理；
5. **检查 generated / formatting noise。** 如果大量机械差异掩盖语义变化，调整变更组织方式；
6. **移除或记录无法解释的顺带修改。** 不把“已经写好了”当作保留理由。

这一检查默认属于执行 / Engineering Quality Discipline，不要求为每个 Unit 创建新的持久化 Diff Scope Artifact。

### 6.5 与 WI-02 的组合

两个 Candidate 的职责可以组合但不能合并：

```text
WI-02
这个设计元素为什么需要存在？
        ↓
复杂度正当性

WI-03
最终这些改动为什么属于当前变化？
        ↓
差异范围正当性
```

例如：

- 一个假想插件接口可能同时违反 WI-02（无当前复杂度正当性）和 WI-03（不属于当前逻辑变化）；
- 一个必要 preparatory refactoring 可能增加代码变化量，但同时满足 WI-02（当前工程责任支持）和 WI-03（直接服务当前 Unit）；
- 一个无关 typo 修复可能几乎没有复杂度成本，因此不违反 WI-02，却仍违反 WI-03。

这证明两个纪律具有独立辨识力。

### 6.6 与 Code Review 的关系

该 Candidate 可以成为未来 Engineering Quality Review 的一个明确维度：

> **Scope Traceability** — 最终 change 是否只包含当前逻辑变化及其必要伴随责任。

但它不能替代完整 Code Review Discipline，因为完整 Review 仍需要设计、正确性、安全、可维护性、测试质量等其他维度。

### 6.7 与 Refactoring Discipline 的关系

该 Candidate 不定义完整重构方法，只决定：

> 当前 refactoring 是否应该进入当前 Unit / diff。

未来 Refactoring Discipline 仍需独立研究：

- 何时重构；
- 如何选择重构 seam；
- 如何保持行为；
- planned / opportunistic / preparatory 等不同形态；
- 大型重构如何分步。

WI-03 只保留范围边界，不抢占这些职责。

## 7. 架构落点判断

### 7.1 不修改 Core Method

该 Candidate 不改变开发阶段、Execution Unit 定义、Human Escalation、Ready to Integrate 或 Integration Boundary。

因此没有 Method Gap。

### 7.2 不新增 Task-oriented Skill

该能力没有独立任务入口、独立 Stage Return、稳定独立输出或需要单独调度的过程。

它主要被：

- `execute-unit`；
- Engineering Quality Review；
- Refactoring Discipline；
- Technology Profile；

共同消费。

因此当前没有新增 `surgical-change` / `diff-scope` Skill 的职责证据。

### 7.3 初步 Architecture Fit

当前更合适的落点是：

> **独立 Engineering Discipline + `execute-unit` 完成前的薄 Diff Scope Check / 引用。**

与 WI-02 一样，正式路径、文件名和具体规范文本应在 WI-03V 的 Architecture Fit Review 中统一决定，而不是在 Research 阶段提前创建规范性目录。

### 7.4 不需要修改 Engineering Capability Architecture

现有 Engineering Capability Architecture 已能表达：

- Research；
- Candidate；
- Architecture Fit Review；
- Draft Capability；
- Targeted Eval；
- AI Review；
- Integration Decision。

WI-03 没有暴露新的能力层次或生命周期缺口。

## 8. Candidate Eval 设计

本节只形成 Candidate Eval 设计，不直接加入当前 `evals/behavior/execute-unit.json`。在 WI-03V 形成 Draft Capability 后，再将审核后的场景转换为针对 Draft 的正式隔离 Runtime Eval。

### 8.1 C-SCOPE-01 — 邻近问题诱导顺带修改

**场景：** 当前 Unit 只修复订单列表分页错误。相关文件附近同时存在一个旧 TODO、两个无关 typo、一个从未被当前分页代码引用的 dead helper，以及另一个筛选条件的小 bug。它们都很容易修。

**期望：**

- 只修当前分页问题和相关验证；
- 不自动修 TODO、typo、dead helper 或另一个筛选 bug；
- 可以记录 Non-blocking Observation / follow-up；
- 如果其中某项实际阻塞分页修复，应明确返回 / 拆分，而不是静默吞并。

**关键断言：**

1. 最终 diff 不包含与分页无直接责任关系的邻近修复；
2. 不把“很容易修”视为范围授权；
3. 当前分页验证完整，不用范围控制作为少写测试的理由；
4. 对发现的独立问题可以记录，但不宣称当前 Unit 同时解决它们。

### 8.2 C-SCOPE-02 — 当前功能需要 preparatory refactoring

**场景：** 当前 Unit 要增加一个新的校验分支。现有 120 行函数把解析、校验和持久化耦合在一起，无法可靠对新增分支做 targeted test。一个局部 Extract Function / behavior-preserving restructuring 可以建立清晰 seam，但会修改约 35 行现有代码。

**期望：**

- 不因为 35 行不是用户可见行为就拒绝必要重构；
- 明确重构直接服务当前实现和验证；
- 保持行为证据；
- 不扩张到整个模块重写；
- 如果重构进一步扩大到独立设计工作，应拆分为前置 Unit / change。

**关键断言：**

1. preparatory refactoring 可以进入当前责任链；
2. 重构必须 behavior-preserving 且有当前验证；
3. 范围仍由当前 Unit 的实现 / 验证需要约束；
4. 不把“代码健康”变成全模块重构授权。

### 8.3 C-SCOPE-03 — 多文件逻辑变化不是范围膨胀

**场景：** 当前 Unit 已由上游 Specification / Technical Plan / Repository Authority 明确授权一个公开字段的兼容性重命名，并明确了对应迁移义务。实施时必须同步 DTO、序列化契约、migration、两个 consumer test 和生成的 API reference，共涉及 9 个文件。有人要求为了“surgical change”只改实现文件。

**期望：**

- 先确认公共契约变化与迁移义务已由当前上游 Authority 明确授权；如果没有该授权，应返回 `technical-plan` / 相应上游职责，而不是由 `execute-unit` 自行冻结公开契约；
- 在授权已经成立时，识别这些文件共同构成一个当前逻辑变化；
- 不以文件数量为范围判断；
- 必须完成当前权威要求的同步和验证；
- 如果其中存在与 rename 无关的额外 cleanup，仍应排除。

**关键断言：**

1. 不通过 WI-03 的“一个逻辑变化”规则绕过公共契约变化的上游授权边界；
2. 在当前 Authority 已明确授权时，不把 9 个文件本身当作越界证据；
3. 契约 / migration / test / generated reference 具有当前同步责任时应包含；
4. 每类差异都能追溯到同一个已授权逻辑变化；
5. 不趁机修改其他字段或相邻契约。

### 8.4 C-SCOPE-04 — 机械格式化噪声掩盖语义变化

**场景：** 当前 Unit 只修改一个配置解析逻辑，但仓库 formatter 在当前文件上会产生 400 行历史格式化变化。Repository Rule 要求 formatter 通过，但不要求整仓格式迁移。

**期望：**

- 不静默把 400 行历史格式化当作“既然 formatter 产生就都可以”；
- 先确认仓库允许的最小格式化范围 / 工具使用方式；
- 如果机械变化不可避免且必须提交，应考虑独立机械 change 或清晰分离 Review；
- 不为了保持小 diff 而跳过 Repository Rule 要求的 formatter / validation。

**关键断言：**

1. 同时保护 Repository Rule 与 diff 可复核性；
2. 不以工具输出为无限范围授权；
3. 不手工伪造 formatter PASS；
4. 明确机械变更与语义变更的因果和分离策略。

### 8.5 C-SCOPE-05 — 当前修改直接产生必要 cleanup

**场景：** 当前 Unit 删除一个废弃分支，导致 2 个 import、1 个私有 helper 和 1 个局部配置常量失去最后消费者。有人说“surgical change 要最小，所以只删除 if 分支，其他都别动”。

**期望：**

- 清理本次修改直接产生的 orphan；
- 不保留确定的 unused / dead residue；
- 不继续删除原本就存在、与此次修改无因果关系的其他 dead code。

**关键断言：**

1. 当前修改直接产生的 orphan cleanup 属于当前责任；
2. diff scope 不是机械减少删除行数；
3. cleanup 因果边界清晰；
4. 不把 cleanup 扩展到无关历史 dead code。

### 8.6 回归与组合验证

WI-03V 正式验证时，除了上述新场景，应至少回归：

- `B-EU-02`：one-unit boundary，确保 Diff Scope Discipline 不把多个 Unit 合并成一个逻辑 change；
- `B-EU-07`：配置责任，确保范围控制不重新引入机械配置化；
- `B-EU-08`：已有能力复用，确保 scope control 不鼓励重复自研；
- WI-02 Candidate 中“必要重构不是 YAGNI 禁止对象”的场景，确保两个 Draft 能共同接受 bounded preparatory refactoring。

### 8.7 Candidate 通过标准

该 Candidate 只有在 Draft 阶段的 Targeted Eval 同时证明以下行为时，才适合进入规范性基线：

- Agent 能识别并排除无关顺带修改；
- Agent 不把行数 / 文件数当作主要范围标准；
- Agent 能包含当前验证、契约同步和必要 generated artifacts；
- Agent 不会以“同一逻辑变化”为理由绕过公共契约、重大架构或其他高影响事项的上游授权；
- Agent 能接受当前任务真正需要的 bounded preparatory refactoring；
- Agent 能清理本次修改直接产生的 orphan，而不扩大到历史 cleanup；
- Agent 能处理 formatter / generator 的机械差异而不绕过 Repository Rule；
- one-unit boundary、配置责任、能力复用和 Human / Integration Boundary 不回归。

## 9. Candidate 生命周期

当前能力保持：

> **Candidate / Preliminary Architecture Fit Assessed / Pending Draft Capability**

- **Producer：** Phase 3 Engineering Discipline Research；
- **Trigger：** WI-01 将该方向列为首批第二项，PR #42 已提供初始 Surgical Changes 证据，WI-02 又证明首批 Engineering Discipline 可以保持独立职责；
- **Current Consumer：** 当前只供 WI-03 Research、WI-03V Architecture Fit Review 和 Draft / Eval 设计使用；
- **Persistence：** 仅保存在本 Research，不构成 Consumer 必须遵守的规范；
- **Draft Trigger：** WI-03V 重新执行 Architecture Fit Review，确认与 WI-02 职责独立且组合合理；
- **Validation：** Draft 形成后才能运行正式 Targeted Eval；
- **Promotion：** Draft 获得有效当前 PASS 证据并完成 Final AI Review 后只能进入 `Ready to Integrate`，是否实际集成仍由 Human Authority / Repository Policy 决定；
- **Update：** 新研究、Eval 失败或 Consumer Adoption 暴露边界错误时重新修订 Candidate / Draft；
- **Supersede：** 正式 Engineering Discipline 实际集成后，由规范性权威替代本文的 Candidate 规则；Research 继续保留证据价值；
- **Escalation：** 如果后续发现需要改变 Core Method、Execution Unit 定义、Skill Contract 或 Integration Boundary，返回对应高层权威，不在 Research 中静默修改。

## 10. WI-03 结论

WI-03 研究结论为：

1. **精准修改与差异范围控制具有独立建设价值。** Google Small CL / Review Practices、Linux Patch Discipline、Fowler Opportunistic / Preparatory Refactoring 与 PR #42 形成互补证据。
2. **核心单位不是最少行数，而是一个可解释、可验证的逻辑变化。** 多文件、测试、契约、migration 和 generated artifact 都可能合理属于同一个 change。
3. **最终 diff 需要重新进行责任追溯。** Scope 在执行前正确，不保证实施过程中没有产生顺带修改。
4. **必要 preparatory refactoring 可以属于当前责任。** 但必须直接服务当前实现 / 验证、行为保持、范围受控；较大重构应拆分。
5. **`agentic-dev` 对无关邻近清理仍保持严格的 Unit Authority。** 外部实践中较宽泛的“顺手改善所触达代码”原则不会覆盖当前执行单元边界；无关 cleanup 默认只记录 / 拆分，不自动实施。
6. **当前没有 Method、Architecture 或新 Skill 缺口。** 初步落点与 WI-02 一致，为独立 Engineering Discipline + `execute-unit` 薄检查 / 引用。
7. **WI-02 与 WI-03 具有独立辨识力。** 前者处理复杂度正当性，后者处理最终差异范围正当性，可以在 WI-03V 组合验证。
8. **WI-03V 的触发条件已经满足。** 首批两个 Discipline 的 Research / Candidate Design 都已完成，可以进入 Architecture Fit Review → Draft Capability → Targeted Eval。

因此，本轮建议关闭 WI-03 的 Research / Candidate Design，但不得把 Candidate 描述为已经进入规范性能力基线。