---
id: research:distribution-model-evidence-review
type: research
status: active
distribution: source-only
---

# Source / Distribution 模型证据复核

**研究基线：** 2026-09-20  
**Issue：** #172  
**对应验收：** `DR-AC-36`

## 1. 研究目的

本文件验证 Issue #172 Gate B 的一个核心实施依据：

> `agentic-dev` 的复杂 Source / Authoring Model 是否必须以同样复杂度传播到普通软件 Consumer，还是可以保留 provider-side semantic owner，同时将 Consumer Distribution 收敛为以 Agent Skills 为主要单位的版本化发布物。

本文件是 Research Evidence，不是 Architecture / Method / Skill / Rule 的规范 Authority。最终稳定语义只有进入真实 canonical owner 后才成为 Current capability。

## 2. 当前 `agentic-dev` 为什么形成复杂 Source Model

当前复杂度不是单纯由目录习惯形成，而是多轮真实 Consumer / governance Evidence 推动的 semantic ownership 收敛结果。

### 2.1 Method

当前 Method 负责一类复杂工作的：

- 进入条件；
- 生命周期 / stage；
- Gate；
- 长期产物；
- 返回 / 回退；
- 整体完成条件。

这一边界用于避免一个 Skill 隐式拥有跨多个阶段的长期工作生命周期。

### 2.2 Skill

当前 Skill 被限定为当前责任明确后，可以独立调用、验证和退出的有界执行能力：

```text
Trigger / Purpose
→ Inputs
→ Procedure
→ Outputs
→ Exit
→ Escalation
```

这一边界用于保持 activation、上下文和行为评估有界，不应因为本次发布模型重构而机械删除。

### 2.3 Rule

当前 Rule 独立持有按任务事实条件性适用的 policy / constraint / invariant，并通过 Rule Discovery 避免全量加载。

Rule 独立于 Skill 的主要原因包括：

- policy 可能横切多个 Skill / Method / direct work；
- Consumer-local specialization 需要独立 owner；
- conditional activation 与 procedure activation 并非同一个问题；
- 真实 Consumer 已证明授权、验证、术语、技术专项规则等经常由目标 Repository Authority 决定。

### 2.4 Architecture

Architecture 当前持有长期结构、ownership、组合关系和运行不变量，避免这些语义散落在多个 Method / Skill / Rule 中形成重复 Authority。

### 2.5 Project Knowledge

Project Knowledge 进一步把 `agentic-dev` 自身使命、当前 capability instance、Roadmap 和稳定演进历史从 reusable capability 中分离，形成“Project 不传播，Capability 传播”的当前边界。

### 2.6 内部结论

因此，当前 Source Model 的复杂度至少有一部分是**有意的 authoring / governance separation**，不能为了获得简单发布目录而直接删除。

当前真正需要重新评估的是：

> 为什么这些 provider-side owner 在 Consumer adoption / upgrade 时被较大程度按同类对象重新投影到了 Consumer。

Source Model 与 Distribution Model 被过度绑定，才是本轮重构需要解决的主要问题。

## 3. Agent Skills Specification 当前能力

### 3.1 固定基线

- Repository：`agentskills/agentskills`
- exact commit：`69ef37e9424c0a7ea9dd2293b559e43ec8176379`
- Specification：https://agentskills.io/specification
- GitHub source：https://github.com/agentskills/agentskills

### 3.2 与本轮直接相关的规范能力

当前 Agent Skills Specification 明确把 Skill 定义为一个目录，只有 `SKILL.md` 是必需文件，并允许附带任意 supporting resources。规范给出的通用约定包括：

```text
skill-name/
├── SKILL.md
├── scripts/
├── references/
└── assets/
```

其中：

- `scripts/`：确定性 / 重复性执行代码；
- `references/`：按需加载的详细资料；
- `assets/`：模板、静态资源等；
- `metadata`：允许客户端 / 发布者加入额外 string metadata；
- `compatibility`：可以说明环境 / Runtime 要求；
- Progressive Disclosure：metadata → `SKILL.md` → supporting resources。

规范还建议 `SKILL.md` 保持有界，并把较长参考内容移动到 references。

### 3.3 推论边界

该规范支持：

> 一个 Skill package 可以比“单一短 Prompt”复杂很多。

因此，Method / Rule / Tool / reference 中的部分 Consumer runtime semantics **可以在发布阶段经过 transformation 后由 Skill package 承载**，并不要求 Consumer 必须重新建立与 provider Source 相同的平级 namespace。

但规范并不证明：

- 所有 Source owner 都应该被删除；
- 所有能力都应该合并成一个 Skill；
- 不同 Runtime 对 repository-local Skill 的发现路径完全相同；
- Consumer-local policy 应被上游 Skill 吸收。

因此本轮应采用“Skill 是主要 Distribution Unit”，而不是“Skill 是唯一 Source semantic owner”。

## 4. OpenAI Codex repository-local Skills

### 4.1 来源

- 官方文档：https://developers.openai.com/docs/build-skills
- 复核日期：2026-09-20

### 4.2 直接证据

当前 OpenAI 文档明确支持 repository-local：

```text
.agents/skills/<skill>/
```

并使用与 Agent Skills 一致的渐进式披露：

1. 先加载 `name` / `description`；
2. Skill 命中后加载 `SKILL.md`；
3. references / scripts 等只在需要时读取 / 执行。

### 4.3 对本轮的意义

这支持把：

```text
.agents/skills/**
```

作为首版普通软件 Consumer 的 Codex repository-local deployment target。

但这只是一个 Runtime deployment target，不应反向成为 `agentic-dev` Source Architecture 的固定物理目录。

## 5. Anthropic Skills：Source Repository 与 Distribution Bundle 分离

### 5.1 固定基线

- Repository：`anthropics/skills`
- exact commit：`34040c9c568585f6929bedeaad110ad08f079624`
- Source：https://github.com/anthropics/skills

### 5.2 Source Repository 实际结构

该仓库当前并不只有 `skills/**`。根目录同时存在：

- `.claude-plugin/**`；
- `spec/**`；
- `template/**`；
- Repository README / notices；
- `skills/**`。

这说明成熟 Skills 项目本身仍然可以拥有：

- specification source；
- template；
- distribution metadata；
- repository documentation；
- Skill authoring / development support。

### 5.3 Distribution 实际结构

当前 `.claude-plugin/marketplace.json` 并不把整个 Repository 当作 Consumer runtime package，而是定义多个 plugin bundle，并显式列出要发布的 `./skills/<name>`。

例如 document bundle 只选择：

- `skills/xlsx`
- `skills/docx`
- `skills/pptx`
- `skills/pdf`

example bundle 也只选择一组 Skill。

### 5.4 结论

Anthropic 样本直接证明：

> **Source Repository 可以包含远多于最终 Distribution 的资产；发布层可以显式选择和组合 Skills，而不是复制整个 source tree。**

这与 Issue #172 的 Source / Distribution 分离方向一致。

## 6. Matt Pocock Skills：复杂 Source + Skills 安装 + bounded setup

### 6.1 固定基线

- Repository：`mattpocock/skills`
- exact commit：`c55ee46073ed923f86ce59a5eb3b6d895095d1b7`
- Source：https://github.com/mattpocock/skills

### 6.2 Source Repository 实际结构

当前根目录包含：

- `.agents/**`；
- `.changeset/**`；
- `.claude-plugin/**`；
- `.github/**`；
- `docs/**`；
- `scripts/**`；
- `skills/**`；
- `AGENTS.md` / `CLAUDE.md` / `CONTEXT.md`；
- package / release metadata。

因此“成熟项目只提供 Skills”不能理解成“源码仓库只有 `SKILL.md`”。

### 6.3 Distribution 实际行为

README 当前提供两类主要安装方式：

1. Claude Code plugin：以 managed bundle 安装；
2. `npx skills@latest add mattpocock/skills`：选择需要的 Skills 并复制到目标 Agent 的 Skill location。

Consumer 并不因此克隆 / 投影整个 upstream Source Repository。

### 6.4 setup Skill 的启示

`setup-matt-pocock-skills` 会读取 Consumer 当前状态，并建立其他 Skills 依赖的少量 Repository-local configuration。

其当前行为具有几个重要特点：

- 先检查已有 `AGENTS.md` / `CLAUDE.md`；
- 不假设 Consumer 是空仓库；
- 在已有 bootstrap 中增加有界 `Agent skills` 区块，而不是把 upstream bootstrap 整文件覆盖过去；
- 把 issue tracker / triage / domain-doc 等 Consumer-specific 决定写到 Consumer 自己的 local docs；
- 明确要求不要覆盖用户对周边内容的修改。

### 6.5 结论

该样本进一步支持：

> **通用能力可以通过 Skills 发布，同时只把必要的 Consumer-specific configuration 留在目标 Repository；发布者的完整 Source Model 不需要进入 Consumer。**

它也支持 Issue #172 已冻结的 Consumer-owned `AGENTS.md` + bounded bootstrap integration 原则。

本轮不因此自动新增 setup Skill。是否 Skill 化仍按 Issue #172 的暂缓边界后续单独判断。

## 7. 三类模型对比

| 维度 | 当前 `agentic-dev` | 成熟 Skills 样本 | Issue #172 目标 |
|---|---|---|---|
| Source repo | Method / Architecture / Rule / Skill / Tool / Eval / Research / Guide | Skills + docs / scripts / spec / template / plugin / release assets | 允许复杂 authoring source |
| Distribution | 当前通过 adoption / upgrade 逐类投影 capability | 选择 Skill / bundle 安装 | 以版本化 Skill release 为主要单元 |
| Consumer bootstrap | 建立 local selector / Rule Discovery / Skill entry 等较复杂 runtime instance | bounded setup / native Skill discovery | Consumer-owned `AGENTS.md` + thin Skill entry |
| Consumer docs | 当前可能承载大量 AI development meta docs | 主要保留项目自身 docs + 少量 skill config | 恢复为业务 / 产品 / 系统 / 技术 / 项目知识 |
| Upstream dependency | adoption 后 runtime 已要求 0，但 upgrade 仍理解 source capability delta | installer / plugin 主要面向发布包 | install / upgrade 都面向 versioned release |
| Progressive disclosure | Skill + Rule Discovery 两套机制 | Skill metadata → body → resources | Release 主要依赖 Skill progressive disclosure，Consumer-local policy 保留本地 owner |

## 8. Gate B 结论

当前 Evidence 支持 Issue #172 已冻结方向，不需要修改 Gate A Acceptance。

### 8.1 应继续保留的 Source 原则

- Single Semantic Ownership；
- Method 对复杂过程生命周期的 owner 边界；
- bounded Skill activation；
- Consumer-local policy specialization；
- Architecture 对长期结构 / ownership 的职责；
- Project Knowledge 不传播；
- Evidence-driven evolution。

### 8.2 应改变的 Distribution 原则

停止默认：

```text
Method → Consumer Method
Architecture → Consumer Architecture
Rule → Consumer Rule
Tool → Consumer Tool
```

改为：

```text
source semantic owner
→ distribution classification
→ release transformation / packaging
→ versioned Skill release
→ bounded Consumer-local integration
```

### 8.3 Gate C / D 必须继续验证的风险

- 不得把全部 lifecycle 合并成一个超级 Skill；
- 不得把 Consumer-specific Rule 静默编译进通用 Skill；
- 不得因为发布模型简化而删除仍有真实 authoring value 的 Source owner；
- 不得假设 ChatGPT + GitHub Connector 与 Codex 具有相同 native Skill discovery；
- 不得把 generated release manifest 变成新的手工 Runtime Catalog；
- 不得让 install / upgrade 重新依赖 upstream Source tree。

## 9. DR-AC-36 结论

`DR-AC-36` 要求的 Evidence Review 已覆盖：

- 当前仓库复杂模型的演进原因；
- 当前 Agent Skills Specification；
- OpenAI repository-local Skill deployment；
- Anthropic Skills；
- Matt Pocock Skills。

当前结论：

**PASS（Evidence Review scope）**。

该 PASS 只支持 Gate B 继续进行 Repository-wide Distribution Classification；不证明 `DR-AC-09`～`DR-AC-11` 已完成，也不提前证明 Gate C / D 的最终 Source / Distribution implementation 正确。
