# Consumer Fixture AGENTS

本目录只用于 `agentic-dev` 规则检索 A/B 评估，不代表任何真实使用方仓库。

## Repository Authority

当前 Consumer Repository 是本项目事实、产品需求、本地开发方法和执行边界的唯一项目权威。

普通功能开发与新上下文恢复优先读取本仓库已经固化的本地 Authority，不依赖未持久化聊天，也不把上游 `agentic-dev` 自身项目状态当作 Consumer 项目事实。

## agentic-dev Baseline

当前记录的上游基线：

`dygapp/agentic-dev@364d23bee5f3505c46e29a13d353de954c216a56`

该精确基线只用于明确的 baseline upgrade、方法缺口复核或被本仓库显式要求的上游对照。

**普通开发不会因为记录了精确 baseline 就每次重新读取上游完整指南。**

只有当前任务明确进入 baseline upgrade 时，才读取目标上游基线并选择性采纳当前 Consumer 真正需要的 Method / Skill / Guide 变化；完成升级后继续以本地 Authority 为主要工作入口。

## 当前授权

当前评估任务只判断恢复与权威边界，不执行 baseline upgrade，也不修改任何文件。
