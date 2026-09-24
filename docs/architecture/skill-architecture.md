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

## 4. 责任边界

- Guide 负责方法理解、Bootstrap 和“下一步做什么”的导航；
- Skill 负责可执行 procedure；
- Consumer Repository 负责当前项目事实与项目级约束；
- `docs/governance/**` 只治理 `agentic-dev` Provider，不进入 Consumer package。

## 5. Inventory 与安装

实际 `skills/*/SKILL.md` corpus 是 Skill inventory 的机器事实来源；`skills/README.md` 只是 Human View。

普通 Consumer 通过标准 Agent Skills 兼容方式安装明确版本的 Skills。安装 / 更新不得覆盖 Consumer-owned `AGENTS.md`、docs、local constraints 或其他项目文件。

## 6. 准入

新增 Skill 至少证明独立 trigger / purpose、稳定 inputs、可重复 procedure、稳定 outputs、明确 exit / escalation、有界上下文、单一语义 owner，并证明现有 Skill / Guide / Consumer-local mechanism 无法更简单地承担该责任。

“很重要”“多个地方都会用”“存在多个步骤”本身不足以新增 Skill。
