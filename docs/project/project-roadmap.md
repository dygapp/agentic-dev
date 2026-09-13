---
id: project:roadmap
type: project
status: active
---

# Project Roadmap

## 当前长期目标

`agentic-dev` 当前正在执行 **V4 — 分布式规则发现与仓库基础重构**。

V4 是断代式 Foundation Rebuild：当前工作树只表达最终有效状态，不维护 V1～V3 current compatibility layer。V1～V3 的演进历史由 Git / Issue / PR 保留。

V3 最终不可变定位：

`agentic-dev@1c8cdfea9ecf23ef33ffab20eec3c93679fd4578`

## V4 目标运行模型

```text
Current task / repository facts
→ 少量可观察 task signals
→ Rule Discovery Tool 扫描 Rule 自身 Front Matter
→ 确定性候选初筛
→ 少量 Rule locators
→ LLM 读取候选正文并确认最终适用性
```

核心验收：工具可以扫描 N 条 Rule，但 LLM discovery context 只随候选数 k 增长，且 `k << N`。

## Gates

- **V4-00 — Baseline Freeze & Rebuild Boundary：完成。** frozen base 与 V3 immutable locator 已建立；V4 工作分支 / Draft PR 策略已确定。
- **V4-01 — Asset Inventory & Classification：完成。** 已完成全仓白名单审计；`ARCHIVE = 0`；历史 project / tasks / discovery surfaces 明确退出 current tree。
- **V4-02 — Front Matter & Rule Discovery Contract：完成。** 已冻结公共 Front Matter、Rule scope、task signals、deterministic matching、locator-only output 与 fail-closed contract。
- **V4-03 — Information Architecture & Rule Decomposition：当前。** 重建 Skill / Rule / Guide / Architecture owner，拆分 runtime Rules，删除 V1～V3 current surfaces，并为所有最终保留 Markdown 收敛 Front Matter。
- **V4-04 — Rule Discovery Tool & Lint：待 V4-03 完成后进入。**
- **V4-05 — Runtime Integration：待前置 Gate。**
- **V4-06 — Generation / Verification Discriminating Evals：待前置 Gate。**
- **V4-07 — Token Scaling Gate：待前置 Gate。** 必须使用 20 / 100 / 500 rules 验证同一任务。
- **V4-08 — Consumer Validation：待前置 Gate。** 真正 Consumer 修改必须在 Consumer 自己的 Fresh Context / Repository Authority 中完成。
- **V4-09 — Closure & Baseline Replacement：待前置 Gate。**

## 当前工作入口

Issue #122 是 V4 的规划、分类、实验与 Gate evidence 入口。当前 V4 foundation candidate 由 Draft PR #123 承载。

Roadmap 不复制瞬时 Actions 状态、精确 PR Head 或临时分支清理事实；这些由 GitHub 原生对象维护。

## 人工门禁

以下操作不因 V4 branch / PR 存在而自动授权：

- merge；
- release / tag；
- destructive remote cleanup；
- Consumer Repository 文件修改；
- 其他 Repository Authority 明确保留给人工的高影响动作。

普通 Rule 拆分、工具实现、lint、eval 与文档收敛在当前 V4 目标内连续推进。