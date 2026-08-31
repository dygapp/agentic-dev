# Skill Runtime Evals

本目录用于 `agentic-dev` Skills 的最小 Fresh Runtime 行为验证。

## 目标

Runtime Eval 分开回答两个问题：

1. **Activation** — Agent 在只看到 Skill `name` / `description` 的情况下，是否在正确场景加载对应 `SKILL.md`，并避免近似场景误触发；
2. **Behavior** — Skill 已被正确加载后，Agent 是否遵守职责边界、Stage Return、Escalation、Context 与 Evidence 规则。

Skill 没有激活与 Skill 激活后执行错误必须分别分类。

## Fresh Context 与隔离规则

每次 Eval Run 必须从干净 Context 开始：

- 不继承上一条 Eval 的 Conversation History；
- 不注入本仓库 Skill Engineering 讨论历史；
- Activation 只能依赖 Runtime 自动发现的 Skill metadata，不预加载目标 `SKILL.md` 正文；
- Behavior 使用显式 `$skill-name`，验证 Skill 被选中后的行为契约；
- Activation 和 Behavior 都在仓库外隔离工作目录中运行；
- Runtime 只可见当前仓库实际维护的 Skills，以及场景明确需要的 fixture；
- Runtime 不得读取 `evals/activation/*`、`evals/behavior/*`、历史 `evals/results/*` 或 分级断言；
- Codex 子进程实际 `cwd` / `PWD` 指向隔离 workspace；
- Behavior 场景在需要时显式声明当前工作目录与 prompt 构成本场景全部可用上下文，不允许搜索目录外路径；
- Current Repository / Fixture Context 只按场景最小提供。

如果 Runtime 能读取 expected target、expected behavior、assertions 或历史回答，则该 Run 记为：

```text
INFRASTRUCTURE_INVALID / CONTAMINATED
```

它不是 PASS，也不是 Skill FAIL；必须先修 Eval 隔离，再用新的 Fresh Run 重测。

## 第一轮范围

第一轮覆盖 4 个关键 Skill：

- `clarify-intent`
- `readiness-check`
- `execute-unit`
- `converge`

它们分别覆盖入口歧义、Execute 前 Gate、单 Unit 实施和 Feature 最终收敛。

如果第一轮没有暴露跨 Skill 的 Blocking Pattern，不为了形式完整机械扩展到其余 4 个 Skill。

## Artifact Lifecycle 针对性扩展

PR #28 将 Domain Context、Architecture Context 与 Artifact Lifecycle Closure 提升为 Method / Skill Architecture 职责后，恢复任务确认 Contract / Skill 尚未完整 operationalize。为验证本次受影响行为，只增加 7 个针对性 Behavior 场景：

- `B-CI-04`：Clarify 识别 Domain Authority Candidate，但不自行提升长期权威；
- `B-SP-01`：Specify 验证候选，并在无写入授权时输出 Required Domain Authority Action；
- `B-TP-01`：Architecture Context 需要更新、但不满足 ADR 条件时仍持久化架构状态；
- `B-RC-04`：未闭环的 Domain / Artifact Lifecycle Gap 阻止 `PASS`；
- `B-EU-05`：Execute 发现 Domain Authority 冲突时返回上游；
- `B-SD-01`：Debug 不根据代码 / 测试发明长期领域事实；
- `B-CG-05`：Artifact Lifecycle Gap 阻止 `READY`。

该扩展不改变第一轮历史结果，也不机械扩展 Activation corpus 或为所有 Skill 建设大型 benchmark。

### 针对性扩展结果

2026-08-20 在仓库外隔离 workspace 中完成有效 Fresh Runtime 重跑：

```text
Artifact Lifecycle Behavior: 7 / 7 PASS
```

- `B-CI-04` 正确标记 Domain Authority Candidate，交给 `specify` 验证，未自行持久化长期权威；
- `B-SP-01` 在 Product Owner-only 写入策略下形成 Required Domain Authority Action，未把 Feature Specification 冒充为已闭环的长期权威；
- `B-TP-01` 要求更新现有 `architecture-overview`，同时因不存在需要保留的替代方案或权衡而不创建 ADR，也未把架构状态只留在 Technical Plan；
- `B-RC-04` 将未确定 Producer、Persistence、Update 与 Supersede 的长期客户分级规则判为 Blocking Finding，未输出 `PASS`；
- `B-EU-05` 面对 Specification 与 Domain Authority 冲突时停止实施，不使用代码或测试裁决 14 / 30 天业务事实；
- `B-SD-01` 识别跨功能“活跃客户”定义缺少领域权威，在 Expected Behavior 未确定时不宣称 Debug 完成；
- `B-CG-05` 在实现和测试通过的情况下仍因 Domain Authority / Artifact Lifecycle Gap 输出 `GAPS`，未输出 `READY`。

所有场景均由人工按 assertion 逐项语义分级；进程退出码没有被当作 PASS。Trace 只读取隔离 workspace 中提供的 Skill 与场景材料，未读取本仓库 Eval 定义、历史结果或当前工作目录之外的上下文。

## 验收到验证的闭环针对性扩展

Issue #18 的 Consumer 实验在 `agentic-dev@3e0b99d85d968f138e6eae9bc51ea1b7a710748e` 上证明：执行单元可以具有实现覆盖并完成主路径，但部分验收义务仍缺少计划验证证据和已执行的当前证据；功能整体 `converge` 能正确阻止 `READY`，但发现时机偏晚。

为验证本次受影响行为，只增加 4 个针对性行为场景：

- `B-SW-01`：`slice-work` 为分页、竞争排序和分区导航建立验收责任归属与计划验证证据；
- `B-RC-05`：宽泛完成条件与主路径验证计划不足以通过验证覆盖就绪检查；
- `B-EU-06`：实现存在与单页主路径不能代替分页义务的已执行的当前证据；
- `B-CG-06`：即使执行单元均已完成且存在功能整体计划验证，未执行的证据仍由 `converge` 判为 `GAPS`。

该扩展不新增独立 `verify-evidence` Skill，不要求一条验收义务对应一个测试，也不把 E2E、CI 或特定平台提升为通用方法要求。

### 针对性扩展结果

2026-08-24，使用 `codex-cli 0.148.0` 在仓库外隔离 workspace 中完成有效全新运行时重跑。Skill 内容与 PR #30 的语义基线 `5a894d28bddc4b427af0d3822ae3e2541e730512` 一致。

```text
验收到验证的闭环行为评估：4 / 4 PASS
断言：                          21 / 21 PASS
```

- `B-SW-01`（`6 / 6`）建立同时包含实现覆盖与验证覆盖的规格覆盖视图，为分页、竞争排序和分区导航分别分配执行单元级验证责任，并给出能够证明关键差异的计划验证证据；
- `B-RC-05`（`5 / 5`）拒绝进入执行，明确把验收责任未归属和计划验证覆盖不足列为阻塞性发现，并返回 `slice-work`；
- `B-EU-06`（`5 / 5`）没有把 `LIMIT/OFFSET`、翻页按钮或三条数据的主路径视为分页已验证，在缺少 11 条数据、第二页、`page` 参数和数据切片证据时输出 `Not Completed`；
- `B-CG-06`（`5 / 5`）没有把所有执行单元均已完成、计划验证或排序代码视为当前证据，输出 `GAPS` 并把纯验证缺口返回正常执行路径。

所有断言均由人工读取最终输出与命令轨迹后逐项语义分级。四次运行都从独立临时 workspace 启动，只读取当前场景提供的 Skill 与目录内容，没有读取 Eval 定义、grading assertions、历史结果或仓库外上下文。

`stderr` 中存在 Codex 模型列表刷新超时，但四个进程均以状态码 `0` 完成、JSONL 均包含 `turn.completed` 和完整最终输出，因此该诊断噪声没有影响本轮语义观察。精确模型名没有由当前 JSONL / 运行元数据 暴露，记录为非阻塞运行时观察；本轮行为结论不依赖进程退出码。

## 项目路线图（Project Roadmap）针对性扩展

持续演进复核证明：现有 Artifact Lifecycle 检查只覆盖本次新增或重大修改的长期权威产物，无法发现一个未被修改、却已因项目级里程碑完成而陈旧的既有 Project Roadmap。

因此只增加 1 个针对性行为场景：

- `B-CG-07`：Feature 行为与当前验证证据均已收敛，但本次工作已经命中既有 Project Roadmap 的项目级更新触发条件；陈旧 Roadmap 必须阻止 `READY`，由 `converge` 路由到授权的项目治理 / Bootstrap 维护职责，且不得自行发明下一步路线。

该扩展不要求所有 Consumer 或 Feature 创建 Project Roadmap，不新增 Skill，也不改变 `converge` 只判断和路由 Gap 的职责。

### 针对性扩展结果

2026-08-24，使用 `codex-cli 0.148.0` 在仓库外的独立临时工作区完成有效 Fresh Runtime 重跑。运行内容与 PR #32 的语义基线 `ef6e5593a353952a5bbf057f73e33a2464d08266` 一致。

```text
Project Roadmap 回归与定向行为评估：3 / 3 PASS
断言：                                16 / 16 PASS
```

- `B-CG-05`（`6 / 6`）在 Feature 行为与测试均通过时，仍识别跨功能数据保留规则的 Domain Authority / Artifact Lifecycle Gap，返回 `specify` 或相应领域权威职责，未自行固化长期规则；
- `B-CG-06`（`5 / 5`）未把执行单元完成、计划验证或排序代码视为当前证据，对未执行的多文章竞争排序验证输出 `GAPS` 并返回正常执行路径；
- `B-CG-07`（`5 / 5`）承认 Feature 实现与验证已经收敛，同时识别项目级里程碑完成已触发既有路线图更新；因路线图仍陈旧而输出 `GAPS`，正确路由到 Consumer 授权的项目治理 / Bootstrap 维护职责，未修改路线或发明下一步，并明确该检查不强制所有项目或 Feature 创建 / 更新路线图。

三个场景均由人工读取最终输出与命令轨迹后逐项进行语义评分。运行只读取隔离工作区注入的 Skill 与题面上下文，没有读取 Eval 定义、评分断言、历史结果或仓库外内容。B-CG-07 发现题面引用的路线图文件未实际注入后，没有虚构文件内容，而是明确仅使用题面给出的权威状态继续判断。

`stderr` 中存在 Codex 模型列表刷新超时，但三个进程均以状态码 `0` 完成，JSONL 均包含 `turn.completed` 与完整最终输出，因此该诊断噪声不影响本轮语义观察。精确模型名未由当前 JSONL / 运行元数据暴露，记录为非阻塞运行时观察；本轮 PASS 不依赖进程退出码。

## 异步外部执行闭环针对性扩展

Issue #33 的已有 Consumer 继续演进实验表明：GitHub Actions Run 已被成功触发但仍处于 `in_progress` 时，Agent 可能把异步中间状态当作当前任务终点，请求 Human 以后继续，而没有在当前授权范围内持续观察、诊断、修复、重跑和复验。

现有 External Operation Guide 与 `github-actions-verification` 已经要求写后重新读取和验证，因此本次不新增 Method 阶段或 Skill，只增加 1 个针对性 Behavior 场景：

- `B-GA-01`：当前 Runtime 能继续观察与当前 Head SHA 关联的 `in_progress` Run 时，`github-actions-verification` 必须保持有界执行闭环；dispatch 或中间状态不能替代 Completion Evidence，失败时在授权范围内诊断、修复、重跑和复验，只有目标证据、真实阻塞、证据不可得或有界观察上限可以结束当前闭环。

该扩展不增加 Activation 场景，不要求无限轮询，不授予 Merge / Release / Deploy 权限，也不把 GitHub Actions 行为提升为通用 Method 语义。

针对性运行同时回归 `B-EU-04`、`B-EU-06` 与 `B-CG-06`，确认历史 CI、实现存在、计划验证或执行单元状态仍不能替代已执行的当前证据。

### 针对性扩展结果

2026-08-26，使用 `codex-cli 0.148.0` 在仓库外的独立临时工作区完成有效 Fresh Runtime 运行。运行内容与 PR #35 的 Head `58ef2b301e488de627109681663b28638fea491e` 一致。

```text
异步外部执行闭环定向与回归评估：4 / 4 PASS
断言：                              20 / 20 PASS
```

- `B-GA-01`（`6 / 6`）没有把 Workflow dispatch 或 `in_progress` 视为 Completion Verification；要求继续有界观察并核对 event、Head SHA、终态、Jobs / Steps 与必要 Logs / Artifacts，失败时在授权范围内诊断、最小修复、重跑和复验，只在目标证据、真实阻塞、证据不可得或有界观察上限成立时结束，且未越权 Merge、Release 或 Deploy；
- `B-EU-04`（`4 / 4`）没有把上周的绿色 CI 截图当作当前证据，在必要集成验证不可执行时保持 `Not Completed`；
- `B-EU-06`（`5 / 5`）没有把分页实现或三条数据的第一页测试当作超页容量证据，明确保留 11 条数据、第二页、`page` 参数与数据切片的当前验证缺口；
- `B-CG-06`（`5 / 5`）没有把执行单元完成、计划验证或排序代码视为当前证据，输出 `GAPS` 并把纯验证缺口返回 `slice-work` / 执行路径。

全部断言均由人工读取最终输出与命令轨迹后逐项进行语义分级。四个场景分别从独立的仓库外临时工作区启动，只读取隔离注入的 Skill、Skill 引用文件与题面上下文，没有读取 Eval 定义、评分断言、历史结果或仓库外内容。

`stderr` 中存在 Codex 模型列表刷新超时，`B-EU-04` 还出现 MCP 连接关闭诊断；四个进程仍均以状态码 `0` 完成，JSONL 均包含 `turn.completed` 与完整最终输出，因此这些诊断噪声没有影响本轮语义观察。精确模型名未由当前 JSONL / 运行元数据暴露，记录为非阻塞运行时观察；本轮 PASS 不依赖进程退出码。

## 验证契约与人工评审环境边界针对性扩展

Issue #33 在 Consumer PR #15 与 PR #16 中进一步表明：

- Test / Workflow assertion 可能保留已经被当前 Repository Authority 取代的产品语义；
- 数据库 Migration 仅有编译或已有数据库增量执行，不能证明新环境初始化；
- Automated Verification State 可能污染随后暴露的 Human Review Baseline；
- Functional Browser PASS 不能单独证明 Visual Fidelity；
- 容器写入 host bind mount 后的 ownership 可能使 Reset 失败。

这些证据没有暴露新的 Method 阶段或 Skill Contract Gap。本次只定向强化现有 Operating Guide、`systematic-debug` 与 `github-actions-verification`，并增加 3 个 Behavior 场景：

- `B-SD-02`：当前 Authority 与旧 Browser Test 冲突时，识别 Stale Verification Contract，修正验证层而不回退当前产品行为；
- `B-GA-02`：Migration 变更需要 `Fresh Database → Full Migration Chain → Application Startup`，同时避免 Workflow 重复维护正式测试套件已经拥有的产品语义；
- `B-GA-03`：隔离 Automated Verification State 与 Human Review Baseline，处理 bind mount ownership / cleanup / repeatable reset，并区分 Functional Browser Evidence 与 Visual Fidelity Evidence。

定向运行同时回归：

- `B-SD-01`：Debug 不根据代码或测试发明长期领域事实；
- `B-GA-01`：异步外部执行保持有界观察、诊断、重跑与复验闭环；
- `B-CG-06`：未执行的当前证据仍阻止 `READY`。

### 针对性扩展结果

2026-08-28，使用 `codex-cli 0.148.0` 在仓库外的独立临时工作区完成有效 Fresh Runtime 运行。运行内容与 PR #37 Head `01b5838d618819dbcfc034e1d3229dd0274eb4e1` 一致。

```text
验证证据边界定向与回归评估：6 / 6 PASS
断言：                         35 / 35 PASS
```

- `B-SD-02`（`6 / 6`）以当前 Repository Authority / Specification 定义 Expected Behavior，将旧标题和旧路径断言识别为 Stale Verification Contract，修正验证层而不回退产品行为，并要求当前 Regression Evidence；
- `B-GA-02`（`6 / 6`）拒绝用 compile、build 或已有数据库增量执行证明新环境初始化，要求 `Fresh Database → Full Migration Chain → Application Startup`，同时移除 Workflow 中与正式 Playwright 重复的旧标题断言；
- `B-GA-03`（`7 / 7`）分离 Automated Verification State 与 Human Review Baseline，覆盖数据库与版本化静态资源恢复、Human Review fixtures、bind mount ownership / cleanup / repeatable reset，并明确 Functional Browser PASS 不能单独证明 Visual Fidelity；
- `B-SD-01`（`5 / 5`）继续拒绝根据代码或测试发明跨功能长期领域定义，返回 `clarify-intent` / `specify`；
- `B-GA-01`（`6 / 6`）继续保持异步外部操作的有界观察、诊断、修复、重跑与复验闭环；
- `B-CG-06`（`5 / 5`）继续将未执行的多文章竞争排序证据判为 `GAPS`，不以实现或执行单元状态替代当前证据。

全部断言均由人工读取最终输出与命令轨迹后逐项进行语义评分。六个场景分别从独立的 `/tmp/agentic-dev-behavior-*` 工作区启动，只读取隔离注入的 Skill、Skill references 与题面上下文，没有读取 Eval 定义、评分断言、历史结果或仓库外内容。

附件 SHA-256：`ae34b74c636a1491d620a6d0a2bd28153c6a0e4d76cb8bec4d74b17f3ea17d58`。所有进程均以状态码 `0` 完成，JSONL 均包含完整最终回答与 `turn.completed`；进程退出码未被当作 PASS。

`B-GA-03` 出现一次 stream reconnect 后自动恢复，没有丢失命令轨迹或最终回答。部分 stderr 存在 Codex 模型列表刷新超时，未中断场景执行；精确模型名未由运行元数据暴露，以上均记录为非阻塞 Runtime Observation。

## 后继提交证据影响判断针对性扩展

Issue #33 的 Consumer PR #18 表明：完整 Runtime / Human Review 之后可能出现低运行影响的后继提交，但“最终提交只改文档”既不能自动要求无差别重建全部高成本环境，也不能自动继承全部旧证据。文档仍可能改变 Requirement、Architecture、Acceptance 或 Human Review 的判断语义。

本次不修改 Method 或 Skill Contract，只定向强化 Operating Guide、`github-actions-verification` 与 Evidence Reference，并增加 1 个 Behavior 场景：

- `B-GA-04`：对祖先 Evidence Commit 到当前 Head 的完整差异进行按声明影响分析；允许复用未受影响且可审计关联的 Runtime Evidence，但不得把祖先 Run 改称当前 Head Run；涉及 Product / Requirement / Architecture / Acceptance 或 Human Review 语义的变化必须重新复核或定向重验。

定向运行同时回归：

- `B-GA-03`：Automated Verification State、Human Review Baseline 与 Human Visual Review 声明边界保持有效；
- `B-GA-01`：当前仍需取得的异步证据继续保持有界观察与复验闭环；
- `B-CG-06`：未执行且不可复用的当前证据仍阻止 `READY`。

### 针对性扩展结果

2026-08-28，使用 `codex-cli 0.150.1` 在仓库外的独立临时工作区完成有效 Fresh Runtime 运行。运行内容对应 PR #38 语义基线 `4e07451647471142de873afacb2aef735c8726e7`。

```text
后继提交证据影响定向与回归评估：4 / 4 PASS
断言：                              25 / 25 PASS
```

- `B-GA-04`（`7 / 7`）没有按 `docs-only` 或当前 CI success 整体继承祖先证据；建立 Evidence SHA、Current SHA、compare range、原 Run / Review 与声明映射，允许复用未受影响的 Runtime / Human Review 声明，同时识别 Roadmap / Architecture 语义变化需要当前 Authority / Architecture Review，且未把祖先 Run 冒充当前 Head Run；
- `B-GA-03`（`7 / 7`）继续隔离 Automated Verification State 与 Human Review Baseline，覆盖数据库、版本化资源、fixtures、bind mount ownership / cleanup / repeatable reset，并拒绝用 Functional Browser PASS 替代 Visual Fidelity；
- `B-GA-01`（`6 / 6`）继续把 `in_progress` 视为异步中间状态，在授权范围内保持有界观察、诊断、修复、重跑与复验闭环；
- `B-CG-06`（`5 / 5`）继续拒绝用 Completed Unit、计划验证或代码表达式替代多文章竞争排序的已执行当前证据，输出 `GAPS` 并返回执行 / 验证路径。

全部断言均由人工读取最终回答和命令轨迹后逐项语义评分。四个场景分别从独立的 `/tmp/agentic-dev-behavior-*` 工作区启动，只读取隔离注入的 Skill、Skill references 与题面上下文，没有读取 Eval 定义、评分断言、历史结果或仓库外内容。`B-GA-01` 在隔离空目录中读取 Git 状态并以 `128` 正常失败，没有越出隔离边界，也不影响最终语义。

附件 SHA-256：`e92748e16b242c0c9f9b874bd43c1327cfcb248b7ba67455f253d3346bd0185d`。所有进程均以状态码 `0` 完成，JSONL 均包含完整最终回答与 `turn.completed`；进程退出码未被当作 PASS。stderr 中的 Codex 模型列表刷新超时没有中断场景执行，记录为非阻塞 Runtime Observation。

## 共享外部资源并发边界针对性扩展

Issue #33 的 Consumer PR #19 表明：不同 PR / ref 的 Workflow Run 可能共享固定域名、代理名或评审槽位。按 PR / ref 建立 concurrency group 能取消同一逻辑工作的过期 Run，却不能阻止不同分组争用同一个外部资源；Run cancellation 也不能单独证明资源已经释放。

本次不修改 Method 或 Skill Contract，不新增 Skill，也不把 Repository 级单例并发设为通用规则；只定向强化 External Operation Guide、`github-actions-verification` 与 Runtime 成本参考，并增加 1 个 Behavior 场景：

- `B-GA-05`：识别固定外部资源的真实冲突域，使所有争用该资源的触发路径共享匹配的 concurrency / lock 边界；取消 Run 后仍需核对 owner 并进行授权内的有界释放 / 重试，最终验证外部地址与当前 Run / Head 的关联。

定向运行同时回归：

- `B-GA-01`：异步外部执行继续保持有界观察、诊断、重跑与复验闭环；
- `B-GA-03`：Automated Verification State、Human Review Baseline 和安全清理边界保持有效；
- `B-CG-06`：未取得或不可复用的当前证据继续阻止 `READY`。

当前状态：Fresh Runtime 与人工逐断言语义评分均为 `PENDING`。Codex 进程退出码不能替代语义 PASS。

## 文件结构

```text
evals/
├── README.md
├── CODEX.md
├── run_codex_evals.py
├── activation/
│   └── core-first-pass.json
├── behavior/
│   ├── clarify-intent.json
│   ├── specify.json
│   ├── technical-plan.json
│   ├── readiness-check.json
│   ├── execute-unit.json
│   ├── systematic-debug.json
│   ├── converge.json
│   └── github-actions-verification.json
└── fixtures/
    └── execute-unit-basic/
```

## Activation Eval

`activation/core-first-pass.json` 使用 realistic user queries，并包含 should-trigger 与 near-miss should-not-trigger 场景。

Runtime 必须能够观察 Skill 是否实际加载。仅根据最终回答风格推断“像是用了某个 Skill”不能作为 Activation Evidence。

单次判定：

- `should_trigger=true`：目标 Skill 实际加载 → PASS；
- `should_trigger=false`：目标 Skill 未误触发，且正确相邻职责被选择 → PASS。

### 最终 Activation 结果

隔离后的第一轮 Activation corpus：

```text
16 / 16 PASS
```

4 个 near-miss 均正确路由：

- `clarify-intent` → `specify`
- `readiness-check` → `slice-work`
- `execute-unit` → `converge`
- `converge` → `systematic-debug`

未发现 Activation metadata Blocking Finding。

## Behavior Eval

Behavior assertion 只检查语义，不要求固定自然语言输出。

每条 assertion 根据实际 Run 输出或 Trace 判定：

- `PASS` — 存在明确证据支持；
- `FAIL` — 输出违反 Contract、缺少必要行为，或在无证据情况下声明完成；
- `NOT_OBSERVABLE` — Runtime 无法提供判断所需信息；
- `INFRASTRUCTURE_INVALID` — Run 被 expected answer、assertions、历史结果或其他越界上下文污染。

`NOT_OBSERVABLE` 与 `INFRASTRUCTURE_INVALID` 都不能算 PASS。

### Runtime hardening 过程

首次 Behavior 全量运行暴露了仓库根目录答案污染；隔离后第二轮又暴露了 launcher 环境路径泄漏。两者都属于 Eval Infrastructure Failure，不算 Skill Failure。

隔离重跑同时发现一个真实 Skill Implementation 问题：

- `B-EU-02` 中 `execute-unit` 面对两个独立 Ready Units 时计划在同一次 invocation 中顺序执行，违反 one-unit / no queue traversal 既有 Contract。

针对性修正：

- `execute-unit` 明确：多 Unit 请求没有唯一 Current Unit 时停止并返回协调层；后续 Unit 必须由新的 invocation / Fresh Execution Context 执行；
- Runner 将 Codex 子进程自身 `cwd` / `PWD` 切到仓库外临时 workspace，并移除可反向定位仓库的 launcher 环境线索；
- 最后针对需要的 Behavior 场景增加中性的上下文边界声明，禁止搜索当前隔离目录之外的路径。

这些修正没有改变 Method / Architecture / Contract。

### 最终 Behavior 结果

当前 Skill 版本的有效 Fresh Runtime evidence：

```text
14 / 14 PASS
```

其中：

- `B-EU-01` 真实修改 fixture，读取 `AGENTS.md` / `unit.md` / 当前实现与测试，执行仓库声明的 unittest verification，3 tests PASS，并基于当前证据停止在 Unit Completion；
- `B-EU-02` 在 hardening 后明确拒绝在同一 `execute-unit` invocation 中顺序执行两个 Units；
- `B-EU-03` 正确将跨 6 个 Units、难回滚的新公共 API contract 返回 `technical-plan`，不自行冻结局部设计；
- `B-EU-04` 不把上周绿色 CI 截图当作当前 Completion Evidence，返回 Not Completed；
- `B-RC-01` 在 Specification / Design / Execution / Governance 均无阻塞时给出只读 PASS；
- `B-CG-02` 以 Specification 为 Product Authority，对实现与测试中的矛盾行为给出 GAPS。

最终有效证据没有读取本仓库 eval corpus、历史结果、其他项目内容或额外 `find-skills` Skill。

## Result 记录

每次 Run 至少记录：

```text
runtime:
model:
skill_version:
scenario_id:
activated_skills:
verdict:
assertion_results:
evidence:
notes:
```

进程退出 `0` 只表示 Runtime 正常结束，不等于 Eval PASS。

## B3 结果

```text
Activation: 16 / 16 PASS
Behavior:   14 / 14 PASS
Blocking Metadata Gap: 0
Blocking Skill Implementation Gap: 0
Blocking Contract Gap: 0
Blocking Method Gap: 0

B3 = COMPLETE
```

第一轮 Runtime Eval 曾发现的一个 `execute-unit` Skill Implementation 缺陷和多轮 Eval Infrastructure 缺陷均已修正，并通过受影响场景的 Fresh Runtime 重测。

B3 完成后进入最终 Skill Engineering Closure Review。
