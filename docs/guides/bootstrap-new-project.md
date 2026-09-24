---
id: guide:bootstrap-new-project
type: guide
status: active
---

# 新软件项目 Bootstrap

本 Guide 是 `agentic-dev` 的绿地入口。目标是在 Repository 尚不存在、installed Skills 尚不可用时，用最少必要的人机协作建立一个 Consumer-owned 软件 Repository，然后把普通工作切换到 Repository Authority + installed Skills。

Bootstrap 是 Guide 的有界预运行时例外：它可以编排“澄清 → 建库 → 安装 → 建立入口”。一旦 Consumer runtime 建立完成，可独立复用的执行过程由 Skills 持有，Guide 不继续充当隐藏 Method。

## 1. 最小输入

用户通常只需要提供：

- `agentic-dev` Repository；
- 明确的 `agentic-dev` 精确版本 / immutable tag；
- 新项目目前已知的基本情况。

基本情况可以很少，例如：

```text
我要开发一个高校就业管理系统。
主要用户是省级业务人员、学校管理员和毕业生。
后端计划使用 Java/Kotlin，前端 Vue。
已有一批客户需求材料，后续可以整理。
```

不要求用户先设计目录、Method、Rule、Architecture 或 Skill 组合。

## 2. 先恢复已知事实，不重复访谈

AI 先把输入分成：

- 已明确事实；
- 可以唯一推导的事实；
- 安全的初始候选 / 默认；
- 真正会改变项目目标、范围、核心业务边界或长期高成本约束的阻塞歧义。

已经明确的事实不重复询问。普通技术细节、局部可逆选择、未来 Feature 细节不在 Bootstrap 阶段穷举。

## 3. 最小谈判式澄清

只有下列问题同时满足时才向用户询问：

1. 当前已有信息和来源无法裁决；
2. 至少存在两个合理答案；
3. 不同答案会实质改变项目目标、主要用户、核心范围、关键业务边界或长期高成本约束；
4. 不解决就无法建立一个不误导后续工作的初始 Repository。

典型 Bootstrap 只需要确认：

- 项目解决什么问题；
- 主要使用方 / Actor；
- 第一阶段大致范围；
- 明确非目标；
- 已知外部约束；
- 已知技术 / 部署硬约束；
- 原始需求材料或既有系统的来源角色。

如果当前信息已经足够，就直接形成候选初始包并让用户 review，而不是为了“需求完整”继续提问。

## 4. 什么时候停止澄清

达到以下最低阈值即可建库：

- 项目 Goal 可以清楚表达；
- 主要使用方已知；
- 初始 In / Out of Scope 不会严重误导后续工作；
- 已知硬约束有保存位置；
- 后续 Requirement 建立所需的原始输入可以定位；
- 没有会让“这个项目到底是什么”产生实质不同答案的未决 blocker。

这不是 `Requirement Baseline Ready`。Bootstrap 只建立可以继续工作的最小 Repository。

## 5. 建立 Consumer-owned Repository

推荐起点可以是：

```text
<project>/
├── AGENTS.md
├── README.md
├── docs/
│   ├── requirements/
│   ├── architecture/
│   ├── project/
│   └── work/
└── .agents/
    └── skills/
```

这是推荐 IA，不是强制模板。已有组织标准、单仓 / 多仓边界或项目规模可以决定不同路径。

Bootstrap 至少要确保：

- 根 `AGENTS.md` 很薄；
- 项目事实有 Consumer-owned 稳定入口；
- 原始输入和当前 Authority 可以区分；
- 后续 current work 有可恢复位置；
- 安装 Skills 不会覆盖 Consumer docs。

## 6. 根 AGENTS.md 只做 Bootstrap

根 `AGENTS.md` 建议只维护稳定入口，例如：

```text
# Repository Bootstrap

- 当前 Repository 是本项目事实来源。
- 项目文档入口：<consumer-selected locator>
- installed Skills：.agents/skills/**
- Consumer-local constraints：<consumer-selected locator / native scoped instructions>

## agentic-dev 方法论

- Repository: https://github.com/dygapp/agentic-dev
- adopted ref: <exact immutable tag>
- Guide root: docs/guides/
- 当用户询问“怎么开始 / 下一步做什么 / 方法怎么用”时，按需读取该精确版本 Guide。
- 普通执行不在线读取 upstream Provider docs 补齐 Skill 语义。
```

不要把完整 Guide、全部项目规则、当前工作流水账或 Skill procedure 复制进根 `AGENTS.md`。

## 7. 安装 exact-version Skills

使用标准 Agent Skills 兼容安装路径，把明确版本的 `skills/**` 安装到 Consumer repository-local target。

以当前验证过的 `skills` CLI 形态为例：

```bash
npx -y skills@1.7.0 add \
  https://github.com/dygapp/agentic-dev/tree/<exact-tag> \
  --skill '*' \
  --agent codex \
  --copy \
  --yes
```

这只是一个经过 P1 验证的 Codex 示例。实际安装器版本和目标 Agent 必须先满足其当前运行时前置，不把某个 CLI 版本写成永久方法论要求。

安装后至少验证：

- 预期 Skill inventory 已安装；
- Consumer `AGENTS.md` / project docs 未被覆盖；
- native Agent runtime 能发现 repository-local Skills；
- lock / provenance 能恢复 exact ref；
- ordinary Skill execution 不需要 Provider `docs/**`。

## 8. 建立 exact-version Guide locator

Guide 不复制进 Consumer runtime，但 Consumer 应能知道自己采用的是哪一版方法论。

最小 locator 记录：

- Provider Repository；
- exact immutable tag；
- canonical Guide root / entry。

需要方法论导航时只读取这个精确版本；不可访问时明确报告导航来源不可用，不回退 `latest`、模型记忆或其他版本 Guide。

## 9. Bootstrap 完成边界

以下条件成立后 Bootstrap 结束：

- Consumer Repository 已建立；
- 根 `AGENTS.md` 和项目知识入口可恢复；
- Skills 已安装且 native discovery 成功；
- exact-version Guide locator 已建立；
- 已知项目基本事实已经保存到 Consumer-owned 文档；
- 下一责任可以通过项目事实 + [`choosing-next-step.md`](choosing-next-step.md) 判断。

从这一刻起，普通开发不再由 Bootstrap Guide 编排。

## 10. Bootstrap 后通常做什么

最常见的下一步不是直接编码：

- Requirement 仍只是原始材料 / 零散事实 → `establish-requirement-baseline`；
- Requirement 足够，但存在跨多个 Feature 的长期 Architecture blocker → `clarify-architecture`；
- Requirement / Architecture 已足够，存在明确 Feature → 进入 [`feature-development.md`](feature-development.md)；
- 已有成熟 Repository，只是首次引入 Skills → 不需要重跑绿地 Bootstrap，使用 [`adopting-agentic-dev.md`](adopting-agentic-dev.md)。
