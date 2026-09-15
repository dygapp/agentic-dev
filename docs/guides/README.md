---
id: guide:guides-navigation
type: guide
status: active
---

# Guides — 人类使用文档

`docs/guides/` 只承担 **Human View**：帮助人理解、采用和维护 `agentic-dev`。ordinary Agent runtime 默认不依赖这里的文档；正式 Method、Rule、Skill contract 与 Architecture 以各自 canonical owner 为准。

推荐阅读：

1. [`using-agentic-dev.md`](using-agentic-dev.md) — 从整体上理解项目和日常使用方式；
2. [`establishing-requirement-baseline.md`](establishing-requirement-baseline.md) — 新项目从 Raw Project Inputs 建立 `docs/requirements`、进行高效需求会话、控制问题下钻尺度并收敛到 `Requirement Baseline Ready` 的人类操作指南；
3. [`adopting-agentic-dev.md`](adopting-agentic-dev.md) — 人类视角的 Consumer 首次采用指南；
4. [`upgrading-agentic-dev.md`](upgrading-agentic-dev.md) — 人类视角的 Existing Consumer 升级指南；
5. [`multi-model-collaboration.md`](multi-model-collaboration.md) — 理解 Model Collaboration capability、Consumer adoption、路由与验证边界；
6. [`codex-model-collaboration-reference.md`](codex-model-collaboration-reference.md) — Codex 平台的非规范参考配置、角色 profile 与 runtime smoke 检查结构；
7. [`rule-activation-guide.md`](rule-activation-guide.md) — 理解 Rule Discovery 如何工作；
8. [`consumer-local-rule-activation.md`](consumer-local-rule-activation.md) — 理解 Rule 如何在 Consumer 本地化。

Guide 可以完整解释规范流程，但不重新定义 Gate、routing 或 policy。若 Guide 与 canonical owner 冲突，以 Method / Architecture / Skill / Rule 为准并修正 Guide。