# 实施判断证据处理计划

**状态：** Completed

## 目标

处理 Issue #33 中 Consumer PR #19 新增的配置责任分类与通用 UI 能力复用证据，使现有 Operating Guide 与 `execute-unit` 能够避免机械外部化字面量或重复实现已有通用能力。

## 权威输入

- `agentic-dev` 基线：`master@c8903f2ee437ede1ebfa60bb1d34d23dbc29481c`；
- 实验跟踪：Issue #33 最新证据评论；
- Consumer：`dygapp/jilinjobs-cms` PR #19；
- Consumer 最终 Head：`fc35eae18246ceb949f17e944e844be36e27afcc`；
- Consumer 集成提交：`c9280e5b9a8ab12f6b961766753c92b442fa11f4`。

## 工作项

1. 在 Operating Guide 中明确配置责任分类与已有能力复用边界；
2. 对齐现有 `execute-unit` 的实施检查与最小修改规则；
3. 增加配置责任分类和框架能力复用两个定向 Behavior 场景；
4. 完成静态验证、Fresh Runtime 人工语义评分、Issue 回写和最终 AI Review；
5. 在同一 PR 合并前收敛 Project Roadmap 与本计划状态。

## 非目标

- 不修改 Method 或 Skill Contract；
- 不新增 Skill、配置框架或 Consumer 模板；
- 不把 Consumer 的 Spring、CMS 或 Element Plus 选择推广为固定技术政策；
- 不要求所有字面量外部化，也不建立无条件的“框架优先”规则；
- 不修改 Consumer Repository；
- 不执行 Merge、Release 或 Deploy。

## 完成条件

- Guide 与 `execute-unit` 对配置责任和复用判断的表达一致；
- 两个新场景及必要回归完成有效 Fresh Runtime 运行与人工逐断言语义评分；
- 静态检查与最终 AI Review 通过；
- Issue #33、Project Roadmap 与本计划在合并前记录稳定结论。

## 结果

- PR：#41；
- Fresh Runtime Eval：`4 / 4 PASS`；
- 人工语义评分：`25 / 25 PASS`；
- 隔离与污染检查：`PASS`；
- 评估附件 SHA-256：`04af9397a71b51828b45486605d02ddc529ef3547e0ea85a66f6b4f5744a2415`；
- 最终 AI Review：`PASS`，Blocking / Medium Finding 为 `0 / 0`；
- 集成边界：Ready to Integrate，Merge 仍由 Human / Repository Policy 决定。
