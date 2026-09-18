---
id: guide:guides-navigation
type: guide
status: active
---

# 人类使用指南

`docs/guides/` 只承担 **Human View**：帮助人理解、采用和维护 `agentic-dev`。普通 Agent 运行时默认不依赖这里的文档；正式 Method、Rule、Skill contract 与 Architecture 以各自规范性归属为准。

推荐阅读：

1. [`using-agentic-dev.md`](using-agentic-dev.md) — 从整体上理解项目和日常使用方式；
2. [`language-and-terminology.md`](language-and-terminology.md) — 理解中文表达、原始标识、正式概念身份和语言复核方式；
3. [`establishing-requirement-baseline.md`](establishing-requirement-baseline.md) — 新项目从 Raw Project Inputs 建立 `docs/requirements`、进行高效需求会话、控制问题下钻尺度并收敛到 `Requirement Baseline Ready` 的人类操作指南；
4. [`feature-development.md`](feature-development.md) — 普通 Feature / change 从 Clarify Intent、Specification、可选 Technical Planning、Slice & Ready、Execute 到 Converge / `Ready to Integrate` 的连续人类操作指南；
5. [`human-review.md`](human-review.md) — 理解何时进入人工评审、如何使用结构化 Markdown Review Draft、怎样分类反馈并把长期语义回写真正 Authority，以及 HTML / DOCX 何时才作为显式交付投影生成；
6. [`github-agent-workflow.md`](github-agent-workflow.md) — GitHub 托管 Repository 中 Local / Cloud Repository Runtime、GitHub Connector 与 GitHub Actions 的协同方式、责任转换、副作用边界与人工升级边界；
7. [`adopting-agentic-dev.md`](adopting-agentic-dev.md) — 人类视角的 Consumer 首次采用指南；
8. [`upgrading-agentic-dev.md`](upgrading-agentic-dev.md) — 人类视角的 Existing Consumer 升级指南；
9. [`multi-model-collaboration.md`](multi-model-collaboration.md) — 理解 Model Collaboration capability、Consumer adoption、路由与验证边界；
10. [`codex-model-collaboration-reference.md`](codex-model-collaboration-reference.md) — Codex 平台的非规范参考配置、角色配置与运行时冒烟检查结构；
11. [`rule-activation-guide.md`](rule-activation-guide.md) — 理解 Rule Discovery 如何工作；
12. [`consumer-local-rule-activation.md`](consumer-local-rule-activation.md) — 理解 Rule 如何在 Consumer 本地化。

Guide 可以完整解释规范流程，但不重新定义 Gate、路由或规范策略。若 Guide 与规范性归属冲突，以 Method / Architecture / Skill / Rule 为准并修正 Guide。
