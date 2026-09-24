# Skill 产品工程规范

## 1. 产品身份

`skills/**` 是 `agentic-dev` 唯一正式的 Consumer-facing runtime product。

Skill 是在责任已经明确后，拥有稳定独立执行闭环的有界能力：

```text
Trigger / Purpose
→ Inputs
→ Procedure
→ Outputs
→ Exit Conditions
→ Escalation
```

Skill 不因为自身存在取得 Repository 写入、merge、release、deploy 或其他外部授权。

## 2. 标准 Agent Skills 兼容

每个 `SKILL.md` 使用标准 Agent Skills 兼容 frontmatter。当前 canonical Skills 只要求 `name` 与 `description`。

需要详细资料、脚本或静态资源时使用 Skill-local `references/`、`scripts/`、`assets/`。不得重新引入 distribution classification、release-input composition metadata 或 Consumer 运行时需要理解的自定义 Capability 类型。

## 3. 自包含与渐进披露

正式 Skill package 必须对通用执行责任自包含，不在线依赖 Provider `docs/**`、Project state 或 Research；只按需加载 Skill-local resources；Consumer-specific technology policy、术语、授权和项目事实继续由 Consumer-local Authority 持有。

发现必要输入、执行路径或 Evidence 不可靠时 fail closed / escalation，不在线回 Provider current state 猜测。

## 4. 核心运行角色与责任边界

- **Agent 是执行主体**：恢复 Repository Context、判断当前责任、选择并执行 Skill、解析当前责任适用的 Current Authority 与 Consumer-local Constraint、取得 Evidence，并在授权范围内完成回写；
- **Skill 是 procedure / contract**：定义某类责任的 Trigger / Inputs / Procedure / Outputs / Exit / Escalation，本身不是主动发现项目事实的主体；
- **Guide 是责任导航**：帮助人和 Agent 理解怎么开始、当前下一责任是什么以及哪些 Skill 可以组合，不复制 Skill procedure；
- **Consumer Current Authority 是当前事实与长期语义 owner**：回答“当前什么事实、contract、设计或决定是正确的”，具体类型由 Consumer 自己拥有，不由 Provider 维护固定枚举；
- **Consumer-local Constraint / Policy 是执行约束**：回答“在这个项目里做这件事还必须遵守什么”，与 Current Authority 保持独立；
- **Execution Unit 是跨 Fresh Context 的有界执行责任载体**：保存 Scope、当时已知的 Authority 恢复线索、Dependencies、Completion Conditions 与 Verification responsibility，不复制 Authority 正文，也不成为第二套 Current truth；
- `docs/governance/**` 只治理 `agentic-dev` Provider，不进入 Consumer package。

同一物理文件可以同时包含 Authority 语义与执行 Policy；分类依据是语义归属和用途，而不是文件名、目录名或“必须 / 禁止”等措辞。

## 5. Current Authority 解析与 Skill 消费

Skill 选择前，Agent 只恢复判断当前责任所需的最小 Repository Context 和 installed Skill descriptions；责任确定后，再结合当前 task / claim、Consumer-owned locator / navigation、Unit 中已有恢复线索（如存在）与当前 Repository facts，解析**当前责任实际适用的最小 Current Authority**。

Authority 解析遵循：

- Unit 中的 `Authority inputs` 是恢复线索，不是永久冻结的 owner 清单；切分后新增、替换或遗漏的 Current owner 仍必须按当前责任重新判断；
- 直接从 defect、review 或其他非 Unit 入口开始的责任，同样按当前 task / claim 解析适用 Authority；
- verified no-match 可以继续；applicability / owner / locator 无法可靠判断且会影响当前 claim 时，只 fail closed 受影响的执行或结论；
- 不通过全量枚举 Consumer Authority corpus 兜底，也不根据文件名猜测；
- 当前适用 Authority 对 correctness、Acceptance 或质量属性提出的义务必须进入 planning / readiness / execution / debugging / convergence / review 的判断和 Evidence mapping；
- durable semantic change 返回真实 Current owner。Consumer 未提供对应 owner 或维护 procedure 时，暴露缺口并升级，不由横向 Skill 临时发明新的 Authority；
- 能消费某种 Current Authority 不等于 Provider 必须提供同名 authoring Skill。

Current Authority 与 Consumer-local Constraint 都按需恢复，但语义不同：前者拥有当前正确事实，后者拥有执行方式、权限、流程或技术政策。

## 6. Inventory 与安装

实际 `skills/*/SKILL.md` corpus 是 Skill inventory 的机器事实来源；`skills/README.md` 只是 Human View。

普通 Consumer 通过标准 Agent Skills 兼容方式安装明确版本的 Skills。安装 / 更新不得覆盖 Consumer-owned `AGENTS.md`、docs、local constraints 或其他项目文件。

## 7. 准入

新增 Skill 至少证明独立 trigger / purpose、稳定 inputs、可重复 procedure、稳定 outputs、明确 exit / escalation、有界上下文、单一语义 owner，并证明现有 Skill / Guide / Consumer-local mechanism 无法更简单地承担该责任。

“很重要”“多个地方都会用”“存在多个步骤”本身不足以新增 Skill。
