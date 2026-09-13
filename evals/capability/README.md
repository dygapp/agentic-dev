---
id: eval-guide:capability
type: eval-guide
status: active
---

# 非 Skill 工程能力定向评估

本目录保存不通过 `$skill-name` 调用的隔离工程能力评估。

历史 `vue3-typescript-profile.json` 曾验证 monolithic Vue 3 + TypeScript Profile，并取得 9 / 9 scenarios、41 / 41 assertions PASS。该结果仍是历史 evidence，但 V4 已删除 Technology Profile runtime owner，因此**不能**把该历史 PASS 解释为 V4 technology Rule Discovery 的当前验证。

V4-06 应复用其中仍有辨识力的业务/技术场景，把输入从“整份 profile 预加载”改为：

```text
current task facts
→ task signals
→ Rule Discovery candidates
→ candidate bodies
→ model judgment / verification
```

至少保留 build-vs-typecheck、reactivity/watcher、props/v-model、template ref、tooling compatibility、Consumer override、第三方组件 Authority 与 risk-based verification 等真实差异。

运行隔离原则：

- 每场景独立 Fresh Runtime；
- 只复制场景声明的 current context；
- 不暴露 expected behavior / assertions / 历史结果；
- 退出码不等于 PASS；
- 需要语义判断时逐项人工评分。

当前 `vue3-typescript-profile.json` 在完成 V4-06 rewrite 前仅是迁移输入。