# LLM Wiki 与规则治理适配分析

研究日期：2026-09-09

研究性质：**阶段 D / D1 前置对照研究**

本文只回答一个有限问题：

> LLM Wiki 的哪些思想能够解释或加强 `agentic-dev` 阶段 A～C 已经取得的规则治理 / 知识激活证据，哪些思想与当前 Repository Authority 冲突或缺乏证据，因此不应进入 D1。

本文不是规范性权威，不新增 D1 要求，不改变核心方法、架构、技能、指南或使用方项目规则。任何实际行为变化仍必须进入对应 Repository Authority，并接受当前项目的验证与集成门禁。

## 1. 当前仓库基线

本研究开始时重新核验：

- PR #86 已通过 squash merge 集成；
- 当前 `master`：`e61eddd9c83dd7925eda70ff1527367ab9059b87`；
- 当前活动里程碑：规则治理与知识激活 v1；
- 当前下一实际门禁：阶段 D / D1 — 基于证据实施指南 / 权威收敛；
- 当前没有 Open PR；
- 阶段 C 已完成 9 个可比较 A/B pair：B 直接命中 29 / 29 必需规则，3 / 3 安全回退 reason 正确，行为语义 9 / 9 PASS；A 为 8 / 9。

阶段 C 当前支持的核心结论是：

> **薄入口 + 条件检索 + 当前源指针 + 保守安全回退**

在本轮冻结高影响规则面上优于文件级粗粒度加载。

它不支持全仓库规则数据库、全量拆分指南、删除安全回退、图数据库 / MCP / Obsidian / CodeGraph 核心依赖或派生索引权威化。

## 2. 研究来源与来源层级

### 2.1 原始思想来源

Andrej Karpathy 的 `LLM Wiki` gist：

https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

这是本研究判断“LLM Wiki 原始思想”时的优先来源。该 gist 明确把自身定位为一个交给 LLM Agent 实例化的高层 idea file，而不是固定实现规范。

### 2.2 当前实现样本

`jackwener/llm-wiki`：

https://github.com/jackwener/llm-wiki

该项目把 Karpathy 模式实现为 CLI + Agent Skills，提供短 `AGENTS.md` / `CLAUDE.md` bootstrap、按需 operation skills、BM25 搜索、lint、可选向量检索和 Obsidian 兼容结构。

该实现是有价值的工程样本，但不等于 Karpathy 原始模式的规范性定义。

### 2.3 补充生态参考

`llmwikis.org`：

https://llmwikis.org/

其中 trust label、metadata、memory lifecycle 等内容属于后续社区化治理扩展，可用于观察知识生命周期设计，但不能反向归因成 Karpathy 原始 LLM Wiki 的必需组成，也不能直接作为 `agentic-dev` D1 的实施要求。

## 3. LLM Wiki 原始模式的核心结构

Karpathy 的原始模式可以概括为三层：

```text
Raw sources
    ↓
LLM-maintained Wiki
    ↓
Schema / AGENTS.md / CLAUDE.md
```

其中：

- Raw sources 是人工选入的原始材料，保持不可变；
- Wiki 是 LLM 持续维护的 Markdown 综合知识层；
- Schema 规定目录、约定与 ingest / query / lint 等工作方式；
- `index.md` 用于先找到相关页面，再继续深入读取；
- `log.md` 保存知识库演进活动；
- query 产生的高价值综合可以回写 Wiki，使知识持续积累；
- lint 用于发现矛盾、陈旧内容、孤立页面、缺失交叉引用与知识空洞；
- 到更大规模后才考虑搜索引擎、BM25 / vector 等辅助能力。

这套设计的核心目标是：

> 不要每次从原始资料重新推导全部知识，而是让长期综合知识持续积累并保持可导航。

## 4. 与 agentic-dev 当前问题真正一致的部分

### 4.1 薄启动入口

Karpathy 模式把 schema / Agent 入口作为操作约定；`jackwener/llm-wiki` 进一步把 `AGENTS.md` / `CLAUDE.md` 明确做成只有几十行的 bootstrap，并把详细操作分散到按需加载的 operation skills。

这与阶段 C 已验证的“薄入口 + 条件加载”方向一致。

对 D1 的意义不是复制其文件结构，而是加强当前已有判断：

> 常驻入口负责告诉 Agent 当前是什么、最重要的不变量是什么、去哪里取得条件性知识；不应继续承担全部规则正文。

### 4.2 索引优先，而不是默认扫描全部内容

Karpathy 原始模式建议 query 时先读 `index.md`，找到相关页面后再深入读取。

这与当前 B1～C3 的稀疏查询 / 源指针模型高度同型：

```text
当前任务
→ 最小导航 / 检索
→ 当前规范性源
→ 只读取真正适用的规则
```

因此 LLM Wiki 为当前“导航与知识正文分离”提供了独立外部参考，但 D1 仍以阶段 C 的仓库内 A/B 证据为直接实施依据。

### 4.3 派生知识必须能够回到来源

LLM Wiki 原始模式保留 raw source 与 wiki 两层，说明“导航 / 综合知识”与“原始来源”不是同一层。

这与 `agentic-dev` 已冻结的“派生索引不是 Authority、结果必须回指当前规范性源”具有结构相似性。

可吸收的原则是：

> 派生导航能力可以存在，但必须能回到当前来源，且不能因为导航方便就遮蔽来源身份。

### 4.4 知识健康检查值得作为后继候选

Karpathy 的 lint 会检查矛盾、陈旧 claim、孤立页面、缺失引用和知识空洞；`jackwener/llm-wiki` 也把 lint 独立为按需 operation。

这与当前已经出现的以下长期治理问题有潜在对应：

- 已取代规则仍被活动入口引用；
- 派生索引来源陈旧；
- 跨权威重复 / 冲突；
- 指针失效；
- 规则存在但没有消费者或可发现入口。

但是阶段 C 没有验证“Governance Lint”是当前 D1 的必要实施，因此它只能作为后继候选，不能借 LLM Wiki 研究直接进入 D1。

## 5. 不能直接映射到 agentic-dev 的部分

### 5.1 LLM Wiki 的 Wiki 层不能成为新的 Repository Authority

Karpathy 原始模式中，raw sources 是 source of truth，LLM-maintained Wiki 是长期综合层。

`agentic-dev` 的结构不同：

```text
Method / Architecture / Contract / Guide / Project Authority
= 已经是可执行的规范性长期知识
```

如果再增加：

```text
Repository Authority
    ↓
LLM-generated Wiki
    ↓
Agent
```

会出现第二套长期语义：

- Wiki 综合可能与当前 Authority 漂移；
- Agent 可能开始优先相信综合页而不是规范性源；
- 同一规则产生两份需要同步的长期文本；
- 当前已经验证的 source pointer + stale fallback 边界被弱化。

因此 D1 不应增加新的 `wiki/` 权威或综合层。

### 5.2 Query 结果不能自动晋升为长期规则

Karpathy 模式鼓励把有价值 query synthesis 回写 Wiki，让探索持续累积。

对个人知识库这是核心收益；对 `agentic-dev` 规范性规则治理则存在明显冲突。

当前仓库要求：

```text
外部资料 / 运行证据 / 对话发现
→ Research / Evidence
→ 判断是否形成稳定规则
→ 进入对应 Authority
→ 验证 / 复核 / 集成
```

因此：

> 对话中的有价值综合可以进入 Research / Evidence，但不能因为“值得保存”就自动变成 Method / Guide / Skill 的长期规则。

这也是本研究本身被放入 `docs/research/*` 而不是直接修改 Authority 的原因。

### 5.3 “Raw source 永久不可变”不能机械套用

LLM Wiki 的 raw source 不可变是为了保留原始证据。

`agentic-dev` 的规范性文件本身必须随项目演进修改；Git 历史已经承担版本追溯职责。因此不应为了模仿 LLM Wiki 再建立一套只读 raw 副本。

需要保持不可变 / 可追溯的是具体评估证据和外部来源身份，而不是所有规范性文档的复制品。

### 5.4 Operation Skills 不构成新增核心 Skill 的证据

`jackwener/llm-wiki` 把 ingest / query / lint / research 拆成四个 operation skills，是其知识库产品的职责选择。

`agentic-dev` 不应据此新增：

- `knowledge-query`；
- `knowledge-lint`；
- `research`；
- `ingest`；
- 新的超级知识技能。

是否技能化仍必须满足当前 Engineering Capability Architecture 的独立职责、稳定契约与验证证据。

### 5.5 搜索 / 图 / Metadata 不能提前升级成基础设施

Karpathy 原始模式明确指出：中等规模时 `index.md` 已经可以有效工作，只有规模增长后才需要更强搜索。

`jackwener/llm-wiki` 当前增加 BM25、可选 vector、wikilink graph；`llmwikis.org` 还进一步发展出较丰富 metadata / trust lifecycle。

这些实现说明存在可扩展路径，但当前 `agentic-dev` 的阶段 C 证据仍只支持最小派生索引与薄查询器。

因此 D1 不新增：

- 全仓库统一 Front Matter；
- BM25 / vector database；
- 知识图数据库；
- MCP knowledge server；
- Obsidian 强依赖；
- 大型 trust / status taxonomy。

## 6. D1 决策映射

| LLM Wiki 思想 / 实现 | 当前 agentic-dev 证据 | D1 处理 |
|---|---|---|
| 薄 `AGENTS.md` / schema bootstrap | 与 C3 薄入口结果一致 | **支持现有 D1 收敛，不新增独立机制** |
| 先索引再按需深入 | 与 B1～C3 稀疏检索 / source pointer 一致 | **支持** |
| 派生层保留来源追溯 | 与 derived index / current source pointer 一致 | **支持** |
| stale 时不继续信任旧导航 | 与 C1～C3 fail-closed fallback 一致 | **必须保持当前安全边界** |
| lint 矛盾 / 陈旧 / orphan | 有长期治理价值，但 C 阶段未验证必要性 | **后继候选** |
| Query 综合自动回写长期 Wiki | 与 Authority promotion / review 边界冲突 | **不采用** |
| 新建 LLM-maintained Wiki 层 | 可能形成第二事实来源 | **不采用** |
| ingest / query / lint / research 四技能 | 不构成当前技能准入证据 | **不采用** |
| 全量 Front Matter / trust taxonomy | 当前没有必要性证据 | **不采用** |
| BM25 / vector / graph / MCP | 当前最小原型已足够进入 D1 | **不采用** |
| Obsidian 作为 IDE / Graph UI | 仅有人类治理价值 | **保持可选，不进入核心依赖** |

## 7. 对 D1 的实际影响

本次研究**没有发现需要改变 D1 范围的新需求**。

它主要起两个作用：

1. 为阶段 C 已经得到的“薄入口 + 条件检索 + 当前源指针 + 安全回退”提供一个独立外部设计对照；
2. 提前阻止一种可能的过度实现：因为 LLM Wiki 很适合个人 / 团队知识综合，就误把 `agentic-dev` 的 Repository Authority 再投影成一套新的 LLM-maintained Wiki 权威。

因此 D1 仍应只依据当前 A～C 证据实施：

- 缩减不需要常驻的规则正文；
- 保留少量真正跨任务不变量；
- 增加更精确的当前源 / 段落级激活指针；
- 对已经证明高价值的重复规则做减法；
- 保持 derived index 非权威；
- 保持 stale / unknown / no-match 的 fail-closed fallback；
- 不因本研究新增规则图、MCP、数据库、统一 metadata 或新 Skill。

## 8. Research 固化判断

本次分析值得进入 `docs/research/*`，原因不是 LLM Wiki 本身“足够流行”，而是：

- 它在 D1 实施前提供了直接相关的外部对照；
- 它同时提供“可吸收思想”和“不可照搬结构”；
- 后续需要能够追溯为什么 D1 选择薄入口 / 指针而没有建立第二 Wiki / 图数据库；
- 如果只留在聊天中，新的上下文容易只记住“LLM Wiki 很适合知识管理”，而丢失与 Repository Authority 的关键不兼容边界。

但不应把它加入所有新上下文的常驻恢复清单。它只是 D1 的定向研究输入；D1 收敛完成后，长期行为应由最终 Authority 自身表达。

## 9. 结论

LLM Wiki 对 `agentic-dev` 最有价值的不是“建立 Wiki”，而是以下更小的思想：

```text
薄入口
→ 先导航
→ 按需读取
→ 保留来源
→ 持续检查陈旧与冲突
```

其中前四项已经被阶段 B / C 的仓库内证据独立验证；第五项适合作为后继治理候选，但当前不属于 D1 已验证实施范围。

因此当前正确动作是：

> **把 LLM Wiki 作为 D1 的受限 Research 对照，而不是新的知识架构。继续按阶段 C 证据推进 D1，不扩大当前里程碑。**
