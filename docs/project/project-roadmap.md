# 项目演进路线与当前状态

本文是 `agentic-dev` 仓库自身的项目路线图，记录当前有效的项目阶段、已完成里程碑、候选库与下一步边界。

本文属于 `docs/project/*` 项目级权威，不覆盖更高优先级的方法、架构、契约、工程纪律或技术画像权威。使用方项目不会自动继承本文中的 `agentic-dev` 项目事实。

## 1. 路线图使用规则

本文只维护当前有效路线。历史细节由 Git 历史、已关闭 Issue / PR 和对应收尾文档保存，不在路线图中重复维护完整实验流水。

状态语义：

- **已完成**：完成条件已有当前 Git、PR、Issue、评估或复核证据支持；
- **当前**：正在执行的有限里程碑；
- **待人工决策**：上一有限里程碑已经完成，但下一项尚未由人工权威选择；
- **v1 后候选库**：保留为后续候选，但不是当前承诺。

不得因为出现新的外部资料、使用方反馈或有价值候选而静默扩展当前路线。

## 2. 当前阶段

当前长期阶段仍为：

> **工程能力扩展与方法演进**

已经完成的主要有限里程碑：

1. 工程能力基础 v1；
2. 工程纪律扩展 v1；
3. 中文交互与上下文清理 v1；
4. 工程术语语义安全与现行文档全量收敛 v1；
5. Squash Merge 下 Stacked PR 集成拓扑安全 v1；
6. 规则治理与知识激活 v1。

最近完成并已集成的有限里程碑是：

> **规则治理与知识激活 v1**

该里程碑已完成激活审计、最小检索模型、真实隔离 A/B 与人工评分、薄启动 / 规则导航收敛、真实 Consumer 新上下文验证、陈旧派生索引 fail-closed 验证与最终 AI 复核。PR #89 已于 2026-09-09 按最终复核 Head `6a97bdc6d31e4997b89415a8ab4a75f97e6a6022` 通过 squash merge 集成，合并提交为 `4a42d7a23a40e4dbae84c2817b6d30acc1b6aa14`；Issue #73 已按完成关闭。

当前路线状态：**待人工决策**。下一有限里程碑尚未由人工权威选择；WI-07 — 代码复核能力 v1 仍只是优先候选，不自动启动。

2026-09-08，人工权威曾显式选择该有限里程碑；历史跟踪入口：Issue #73。

启动基线：

`master@0895ca30f76c666f3a0d4d9c2f9af6f14cded5d6`

阶段 A“激活审计”已形成 A1～A5 可复核结果，确认当前历史场景既包含纯激活失败，也包含已经由当前仓库权威关闭的历史规则缺口；当前不应继续为相同场景机械新增同义规则。

阶段 B“最小检索模型”已完成：B1 冻结稀疏检索契约，B2 选择 JSON 派生规则索引 + Python 标准库薄查询器，B3 建立 61 项 / 8 个规范性来源的首轮派生索引并验证来源追溯、条件筛选、未知维度与来源陈旧回退、可删除 / 可重建边界。原型仍属于 `evals/` 评估资产，不是新的规则权威，也没有证据要求全库统一增加文件头。

阶段 C“检索 / 激活评估”已完成：C1 冻结 9 个有辨识力场景；C2 建立可重复 A/B runner、Consumer-local / stale-source 控制与分层结果结构；C3 完成 9 个可比较 A/B pair 的真实隔离运行与人工评分。B 直接命中 29 / 29 必需规则，3 个安全回退 reason 全部正确，行为语义 9 / 9 PASS；A 为 8 / 9，并在 RR-C1-02 出现一次误停。阶段 C 已形成进入阶段 D 的收益证据。

阶段 D“权威 / 指南收敛”已完成 D1 / D2：README 已压薄为启动 / 路由入口；新增 `docs/guides/rule-activation-guide.md`，只维护三条跨任务不变量、按职责 / 风险的当前源段落指针和 fail-closed 回退；详细规则仍由现行 Guide / Skill / Repository Authority 单点维护。D2 重新验证 9 个既有 A/B 场景仍可静态装配。PR #88 后续状态闭环修改了 `AGENTS.md` / Roadmap 等项目状态输入；这些变化没有改变 C3 冻结的详细规则语义，但使派生 rule-index 的整文件源身份按设计陈旧。F1 已保留该 fail-closed 结果并重建当前源身份；绑定旧项目阶段 expected behavior 的历史治理评估不机械作为当前状态回归。

阶段 E“使用方验证”已完成 E1：以 `dygapp/jilinjobs-cms` 当前 `main@982a214d65f8ebfa461a6488b89709c2be1a3863` 与 PR #117 Head `547ac9453fd4ca6b85949810f3991d02f172e02f` 做逻辑 Fresh Context 验证，Consumer Authority / Consumer-local Method / 精确 baseline 始终优先；薄导航只激活当前执行、异步外部操作、GitHub Actions 证据与临时证据晋升所需规则，全部 E1 检查 PASS。E2 CodeGraph A/B 为可选项，本轮未执行且不阻塞。

阶段 F 的 F1 最终静态验证已完成：首次运行正确发现 `AGENTS.md` source identity 陈旧并 fail-closed；最终 Run `34325868257` 在完成证据措辞修正、最终源 identity 重建后，9 场景静态检索回归与 E1 证据边界检查全部通过。F3 稳定状态由当前候选同步收敛；F2 最终 AI 复核与人工集成决策属于最终 PR 原生证据，不在 Roadmap 预写结果。

当前没有新的里程碑实施门禁。下一有限里程碑尚未选择；只有规则治理与知识激活 v1 完成集成后才重新进入人工路线决策，WI-07 仍只是优先候选，不自动启动。完整研究和实施边界分别位于：

- `docs/research/knowledge-activation-and-code-intelligence-analysis.md`
- `docs/research/knowledge-activation-evidence-appendix.md`
- `docs/research/minimal-rule-retrieval-contract.md`
- `docs/research/rule-retrieval-prototype-selection.md`
- `docs/research/rule-retrieval-prototype-validation.md`
- `docs/research/rule-retrieval-targeted-evaluation-design.md`
- `docs/research/rule-retrieval-ab-baseline-validation.md`
- `docs/research/rule-retrieval-c3-evaluation-results.md`
- `docs/research/rule-activation-e1-consumer-validation.md`
- `docs/project/rule-governance-knowledge-activation-v1.md`
- `docs/guides/rule-activation-guide.md`
- `tasks/plans/20260908/01-rule-governance-knowledge-activation.md`

WI-06、WI-07、WI-09、第四工程纪律和 Issue #71 均未因本里程碑启动而自动进入实现。**WI-07 — 代码复核能力 v1** 已登记为本里程碑完成后的优先后继方向，但必须在规则治理与知识激活 v1 完成并集成后重新进入人工里程碑决策。

Issue #58 继续作为长期使用方经验反馈入口。

## 3. 当前路线状态

| 路线 | 状态 | 当前边界 |
|---|---|---|
| 核心方法 | 稳定维护 | 只有高质量通用证据揭示生命周期或权威缺口时才定向修改 |
| 规则治理与知识激活 | **已完成并集成** | PR #89 已合并为 `4a42d7a23a40e4dbae84c2817b6d30acc1b6aa14`，Issue #73 已关闭；当前进入下一有限里程碑人工决策 |
| 工程纪律 | 已完成基础建设，可条件扩展 | 当前已有三项正式工程纪律；第四项未启动 |
| 技术画像 | 基础建设已完成，进入候选库 | 技术画像契约与 Vue 3 + TypeScript 画像已完成；WI-06 暂缓，等待代码复核 / 使用方评估暴露真实增量缺口 |
| 使用方采用 | E1 真实使用方验证已通过 | `jilinjobs-cms` 验证保持使用方仓库权威与 Consumer-local Method 优先；CodeGraph E2 本轮未执行，继续只是可选代码智能实验输入 |
| 任务型技能 | v1 后候选库 | WI-07 未启动；代码复核能力 v1 已成为当前优先后继候选 |
| 运行时与分发 | v1 后候选库 | WI-09 未启动 |
| 项目语言治理 | 已完成并集成 | 工程术语语义安全与现行文档全量收敛 v1 已通过 PR #67 集成 |
| GitHub 集成拓扑安全 | 已完成并集成 | PR #70 已合并，提交 `96197d8664ec72aa4cdc8f5498993a228dd59357`；Issue #69 已关闭 |
| 模型路由 / 盲测对照证据 | 候选输入 | Issue #71 同时作为独立规划复核 / 模型路由研究输入；不与代码复核合并为超级能力 |

## 4. 里程碑与维护记录

### 4.1 工程能力基础 v1

已完成。

主要集成锚点：

- 首批工程纪律：PR #48，合并提交 `6130d7251d81bbfc9f13b2dd827b6a40dfd09076`；
- 技术画像 / 验证画像契约：PR #49，合并提交 `16151149ab52211e266839a110fc9a3c73415623`；
- Vue 3 + TypeScript 技术画像：PR #50，合并提交 `b80b2b1b7cea38eed0aef9807879e2a0d56afd2f`；
- 既有使用方采用交接：PR #51，合并提交 `18a48bcada8b4eeb0e6d8c3043b21c54aa8e492b`；
- 采用证据复核：Issue #52，未解决的阻塞 / 中等级通用问题为 `0 / 0`。

正式能力基线：

`b80b2b1b7cea38eed0aef9807879e2a0d56afd2f`

收尾文档：

`docs/project/engineering-capability-foundation-v1-closure.md`

### 4.2 既有使用方持续演进实验

Issue #33 已完成并关闭。

最终未解决的问题：

- 阻塞 / 中等级问题：`0 / 0`；
- 方法 / 契约缺口：`0`；
- 待补技能 / 评估：`0`。

Issue #33 只作为历史证据来源，不再承担活动路线总控职责。

### 4.3 工程纪律扩展 v1

已完成。

唯一建设候选为“数据访问作用域与有界性控制”，最终形成第三项正式工程纪律。

专项运行时评估：

```text
新场景：   8 / 8 通过，41 / 41 断言通过
历史回归： 4 / 4 通过，19 / 19 断言通过
合计：    12 / 12 通过，60 / 60 断言通过
```

最终 AI 复核未发现阻塞或中等级问题。

集成锚点：PR #56，合并提交 `8d0c7ccd1b13db05540fefc619725f9d1f7fc2de`。

收尾文档：

- `docs/project/engineering-discipline-expansion-v1.md`
- `docs/project/engineering-discipline-expansion-v1-closure.md`

### 4.4 中文交互与上下文清理 v1

已完成并集成。

启动基线：

`master@9818b3209a80bba22c6fbec2af740f49a17fa2d4`

主要结果：

- 当前高影响语言规则与示范入口完成严格中文收敛；
- 新增项目治理定向运行时评估；
- 独立运行时评估 6 / 6 场景通过；
- 人工语义评分 30 / 30 断言通过；
- 最终 AI 复核未解决阻塞 / 中等级问题为 `0 / 0`；
- 账户级记忆清理后的真正新上下文语言验收通过；
- 完成状态回写后的 `G-LANG-01` 定向回归 5 / 5 断言通过；
- PR #63 已合并，合并提交为 `5dc5b7135d59b43d624cf5a8407dae6d6b04a514`。

跟踪与证据入口：

- Issue #62；
- PR #63；
- `docs/project/chinese-interaction-context-cleanup-v1.md`；
- `tasks/plans/20260906/02-chinese-interaction-context-cleanup.md`。

### 4.5 工程术语语义安全与现行文档全量收敛 v1

已完成并集成。

启动基线：

`master@5dc5b7135d59b43d624cf5a8407dae6d6b04a514`

跟踪入口：Issue #64。

阶段 A“正式概念语义安全”已经完成：

- 建立唯一首选中文名称与正式英文身份映射；
- 明确技术画像、验证画像、任务型技能和运行时适配器的对象类型与定义权威；
- 明确技术规划阶段 / 技术计划产物，以及整体收敛阶段 / `converge`、就绪门禁 / `readiness-check`、执行阶段 / `execute-unit` 的对象边界；
- `G-LANG-01`、`G-TERM-01`、`G-TERM-02` 初始运行均为 `5 / 5`，合计 `15 / 15` 断言通过；
- 阶段 A 静态 AI 复核未解决阻塞 / 中等级问题为 `0 / 0`。

阶段 B“现行文档全量收敛”的仓库内容工作已经完成：

- 按当前分支实际目录树枚举根目录、`docs/`、`skills/`、`evals/`、`tasks/` 下的人类可读材料；
- 当前方法、架构、工程纪律、技术画像、项目治理入口和平台专项参考完成逐文件检查与必要收敛；
- 9 个 `SKILL.md` 作为双用途 Agent 契约实现，保留 front matter、契约结构字段与精确调用名，不为表面中文化修改已有行为契约；
- 历史研究、旧计划和历史评估材料完成扫描，但不机械重写；
- `G-TERM-01` 已改为验证旧材料输入不能重新覆盖当前已收敛定义，而不再假设现行定义文件仍包含旧别名。

全量扫描与处理记录：

`docs/project/terminology-semantic-safety-v1.md`

协调计划：

`tasks/plans/20260906/03-terminology-semantic-safety-and-doc-scan.md`

最终候选运行时证据：

- `G-LANG-01`：`5 / 5`；
- `G-TERM-01`：`5 / 5`；
- `G-TERM-02`：`5 / 5`；
- 合计：`15 / 15`；
- 三个进程退出码均为 `0`；
- 三个标准错误文件均为空；
- 三个 JSONL 均包含 `turn.completed`；
- 完整运行轨迹只读取各场景声明的仓库内相对路径，没有访问评分语料、历史结果、Git 历史或隔离目录外路径；
- 最终回归附件 SHA-256：`23409babbac9e2e91c519c27b832d5689310babcd80122e97243f144bb9d7e87`。

最终 AI 复核 Review `5125945453` 未解决阻塞 / 中等级问题为 `0 / 0`。

集成结果：PR #67 已合并，合并提交为 `74f0306731e12c1757df1fadd5f8b269834c48e7`；Issue #64 已按完成关闭。该里程碑不再承担当前工作入口职责，只保留为历史证据与恢复锚点。

### 4.6 Issue #58 稳定维护结果

Issue #58 继续作为长期使用方经验反馈入口。已经完成的三轮定向维护均属于稳定维护，不构成新的能力里程碑：

1. 临时执行证据晋升与长生命周期单实例评审环境治理；
2. 规划候选与执行单元身份边界；
3. 验证触发、就绪回退重入与既有项目协作约定可发现性。

最近一轮维护的运行时评估结果为：

```text
新场景：   2 / 2 通过，14 / 14 断言通过
直接回归： 4 / 4 通过，23 / 23 断言通过
合计：     6 / 6 通过，37 / 37 断言通过
```

评估对应行为提交：

`ade7a59c5bf3e0819e336beec1d223e174ec8bc2`

评估附件摘要：

`f40a91054bc03ce3be92002f2c9623d0b25ea1dbad367c5ed76a7c388aa55cab`

其中“可执行架构边界证据模式”仍保留为延后候选。现有证据不足以把它提升为方法、工程纪律或强制验证画像规则。

最新维护集成锚点：PR #61，合并提交 `9818b3209a80bba22c6fbec2af740f49a17fa2d4`。

### 4.7 Squash Merge 下 Stacked PR 集成拓扑安全 v1

已完成并集成。

启动基线：

`master@d1119e77a6fd83caa9e65334636d7aab6abdb06e`

跟踪入口：Issue #69、PR #70。

主要结果：

- 重新读取并确认 Issue #33 的历史 Consumer 证据与 `Low / Future Improvement Candidate` 分类；
- 核验 GitHub 当前原生 stacked pull requests public preview 行为；
- 明确原生 stack 与普通手工依赖 PR 链不能使用同一故障模型；
- 确定长期规则最小落点为 `docs/guides/external-operation-guidelines.md`，不修改核心方法、技能契约或 Skill；
- 增加依赖 PR 审查拓扑 / 集成拓扑薄指导；
- 设计 `G-PR-TOPO-01`、`G-PR-TOPO-02`、`G-PR-TOPO-03` 三个治理定向评估场景，共 15 条断言；
- 运行时前 AI 复核 Review `5128856306` 未解决阻塞 / 中等级问题为 `0 / 0`；
- 首轮人工语义评分为 `14 / 15`，随后针对 `G-PR-TOPO-02` 唯一缺口完成长期边界激活修订，并在第二次定向重跑仍为 `4 / 5` 后进一步修正评估提问覆盖，未降低期望行为或断言；
- 最终有效结果为 `G-PR-TOPO-01 = 5 / 5`、`G-PR-TOPO-02 = 5 / 5`、`G-PR-TOPO-03 = 5 / 5`，合计 **`15 / 15`**；
- 最终 AI 复核 Review `5129305394` 未解决阻塞 / 中等级问题为 `0 / 0`；
- 最终状态性复核 Review `5129344257` 确认最终复核后的变化仅为状态回写；
- PR #70 已于 2026-09-07 通过 squash merge 集成，合并提交为 `96197d8664ec72aa4cdc8f5498993a228dd59357`；
- Issue #69 已按完成关闭。

该里程碑不再承担当前工作入口职责，只保留为最近完成里程碑的证据与恢复锚点。

里程碑记录：

`docs/project/stacked-pr-squash-topology-v1.md`

研究记录：

`docs/research/github-stacked-pr-squash-topology.md`

协调计划：

`tasks/plans/20260907/01-stacked-pr-squash-topology-safety.md`

### 4.8 规则治理与知识激活 v1

**已完成并集成。**

人工选择日期：2026-09-08。

启动基线：

`master@0895ca30f76c666f3a0d4d9c2f9af6f14cded5d6`

跟踪入口：Issue #73。

核心目标：从“保存更多规则”转向“当前任务可靠取得最小正确规则集”，并用历史真实失效场景与使用方新上下文证明新的激活模式有效。

阶段 A“激活审计”已经完成：

- A1 冻结审计基线、13 个高影响交叉主题和 6 个真实历史场景；
- A2 将 `using-agentic-dev.md` 映射为 27 个语义激活单元候选，并只提名 3 个常驻核心候选；
- A3 将 `external-operation-guidelines.md` 映射为 28 个条件激活单元候选，不新增全局常驻核心；
- A4 登记 14 组跨权威关系并识别 5 组后续高价值减法候选；
- A5 区分纯激活失败、选择 / 冲突、误导 / 陈旧上下文和历史真实规则缺口，确认这些历史规则缺口已经进入当前仓库权威；
- 当前没有证据支持继续为相同场景机械新增同义规则；“指令密度导致失败”保留为阶段 C 待验证假设。

阶段 B“最小检索模型”已完成：

- B1 冻结 `scope + responsibility + [stage] + [subject] + [conditions]` 的稀疏检索契约；
- B2 选择 **JSON 派生规则索引 + Python 标准库薄查询器**；
- B3 建立 61 个条目、8 个唯一规范性来源的首轮派生索引；
- 27 个使用指南激活单元与 28 个外部操作激活单元均已纳入首轮索引；
- 只增加 1 个 AGENTS 薄指针与 5 个 Skill 职责消费项用于跨层关系验证；
- 查询器支持来源身份检查、稀疏条件过滤、未知维度显式回退和取代关系算法边界；
- 任一活动来源陈旧或缺失时在筛选前显式回退，不使用旧索引继续声称完整召回；
- 原型删除后不损失任何规范性事实，也没有把 Research / JSON 变成新的规则权威；
- B3 只证明原型可进入阶段 C，不证明新激活模式已经优于当前粗粒度加载。

阶段 C 的 C1“定向评估设计”已完成：

- 冻结 9 个场景，其中 6 个来自 A5 真实历史场景，3 个是负向条件、来源陈旧和真实规则缺口控制；
- A 组按当前职责加载相关整份规范性文档，不人为加载全仓库，也不故意弱化对照；
- B 组使用 B3 查询器定位最小规则入口，只有在无需回退时读取对应源段落；出现陈旧、未知维度、未知值或零命中时按 B1 回退当前仓库权威；
- A/B 使用相同 Git 基线、任务提示、模型、推理强度、工具边界和独立新上下文；
- `expected_behavior`、隐藏断言、预期规则键和历史结果不得进入 Agent 可见目录；
- 记录规则召回、精确度、上下文输入、文件 / 工具读取、语义断言、误停 / 误升级 / 误执行与权威混淆等指标；
- C1 静态设计暴露“已建模词表内零命中”漏检路径，查询器已补充 `no_indexed_rule_match` 显式回退，不通过扩索引或伪造作用域让场景通过；
- C1 只冻结设计和修正保守回退，不执行 Agent A/B，也不证明 B 优于 A。

阶段 C 的 C2“A/B 基线实现与静态校验”已完成：

- 建立可重复 A/B 隔离 runner，默认 `--validate-only`，只有显式 `--run` 才进入 C3；
- 建立 Consumer-local Authority 最小 fixture；
- 在临时副本动态制造无语义来源 blob 漂移，不持久化第二份规范性源；
- B 直接命中时从当前规范性源按 `source_pointer` 物化章节 / 独立职责载体；发生 fallback 时停止信任临时来源视图并重新从当前 Repository Authority 装配完整基线；
- Agent 可见输入不包含 A/B 分组、`metric_focus`、隐藏断言、预期规则键或预期回退；
- 固定结果结构，区分进程退出、查询回退、人工语义评分和失败分类；
- 当前仓库没有能由 runner 自动证明的统一 Codex 实际模型 / 推理强度锁定契约；C3 必须以运行证据证明配对一致，无法证明一致的配对不得进入效果比较；
- 最终差异复核发现并修正 stale-source fallback 仍消费临时陈旧副本的缺口，并增加 fallback 工作区与当前 Authority / fixture 的字节一致性断言；
- 修正后的只读 GitHub Actions Run `34296395675` / Job `102293842203` 在 Head `96eb5f356383bfb54ec5bd99e76f48f74d7ec01c` 上成功执行 Python 编译与 `python3 evals/run_rule_retrieval_ab.py --validate-only`，确认 9 个场景的 A/B 工作区可装配且没有执行 Agent A/B；此前 Run `34291536760`、`34296037510` 仅保留为祖先验证 / 诊断证据，临时 workflow 取证后已删除。

阶段 C 的 C3“隔离运行时与人工评分”已完成：

- 9 / 9 A/B pair 均取得 `gpt-5.6-sol / high` 的可比较运行事实；
- B 直接命中 29 / 29 必需规则，3 / 3 回退 reason 正确，行为语义 9 / 9 PASS；
- A 为 8 / 9，RR-C1-02 A 出现一次 `wrong_stop_or_escalation / 选择 / 冲突`；
- 直接命中场景 B 的观察到的命令输出字节约减少 `48.6%`，wall-clock 约减少 `49.8%`；
- fallback 成本显著增加，但 stale / unknown / no-match 的安全回退全部正确，不能为了成本删除 fail-closed 回退；
- 证据见 `docs/research/rule-retrieval-c3-evaluation-results.md` 与 `evals/rule-retrieval/c3-human-scoring.json`。

最终集成结果：

- D1 / D2 已将 README 收敛为薄 Bootstrap，并以 `docs/guides/rule-activation-guide.md` 提供最小长期规则导航；
- E1 在真实 Consumer `dygapp/jilinjobs-cms` 上完成逻辑 Fresh Context 验证，保持 Consumer Authority / Consumer-local Method / 精确 baseline 优先；
- E2 CodeGraph A/B 未执行，属于可选且非阻塞输入；
- F1 首次回归正确发现 `AGENTS.md` source identity 陈旧并 fail-closed，最终 Run `34325868257` 在重建最终源身份后通过；
- F2 Final AI Review `5151401609` 未解决 Blocking / Medium = `0 / 0`；
- F3 稳定状态收敛完成；
- PR #89 已按最终复核 Head 集成，合并提交为 `4a42d7a23a40e4dbae84c2817b6d30acc1b6aa14`；Issue #73 已关闭。

该里程碑不再承担当前工作入口职责。当前回到下一有限里程碑的人工决策，不自动启动代码复核、技术画像、运行时适配或其他候选。

项目记录：

`docs/project/rule-governance-knowledge-activation-v1.md`

研究记录：

- `docs/research/knowledge-activation-and-code-intelligence-analysis.md`
- `docs/research/knowledge-activation-evidence-appendix.md`
- `docs/research/rule-activation-audit-baseline.md`
- `docs/research/using-agentic-dev-activation-map.md`
- `docs/research/external-operation-guidelines-activation-map.md`
- `docs/research/cross-authority-duplication-audit.md`
- `docs/research/activation-failure-classification.md`
- `docs/research/minimal-rule-retrieval-contract.md`
- `docs/research/rule-retrieval-prototype-selection.md`
- `docs/research/rule-retrieval-prototype-validation.md`
- `docs/research/rule-retrieval-targeted-evaluation-design.md`
- `docs/research/rule-retrieval-ab-baseline-validation.md`
- `docs/research/rule-retrieval-c3-evaluation-results.md`

协调计划：

`tasks/plans/20260908/01-rule-governance-knowledge-activation.md`

## 5. 当前工程纪律清单

当前正式工程纪律：

1. 实现最小化与推测性复杂度控制；
2. 精准修改与差异范围控制；
3. 数据访问作用域与有界性控制。

规范入口：

`docs/architecture/engineering-disciplines.md`

当前没有第四项工程纪律的活动研究、草案或评估计划。

## 6. 当前技能与技术画像状态

- 当前仓库共有 8 个核心技能和 1 个平台专项技能；
- 工程纪律扩展 v1 没有新增技能；
- 技术画像契约已经集成；
- 当前代表性技术画像为 Vue 3 + TypeScript；
- Element Plus、Spring Framework / Spring Boot / Spring MVC、Gradle 等仍是未来候选，不构成当前路线承诺；
- WI-06 继续暂缓，先由代码复核 / 使用方评估判断哪些技术知识确有持久化增量价值。

## 7. v1 后候选库

以下候选继续保留，当前均未启动。

### WI-06 — 第二及后续技术画像

可能候选包括：

- Spring Framework / Spring Boot / Spring MVC；
- Gradle；
- Element Plus；
- 其他后续证据支持的技术栈。

已有技术画像完成不会自动触发 WI-06。

当前优先边界进一步收紧为：

> 先用代码复核 / 使用方评估判断“模型自身知识 + 当前仓库 + 必要时当前官方资料”是否仍存在稳定、跨项目、会实质影响工程决策的缺口，再决定是否持久化新的技术画像。

当前研究假设：Spring 与 Gradle 具有较高代码复核评估价值；Element Plus 的通用长期技术画像价值相对较低。该判断只是研究输入，不构成 WI-06 启动。

### WI-07 — 任务型技能提炼

只有出现可证明的独立稳定任务职责，并具有明确输入、过程、输出、退出和升级边界时，才重新评估。

不得机械创建按技术名称组织的百科式技能。

#### 优先后继候选：代码复核能力 v1

当前状态：**优先后继候选，未启动**。

当前证据已经足以把 `code-review` 从抽象未来可能性提升为 WI-07 的明确优先候选；其启动仍受新的有限里程碑人工决策约束。

候选职责：

- 独立、使用新上下文或严格控制上下文的高信噪比代码复核；
- 输入包括当前仓库权威、相关规格说明 / 技术计划 / 架构、差异 / 当前源码与验证证据；
- 输出为可执行的问题发现、无阻塞 / 中等级问题结论，或证据不足 / 升级说明；
- 重点检查规格符合性、真实缺陷 / 回归、数据 / 状态 / 并发 / 生命周期、边界 / 依赖 / 副作用、推测性复杂度、差异范围、验证证据和按风险触发的技术误用；
- 可以由使用方代码智能（如 CodeGraph）辅助结构发现，但不能对其形成强依赖。

候选边界：

- 不成为新的通用方法阶段；
- 不要求所有微小工作机械进入独立复核；
- 不与独立高风险规划复核 / 架构复核合并；
- 不成为“复核一切”的超级 Skill；
- 不创建 `vue-review-skill`、`spring-review-skill`、`gradle-review-skill` 等按技术名称组织的复核 Skill；
- 不预加载全部指南 / 工程纪律 / 技术画像；
- 不把命名、格式、个人风格或无证据未来扩展性作为主要问题发现。

启动前置条件：

1. 规则治理与知识激活 v1 已完成并集成；
2. “任务 / 风险 → 规则激活”模式已经有可验证证据；
3. 重新读取 Issue #71，区分代码复核与独立高风险规划复核；
4. 冻结代码复核输入 / 输出 / 退出 / 升级契约；
5. 设计真实使用方差异专项评估；
6. 明确无 CodeGraph / 无专项技术画像时的可靠回退路径。

### WI-09 — 运行时适配与分发

包括未来可能的：

- 运行时适配器；
- Marketplace；
- Plugin Bundle；
- Controller；
- 统一安装或分发机制。

当前没有真实多运行时交付需求足以使其成为活动里程碑。

#### 候选有限里程碑：Codex 多模型协同采用适配 v1

状态：**v1 后候选，未启动**。

该候选只面向 Codex 平台，拟以平台专项非核心 Skill 为主要载体，帮助使用方读取自身仓库权威、项目风险、验证能力与当前 Codex 运行时事实，推演多代理角色、模型与推理强度的候选映射，并形成待确认的项目规则、`.codex` 配置差异、专项评估与回退方案。它与 `github-actions-verification` 同属按实际平台条件触发的专项能力，不构成所有使用方项目的默认依赖。

当前可行性依据仅包括：Codex 官方文档已经公开支持为本地自定义代理配置不同模型与推理强度，并明确子代理工作通常比可比的单代理运行消耗更多令牌；当前仓库架构也已经允许按实际平台条件建立专项非核心 Skill 与运行时适配；Issue #71 已收录一组尚待本仓库复核的使用方模型路由与盲测对照证据。官方能力依据见 [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)。这些依据只支持继续研究候选，不证明任何具体模型映射已经正确，也不证明工程质量或 Plus 限额利用率已经改善。

候选采用混合边界：

- Skill 固化 Codex 平台内相对稳定的输入要求、任务 / 风险分类维度、角色能力要求、升级条件、输出契约、停止条件与验证要求；
- 具体模型标识、推理强度、配置字段、账户可用性与限额行为只作为带来源、版本和日期的当前运行时事实，不固化为跨版本永久结论；
- 使用方运行 Skill 后只得到候选方案，最终采用结果仍由使用方固化到自身 `AGENTS.md`、`.codex/config.toml`、`.codex/agents/*.toml` 或其他项目权威；
- 默认过程只读。写入使用方配置、修改项目权威、调用外部服务或执行集成操作必须获得对应任务的明确授权，并在写入后重新验证实际状态；
- 模型发布、停用、可用范围、配置结构、限额规则或专项质量证据发生实质变化时，触发重新评估而不是自动迁移。

候选非目标：

- 不修改核心方法、原则、通用工程纪律、技术画像或通用 Skill 契约；
- 不建立跨 Codex、Claude Code、Cursor 等运行时的通用模型路由规范；
- 不永久规定某个命名模型必然承担固定角色，也不承诺无法由当前证据精确证明的 Plus 限额节省比例；
- 不让单一 Skill 接管需求、规划、实施、验证、集成的完整生命周期；
- 不以 Skill 自身推演替代独立专项评估、当前运行时证据或人工采用决策。

未来如由人工权威选择为活动里程碑，启动前至少需要冻结：

1. 当前 Codex 官方能力、配置结构、模型可用性与子代理用量边界的证据基线，并完成 Issue #71 的证据复核与架构适配判断；
2. 平台专项 Skill 的明确输入、输出、只读默认、授权写入与退出契约；
3. 单一主力模型基线与多模型候选方案的对照评估设计，分别观察工程质量、返工、延迟、代理 / 令牌用量等可取得指标，不使用不可观察数据推导虚假精确收益；
4. 模型演进场景，包括模型替换、能力趋同、限额变化、配置失效与证据过期时的重新解析和安全回退；
5. 能识别不适用项目、环境未知、危险下沉、自证循环和静默修改的有辨识力专项评估；
6. 与风险相称的隔离运行时评估、人工语义评分、最终 AI 复核和使用方验证边界。

当前证据只支持把该方向登记为候选，不构成平台专项 Skill 的准入完成证据，也不启动 WI-09。

### Issue #71 — 模型路由与盲测对照证据

Issue #71 收录使用方在关键架构评审中形成的配对盲测、隐藏断言、低成本优先与基于证据升级相关证据。

当前只把它作为规划 / 研究候选：

- 尚未由 `agentic-dev` 完成证据复核与架构适配判断；
- 不构成新的常规方法门禁；
- 不构成新的技能、模型路由框架或默认模型策略；
- 请求模型 / 实际运行模型的证据声明边界仍需在后续规划时单独评估；
- 其中 AR-04 同时支持“高返工技术规划的独立新上下文复核”研究价值，但该职责必须与未来代码复核分开评估。

### 其他候选

- 新的工程纪律研究候选；
- Issue #58 后续形成的通用能力候选；
- 可执行架构边界证据模式。

这些候选都必须重新经过证据检查、架构适配评估和人工里程碑决策，不能直接进入当前权威。

## 8. 当前边界

当前没有活动有限里程碑，路线状态为：

> **待人工决策**

规则治理与知识激活 v1 已完成并集成；在人工权威选择新的有限里程碑前，不进入任何候选的实施阶段。

当前候选继续包括：

- WI-07 — 代码复核能力 v1（优先后继候选）；
- WI-06 — 第二及后续技术画像；
- WI-09 — 运行时适配与分发；
- 第四工程纪律建设；
- 第二次基础型既有项目采用门禁；
- 可执行架构边界证据模式；
- Issue #71 的模型路由 / 多模型采用研究与候选实施。

优先级不等于启动授权；新的证据也只更新候选判断，不自动创建活动里程碑。

## 9. 后续有限里程碑决策规则

下一正式有限里程碑必须：

1. 由人工权威显式选择；
2. 有清晰的单一或有限目标；
3. 在开始时冻结完成定义；
4. 明确非目标与范围扩张门禁；
5. 根据候选类型完成必要的研究、架构适配评估、草案、专项评估、AI 复核和集成；
6. 不因为新候选出现而自动追加到同一里程碑。

规则治理与知识激活 v1 已完成并集成。当前优先重新评估 WI-07 — 代码复核能力 v1，但优先级不等于自动启动；下一正式有限里程碑仍需新的人工权威显式选择。

## 10. 新上下文恢复顺序

新的 `agentic-dev` 工作上下文应：

1. 读取根目录 `AGENTS.md`；
2. 读取本文，确认当前长期阶段、最近完成并已集成的有限里程碑，以及当前是活动里程碑还是待人工决策；
3. 读取当前 GitHub `master`、开放 PR 和开放 Issue，确认是否存在晚于本文的新人工决定或集成事实；
4. 若当前为待人工决策，只按候选评估需要读取 Issue #58 / #71、历史里程碑记录或相关 Research，不机械恢复已关闭里程碑的完整协调计划；
5. 若人工权威已经选择新的有限里程碑，再读取该里程碑的 Issue、项目记录、Research / Plan 和当前下一实际门禁；
6. 只有当前任务确实需要时，继续读取 `using-agentic-dev.md`、`external-operation-guidelines.md`、Skill Architecture、Skill Contracts、工程纪律或历史评估；不得因为研究对象很多而默认全量加载；
7. 不把 WI-06、WI-07、WI-09、第四工程纪律或 Issue #71 当作当前实施工作，除非存在晚于本文的明确人工里程碑决定；
8. 代码复核能力 v1 当前只是优先后继候选，必须由新的人工里程碑决策显式选择后才能启动；
9. CodeGraph / Obsidian 是 Research 中的外部输入，不是当前仓库权威或强制工具；使用方 CodeGraph 采用只能按实际使用方环境独立验证；
10. 不依赖历史聊天、其他会话或个人记忆补充未固化的项目事实；
11. 面向人的输出遵循当前仓库严格中文表达规则，并使用当前正式概念身份映射，不从历史会话或个人记忆恢复旧的中英文混写语风或冲突中文别名。

## 11. 更新触发条件

出现以下情况时更新本文：

- 当前有限里程碑完成、取消或被取代；
- 人工权威选择新的有限里程碑；
- 当前仓库权威发生新的能力集成；
- 高质量证据导致现有方法、架构、工程纪律或技术画像需要正式修订；
- 当前路线与 GitHub 集成事实不再一致。

普通使用方局部问题、单个外部来源或尚未完成架构适配评估的候选，不要求更新本文。