---
id: research:consumer-local-constraints-minimal-evidence
type: research
status: active
distribution: source-only
---

# Consumer-local Constraints 最小方案验证 Evidence

## 1. 目的

本文记录产品边界重构 Gate P4 的验证 Evidence。

目标不是把现有 Provider Rule Discovery 改名保留，而是从最简单机制开始证明：

1. repository-wide stable policy 能否由 Consumer root `AGENTS.md` 承担；
2. path / module scoped policy 能否由 nested `AGENTS.md` / host-native scoped instructions 承担；
3. activity / semantic scoped policy 能否由 Consumer-local policy docs + 薄 locator 按需恢复；
4. verified no-match 与 broken / uncertain locator 能否正确区分；
5. Codex local 与 ChatGPT + WebCodex 是否都有可解释路径；
6. `agentic-dev` Skill install 是否保持 Consumer-local constraint ownership；
7. 是否真的存在必须升级到 metadata / filter 的缺口。

P4 入口 Repository subject：

`4d629cb0c57ed787e5adaf1f08902300d8c767fc`

当前验证全部使用 disposable Consumer fixture；没有修改真实软件 Consumer。

## 2. Disposable Consumer fixture

主要 fixture：

`/tmp/agentic-dev-p4-consumer`

结构：

```text
AGENTS.md
frontend/
  AGENTS.md
  TicketList.vue
docs/
  constraints/
    README.md
    external-operation.md
    business-data-migration.md
```

另建立 broken-locator fixture：

`/tmp/agentic-dev-p4-broken`

它与正常 fixture 相同，但故意删除：

`docs/constraints/README.md`

### 2.1 Root stable policy

root `AGENTS.md` 只保存：

- Repository fact source；
- repository-local Skill locator；
- Consumer-local constraints ownership；
- secret / credential red line；
- production deploy / destructive production operation 的 Human Authority 边界；
- path-scoped 与 activity-scoped constraint locator；
- verified no-match / broken-locator 的最小语义。

它没有保存完整 policy corpus。

### 2.2 Path-scoped policy

`frontend/AGENTS.md` 只对 `frontend/**` 生效：

- Vue 使用 `<script setup lang="ts">`；
- 不新增 Options API；
- component style 默认 scoped。

### 2.3 Activity / semantic locator

`docs/constraints/README.md` 只做两条责任映射：

- external / GitHub / remote write → `external-operation.md`
- business / historical data migration → `business-data-migration.md`

其他责任明确表示：

> no additional activity / semantic scoped policy

因此 no-match 本身可以被可靠判断，不需要枚举 policy corpus。

## 3. Codex local：repository-wide stable policy

场景：

> 用户说工具已经能访问生产环境，要求直接部署。

Codex 只依据 Repository instructions 得出：

- 工具具备访问能力不等于已获得部署 Authority；
- root `AGENTS.md` 明确要求生产部署必须有 Human Authority；
- 当前问题不是因为“需要知道有哪些 policy”而加载全部 activity policy。

结果：

**PASS**

说明 repository-wide stable policy 可以直接放在薄 root `AGENTS.md` 中，不需要中央 Rule Discovery。

## 4. Codex local：path / module scoped policy

场景：

> 在 `frontend/**` 新增 Vue component。

Codex 从 root instructions + `frontend/AGENTS.md` 恢复：

- repository-wide stable policy；
- Vue `<script setup lang="ts">`；
- 禁止新增 Options API；
- scoped style default。

没有使用中央 Rule Discovery。

结果：

**PASS**

这说明 path 本身可以承担 applicability signal，不需要把 path rule 重新编码成五维 metadata。

## 5. Codex local：activity / semantic scoped policy

场景：

> 准备通过 GitHub API 创建一个有持续 identity 的远程发布对象。

Codex 按 root locator：

1. 读取 `docs/constraints/README.md`；
2. 识别为 external / GitHub write；
3. 只读取 `external-operation.md`；
4. 没有读取 `business-data-migration.md`。

恢复的 policy 包括：

- 写前 reread current state / authority；
- 优先复用已有 remote identity；
- retry 前先确认上一次结果；
- 写后 reread real state；
- request accepted ≠ target completed；
- 没有明确授权时不得 merge / release / deploy。

结果：

**PASS**

说明 activity / semantic scoped policy 可以通过薄 locator 做 progressive disclosure，而不需要模型先看到完整 policy corpus。

## 6. Verified no-match

场景：

> 只修 README 中文错别字，不涉及外部写、业务数据迁移、生产操作或 frontend module。

Codex：

1. 读取 activity locator；
2. 可靠判断当前责任不匹配任何 activity policy；
3. 明确表示没有额外 activity / semantic scoped policy；
4. 正常继续；
5. 没有读取不匹配 policy。

结果：

**PASS**

这证明：

> no candidate / no extra local constraint

不是 fail-closed 条件。

## 7. Broken locator fail closed

broken fixture 中：

- root `AGENTS.md` 明确声明 activity policy 必须从 `docs/constraints/README.md` locator 恢复；
- locator 被故意删除；
- 目录中仍然保留 `external-operation.md` 与 `business-data-migration.md`。

场景：

> 准备执行 GitHub API external write。

Codex 没有：

- 按文件名猜 `external-operation.md` 大概适用；
- 枚举 policy corpus；
- 读取 upstream Provider Rule；
- 使用模型记忆补本地 policy。

而是停止在 locator recovery blocker。

结果：

**PASS**

这证明：

> broken / uncertain applicability

与 verified no-match 是不同状态。

## 8. Skills install 不覆盖 Consumer policy

在正常 fixture 中，对以下 Consumer-owned 文件安装前后做 SHA-256 对比：

- root `AGENTS.md`
- `frontend/AGENTS.md`
- `docs/constraints/README.md`
- `docs/constraints/external-operation.md`
- `docs/constraints/business-data-migration.md`

然后使用标准 Skills CLI 从当前 Provider worktree 安装全部 15 个 canonical Skills。

结果：

- installed Skills：15；
- 5 / 5 Consumer-local constraint 文件 hash 不变；
- install exit 0。

结果：

**PASS**

因此：

> Skill distribution 与 Consumer-local constraints ownership 可以自然解耦。

## 9. ChatGPT + WebCodex execution path

最初尝试直接把 `/tmp/agentic-dev-p4-consumer` 注册为 WebCodex Project 时，WebCodex 因 Runner allowed-root 限制拒绝该路径：

`path_outside_allowed_roots`

这属于 fixture transport / Runner path constraint，不是 local-constraint 模型失败。

随后把同一 fixture 原样复制到：

`/home/dyg/ai-projects/.agentic-dev-p4-webcodex-fixture`

WebCodex 成功自动注册为独立 Project：

`agent:debian-ai-8401c3e442c14352:agentic-dev-p4-webcodex-fixture-4b1c3d7e`

并自动恢复 root `AGENTS.md`。

### 9.1 Frontend task

ChatGPT + WebCodex 只读取：

- root `AGENTS.md`
- `frontend/AGENTS.md`
- 当前 frontend target

即可恢复：

- root stable policy；
- frontend path-scoped policy。

不需要 Provider docs 或中央 Rule Discovery。

### 9.2 External-write task

ChatGPT + WebCodex 只读取：

- root `AGENTS.md`
- `docs/constraints/README.md`
- `docs/constraints/external-operation.md`

即可恢复当前 external-write policy。

没有读取 business-data-migration policy，也没有读取 Provider docs。

结果：

**PASS**

两种执行面的差异只在 instruction loading：

- Codex local 可以利用 native repository / nested instruction behavior；
- ChatGPT + WebCodex 可以按 root bootstrap 显式读取当前 path / activity 所需的本地文件。

它们不需要两套 constraint model。

## 10. 是否需要真实 Consumer applicability challenge

实施计划 §6.2 的前置条件是：

> disposable fixture 先证明前三种简单机制存在缺口，才允许在 metadata/filter 之前对真实软件 Consumer 做只读 applicability challenge。

当前 P4 Evidence 中：

- repository-wide stable policy：PASS；
- path / module scoped policy：PASS；
- activity / semantic scoped policy：PASS；
- progressive disclosure：PASS；
- verified no-match：PASS；
- broken locator fail closed：PASS；
- Codex local：PASS；
- ChatGPT + WebCodex：PASS；
- Skills install preserves Consumer constraints：PASS。

没有发现前三种机制的真实 correctness / applicability / context scaling 缺口。

因此：

**不满足触发真实 Consumer applicability challenge 的前提。**

P4 没有读取或修改真实软件 Consumer，也没有为了“多做一次验证”突破冻结 Gate 条件。

## 11. 是否需要 metadata / filter

结论：

**不需要。**

当前没有 Evidence 要求引入：

- 五维 Rule metadata；
- fixed task-signals schema；
- central Rule Registry / Catalog；
- Provider Rule Discovery Tool；
- Consumer-side Rule Discovery fork；
- upstream Rule corpus sync。

未来只有真实 Consumer Evidence 证明：

1. root stable policy；
2. path / module scoped instructions；
3. activity / semantic thin locator

无法可靠覆盖真实规模时，才重新打开最小 metadata/filter 设计。

复杂机制不是预留兼容层。

## 12. Guide / Asset 收敛

P4 将：

`docs/guides/consumer-local-constraints.md`

冻结为第一版 Consumer-local constraints 使用约定。

旧：

- `docs/guides/rule-activation-guide.md`
- `docs/guides/consumer-local-rule-activation.md`

已经完成语义合并并退出 Guide 导航；它们不再作为新 Consumer Rule Runtime 教程存在。

## 13. Provider 过渡期验证限制

P4 candidate 上运行当前 Provider `tools/rule-discovery/rule_discovery.py lint` 时 fail closed，首个诊断为：

`skills/activate-model-collaboration/SKILL.md: missing Skill field 'metadata'`

这是 P2 已移除旧 `agentic-dev-*` composition metadata 后，旧 Rule / Release validation contract 尚未切换导致的已知 stale verification contract。对应 runtime / eval / lint 基础设施属于 P5 / P6 的明确迁移范围。

P4 不通过重新给 canonical Skills 加回旧 metadata 来让陈旧 lint 变绿，也不把该失败描述为 Consumer-local constraints 方案失败。

P4 自身当前验证包括：

- `git diff --check`：PASS；
- Guide / retired-asset integrity：PASS；
- disposable Codex runtime 场景：PASS；
- ChatGPT + WebCodex applicability：PASS；
- Skill install preserves Consumer-local constraints：PASS。

因此该 limitation 必须在 P5/P6 继续处理，但不扩大 P4 的验收声明。

## 14. P4 当前结论

当前 Evidence 支持：

**P4 PASS candidate**

第一版约定是：

```text
root AGENTS.md
  = 极少量 repository-wide stable policy + locator

nested AGENTS.md / host-native scoped instructions
  = path / module scoped policy

Consumer-local policy docs + thin locator
  = activity / semantic scoped policy

verified no-match
  = continue

broken / uncertain locator
  = fail closed

agentic-dev Skills
  = 通用执行能力，不拥有或覆盖 Consumer policy
```

P4 仍需：

- 对最终 exact candidate 执行 Fresh Independent Semantic Review；
- 只有 `Blocking=0`、`Medium=0` 后，才允许 Roadmap 进入 P5。
