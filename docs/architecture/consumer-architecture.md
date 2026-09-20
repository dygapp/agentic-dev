---
id: architecture:consumer
type: architecture
status: active
distribution: release-input
release-target: consumer-installation
---

# Consumer 架构

## 1. Consumer 归属

普通软件 Consumer Repository 始终拥有自己的项目事实、Project Knowledge、Requirement、System Architecture、代码、验证、权限、技术专项 policy 与当前工作状态。`agentic-dev` 提供的是**版本化 Software Development Agent Skills Release**，不是要求 Consumer 复制 upstream Source / Authoring Model。

核心边界：

> **Source semantics 可以进入发布物；Source type / path 不直接传播。Consumer 安装 Release，同时保留自己的 Repository Authority。**

因此：

- upstream Method / Architecture / Rule / Tool 可以继续作为 `agentic-dev` Source canonical owner；
- 它们如果参与 Consumer runtime，先经过 Distribution Build 转换 / 组合进一个或多个 Skill package；
- Consumer 不因为 upstream 存在 Method / Architecture / Rule，就自动建立同名一级 runtime namespace；
- upstream Project Charter / Capability Profile / Roadmap / Evolution 永远不是 Consumer release object。

首次安装与后续升级过程分别由对应 Method 持有；本 Architecture 只定义长期 ownership、installation boundary 与 ordinary runtime 不变量。

## 2. repository-local 默认安装形态

首版 repository-local target 以以下最小结构为核心；其中主要运行路径明确为 `.agents/skills/**`：

```text
AGENTS.md                  # Consumer-owned Repository Bootstrap / Authority

.agents/
  README.md                # Human View
  skills/
    <skill>/
      SKILL.md
      references/          # optional
      scripts/             # optional
      assets/              # optional
```

默认**不要求**创建：

```text
.agents/methods/
.agents/architecture/
.agents/rules/
.agents/contracts/
.agents/tools/
.agents/evals/
```

如果未来 Evidence 证明某种额外 repository-local runtime owner 不可替代，应先修改对应 Architecture / Release contract，而不是因为 upstream Source tree 存在同名目录就自动投影。

平台要求固定位置的 adapter 继续使用平台原生路径，例如 `.github/workflows/**`；目录统一不能覆盖平台 contract。

## 3. Consumer-owned Bootstrap

根 `AGENTS.md` 始终由 Consumer 拥有。

Release 安装 / 更新只允许建立或更新一个**薄的 Skill runtime entry / compatibility locator**，不得：

- 用 upstream / generated `AGENTS.md` 整文件覆盖 Consumer Authority；
- 删除 Consumer 已有 Product / Project / authorization / technology policy；
- 把 provider Project state 写成 Consumer current state；
- 把全部 Skill / reference / Rule 正文塞进 Bootstrap。

安装 / 更新必须具有 bounded / idempotent integration behavior：重复执行时能够识别已有 integration，只修改当前 Release contract 真正负责的片段。

## 4. 普通运行时

安装完成后：

```text
Consumer Repository Authority / current facts
→ Consumer-owned Bootstrap
→ repository-local Skill discovery
→ matching SKILL.md
→ references / scripts / assets（按需）
→ execute / verify / return
```

ordinary runtime 默认 **`upstream access = 0`**。

本地 discovery、Skill resource、execution path 或 metadata 异常必须在 Consumer-local state 内 fail closed 或按 Consumer Authority 升级；不得自动访问 `agentic-dev` Source Repository 补流程、规则或“latest baseline”。

新的 Distribution Model 不要求普通 Consumer 运行 `agentic-dev` 自身 Rule Discovery。Consumer 如果有本地条件性 policy，可以继续由自身 Repository Authority 选择合适的承载机制；首版通用 Release 不默认安装 upstream Rule tree / Rule Discovery tool。

## 5. Consumer-local Project Knowledge 与 policy

Consumer 自己持有：

- 产品 / 项目使命与非目标；
- Requirement / Domain facts；
- System / Application / Data / Interface Architecture；
- 技术栈专项规则；
- repository / Git / external-operation authorization；
- 术语、审批、迁移、环境与组织约束；
- Roadmap / current work / integration state；
- 对当前 Consumer 仍有长期价值的演进摘要。

这些内容默认留在 Consumer 自己的 `docs/**`、`AGENTS.md` 或其他真实 Repository Authority 中，而不是被迁入 `.agents/**` 只因为 Agent 会读取它们。

Consumer-local policy 可以约束通用发布 Skill；通用 Skill 不得为了统一所有 Consumer 而吸收必然因 Repository Authority 不同而变化的本地 policy。

## 6. 可执行能力闭环

发布 Skill 如果依赖 Tool、compute 或 external integration，安装结果必须建立可恢复的 **Consumer-local executable instance**，至少能确定：

- 当前 obligation；
- canonical locator；
- direct execution path；
- direct path 不可用时的 automated alternate path；
- result / Evidence recovery；
- 所有 declared path 不可用、subject 不一致或结果不可恢复时的 fail-closed behavior。

`scripts/**` 可以随 Skill 发布，但“脚本文件存在”不等于当前 Runtime 能执行。Runtime compatibility 与 alternate path 必须由 Release contract / Skill metadata / supporting reference 清楚表达并可验证。

Fresh Runtime 必须能仅依赖 Consumer Repository 恢复这些路径；不得通过 upstream Source、Human Guide、历史聊天或模型记忆补齐。

## 7. 安装 / 升级与上游解耦

首次安装输入是：

```text
Consumer Authority
+ exact versioned release
+ release compatibility / migration metadata
```

后续升级输入是：

```text
current installed release
+ Consumer-local retained obligations
+ candidate release
```

两者都不得把以下对象重新变成普通输入：

- upstream current branch / Source tree；
- upstream Method / Architecture / Rule corpus；
- upstream Project Charter / Capability Profile / Roadmap / Evolution；
- upstream Open Issue / PR；
- “latest baseline” 在线解析。

Release provenance 可以记录 source SHA、version、Skill identities 与 migration information，但 provenance 不取得 Consumer current Authority。

## 8. Consumer Evidence 反馈

Consumer Evidence 可以通过 Issue / Comment 等方式反馈给 `agentic-dev`，但只成为 research / evolution candidate。是否改变 upstream Project Charter、Architecture、Method、Skill、Rule、Build 或 Release contract，必须在 `agentic-dev` 自己的 Repository Authority 下重新裁决。

Consumer-local 成功、目录结构或 policy 不因反馈自动泛化为所有 Consumer 的 reusable requirement。
