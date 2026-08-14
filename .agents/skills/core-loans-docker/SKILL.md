---
name: core-loans-docker
description: >-
  Run core-loans Python/Django commands (tests, migrations, manage.py scripts,
  isort, black, pytest) exclusively via Docker. Use automatically for any
  core-loans repo task involving tests, migrations, scripts, lint/format, or
  local validation — including worktrees under /data/code or /home/jesse/code.
  For multi-step ticket validation, keep the stack warm with --keep-up / --no-up
  and run focused tests with --keepdb to avoid slow cold starts and busy-wait polls.
---

# core-loans Docker

Run **all** core-loans Python/Django operations inside Docker backend
containers. Never invoke `./manage.py`, `python`, `pytest`, `pip`, `isort`, or
`black` directly on the host inside a core-loans checkout.

For read-only lending analytics, use `metabase-core-loans` instead.

## When to use

- Running unit tests or focused test files
- Applying or checking migrations
- Executing one-off Python scripts or Django management commands
- Formatting/linting changed files before commit
- Local validation during Linear ticket work on `core-loans`

## Hard rules

1. **Docker only** — all commands below run via `docker compose exec` (or the
   helper script). Do not use host Python in the repo.
2. **Repo resolution** — use the active checkout
   (`git rev-parse --show-toplevel`). Worktrees (e.g.
   `/data/code/core-loans-oi-2974`) use their own directory. If ambiguous,
   default to `/data/code/core-loans` per `EPD_CODEBASES.md`.
3. **Context** — default **Danacita**. Use Bukas only when the task is
   PH-specific or the user requests it.
4. **Local only** — migrations and tests target the local Docker Postgres. Never
   run against staging or production databases.
5. **Stack lifecycle** —
   - **One-shot** command (single migrate/format/test, then done): default
     helper behavior is fine (up → run → `docker compose down`).
   - **Multi-step validation** (Linear ticket, iterative test/fix loops):
     keep the stack warm with `--keep-up` for the session; use `--no-up` on
     follow-up commands; tear down once at the end. Do **not** pay cold-start
     cost on every test rerun.

## Context mapping

| Context | Compose file | Backend service | API port |
|---------|--------------|-----------------|----------|
| **Danacita** (default) | `docker-compose.danacita.yml` | `backend_danacita` | 8001 |
| Bukas | `docker-compose.bukas.yml` | `backend` | 8000 |
| Both countries | `docker-compose.yml` | pick per command | 8000 / 8001 |

Set once per session (Danacita default):

```bash
COMPOSE="-f docker-compose.danacita.yml"
BACKEND=backend_danacita
```

For Bukas:

```bash
COMPOSE="-f docker-compose.bukas.yml"
BACKEND=backend
```

## Workflow

### A. Multi-step ticket / iterative validation (preferred when testing more than once)

Copy this checklist and track progress:

```
- [ ] 1. Resolve repo path (worktree or /data/code/core-loans)
- [ ] 2. Resolve Danacita vs Bukas (default Danacita)
- [ ] 3. Warm the stack once with --keep-up up
- [ ] 4. Run focused commands with --keep-up --no-up (and --keepdb for tests)
- [ ] 5. Prefer the narrowest test path (module.Class.method)
- [ ] 6. Wait with one blocking exec or a single long process.poll — never timeout:0 spam
- [ ] 7. Tear the stack down once when validation is finished
- [ ] 8. Report exit code and relevant output
```

Warm once, then reuse:

```bash
SCRIPT=~/.openclaw/workspace/skills/core-loans-docker/scripts/run.sh
REPO=/data/code/.worktrees/core-loans-<issue-id-kebab>   # or active checkout

# 1) Bring stack up and leave it running
bash "$SCRIPT" --repo "$REPO" --keep-up up

# 2) Fast reruns (no compose up/down)
bash "$SCRIPT" --repo "$REPO" --keep-up --no-up \
  test tests.loans.test_foo.TestClass.test_method --keepdb

bash "$SCRIPT" --repo "$REPO" --keep-up --no-up \
  manage makemigrations --check

bash "$SCRIPT" --repo "$REPO" --keep-up --no-up \
  isort path/to/file.py

# 3) Tear down once when done (omit --keep-up on a final throwaway command,
#    or compose down explicitly)
docker compose -f docker-compose.danacita.yml --project-directory "$REPO" down
```

### B. One-shot command

```
- [ ] 1. Resolve repo path
- [ ] 2. Resolve Danacita vs Bukas (default Danacita)
- [ ] 3. Run via scripts/run.sh (default: up → command → down)
- [ ] 4. Report exit code and relevant output
```

```bash
bash ~/.openclaw/workspace/skills/core-loans-docker/scripts/run.sh \
  --repo "$REPO" test loans.tests.test_foo --keepdb
```

### Step details

1. **Repo** — `cd` to the core-loans checkout root before any Docker command, or
   pass `--repo`.
2. **Context** — default Danacita; see mapping table above.
3. **Preflight** — for multi-step work, warm with `--keep-up up` first. For
   one-shot, the helper brings the stack up automatically.
4. **Run** — prefer the helper script from the OpenClaw workspace:

```bash
SCRIPT=~/.openclaw/workspace/skills/core-loans-docker/scripts/run.sh

# One-shot (tears down after)
bash "$SCRIPT" --repo "$REPO" test loans.tests.test_foo --keepdb
bash "$SCRIPT" --repo "$REPO" migrate
bash "$SCRIPT" --repo "$REPO" manage makemigrations --check
bash "$SCRIPT" --repo "$REPO" exec python scripts/foo.py --arg
bash "$SCRIPT" --repo "$REPO" --context bukas test payments.tests.test_bar
bash "$SCRIPT" --repo "$REPO" isort path/to/file.py
bash "$SCRIPT" --repo "$REPO" black path/to/file.py

# Multi-step session (warm stack)
bash "$SCRIPT" --repo "$REPO" --keep-up up
bash "$SCRIPT" --repo "$REPO" --keep-up --no-up test loans.tests.test_foo --keepdb
bash "$SCRIPT" --repo "$REPO" --keep-up --no-up migrate
```

Or build commands manually from repo root (stack already up):

```bash
docker compose $COMPOSE exec -T $BACKEND ./manage.py migrate
docker compose $COMPOSE exec -T $BACKEND ./manage.py makemigrations --check
docker compose $COMPOSE exec -T $BACKEND ./manage.py test {test_path} --keepdb
docker compose $COMPOSE exec -T $BACKEND isort {files}
docker compose $COMPOSE exec -T $BACKEND black {files}
docker compose $COMPOSE exec -T $BACKEND python {script_path} {args}
```

Use `-T` (no TTY) for non-interactive agent runs. Omit `-T` only for interactive
shell debugging.

Without `--keep-up`, the helper brings up required services, runs the command,
then executes `docker compose down`. That cold start/teardown cycle is expensive;
avoid it during iterative validation.

### Test guidance (efficiency)

- **Narrowest target first** — prefer
  `app.tests.test_mod.TestClass.test_method` over a whole module or the full
  suite. Widen only after the focused case passes or when acceptance criteria
  require broader coverage.
- Prefer **`--keepdb`** for faster reruns when schema/migrations did not change.
- Omit `--keepdb` when migrations, test DB setup, or schema changes require a
  fresh database.
- During a ticket session: **`--keep-up` + `--no-up` + `--keepdb`** for every
  test rerun after the first warm-up.
- Do **not** start OpenCode, full-suite tests, and migration checks as many
  overlapping background sessions unless the user asked for parallel work.
- **Waiting on long commands** — prefer one blocking `exec` that runs to
  completion, or a single `process` poll/log with a real wait timeout
  (tens of seconds). Never spam `process.poll` with `timeout: 0` every few
  seconds (that burns model turns without speeding up Docker/tests).
- Example focused rerun:

```bash
bash "$SCRIPT" --repo "$REPO" --keep-up --no-up \
  test tests.loans.test_coordination_dashboard.SomeTest.test_revision_required --keepdb
```

### Host exception

One command runs on the **host** per repo README:

```bash
python scripts/init_minio.py bukas|danacita|main
```

Run from repo root after starting the matching Docker stack.

## Pre-commit gotcha

core-loans pre-commit includes a local hook:

```yaml
entry: docker exec backend ./manage.py makemigrations --check
```

This requires the **Bukas `backend`** container (from `docker-compose.bukas.yml`
or full `docker-compose.yml`) to be running — even for Danacita-focused work.
Before committing in core-loans, ensure that container is up:

```bash
docker compose -f docker-compose.bukas.yml up -d backend
```

Use `core-loans-docker` for formatters (`isort`, `black`) inside the appropriate
backend container before running pre-commit.

## Safety rules

- Migrations and tests: **local Docker only**. Never staging/production.
- One-shot helper runs should leave **no** core-loans containers running after
  they complete (default tear-down).
- Multi-step sessions **should** leave the stack up until validation finishes,
  then tear down once. Record workflow-owned containers; do not stop shared or
  pre-existing stacks you did not start.
- Never leave a forgotten stack running across unrelated sessions; clean up at
  end of the ticket workflow.

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/run.sh` | Wrapper: repo/context resolution, stack up, docker exec |

Requires: Docker, `docker compose`, bash. No pip packages.

## Additional resources

- [reference.md](reference.md) — setup, pytest, translations, Celery, CI context
