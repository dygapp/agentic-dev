# 共享外部资源并发边界处理计划

**状态：** Completed

## 目标

处理 Issue #33 中 Consumer PR #19 暴露的共享外部资源并发证据，使现有外部操作治理与 `github-actions-verification` 能够按真实资源冲突域设计并发、释放、重试和验证闭环。

## 权威输入

- `agentic-dev` 基线：`master@bf21c7bcd711fd667c43007a72fae65750d1af09`；
- 实验跟踪：Issue #33；
- Consumer：`dygapp/jilinjobs-cms` PR #19；
- 实际修复证据：Consumer commit `f350ff24ed2169e41dd838c973a1e2ceebe2c761`。

## 工作项

1. 强化 External Operation Guide 的共享资源冲突域与安全释放边界；
2. 对齐现有 `github-actions-verification` Skill 及 Runtime 成本参考；
3. 增加一个针对不同 ref 争用固定外部资源的 Behavior 场景；
4. 完成静态验证、Fresh Runtime 语义评分、Issue 回写和最终 AI Review；
5. 在同一 PR 合并前收敛 Project Roadmap 与本计划状态。

## 非目标

- 不修改 Method 或 Skill Contract；
- 不新增 Skill 或 Method 阶段；
- 不把 Repository 级单例并发设为所有 Workflow 的固定政策；
- 不修改 Consumer Repository；
- 不执行 Merge、Release 或 Deploy。

## 完成条件

- Guide、Skill 与 Reference 对真实共享资源冲突域的表达一致；
- 新场景和必要回归完成有效 Fresh Runtime 运行与人工逐断言语义评分；
- 静态检查与最终 AI Review 通过；
- Issue #33、Project Roadmap 与本计划在合并前记录稳定结论，不再依赖合并后的机械状态 PR。

## 结果

- PR：#40；
- Fresh Runtime Eval：`4 / 4 PASS`；
- 人工语义评分：`25 / 25 PASS`；
- 隔离与污染检查：`PASS`；
- 最终 AI Review：`PASS`，Blocking / Medium Finding 为 `0 / 0`；
- 集成边界：Ready to Integrate，等待 Human / Repository Policy 决定是否合并。
