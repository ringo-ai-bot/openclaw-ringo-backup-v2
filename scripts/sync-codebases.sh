#!/usr/bin/env bash
# Fast-forward local main/master for every top-level git repo under /data/code.
# Does not clobber dirty worktrees or feature-branch checkouts.
set -euo pipefail

CODE_ROOT="${CODE_ROOT:-/data/code}"
LOG_PATH="${LOG_PATH:-/home/jesse/.openclaw/workspace/memory/codebase-sync-last.json}"
TIMESTAMP="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"

ok_count=0
updated_count=0
skipped_count=0
error_count=0

results_tmp="$(mktemp)"
trap 'rm -f "$results_tmp"' EXIT

json_escape() {
  python3 -c 'import json,sys; print(json.dumps(sys.argv[1]))' "$1"
}

resolve_default_branch() {
  local repo="$1"
  local branch=""

  branch="$(git -C "$repo" symbolic-ref --quiet --short refs/remotes/origin/HEAD 2>/dev/null | sed 's#^origin/##' || true)"
  if [[ -n "$branch" ]]; then
    printf '%s\n' "$branch"
    return 0
  fi

  if git -C "$repo" show-ref --verify --quiet refs/remotes/origin/main; then
    printf 'main\n'
    return 0
  fi
  if git -C "$repo" show-ref --verify --quiet refs/remotes/origin/master; then
    printf 'master\n'
    return 0
  fi
  if git -C "$repo" show-ref --verify --quiet refs/heads/main; then
    printf 'main\n'
    return 0
  fi
  if git -C "$repo" show-ref --verify --quiet refs/heads/master; then
    printf 'master\n'
    return 0
  fi

  return 1
}

is_clean() {
  local repo="$1"
  [[ -z "$(git -C "$repo" status --porcelain 2>/dev/null)" ]]
}

record() {
  local name="$1"
  local status="$2"
  local detail="$3"
  local branch="${4:-}"

  printf '{"name":%s,"status":%s,"detail":%s,"branch":%s}\n' \
    "$(json_escape "$name")" \
    "$(json_escape "$status")" \
    "$(json_escape "$detail")" \
    "$(json_escape "$branch")" >>"$results_tmp"

  printf '%-24s %-10s %s\n' "$name" "$status" "$detail"
}

finish_status() {
  local name="$1"
  local branch="$2"
  local before_sha="$3"
  local after_sha="$4"
  local detail="$5"

  if [[ -z "$before_sha" ]]; then
    record "$name" "updated" "created local $branch at ${after_sha:0:7}; $detail" "$branch"
    updated_count=$((updated_count + 1))
  elif [[ "$before_sha" != "$after_sha" ]]; then
    record "$name" "updated" "${before_sha:0:7} -> ${after_sha:0:7}; $detail" "$branch"
    updated_count=$((updated_count + 1))
  else
    record "$name" "ok" "already at ${after_sha:0:7}; $detail" "$branch"
    ok_count=$((ok_count + 1))
  fi
}

is_ancestor() {
  local repo="$1"
  local maybe_ancestor="$2"
  local commit="$3"
  git -C "$repo" merge-base --is-ancestor "$maybe_ancestor" "$commit" 2>/dev/null
}

sync_repo() {
  local repo="$1"
  local name
  name="$(basename "$repo")"

  if [[ ! -d "$repo/.git" ]]; then
    return 0
  fi

  if ! git -C "$repo" remote get-url origin >/dev/null 2>&1; then
    record "$name" "skipped" "no origin remote" ""
    skipped_count=$((skipped_count + 1))
    return 0
  fi

  local fetch_err
  if ! fetch_err="$(git -C "$repo" fetch origin --prune 2>&1)"; then
    record "$name" "error" "fetch failed: ${fetch_err//$'\n'/; }" ""
    error_count=$((error_count + 1))
    return 0
  fi

  local branch
  if ! branch="$(resolve_default_branch "$repo")"; then
    record "$name" "skipped" "could not resolve main/master default branch" ""
    skipped_count=$((skipped_count + 1))
    return 0
  fi

  if ! git -C "$repo" show-ref --verify --quiet "refs/remotes/origin/$branch"; then
    record "$name" "error" "missing origin/$branch after fetch" "$branch"
    error_count=$((error_count + 1))
    return 0
  fi

  local before_sha=""
  if git -C "$repo" show-ref --verify --quiet "refs/heads/$branch"; then
    before_sha="$(git -C "$repo" rev-parse "refs/heads/$branch")"
  fi

  local remote_sha
  remote_sha="$(git -C "$repo" rev-parse "refs/remotes/origin/$branch")"

  local head
  head="$(git -C "$repo" rev-parse --abbrev-ref HEAD 2>/dev/null || true)"

  # Already up to date at the tip.
  if [[ -n "$before_sha" && "$before_sha" == "$remote_sha" ]]; then
    if [[ "$head" == "$branch" ]]; then
      if is_clean "$repo"; then
        finish_status "$name" "$branch" "$before_sha" "$remote_sha" "working tree clean"
      else
        finish_status "$name" "$branch" "$before_sha" "$remote_sha" "checkout is dirty; tip already current"
      fi
    else
      finish_status "$name" "$branch" "$before_sha" "$remote_sha" "on $head; left alone"
    fi
    return 0
  fi

  # Local tip exists but cannot fast-forward to origin.
  if [[ -n "$before_sha" ]] && ! is_ancestor "$repo" "$before_sha" "$remote_sha"; then
    record "$name" "skipped" "local $branch is not a fast-forward of origin/$branch" "$branch"
    skipped_count=$((skipped_count + 1))
    return 0
  fi

  if [[ "$head" == "$branch" ]]; then
    # Checked out: update via ff-only merge when clean.
    if ! is_clean "$repo"; then
      record "$name" "skipped" "on dirty $branch; origin moved to ${remote_sha:0:7}; left alone" "$branch"
      skipped_count=$((skipped_count + 1))
      return 0
    fi

    local merge_err
    if ! merge_err="$(git -C "$repo" merge --ff-only "origin/$branch" 2>&1)"; then
      record "$name" "error" "ff-only merge failed: ${merge_err//$'\n'/; }" "$branch"
      error_count=$((error_count + 1))
      return 0
    fi

    local after_sha
    after_sha="$(git -C "$repo" rev-parse "refs/heads/$branch")"
    finish_status "$name" "$branch" "$before_sha" "$after_sha" "updated working tree"
    return 0
  fi

  # Not checked out: move local branch tip with a non-forced refspec (ff-only).
  local ff_err
  if ! ff_err="$(git -C "$repo" fetch origin "refs/heads/$branch:refs/heads/$branch" 2>&1)"; then
    record "$name" "error" "failed to update local $branch: ${ff_err//$'\n'/; }" "$branch"
    error_count=$((error_count + 1))
    return 0
  fi

  local after_sha
  after_sha="$(git -C "$repo" rev-parse "refs/heads/$branch")"
  finish_status "$name" "$branch" "$before_sha" "$after_sha" "on $head; left alone"
}

if [[ ! -d "$CODE_ROOT" ]]; then
  echo "ERROR: CODE_ROOT not found: $CODE_ROOT" >&2
  exit 1
fi

shopt -s nullglob
for repo in "$CODE_ROOT"/*/; do
  sync_repo "${repo%/}"
done

python3 - "$LOG_PATH" "$TIMESTAMP" "$ok_count" "$updated_count" "$skipped_count" "$error_count" "$results_tmp" <<'PY'
import json, sys
log_path, ts, ok, updated, skipped, errors, results_path = sys.argv[1:8]
repos = []
with open(results_path) as f:
    for line in f:
        line = line.strip()
        if line:
            repos.append(json.loads(line))
payload = {
    "timestamp": ts,
    "counts": {
        "ok": int(ok),
        "updated": int(updated),
        "skipped": int(skipped),
        "error": int(errors),
        "total": len(repos),
    },
    "repos": repos,
}
with open(log_path, "w") as f:
    json.dump(payload, f, indent=2)
    f.write("\n")
print(f"\nsummary: ok={ok} updated={updated} skipped={skipped} error={errors} total={len(repos)}")
print(f"log: {log_path}")
PY

if [[ "$error_count" -gt 0 ]]; then
  exit 1
fi
exit 0
