#!/usr/bin/env python3
from pathlib import Path

path = Path('docs/project/rule-governance-knowledge-activation-v1.md')
text = path.read_text(encoding='utf-8')
replacements = [
    (
        '当前下一工作项：\n\n> **C3 — 隔离运行时与人工评分**',
        'C3 评估设计（已完成）：\n\n> **C3 — 隔离运行时与人工评分**',
    ),
    (
        'C3 才执行冻结场景的真实新上下文 / 隔离 A/B，并由人工逐项评分。只有实际模型 / 推理强度、公平输入边界和隐藏断言隔离都能由证据支持的 A/B 配对，才可以进入效果比较。',
        'C3 已按冻结场景执行真实新上下文 / 隔离 A/B，并由人工逐项评分；只有实际模型 / 推理强度、公平输入边界和隐藏断言隔离都能由证据支持的 A/B 配对进入效果比较。',
    ),
    (
        '阶段 A 与阶段 B 已完成，阶段 C 的 C1、C2 已完成。下一实际步骤不是拆分指南、全库增加文件头，也不是实现代码复核，而是：',
        '阶段 A、阶段 B、阶段 C 已完成。下一实际步骤不是拆分指南、全库增加文件头，也不是实现代码复核，而是：',
    ),
]
for old, new in replacements:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'expected one target, got {count}: {old[:100]!r}')
    text = text.replace(old, new, 1)
path.write_text(text, encoding='utf-8')
Path('evals/c3_milestone_cleanup_tmp.py').unlink(missing_ok=True)
Path('.github/workflows/c3-milestone-cleanup.yml').unlink(missing_ok=True)
