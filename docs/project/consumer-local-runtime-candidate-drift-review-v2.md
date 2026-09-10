# Consumer-local Runtime Candidate Drift 复核 v2

## 状态

**Phase G Current Evidence Gate — 已完成 / PASS**

Phase F 已在 `agentic-dev@ec945368678715732fe729c331bd3bcdd919bbdd` 上通过真实 Consumer R1～R5。Phase G Final AI Review 随后修复了两个会影响 reusable Guide 的中等级问题，因此旧 Phase F Evidence 不能未经影响判断直接覆盖后续 Candidate。

本复核冻结并验证的 reusable candidate 为：

`agentic-dev@29f88efd25232e57ccb4a82ffff039be047e4d1e`

## 1. Candidate Drift

从旧验证 Candidate：

`ec945368678715732fe729c331bd3bcdd919bbdd`

到冻结 reusable candidate：

`29f88efd25232e57ccb4a82ffff039be047e4d1e`

后续变化分成两类。

### 1.1 project-only / evidence state

以下变化只属于 `agentic-dev` 自身项目状态，不进入 Consumer reusable runtime：

- README；
- `docs/project/*`；
- Project Roadmap；
- task / Issue / PR / Phase 状态；
- Phase F / Phase G 验证记录。

### 1.2 reusable changes

真正需要 Consumer 重新评估的 reusable 变化为：

- `docs/guides/consumer-local-rule-activation.md`：明确 ordinary runtime 以 Consumer Repository Authority 和当前本地已采用版本为准，upstream latest 不自动参与运行时裁决；
- `docs/guides/rule-activation-guide.md`：更新薄导航，移除旧 Guide §5.x 路径并指向当前 semantic owner；
- `docs/guides/using-agentic-dev.md`：核心职责过程归回对应 Skill，Guide 只保留 bootstrap、adoption、routing pointer、Roadmap lifecycle、Fresh Context 和实验边界；
- `docs/guides/verification-evidence-rules.md`：新增真正跨职责的验证证据规则 owner。

## 2. 最小追加 Gate

基于 Evidence Claim 影响映射，不重跑完整 Phase F，只执行：

- T1 — updated adopted Guide ordinary local-only；
- T2 — Consumer override after updated local Guide；
- T3 — incremental baseline adoption `ec945... → 29f88...`；
- T4 — updated semantic-reviewed source identity / Catalog currentness。

R2 Stage Return / ambiguity / routing-only 与 R5 stale / rebuild 核心机制复用原 Phase F Evidence，只补受 source identity 变化影响的 currentness 检查。

## 3. Consumer 定向重验结果

Consumer：`dygapp/jilinjobs-cms`

原 Phase F source Head：

`14f2ad7f142f970188a4b7823a158e7026043f5a`

定向重验分支：

`experiment/rule-activation-v2-final-candidate-revalidation`

最终 exact Head：

`c29da21b41ff3ddad023ecb64e3628dc3136a77e`

结果：

```text
T1: PASS
T2: PASS
T3: PASS
T4: PASS
```

### T1

更新后的 local Guide 继续保持：

- Consumer Repository Authority first；
- ordinary runtime 使用 Consumer 当前本地化并明确采用的 reusable semantics；
- upstream latest 不自动被重新读取或覆盖本地规则；
- ordinary runtime upstream access = 0。

### T2

真实 Consumer Repository Operation Boundary 继续覆盖更通用 reusable default。`agentic-dev` 文件、Branch、Commit、PR、Actions mutation 仍受 Consumer-specific Authority 禁止。

### T3

增量 baseline adoption 正确完成逐项分类：

- 需要的 Consumer-local Guide 更新被采用；
- `rule-activation-guide.md` 与 `using-agentic-dev.md` 不作为 Consumer ordinary-runtime asset 被机械 vendor；
- 新 `verification-evidence-rules.md` 按 Consumer 当前需要分类，没有因 upstream 新增而自动进入 active Manifest；
- 旧 Guide identity / provenance 被新的 current identity 正确 supersede；
- 未变化的 `technical-plan` Skill 保留其真实旧 provenance，没有因为 `last evaluated upstream baseline` 前进而机械重标；
- `last evaluated upstream baseline` 与每个 active asset 的 `adopted_from` 继续分离。

### T4

已验证：

```text
old semantic-reviewed identity
→ stale detected
→ old discovery rejected / fail-closed
→ semantic review / adoption
→ current identity update
→ Catalog rebuild / currentness PASS
```

不是仅更新 hash 绕过语义复核。

## 4. Current Evidence

最终 Workflow：`Phase G Candidate Drift Revalidation`

- Run：`34450265966`
- Head：`c29da21b41ff3ddad023ecb64e3628dc3136a77e`
- Conclusion：success
- Artifact：`phase-g-candidate-drift-evidence`
- Artifact ID：`10141246815`
- Artifact digest：`sha256:7d1a9dc47a6192e4b6c010585d2c69ff387392083448b504c89848465a74fb06`
- Manifest currentness：PASS
- Catalog currentness / rebuild：PASS
- ordinary runtime upstream access：0
- Blocking reusable findings：0
- Medium reusable findings：0

Consumer `14f2ad7f... → c29da21b...` 只有两次定向实验提交，只涉及 activation / adoption / eval / workflow evidence 资产；Consumer `AGENTS.md`、README、`docs/README.md`、Roadmap 与产品代码均未修改。

## 5. 原 Phase F Evidence 复用结论

以下 claim 保持有效：

- R2 Stage Return / ambiguity / routing-only：后续 reusable Guide 去重没有改变已验证 Stage Return / responsibility 语义；
- R5 stale / rebuild：核心机制保持不变，T4 已对新的 source identity 取得 currentness evidence；
- Bootstrap slimming：定向重验没有重新把 Phase / EU / PR / Run、baseline history 或重复 Skill / Method 正文放回 Consumer Bootstrap。

因此：

> 原 Phase F Evidence + 本次 T1～T4 Current Evidence 可以共同支持 frozen reusable candidate `29f88efd...`。

## 6. 结论

**Candidate Drift 定向重验：PASS。**

满足：

- T1～T4 全部 PASS；
- Consumer-specific override 继续优先；
- rejected / not-applicable delta 不进入 active Manifest；
- current adopted source identity 可验证；
- ordinary runtime upstream access = 0；
- Blocking / Medium reusable finding = `0 / 0`。

本 PASS 不等于 Consumer 正式 adoption 或实验分支合并。它只用于支持 `agentic-dev` Phase G Final AI Review 与 v2 集成准备。

后续如果 PR #93 只发生 README、`docs/project/*`、task、Issue / PR 状态等 project-only 收敛，不需要重新打开 Consumer 验证；只有 reusable Guide / Skill / Method / Architecture 再发生实质变化，才重新评估 Evidence Claim 影响。