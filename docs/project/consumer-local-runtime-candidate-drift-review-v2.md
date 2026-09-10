# Consumer-local Runtime Candidate Drift 复核 v2

## 状态

**Phase G Current Evidence Gate — 需要定向 Consumer 重验**

Phase F 已在 `agentic-dev@ec945368678715732fe729c331bd3bcdd919bbdd` 上通过真实 Consumer R1～R5。Phase G Final AI Review 随后发现并修复两个 Medium：

1. `consumer-local-rule-activation.md` 的冲突措辞可能让 ordinary runtime 误读为需要当前 upstream；
2. `using-agentic-dev.md` 仍重复维护核心 Skill-owned 过程语义，违反单点 semantic owner。

第二项修复同时把跨职责 verification rules 归位到独立 Guide owner，并更新薄导航。因此最终 reusable Candidate 已晚于 Phase F 冻结 baseline，旧 Phase F PASS 不能不经影响判断直接声称覆盖最终 Candidate。

## 1. 冻结 reusable candidate

本轮定向重验冻结：

`agentic-dev@29f88efd25232e57ccb4a82ffff039be047e4d1e`

在定向 Consumer Evidence 返回前，不再修改 reusable Guide / Skill / Method / Architecture 内容；如定向重验暴露新的 Blocking / Medium，解除冻结并返回相应 owner 修订。

后续为了记录验证结果、Phase G 状态、PR / Issue 收敛而产生的 `docs/project/*` / README / task 状态提交，不改变本次 Consumer reusable baseline。

## 2. 相对 Phase F baseline 的实际 drift

比较：

```text
ec945368678715732fe729c331bd3bcdd919bbdd
→
29f88efd25232e57ccb4a82ffff039be047e4d1e
```

共 9 个提交。

### 2.1 project-only / evidence state

以下变化不进入 Consumer reusable runtime：

- `README.md`
- `docs/project/consumer-local-runtime-validation-result-v2.md`
- `docs/project/project-roadmap.md`
- `docs/project/rule-governance-knowledge-activation-v2.md`
- `tasks/plans/20260910/01-rule-governance-knowledge-activation-v2.md`

它们只记录 `agentic-dev` Phase F / G 状态与证据，不要求 Consumer adoption，也不影响 ordinary Consumer routing。

### 2.2 reusable changes

#### `docs/guides/consumer-local-rule-activation.md`

`+1 / -1`。把冲突边界从可能暗示“当前 upstream 高层规则参与 ordinary runtime”收紧为：

- Consumer Repository Authority first；
- adopted reusable semantics 使用 Consumer 当前本地化、明确采用的版本；
- upstream latest 不自动参与 ordinary runtime；
- 只有显式 baseline upgrade、local capability 缺失或 Consumer Authority 要求时重新进入 upstream。

影响 R1 / R3 / R4 的 local-only 与 override claim。

#### `docs/guides/rule-activation-guide.md`

薄导航更新，移除 `using-agentic-dev.md` 旧 §5.x pointer，并指向新的 semantic owners。

它主要影响 upstream adoption / discovery 导航，不应成为 adoption 完成后的 ordinary runtime 依赖；影响 R4 adoption 输入边界。

#### `docs/guides/using-agentic-dev.md`

`+181 / -489`。这是实质性职责去重：

- 核心职责完整过程归回 8 个 Skill owner；
- Engineering Discipline 归回 `engineering-disciplines.md`；
- external-operation / GitHub Actions 归回各自 owner；
- Guide 只保留 bootstrap、adoption、routing pointers、Roadmap lifecycle、Fresh Context 与 experiment boundary。

虽然目标是语义保持与 context reduction，但变化规模和 owner 关系足以影响 R4 baseline adoption，不能只凭静态推断复用旧 R4 Evidence。

#### `docs/guides/verification-evidence-rules.md`

新增跨职责验证证据 Guide owner，承载：

- verification contract currentness；
- visual evidence；
- Human Review baseline isolation；
- database migration completion evidence；
- evidence claim reuse across commits；
- evidence type must match claim。

平台细节继续指向 `github-actions-verification` / external-operation owners。

该文件不是所有 Consumer 必装模块。R4 必须按当前 Consumer Authority 对其做 adopt / retain-or-override / reject-not-applicable 判断，而不是因为它是新 reusable Guide 就自动 vendor。

## 3. Evidence Claim 影响映射

| Phase F Claim | Drift 影响 | 处理 |
|---|---|---|
| R1 Ordinary Fresh Context local-only | `consumer-local-rule-activation` local-only wording直接相关 | 定向重验 |
| R2 Stage Return / ambiguity / routing-only | routing contract / Consumer local runtime assets未改变；Guide 改动没有改变已验证 Stage Return semantics | 复用旧 Evidence，静态回归 |
| R3 Consumer-specific override | local conflict wording直接相关 | 定向重验 |
| R4 Baseline upgrade lifecycle | `using-agentic-dev` 大幅去重 + 新 verification Guide + navigation变化 | 必须定向重验 |
| R5 stale / Catalog rebuild | stale / rebuild mechanism 未改变 | 复用旧机制 Evidence；对更新后的 adopted source identity 补 source-currentness 检查 |
| Consumer Bootstrap slimming | 后续 reusable changes 未恢复状态/baseline history 到 Bootstrap | 静态回归 |

因此不重跑完整 Phase F；最小追加 Gate 为：

```text
T1 — updated adopted Guide ordinary local-only
T2 — Consumer override after updated local Guide
T3 — incremental baseline adoption ec945... → 29f88...
T4 — updated semantic-reviewed source identity / Catalog currentness
```

## 4. Consumer 定向重验边界

建议从已验证 Consumer 实验最终 Head：

`dygapp/jilinjobs-cms@14f2ad7f142f970188a4b7823a158e7026043f5a`

建立新的隔离 revalidation branch，保留原 Phase F Evidence 不变。

定向工作只需要：

1. 显式比较旧 candidate `ec945...` 与新 reusable candidate `29f88...`；
2. 按 Consumer 当前 Authority 对 reusable delta 逐项 `adopt / retain-or-override / reject-not-applicable / supersede-remove`；
3. 更新真正被采用的 Consumer-local source / provenance / Activation Manifest；
4. 不把 `agentic-dev/docs/project/*`、README/Roadmap/status 变化投射给 Consumer；
5. 验证 T1～T4；
6. ordinary runtime 测试阶段 upstream access 必须继续为 0；
7. 记录 exact revalidation branch / Head / Current Evidence；
8. 不合并 Consumer 实验分支，不把定向重验等同于正式 Consumer adoption。

## 5. PASS Gate

只有以下全部成立，旧 Phase F Evidence 才可与本次增量 Evidence 共同支持最终 v2 Candidate：

- T1～T4 PASS；
- R2 / R5 旧 Evidence 的未受影响映射仍成立；
- Consumer-specific override 继续优先；
- new verification Guide 没有被机械全量采用；
- rejected / not-applicable delta 不进入 active Manifest；
- updated adopted source identity current；
- ordinary runtime upstream access = 0；
- Blocking / Medium reusable finding = 0 / 0。

失败时只返回真正受影响 owner，不机械重跑全部 Phase F。

## 6. Phase G 边界

本定向重验是 Phase G 的 Current Evidence 修复门禁，不重新打开 Phase A～F 的全部设计与实验范围。

在结果返回前：

- PR #93 保持 Draft；
- Issue #92 保持 open；
- 不声明 Final AI Review PASS；
- 不进入人工 merge 决策。

结果通过后，继续 Final AI Review 的受影响维度复核与稳定状态收敛。