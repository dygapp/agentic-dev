# 第一批核心 Skill 设计基线

**状态：** Design Baseline v0.1  
**输入权威：** `AGENTS.md`、`docs/method/ai-development-method.md`、`docs/architecture/skill-architecture.md`、`docs/architecture/skill-contracts.md`

## 1. 目的

本文把已复核的 Skill Contract 转换为第一批 `SKILL.md` 的实现设计约束。它不新增开发方法，只说明第一批 Skill 应如何实现既有方法语义。

第一批固定为：

- `clarify-intent`
- `specify`
- `technical-plan`
- `slice-work`
- `readiness-check`
- `execute-unit`
- `systematic-debug`
- `converge`

## 2. 统一实现原则

每个 Workflow / Investigation Skill 的 `SKILL.md` 应至少包含：

```text
Purpose
Use When
Do Not Use When
Inputs
Authority Sources
Procedure
Outputs
Exit Conditions
Escalation Conditions
Context Rules
Allowed Sub-skills / Disciplines
```

实现时统一遵守：

1. Skill 只实现一个清晰职责，不自动接管完整生命周期。
2. Authority First，发生冲突时遵守 Repository Authority Hierarchy。
3. 使用 Progressive Disclosure，只加载当前职责需要的上下文。
4. Conversation History 不是权威知识。
5. Exit Condition 必须可以明确判断，避免无限分析。
6. Human Escalation 统一基于 Authority、Impact、Reversibility。
7. 没有当前证据，不得声明实现、验证或收敛完成。
8. Ready to Integrate 是通用方法终点；Skill 不自动 Merge / Push / Release / Deploy。

## 3. 各 Skill 的最小实现重点

### 3.1 `clarify-intent`

实现重点：

- 只识别会 materially affect Product Intent / Acceptance 的问题；
- 自动忽略普通、低影响、可逆实现细节；
- 输出必须可以直接喂给 `specify`；
- 如果没有阻塞问题，应快速退出，不制造讨论流程。

首版不需要：

- 技术方案模板；
- Code Inspection 流程；
- 单独永久 Clarification Artifact 强制要求。

### 3.2 `specify`

实现重点：

- 强制 WHAT / WHY 边界；
- 对 Existing Specification 支持增量更新；
- 必须包含 Fresh-Agent Spec Ready 自检；
- 能明确发现 Requirement Conflict / Product Decision 缺失并停止。

首版不需要：

- 固定文件名或目录；
- 特定 Markdown / YAML 模板要求；
- Framework / Persistence 设计字段。

### 3.3 `technical-plan`

实现重点：

- 先判断是否真的需要 Technical Planning；
- 只保留跨 Unit 有持续协调价值的决定；
- 明确区分 Durable Technical Plan 与 JIT Execution Plan；
- 检查是否 Silent Redefinition of Intent。

首版不需要：

- 逐文件施工步骤；
- 固定 ADR 生成要求；
- 特定 Architecture Diagram 格式。

### 3.4 `slice-work`

实现重点：

- 以 Vertical / Independently Verifiable 为首要拆分方向；
- 为每个 Unit 强制最小逻辑字段；
- 检查 Context-fit 与 Hidden Dependency；
- 产生的是候选执行结构，不承担最终 Readiness Verdict。

首版不需要：

- 绑定 Jira / GitHub / Markdown Task；
- 强制精确 Source File Paths；
- Runtime-specific Worker 分配协议。

### 3.5 `readiness-check`

实现重点：

- 只读 Checker；
- 四维 Gate：Specification / Design / Execution / Governance；
- Finding 必须分 Blocking / Non-blocking；
- Blocking Finding 要指出返回哪个职责层，而不是自己修文档；
- 允许 Controller / Runtime 自动调用。

首版不需要：

- 自动 Rewrite Specification / Plan / Units；
- 人工 Review 作为默认步骤；
- 独立 Reviewer Agent 强制要求。

### 3.6 `execute-unit`

实现重点：

- 严格一次只执行一个 Unit；
- Fresh Execution Context；
- 先 Inspect Actual Repository State；
- Repository-specific Verification Commands 运行时发现，不硬编码；
- JIT Plan 临时化；
- Unexpected Failure 转 `systematic-debug`；
- Completion 必须由 Current Evidence 支持。

首版不需要：

- 自动遍历 Queue；
- 自动 `converge`；
- 自动 Integration；
- 永久保存 JIT Plan。

### 3.7 `systematic-debug`

实现重点：

- Reproduce first；
- Expected vs Actual 明确；
- Falsifiable Hypothesis；
- Minimal Root-cause Fix；
- Regression Evidence；
- Expected Behavior 不明确时必须回上游，而不是猜需求。

首版不需要：

- 独立 Bug Tracker 适配；
- 特定 Debugger / Observability 工具；
- 用连续 Patch 尝试替代 Root Cause Investigation。

### 3.8 `converge`

实现重点：

- Feature-wide，而不是 Unit-wide；
- READY / GAPS 二元主结果；
- 检查 Missing / Partial / Contradicting / Unrequested / Obsolete Plan / Missing Verification / Integration Gap；
- Gap 需要执行工作时交给 `slice-work` 塑形；
- READY 必须基于 Current System + Current Evidence。

首版不需要：

- 把 Unit Status 聚合为完成结论；
- 自动修改 Specification / Technical Plan；
- 自动 Integration。

## 4. 建议实现顺序

为了尽早验证 Contract 结构，同时避免一次批量实现全部 Skills，建议按以下顺序逐个落地：

1. `readiness-check`
2. `slice-work`
3. `clarify-intent`
4. `specify`
5. `technical-plan`
6. `systematic-debug`
7. `execute-unit`
8. `converge`

理由：

- `readiness-check` 是只读 Gate，副作用最低，最适合验证统一 `SKILL.md` 结构、Authority / Exit / Escalation 写法；
- `slice-work` 可以紧接着验证 Execution Unit 契约与 Gate 边界；
- Intent / Specification / Technical Planning 再补齐上游 Workflow；
- `systematic-debug` 先于 `execute-unit`，使 Execute 的 Unexpected Failure 路径在实现时已有可调用目标；
- `converge` 最后实现，因为它依赖前述 Unit、Evidence 与阶段回退语义已经稳定。

该顺序是 Skill Engineering 的实现顺序，不改变方法阶段顺序。

## 5. 第一批完成判定

第一批 Skill Engineering 不以“8 个目录都存在”为完成标准。至少需要满足：

- 每个已实现 Skill 与 reviewed contract 一致；
- 没有新增超级 Skill 或职责重叠；
- Authority Sources、Exit Conditions、Escalation Conditions、Context Rules 均明确；
- Workflow 与 Embedded Discipline 没有错误混合；
- Skill 不绑定特定语言、框架、Issue Tracker 或 Agent Runtime；
- 能够仅凭 Method + Architecture + Contract 明确判断其行为边界；
- 对完成状态的声明有当前证据。
