#!/usr/bin/env bash
set -euo pipefail

BASE_COMMIT="3c31ae96683c4a653f001402b889b40e87df976b"
EXPECTED_REMOTE_REF="origin/eval/rule-governance-v3-gpt6-review"
MODEL="gpt-6-astra"
EFFORT="xhigh"
MIN_CODEX_VERSION="0.153.0"

ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

PROMPT="$ROOT/evals/rule-governance-v3/gpt6-review-prompt.md"
SCHEMA="$ROOT/evals/rule-governance-v3/review-output-schema.json"
RESULT_ROOT="$ROOT/evals/results/rule-governance-v3-gpt6-review"
RUN_ID="$(date -u +%Y%m%dT%H%M%SZ)"
OUT="$RESULT_ROOT/$RUN_ID"

fail() {
  echo "[FAIL] $*" >&2
  exit 1
}

command -v git >/dev/null 2>&1 || fail "git not found"
command -v codex >/dev/null 2>&1 || fail "codex not found"
command -v jq >/dev/null 2>&1 || fail "jq not found"
command -v sort >/dev/null 2>&1 || fail "sort not found"

git rev-parse --verify "$EXPECTED_REMOTE_REF" >/dev/null 2>&1 || \
  fail "missing remote eval ref '$EXPECTED_REMOTE_REF'; run git fetch origin first"

HEAD_BEFORE="$(git rev-parse HEAD)"
EXPECTED_HEAD="$(git rev-parse "$EXPECTED_REMOTE_REF")"
CURRENT_BRANCH="$(git branch --show-current)"
CHECKOUT_MODE="named-branch"
[[ -n "$CURRENT_BRANCH" ]] || CHECKOUT_MODE="detached"

[[ "$HEAD_BEFORE" == "$EXPECTED_HEAD" ]] || \
  fail "current HEAD $HEAD_BEFORE does not equal remote eval HEAD $EXPECTED_HEAD"

git merge-base --is-ancestor "$BASE_COMMIT" HEAD || \
  fail "current eval HEAD is not descended from frozen base $BASE_COMMIT"

UNEXPECTED_FILES="$(git diff --name-only "$BASE_COMMIT"...HEAD | grep -v '^evals/rule-governance-v3/' || true)"
[[ -z "$UNEXPECTED_FILES" ]] || {
  echo "$UNEXPECTED_FILES" >&2
  fail "evaluation ref contains changes outside evals/rule-governance-v3/"
}

[[ -z "$(git status --porcelain --untracked-files=normal)" ]] || \
  fail "working tree is not clean before review"

[[ -f "$PROMPT" ]] || fail "missing prompt: $PROMPT"
[[ -f "$SCHEMA" ]] || fail "missing schema: $SCHEMA"

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

STATUS_BEFORE="$(git status --porcelain --untracked-files=normal)"

jq -n \
  --arg repository "dygapp/agentic-dev" \
  --arg base_commit "$BASE_COMMIT" \
  --arg eval_ref "$EXPECTED_REMOTE_REF" \
  --arg eval_head "$HEAD_BEFORE" \
  --arg checkout_mode "$CHECKOUT_MODE" \
  --arg local_branch "$CURRENT_BRANCH" \
  --arg codex_version "$CODEX_VERSION" \
  --arg model_requested "$MODEL" \
  --arg reasoning_effort_requested "$EFFORT" \
  --arg started_at_utc "$RUN_ID" \
  '{
    repository: $repository,
    base_commit: $base_commit,
    eval_ref: $eval_ref,
    eval_head: $eval_head,
    checkout_mode: $checkout_mode,
    local_branch: $local_branch,
    codex_version: $codex_version,
    model_requested: $model_requested,
    reasoning_effort_requested: $reasoning_effort_requested,
    started_at_utc: $started_at_utc
  }' > "$META"

echo "[INFO] repository:  dygapp/agentic-dev"
echo "[INFO] eval ref:    $EXPECTED_REMOTE_REF"
echo "[INFO] eval head:   $HEAD_BEFORE"
echo "[INFO] checkout:    $CHECKOUT_MODE${CURRENT_BRANCH:+ ($CURRENT_BRANCH)}"
echo "[INFO] base:        $BASE_COMMIT"
echo "[INFO] codex:       $CODEX_VERSION_RAW"
echo "[INFO] model:       $MODEL"
echo "[INFO] effort:      $EFFORT"
echo "[INFO] output:      $OUT"

# Fresh, read-only Codex execution. The prompt is passed through stdin so shell
# quoting cannot alter the review text. stdout is JSONL telemetry; the final
# model response is separately written to FINAL and constrained by SCHEMA.
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
CODEX_EXIT=${PIPESTATUS[0]}
TEE_EXIT=${PIPESTATUS[1]}
set -e

[[ "$CODEX_EXIT" -eq 0 ]] || fail "codex exec failed with exit $CODEX_EXIT"
[[ "$TEE_EXIT" -eq 0 ]] || fail "tee failed with exit $TEE_EXIT"
[[ -s "$EVENTS" ]] || fail "events.jsonl is empty"
[[ -s "$FINAL" ]] || fail "review-result.json is empty"

jq -e . "$FINAL" >/dev/null || fail "final response is not valid JSON"
jq -e 'select(.type == "turn.completed")' "$EVENTS" >/dev/null || \
  fail "JSONL contains no turn.completed event"

if jq -e 'select(.type == "turn.failed")' "$EVENTS" >/dev/null; then
  fail "JSONL contains turn.failed"
fi

jq -e --arg expected "$BASE_COMMIT" \
  '.review_target.base_commit == $expected' "$FINAL" >/dev/null || \
  fail "review result did not preserve frozen base commit"

jq -e '
  .verdict as $v |
  ([.findings[] | select(.severity == "Blocking" or .severity == "Medium")] | length) as $major |
  if $v == "PASS" then $major == 0
  elif $v == "REVISE" then $major > 0
  else true
  end
' "$FINAL" >/dev/null || \
  fail "verdict is inconsistent with Blocking/Medium findings"

HEAD_AFTER="$(git rev-parse HEAD)"
STATUS_AFTER="$(git status --porcelain --untracked-files=normal)"
[[ "$HEAD_AFTER" == "$HEAD_BEFORE" ]] || fail "repository HEAD changed during read-only review"
[[ "$STATUS_AFTER" == "$STATUS_BEFORE" ]] || fail "tracked/unignored working tree changed during read-only review"

# Capture the runtime header if the CLI exposes it. Absence is not a hard
# failure because header formatting is not a stable result contract.
grep -E '^(model|reasoning effort):' "$STDERR_LOG" > "$OUT/runtime-selection.txt" || true

jq '. + {completed: true}' "$META" > "$META.tmp"
mv "$META.tmp" "$META"

echo
printf '[PASS] GPT-6 governance review run completed\n'
printf '[PASS] verdict: %s\n' "$(jq -r '.verdict' "$FINAL")"
printf '[PASS] findings: Blocking=%s Medium=%s Low=%s\n' \
  "$(jq '[.findings[] | select(.severity == "Blocking")] | length' "$FINAL")" \
  "$(jq '[.findings[] | select(.severity == "Medium")] | length' "$FINAL")" \
  "$(jq '[.findings[] | select(.severity == "Low")] | length' "$FINAL")"
printf '[PASS] result directory: %s\n' "$OUT"
