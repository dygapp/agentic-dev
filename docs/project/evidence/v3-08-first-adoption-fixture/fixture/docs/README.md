# Local Discovery Entry

本文件是该 Evidence fixture 的薄本地发现入口，不拥有产品、方法或 Skill 正文。

## Stable local entries

- Repository Authority：`../AGENTS.md`
- Product Specification：`../SPECIFICATION.md`
- 当前按需能力：`../skills/technical-plan/SKILL.md`

## Progressive loading

- state-only：读取 Repository Authority / Product Specification；不为了 ordinary state recovery 默认加载 Skill、provenance 或 adoption history；
- routing-only：只返回 primary responsibility 与 locator，不读取完整 Skill；
- execute：确认进入 Technical Planning 后才读取完整 `technical-plan` Skill。

当前 evaluated upstream baseline 有独立本地 owner，但不属于 ordinary capability discovery；只有当前任务明确需要恢复 adoption / upgrade frontier 时，才在 fixture-local governance 范围做最小定位并读取。

## Fail closed

如果 locator 缺失、Authority 冲突或无法可靠判断 primary responsibility：

```text
Local Discovery Entry
→ Consumer Repository Authority / Specification
→ 最小本地扩读
→ 仍无法解析则停止
```

普通运行不以 discovery failure 为由自动访问 upstream。

## Deliberate exclusions

本入口不引用：

- evaluated-baseline provenance / adoption history；
- upstream project Roadmap / state；
- Reviewed Discovery Map；
- Runtime View / Catalog / Manifest。

当前 fixture 复杂度不需要上述额外层。