# Data Access Scope & Boundedness Discipline Plan

## 1. 目标

执行 `Engineering Discipline Expansion v1`，围绕唯一候选 **Data Access Scope & Boundedness Control（数据访问作用域与有界性控制）** 完成 Research、Architecture Fit、Draft、Targeted Eval、AI Review 与 Integration。

当前基线：

`master@a0aece02414aa36ca7421db391cb3124ad0780f2`

## 2. 输入

- `AGENTS.md`
- `docs/project/project-roadmap.md`
- `docs/project/engineering-discipline-expansion-v1.md`
- `docs/architecture/engineering-capability-architecture.md`
- `docs/architecture/engineering-disciplines.md`
- `docs/architecture/skill-contracts.md`
- `skills/execute-unit/SKILL.md`
- Issue #33 Final Summary 与其中 Data Access Consumer Evidence
- 当前外部官方 / 成熟工程 Research Evidence

## 3. 执行顺序

### Step 1 — Research

- 提取 Issue #33 已核验实例；
- 研究 collection scope、filtering、pagination/windowing、ordering、partial representation、large collection consistency；
- 记录来源、当前日期、适用范围、冲突与反例；
- 不把“分页是好实践”直接提升成规则。

### Step 2 — Candidate / Architecture Fit

回答：

1. 该规则是否跨技术栈成立？
2. 它是否只是 Performance / Database 技巧，还是会影响正确性与验证？
3. 是否需要独立任务入口、输出或 Stage Return？
4. 是否应成为 Engineering Discipline、Technology Profile、Verification Profile 或仅 Implementation Guidance？
5. 与 Implementation Minimality、Surgical Change 是否职责重叠？

预期但未预设的候选方向：**独立 Engineering Discipline + `execute-unit` 薄消费**。

### Step 3 — Draft

如果 Architecture Fit 通过：

- 更新 `docs/architecture/engineering-disciplines.md`；
- 更新 `docs/architecture/skill-contracts.md` 的薄契约引用；
- 更新 `skills/execute-unit/SKILL.md` 的实施 / 验证摘要；
- 不新增 Skill；
- 不修改 Core Method。

### Step 4 — Targeted Eval

新增数据访问专项场景，并保留必要历史回归。

候选场景至少覆盖：

- global Top-N 后 client filtering 的正确性截断；
- bounded stable snapshot 不应机械分页；
- unbounded operational collection 的 server filtering / pagination；
- presentation N 与 retrieval scope 分离；
- 明确全局 ranking contract 时不机械执行 filter-before-limit；
- 超过 page/window 边界的数据规模验证；
- pagination / window 稳定 ordering；
- bounded snapshot 的 freshness / lifecycle invalidation。

必要回归至少包括：

- `B-EU-01`
- `B-EU-06`
- `B-EU-09`
- `B-EU-13`

Fresh Runtime 必须逐 assertion 语义评分；进程退出 0 不等于 PASS。

### Step 5 — AI Review / Integration

检查：

- Authority Alignment；
- 与既有两个 Discipline 的职责分离；
- 是否误变成 Pagination Rule / Database Method；
- 是否允许 bounded snapshot 与明确 global ranking 的反例；
- 是否没有创建新 Skill / Profile；
- Targeted Eval Evidence freshness；
- Human / Integration Boundary。

Blocking / Medium = 0 后达到 Ready to Integrate。

## 4. 当前状态

`ED1 Completed → ED2 Research / Candidate in progress`

当前不得启动 WI-06、WI-07、WI-09 或 stacked-PR topology 工作。

## 5. 完成后

只有实际 Integration 后才关闭本里程碑。Closure 后重新进行 Milestone Decision，不自动选择下一 Post-v1 候选。