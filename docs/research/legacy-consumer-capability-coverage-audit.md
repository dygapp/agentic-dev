---
id: research:legacy-consumer-capability-coverage-audit
type: research
status: active
distribution: source-only
---

# Legacy Consumer 能力覆盖审计

**Gate：** F — Legacy Consumer Capability Coverage Audit  
**性质：** 非规范性验收 Evidence，不是新的 Distribution / Consumer canonical owner  
**Acceptance：** `DR-AC-31`、`DR-AC-32`

## 1. 审计边界

本审计严格使用 `docs/project/distribution-rebuild-specification.md` Gate F 的冻结口径：比较单位是 **legacy Consumer AI development obligation**，不是旧目录与新目录逐文件映射。

Provider / Release subject：

- `dygapp/agentic-dev@d4176b14bec9c4f14d118a791497d4cfb86b23f0`
- Release Build Run：`35692280317`
- Release：`agentic-dev@0.0.0-candidate.d4176b14bec9+d4176b14bec9`
- Release archive SHA-256：`b7f87e33f9f98c03fd607da264138a52fe9f1d27c6e0af21686823af68946f15`
- 发布 Skill：15
- software release inputs：26
- installation inputs：3

真实 Consumer subject：

- `dygapp/jilinjobs-cms@a8f96a949973f8d6592180464f5d72c52e8174be`
- `docs/work/current/README.md`：Current Ready Execution Unit = `NONE`
- Consumer mutation：0

Consumer SHA 在本 Gate 固定为只读审计 subject。Consumer 后续提交不会隐式改变本次 Gate F 结论；需要换 subject 时必须显式重做审计。

机器可读 Evidence：`evals/fixtures/legacy-consumer-coverage/gate-f.json`。确定性约束：`tools/distribution-audit/tests/test_legacy_consumer_coverage.py`。

## 2. Evidence 来源

### Consumer 当前治理

按 Consumer 自身 Local Discovery 恢复，主要当前 owner 为：

- `AGENTS.md` — Repository Governance、Authority / Knowledge Boundary、Fresh Context、Human Escalation；
- `docs/README.md` — Documentation Authority Map / Local Discovery Entry；
- `docs/project/project-capability-profile.md` — Consumer-local Method / Rule / Skill / Architecture capability instance；
- `docs/work/README.md`、`docs/work/current/README.md`、`docs/project/project-roadmap.md` — work / Roadmap ownership；
- `docs/architecture/rule-discovery.md` + `tools/rule-discovery/rule_discovery.py` — Consumer-local conditional Rule activation；
- `docs/rules/technology/vue/component-authoring.md`、`docs/rules/technology/vue/typecheck.md` — 当前技术专项 policy 样本。

Consumer 当前 evaluated upstream baseline `b71783782b97e2033b99014744d1286dd69cb107` 只用于理解 legacy capability provenance；它不是本 Gate 的 upstream runtime dependency。

### 新 Release

合并后 Release Build Run `35692280317` exact-SHA PASS，生成 artifact 的 manifest / index 实际包含 15 个 Skill：

`activate-model-collaboration`、`clarify-architecture`、`clarify-intent`、`converge`、`establish-requirement-baseline`、`execute-unit`、`external-operation`、`github-actions-verification`、`human-review`、`readiness-check`、`review-change`、`slice-work`、`specify`、`systematic-debug`、`technical-plan`。

安装支持包含：

- `installation/references/architecture--consumer.md`
- `installation/references/method--consumer-adoption.md`
- `installation/references/method--consumer-upgrade.md`
- `install.py`

Gate E 已证明 provider Source root 不可读时，Release-installed runtime 仍能完成 Codex native Skill discovery 15 / 15；因此普通运行的 upstream decoupling 不依赖目录静态推断。

## 3. Obligation 覆盖矩阵

| ID | legacy obligation | disposition | 当前覆盖 / owner |
|---|---|---|---|
| GF-01 | Repository Authority / Knowledge Boundary | `consumer-local` | `AGENTS.md`、`docs/README.md`、`docs/project/project-capability-profile.md` |
| GF-02 | Fresh Context / Bootstrap | `bootstrap-covered` | `install.py` 的 bounded `AGENTS.md` marker + `.agents/README.md` + generated skill index；不覆盖 Consumer Authority |
| GF-03 | Requirement Baseline Establishment | `release-covered` | `.agents/skills/establish-requirement-baseline/SKILL.md` |
| GF-04 | Architecture Clarification | `release-covered` | `.agents/skills/clarify-architecture/SKILL.md` |
| GF-05 | ordinary Feature / change lifecycle | `release-composed` | `clarify-intent → specify → technical-plan → slice-work → readiness-check → execute-unit → converge` |
| GF-06 | Specification | `release-covered` | `.agents/skills/specify/SKILL.md` |
| GF-07 | Technical Planning | `release-covered` | `.agents/skills/technical-plan/SKILL.md` |
| GF-08 | work slicing | `release-covered` | `.agents/skills/slice-work/SKILL.md` |
| GF-09 | readiness | `release-covered` | `.agents/skills/readiness-check/SKILL.md` |
| GF-10 | implementation | `release-covered` | `.agents/skills/execute-unit/SKILL.md` |
| GF-11 | systematic debugging | `release-covered` | `.agents/skills/systematic-debug/SKILL.md` |
| GF-12 | convergence | `release-covered` | `.agents/skills/converge/SKILL.md` |
| GF-13 | verification / evidence discipline | `release-composed` | `rule:evidence-type-must-match-claim` + `rule:verification-contract-currentness` 被组合进相应 Skill；`execute-unit` / `converge` 承担执行与整体证据闭环 |
| GF-14 | independent change review | `release-covered` | `.agents/skills/review-change/SKILL.md` |
| GF-15 | human review | `release-covered` | `.agents/skills/human-review/SKILL.md` |
| GF-16 | human escalation | `release-composed` | `rule:human-intervention-necessity` 作为 release input 进入需要人工升级的多个 Skill，不建立独立万能流程 |
| GF-17 | external operation safety | `release-covered` | `.agents/skills/external-operation/SKILL.md` + packaged `rule:safe-external-write` |
| GF-18 | GitHub Actions verification | `release-covered` | `.agents/skills/github-actions-verification/SKILL.md` |
| GF-19 | conditional policy / rule activation | `consumer-local` | Consumer `docs/architecture/rule-discovery.md` + `tools/rule-discovery/rule_discovery.py`；通用 Release 有意不安装 provider Rule tree |
| GF-20 | language / terminology governance | `consumer-local` | Consumer `AGENTS.md` + `docs/architecture/requirement-authority.md`；Release 不取得本地语言 / 业务术语 owner |
| GF-21 | technology-specific policy | `consumer-local` | `docs/rules/technology/vue/component-authoring.md`、`typecheck.md`；技术栈 policy 继续由 Consumer 拥有 |
| GF-22 | current work / Roadmap ownership | `consumer-local` | `docs/work/README.md`、`docs/work/current/README.md`、`docs/project/project-roadmap.md`；Release 明确排除 provider Current Gate / Roadmap |
| GF-23 | upstream decoupling | `release-composed` | `architecture:consumer` installation reference + Gate E provider Source unreadable negative control |
| GF-24 | adoption / upgrade / release update | `release-composed` | `method--consumer-adoption.md` + `method--consumer-upgrade.md` + `install.py` |
| GF-25 | executable capability / alternate path / fail-closed | `release-composed` | `architecture:consumer §6` + `external-operation` / `github-actions-verification` + Gate E executable negative controls |
| GF-26 | Current Evidence / exact-subject verification | `release-composed` | packaged Evidence / verification-currentness rules + Release Build / Runtime Acceptance exact-SHA contracts |

## 4. 分类判断

### `consumer-local` 不是缺口

本次 5 项 `consumer-local` 都有显式 Consumer owner，并且这些责任本来就会随项目事实、技术栈或当前工作状态变化：

1. Repository Authority / Knowledge Boundary；
2. conditional policy / rule activation；
3. language / terminology governance；
4. technology-specific policy；
5. current work / Roadmap ownership。

将这些内容重新复制进通用 Release 反而会违反当前 Consumer Architecture 的 ownership / upstream-decoupling 目标。因此这里的 `consumer-local` 是冻结规范允许的有意边界，不是 release gap。

### 生命周期由组合能力覆盖

旧 Consumer 的 `method:ai-development` 是一个本地 canonical Method；新 Release 不把 provider Method 目录作为平级 runtime namespace 投影。其普通 Feature lifecycle 通过多个有界 Skill 与 packaged release inputs 组合恢复，因此 GF-05、GF-13、GF-16、GF-23～GF-26 使用 `release-composed`，而不是要求出现旧目录同构副本。

### Bootstrap 保留 Consumer ownership

GF-02 使用 `bootstrap-covered`：安装器只在 Consumer-owned `AGENTS.md` 中维护有界 marker，并生成 `.agents/README.md`、release manifest / skill index。它不复制 Skill Procedure、provider Project state 或 provider Rule tree。

## 5. Gate F 结果

机器 Evidence 派生统计：

```text
total = 26
classified = 26
release-covered = 13
release-composed = 7
consumer-local = 5
bootstrap-covered = 1
platform-covered = 0
intentionally-retired = 0
unclassified = 0
gap = 0
consumer mutation = 0
```

因此当前审计结果满足：

- `DR-AC-31`：26 项最低 obligation 全部完成行为级分类；
- `DR-AC-32`：`unclassified=0`、`gap=0`，且全部 `consumer-local` 项具有显式 local owner；
- 未发现需要返回 Gate C / D / E 的 upstream Release gap；
- `dygapp/jilinjobs-cms` 未发生任何 mutation。

本文件只支持 Gate F 验收，不宣称 Gate G Final Specification Conformance / RC Freeze 或 Gate H real Consumer migration 已完成。
