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

Execution Unit 用于确实需要独立恢复、协调依赖或独立验收的执行责任，不由“发生了代码修改”自动触发。若目标和验收已能从当前 Consumer Authority 恢复，修改局部、低风险、可逆，且不需要独立的长期执行生命周期，Agent 可以直接实施有界变更并取得与当前 claim 匹配的按范围验证证据。没有正式 Unit 不免除 Authority、约束、验证、复核或授权责任；范围扩大、语义缺口或风险变化时，重新判断是否需要上游澄清、切分和就绪检查。

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

## 6. 长期设计知识责任

Consumer 可以按自身事实建立长期 Design owner，但 Provider 不规定固定设计文档、目录、类型枚举或 Registry。判断依据是设计决定是否持续约束未来组件 / 接口消费者、系统替换、安全、验证或后续工作，而不是出现于多少个 EU、是不是传统“详细设计”阶段，或具体写在 Markdown、IDL / Schema、代码契约还是测试中。

- **Requirement / Specification** 拥有 WHY / WHAT、对外可观察契约、业务错误语义与 Acceptance；设计活动不得反向改写这些决定。
- **Architecture** 拥有跨 Feature、长期且难逆的系统性结构、责任与替换边界；局部但稳定的组件 / 数据 / 接口设计可以由 Consumer 另选合法 Design owner，不全部升级为 Architecture。
- **Durable Design** 是长期语义责任而非新的默认文件类型或步骤：逻辑设计可以脱离某种技术实现，物理设计只在适用实现 / 版本范围内有效。不同表示载体须遵循单一语义 owner，不以代码现状反向取代更高层 Authority。
- **Technical Planning** 是收敛 HOW 的活动；**Technical Plan** 是条件性实施方案，不因其存在就成为长期设计权威；**ADR** 条件性保留重要取舍的理由与历史，不取代当前设计；**EU / JIT Plan** 是短生命周期执行责任，不保存第二套设计真值。

当长期设计候选在规划或执行时出现，Agent 判断长期约束价值与现有 owner；在 Consumer 允许的 owner 建立 / 更新程序下明确适用范围、消费者、版本与可发现路径，再实施相应写回与验证。缺少合法 owner / 程序且影响当前 claim 时升级受影响责任，不允许横向 Skill 静默创造 Authority。新旧 owner 替代 / 退役同步迁移 locator、消费引用、契约与测试；正常局部可逆修改不强制 Technical Plan、设计文件或 EU。

### 设计责任边界的长期取舍依据

此前按“跨多个 EU 的 HOW”决定是否进入 Technical Planning，无法覆盖单个 EU 中形成、但未来组件、接口消费者或替换工作仍必须遵守的长期契约。故将判断标准改为**持续约束价值、合法 owner 与可恢复性**，而非 EU 数量；也不因此对所有局部实施强制事前设计。

对曾比较的路径，明确保留以下取舍：

- **仅写 Guide / Consumer-local 建议**不足以修复已经写入 canonical Skill 的跨 EU 硬门槛；必须同步修订相关 Skill contract。
- **单独新增 `detailed-design` Skill**尚无独立 Trigger / Procedure / Exit 的跨 Consumer 证据，容易与 `technical-plan`、`clarify-architecture` 重叠；目前通过扩展现有责任形成和回流设计知识，未来只在真实缺口证明必要时重评。
- **将所有详细设计放进系统 Architecture 或一次性 Technical Plan**会混淆跨 Feature 系统边界、局部长期契约与施工计划，制造第二个 Current owner。合法长期设计仍由 Consumer 的真实 owner 保存，具体载体不限于文档。

以上理由与当前模型一起保存在本仓库的版本化 Architecture 中，不依赖 Issue / PR 讨论才能恢复。背景讨论和审查 Evidence 可以从 Git 历史追溯，但不得作为 ordinary runtime 的必读 Authority。

## 7. Inventory 与安装

实际 `skills/*/SKILL.md` corpus 是 Skill inventory 的机器事实来源；`skills/README.md` 只是 Human View。

普通 Consumer 通过标准 Agent Skills 兼容方式安装明确版本的 Skills。安装 / 更新不得覆盖 Consumer-owned `AGENTS.md`、docs、local constraints 或其他项目文件。

## 8. 准入

新增 Skill 至少证明独立 trigger / purpose、稳定 inputs、可重复 procedure、稳定 outputs、明确 exit / escalation、有界上下文、单一语义 owner，并证明现有 Skill / Guide / Consumer-local mechanism 无法更简单地承担该责任。

“很重要”“多个地方都会用”“存在多个步骤”本身不足以新增 Skill。
