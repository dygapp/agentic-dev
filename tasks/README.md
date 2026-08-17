# Tasks

Tasks 只承担工作协调职责，不构成方法权威。

## 当前下一阶段

下一里程碑：

> **First Skill Implementation**

第一批 8 个核心 Skill Contract 已完成复核，并形成 `docs/architecture/first-batch-skill-design.md` 设计基线。

推荐顺序：

1. 实现并验证 `readiness-check`。
2. 实现并验证 `slice-work`。
3. 按第一批 Skill 设计基线逐个推进其余 Skill。
4. 每次只实现一个 Skill。
5. 每个 Skill 都先根据 Method / Architecture / Contract 验证，再继续下一个。

方法结论不能只存在于 Task 中。

如果 Task 产生新的 Method Decision，应先更新对应权威文档；如果实现暴露 Skill Contract 问题，应先修改并提交 Contract，再继续实现。
