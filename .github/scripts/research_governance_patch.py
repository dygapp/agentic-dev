from pathlib import Path

p = Path('docs/project/project-roadmap.md')
text = p.read_text(encoding='utf-8')
old = '- 证据见 `docs/research/rule-retrieval-c3-evaluation-results.md` 与 `evals/rule-retrieval/c3-human-scoring.json`。'
new = '- 机器可读人工评分保存在 `evals/rule-retrieval/c3-human-scoring.json`；精确运行与文档演进历史由 Git / PR #83～#86 保存。'
if old not in text:
    raise SystemExit('roadmap C3 historical Research reference not found')
p.write_text(text.replace(old, new, 1), encoding='utf-8')
