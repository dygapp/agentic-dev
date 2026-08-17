# 研究总结 — mattpocock/skills

**研究日期：** 2026-08-17  
**性质：** 非规范性研究输入

## 1. 项目定位

上游仓库：

https://github.com/mattpocock/skills

该项目更接近一组小型、可适配、可组合的 Agent Skills，而不是接管完整软件生命周期的框架。

## 2. 主要观察

### 2.1 生命周期采用组合方式，而不是固定状态机

可以归纳出类似：

```text
clarify / grill
→ specify
→ ticket / slice
→ implement
→ review
```

的主链，但仓库本身并不要求所有工作严格遵守一个统一 SDLC。

### 2.2 Vertical Slicing 是核心

`to-tickets` 与 TDD 相关设计强调窄而完整的端到端行为，而不是数据库、后端、前端、测试的横向阶段。

尤其重要的是：

> Work Unit 应适合一个 Fresh Agent Context。

这直接形成了本方法中的 **context-fit** 概念。

### 2.3 Durable Ticket 应保持行为导向

该体系对在 Spec/Ticket 中固化易过时的 File Path 和低层施工细节比较谨慎。

本方法因此区分：

- Durable Execution Unit；
- Transient JIT Execution Plan。

### 2.4 Fresh Context 是工作拆分的一部分

工作单元的大小本身必须考虑 Agent Context Capacity，而不是只考虑传统工时或文件数量。

### 2.5 Handoff 不应重复长期知识

Handoff 更适合传递：

- Current State
- Next Action
- Artifact References

而不是复制已经存在于 Spec、Plan、ADR、Commit 或 Diff 中的信息。

### 2.6 Domain Context 与 ADR 是长期知识载体

Glossary、Domain Facts 和重要决策应进入 Repository Artifact，而不是反复依赖聊天解释。

## 3. 本方法吸收的内容

- Small Composable Skills
- Human / Controller Controlled Workflow
- Vertical Execution Unit
- Fresh-context Sizing
- Behavior-oriented Durable Work Item
- Repository-based Durable Context
- Lightweight Handoff

## 4. 未直接照搬的内容

- 上游 Skill 名称；
- 上游具体 Specification Template；
- Issue Tracker 配置；
- 将 Technical Decision 与 Specification 混合存放的做法。

本方法最终更明确地采用：

```text
Specification = WHAT / WHY
Technical Plan = HOW
```

## 5. 参考

- https://github.com/mattpocock/skills
- https://github.com/mattpocock/skills/blob/main/README.md
