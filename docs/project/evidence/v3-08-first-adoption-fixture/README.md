# V3-08 First-adoption Gate C Durable Evidence

**性质：** Independent Review Gate C 的 Evidence-only fixture  
**关联：** Issue #118 Finding M-03；Issue #115 Track E E-02A / E-02B  
**可复用基线：** `agentic-dev@2fe193035c629f6b8805fd473bd322f70fe6e172`

## 1. 目的

本目录只用于修复 Independent Review M-03 暴露的 Evidence durability 缺口：原 E-02 fixture 位于无 remote 的 `/tmp` Git 仓库，Issue #115 持久保存了结果摘要，但无法从 GitHub 重新解析原始 fixture tree 与底层验证载体。

本目录**不声称重建原始 `/tmp` fixture 的 exact bytes 或原 commit `ffb8ed48110e2999626fb594fe837365b3fe582c`**。它提供一个新的、GitHub-addressable 的最小 replacement fixture snapshot，并针对同一组 first-adoption claims 执行定向复核。

它不是：

- production Consumer；
- Consumer 初始化模板；
- `agentic-dev` ordinary runtime 资源；
- 新的 mandatory Repository layout；
- Reviewed Discovery Map / Runtime View / Manifest / Catalog 的范本。

## 2. Durable fixture tree

`fixture/` 是定向复核使用的 final ordinary-runtime snapshot，加上一份只服务 Evidence 的 pre-verification candidate-state record：

- `AGENTS.md`
- `README.md`
- `SPECIFICATION.md`
- `docs/README.md`
- `governance/candidate-baseline-before-verification.md` — Evidence-only candidate state，不进入 ordinary runtime
- `governance/current-evaluated-baseline.md`
- `governance/active-asset-provenance.md`
- `governance/history/first-adoption.md`
- `skills/technical-plan/SKILL.md`

其中 `skills/technical-plan/SKILL.md` 固定复制自 exact upstream baseline `2fe193035...`，source blob identity 为 `14bdac2b735bd2ba1a3c38e0a343748b5e50125d`。

## 3. Seed / candidate / final lifecycle

为了避免把 Evidence fixture 变成三份长期 Consumer 模板，本目录只版本化 final snapshot，并用一个明确标记为 Evidence-only 的 candidate-state record 保留 baseline advancement 前边界：

- seed：只有最小 Repository Authority / README / product Specification；没有 evaluated baseline、Local Discovery Entry、adopted Skill、Map/View/Catalog；
- candidate：在 exact baseline 上完成 per-item adoption 与本地投影，但 `candidate-baseline-before-verification.md` 明确 current evaluated baseline 不得推进；
- final：adoption verification 通过后才由 `current-evaluated-baseline.md` 表达 evaluated baseline 已推进到 `2fe193035...`，随后进入 ordinary runtime。

这种记录方式只服务 Evidence durability，不规定真实 Consumer 必须使用这些文件名或目录。

## 4. Revalidation

定向复核断言、实际读取边界、routing-only / JIT Skill loading、Consumer-specific Authority override、history isolation 与 fail-closed 结果见：

`revalidation.md`

Gate C 只能在该 Evidence 与最终 PR exact Head 可从 GitHub 重新读取后，才把 M-03 视为 resolved candidate。