#!/usr/bin/env bash
# Run core-loans commands inside Docker backend containers.
set -euo pipefail

CONTEXT="danacita"
REPO=""
COMPOSE_FILE=""
NO_UP=0
KEEP_UP=0
SHOULD_CLEANUP=0

usage() {
  cat <<'EOF'
Usage: run.sh [options] <command> [args...]

Commands:
  test [args...]       ./manage.py test
  migrate [args...]    ./manage.py migrate
  manage [args...]     ./manage.py (any subcommand)
  exec [args...]       run arbitrary command in container
  isort [args...]      isort
  black [args...]      black
  pytest [args...]     pytest
  shell                interactive bash (no -T)
  up                   ensure stack is up (no exec)

Options:
  --repo PATH          core-loans checkout (default: detect from $PWD)
  --context CTX        danacita (default) or bukas
  --compose-file FILE  override compose file
  --no-up              skip docker compose up -d
  --keep-up            leave containers running after command exits
  -h, --help           show this help

Examples:
  run.sh test loans.tests.test_foo --keepdb
  run.sh migrate
  run.sh manage makemigrations --check
  run.sh exec python scripts/foo.py --arg
  run.sh --context bukas test payments.tests.test_bar
  run.sh --repo /data/code/core-loans isort path/to/file.py
  # Multi-step ticket session (warm stack — prefer this for iterative tests):
  run.sh --repo /path/to/worktree --keep-up up
  run.sh --repo /path/to/worktree --keep-up --no-up test app.tests.mod.T.test_x --keepdb
EOF
}

die() {
  echo "run.sh: $*" >&2
  exit 1
}

cleanup_stack() {
  if [[ "$SHOULD_CLEANUP" -eq 1 && "$KEEP_UP" -eq 0 ]]; then
    docker compose -f "$COMPOSE_FILE" down >/dev/null 2>&1 || true
  fi
}

resolve_repo() {
  if [[ -n "$REPO" ]]; then
    REPO="$(cd "$REPO" && pwd)"
    return
  fi
  if git rev-parse --show-toplevel >/dev/null 2>&1; then
    local root
    root="$(git rev-parse --show-toplevel)"
    if [[ -f "$root/manage.py" && -f "$root/docker-compose.danacita.yml" ]]; then
      REPO="$root"
      return
    fi
  fi
  if [[ -f /data/code/core-loans/manage.py ]]; then
    REPO="/data/code/core-loans"
    return
  fi
  die "could not detect core-loans repo; use --repo PATH"
}

map_context() {
  case "$CONTEXT" in
    danacita)
      COMPOSE_FILE="${COMPOSE_FILE:-docker-compose.danacita.yml}"
      BACKEND="backend_danacita"
      ;;
    bukas)
      COMPOSE_FILE="${COMPOSE_FILE:-docker-compose.bukas.yml}"
      BACKEND="backend"
      ;;
    *)
      die "unknown context: $CONTEXT (use danacita or bukas)"
      ;;
  esac
}

ensure_stack() {
  if [[ "$NO_UP" -eq 1 ]]; then
    return
  fi
  SHOULD_CLEANUP=1
  docker compose -f "$COMPOSE_FILE" up -d "$BACKEND" postgres redis >/dev/null
}

run_exec() {
  local use_tty="-T"
  if [[ "${1:-}" == "shell" ]]; then
    use_tty=""
    shift
  fi
  if [[ -n "$use_tty" ]]; then
    docker compose -f "$COMPOSE_FILE" exec $use_tty "$BACKEND" "$@"
  else
    docker compose -f "$COMPOSE_FILE" exec "$BACKEND" "$@"
  fi
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --repo)
      REPO="${2:?--repo requires a path}"
      shift 2
      ;;
    --context)
      CONTEXT="${2:?--context requires danacita or bukas}"
      shift 2
      ;;
    --compose-file)
      COMPOSE_FILE="${2:?--compose-file requires a file}"
      shift 2
      ;;
    --no-up)
      NO_UP=1
      shift
      ;;
    --keep-up)
      KEEP_UP=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    --)
      shift
      break
      ;;
    -*)
      die "unknown option: $1"
      ;;
    *)
      break
      ;;
  esac
done

[[ $# -ge 1 ]] || { usage; exit 1; }

resolve_repo
map_context
cd "$REPO"
trap cleanup_stack EXIT

[[ -f "$COMPOSE_FILE" ]] || die "compose file not found: $REPO/$COMPOSE_FILE"

CMD="$1"
shift

case "$CMD" in
  up)
    docker compose -f "$COMPOSE_FILE" up -d
    ;;
  test)
    ensure_stack
    run_exec ./manage.py test "$@"
    ;;
  migrate)
    ensure_stack
    run_exec ./manage.py migrate "$@"
    ;;
  manage)
    ensure_stack
    run_exec ./manage.py "$@"
    ;;
  exec)
    ensure_stack
    run_exec "$@"
    ;;
  isort)
    ensure_stack
    run_exec isort "$@"
    ;;
  black)
    ensure_stack
    run_exec black "$@"
    ;;
  pytest)
    ensure_stack
    run_exec pytest "$@"
    ;;
  shell)
    ensure_stack
    run_exec shell
    ;;
  *)
    die "unknown command: $CMD"
    ;;
esac
