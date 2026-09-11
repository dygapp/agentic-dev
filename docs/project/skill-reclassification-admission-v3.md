# V3-04 技能重分类与准入审计

**状态：** v0.1（V3-04）  
**性质：** 项目级技能重分类与准入结果  
**跟踪：** Issue #107  
**审计基线：** `master@3043e95193f462348dd9fcb99f8a1871145d503d`

## 1. 目的

本文在 V3-02 已完成所有权盘点的基础上，只处理 Skill 身份、Skill 与其他工程能力 / Guide / 仓库本地规则之间的正文边界，以及未来新增 Skill 的准入判断。

本阶段不重新打开第一批核心 Skill 工程，不因为某段内容“可复用”“重要”“会被 Agent 读取”或“存在步骤”就自动 Skill 化。

## 2. Skill 身份判定

一个当前能力只有在同时具有以下稳定属性时才适合作为 Skill：

- 明确触发条件与不适用条件；
- 稳定输入；
- 可重复过程；
- 明确输出；
- 明确退出、阶段返回或升级条件；
- 可以独立组合或调用；
- 过程复杂度足以值得按需加载和独立维护。

以下信号单独存在时都不足以形成新 Skill：

- 跨仓库可复用；
- Agent 在普通运行中会读取；
- 内容很重要；
- 有若干按顺序执行的步骤；
- 会被多个现有 Skill 消费；
- 当前文件位于 `skills/` 或 Guide 中。

如果一个能力主要表达横切约束、默认知识、仓库本地值、使用方生命周期或人类说明，应由对应工程能力、仓库本地规则、生命周期权威或 Guide 持有，而不是为了激活方便升级为 Skill。

稳定的新增 Skill 准入门禁已经提升到 `docs/architecture/skill-architecture.md`；本文记录 V3-04 的项目级裁决与证据关系，不维护第二份长期 Skill Architecture。

## 3. 当前 9 个 Skill 身份结论

| Skill | 当前身份 | 结论 | overlap / 边界 | V3-04 结果 |
|---|---|---|---|---|
| `clarify-intent` | 核心工作流 Skill | keep | 只处理高影响 Product Intent 歧义；长期领域事实只识别候选并返回 `specify` | 保持 current Skill |
| `specify` | 核心工作流 Skill | keep | 拥有 WHAT / WHY 形成过程；长期领域事实写入仍服从使用方仓库权威 | 保持 current Skill |
| `technical-plan` | 核心工作流 Skill | keep | 拥有跨执行单元长期 HOW 与 Architecture / ADR 评估过程，不拥有产品意图 | 保持 current Skill |
| `slice-work` | 核心工作流 Skill | keep | 拥有执行单元塑形与验收 / 验证责任映射，不拥有最终 Readiness | 保持 current Skill |
| `readiness-check` | 核心工作流 Skill | keep | 只读门禁；消费验证 / 治理规则但不取得它们的规范正文所有权 | 保持 current Skill |
| `execute-unit` | 核心工作流 Skill | keep；overlap 已修正 | 单执行单元实施 / 验证职责成立；原正文对三个 Engineering Discipline 复制过厚 | 已缩回薄消费；纪律正文由 `engineering-disciplines.md` 单点拥有 |
| `systematic-debug` | 核心调查 Skill | keep | Expected Behavior 未定义时返回上游，不接管 Requirement / Specification | 保持 current Skill |
| `converge` | 核心工作流 Skill | keep | Feature-wide 收敛、Evidence coverage 与 Gap routing 属其过程；跨职责证据类型 / currentness 规则仍由 verification capability 持有 | 复核后无需修改 Skill 正文 |
| `github-actions-verification` | 平台专项非核心 Skill | keep | GitHub Actions trigger / observability / runtime / artifact / diagnostics 是稳定平台过程；通用外部操作与跨职责证据规则由各自 owner 持有 | 复核后无需修改 Skill 正文 |

当前没有证据支持删除、合并或批量重写上述 9 个 Skill，也没有证据支持新增第 10 个 Skill。

## 4. 关键 overlap 裁决

### 4.1 `execute-unit` 与工程纪律

`execute-unit` 的稳定任务入口、输入、输出、退出和阶段返回均成立，因此 Skill 身份不受影响。

`docs/architecture/engineering-disciplines.md` 已明确：三个工程纪律没有独立任务入口，应由多个职责消费，`execute-unit` **只需要保留薄执行规则，不复制完整纪律正文**。

V3-04 已将 `execute-unit/SKILL.md` 中原先展开的：

- 实现最小化与推测性复杂度控制；
- 精准修改与差异范围控制；
- 数据访问作用域与有界性控制；
- 相关配置责任与既有能力复用细则；

缩回为当前 Unit 中的条件识别、规范 owner 指针和薄执行判断。具体纪律规则只在 `engineering-disciplines.md` 单点维护。

本次去重没有改变 `execute-unit` 的职责、触发、输入、输出、一次一 Unit、调试返回、阶段返回或退出条件。

### 4.2 `converge` 与跨职责验证规则

`converge` 必须拥有 Feature-wide 收敛过程，包括：

- 规格到系统覆盖视图；
- Missing / Partial / Contradiction / Unrequested Behavior；
- Feature-wide Current Evidence coverage；
- Cross-unit Integration Gap；
- Domain / Architecture / ADR / Artifact Lifecycle / Roadmap Gap routing；
- `READY / GAPS` 结论。

这些是 `converge` procedure 的组成部分，不应抽走。

但下列横切规则不是 `converge` 独有：

- Verification Contract Currentness；
- Evidence Type Must Match Claim；
- Evidence Claim Reuse Across Commits；
- Visual Evidence；
- Human Review Baseline Isolation；
- Database Migration Completion Evidence。

它们应由跨职责验证工程能力持有。对当前 `converge/SKILL.md` 复核后，没有发现需要在 V3-04 立即删除的第二份完整规范正文，因此不为了阶段形式机械修改该 Skill。

当前证据不足以创建 `verify-evidence` Skill：这些规则没有统一独立任务入口、独立输出或稳定单独调度价值。

### 4.3 `github-actions-verification` 与通用外部操作 / 验证能力

该 Skill 具有独立且稳定的平台过程：

- 识别 GitHub Actions 验证范围；
- 检查 workflow / runtime capability；
- 选择可观察 trigger path；
- 对齐 claim / verification layer / actual trigger；
- 分层反馈与 completion verification；
- runtime / artifact / diagnostics / shared-resource 处理。

因此平台专项 Skill 身份成立。

但其语义层级必须保持：

```text
通用外部操作 / 验证工程能力
→ GitHub Actions 平台 procedure
→ 使用方仓库具体 workflow / policy / runtime state
```

`github-actions-verification` 不拥有：

- 通用“工具能力 ≠ 授权”原则；
- 所有平台的外部写后重读闭环；
- 通用 Evidence-before-claims；
- 使用方的 Merge / Release / Deploy 权限；
- 所有 Consumer 的统一 CI 拓扑。

当前 `github-actions-verification/SKILL.md` 已明确自身实现既有方法 / 外部操作 / 验证语义并服从使用方策略；复核后没有证据要求在 V3-04 机械重写。

### 4.4 使用方生命周期不是 adoption / upgrade Skill

V3-03 已明确“使用方生命周期（`Consumer Lifecycle`）”属于可复用工程能力，而不是产品开发方法阶段，也不因为具有状态转换和过程顺序就自动成为 Skill。

原因：生命周期主要拥有**何时允许进入上游、何时完成采用 / 升级、普通运行如何回到本地、何时允许重新进入**等跨过程规范语义；具体动作由 Guide、仓库权威、验证能力和未来资源 / 发现架构共同实现。

因此 V3-04 不创建 `adopt-agentic-dev`、`upgrade-baseline` 或类似 Skill。

## 5. Guide / 派生路由与 Skill 边界

### 5.1 `using-agentic-dev.md`

Skill inventory / responsibility routing 表属于 Guide / 派生导航，不拥有 Skill procedure。长期方向仍是减少手工维护第二职责表，由 V3-06 决定未来发现机制；V3-04 不提前实现发现架构。

### 5.2 `consumer-local-rule-activation.md`

- 主职责路由：属于资源发现 / 路由能力，等待 V3-06；
- routing-only 与 Skill execution：属于 discovery / Skill interface，等待 V3-06；
- Stage Return 的方法 / Skill Contract 语义由现行 owner 持有；Guide 只能保留 Stage Return 后重新做本地 discovery / routing 的后果；
- 不创建 Stage Router Skill。

### 5.3 `rule-activation-guide.md`

它是当前薄派生导航入口，不拥有 Skill procedure。当前继续保持兼容；V3-06 决定如何取代或重建。V3-04 只保证其指针不把 Guide 误写成 Skill owner。

## 6. Verification 与 external-operation rule families

### 6.1 Verification rule families

结论：**可复用验证工程能力，不形成独立 Skill。**

理由：

- 规则按条件横切 `execute-unit`、`converge`、平台专项 Skill 与调试场景；
- 没有统一稳定的独立任务入口；
- 没有单一独立输出；
- 多数规则是条件性约束和证据契约，而不是一个可独立调度 procedure。

物理载体 / metadata / profile 形式留给 V3-05，不在 V3-04 冻结。

### 6.2 External-operation rule families

结论：**当前仍不形成新的通用 external-operation Skill。**

现有规则族混合了：

- 跨平台外部写前读取 / 写后重读验证；
- 授权与多仓库边界；
- 异步观察；
- 共享资源 owner / lease / cleanup；
- 临时 evidence → 持久输入晋升；
- dependent / stacked PR integration discipline；
- 二进制 / 媒体输入真实性验证。

它们没有一个统一稳定输出，也不是每次外部操作都需要全部执行。当前更适合作为若干可复用工程能力 / repository-policy hook，被具体平台 Skill 按条件消费。

如果未来证据证明其中某个子过程具备稳定独立触发、输入、输出、退出和单独调度价值，再重新按 Skill admission 判断；V3-04 不提前升级。

## 7. 历史 Skill design 与当前 Authority

`docs/architecture/first-batch-skill-design.md` 记录第一批 8 个核心 Skill 从已复核 Contract 转换为 `SKILL.md` 的**历史实现设计基线**。

当前长期规范关系是：

```text
Engineering Capability Architecture
→ Skill Architecture
→ Skill Contracts
→ 当前 `SKILL.md`
```

V3-04 已完成：

- `first-batch-skill-design.md` 显式降为历史设计 / Evidence；
- `skills/README.md` 不再把它列为“权威设计参考”；
- `skills/README.md` 明确当前权威为 Engineering Capability Architecture、Skill Architecture、Skill Contracts 和当前 `SKILL.md`；
- 历史设计物理上仍位于 `docs/architecture/`，但其状态已明确，不再因目录位置自动 current；是否物理迁移留给 V3-07 自采用 / repository migration。

## 8. Supporting resource 边界

稳定规则已经提升到 `docs/architecture/skill-architecture.md`：某个 Skill 下的 `references/*`、fixture、template 或脚本只有在以下条件下才保持 supporting body：

- 直接服务该 Skill procedure；
- 不独立定义跨 Skill / 跨仓库长期规范语义；
- 生命周期随该 Skill 的当前身份管理；
- 被删除后不会丢失其 Skill 之外的规范事实。

如果 supporting resource 开始被多个 Skill / Guide 独立消费，或出现独立触发 / 更新 / 适用范围，就必须重新判断真实语义所有者，不能因为物理位置在某 Skill 目录就继续把它当内部附件。

当前 `skills/github-actions-verification/references/*` 继续属于该平台 Skill supporting body，没有证据要求提升为平级 owner。

## 9. 新 Skill 准入门禁

稳定准入规则已经提升到 `docs/architecture/skill-architecture.md`。未来新增 Skill 至少必须同时回答：

1. **Trigger**：什么时候应进入该职责？什么时候明确不进入？
2. **Inputs**：是否存在稳定、可描述的最小输入？
3. **Procedure**：是否存在可重复、足够复杂、值得按需加载的过程？
4. **Outputs**：是否存在稳定独立输出，而不只是“遵守若干规则”？
5. **Exit / Return / Escalation**：如何停止、返回上游或升级？
6. **Composability**：能否作为独立职责被其他流程调用，而不是接管完整生命周期？
7. **Ownership**：是否会复制 Method、Architecture、Engineering Discipline、Consumer Lifecycle、Repository Policy 或 Guide 已拥有的正文？
8. **Evidence**：是否有官方 / 成熟工程实践、专项评估或使用方证据支持该独立职责，而不只是命名偏好？
9. **Evaluation**：是否能设计有辨识力的行为评估证明它比现有 owner / supporting capability 更合适？

任一高影响边界无法回答时，保持工程能力 / Guide / Research 候选，不为了目录完整或运行时激活便利提前 Skill 化。

## 10. V3-04 已执行的 current-authority 修正

V3-04 当前已完成以下最小修正：

1. `skills/README.md`：将 `first-batch-skill-design.md` 从 current authority 列表中移出并明确为历史设计参考；
2. `docs/architecture/first-batch-skill-design.md`：显式标记为历史设计 / Evidence，保留其历史正文；
3. `docs/architecture/skill-architecture.md`：加入 V3-04 已确认的新增 Skill admission、supporting-resource 与 no-super-skill 边界；
4. `skills/execute-unit/SKILL.md`：缩回对三个 Engineering Discipline 的详细复制，只保留当前 Unit 内的薄消费与 owner 指针；
5. `converge/SKILL.md` / `github-actions-verification/SKILL.md`：针对性复核后未发现需要立即修改的第二份完整规范正文，因此保持不变。

Guide 物理拆分、verification capability 最终载体、external-operation capability 最终载体、metadata 表示和 discovery implementation 均留给后序阶段。

## 11. V3-04 门禁

进入集成决策前必须确认：

- 9 个当前 Skill 的身份和 overlap 均有明确结论；
- `execute-unit` 的工程纪律消费不再形成第二规范 owner；
- `converge` 与跨职责验证规则边界明确；
- `github-actions-verification` 与通用验证 / 外部操作能力边界明确；
- verification / external-operation rule families 没有被错误 Skill 化；
- Consumer Lifecycle 没有被错误 Skill 化；
- Guide / 派生路由不再被误认为 Skill procedure owner；
- `first-batch-skill-design.md` 不再与 current Skill Authority 平行；
- supporting resource 与平级 owner 的判断规则明确；
- V3-05 / V3-06 可以直接消费 Skill 身份和准入结论；
- AI 复核对高影响 Skill ownership / admission ambiguity 的 Blocking / Medium 为 0。

达到门禁后，只进入“是否启动 V3-05”的规划判断，不自动执行后序迁移、资源模型或发现架构。