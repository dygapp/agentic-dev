---
id: guide:github-agent-workflow
type: guide
status: active
---

# GitHub Agent 工作指南

本 Guide 面向使用 GitHub 托管 Repository 的项目参与者，解释 ChatGPT / Codex / Codex CLI、Repository Runtime、GitHub Connector 与 GitHub Actions 如何协同工作。

它只承担 **Human View**。Repository Authority、Method、Architecture、Skill、Rule 与 Tool contract 仍由各自 canonical owner 定义；ordinary Agent runtime 不依赖本 Guide。若本 Guide 与目标 Repository 的 `AGENTS.md` 或 canonical capability 冲突，以后者为准。

## 1. 三层模型

GitHub 场景采用 `Repository Authority / execution transport / verification` 三层模型，并把三类责任分开：

```text
Repository Authority / Rule Discovery
→ 决定按什么约束工作

execution transport
→ 决定当前通过什么可用 surface 执行动作

verification
→ 决定是否可以声明 completion / PASS / Ready to Integrate
```

execution transport 不拥有 Method、Rule 或 Authority 语义。Connector 可写、Actions 可运行、当前存在 shell，都只说明某条执行路径可能可用，不说明任务已获授权，也不说明验证义务已经满足。

## 2. 最薄 Project Instruction

ChatGPT Project Instruction 只保存会话级、Repository 外无法恢复的稳定入口。例如：

```text
目标仓库：<owner/repository>。
GitHub Repository 是唯一项目事实来源。
开始后先从目标仓库 AGENTS.md 恢复 Repository Authority、Development Method 与当前工作规则。
需要 Repository mutation 时，优先使用当前可用 Repository Runtime；GitHub-native 协调使用已授权 Connector / Actions。
不要把其他聊天、个人记忆或本提示中的仓库状态当作当前事实。
```

不要把 Method、Rule body、Skill procedure、Roadmap 快照、workflow catalog 或旧 SHA 复制进 Project Instruction。Consumer 有额外生产权限、跨仓库边界或人工审批约束时，只补充 Repository 无法持有的特殊限制。

## 3. Fresh Chat Bootstrap

Fresh Chat 的入口同样保持简洁：Fresh Context、目标 Repository、事实源、bounded goal 和必要特殊约束。Agent 随后从 Repository 恢复真实运行语义：

```text
current Repository AGENTS.md
→ Project Capability Profile + GitHub current facts
→ Method Selection 或 direct responsibility
→ task signals
→ task-level Rule Discovery
→ applicable Rules / Skills / Architecture
→ execute
→ required verification
→ completion decision
```

定位用的 branch、PR、Issue 或 SHA 必须重新核验。历史聊天、memory、Guide 和模型常识都不能代替当前 Bootstrap；即使最终答案碰巧正确，没有实际走过 Authority / Rule Discovery 链仍不构成合格执行。

## 4. execution transport 的选择

选择 transport 时先看当前责任和实际能力，不给整个会话贴固定模式标签。

- 已有绑定目标 Repository 和目标 baseline 的 worktree、filesystem、shell、Python、git、build 或 test 能力时，直接使用现有 Repository Runtime；
- GitHub Issue、PR、Review、branch、commit、Actions 等 coordination 使用已授权 GitHub Connector / API；
- 当前 Agent 没有 worktree，而 Repository 声明了自动化远程路径时，可以让 GitHub Actions 在 exact SHA / exact PR Head 上执行 Repository 自己的 Tool、script、build 或 test；
- 一个 surface 做不到时，继续检查 Repository 已声明且已授权的其他自动化路径；只有适用路径都不可用时才进入 Human escalation。

当前 Agent 没有 checkout 不能成为跳过 Rule Discovery、跳过 verification 或默认要求用户在本地代跑命令的理由。反过来，已有 Repository Runtime 时也不应为了形式统一强制绕行 Actions。

## 5. Existing Repository Runtime first

可用 Repository Runtime 能直接提供真实 worktree 语义：

- 编辑多个关联文件；
- 查看完整 diff；
- 运行 Repository scripts、lint、tests 与 build；
- 使用 git 建立 commit；
- 在本地重现失败并验证修复。

使用前仍需确认 worktree 实际属于目标 Repository、baseline 正确、工作区变化可识别。现有 runtime 不因“本地”而获得额外 Authority，也不能绕过 side-effect 前的 task-level Rule Discovery。

## 6. GitHub Connector 是 control plane

GitHub Connector / API 适合承担：

- 读取 current branch、commit、Issue、PR、Review 与 workflow 状态；
- 创建或更新 Authority 允许的有界 GitHub 对象；
- 触发 Repository 已声明的 workflow；
- 读取 run、job、step、logs、artifact 与 terminal result；
- 在 GitHub-native mutation 足以完整表达改动时建立 branch、commit 与 PR。

写入前先读取 live object 并检查可复用 identity，避免重复 Issue、PR、branch 或 run。API 返回成功后重新读取事实来源。Connector 的某个 wrapper 缺少按钮时，应检查 standard GitHub API、Repository Runtime 或 Actions 等适用路径，不能立即把机械中转交给人。

## 7. GitHub Actions 是 repository compute plane

GitHub Actions 可以为没有本地 checkout 的 Agent 提供 Repository-native deterministic compute。典型 workflow 以明确输入绑定 subject：

```yaml
- uses: actions/checkout@v4
  with:
    ref: ${{ inputs.target_sha }}
    fetch-depth: 1

- name: Verify exact subject
  run: |
    test "$(git rev-parse HEAD)" = "${{ inputs.target_sha }}"
    python3 path/to/repository_tool.py
    ./path/to/repository_verification
```

关键要求是：

- 输入使用 exact 40-character commit SHA 或可解析的 exact PR Head；
- `actions/checkout` 后验证 actual `HEAD` 与 requested subject；
- 执行该 checkout 自己的 canonical Tool / tests / scripts；
- 输出 invocation、输入、requested / actual subject、result 与 terminal state；
- 需要跨 surface 恢复结果时上传 artifact，并保留 logs；
- invalid input、checkout drift、Tool failure、缺失 artifact 或不可恢复 result 均 fail closed。

Actions 是执行和证据生成 surface，不是新的 Authority 层，也不是整场会话的身份。

## 8. task-level Rule Discovery 不等于 smoke CI

同名 workflow 可以有不同责任，必须看实际输入与执行链：

- PR / push smoke CI 通常只验证 Rule corpus、Tool 与固定场景是否健康；
- task-level Rule Discovery 必须携带当前 responsibility 的 bounded task signals，在明确 Repository baseline 上调用该 baseline 自己的 canonical Tool，并返回 locator-only result。

因此 smoke CI PASS 不能证明当前 Agent 已完成 task-level discovery。当前 Agent 取得 candidates 后仍需读取候选 Rule 正文并确认真实适用性；空 candidates 也不能触发全量 Rule 枚举或从 Guide 反向猜测 locator。

如果 canonical locator 或所有 declared transports 已破坏，应 fail closed。Guide 中恰好写着正确答案不能成为 runtime fallback。

## 9. GitHub-native mutation

当 Repository Authority 允许、当前任务能够由 GitHub Contents / Git Data / Issue / PR API 完整表达，且不需要模拟未执行的 worktree 行为时，GitHub-native implementation 是合法路径。例如：

- 更新一个有明确 current blob SHA 的文本文件；
- 由多个 blob / tree 建立单一目的 commit；
- 推进已存在 branch 并创建或更新 Draft PR；
- 在 Issue / PR 回写 Evidence。

这类 mutation 仍受同样治理约束：首次 side effect 前完成当前责任的 Rule Discovery，写入时绑定 expected current state，写后重新读取 branch / commit / PR，并按当前 Authority 执行 verification。不能因为 API 已提交文件就宣称 build、test 或 runtime behavior 已通过。

## 10. Verification closure

verification obligation 来自当前 Method、Rule、acceptance 与目标 Repository，不来自 transport 偏好。完成声明至少回答：

- 验证的 exact subject 是什么；
- required checks 实际执行了什么；
- 执行是否到达可观察 terminal state；
- logs / artifact / report 是否可恢复；
- 当前 Evidence 是否支持所声称的 completion、PASS 或 Ready to Integrate。

`workflow started` 不等于 PASS；workflow request accepted 也不等于目标 job 成功。`ancestor Evidence` 不自动支持 current Head：验证后 Head drift 时，受影响 claim 必须在新 exact Head 重新取得 Evidence，或满足 Repository 明确允许的严格 claim-level reuse contract。

## 11. Governance checkpoints

### Discussion → Mutation

讨论或设计即使已经形成完整方案，第一次 Repository / Issue / PR / workflow / deploy side effect 前，仍需依据当前 exact baseline、direct responsibility 与 task signals 完成 Rule Discovery。聊天中的方案不获得自动执行权限。

### responsibility transition

activity、technology、artifact、risk 或 Method responsibility 实质变化后，旧 candidate set 不自动跨责任有效。下一次 side effect 前重新发现，并重新核验当前 branch / PR / Head 等 live facts。

### Repository switch

同一 Chat 切换到另一个 Repository 时，从新 Repository 的 `AGENTS.md` 重新 Bootstrap。原 Repository 的 Profile、Rule candidates、permissions、branch 与 Evidence 不得被带入新 Repository。

## 12. Consumer-local adoption / upgrade

Consumer ordinary runtime 默认 `upstream access = 0`。首次 adoption 不能只复制 Method、Architecture、Rule、Tool source 或 locator；对于依赖 Tool、compute 或 external integration 的 accepted capability，还要在 Consumer-local Authority 建立：

- obligation 与 canonical locator；
- direct execution path；
- automated alternate path；
- result / Evidence recovery；
- fail-closed behavior；
- Fresh Runtime validation。

upstream delta 改变 Tool contract、runtime assumption、Rule Discovery、verification behavior 或 executable path requirement 时，upgrade 必须刷新受影响的 local executable instance，并为改变后的 ordinary runtime behavior 重新取得 Current Evidence。具体 transport 可以不同于 `agentic-dev`，但不能在线依赖 upstream Guide 或 Profile 补流程。

## 13. Human escalation last

以下情况才可能形成真实人工 blocker：

- Authority 明确保留给人的决定或操作；
- 缺少不可替代的 credential、permission 或 secret；
- 多个高影响选择无法从 current Authority 唯一解析；
- 需要现实世界动作，而当前系统不能执行；
- 所有 Repository 已声明且适用的自动化路径都无法安全完成。

准备请求人工前，应按目标 Repository 的 Rule Discovery 重新进入 human escalation responsibility。不要仅因当前首选 surface 缺少一个能力，就要求用户复制命令、代跑 discovery、下载再上传 artifact，或在两个 Agent 都可访问的系统间人工搬运信息。

## 14. 历史失败模式与替代路径

| 失败模式 | 正确替代路径 |
|---|---|
| 依赖旧聊天、memory 或提示中的 SHA | 从 current `AGENTS.md` 与 GitHub live state Bootstrap |
| 当前 Agent 无 checkout，因此跳过 Rule Discovery | 使用 Repository-local declared exact-baseline transport；都不可用才 fail closed |
| 有 local runtime 仍强制远程绕行 | 直接运行 canonical Tool / verification，并用 Connector 处理 coordination |
| PR / push smoke 绿色，视为当前任务 discovery 完成 | 以当前 task signals 执行 task-level discovery |
| writable Connector 直接改文件 | 先完成 Authority / Rule Discovery，再做 bounded mutation 与写后核验 |
| workflow 已触发就报告 PASS | 等待目标 subject 的 jobs 到达 terminal state并恢复 logs / artifact |
| 使用旧 Head 的成功结果支持新 Head | 对受影响 claim 重新取得 exact-head Current Evidence |
| canonical locator 已坏但从 Guide 猜出答案 | fail closed 并修复 canonical owner / local instance |
| Consumer 在线读取 upstream 补运行路径 | 在 adoption / upgrade 中建立或刷新 Consumer-local executable instance |
| Connector 单一接口不足便请求人工 | 先检查 API、Repository Runtime、Actions 与其他已声明自动化路径 |

## 15. 独立 AI Reviewer 的边界

Repository 未来可以单独评估在 Actions 中调用独立 LLM reviewer，但这会引入模型选择、credential、费用、输入边界、可重复性与输出治理问题。它不是当前 GitHub bootstrap、Rule Discovery 或 deterministic verification 的 required capability，也不能替代 Repository 已有的 Chat / Fresh Context / Human semantic review flow。
