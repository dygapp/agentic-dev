#!/usr/bin/env python3
from pathlib import Path
import hashlib
import subprocess

INDEX = Path('evals/rule-retrieval/rule-index.json')
AGENTS = Path('AGENTS.md')
OLD = b'0bd04757c64e6eda6a7ba00e04eca40e92651c29'

agents = AGENTS.read_bytes()
new_identity = hashlib.sha1(b'blob ' + str(len(agents)).encode() + b'\0' + agents).hexdigest().encode()
original = subprocess.check_output(['git', 'show', 'origin/master:evals/rule-retrieval/rule-index.json'])
if original.count(OLD) != 1:
    raise SystemExit(f'old AGENTS identity count in master index = {original.count(OLD)}')
restored = original.replace(OLD, new_identity, 1)
INDEX.write_bytes(restored)

Path('evals/c3_index_format_fix_tmp.py').unlink(missing_ok=True)
Path('.github/workflows/c3-index-format-fix.yml').unlink(missing_ok=True)
