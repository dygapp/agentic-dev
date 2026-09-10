#!/usr/bin/env bash
set -euo pipefail

CANDIDATE_HEAD="a6a61a41db762dc81d5105fe3d63ebba3d418c7e"
EXPECTED_REMOTE_REF="origin/eval/rule-governance-v3-v3-01-medium-rereview"
MODEL="gpt-6-astra"
EFFORT="high"
MIN_CODEX_VERSION="0.153.0"

ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

PROMPT="$ROOT/evals/rule-governance-v3/v3-01-medium-rereview/prompt.md"
SCHEMA="$ROOT/evals/rule-governance-v3/v3-01-medium-rereview/output-schema.json"
RESULT_ROOT="$ROOT/evals/results/rule-governance-v3-v3-01-medium-rereview"
RUN_ID="$(date -u +%Y%m%dT%H%M%SZ)"
OUT="$RESULT_ROOT/$RUN_ID"

fail() {
  echo "[FAIL] $*" >&2
  exit 1
}

command -v git >/dev/null 2>&1 || fail "git not found"
command -v codex >/dev/null 2>&1 || fail "codex not found"
command -v python3 >/dev/null 2>&1 || fail "python3 not found"
command -v sort >/dev/null 2>&1 || fail "sort not found"

git rev-parse --verify "$EXPECTED_REMOTE_REF" >/dev/null 2>&1 || \
  fail "missing remote eval ref '$EXPECTED_REMOTE_REF'; run git fetch origin first"
git cat-file -e "$CANDIDATE_HEAD^{commit}" 2>/dev/null || \
  fail "candidate head $CANDIDATE_HEAD is not available locally"

HEAD_BEFORE="$(git rev-parse HEAD)"
EXPECTED_HEAD="$(git rev-parse "$EXPECTED_REMOTE_REF")"
CURRENT_BRANCH="$(git branch --show-current)"
CHECKOUT_MODE="named-branch"
[[ -n "$CURRENT_BRANCH" ]] || CHECKOUT_MODE="detached"

[[ "$HEAD_BEFORE" == "$EXPECTED_HEAD" ]] || \
  fail "current HEAD $HEAD_BEFORE does not equal remote eval HEAD $EXPECTED_HEAD"
git merge-base --is-ancestor "$CANDIDATE_HEAD" HEAD || \
  fail "eval HEAD is not descended from candidate $CANDIDATE_HEAD"

UNEXPECTED_FILES="$(git diff --name-only "$CANDIDATE_HEAD"...HEAD | grep -v '^evals/rule-governance-v3/v3-01-medium-rereview/' || true)"
[[ -z "$UNEXPECTED_FILES" ]] || {
  echo "$UNEXPECTED_FILES" >&2
  fail "eval ref contains changes outside the targeted review asset directory"
}

[[ -z "$(git status --porcelain --untracked-files=normal)" ]] || \
  fail "working tree is not clean before review"
[[ -f "$PROMPT" ]] || fail "missing prompt: $PROMPT"
[[ -f "$SCHEMA" ]] || fail "missing schema: $SCHEMA"

python3 - "$SCHEMA" <<'PY' || exit 1
import json, sys
p=sys.argv[1]
try:
    obj=json.load(open(p, encoding='utf-8'))
except Exception as e:
    print(f"[FAIL] invalid JSON schema: {e}", file=sys.stderr)
    raise SystemExit(1)
def walk(x):
    if isinstance(x, dict):
        if 'const' in x and 'type' not in x:
            raise ValueError('schema node using const lacks explicit type')
        for v in x.values(): walk(v)
    elif isinstance(x, list):
        for v in x: walk(v)
try:
    walk(obj)
except Exception as e:
    print(f"[FAIL] {e}", file=sys.stderr)
    raise SystemExit(1)
PY

CODEX_VERSION_RAW="$(codex --version)"
CODEX_VERSION="$(printf '%s\n' "$CODEX_VERSION_RAW" | grep -Eo '[0-9]+\.[0-9]+\.[0-9]+' | head -n1 || true)"
[[ -n "$CODEX_VERSION" ]] || fail "cannot parse Codex version from: $CODEX_VERSION_RAW"
LOWEST="$(printf '%s\n%s\n' "$MIN_CODEX_VERSION" "$CODEX_VERSION" | sort -V | head -n1)"
[[ "$LOWEST" == "$MIN_CODEX_VERSION" ]] || \
  fail "GPT-6 Astra requires Codex CLI >= $MIN_CODEX_VERSION; current: $CODEX_VERSION"

mkdir -p "$OUT"
EVENTS="$OUT/events.jsonl"
STDERR_LOG="$OUT/stderr.log"
FINAL="$OUT/review-result.json"
META="$OUT/run-metadata.json"

python3 - "$META" "$CANDIDATE_HEAD" "$EXPECTED_REMOTE_REF" "$HEAD_BEFORE" "$CHECKOUT_MODE" "$CURRENT_BRANCH" "$CODEX_VERSION" "$MODEL" "$EFFORT" "$RUN_ID" <<'PY'
import json,sys
p=sys.argv[1]
keys=['candidate_head','eval_ref','eval_head','checkout_mode','local_branch','codex_version','model_requested','reasoning_effort_requested','started_at_utc']
vals=sys.argv[2:]
obj={'repository':'dygapp/agentic-dev', **dict(zip(keys, vals))}
with open(p,'w',encoding='utf-8') as f: json.dump(obj,f,ensure_ascii=False,indent=2)
PY

STATUS_BEFORE="$(git status --porcelain --untracked-files=normal)"

echo "[INFO] repository:  dygapp/agentic-dev"
echo "[INFO] candidate:   $CANDIDATE_HEAD"
echo "[INFO] eval ref:    $EXPECTED_REMOTE_REF"
echo "[INFO] eval head:   $HEAD_BEFORE"
echo "[INFO] checkout:    $CHECKOUT_MODE${CURRENT_BRANCH:+ ($CURRENT_BRANCH)}"
echo "[INFO] codex:       $CODEX_VERSION_RAW"
echo "[INFO] model:       $MODEL"
echo "[INFO] effort:      $EFFORT"
echo "[INFO] output:      $OUT"

set +e
codex exec \
  --cd "$ROOT" \
  --sandbox read-only \
  --json \
  --model "$MODEL" \
  --config "model_reasoning_effort=\"$EFFORT\"" \
  --output-schema "$SCHEMA" \
  --output-last-message "$FINAL" \
  - < "$PROMPT" \
  2> >(tee "$STDERR_LOG" >&2) | tee "$EVENTS"
PIPE_STATUSES=("${PIPESTATUS[@]}")
CODEX_EXIT="${PIPE_STATUSES[0]:-1}"
TEE_EXIT="${PIPE_STATUSES[1]:-1}"
set -e

[[ "$CODEX_EXIT" -eq 0 ]] || fail "codex exec failed with exit $CODEX_EXIT"
[[ "$TEE_EXIT" -eq 0 ]] || fail "tee failed with exit $TEE_EXIT"
[[ -s "$EVENTS" ]] || fail "events.jsonl is empty"
[[ -s "$FINAL" ]] || fail "review-result.json is empty"

python3 - "$FINAL" "$EVENTS" "$META" "$CANDIDATE_HEAD" <<'PY' || exit 1
import json,sys
final,events,meta,expected=sys.argv[1:]
try:
    r=json.load(open(final,encoding='utf-8'))
except Exception as e:
    print(f"[FAIL] final response is not valid JSON: {e}",file=sys.stderr); raise SystemExit(1)
ev=[json.loads(x) for x in open(events,encoding='utf-8') if x.strip()]
if not any(x.get('type')=='turn.completed' for x in ev):
    print('[FAIL] JSONL contains no turn.completed event',file=sys.stderr); raise SystemExit(1)
if any(x.get('type')=='turn.failed' for x in ev):
    print('[FAIL] JSONL contains turn.failed',file=sys.stderr); raise SystemExit(1)
t=r.get('review_target',{})
if t.get('candidate_head')!=expected or t.get('candidate_pr')!=100:
    print('[FAIL] review result did not preserve exact candidate identity',file=sys.stderr); raise SystemExit(1)
paths=[x.get('path') for x in r.get('classifications',[])]
if len(paths)!=4 or len(set(paths))!=4:
    print('[FAIL] targeted classifications are incomplete or duplicated',file=sys.stderr); raise SystemExit(1)
major=sum(1 for x in r.get('findings',[]) if x.get('severity') in ('Blocking','Medium'))
if r.get('verdict')=='PASS' and not (major==0 and r.get('medium_resolved') is True and r.get('gate_assessment',{}).get('ready_for_v3_02_audit') is True):
    print('[FAIL] PASS verdict is inconsistent with findings/gate',file=sys.stderr); raise SystemExit(1)
if r.get('verdict')=='REVISE' and major==0:
    print('[FAIL] REVISE verdict has no Blocking/Medium finding',file=sys.stderr); raise SystemExit(1)
m=json.load(open(meta,encoding='utf-8')); m['completed']=True
with open(meta,'w',encoding='utf-8') as f: json.dump(m,f,ensure_ascii=False,indent=2)
print(f"[PASS] verdict: {r.get('verdict')}")
print(f"[PASS] medium resolved: {str(r.get('medium_resolved')).lower()}")
print(f"[PASS] ready for V3-02 audit: {str(r.get('gate_assessment',{}).get('ready_for_v3_02_audit')).lower()}")
print('[PASS] findings: Blocking=%d Medium=%d Low=%d' % tuple(sum(1 for x in r.get('findings',[]) if x.get('severity')==s) for s in ('Blocking','Medium','Low')))
PY

HEAD_AFTER="$(git rev-parse HEAD)"
STATUS_AFTER="$(git status --porcelain --untracked-files=normal)"
[[ "$HEAD_AFTER" == "$HEAD_BEFORE" ]] || fail "repository HEAD changed during read-only review"
[[ "$STATUS_AFTER" == "$STATUS_BEFORE" ]] || fail "tracked/unignored working tree changed during read-only review"

echo "[PASS] GPT-6 V3-01 Medium re-review completed"
echo "[PASS] result directory: $OUT"
