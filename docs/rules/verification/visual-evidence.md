---
id: rule:visual-evidence
type: rule
status: active
scope:
  phases: [execute, converge]
  activities: [verification, review]
  technologies: []
  artifacts: [user-interface]
  risks: [visual-fidelity]
---

# 视觉证据

当 Requirement 明确要求现网站点复刻、设计稿还原、品牌视觉一致性或其他视觉 fidelity 时，浏览器功能验证只能证明路由、交互、资源加载等机器可判定行为，不能单独证明视觉一致性。

视觉结论应按风险使用真实运行页面、参考截图或真实资源、AI 视觉对照与人工视觉复核。除非 Requirement 已提供可机器判定的完整视觉容差契约，不得把“功能通过”扩大成“视觉通过”。