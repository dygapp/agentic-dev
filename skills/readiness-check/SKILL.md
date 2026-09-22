---
name: readiness-check
description: Performs a read-only pre-execution gate across specification, optional technical plan, execution units, domain and architecture authority, artifact lifecycle responsibilities, and governance. Use immediately before execution to return PASS or evidence-backed findings; never repair authoritative artifacts inside the check.
metadata:
  agentic-dev-id: "skill:readiness-check"
  agentic-dev-type: "skill"
  agentic-dev-status: "active"
  agentic-dev-distribution: "release-direct"
  agentic-dev-release-target: "software-development"
  agentic-dev-release-inputs: "method:ai-development;rule:human-intervention-necessity;rule:evidence-type-must-match-claim;rule:execution-continuity-and-stop-condition;rule:verification-contract-currentness"
---

# readiness-check

## 目的

在 Execute 前做只读门禁，判断目标 Execution Unit 是否具备清晰 Authority、边界、依赖、验证责任与当前可执行性。

## 输入

- Target Execution Unit；
- Current Specification / optional Technical Plan；
- Domain / Architecture / Repository Authority；
- 当前仓库事实；
- 当前运行环境提供的适用约束 / references 与 Consumer-local policy。

## 流程

1. 重新读取当前 Unit 与其直接 Authority，不沿用旧会话的就绪结论。
2. 读取并应用当前运行环境为本职责提供的适用约束；Consumer Release 使用随 Skill 打包的 references 与 Consumer-local policy，provider runtime 服从当前 Repository Bootstrap。
3. 检查 Specification readiness、必要技术决定、Unit scope、依赖、artifact lifecycle、权限和 completion/verification 定义。
4. 检查 base drift 或当前仓库状态是否使既有计划失效。
5. 只报告 evidence-backed finding；本 Skill 内不修复 Authority、计划、代码或配置。

## 输出

- `PASS`；或
- Findings：事实、影响、责任层与最小返回路径。

## 退出条件

只有不存在阻塞执行的已知 finding 时返回 PASS；否则准确返回负责修复的上游层。

## 升级

Authority 冲突、产品/架构高影响决定或权限问题需要人工时升级。PASS 不自动授予 merge / release / deploy 权限。
