# V3-08 Track E — Gate C Targeted Revalidation

**关联：** Issue #118 Finding M-03  
**性质：** replacement durable Evidence 的定向复核；不冒充原 `/tmp` fixture  
**candidate upstream baseline：** `agentic-dev@2fe193035c629f6b8805fd473bd322f70fe6e172`

## 1. Evidence boundary

原 E-02A / E-02B 已在 Issue #115 记录 first-adoption 与 Fresh Context PASS，但原 fixture 位于无 remote 的 `/tmp/v3-08-e02-first-adoption-consumer`。本轮不声称恢复其 exact bytes，而是建立新的 GitHub-addressable replacement fixture，对 M-03 指出的关键 claim 做定向复核。

本轮把两类访问明确分开：

1. **adoption / provenance revalidation**：允许读取 exact upstream candidate source，以核对 adopted asset provenance；
2. **ordinary-runtime trace**：从 trace 边界开始只读取本目录 `fixture/**`，upstream reads = 0。

## 2. Durable fixture identity

Final fixture root：

`docs/project/evidence/v3-08-first-adoption-fixture/fixture/`

完整文件集合：

- `AGENTS.md`
- `README.md`
- `SPECIFICATION.md`
- `docs/README.md`
- `governance/candidate-baseline-before-verification.md` — Evidence-only pre-verification state
- `governance/current-evaluated-baseline.md`
- `governance/active-asset-provenance.md`
- `governance/history/first-adoption.md`
- `skills/technical-plan/SKILL.md`

最终 exact PR Head / integration commit 由 GitHub PR 与 Issue #118 Gate C Evidence 记录；这些路径因此可以从 GitHub 重新解析，而不依赖临时 `/tmp` 仓库。

Adopted Skill source identity：

- upstream：`2fe193035c629f6b8805fd473bd322f70fe6e172:skills/technical-plan/SKILL.md`
- upstream blob：`14bdac2b735bd2ba1a3c38e0a343748b5e50125d`
- local replacement fixture blob：`14bdac2b735bd2ba1a3c38e0a343748b5e50125d`
- result：**exact blob match / PASS**

## 3. First-adoption lifecycle representation

本 Evidence 不制造 production Consumer，也不把 fixture 变成 reusable template。

可审计生命周期为：

```text
seed
  = minimal Repository Authority + README + product Specification
  + no evaluated baseline
  + no Local Discovery Entry
  + no adopted Skill
  + no Map / Runtime View / Catalog / Manifest

→ explicit candidate baseline 2fe193035...
→ per-item adopt / retain-or-override / reject-not-applicable
→ local projection pending verification
  = thin docs/README.md
  + local adopted technical-plan Skill
  + separated provenance / history
  + candidate-baseline-before-verification explicitly forbids current baseline advancement

→ adoption verification PASS
→ current-evaluated-baseline advances to 2fe193035...
→ ordinary runtime
```

`governance/history/first-adoption.md` 持久保存 per-item disposition 与 verification-before-baseline-advance 规则；`candidate-baseline-before-verification.md` 保存 pre-verification gate；final `current-evaluated-baseline.md` 只保存已通过验证后的 evaluated frontier。普通 Local Discovery Entry 不引用 evaluated-baseline provenance、candidate-state record 或 adoption history。

## 4. Targeted assertions

| ID | Assertion | Evidence | Result |
|---|---|---|---|
| T-01 | fixture 是独立最小 Consumer Evidence，不是 production template | `README.md` / fixture `AGENTS.md` | PASS |
| T-02 | exact upstream candidate baseline 可追溯 | provenance + candidate/final baseline records | PASS |
| T-03 | per-item adoption 明确区分 adopt / retain-or-override / reject | `governance/history/first-adoption.md` | PASS |
| T-04 | adopted `technical-plan` 是 exact local asset，而非 upstream runtime pointer | local blob = upstream blob `14bdac2...` | PASS |
| T-05 | Consumer-specific Product Authority 高于 reusable Skill | fixture `AGENTS.md` + `SPECIFICATION.md` | PASS |
| T-06 | Local Discovery Entry 足够薄，不复制 Skill / Product / project-state 正文，也不吸收 adoption provenance | fixture `docs/README.md` | PASS |
| T-07 | 当前复杂度不要求 Reviewed Discovery Map | one Specification + one adopted Skill + stable Authority | PASS |
| T-08 | 当前复杂度不要求 Runtime View / Catalog / Manifest | same as T-07 | PASS |
| T-09 | candidate baseline、evaluated baseline、active asset provenance、adoption history 分离，且 baseline 只在 verification 后推进 | four governance roles separated | PASS |
| T-10 | state-only / routing-only 不加载完整 Skill 或 adoption history | ordinary trace below | PASS |
| T-11 | execute 才 JIT 加载 local `technical-plan`，且 Skill 不覆盖 Consumer constraint | ordinary trace + planning result below | PASS |
| T-12 | ordinary discovery failure 不自动访问 upstream；history 不进入普通输入 | fixture `AGENTS.md` + `docs/README.md` + ordinary trace | PASS |

## 5. Ordinary-runtime trace

### 5.1 State-only

Trace boundary 从这里开始计数；不再读取 upstream。

Actual fixture-local content reads：

1. `fixture/AGENTS.md`
2. `fixture/SPECIFICATION.md`
3. `fixture/docs/README.md`
4. `fixture/governance/current-evaluated-baseline.md`

第 4 项只因为本次 state-only 复核明确要求同时恢复“当前 evaluated upstream baseline”而进入读取；`docs/README.md` 并不把 baseline owner 作为 ordinary capability discovery entry。定位动作只在 fixture-local `governance/**` 范围内最小完成，没有读取 candidate-state record、active provenance、adoption history 或 upstream。

Recovered：

- Consumer Repository Authority；
- Audit Event persistence WHAT / WHY；
- external managed database/service prohibited；
- writable local filesystem available；
- evaluated upstream baseline = `2fe193035...`；
- current local discovery / fail-closed boundary。

Not loaded in state-only：

- full `technical-plan` Skill；
- `candidate-baseline-before-verification.md`；
- `active-asset-provenance.md`；
- `governance/history/first-adoption.md`；
- any upstream project file。

Result：**PASS**。

### 5.2 Routing-only

Using only Repository Authority + Specification + Local Discovery Entry：

- primary responsibility：`technical-plan`
- primary locator：`fixture/skills/technical-plan/SKILL.md`
- minimal supporting owner：`fixture/SPECIFICATION.md`

Full Skill body is not required to reach this routing result.

Result：**PASS**。

### 5.3 Execute / JIT loading

Only after Technical Planning became the primary responsibility, load:

`fixture/skills/technical-plan/SKILL.md`

For the current product constraint, compare two representative local persistence options:

1. embedded H2 JDBC file mode；
2. daily append-only JSONL segments。

Targeted planning result：

- prefer **embedded H2 file mode behind an `AuditEventStore` boundary**；
- reason：remains local-filesystem based, avoids external managed service, provides transaction / recovery / indexed time-range query without inventing a custom storage engine；
- JSONL remains a feasible simpler alternative but would require the Consumer to own more indexing / recovery / compaction semantics；
- this is a HOW recommendation and does not change the Specification prohibition on external managed service。

Consumer-specific Authority therefore remains controlling; reusable Skill only supplies the planning process.

Result：**PASS**。

### 5.4 History isolation / fail-closed

During state-only, routing-only and execute input formation, candidate-state / provenance / adoption history are not required. They remain durable adoption / decision Evidence only.

If the technical-plan locator becomes missing or primary responsibility becomes ambiguous, the Local Discovery Entry requires returning to fixture-local Authority / Specification and stopping if unresolved. Upstream is not an implicit ordinary-runtime fallback.

Ordinary-runtime upstream reads inside §5 trace：**0**。

Result：**PASS**。

## 6. Finding impact

This targeted replacement does not prove that the old `/tmp` commit can now be reconstructed; it resolves the durability problem by replacing the non-addressable raw fixture with a new GitHub-addressable Evidence fixture and repeating the claims that depended on raw fixture visibility.

Result：

- original E-02 summary remains historical Evidence；
- replacement fixture provides current durable auditability for first-adoption / local projection / verification-before-baseline-advance / JIT / Consumer override claims；
- no new V3 lifecycle / resource / discovery defect identified；
- no Reviewed Discovery Map / Runtime View universal conclusion is introduced；
- M-03 can be considered **resolved candidate** only after the final Gate C PR exact Head is re-read and this Evidence remains complete and internally consistent。