---
name: core-loans-docker
description: >-
  Run core-loans Python/Django commands (tests, migrations, manage.py scripts,
  isort, black, pytest) exclusively via Docker. Use automatically for any
  core-loans repo task involving tests, migrations, scripts, lint/format, or
  local validation — including worktrees under /data/code or /home/jesse/code.
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
5. **Default cleanup** — after each helper-script run, tear the compose stack
   back down so no core-loans containers remain running. Use `--keep-up` only
   when the user explicitly wants containers left up.

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

Copy this checklist and track progress:

```
- [ ] 1. Resolve repo path (checkout or /data/code/core-loans)
- [ ] 2. Resolve Danacita vs Bukas (default Danacita)
- [ ] 3. cd to repo root
- [ ] 4. Ensure stack is up (start if needed; record containers)
- [ ] 5. Run command via scripts/run.sh or docker compose exec
- [ ] 6. Tear the stack back down unless the user explicitly asked to keep it up
- [ ] 7. Report exit code and relevant output
```

### Step details

1. **Repo** — `cd` to the core-loans checkout root before any Docker command.
2. **Context** — default Danacita; see mapping table above.
3. **Preflight** — ensure stack is running:

```bash
docker compose $COMPOSE ps
docker compose $COMPOSE up -d   # if backend service is not up
```

4. **Run** — prefer the helper script from the OpenClaw workspace:

```bash
# From any directory; pass --repo if not inside the checkout
python3 .agents/skills/core-loans-docker/scripts/run.sh test loans.tests.test_foo --keepdb
python3 .agents/skills/core-loans-docker/scripts/run.sh migrate
python3 .agents/skills/core-loans-docker/scripts/run.sh manage makemigrations --check
python3 .agents/skills/core-loans-docker/scripts/run.sh exec python scripts/foo.py --arg
python3 .agents/skills/core-loans-docker/scripts/run.sh --context bukas test payments.tests.test_bar
python3 .agents/skills/core-loans-docker/scripts/run.sh isort path/to/file.py
python3 .agents/skills/core-loans-docker/scripts/run.sh black path/to/file.py
python3 .agents/skills/core-loans-docker/scripts/run.sh --keep-up migrate
```

Or build commands manually from repo root:

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

The helper script brings up the required services, runs the command, then
executes `docker compose down` by default on exit. Pass `--keep-up` only when
the user explicitly wants the containers to remain running after the command.

### Test guidance

- Prefer `--keepdb` for faster reruns when schema/migrations did not change.
- Omit `--keepdb` when migrations, test DB setup, or schema changes require a
  fresh database.
- Example: `scripts/run.sh test loans.tests.test_loan_approval --keepdb`

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
- The helper script should leave **no core-loans containers running** after it
  completes unless the user explicitly asked for `--keep-up`.
- Use `--keep-up` sparingly, and only when the user wants to inspect or reuse a
  live local stack.

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/run.sh` | Wrapper: repo/context resolution, stack up, docker exec |

Requires: Docker, `docker compose`, bash. No pip packages.

## Additional resources

- [reference.md](reference.md) — setup, pytest, translations, Celery, CI context
