# WI-05 — Vue 3 + TypeScript Technology Profile

## 目标

完成 Engineering Capability Foundation v1 的 **F3 / WI-05**：以当前官方资料为主、成熟工程证据为辅，建立并验证首个代表性 **Vue 3 + TypeScript Technology Profile**，证明 `technology-profile-contract.md` 能够承载真实技术工程能力。

本 Plan 只协调当前 WI-05，不改变 Foundation v1 的完成边界。

## 当前状态

**Validated Draft / Targeted Eval PASS / Pending Final AI Review & Integration**

- Research：已完成；
- Architecture Fit：已完成；
- Draft Profile + Verification Profile：已完成；
- Capability Eval harness：已完成；
- Fresh Runtime Targeted Eval：`9 / 9 PASS`；
- Assertions：`41 / 41 PASS`；
- Runtime contamination：未发现；
- Final AI Review：待完成；
- Integration：待 Human / Repository Decision。

PR #50 实际合并前，F3 仍不能标记为已完成，也不能进入 F4 Consumer Adoption。

## 当前基线

- `agentic-dev`: `master@16151149ab52211e266839a110fc9a3c73415623`
- 待集成 PR：#50
- 受测 Profile 语义 Blob：`999911e83b23389d16f9cbbadeb4d5c29f56de75`
- Vue 稳定研究锚点：`vue@3.5.42`
- Vue 3.6：当前仍为 RC，不进入本轮规范基线
- TypeScript 稳定研究锚点：`7.0.2`
- Vue Language Tools：`3.3.11`
- Vue docs：`vuejs/docs main@b75d188ab16bf83bd1f364a77dfd2315be8f3fa4`
- `@vue/tsconfig`: `vuejs/tsconfig main@dc7af0b6a1e8a66239950a65423c5456ef5ba739`

研究证据：

`docs/research/vue3-typescript-profile-analysis.md`

Runtime 结果包 SHA-256：

`abf788b5e51db9fdc145d73dd6eafc16a99a6d3417dbd81b0aa00e538e22a088`

## 权威输入

执行本 WI 时重新读取：

- `AGENTS.md`
- `docs/architecture/engineering-capability-architecture.md`
- `docs/architecture/engineering-disciplines.md`
- `docs/architecture/technology-profile-contract.md`
- `docs/technology-profiles/README.md`
- `docs/project/engineering-capability-foundation-v1.md`
- `docs/project/project-roadmap.md`
- `docs/research/vue3-typescript-profile-analysis.md`
- `evals/capability/README.md`
- `evals/run_codex_evals.py`

## 范围

本 WI 只完成：

1. 当前官方 / 一手证据研究；
2. Architecture Fit Review；
3. Vue 3 + TypeScript Draft Profile；
4. 内嵌 Verification Profile；
5. 非 Skill Capability Targeted Eval 的最小 harness 扩展；
6. Fresh Runtime Targeted Eval；
7. assertion 级语义判分与必要修订 / 重跑；
8. 最终高影响 AI Review；
9. `Ready to Integrate`。

明确不进入：

- Vue 3.6 RC / Vapor Mode；
- Element Plus；
- 第二个 Technology Profile；
- `vue-skill` / `typescript-skill`；
- Spring / Gradle；
- Runtime Adapter / Distribution；
- Consumer Adoption；
- Core Method 修改，除非 Targeted Eval 证明存在 Blocking 的上层缺口。

## 执行顺序

```text
Research
→ Candidate
→ Architecture Fit Review
→ Draft Profile
→ Capability Eval Harness
→ Targeted Eval Materialization
→ Fresh Runtime Eval
→ Assertion-level Grading
→ Failure Loop（如需要）
→ Final AI Review
→ Ready to Integrate
→ Human / Repository Integration Decision
```

当前已推进到：

```text
Fresh Runtime Eval PASS
→ Final AI Review（当前）
→ Ready to Integrate
```

## Architecture Fit

当前结论：

- 层次：Technology Profile；
- 形式：一个 Vue 3 + TypeScript 组合 Profile；
- 验证：内嵌 Verification Profile；
- 运行时验证：非 Skill Capability Targeted Eval；
- Skill：新增 0；
- Method：不变。

已确认：

- Vue-specific、TypeScript-specific 与联合工具链规则可以清晰分区；
- 组合不是因为“常一起使用”，而是存在 SFC 类型检查、Vue macros、template typing、Vue Language Tools 等真实联合决策边界；
- Consumer-local versions / architecture / commands 继续高于 Profile Engineering Defaults；
- Element Plus-specific API 继续位于本 Profile Authority 之外。

## Targeted Eval 结果

`C-VTS-01`～`C-VTS-09` 已全部执行并逐 assertion 语义判分：

```text
Capability scenarios: 9 / 9 PASS
Assertions:           41 / 41 PASS
```

覆盖：

- Vite build 与 Vue-aware type-check 分离；
- computed / watcher 职责；
- prop mutation / standard v-model；
- `reactive<T>` 与 composable destructure；
- template ref 生命周期；
- TypeScript 7 与 Vue tooling compatibility；
- Consumer Override；
- Element Plus authority boundary；
- 风险驱动的验证扩展。

Eval 完整性：

- 每个场景使用独立 Fresh `codex exec --ephemeral --json`；
- Runtime 只读取声明的 Profile / context；
- 未读取 expected behavior / assertions / Research / 历史结果；
- 未通过创建 Skill 激活 Profile；
- 进程退出码未作为 PASS；
- 结果包中的 9 个 stderr 均为空；
- 受测 Profile 内容重建后的 Git Blob SHA 与 PR #50 冻结 Blob 完全一致。

Targeted Eval 后未修改 Profile 的 Technology Constraint、Engineering Default、Conditional Guidance、Known Misuse、Consumer Override 或 Verification Profile 语义，因此本轮证据仍覆盖当前规范行为；后续只允许证据 / 状态 / Project Governance 收口，不得在不重跑的情况下修改受测语义。

## 完成条件

WI-05 只有在以下条件同时成立时才达到 `Ready to Integrate`：

- Research 有明确 provenance / baseline / freshness / applicability；
- Draft Profile 满足 Technology Profile Contract；
- Vue 3.6 RC、Element Plus 等范围没有被机械吸收；
- Consumer Override / project-local command boundary 明确；
- Capability Eval harness 隔离成立且没有 Eval contamination；
- `C-VTS-01`～`C-VTS-09` 获得当前有效 PASS 证据；
- 没有未解决 Blocking / Medium Finding；
- Final AI Review: PASS；
- PR 只停在 `Ready to Integrate`，不自动 Merge。

当前除 Final AI Review / PR 状态收口外均已满足。

只有 WI-05 的 Profile 实际合并后，才把 F3 标记完成并进入 F4 Existing Consumer Adoption。