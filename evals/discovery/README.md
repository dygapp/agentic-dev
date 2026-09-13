---
id: eval:rule-discovery-v4
type: eval-guide
status: active
---

# V4 Rule Discovery Discriminating Evals

本目录验证 V4 中**必须由模型参与**的规则发现行为，不重复证明 V4-04 已由普通代码保证的 schema / deterministic matching。

当前 corpus：

`v4-discriminating.json`

覆盖：

- generation discovery；
- verification discovery；
- mixed responsibility 与 re-discovery；
- negative / ambiguity；
- invalid metadata fail-closed；
- Skill vs Rule；
- Consumer-local ordinary runtime。

运行：

```bash
python3 evals/run_codex_evals.py --discovery
```

单场景：

```bash
python3 evals/run_codex_evals.py --discovery --scenario D-V4-GEN-01
```

每个场景使用独立临时 workspace。Runtime 只得到当前 `AGENTS.md` / local Consumer Authority、Rule Discovery Tool、current Rules、current Skills 与场景输入；corpus 本身、`expected_behavior`、`assertions` 和历史结果不会复制进 workspace。

`returncode == 0` 只表示 Codex 进程完成。最终 PASS / FAIL 必须人工读取 JSONL trace 与最终输出，逐条断言判断：

- task signals 是否由真实事实提取；
- 是否实际调用 discovery；
- 是否只读取返回 candidates，而非全量 Rules；
- LLM 是否正确做最终适用性确认；
- responsibility 改变时是否重新发现；
- fail-closed / Skill / Consumer 边界是否保持。

运行结果写入 `evals/results/discovery/`，该目录仍属于临时评估证据。