# Engineering Discipline Expansion v1

## 1. 目的

本里程碑在 Engineering Capability Foundation v1 已完成、Issue #33 Existing Consumer continuous-evolution experiment 已关闭后，选择一个证据最充分的 Post-v1 Engineering Discipline Candidate，完成有限范围的研究、设计、专项评估、AI Review 与集成闭环。

本轮唯一候选：

> **Data Access Scope & Boundedness Control（数据访问作用域与有界性控制）**

本里程碑不自动启动第二个 Technology Profile、Task-oriented Skill、Runtime Adapter / Distribution 或第二个 Engineering Discipline。

## 2. 启动依据

当前项目基线：

`master@a0aece02414aa36ca7421db391cb3124ad0780f2`

启动证据：

- Engineering Capability Foundation v1 已完成；
- Issue #33 已形成 Final Summary 并以 `PASS / Completed` 关闭；
- Issue #33 对 Data Access Scope / Boundedness / Lifecycle 的多实例 Consumer Evidence 已完成独立核验，并分类为 **Post-v1 Engineering Discipline / Implementation Guidance Research Candidate**；
- 当前没有未解决的 Blocking / Medium Method / Contract Gap；
- 当前没有 open Issue 要求优先处理其他通用缺口。

## 3. 为什么选择这一候选

本候选已经在同一真实 Consumer 的多个独立变化中重复出现：

- 全站固定 Top-N 后再客户端按业务栏目过滤会导致目标数据静默截断；
- 明确业务 scope 的列表应把 scope 进入服务端查询契约，而不是先读取全局窗口再本地筛选；
- 规模稳定、有界的站点结构数据可以保留完整快照，但需要检查应用生命周期内是否重复装配；
- 持续增长的管理端业务集合需要服务端过滤、分页和适当列表表示；
- 页面最终展示 N 条并不自动意味着数据查询只应读取全局 N 条。

这些现象跨前端、后端、数据库和 API 设计成立，当前证据更接近 Engineering Discipline，而不是某个 Technology Profile 或 Consumer-local Rule。

## 4. 固定完成边界

本里程碑固定四个阶段：

### ED1 — Milestone Definition

- 冻结唯一候选；
- 记录启动证据与非目标；
- Project Roadmap 指向本里程碑。

### ED2 — Research / Candidate / Architecture Fit

- 复核 Issue #33 Consumer Evidence；
- 主动补充官方规范、成熟开源工程实践和反例；
- 区分业务作用域、集合有界性、生命周期复用、filter/window/pagination 顺序、representation 与 verification；
- 判断候选是否属于 Engineering Discipline；
- 形成可被 Targeted Eval 区分的 Candidate。

### ED3 — Draft / Targeted Eval

- 如 Architecture Fit 通过，形成 Engineering Discipline Draft；
- `execute-unit` 只保留薄消费规则；
- 不创建 `data-access-skill` 或 Data Architecture Method；
- 建立有辨识力的 Targeted Eval 与必要历史回归；
- Fresh Runtime 逐 assertion 评分。

### ED4 — AI Review / Integration / Closure

- Blocking / Medium Finding = 0；
- Draft 实际进入当前 Repository Authority；
- 更新 Project Roadmap 为 Completed；
- 形成简短 Closure 记录；
- 再决定下一 Milestone，不在本里程碑尾部自动续接 WI-06 / WI-07 / WI-09。

## 5. Completion Conditions

本里程碑完成，当且仅当：

1. 唯一候选完成 Research 与 Architecture Fit；
2. 若候选成立，Draft Engineering Discipline 已形成；
3. Targeted Eval 与必要回归具有当前 Fresh Runtime Evidence；
4. 高影响 AI Review PASS；
5. 规范性 Engineering Discipline 与薄 `execute-unit` 消费规则实际集成；
6. 没有为了本轮能力数量创建新的 Task-oriented Skill；
7. 没有启动第二个 Discipline、第二 Technology Profile 或 Runtime / Distribution；
8. Project Roadmap 明确本里程碑已关闭且下一里程碑未自动选择。

如果 Architecture Fit 证明候选不应成为 Engineering Discipline，本里程碑可以以“Research Completed / Candidate Rejected or Reclassified”关闭，而不为了产物数量强行创建能力。

## 6. 范围冻结

以下内容明确不属于本里程碑 Completion Scope：

- WI-06 第二个及后续 Technology Profile；
- WI-07 Task-oriented Skill 提炼；
- WI-09 Runtime Adapter / Distribution；
- stacked PR + squash merge review/integration topology；
- 第二个新 Engineering Discipline；
- Data Architecture Method；
- `data-access-skill`、`pagination-skill` 或类似技术百科 / 单点规则 Skill；
- Consumer Repository 修改或新的正式 Consumer Adoption Gate。

Consumer 后续使用可以作为 Feedback，但不是本里程碑完成前置条件。

## 7. 范围变更门禁

只有以下情况允许扩大当前 Scope：

1. 当前候选无法完成 Architecture Fit 或 Targeted Eval，且原因是现有 Engineering Capability Architecture / Authority 的 Blocking 冲突；
2. Targeted Eval 证明必须修复现有 Engineering Discipline / `execute-unit` 的直接回归才能验证当前候选；
3. Human Authority 明确改变本里程碑完成定义。

“另一个方向也有价值”“顺便做第二个 Profile”“现在可以一起做 Runtime Adapter”都不足以扩大范围。

## 8. 生命周期

- **Producer：** 当前 `agentic-dev` Project Governance；
- **Trigger：** Foundation v1 Closure + Issue #33 Final Summary 完成，且 Data Access Candidate 拥有最强 Post-v1 当前证据；
- **Consumer：** Project Roadmap、当前 Research / Draft、Human Integration Decision；
- **Persistence：** 作为本次有限里程碑的项目级权威保存；
- **Update：** ED1～ED4 状态变化或 Completion Definition 被证据证明无效时更新；
- **Supersede：** 本里程碑 Closure 后由新的 Milestone Decision 接替当前工作职责；
- **Escalation：** 如果候选需要改变 Core Method 生命周期、重大能力架构或 Consumer Authority，返回更高 Authority，不在本里程碑中静默扩张。