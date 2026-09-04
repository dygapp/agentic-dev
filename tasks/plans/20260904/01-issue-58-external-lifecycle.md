# Issue #58 外部证据与评审环境生命周期强化计划

**状态：** Completed

## Goal

基于 Issue #58 的 Consumer Evidence，定向强化临时执行证据晋升为持久 Consumer Authority，以及长生命周期单实例评审环境的归属、租约与陈旧运行处理边界。

## Authority / Inputs

- `AGENTS.md`
- `docs/architecture/engineering-capability-architecture.md`
- `docs/guides/using-agentic-dev.md`
- `docs/guides/external-operation-guidelines.md`
- `skills/github-actions-verification/*`
- Issue #58 Evidence Review
- 基线：`master@5be2e6aad29b2be6b8535b3690daf3533ee22a46`

## Scope

1. 明确临时执行证据（Ephemeral Execution Evidence）与已接受持久输入（Accepted Durable Input）的职责转换；
2. 明确 promotion 的 Authority、provenance、retention / expiry 和最终 Head 复验边界；
3. 明确单实例 Review Environment 的 owner、lease、stale-run policy，以及自动验证和人工评审的不同保活生命周期；
4. 对齐 `github-actions-verification` Skill 与平台参考；
5. 新增定向 Behavior Eval，并执行必要回归；
6. 完成最终 AI Review 和 Issue #58 状态回写。

## Non-goals

- 不修改 Core Method、Principles 或 Skill Contract；
- 不修改 Data Access Engineering Discipline；
- 不新增 Skill、Technology Profile 或正式能力里程碑；
- 不规定所有 CI 使用 `latest-head-wins`；
- 不固定 Consumer 的目录、Artifact 格式、concurrency key 或解锁 Workflow；
- 不读取、修改或触发 Consumer Repository。

## Work Items

1. 修订 Usage Guide 与 External Operation Guide；
2. 对齐 `github-actions-verification` Skill 和 `diagnostics-and-runtime-cost.md`；
3. 新增 `B-GA-06`、`B-GA-07`；
4. 静态验证并创建 PR；
5. Fresh Runtime 运行：
   - `B-GA-06`
   - `B-GA-07`
   - `B-GA-01`
   - `B-GA-05`
   - `B-CG-05`
6. 人工逐断言语义评分、污染检查与最终 AI Review；
7. 回写 Eval、Roadmap、Plan 和 Issue #58。

## Completion Criteria

- Guide 与 Skill / Reference 语义一致；
- 不把单一 Consumer 实现推广为固定政策；
- 两个新场景及回归场景全部通过 Fresh Runtime 与人工语义评分；
- 最终 PR 无 Blocking / Medium Finding；
- 合并仍由 Human Authority 决定。


## Results

- Guide、Skill 与 Reference 已完成语义对齐；
- 新场景：`B-GA-06 8 / 8 PASS`、`B-GA-07 7 / 7 PASS`；
- 回归场景：`B-GA-01 6 / 6 PASS`、`B-GA-05 7 / 7 PASS`、`B-CG-05 6 / 6 PASS`；
- 合计：`5 / 5 scenarios PASS`，`34 / 34 assertions PASS`；
- 隔离、污染与运行时完整性检查：PASS；
- 附件 SHA-256：`26ddf975a181438071cfb8453cc30fa877943c9bb652f190999e761d0fca56cc`；
- Pre-Runtime AI Review：PASS，Blocking / Medium = `0 / 0`；
- 最终 AI Review 以 PR #59 最新 Head 上的正式 Review 为准；
- Integration 仍由 Human Authority 决定。
