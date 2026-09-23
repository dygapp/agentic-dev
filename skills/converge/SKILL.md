---
name: converge
description: Performs feature-wide convergence against specification, domain and architecture authority, applicable project-roadmap state, artifact lifecycle responsibilities, current implementation, and verification evidence. Use after required execution work is complete enough for final review; return READY or route evidence-backed gaps to the responsible layer, then stop at Ready to Integrate.
---

# converge

## 目的

在功能/变更范围内对 Authority、当前实现和当前证据做最终收敛，判断是否达到 `Ready to Integrate`，而不是执行集成。

## 输入

- Current Specification / Domain / Architecture Authority；
- Relevant Execution Units and implementation；
- Current verification evidence；
- Consumer-local constraints。

## 流程

1. 重新读取最终 Authority、Consumer-local constraints、当前实现与当前 Evidence，不把单个 Unit、测试、Job、Review 或工具调用的终态自动等同于整体完成。
2. 对每项可观察行为、边界、非功能义务和长期 artifact responsibility 建立当前证据对应关系。验证产物只有在其 expected behavior 仍与 Current Requirement / Specification / Architecture 一致时才有效；失败先区分 implementation defect、stale verification contract、runtime / environment 与 external dependency。
3. 检查跨 Unit 接缝、遗漏、未关闭 finding、base drift、Current locator / navigation 与状态文档一致性。长期 owner 被 replace / retire / archive 时，确认 ordinary runtime、verification consumer 与 durable current-state wording 已迁移，historical reference 被明确限制在 provenance 角色。
4. 复用祖先 commit 的 CI / Review / Runtime evidence 时，必须取得 ancestor→current 精确 diff，并证明受复用 claim 不受差异影响；记录 ancestor SHA、current SHA、差异范围和 claim mapping，不能把祖先 Run 描述成当前 Run。
5. 当前变更涉及数据库 schema / migration lifecycle 且环境允许时，最终证据至少覆盖 `Fresh Database → Full Migration Chain → Application Startup`；做不到时明确保留 Evidence gap。
6. 当前变更涉及 legacy / historical / business data migration 时，检查 source / scope coverage、semantic preservation、identity / duplicate、replay / idempotency、exception / conflict disposition、provenance 与 target-side observable verification；脚本成功不能替代这些责任，legacy source 也不能反向成为新 Requirement Authority。
7. Requirement 明确要求视觉复刻、设计稿还原或视觉 fidelity 时，功能 / 路由通过不能单独推出视觉通过；按风险使用真实运行页面、参考视觉、AI 对照和必要人工复核。
8. Workflow artifact、远程输出或临时快照默认只是一次运行 Evidence；只有当前 Authority 显式接受且确需稳定消费时才晋升为持久输入，并重新验证完整性、来源与受影响 Current Evidence。
9. 高影响 Authority / Skill / Repository governance 变化按 Consumer policy 进入 fresh / independent `review-change`；复核 PASS 不等于人工集成授权。
10. 缺口按责任层返回 Clarify / Specify / Technical Plan / Slice / Execute / Debug，而不是在 Converge 中静默重设计；只要仍有当前职责可自动关闭的剩余问题就继续收敛。
11. 只有不存在已知阻塞缺口且 Authority、实现与当前 Evidence 匹配目标状态时返回 READY。

## 输出

- `READY TO INTEGRATE`；或
- Evidence-backed convergence gaps 与责任层。

## 退出条件

Authority、实现与当前证据一致，且没有已知阻塞缺口。

## 升级

集成、merge、release、deploy 以及必须由人工承担的高影响决定保持在仓库 / Human Authority。请求人工前先验证当前已授权工具、Evidence 与等价自动路径确实不足，并把请求缩到最小不可替代动作或决定。READY 不是集成授权。
