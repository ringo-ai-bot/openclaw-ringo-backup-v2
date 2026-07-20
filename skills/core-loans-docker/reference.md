# core-loans Docker reference

Detailed commands and setup notes. For day-to-day work, start with
[SKILL.md](SKILL.md).

## First-time setup

From repo root (`/data/code/core-loans` or a worktree):

```bash
cp .example.env .docker.env
cp .env.danacita.example .env.danacita
cp ./.secrets/gcp-creds.json.example ./.secrets/gcp-creds.json
cp aws-creds-danacita.json.example .secrets/aws-creds.json   # Danacita
# or aws-creds-bukas.json.example for Bukas
```

Start stack (pick one):

```bash
docker compose -f docker-compose.danacita.yml up -d   # Danacita only
docker compose -f docker-compose.bukas.yml up -d      # Bukas only
docker compose up -d                                   # both (RAM-heavy)
```

Initialize MinIO buckets (host, after stack is up):

```bash
python scripts/init_minio.py danacita   # or bukas | main
```

Run migrations and create superuser inside container:

```bash
scripts/run.sh migrate
scripts/run.sh manage createsuperuser
```

### Postgres 17 volume note

Compose uses Postgres 17. If upgrading from an older Postgres 13 volume, remove
the disposable `postgres_volume` or migrate data before restarting.

## API endpoints (local)

| Context | URL |
|---------|-----|
| Danacita | http://localhost:8001, http://api.danacita.localhost |
| Bukas | http://localhost:8000, http://api.bukas.localhost |

Add to `/etc/hosts` if needed:

```
127.0.0.1 api.bukas.localhost
127.0.0.1 api.danacita.localhost
```

## Tests

### Django test runner (default)

```bash
scripts/run.sh test                                    # full suite
scripts/run.sh test loans.tests.test_loan_approval --keepdb
scripts/run.sh test -v2 --failfast loans.tests.test_foo
```

Use `--keepdb` unless migrations or test DB setup changed.

### pytest + xdist (experimental, inside container)

```bash
scripts/run.sh pytest -n 6
scripts/run.sh pytest --duration 20
```

Note: concurrency and duration profiling do not combine well.

## Migrations

```bash
scripts/run.sh migrate
scripts/run.sh manage makemigrations
scripts/run.sh manage makemigrations --check
scripts/run.sh manage makemigrations --dry-run --check
scripts/run.sh manage sqlflush
```

## Formatting and lint

```bash
scripts/run.sh isort path/to/file.py
scripts/run.sh black path/to/file.py
```

Pre-commit (host) runs isort, black, flake8, and a Docker makemigrations check.
See SKILL.md for the Bukas `backend` container requirement.

## Translations

```bash
scripts/run.sh manage makemessages -e 'html,txt,py,sms,email' --all
scripts/run.sh manage compilemessages
```

## Celery workers

View logs for background workers:

```bash
docker compose -f docker-compose.danacita.yml logs -f worker_danacita
docker compose -f docker-compose.danacita.yml logs -f beat_danacita
docker compose -f docker-compose.bukas.yml logs -f worker
```

## MinIO ports by compose file

| Compose file | API | Console |
|--------------|-----|---------|
| docker-compose.danacita.yml | 9020 | 9021 |
| docker-compose.bukas.yml | 9040 | 9041 |
| docker-compose.yml | 9030 | 9031 |

Login: `minio` / `minio123`

## CI context (reference only)

GitHub Actions (`.github/workflows/main.yml`) runs natively on Python 3.11, not
Docker:

| Job | Commands |
|-----|----------|
| lint | `black --check .`, `isort --check .` |
| migration_check | `makemigrations --dry-run --check`, `migrate`, `sqlflush` |
| test_1–test_4 | `./manage.py test -v2 --failfast <app packages>` (split) |

Local validation should still use Docker per SKILL.md.

## Adding dependencies

Inside container:

```bash
scripts/run.sh exec pip install <package>
scripts/run.sh exec pip freeze | grep <package>   # pin in requirements.txt
```

Rebuild image if Dockerfile dependencies change.

## Troubleshooting

| Problem | Action |
|---------|--------|
| Backend not running | `scripts/run.sh up` or `docker compose -f ... up -d` |
| Test DB stale after migration | rerun tests without `--keepdb` |
| pre-commit makemigrations fails | start Bukas `backend`: `docker compose -f docker-compose.bukas.yml up -d backend` |
| Wrong country context | pass `--context bukas` or `--context danacita` |
| Worktree path | pass `--repo /path/to/worktree` |
