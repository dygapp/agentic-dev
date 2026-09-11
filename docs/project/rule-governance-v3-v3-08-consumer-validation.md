# V3-08 — Consumer 验证与持续有效性复核

**状态：** Gate A — Validation Design Candidate  
**跟踪：** Issue #115  
**agentic-dev 启动基线：** `master@2fe193035c629f6b8805fd473bd322f70fe6e172`

## 1. 目的

本文把 V3-08 的真实 Consumer 验证设计固化为可恢复的项目级 Evidence / Planning 记录。

V3-08 不重新定义：

- 使用方生命周期；
- Agent 资源模型；
- 资源发现架构；
- `agentic-dev` 自采用机制；
- Consumer 产品事实。

长期规范语义继续由以下 current owner 持有：

- `docs/architecture/consumer-lifecycle.md`；
- `docs/architecture/agent-resource-model.md`；
- `docs/architecture/resource-discovery-architecture.md`。

本文只回答：如何用真实 Consumer 验证这些语义在采用、升级、普通运行、currentness、失败关闭、上下文成本和后续演进中是否实际成立。

## 2. Repository Boundary

### 2.1 `agentic-dev`

本仓库负责：

- 定义 V3-08 验证矩阵与 Evidence Contract；
- 读取真实 Consumer 当前状态；
- 接收 Consumer 运行证据；
- 分类 reusable / Consumer-only findings；
- 如有必要，修改 `agentic-dev` 自身长期 owner 并重新验证。

### 2.2 `dygapp/jilinjobs-cms`

V3-08 选定的主要真实 Consumer 为：

`dygapp/jilinjobs-cms`

本 `agentic-dev` 会话只读该仓库，不创建 Consumer Branch、Commit、PR，不修改 Consumer Authority / Code / Workflow。

需要执行 baseline upgrade、建立 Consumer-local candidate discovery asset、做受控 drift / fail-closed 实验时，必须在 `jilinjobs-cms` 独立会话 / Repository Authority 下执行。

Consumer Evidence 回流到 Issue #115 或后续专门 Evidence 载体；Consumer Evidence 不自动修改 `agentic-dev` Authority。

## 3. 当前真实 Consumer snapshot

### 3.1 Repository / active work

V3-08 Gate A 恢复时观察到：

- Consumer：`dygapp/jilinjobs-cms`；
- 当前 `main`：`989405a0006eafd52f361d391ebefe0d55c8014e`；
- 该提交集成 Rich Text V2 Planning / EU-54 Candidate Authority；
- Open implementation PR：#138 — `EU-54 — Rich Text V2 Mature Editor Adoption`；
- PR #138 的 Execute baseline：`main@989405a0006eafd52f361d391ebefe0d55c8014e`；
- Issue #60 Current Evidence 已记录：EU-54 `Readiness PASS / Execute Authority GRANTED`；
- Issue #137 是 Page Content Architecture 的独立 Planning Capture，不属于 EU-54 scope。

PR #138 的具体 Head、Checks、Review Environment 与 Human Review 状态属于高频 GitHub Current Evidence，V3-08 不把某个瞬时 Head 固化为长期 Consumer Authority；运行时必须重新读取。

### 3.2 Consumer 当前采用的 agentic-dev baseline

Consumer 当前 `AGENTS.md` 与 `docs/project/development-method.md` 声明：

```text
agentic-dev evaluated baseline:
master@d9fad0da83dbdb61cac5eb9778b0258c6861eef1
```

V3-08 candidate upstream baseline：

```text
master@2fe193035c629f6b8805fd473bd322f70fe6e172
```

精确比较结果：

```text
d9fad0d... → 2fe1930...
ahead_by = 34
behind_by = 0
```

该 delta 同时包含：

- 可复用长期能力变化：使用方生命周期、资源模型、资源发现架构、Guide / Skill / Engineering Capability 所有权收敛等；
- `agentic-dev` 自身 Project / Roadmap / Research / Eval / self-discovery 资产；
- 历史设计 / Evidence。

因此 V3-08 禁止把“candidate baseline 更新”简化为复制 34 个提交或完整 upstream 文档树。

### 3.3 Consumer 当前本地恢复入口

当前 Consumer 明确的 Fresh Context 恢复链为：

```text
AGENTS.md
→ README.md
→ docs/README.md
→ docs/project/project-roadmap.md
→ docs/project/development-method.md
→ 当前任务直接相关 Authority / Work / GitHub Current Evidence
```

其中 `docs/README.md` 已经承担 Documentation Authority Map；当前没有独立名为 Local Discovery Entry、Activation Manifest 或 Runtime Catalog 的资产。

### 3.4 当前静态状态漂移是现成验证样本

当前 `main` 中：

- `docs/work/current/README.md` 仍写 `Current Ready Execution Unit = NONE`、EU-54 `Readiness PENDING`；
- `docs/work/current/eu54-rich-text-v2-mature-editor-adoption.md` 仍写 `Readiness PENDING / Execute Authority NOT GRANTED`；
- Issue #60 Current Evidence 已记录 EU-54 `Readiness PASS / Execute Authority GRANTED`；
- PR #138 已存在并处于 implementation 生命周期。

这不是 V3-08 人工制造的错误，而是一个真实的“稳定 locator / Planning artifact 正文变化频率低于 GitHub Current Evidence”的 Consumer 场景。

V3-08 将它作为 `current-locator` 语义验证样本：

> 高频 Current Gate 不能因为静态文档摘要暂未回写就被旧值反向覆盖；Fresh Context 必须重新读取 GitHub Current Evidence，并按 Consumer Repository Authority 判断真实当前状态。

它不自动证明这些静态文件本身应删除或被视为 defect；是否需要后续 Consumer 状态治理调整属于 Consumer-local 结论。

## 4. Context-cost observation baseline

当前 GitHub 文件大小：

| 默认入口文件 | bytes |
|---|---:|
| `AGENTS.md` | 22,413 |
| `README.md` | 7,367 |
| `docs/README.md` | 5,732 |
| `docs/project/project-roadmap.md` | 17,956 |
| `docs/project/development-method.md` | 37,516 |
| **合计** | **90,984** |

这还不包含：

- 当前 Requirement / Specification / Technical Authority；
- Current Work；
- Issue / PR / Actions；
- Code / Tests；
- supporting method notes。

因此 Gate A 固定一个可证伪假设：

> 普通状态恢复不应机械加载完整 37 KB+ Consumer-local Development Method。Consumer 如果能够从稳定 Bootstrap / Documentation Authority Map / Roadmap / GitHub Current Evidence 恢复当前 Gate，应允许在进入职责 / capability discovery 前停止。

V3-08 不以减少 bytes 为唯一目标。任何精简都必须先保证 correctness、Authority、fail-closed 与必要能力召回。

## 5. 为什么不在 EU-54 执行期间做 Consumer 写实验

当前 EU-54 已有独立 Execute Authority 和 Draft implementation PR #138。

V3-08 baseline upgrade 会触达：

- Consumer `AGENTS.md`；
- Consumer-local Development Method；
- Fresh Context / discovery entry；
- 可能的 Consumer-local Reviewed Discovery Map；
- baseline / provenance 记录。

这些都是跨后续工作的治理资产，不属于 EU-54 产品实现 scope。

因此 Gate A 采用：

```text
EU-54 执行期间
→ 只读旁路观测
→ 不修改 Consumer

EU-54 自然 closure 后
→ 重新读取最新 Consumer main / Authority
→ 从届时 exact main 建立独立 V3-08 Consumer experiment branch
→ 再执行 baseline upgrade / local projection validation
```

这样避免：

- 方法升级与当前产品 Execute PR 并发改变共同 Bootstrap；
- V3-08 反向扩大 EU-54 scope；
- V3-08 Evidence 与 EU-54 Current Evidence 混为同一 claim。

## 6. Gate A 验证总体结构

V3-08 分四个轨道。

### Track A — Pre-upgrade read-only observation

目标：记录 Consumer 在旧 evaluated baseline 下的真实普通运行和 currentness 行为，形成对照组。

不修改 Consumer。

### Track B — Existing Consumer explicit baseline upgrade

目标：EU-54 closure 后，在独立 Consumer experiment branch 上把 evaluated upstream baseline 从 `d9fad0d...` 比较到 `2fe1930...`，逐项分类、投射、验证。

### Track C — Post-adoption ordinary runtime / fail-closed

目标：验证采用完成后的 Fresh Context、routing-only、execute、supporting capability、currentness、coverage drift 与 local-only runtime。

### Track D — Sustained-validity real evolution

目标：不为 V3-08 人造产品任务。baseline upgrade 进入 Consumer current state 后，优先使用真实后续 Planning：Issue #137 Page Content Architecture，观察新的 Fresh Context / Planning / capability discovery 是否持续有效。

如果届时 Consumer Authority 改变顺序或 Issue #137 不再是下一真实工作，则 Track D 选择当时第一个真实后续工作，并记录原因；不为了守住预设编号扰乱 Consumer Roadmap。

## 7. Track A — Pre-upgrade observation matrix

| ID | 场景 | 输入 | 预期 | Evidence |
|---|---|---|---|---|
| A-01 | 状态恢复 | current `main` + AGENTS / README / docs map / Roadmap / GitHub | 能识别 EU-54 已 Readiness PASS / Execute，不能被静态 PENDING 摘要反向覆盖 | 实际读取清单 + current verdict + source precedence |
| A-02 | 状态-only stop | 只问当前工作 / Gate | 不要求打开完整 upstream；若本地 + GitHub 已足够，应避免完整 Method / Skills preload | 文件数 / bytes / 是否跨仓读取 |
| A-03 | routing-only | 判断 EU-54 当前 primary responsibility | 返回 Execute / current work locator；不因为“SunEditor/Vue/GitHub”批量加载所有能力 | primary + supporting locator + loaded sources |
| A-04 | supporting capability | PR #138 需要 GitHub Actions / Human Review / Vue / verification 时 | supporting capability 不夺取 EU-54 primary responsibility | candidate / supporting 解析结果 |
| A-05 | stale current summary | Work artifact PENDING vs GitHub PASS | current-locator / Current Evidence 语义正确；不把 no-match / old summary 当 current truth | conflict resolution trace |

Track A 只形成 baseline observation，不因为旧方案行为可工作就判定 V3-08 PASS。

## 8. Track B — Existing Consumer baseline upgrade matrix

Consumer experiment 必须从 **EU-54 closure 后届时最新 `main`** 创建；不得预先固定当前 `989405a...` 为写实验 base。

上游候选 baseline 固定：

`agentic-dev@2fe193035c629f6b8805fd473bd322f70fe6e172`

前一 evaluated baseline：

`agentic-dev@d9fad0da83dbdb61cac5eb9778b0258c6861eef1`

### B-01 — Exact baseline recovery

必须重新确认 Consumer current baseline 仍是 `d9fad0d...`；若 EU-54 closure 前已有其他会话完成 baseline upgrade，则停止复用本设计中的“previous baseline”，重新比较当前 Consumer Authority。

### B-02 — Delta classification

对 reusable delta 逐项作：

```text
adopt
retain / override
reject / not applicable
supersede / remove
```

最低分类边界：

#### 必须作为 reusable candidate 评估

- Consumer Lifecycle；
- Agent Resource Model；
- Resource Discovery Architecture；
- V3 后的 Skill identity / admission / supporting-resource boundary；
- verification / external-operation 等仍会持续约束 Consumer 的 reusable owner 变化；
- 当前 Consumer 真正需要的 terminology / evidence / integration changes。

#### 默认 project-only / non-runtime，不得机械投射

- `agentic-dev/AGENTS.md` 的项目状态；
- `agentic-dev/README.md` 当前里程碑；
- `agentic-dev/docs/project/project-roadmap.md`；
- V3 项目 Issue / PR / planning state；
- `agentic-dev/docs/discovery/*` 的**本仓库实例**；
- Research / Eval 结果本身；
- rejected / historical design documents。

“默认不投射”不等于不允许把其中已被长期 owner 吸收的 reusable 结论通过真实 owner 采用。

### B-03 — Baseline / provenance separation

实验必须分别记录：

- previous evaluated upstream baseline；
- candidate evaluated upstream baseline；
- active Consumer-local asset provenance（如需要）；
- upgrade-only decision history。

禁止用一个“baseline = 2fe1930...”声明暗示所有 upstream 文件都已采用。

### B-04 — Local Discovery Entry decision

优先评估**复用现有 `docs/README.md`** 作为 Consumer Local Discovery Entry，因为它已经是 Documentation Authority Map / Fresh Context 入口。

只有现有入口职责无法保持薄、无法安全到达 current local capability discovery 时，才新增独立入口文件。

不得为了与 `agentic-dev/docs/discovery/README.md` 路径一致而复制目录结构。

### B-05 — Reviewed Discovery Map necessity decision

当前证据形成强候选假设：Consumer 很可能需要一个本地 Reviewed Discovery Map，因为：

- `development-method.md` 约 37.5 KB；
- `docs/project/` 已存在多个跨职责 method / review / execution / evidence / git / scope 规则；
- Vue / verification / GitHub Actions / external operation / migration / Human Review 等条件性能力长期横切不同 EU；
- 当前普通 Fresh Context 通过大文档预加载解决发现问题，成本较高。

但 Gate B **不得把 Map 设为预设答案**。Consumer session 必须先完成本地资源 inventory：

- 若稳定入口 + 原生 resource identity 已能可靠定位，记录“不需要 Map”；
- 若需要跨资源正规化，建立一个 Consumer-local Reviewed Discovery Map candidate；
- 不建立 Runtime View / Catalog，除非测量证明 Map 本身成为显著固定成本。

### B-06 — Failure / interruption semantics

在 Consumer candidate 尚未完成本地投射与验证前：

- 不推进 Consumer 记录的 evaluated baseline；
- 不删除旧 current local owner；
- 不把 branch candidate 描述为 Consumer current；
- 若实验失败，Consumer `main` 继续按旧本地规则工作。

## 9. Track C — Post-adoption runtime matrix

只有 Track B candidate 完成本地验证后才能执行。

| ID | 场景 | 预期 |
|---|---|---|
| C-01 | 状态-only Fresh Context | 只从 Consumer stable Bootstrap / Current Authority / GitHub 恢复；不读 upstream，不默认加载完整 Method |
| C-02 | routing-only | 返回一个 primary responsibility + 最小 supporting locator；不加载完整 Skill / owner 正文 |
| C-03 | execute | 只加载当前 primary procedure / local owner + 真实命中的 supporting context |
| C-04 | Consumer-specific override | 本地 Requirement / Architecture / Verification / Workflow rule 优先于 reusable default |
| C-05 | Stage Return | 原 Method / Skill owner 判定返回后，旧 discovery decision 失效并重新发现 |
| C-06 | semantic-reviewed drift | 若使用 Map，source 语义 identity 变化后旧提示退出可信范围，不允许只刷新 hash |
| C-07 | membership drift | 若使用 Map，新增 / 删除 / 重分类 local capability 后受影响 coverage 先 stale |
| C-08 | missing source / selector | fail-closed 到 Consumer Current Authority，不按近似文件名 / upstream latest 猜测 |
| C-09 | ambiguity | 无法可靠判断 primary 时停止高影响动作，按 Consumer Authority 升级而不是模型概率猜测 |
| C-10 | no-match + governance fact | 不解释为“无规则”；扩大最小本地读取 |
| C-11 | ordinary runtime | upstream 新提交不改变 Consumer current runtime |
| C-12 | rejected / historical decision | 不进入 ordinary Fresh Context |

如果 Consumer 不采用 Map，则 C-06 / C-07 改为验证实际采用的等价 local discovery currentness 机制；不得为了覆盖用例强制造 Map。

## 10. Controlled negative tests

只有在独立 Consumer experiment branch、且不影响正在执行的产品工作时允许执行。

如果采用 Reviewed Discovery Map，至少用受控、可回滚的实验提交验证：

1. **semantic source drift**：改变一个实验性或可安全复原的 semantic owner，Map 应 stale；
2. **membership drift**：在实验 inventory 增加 / 删除一个明确实验资源，coverage 应 stale；
3. **missing selector**：让一个实验 locator 失效，应 fail-closed；
4. **ambiguous primary**：构造两个无法安全区分的候选，不得随机选择；
5. **no-match + known risk**：存在明确 governance fact 时空结果不得解释为无规则。

这些变更全部是实验分支证据，不允许因 V3-08 测试需要进入 Consumer 产品 `main`。

## 11. Track D — Sustained-validity real evolution

### 11.1 首选真实样本

当前 Consumer 的真实后续 Planning Capture：

Issue #137 — Page Content Architecture & Special Page Rendering。

它明确要求 EU-54 closure 后重新从当时 Repository Current Authority 进入 Planning，并包含 Rich / Structured / Engineering / Embedded Page 的架构判断。

如果 baseline upgrade 在 EU-54 closure 后完成并成为 Consumer current，Issue #137 是理想 post-adoption 样本，因为它会真实触发：

- Product / Architecture reasoning；
- current Requirement / Specification formation；
- Technical Planning；
- Vue / Public Renderer / Site Package 等 supporting context；
- 后续 `slice-work → readiness-check`；
- GitHub external-operation / evidence / Human Review boundary。

### 11.2 持续有效性判据

至少确认：

- Fresh Context 能从本地入口恢复真实 current Planning Gate；
- 不因为 upstream V3-08 仍在进行就在线读取 `agentic-dev` 当前项目状态；
- 新增 / 修改的 Consumer resource 能被本地 discovery currentness 机制感知；
- `AGENTS.md` / README / Method 不因本轮升级再复制一套完整 routing 表；
- baseline upgrade history / rejected items 不进入普通 Context；
- 多轮 Consumer 状态变化不会要求同步更新大量无语义价值的 metadata；
- 一次真实后续工作仍能保持 primary responsibility + minimal supporting context。

如果 Issue #137 届时不再是当前真实下一工作，使用当时第一个真实后续 Planning / Execute 场景，并在 Evidence 中记录替代原因。

## 12. First-adoption coverage

`jilinjobs-cms` 是成熟 Existing Consumer，不适合把当前仓库伪装成“新项目首次采用”。

V3-08 不通过删除其现有 baseline / Authority 来制造首次采用证据。

首次采用语义采用次级隔离轨道：

- 在 Gate B 完成后，如果现有真实证据不足，建立**最小隔离 Consumer fixture**；
- fixture 只包含最小 Repository Authority / README / 一个真实工作目标，不复制 `agentic-dev` 目录树；
- 验证初始化 → per-item adoption → local projection → adoption verification → local-only ordinary runtime；
- fixture 只提供生命周期 / discovery 行为证据，不替代 `jilinjobs-cms` 的真实 Existing Consumer 证据。

是否需要该 fixture 在 Track B / C Evidence 后再判断；若真实 Existing Consumer 证据已经充分覆盖同一语义，不为了数量机械扩大评估。

## 13. Evidence Contract

每个执行场景至少记录以下字段；物理格式可由 Consumer 实验实现决定，不要求统一 JSON。

```text
scenario_id
track
consumer_repository
consumer_base_sha
consumer_candidate_branch
consumer_candidate_head
previous_evaluated_upstream_baseline
candidate_upstream_baseline
current_goal
current_authority_inputs
expected_primary_responsibility
expected_supporting_sources
actual_sources_read
actual_primary_responsibility
actual_supporting_sources
full_skill_or_owner_loaded
upstream_access_during_ordinary_runtime
source_currentness_result
coverage_result
stage_action
fail_closed_result
context_file_count
context_bytes_or_equivalent_measure
verification_evidence
consumer_integration_state
finding_classification
notes
```

### 13.1 Evidence classification

每个 finding 必须归入：

1. `covered` — 当前 v3 架构已正确覆盖；
2. `consumer-only` — 只属于 Consumer 项目治理 / IA / workflow；
3. `mapping-defect` — local / reusable discovery mapping defect；
4. `lifecycle-resource-discovery-defect` — reusable V3 architecture defect；
5. `efficiency-opportunity` — correctness 成立但 context / maintenance cost 有改进空间；
6. `future-candidate` — 有信号但当前证据不足。

Blocking / Medium 不得通过标记 `future-candidate` 跳过。

## 14. Context-cost measurement

至少比较三个状态：

### Baseline P0 — 当前 pre-upgrade

记录当前声明的默认 Fresh Context 路径文件数 / bytes，以及真正完成状态恢复实际需要的最小集合。

已知静态起点：5 个默认入口文件合计约 `90,984 bytes`。

### Candidate P1 — baseline upgrade / local projection

记录：

- Bootstrap / Local Discovery Entry；
- Map（若存在）；
- baseline upgrade 专用 inputs；
- 不把一次 upgrade 成本混入 ordinary runtime 成本。

### Ordinary P2 — post-adoption

分别测：

- state-only；
- routing-only；
- execute；
- one / multiple supporting condition。

目标不是固定百分比，而是同时满足：

- correctness 不下降；
- 必需 rule / capability 不漏召回；
- state-only 与 routing-only 不因“保险”全量加载大 Method / Skills；
- 没有为了节省 token 引入第二规范正文或静默模型猜测。

## 15. Gate A 完成定义

Gate A 只有同时满足以下条件才可声明 Ready：

- Primary real Consumer = `dygapp/jilinjobs-cms` 已明确；
- pre-upgrade read-only snapshot 已建立；
- previous evaluated baseline 与 candidate upstream baseline 已精确固定；
- 当前 active Consumer work / PR 已恢复，且 V3-08 不干扰 EU-54；
- baseline-upgrade 写实验明确延后到 EU-54 natural closure 后的 latest main；
- Track A～D 场景与成功 / 失败判据明确；
- Evidence Contract 明确；
- controlled negative test 边界明确；
- context-cost baseline / measurement 方式明确；
- Consumer write / integration / cleanup 权限边界明确；
- first-adoption 不通过破坏成熟 Consumer 状态伪造；
- 没有开始 Consumer write experiment；
- 没有提前声明 V3-08 PASS。

## 16. Gate A 后的 Consumer handoff contract

Gate A 通过后，Consumer 独立会话应先重新读取：

- 当时最新 `jilinjobs-cms/main`；
- Open PR / Issue / Actions；
- `AGENTS.md`、README、`docs/README.md`、Roadmap、Development Method；
- EU-54 是否已经完成 / Execute Authority 是否终止；
- Consumer 当前记录的 exact `agentic-dev` evaluated baseline；
- `agentic-dev@2fe193035c629f6b8805fd473bd322f70fe6e172` 的 V3-03～V3-07 直接 reusable owner。

如果 EU-54 尚未完成：

> 只做 V3-08 Track A 只读观察，不创建 baseline-upgrade branch。

如果 EU-54 已完成且没有新的 conflicting active Execute work：

> 从当时 latest Consumer main 创建独立 experiment branch，执行 Track B → C；只有通过 Consumer-local adoption verification 后才进入是否集成 baseline upgrade 的 Consumer 决策。

任何 Consumer merge 都服从 Consumer Repository Authority / Human Authority；V3-08 Planning Authority 不授予 Consumer merge 权限。

## 17. 当前 Gate

当前：**Gate A design candidate 已形成；Consumer write execution 尚未开始。**

下一实际步骤：

1. 对本 Gate A 设计执行风险复核；
2. 固化协调计划与稳定 V3-08 恢复入口；
3. 若 Gate A 无 Blocking / Medium，记录 Gate A PASS；
4. 生成 Consumer 独立会话的精确 handoff；
5. 在 Consumer EU-54 closure 前只允许 Track A 只读 Evidence；
6. 不提前进入 Track B Consumer 写实验。