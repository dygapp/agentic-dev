---
id: research:implementation-minimality
type: research
status: active
distribution: source-only
---

# 实现最小化与推测性复杂度控制研究

**研究日期：** 2026-09-02  
**性质：** 非规范性 Research

## 1. 研究问题

Implementation Minimality 不是“代码越少越好”，而是在满足当前权威需求、验证责任、工程健康和长期约束的前提下，避免为尚未出现的未来需求提前引入没有当前证据支持的功能、抽象、配置、扩展点、依赖和结构复杂度。

## 2. 外部证据

研究基线引用：

- Martin Fowler — YAGNI；
- Martin Fowler 对 Kent Beck Simple Design 的整理；
- Google Engineering Practices — Complexity / Over-engineering；
- Sandi Metz — The Wrong Abstraction；
- Go Code Review Comments — Interfaces（作为技术实例，不直接泛化成跨语言接口规则）。

共同支持：

- 未来需求没有证据时，不应提前建设 presumptive feature / abstraction / configurability；
- 复杂度存在持续的理解、修改、验证和错误风险成本；
- 抽象应追随已观察到的稳定共享语义，而不是只由表面重复触发；
- “最少元素”必须与正确性、清晰表达和真实重复消除共同理解；
- 保持代码可修改性、必要测试、安全、错误处理和当前约束不属于应被 YAGNI 删除的推测性复杂度。

## 3. 判断边界

### 当前责任优先

新增复杂度应能追溯到当前需求、架构/安全约束、真实消费者、验证责任或已经可见的风险。

### 抽象不是默认目标

- 单一实现的“未来可能第二种”不足以创建通用接口；
- 两段表面重复不自动证明存在稳定共享概念；
- 已经存在多个真实消费者且共享语义稳定时，抽象仍然是合理工具；
- 错误抽象若依赖越来越多条件参数维持，应允许退回更直接结构。

### 最小化不是最少代码

不能为了减少代码量而：

- 放弃当前必要测试；
- 隐藏真实差异；
- 绕过安全 / 错误处理 / 可观察性；
- 忽略已存在公共契约、兼容义务或难逆数据约束。

### 低成本演进准备

如果某项设计几乎不增加当前理解与维护成本、不形成额外公共承诺，并有当前证据显示能显著降低已经可见的后续成本，可以单独权衡，而不是机械拒绝。

## 4. V4 当前落点

该能力本身不是独立任务流程，因此不形成 Skill。V4 当前规范 owner：

`docs/rules/generation/implementation-minimality.md`

本文件只保留外部证据和判断边界，不再描述旧 Candidate / Engineering Discipline / milestone 状态。

## 5. 结论

实现应选择当前证据支持的最低必要复杂度。真正需要的测试、失败路径、安全约束、已有真实多消费者的稳定抽象和薄适配可以是必要复杂度；仅服务假想未来需求的复杂度默认不进入当前实现。