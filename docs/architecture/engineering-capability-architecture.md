---
id: architecture:engineering-capability
type: architecture
status: active
---

# 工程能力架构

## 1. 分层

`agentic-dev` 的 current reusable capability 由四类 owner 组成：

1. **Method**：定义软件开发生命周期、阶段返回、权威与人工边界；
2. **Skill**：定义可独立调用的稳定执行闭环；
3. **Rule**：定义跨一个或多个过程按条件生效的约束、默认值、不变量与完成声明要求；
4. **Guide**：只提供面向人的初始化、采用、升级与低频说明。

Research / Eval 为证据与回归资产，不是规范性 owner。Consumer Repository Authority 始终拥有自身项目事实。

## 2. 单一语义所有者

同一规范语义只允许一个 current owner：

- 完整过程属于 Skill；
- 普通横切约束属于 Rule；
- 生命周期语义属于 Method / Architecture；
- 人类说明属于 Guide。

不得为了发现方便复制规范正文，也不得为了减少 Rule 数量把普通约束机械升级为 Skill。

## 3. Skill 准入

Skill 必须同时存在稳定 Trigger、Inputs、Procedure、Outputs、Exit Conditions 与 Escalation，并具有独立调用价值。只表达“应遵守什么”的内容不满足 Skill 身份。

当前核心方法 Skill 为：`clarify-intent`、`specify`、`technical-plan`、`slice-work`、`readiness-check`、`execute-unit`、`systematic-debug`、`converge`。

V4 重新分类后新增两个 reusable supporting Skill 候选：`external-operation` 与 `review-change`；`github-actions-verification` 继续作为平台专项 Skill。它们不增加新的 Method Stage。

## 4. Rule 准入

Rule 必须能独立回答一个规范问题，并具有可观察的适用信号。一个 Rule 文件不应同时承担多个可独立触发、独立演进的约束。

Rule 的 discovery metadata 与正文同文件维护，发现 contract 由 `rule-discovery-architecture.md` 定义。

## 5. Guide 边界

Guide 不承担 ordinary runtime rule routing。Consumer 初始化、首次采用、baseline upgrade、人工操作说明可以保留 Guide；真正执行时的规范约束必须回到 Method / Skill / Rule / Consumer Authority。

## 6. Consumer lifecycle

上游能力只有经过 Consumer 显式采用才进入 Consumer current state。普通运行只依赖 Consumer-local current owner；upstream 新提交不会自动改变 Consumer。