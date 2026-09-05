# Issue #58 Planning Candidate 与 Execution Unit 身份边界计划

**状态：** In Progress

## Goal

基于 Issue #58 的 Consumer Evidence，明确 Planning / Requirement Candidate、Candidate Execution Unit 与 Ready Execution Unit 的身份和状态边界，避免 Roadmap 顺序或预编号被误读为已经完成 Slice / Readiness。

## Authority / Inputs

- `AGENTS.md`
- `docs/method/ai-development-method.md`
- `docs/guides/using-agentic-dev.md`
- `skills/slice-work/SKILL.md`
- `skills/readiness-check/SKILL.md`
- Issue #58 Finding 3 与 Consumer PR #58 / Issues #59、#60
- 基线：`master@394d1c3cde04b35940d5e33b7cbcaaf6557678ce`

## Scope

1. 明确 Roadmap / Backlog / Issue 中的 Future Work 可以保持 Planning / Requirement Candidate，不因排序或名称获得 Execution Unit 身份；
2. 明确 `slice-work` 可以为已形成的 Candidate Execution Unit 分配稳定标识，但该标识不是 Readiness PASS；
3. 明确只有 Readiness Gate PASS 后，Execution Unit 才能作为 Ready Unit 进入 Execute；
4. 对齐 Usage Guide、`slice-work` 与 `readiness-check`；
5. 新增定向 Behavior Eval 并执行必要回归；
6. 回写 Issue #58，Issue 继续作为长期 Consumer Feedback 渠道保持开放。

## Non-goals

- 不修改 Core Method、Principles 或 Skill Contract；
- 不改变 Stage 4 `Slice & Ready` 的顺序；
- 不要求所有项目使用 `EU-xx`、GitHub Issue 或固定 Backlog ID；
- 不禁止 `slice-work` 为候选 Execution Unit 分配 identifier；
- 不修改 Consumer Repository；
- 不把 Consumer 的具体 Roadmap、Issue 编号或产品候选提升为通用事实。

## Work Items

1. 修订 Usage Guide 的 Project Roadmap 与 Execution Unit 使用边界；
2. 对齐 `slice-work` 与 `readiness-check` 的身份 / 状态语义；
3. 新增：
   - `B-SW-02`：Planning Candidate 不能因预编号直接成为 Execution Unit；
   - `B-RC-06`：identifier / Roadmap 顺序不能替代可检查输入和 Readiness；
4. 回归：
   - `B-SW-01`
   - `B-RC-01`
   - `B-RC-05`
5. 静态验证、Fresh Runtime、人工语义评分和最终 AI Review；
6. 回写 Eval、Project Roadmap、Plan 与 Issue #58。

## Completion Criteria

- Guide 与两个 Skills 语义一致且不改变 Method；
- Planning Candidate、Candidate Execution Unit、Ready Execution Unit 三种状态可明确区分；
- 新场景与回归场景全部通过 Fresh Runtime 和人工语义评分；
- 最终 PR 无 Blocking / Medium Finding；
- 合并仍由 Human Authority 决定。
