# Consumer-local Runtime 真实验证计划 v2

## 状态

**Phase F 验证计划 — 待真实 Consumer 执行**

上层里程碑：Issue #92 / `docs/project/rule-governance-knowledge-activation-v2.md`

正式 reusable input：

- `docs/guides/consumer-local-rule-activation.md`
- `docs/guides/using-agentic-dev.md` §6.1
- 当前正式 Skill / Engineering Capability，只按 Consumer 实际采用需要读取

设计 / 评分 Authority：

- `docs/project/consumer-local-rule-runtime-acceptance-v2.md`
- `docs/project/consumer-local-activation-metadata-contract-v2.md`
- `docs/project/consumer-local-runtime-routing-interface-v2.md`
- `docs/project/consumer-local-baseline-adoption-projection-v2.md`

本文只定义 `agentic-dev` 侧的验证要求与交接边界，不授权本仓库会话修改 Consumer Repository。

## 1. 验证目标

Phase F 必须证明当前 v2 不是只在 `agentic-dev` 仓库内部成立，而能够被真实 Consumer 选择性采用并长期本地运行。

核心判断：

> 一个新的 Consumer Fresh Context，在完成显式 adoption / projection 后，是否可以只依赖 Consumer Repository 与本地 capability set，正确发现 Consumer-native Authority 与 adopted reusable capability，确定 primary responsibility、按需加载 Skill、正确 Stage Return / fail-closed，并且不把 upstream 作为 ordinary runtime 依赖？

只有真实 Consumer 证据通过后，v2 才能进入 Phase G。

## 2. Consumer 选择

首个真实 Consumer 使用：

`dygapp/jilinjobs-cms`

这是现实使用样本，不是所有 Consumer 的固定模板。

开始验证时必须从 GitHub 重新读取其当前 `main`、Open PR / Issue、相关 Actions、`AGENTS.md`、`README.md`、Documentation Authority Map、Project Roadmap 与 Consumer-local Development Method；不得把本文记录的任何 Consumer commit、阶段或工作状态直接视为当前事实。

`agentic-dev` candidate baseline 也必须在验证开始时重新解析：

```text
repository: dygapp/agentic-dev
candidate ref: docs/rule-governance-knowledge-activation-v2
candidate exact head: <validation-start-time resolution>
```

不得在本文中固定一个会随当前 v2 分支继续演进而立即陈旧的 Head。

## 3. Repository Boundary

### Consumer Repository

实际修改、分支、提交、PR、Actions、隔离运行与验证只能在新的 `jilinjobs-cms` 授权上下文中按其当前 `AGENTS.md` 执行。

### agentic-dev Repository

Consumer 验证期间：

- 作为候选 reusable capability / method source 读取；
- 可以向 Issue #92 / #58 回传验证证据；
- 不允许 Consumer 会话静默修改 `agentic-dev` 正式文件；
- 如果验证暴露 reusable design gap，应先记录证据，再回到独立 `agentic-dev` 上下文处理。

## 4. 验证采用范围

Phase F 不要求 Consumer 一次采用整个 `agentic-dev` v2。

应只采用足以覆盖真实场景的最小集合：

1. Consumer-local rule activation reusable Guide semantics；
2. 一个当前 Consumer 真正需要、可本地解析的核心 Skill；
3. 至少一个 Consumer-native Authority locator；
4. 至少一个 Consumer-specific override / project-specific constraint；
5. 最小 Activation Manifest / Catalog 或等价 local discovery entry；
6. upgrade-only baseline / adoption state，且与 ordinary runtime active state 分离。

不得为了完成实验把全部 upstream Guide、Skill、Research、Project Roadmap 或 `docs/project/*` vendor 到 Consumer。

## 5. Consumer Bootstrap / AGENTS 瘦身检查

Phase F 必须把根入口职责作为真实验证项，而不是附带清理。

开始后检查 Consumer 当前 `AGENTS.md` / local Method 是否存在以下反模式：

- 当前阶段 / EU / PR / Issue / Run 等易变化状态堆入最高优先级 Bootstrap；
- 多轮 upstream baseline 升级历史持续累加到 ordinary Fresh Context 默认输入；
- Method / Guide / Skill 规则正文被 Bootstrap 重复维护；
- README / Roadmap / Documentation Authority Map 与 AGENTS 并行维护同一 Current State；
- 已关闭 Execution Unit / 历史证据默认进入 Fresh Context。

如果当前 Consumer Authority 允许调整，并且这些问题真实存在，应按 Consumer 自己的权威进行最小职责归位：

```text
AGENTS / Bootstrap
→ 稳定 Repository Governance / Authority Boundary / local discovery entry

README
→ 简短当前状态 / 稳定导航

Roadmap / Documentation Authority Map / current project docs
→ 详细 Current State / Gate / Authority locator

baseline adoption history
→ upgrade-only local history，ordinary runtime 默认不加载
```

不得为了匹配 `agentic-dev` 形式机械改目录或删除仍属于 Consumer Authority 的有效规则。

## 6. R1 — Ordinary Fresh Context

覆盖 CL-01 + CL-04 + CL-06。

选择一个真实、当前可执行或可安全分析的 Consumer responsibility。

必须证明：

- Fresh Context 从 Consumer-local Bootstrap / discovery 开始；
- 不允许 ordinary runtime 读取 upstream；
- local discovery 至少定位一个 Consumer-native Authority；
- 同时定位一个 adopted reusable responsibility / capability；
- primary responsibility 正确；
- 真正执行职责时只加载对应 local Skill；
- supporting constraints 不造成批量 Skill / Guide 加载；
- Consumer project facts 不由 Skill 推断。

如果当前 Consumer 没有适合安全执行的业务单元，可以使用对当前 Authority 的只读职责执行，但不得伪造一个不存在的 Execute Authority。

## 7. R2 — Stage Return / Ambiguity / Routing-only

覆盖 CL-02 + CL-05 + CL-08。

必须构造或选择一个受控场景，同时包含：

- 当前执行 / readiness 信号；
- 新证据导致 Product / Specification / Durable HOW / Architecture basis 中至少一项需要返回上游职责；
- 不属于 expected-behavior 明确下的普通 runtime defect。

必须：

- 解析正确 primary responsibility；
- execution / readiness 等只作为 supporting context；
- routing-only 时不加载完整目标 Skill；
- 不误进 `systematic-debug`；
- 基础语义变化时旧 Readiness 不继续授予 Execute；
- ambiguity / no-match 时 fail-closed 到 Consumer-local Authority，而非访问 upstream。

受控场景不得改变真实产品 Authority，只用于隔离行为验证。

## 8. R3 — Consumer Override

覆盖 CL-03。

必须从 Consumer 当前 Repository Authority 中找到一个**真实存在**的 project-specific rule / Architecture / Verification / Technology override，与一个 reusable default 形成竞争。

不得为了实验新造一个无真实项目意义的 override。

必须证明：

- local discovery 能同时找到两者；
- Consumer-specific current Authority 胜出；
- reusable default 不覆盖项目事实；
- 差异不会被自动判定为 Consumer 错误；
- ordinary runtime 不访问 upstream 寻找“更新答案”。

## 9. R4 — Baseline Upgrade Lifecycle

覆盖 CL-09 + CL-10 + CL-11。

执行一次真实或受控的显式 baseline adoption：

```text
previous evaluated baseline
→ candidate exact baseline
→ reusable delta classification
→ adopt / retain-or-override / reject-not-applicable
→ local projection
→ validation
```

至少包含：

- 1 项 `adopt`；
- 1 项 `retain / override`；
- 1 项 `reject / not applicable`；

如果当前 exact delta 无法自然提供三类，可以使用受控 adoption fixture，但不能把 fixture 写成 Consumer 产品 Authority。

必须证明：

- last evaluated upstream baseline 与每项 active asset 的 `adopted_from` 分离；
- rejected candidate 不进入 ordinary runtime；
- retained override 不被 candidate baseline 覆盖；
- upstream 后续变化在未进行下一次 upgrade 前不改变 Consumer runtime；
- superseded old asset 不残留双重激活；
- upgrade history 不成为普通 Fresh Context 默认输入。

## 10. R5 — Stale / Rebuild

覆盖 CL-07 + CL-12。

使用受控、无语义破坏的方式验证：

### stale

- 修改 / 复制一个测试用 semantic-reviewed source identity，或制造等价无语义 drift；
- 保留旧 discovery identity；
- 验证 old metadata 被判 stale；
- 不能继续用旧 derived discovery 授权当前任务。

### rebuild

- 删除纯派生 Runtime Catalog；
- 保留 Consumer semantic owners 与 Manifest；
- 重新生成 / 重建 Catalog；
- 验证 Current behavior 不变。

不得为了测试破坏真实 Consumer Requirement / Architecture / Work Authority。

## 11. 证据要求

每个 R1～R5 至少保存：

- Consumer exact Head / Branch；
- candidate `agentic-dev` exact Head；
- runtime / model / reasoning 能观测到什么就记录什么，不能观测的不虚构；
- Agent-visible input boundaries；
- actual local files / sources read；
- whether upstream access was available / prohibited / observed；
- primary responsibility；
- supporting sources；
- Skill activation；
- Stage Action；
- stale / fail-closed result；
- human semantic grading；
- blocking / medium findings；
- context / file-read / token / wall-clock 等可取得效率指标。

进程退出码、Catalog 命中或 Skill 被读取都不能单独作为 PASS。

## 12. 评分

统一按照：

`docs/project/consumer-local-rule-runtime-acceptance-v2.md`

评分。

最终状态只能是：

- `PASS`
- `INCONCLUSIVE`
- `REJECT`

只有以下条件同时满足才进入 Phase G：

- R1～R5 覆盖完整；
- 无未解决 Blocking / Medium reusable finding；
- Consumer Authority precedence 正确；
- ordinary runtime 无 upstream dependency；
- local discovery / Skill / override / stale / adoption lifecycle 均可持续；
- root Bootstrap 没有因为 adoption 再次膨胀；
- 没有第二套规范性 Authority。

## 13. 回传边界

Consumer 验证完成后，向 `agentic-dev` 至少回传：

- exact Consumer branch / Head / PR / evidence references；
- exact candidate `agentic-dev` Head；
- R1～R5 verdict；
- Blocking / Medium reusable findings；
- Consumer-only findings，明确不提升为通用规则；
- AGENTS / Bootstrap 瘦身前后对 ordinary Fresh Context 的影响；
- 是否建议 `PASS / INCONCLUSIVE / REJECT` v2 Consumer-local model。

Issue #92 承担本有限里程碑 Phase F 证据入口；Issue #58 只有在出现具有长期跨项目复用价值的 Consumer experience finding 时才追加，不为每个实验步骤制造评论。

## 14. Consumer Fresh Context 交接模板

下面的模板只承担定位和验证目标，不复制 Consumer 当前项目状态：

```text
这是一个 Fresh Context。不要依赖其他聊天、历史会话或个人记忆；GitHub Repository 是唯一项目事实来源。

继续维护：dygapp/jilinjobs-cms

本轮执行 agentic-dev Issue #92 / 规则治理与知识激活 v2 的 Phase F — Consumer-local Runtime Validation。

先从 GitHub 重新恢复 Consumer 当前 main、Open PR / Issue、相关 Actions、AGENTS.md、README.md、docs/README.md、Project Roadmap、Consumer-local Development Method 与当前直接 Authority；不得把本提示词中的状态描述当作当前项目事实。

随后读取 dygapp/agentic-dev 当前候选 ref：docs/rule-governance-knowledge-activation-v2，解析其 exact Head，并只读取本次 adoption / validation 真正需要的 reusable Guide、Skill 与 Phase F validation requirements。agentic-dev 在本会话中只读；不得修改其仓库文件。

按 Consumer 当前 Repository Authority 建立独立实验分支，执行 R1～R5。任何 Consumer 修改必须保持产品路线与现有 Authority，不得为了实验发明产品规则。重点同时审计并收敛 Consumer AGENTS / Bootstrap 中不属于稳定治理入口的项目状态、baseline history 和重复方法正文；应归位到 README、Roadmap、Documentation Authority Map、upgrade-only history 或其他 Consumer 合适 owner，而不是机械删除。

完成 adoption 后，ordinary Fresh Context 验证必须禁止依赖 upstream；只允许 Consumer-local Authority / Manifest / Catalog / local Skill / Current Evidence。按隐藏验收语义人工评分并保存可审计证据。

连续执行到 Phase F 当前自然 Gate；只有遇到 Consumer Repository Authority 规定的真正人工决策、权限或重大不可逆架构问题才停止。
```

该模板中的 Consumer 状态必须在执行时重新恢复，不能随着时间把本文变成 Consumer Current State 的替代来源。