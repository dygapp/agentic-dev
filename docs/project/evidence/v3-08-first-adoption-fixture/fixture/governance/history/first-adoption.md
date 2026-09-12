# First Adoption Decision History

**性质：** adoption-only historical Evidence；ordinary runtime 不默认读取。

Candidate upstream baseline：

`agentic-dev@2fe193035c629f6b8805fd473bd322f70fe6e172`

Per-item disposition：

- Consumer Lifecycle：`retain / override` Consumer-specific Authority，同时采用 explicit candidate / per-item disposition / verification-before-baseline-advance 语义；
- Agent Resource Model：`adopt` owner / provenance / current-authority separation；不采用 universal metadata / Manifest / Catalog；
- Resource Discovery Architecture：`adopt` thin Consumer-local Local Discovery Entry 与 local fail-closed；Reviewed Discovery Map / Runtime View 由复杂度决定；
- `technical-plan` Skill：`adopt`，复制为本地 on-demand capability；
- upstream project Roadmap / V3 project state / self `docs/discovery/**` / Research / Eval / unrelated Skills：`reject / not applicable`；
- `supersede / remove`：新 Consumer seed 无既有 adopted asset，因此不适用。

Baseline advancement rule：只有 local projection 与 adoption verification 均通过后，才把 `current-evaluated-baseline.md` 推进到 candidate baseline。
