---
id: rule:high-impact-ai-review-required
type: rule
status: active
scope:
  phases: []
  activities: [review]
  technologies: []
  artifacts: [authority, skill, rule, repository-governance]
  risks: [high-impact-change]
---

# 高影响变更必须 AI 复核

会实质改变 Method、Principle、Architecture、Skill contract / core Skill、Repository Authority、Rule Discovery contract 或其他持续塑造 Agent 行为的高影响变更，在进入最终人工复核或集成决策前必须执行独立 change review。

该 Rule 只负责触发 `review-change`；具体复核 procedure 由 Skill 自身拥有。AI 复核通过不等于人工批准或集成授权。