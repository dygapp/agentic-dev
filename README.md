---
id: repository:readme
type: repository
status: active
---

# agentic-dev

`agentic-dev` 是面向 AI Agent 驱动软件开发的通用 Method、Skill 与 Rule 仓库。

## 当前模型

```text
Repository facts + current task
→ 少量 task signals
→ Rule Discovery Tool 扫描 Rule 自身 Front Matter
→ 少量 Rule locators
→ LLM 读取候选正文并确认适用性
→ Skill / Method 按当前 Authority 执行
```

规则发现不再依赖人工同步的 Reviewed Discovery Map、Activation Manifest、Runtime Catalog 或 rule-index。规则 metadata 与正文同文件维护；全量 metadata 不进入 ordinary LLM context。

## 入口

- 稳定仓库治理：`AGENTS.md`
- 当前项目路线：`docs/project/project-roadmap.md`
- 核心方法：`docs/method/ai-development-method.md`
- 顶层原则：`docs/method/principles.md`
- Rule Discovery 架构：`docs/architecture/rule-discovery-architecture.md`
- Skill 架构：`docs/architecture/skill-architecture.md`
- Consumer 生命周期：`docs/architecture/consumer-lifecycle.md`
- Rules：`docs/rules/`
- Skills：`skills/`
- 面向人的采用说明：`docs/guides/`
- 非 Authority 研究：`docs/research/`

## Fresh Context

新会话只需要声明 Fresh Context、目标仓库、必要前置动作和本轮特殊约束。Repository Authority、开发方法、运行规则和发现机制应从目标仓库当前文件恢复，不应复制到会话提示词中。

## Skill / Rule / Guide

- **Skill**：稳定独立执行闭环；
- **Rule**：必须遵守但不构成完整流程的最小规范单元；
- **Guide**：面向人的初始化、adoption、upgrade、恢复与低频说明。

当前 Skill inventory 见 `skills/README.md`。Rule 目录仅供人类组织，真正匹配只使用 Front Matter。

## Consumer

Consumer 自己的 Repository 是唯一项目事实来源。首次采用与显式 baseline upgrade 可以读取 `agentic-dev`；采用完成后的 ordinary runtime 使用 Consumer-local Rules、Skills 和 Rule Discovery Tool，不在线依赖本仓库。

## 当前项目状态

V4 Foundation Rebuild 正在 Issue #122 下进行。V3 最终不可变定位为：

`agentic-dev@1c8cdfea9ecf23ef33ffab20eec3c93679fd4578`

当前 Gate 与下一步只在 `docs/project/project-roadmap.md` 和 GitHub 当前 Issue / PR 中维护。