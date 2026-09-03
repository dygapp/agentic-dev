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

状态：**Completed**。

Research：`docs/research/data-access-scope-boundedness-analysis.md`。

### Step 2 — Candidate / Architecture Fit

回答：

1. 该规则是否跨技术栈成立？
2. 它是否只是 Performance / Database 技巧，还是会影响正确性与验证？
3. 是否需要独立任务入口、输出或 Stage Return？
4. 是否应成为 Engineering Discipline、Technology Profile、Verification Profile 或仅 Implementation Guidance？
5. 与 Implementation Minimality、Surgical Change 是否职责重叠？

结论：**PASS — Independent Engineering Discipline + thin `execute-unit` consumption**。

不修改 Core Method / Engineering Capability Architecture，不创建 Technology Profile、Verification Profile 或新 Skill。

### Step 3 — Draft

已完成：

- `docs/architecture/engineering-disciplines.md` 增加第三项 Draft；
- `docs/architecture/skill-contracts.md` 增加 `execute-unit` 薄契约引用；
- `skills/execute-unit/SKILL.md` 增加实施 / 验证 / Engineering Quality 薄判断；
- 不新增 Skill；
- 不修改 Core Method。

状态：**Completed**。

### Step 4 — Targeted Eval

已新增并完成 Fresh Runtime：

- `B-EU-18`：global Top-N 后 client filtering 的正确性截断；
- `B-EU-19`：bounded stable snapshot 不应机械分页，且没有 freshness Authority 时不发明实时刷新；
- `B-EU-20`：unbounded operational collection 的 server filtering / pagination / summary；
- `B-EU-21`：presentation N 与 retrieval scope 分离；
- `B-EU-22`：明确全局 ranking contract 时允许 window-first 业务语义；
- `B-EU-23`：超过 page / window 与 competing scope 边界的数据验证；
- `B-EU-24`：pagination ordering / continuation stability；
- `B-EU-25`：bounded snapshot 仍受明确 freshness / lifecycle invalidation 责任约束。

必要回归：

- `B-EU-01`
- `B-EU-06`
- `B-EU-09`
- `B-EU-13`

Fresh Runtime 结果：

```text
新场景： 8 / 8 PASS，41 / 41 assertions PASS
历史回归：4 / 4 PASS，19 / 19 assertions PASS
合计：   12 / 12 PASS，60 / 60 assertions PASS
```

冻结待测 Head：

`31e8d7597cbe9ea37746b34a6c50907e6dea37b0`

结果 ZIP SHA-256：

`d32233916e2ce923f2f052fe6750eda4bf0674992906bd18223b43f83f21a855`

隔离检查：**PASS**。12 个 stderr 全空；未发现读取 Eval 定义、历史结果、grading assertions 或隔离 workspace 外上下文。

状态：**Completed / PASS**。

### Step 5 — AI Review / Integration

检查：

- Authority Alignment；
- 与既有两个 Discipline 的职责分离；
- 是否误变成 Pagination Rule / Database Method；
- 是否允许 bounded snapshot 与明确 global ranking 的反例；
- 是否没有创建新 Skill / Profile；
- Targeted Eval Evidence freshness；
- Human / Integration Boundary。

当前状态：**Final AI Review / Integration Decision**。

只有最终 AI Review 的 Blocking / Medium = 0 后达到 Ready to Integrate；实际 Merge 继续由 Human Authority / Repository Policy 决定。

## 4. 当前状态

`ED1 Completed → ED2 Completed → ED3 Completed / Runtime PASS → ED4 Final AI Review / Integration Decision`

当前不得启动 WI-06、WI-07、WI-09 或 stacked-PR topology 工作。

## 5. 完成后

只有实际 Integration 后才关闭本里程碑。Closure 后重新进行 Milestone Decision，不自动选择下一 Post-v1 候选。
