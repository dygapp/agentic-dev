# 规则治理与知识激活 v1

## 状态

**已完成并集成**

人工决策日期：2026-09-08

跟踪入口：Issue #73

启动基线：

`master@0895ca30f76c666f3a0d4d9c2f9af6f14cded5d6`

集成结果：PR #89 已通过 squash merge 集成；Issue #73 已按完成关闭。

启动固化分支：

`docs/rule-governance-knowledge-activation-v1`

长期阶段保持：

> **工程能力扩展与方法演进**

本里程碑不启动 WI-06、WI-07、WI-09、第四工程纪律或其他候选能力的实现。WI-07 — 代码复核能力 v1 被明确登记为本里程碑完成后的优先后继方向，但不会因为本里程碑启动而自动进入执行。

## 1. 决策背景

项目已经从早期“能力不足”逐步进入“能力存在但激活可靠性不足”的阶段。

当前仓库已经具有较成熟的：

- 仓库权威；
- 方法 / 架构 / 工程纪律 / 技术画像 / 指南 / 技能分层；
- 新上下文与渐进式披露原则；
- 当前证据与集成状态闭环；
- 多轮使用方证据；
- 运行时评估与人工语义评分机制。

但真实演进中出现了新的结构性风险：

1. `using-agentic-dev.md`、`external-operation-guidelines.md` 等较大指南已包含多个可以独立触发的长期职责；
2. 为避免超级技能而保留在指南中的规则，如果仍以整份指南为激活单位，会形成“文档型超级能力”；
3. 新问题出现后继续默认“补一条规则 / 补一个指南段落”，会扩大活动指令面和重复规则；
4. 已经出现“规则存在，但没有在正确任务路径中可靠激活”的现实信号；
5. 高能力模型本身已经具备大量通用技术知识，继续扩大百科式技术指导的边际价值下降；
6. 使用方真实开发还存在源码发现成本，应该区分“规则激活”和“代码结构发现”，后者可以优先使用成熟代码智能工具，而不是由 `agentic-dev` 自己再造。

因此人工权威选择“规则治理与知识激活 v1”作为下一有限里程碑。

完整研究依据：

- `docs/research/knowledge-activation-and-code-intelligence-analysis.md`
- `docs/research/knowledge-activation-evidence-appendix.md`

## 2. 核心目标

本里程碑只解决一个有限问题：

> **让当前任务能够以更小、更准确、可验证的活动上下文发现并激活正确规则，同时抑制指南、重复规则和长期上下文面的继续膨胀。**

具体目标：

1. 对当前高影响指南和跨层规则执行激活审计；
2. 识别真实的规则激活单元，而不是以文件大小或目录结构作为治理单位；
3. 区分常驻核心规则、任务能力上下文、条件规则上下文；
4. 冻结一个最小“任务 / 风险 → 规则集”检索模型；
5. 使用真实历史失效场景验证检索 / 激活，而不是只检查文档结构；
6. 基于评估证据决定哪些指南应拆分、哪些只需要段落级指针、哪些规则应删除 / 合并 / 取代、哪些必须留在常驻核心规则中；
7. 至少在一个使用方新上下文中验证新的激活方式；
8. 建立“先判断激活失败，再决定是否新增规则”的长期治理路径。

## 3. 关键设计原则

### 3.1 治理对象是激活单元，不是文件大小

大文件不自动等于错误，小文件也不自动等于可发现。

不得设定“超过某个 KB 就拆分”之类机械规则。所有结构调整必须能够说明：

- 该语义由什么触发；
- 谁消费；
- 是否需要独立加载；
- 是否与其他规则重复 / 冲突；
- 是否能通过检索评估观察到改善。

### 3.2 常驻核心规则必须保持薄

只有真正跨任务成立的不变量才可以进入常驻核心规则。

“重要”不等于“每次都加载”。

### 3.3 技能不拥有全部知识

技能负责稳定任务职责与流程边界；条件性知识继续存在于合适的长期权威中，通过指针或检索按需进入当前上下文。

不得为了修复指南激活问题，把所有指南内容重新复制到技能。

### 3.4 权威与索引分离

如果后续出现规则元数据 / 索引 / 查询原型：

- Git 仓库中的规范性文档继续是权威；
- 索引必须可重建；
- 索引必须可检测陈旧；
- 索引不得成为第二事实来源；
- 同一规则不得因为方便检索而在多个权威中复制全文。

### 3.5 检索必须可评估

评估对象不是“索引能运行”，而是：

> 当前任务得到的规则集合是否足够正确完成任务，并且没有大量无关规则干扰。

## 4. 当前研究输入

### 4.1 仓库内与长期技术输入

当前树长期保留的主要技术输入：

- `AGENTS.md`；
- `docs/guides/rule-activation-guide.md`；
- `docs/guides/using-agentic-dev.md`；
- `docs/guides/external-operation-guidelines.md`；
- `docs/architecture/skill-architecture.md`；
- `docs/architecture/skill-contracts.md`；
- `docs/research/knowledge-activation-and-code-intelligence-analysis.md`；
- `docs/research/knowledge-activation-evidence-appendix.md`；
- `docs/research/llm-wiki-rule-governance-fit-analysis.md`；
- `docs/research/rule-retrieval-design-reference.md`；
- `evals/rule-retrieval/*`。

阶段 A～E 的审计、基线冻结、原型选择 / 验证和运行结果 Markdown 属于里程碑过程证据；2026-09-09 起不再作为当前 Research 文档。精确历史由 Git、PR #74～#89、Issue #73、本项目记录和 `evals/` 承接。

### 4.2 外部研究

- OpenAI 当前模型提示与工具指导；
- Obsidian Graph / Backlinks / Properties / Bases；
- `colbymchenry/codegraph` 当前实现与 Agent 集成；
- CodeGraph 检索 / Agent A/B 评估设计。

外部研究不能自动覆盖本仓库权威。

## 5. 分阶段实施路线

### 阶段 A — 激活审计

状态：**已完成**。

阶段 A 已完成：

1. `using-agentic-dev.md` 语义激活映射；
2. `external-operation-guidelines.md` 语义激活映射；
3. 跨权威重复 / 范围敏感关系审计；
4. A1 冻结的六个真实历史场景失效分类；
5. 区分合理薄摘要 / 职责消费与后续值得做减法的实质重复候选；
6. 明确历史上存在过真实规则缺口，但 PR #59 / #60 / #61 / #72 等已经把相关长期语义补入当前仓库权威；当前不应继续为相同场景机械增加同义规则。

阶段 A 的五份审计 / 激活映射过程文档已在 2026-09-09 Research 信息架构维护中从当前树移除。需要复核阶段 A 原始材料时，从 PR #75～#79、Issue #73 或 Git 历史恢复；长期技术结论已由当前 Guide、Project Record 与规则检索设计参考承接。

阶段 A 完成门禁已经满足：

- 至少两个大型指南已完成可审查的激活映射；
- 已明确区分“规则缺失”和“规则已存在但未激活”的历史场景；
- 未以“把指南拆小”作为默认结论；
- “指令密度导致失败”仍保持为阶段 C 待验证假设，而不是由文件体量预先断言。

### 阶段 B — 最小检索模型

状态：**已完成**。

目标：冻结最小、工具无关的检索语义并验证最小原型。

B1 已冻结：

- 必需输入：`scope + responsibility`；
- 条件输入：`stage / subject / conditions`；
- 最小结果：源权威指针、短激活摘要、适用信息、必需检查和匹配解释；
- 条目角色：authority / pointer / consumer / evidence；
- 最小关系：equivalent / scope-variant / superseded-by；
- 来源身份变化、范围冲突、高影响授权不确定或索引不可用时，直接回退当前仓库权威；
- 当前不要求全库统一增加文件头，也不要求特定索引技术。

B1 的长期技术设计已收敛到：

`docs/research/rule-retrieval-design-reference.md`

B2 已选择：

> **JSON 派生规则索引 + Python 标准库薄查询器**

B2 选择依据：

- 当前 `evals/` 已采用 JSON 语料和 Python 标准库薄执行器；
- JSON 能稳定表达 B1 的稀疏条件、来源身份和最小关系；
- Python 标准库足以执行确定性过滤、陈旧检测和机器可读输出；
- 不需要新增第三方包、数据库、MCP、服务或统一文件头；
- 首轮只覆盖阶段 A 已审计的高影响规则面，不建立全仓库规则数据库。

B2 的实现选择依据已收敛到 `docs/research/rule-retrieval-design-reference.md`；精确历史由 PR #81 / Git 保存。

B3 已实现并验证原型：

```text
evals/rule-retrieval/rule-index.json
evals/query_rule_index.py
```

B3 的当前可执行证据位于 `evals/rule-retrieval/` 与 `evals/query_rule_index.py`；精确实现 / 验证历史由 PR #82 / Git 保存。

B3 当前结果：

- 首轮派生索引包含 61 个条目、8 个唯一规范性来源；
- 27 个 `using-agentic-dev.md` 激活单元与 28 个外部操作激活单元已进入首轮索引；
- 只增加 1 个 `AGENTS.md` 薄指针和 5 个 Skill 职责消费项用于跨层关系验证；
- 查询器能区分作用域、职责、阶段、目标对象和条件，并在缺失必要维度时显式回退；
- 查询前校验全部活动来源身份，任一来源陈旧或缺失时显式回退，不用旧索引继续声称完整召回；
- 原型删除后不损失任何规范性事实，仍可从仓库权威和阶段 A 审计重建；
- 原型验证不证明按需检索已经优于现有粗粒度加载，效果判断留给阶段 C。

阶段 B 完成门禁已经满足：

- 能从有限任务上下文返回可解释的最小规则集；
- 每条结果可追溯到唯一权威来源；
- 索引删除后可以从仓库恢复，不损失权威。

### 阶段 C — 检索 / 激活评估

状态：**已完成**。

目标：证明检索模式能改善 Agent 行为，而不是只改善文档观感。

C1“定向评估设计”已经完成：

- 冻结 6 个真实历史场景 S-01～S-06 与 3 个控制场景；
- A 组使用当前职责下相关整份规范性文档，避免人为弱化对照组；
- B 组使用稀疏查询 + 当前源指针，并把 stale / unknown / no-match 回退作为显式可测行为；
- 运行时不得暴露 `expected_behavior`、隐藏断言或预期规则键；
- 结果必须区分进程退出、查询回退和人工语义评分；
- C1 静态设计发现首轮索引对 `agentic-dev` 项目级 Roadmap 状态闭环没有直接覆盖；查询器已增加 `no_indexed_rule_match` 安全回退，不通过伪造 `consumer-project` scope 或新增规则掩盖覆盖边界。

C1 研究 / 机器可读设计：

- `evals/rule-retrieval/targeted-evaluation-design.json`

C2“A/B 基线实现与静态校验”已经完成：

- 建立 `evals/run_rule_retrieval_ab.py`，默认只静态校验，只有显式 `--run` 才进入 C3；
- 建立 Consumer-local Authority 最小 fixture，并在临时目录动态生成无语义来源 identity 漂移控制；
- B 无回退时从当前规范性源按 `source_pointer` 物化章节 / 独立职责载体；发生 fallback 时停止信任临时来源视图，重新从当前 Repository Authority 装配 C1 已声明的完整基线；
- Agent 可见上下文不包含 A/B 分组、`metric_focus`、隐藏断言、预期规则键或预期回退；
- `result-schema.json` 区分进程退出、查询回退、人工语义评分和失败分类；
- 当前仓库没有可由 runner 自动证明的统一 Codex 模型锁定契约，因此 C3 必须用实际运行证据证明 A/B 模型与推理强度一致；无法证明一致的配对不能进入效果比较；
- 最终差异复核发现并修正 stale-source fallback 仍消费临时陈旧副本的缺口；静态校验现在逐文件确认 fallback 工作区与当前 Authority / fixture 一致；
- 修正后的只读 GitHub Actions Run `34296395675` / Job `102293842203` 在 Head `96eb5f356383bfb54ec5bd99e76f48f74d7ec01c` 上实际执行 `py_compile` 与 `python3 evals/run_rule_retrieval_ab.py --validate-only` 并成功，确认 9 个场景的 A/B 工作区可装配，且未执行 Agent A/B；此前运行只保留为祖先验证 / 诊断证据；临时 workflow 取得证据后已删除。

C2 研究 / 评估入口：

- `evals/rule-retrieval/README.md`
- `evals/rule-retrieval/result-schema.json`
- `evals/run_rule_retrieval_ab.py`

C3 评估设计（已完成）：

> **C3 — 隔离运行时与人工评分**

C3 已按冻结场景执行真实新上下文 / 隔离 A/B，并由人工逐项评分；只有实际模型 / 推理强度、公平输入边界和隐藏断言隔离都能由证据支持的 A/B 配对进入效果比较。

阶段 C 至少观察：

- 必须规则召回；
- 无关规则数量 / 精确度；
- 上下文令牌；
- 工具 / 文件读取；
- 行为语义正确性；
- 是否出现误停 / 误升级 / 误执行；
- 是否产生双重权威或陈旧状态；
- 安全回退发生率与回退成本。

进程退出码为 0 不等于语义通过。必须人工语义评分。

C3“隔离运行时与人工评分”已经完成：

- 18 / 18 Codex 进程退出 0，9 / 9 A/B pair 均为 `comparable`，实际 provider model / reasoning effort 均为 `gpt-5.6-sol / high`；
- B 直接命中场景 6 / 6 精确得到冻结 expected set，必需规则 `29 / 29`；3 个控制回退 reason `3 / 3` 正确；
- B 行为语义 `9 / 9` PASS；A 为 `8 / 9`，RR-C1-02 A 记为 `wrong_stop_or_escalation / 选择 / 冲突`；
- 直接命中场景 B 的观察到的命令输出字节约减少 `48.6%`，wall-clock 约减少 `49.8%`；fallback 成本上升但安全性正确；
- 机器可读人工评分保存在 `evals/rule-retrieval/c3-human-scoring.json`；精确运行 / PR 历史由 GitHub 原生记录。

阶段 C 已形成足够收益证据；不支持全仓库规则数据库、全量拆分指南、删除 fallback 或派生索引权威化。

### 阶段 D — 权威 / 指南收敛

状态：**已完成**。

D1 只实施阶段 C 直接支持的最小长期收敛：

- README 从综合状态 / 规则摘要入口收敛为薄 Bootstrap，并把详细当前路线继续单点指向 Project Roadmap；
- 新增 `docs/guides/rule-activation-guide.md`，只保留使用方仓库权威优先、渐进式披露、证据先于完成声明三条跨任务不变量，以及按职责 / 风险定位当前 Guide / Skill 的稳定段落指针；
- 段落无法精确定位、导航无命中、范围冲突或高影响授权不明确时 fail-closed 回退当前 Repository Authority；
- 详细规则正文继续由现行 Guide / Skill 单点维护；本轮没有删除阶段 A 标记的源规则，也没有修改 B/C 派生索引的 8 个规范性来源；
- 没有引入第二 Wiki 权威、全仓库统一元数据、BM25 / vector / graph、MCP knowledge server 或新的知识型 Skill。

D2 回归结论：

- GitHub Actions Run `34320938617` 在 Head `bfa76f95e2dcb8de39bd2a98ab1819f71e710abc` 上成功；Python 编译检查、`evals/run_rule_retrieval_ab.py --validate-only`、最终 Bootstrap / 指针 / 回退静态断言全部通过；
- 9 个既有 A/B 场景仍可装配，B 查询与 C1 冻结命中 / 回退保持一致；
- 现有四组历史治理评估不读取 README 或新规则导航，但部分 `context_paths` 包含 `AGENTS.md` / Roadmap；PR #88 后续项目状态闭环改变了这些状态输入，因此不把绑定旧阶段事实的 expected behavior 机械作为当前状态回归。F1 发现并保留 `AGENTS.md` 的 `source_identity_changed` fail-closed 证据；核对已索引“外部操作治理”段落语义未变后，仅重建派生 rule-index 的当前源身份；
- 新入口不要求读取完整历史，也没有改变正式工程概念身份或中文表达规则。

阶段 D 没有证据要求机械执行原候选动作清单中的所有结构变化；源规则删除 / 合并、更多元数据或长期检索运行时继续等待真实使用方证据。

### 阶段 E — 使用方验证

状态：**已完成**。

E1 真实使用方验证：**PASS**。

- Consumer：`dygapp/jilinjobs-cms`；
- Consumer integrated baseline：`main@982a214d65f8ebfa461a6488b89709c2be1a3863`；
- 实际执行对象：PR #117 / Head `547ac9453fd4ca6b85949810f3991d02f172e02f`；
- Consumer 自身记录的 `agentic-dev` baseline 继续保持 `master@d9fad0da83dbdb61cac5eb9778b0258c6861eef1`，本次验证没有执行 baseline upgrade；
- 薄入口只激活当前执行单元、异步外部操作、GitHub Actions 证据与临时证据晋升所需规则；Consumer-specific source error / migration ownership 全部回到 Consumer Authority；
- E1 六项检查全部 PASS；精确 Consumer 验证与 Actions / Artifact 证据由 PR #89、Issue #73 和 GitHub 原生历史保存。

E2 Consumer CodeGraph A/B：**未执行 / 可选 / 不阻塞**。当前没有证据要求用源码发现实验替代或补充 E1 的 Repository Authority / Method Activation 验证，也不因此否定 CodeGraph 的后续可选价值。

### 阶段 F — 最终复核与集成

F1 最终验证已完成：首次 `--validate-only` 按设计报告 `AGENTS.md (source_identity_changed)`，证明陈旧派生索引没有被静默消费；确认被索引“外部操作治理”段落正文未变后，以最终源 blob 重建派生 identity。最终 Run `34325868257` 的陈旧源审计、9 场景静态检索回归、E1 证据边界检查与临时工作流自清理全部成功。

F2 最终 AI 复核已完成，F3 稳定项目状态已收敛；最终集成通过 PR #89 完成，Issue #73 已关闭。

本里程碑已完成并集成，不再承担当前工作入口职责。当前路线为待人工决策；WI-07 仍只是优先候选，不自动启动。

## 6. 非目标

本里程碑不做：

- `code-review` 技能实现；
- Spring / Gradle / Element Plus 技术画像建设；
- 第四工程纪律建设；
- Obsidian 强制采用；
- CodeGraph 强制采用；
- 规则图 / MCP 平台化；
- 所有指南机械拆文件；
- 把所有长期规则改成 YAML；
- 把所有规则复制进技能；
- 运行时 / 分发 / Marketplace 建设；
- 多模型协同候选实施。

## 7. CodeGraph / 使用方代码智能边界

CodeGraph 研究被保留为本里程碑的重要外部参考，但它同时解决一个不同的使用方问题：源码结构发现。

当前边界：

- `agentic-dev` 研究规则 / 权威激活；
- 使用方可以独立实验 CodeGraph 作为可选代码智能；
- 使用方主要使用 CodeGraph 的本地索引 + MCP / CLI + 极薄激活指令，不复制其内部开发技能；
- `.codegraph/` 只是派生索引，不构成使用方权威；
- CodeGraph 不替代编译器、测试、运行时验证、规格说明或代码复核；
- ChatGPT + GitHub Connector 当前不能直接消费使用方本地 `.codegraph/`，Local Codex 等本地 Agent 才是直接受益环境。

本里程碑可以保留使用方 CodeGraph A/B 设计，但不要求把 CodeGraph 纳入 `agentic-dev` 核心依赖。

## 8. 后继方向：WI-07 — 代码复核能力 v1

代码复核是本里程碑完成后的优先后继候选。

当前规划边界已经冻结到以下程度，以确保未来新上下文不需要恢复本次聊天：

### 8.1 为什么值得重新评估

- 代码复核在早期技能架构中已经存在，但第一批 8 个核心技能阶段选择保持为内嵌纪律；
- 当前已有更多使用方 / 独立复核证据；
- Issue #71 的新上下文架构盲测证明独立复核者可以在高返工问题实施前发现真实结构缺陷；
- 代码复核现在具备独立输入、稳定过程、独立输出、退出 / 升级边界和专项评估条件，符合 WI-07 的重新评估门槛。

### 8.2 预期职责

输入：

- 当前仓库权威；
- 相关规格说明 / 技术计划 / 架构；
- 差异 / 变更文件 / 当前源码；
- 可用验证证据；
- 按风险激活的工程纪律 / 技术检查。

输出：

- 高信噪比、可执行的问题发现；或
- 明确的无阻塞 / 中等级问题结论；或
- 证据不足 / 需升级说明。

### 8.3 预期检查重点

- 规格符合性；
- 明确缺陷 / 回归；
- 数据、状态、并发、生命周期；
- 边界 / 依赖 / 副作用；
- 推测性复杂度 / 不必要抽象；
- 差异范围；
- 验证证据；
- 当前上下文触发的高风险技术误用。

### 8.4 明确非目标

- 不成为新的通用方法阶段；
- 不强制所有微小变更都执行独立复核；
- 不与规划复核合并；
- 不与安全复核等其他专项复核合并为超级技能；
- 不创建 `vue-review-skill`、`spring-review-skill`、`gradle-review-skill`；
- 不预加载所有技术画像；
- 不把命名、格式、个人风格或无证据未来扩展性作为主要问题发现。

### 8.5 与规则治理的依赖关系

代码复核 v1 不应在当前规则激活问题尚未收敛时直接实现，否则很容易形成新的超级技能：

```text
code-review
→ 全量方法 + 指南 + 工程纪律 + 技术画像
→ 上下文爆炸
```

因此推荐：

```text
规则治理与知识激活 v1
→ 任务 / 风险 → 规则激活可验证
→ 再启动 WI-07 代码复核能力 v1
```

### 8.6 与 CodeGraph 的关系

CodeGraph 可以作为使用方代码复核的可选结构发现能力：

```text
差异
→ CodeGraph 相关源码 / 调用者 / 影响范围
→ 规则激活
→ 复核者
```

但代码复核契约不能依赖 CodeGraph 才能成立；没有 CodeGraph 时必须可以回退到仓库原生搜索和读取。

## 9. 技术画像决策边界

WI-06 暂不启动。

后续只有代码复核 / 使用方评估证明存在稳定、跨项目、模型自身知识 + 当前仓库 + 当前官方资料仍无法可靠补足的增量技术检查知识时，才重新评估持久化技术画像。

当前优先级仅作为研究假设：

- Vue 3 + TypeScript：保留现有技术画像，不机械扩张；
- Spring：较高代码复核评估价值；
- Gradle：较高代码复核评估价值，已有真实应用边界证据；
- Element Plus：通用长期技术画像价值较低。

不把该优先级当作 WI-06 已启动事实。

## 10. AI 友好代码边界

本轮认可的方向不是“所有代码都要更短”，而是：

> **尽量缩小安全变更推理面。**

未来代码复核可以评估：

- 变更局部性；
- 依赖方向；
- 状态所有权；
- 显式副作用；
- 抽象必要性；
- 间接层成本；
- 契约清晰度；
- 测试接缝。

但现有工程纪律已经覆盖实现最小化与精准修改，因此本里程碑不新增第四工程纪律。是否需要“结构可推理性 / 上下文半径”类纪律，必须等后续复核评估形成稳定证据。

## 11. 完成定义

本里程碑只有以下条件全部满足才可进入集成决策：

1. 完整研究已进入 `docs/research/`；
2. `using-agentic-dev.md` 和 `external-operation-guidelines.md` 至少完成激活审计；
3. 最小检索模型已冻结；
4. 历史检索 / 激活评估已建立并具有辨识力；
5. 完整 / 粗粒度上下文与缩减 / 按需上下文已完成隔离运行时对照和人工语义评分；
6. 必要指南 / 权威 / 技能激活指针已按证据收敛；
7. 没有通过复制规则制造新的双重权威；
8. 至少完成一次使用方新上下文验证；
9. 最终 AI 复核未解决阻塞 / 中等级问题为 `0 / 0`；
10. 集成前项目状态入口完成闭环。

这里的“进入集成决策”指整个“规则治理与知识激活 v1”里程碑在阶段 F 的完成状态，不等同于本启动 PR #74 的集成门禁。PR #74 只负责固化里程碑研究、路线、恢复入口和协调计划；其自身在最终 AI 复核与集成后状态闭环满足仓库规则后，可单独达到“已具备进入集成决策的条件”，随后里程碑才从阶段 A 开始实际实施。

## 12. 当前下一步

阶段 A、阶段 B、阶段 C 已完成。下一实际步骤不是拆分指南、全库增加文件头，也不是实现代码复核，而是：

> **阶段 D — 权威 / 指南收敛 / D1 — 基于证据实施指南 / 权威收敛。**

本文件现在是已完成里程碑的历史项目记录，不再承担 Fresh Context 当前工作入口。普通新上下文应读取 `AGENTS.md` 与 Project Roadmap；只有需要调查规则治理 v1 的历史设计或证据时，才按需读取本文件、长期 Research、`evals/rule-retrieval/*`，或通过 Git / PR #74～#89 / Issue #73 恢复已移除的过程材料。

不得因为历史文档曾记录 D1 / C3 / E1 等阶段，就把这些阶段重新解释为当前 Gate。
