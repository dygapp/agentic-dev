---
id: architecture:engineering-capability
type: architecture
status: active
---

# 工程能力架构

## 1. 分层

`agentic-dev` 的长期可复用能力只有以下主要类型：

- **Method**：定义工作生命周期、阶段职责、返回与完成语义；
- **Architecture**：定义长期能力边界、组合关系和运行不变量；
- **Skill**：拥有稳定独立执行闭环的能力；
- **Rule**：在具体工作中按条件适用的约束、默认、不变量或完成声明要求；
- **Guide**：面向人的初始化、采用、升级与低频说明；
- **Research**：非规范性的外部证据与技术参考。

目录不是语义 owner。资源身份由自身 contract 与正文决定。

## 2. 升级为 Skill 的条件

候选只有同时具有稳定 Trigger、Inputs、Procedure、Outputs、Exit Conditions、Escalation、可组合性和独立评估价值时才成为 Skill。仅“重要”“多个阶段都会用”“包含若干步骤”或“希望减少 Rule 数”都不足以 Skill 化。

## 3. Rule 的位置

实现最小化、验证证据、外部操作授权、提交约束、语言规则、技术 API 约束等本身没有独立任务闭环，应成为最小 Rule，并通过当前 task signals 按需发现。

Rule 不创建新的 Method stage，也不拥有项目事实。

## 4. 能力演进

外部规范、成熟工程实践、专项 eval 或 Consumer Evidence 可以触发能力变化，但必须先判断真实 semantic owner：

- 改变生命周期 → Method；
- 改变能力边界 → Architecture；
- 形成独立过程 → Skill；
- 形成条件性约束 → Rule；
- 只是人类说明 → Guide；
- 只有证据价值 → Research。

不得为了兼容历史载体保留重复 owner。