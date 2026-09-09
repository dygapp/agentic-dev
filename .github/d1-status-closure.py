from pathlib import Path


def replace_once(path: str, old: str, new: str) -> None:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{path}: expected exactly one match, got {count}\nOLD:\n{old}")
    p.write_text(text.replace(old, new, 1), encoding="utf-8")


# AGENTS: move current gate from D1 to E1 and expose the durable activation entry.
replace_once(
    "AGENTS.md",
    """当前下一实际门禁：\n\n> **阶段 D — 权威 / 指南收敛 / D1 — 基于证据实施指南 / 权威收敛**\n\n本里程碑解决巨型指南、规则重复、粗粒度加载和“规则存在但没有在恰当任务中可靠激活”的问题。阶段 C 已证明“薄入口 + 条件检索 + 当前源指针 + 保守安全回退”在本轮冻结高影响规则面上优于文件级粗粒度加载；当前进入 D1，只实施证据直接支持的收敛。fallback 成本较高不能作为删除 stale / unknown / no-match 安全回退的理由。\n""",
    """阶段 D“权威 / 指南收敛”已经完成 D1 / D2：README 已收敛为薄启动入口，新增长期 `docs/guides/rule-activation-guide.md` 只保留三条跨任务不变量、按职责 / 风险指向当前 Guide / Skill 的稳定段落指针和保守安全回退；没有复制详细规则正文、没有把评估索引提升为权威，也没有引入新的 Wiki / 数据库 / MCP / 统一元数据层。D2 重新验证 9 个既有 A/B 场景仍可静态装配，且本轮没有修改既有治理评估的输入权威。\n\n当前下一实际门禁：\n\n> **阶段 E — 使用方验证 / E1 — 使用方新上下文验证**\n\nE1 必须在真实使用方的新上下文中验证薄入口能否取得当前任务所需最小规则集，同时保持使用方仓库权威优先、关键规则不漏失和安全回退；在 E1 取得证据前，不继续删除源规则正文或扩张检索基础设施。\n""",
)
replace_once(
    "AGENTS.md",
    "- `docs/project/rule-governance-knowledge-activation-v1.md`\n",
    "- `docs/project/rule-governance-knowledge-activation-v1.md`\n- `docs/guides/rule-activation-guide.md`\n",
)

# Roadmap: keep current milestone active, but move its actual gate to E1.
replace_once(
    "docs/project/project-roadmap.md",
    """当前下一实际门禁：\n\n> **阶段 D — 权威 / 指南收敛 / D1 — 基于证据实施指南 / 权威收敛**\n\n本里程碑优先解决巨型指南、规则重复、粗粒度加载和“规则存在但未在正确任务中激活”的问题。完整研究和实施边界分别位于：\n""",
    """阶段 D“权威 / 指南收敛”已完成 D1 / D2：README 已压薄为启动 / 路由入口；新增 `docs/guides/rule-activation-guide.md`，只维护三条跨任务不变量、按职责 / 风险的当前源段落指针和 fail-closed 回退；详细规则仍由现行 Guide / Skill / Repository Authority 单点维护。D2 重新验证 9 个既有 A/B 场景仍可静态装配；本轮未修改现有四组治理评估的输入权威，因此不重复执行没有输入变化的历史语义评估。\n\n当前下一实际门禁：\n\n> **阶段 E — 使用方验证 / E1 — 使用方新上下文验证**\n\nE1 需要在真实使用方的新上下文中验证薄激活入口的实际采用效果。完整研究和实施边界分别位于：\n""",
)
replace_once(
    "docs/project/project-roadmap.md",
    "- `docs/project/rule-governance-knowledge-activation-v1.md`\n",
    "- `docs/project/rule-governance-knowledge-activation-v1.md`\n- `docs/guides/rule-activation-guide.md`\n",
)
replace_once(
    "docs/project/project-roadmap.md",
    "| 规则治理与知识激活 | **当前有限里程碑** | Issue #73；阶段 A、B、C 已完成，当前进入阶段 D / D1；只实施评估证明有价值的收敛并保留安全回退 |",
    "| 规则治理与知识激活 | **当前有限里程碑** | Issue #73；阶段 A～D 已完成，当前进入阶段 E / E1 使用方新上下文验证；保持薄入口、当前源指针与安全回退，不提前扩张检索基础设施 |",
)

# Milestone project record: D complete, E current.
replace_once(
    "docs/project/rule-governance-knowledge-activation-v1.md",
    "**当前活动有限里程碑 / 阶段 D — 权威 / 指南收敛**",
    "**当前活动有限里程碑 / 阶段 E — 使用方验证**",
)
replace_once(
    "docs/project/rule-governance-knowledge-activation-v1.md",
    "- `docs/guides/using-agentic-dev.md`；\n- `docs/guides/external-operation-guidelines.md`；\n",
    "- `docs/guides/rule-activation-guide.md`；\n- `docs/guides/using-agentic-dev.md`；\n- `docs/guides/external-operation-guidelines.md`；\n",
)
replace_once(
    "docs/project/rule-governance-knowledge-activation-v1.md",
    "### 阶段 C — 检索 / 激活评估\n\n状态：**当前**。",
    "### 阶段 C — 检索 / 激活评估\n\n状态：**已完成**。",
)
old_d = """### 阶段 D — 权威 / 指南收敛\n\n状态：**当前**。\n\n阶段 C 已证明收益；当前从 D1 开始，只实施证据直接支持的长期结构收敛。\n\n可能动作包括：\n\n- 缩减常驻 AGENTS 内容；\n- 为指南建立稳定段落指针；\n- 拆分真正独立的激活单元；\n- 合并重复规则；\n- 删除陈旧 / 已被取代的规则；\n- 修正技能激活指针；\n- 建立最小规则元数据 / 索引；\n- 明确规则删除 / 取代生命周期。\n\n不能预先承诺必须执行所有动作。\n\n### 阶段 E — 使用方验证\n\n至少选择一个真实使用方做新上下文验证。\n"""
new_d = """### 阶段 D — 权威 / 指南收敛\n\n状态：**已完成**。\n\nD1 只实施阶段 C 直接支持的最小长期收敛：\n\n- README 从综合状态 / 规则摘要入口收敛为薄 Bootstrap，并把详细当前路线继续单点指向 Project Roadmap；\n- 新增 `docs/guides/rule-activation-guide.md`，只保留使用方仓库权威优先、渐进式披露、证据先于完成声明三条跨任务不变量，以及按职责 / 风险定位当前 Guide / Skill 的稳定段落指针；\n- 段落无法精确定位、导航无命中、范围冲突或高影响授权不明确时 fail-closed 回退当前 Repository Authority；\n- 详细规则正文继续由现行 Guide / Skill 单点维护；本轮没有删除阶段 A 标记的源规则，也没有修改 B/C 派生索引的 8 个规范性来源；\n- 没有引入第二 Wiki 权威、全仓库统一元数据、BM25 / vector / graph、MCP knowledge server 或新的知识型 Skill。\n\nD2 回归结论：\n\n- GitHub Actions Run `34320938617` 在 Head `bfa76f95e2dcb8de39bd2a98ab1819f71e710abc` 上成功；Python 编译检查、`evals/run_rule_retrieval_ab.py --validate-only`、最终 Bootstrap / 指针 / 回退静态断言全部通过；\n- 9 个既有 A/B 场景仍可装配，B 查询与 C1 冻结命中 / 回退保持一致；\n- 现有四组治理评估均不读取 README 或新规则导航，本轮也未修改其 `context_paths` 指向的输入权威，因此历史治理语义证据可按精确影响分析继续复用；\n- 新入口不要求读取完整历史，也没有改变正式工程概念身份或中文表达规则。\n\n阶段 D 没有证据要求机械执行原候选动作清单中的所有结构变化；源规则删除 / 合并、更多元数据或长期检索运行时继续等待真实使用方证据。\n\n### 阶段 E — 使用方验证\n\n状态：**当前**。\n\n当前下一实际门禁：\n\n> **E1 — 使用方新上下文验证**\n\n至少选择一个真实使用方做新上下文验证。\n"""
replace_once("docs/project/rule-governance-knowledge-activation-v1.md", old_d, new_d)

# Coordination plan: D1/D2 done, E1 current; add the durable activation guide to recovery inputs.
replace_once(
    "tasks/plans/20260908/01-rule-governance-knowledge-activation.md",
    "17. `docs/guides/using-agentic-dev.md`；\n18. `docs/guides/external-operation-guidelines.md`；\n19. 按当前工作需要读取 `skill-architecture.md`、`skill-contracts.md`、工程纪律、历史治理评估与使用方证据；\n20. 开放 PR / Issue 和当前 `master`，确认没有晚于本计划的人工路线决定或集成事实。",
    "17. `docs/guides/rule-activation-guide.md`；\n18. `docs/guides/using-agentic-dev.md`；\n19. `docs/guides/external-operation-guidelines.md`；\n20. 按当前工作需要读取 `skill-architecture.md`、`skill-contracts.md`、工程纪律、历史治理评估与使用方证据；\n21. 开放 PR / Issue 和当前 `master`，确认没有晚于本计划的人工路线决定或集成事实。",
)
replace_once(
    "tasks/plans/20260908/01-rule-governance-knowledge-activation.md",
    "> **阶段 D — 权威 / 指南收敛 / D1 — 基于证据实施指南 / 权威收敛**",
    "> **阶段 E — 使用方验证 / E1 — 使用方新上下文验证**",
)
old_plan = """### D1 — 基于证据实施指南 / 权威收敛\n\n只实施阶段 C 证明有价值的动作，例如：\n\n- [ ] 缩减常驻内容；\n- [ ] 增加段落级指针；\n- [ ] 拆出真正独立激活单元；\n- [ ] 合并重复规则；\n- [ ] 删除陈旧 / 已取代规则；\n- [ ] 修正技能激活指针；\n- [ ] 固化最小规则元数据 / 派生索引；\n- [ ] 定义规则删除 / 取代生命周期。\n\n禁止无证据全量重构。\n\n### D2 — 回归\n\n- [ ] 原有治理评估不回退；\n- [ ] 新检索评估继续通过；\n- [ ] 新上下文不需要读取整个历史；\n- [ ] 当前正式术语与中文规则不回退。\n"""
new_plan = """### D1 — 基于证据实施指南 / 权威收敛\n\n状态：**已完成**。\n\n本轮只实施阶段 C 直接证明有价值的动作：\n\n- [x] 缩减常驻 / 启动内容：README 收敛为薄 Bootstrap，不再复制阶段流水、完整研究清单、原则和 Skill 清单；\n- [x] 增加稳定段落级指针：新增 `docs/guides/rule-activation-guide.md`，按职责 / 风险路由到当前 Guide / Skill；\n- [x] 保持安全回退：段落无法精确定位、无命中、范围冲突或高影响边界不明确时回退当前 Repository Authority。\n\n以下原候选动作本轮**不实施且不构成未完成门禁**：拆分更多文件、删除 / 合并源规则、修改 Skill 规则语义、扩大规则元数据 / 派生索引、建立新的删除 / 取代运行机制。阶段 C 没有直接证明这些动作是 D1 的必要条件。\n\n禁止无证据全量重构。\n\n### D2 — 回归\n\n状态：**已完成**。\n\n- [x] 原有治理评估不回退：四组治理评估均不读取 README / 新导航，本轮未修改其输入权威，按精确影响分析复用已有语义证据；\n- [x] 新检索评估继续通过：Run `34320938617` 上 9 个场景 A/B 静态装配通过，B 查询与 C1 冻结命中 / 回退一致；\n- [x] 新上下文不需要读取整个历史：README 与规则导航只要求薄入口 + 当前任务最小来源；\n- [x] 当前正式术语与中文规则不回退：本轮未修改术语 / 方法对象定义，新增面向人工内容继续使用当前自然中文规则。\n"""
replace_once("tasks/plans/20260908/01-rule-governance-knowledge-activation.md", old_plan, new_plan)

# README current gate should match the proposed integrated route.
replace_once(
    "README.md",
    "- **当前下一实际门禁：** 阶段 D — 权威 / 指南收敛 / D1 — 基于证据实施指南 / 权威收敛",
    "- **当前下一实际门禁：** 阶段 E — 使用方验证 / E1 — 使用方新上下文验证",
)

print("D1/D2 proposed integration state closed; next gate E1")
