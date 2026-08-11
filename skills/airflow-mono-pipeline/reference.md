# Airflow mono-pipeline API reference

Company Airflow: `https://airflow.erudifi.com` (Apache Airflow **2.7.2**).
Helper: `scripts/airflow_api.py` (Basic Auth from `~/.openclaw/secrets/airflow-api-*.txt`).

## Auth layers

1. **Cloudflare Access** — this OpenClaw host (`20.195.24.194`) is IP-allowlisted.
2. **Airflow Basic Auth** — username/password secret files; required for `/api/v1/*`
   except some public health endpoints.

OAuth (Google) applies to the Web UI only, not the REST API.

The helper sets `User-Agent: curl/8.5.0` because Cloudflare blocks the default
Python-urllib signature (error 1010).

## Helper → REST map

| Helper command | Method | Path |
|---|---|---|
| `health` | GET | `/api/v1/version` + `/health` |
| `dags list` | GET | `/api/v1/dags` |
| `dags get <dag_id>` | GET | `/api/v1/dags/{dag_id}` |
| `dags pause <dag_id>` | PATCH | `/api/v1/dags/{dag_id}` `{"is_paused": true}` |
| `dags unpause <dag_id>` | PATCH | `/api/v1/dags/{dag_id}` `{"is_paused": false}` |
| `runs list <dag_id>` | GET | `/api/v1/dags/{dag_id}/dagRuns` |
| `runs get <dag_id> <run_id>` | GET | `/api/v1/dags/{dag_id}/dagRuns/{dag_run_id}` |
| `runs trigger <dag_id>` | POST | `/api/v1/dags/{dag_id}/dagRuns` |
| `runs clear <dag_id> <run_id>` | POST | `/api/v1/dags/{dag_id}/clearTaskInstances` |
| `tasks list <dag_id>` | GET | `/api/v1/dags/{dag_id}/tasks` |
| `tasks instances <dag_id> <run_id>` | GET | `/api/v1/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances` |
| `tasks logs <dag_id> <run_id> <task_id>` | GET | `/api/v1/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/logs/{try_number}` |

Write helpers require `--confirm-write`.

## Useful list filters

`dags list`:

- `--only-active` → `only_active=true`
- `--paused true|false`
- `--pattern <glob-ish>` → `dag_id_pattern`
- `--tag <tag>` (repeatable)
- `--limit` / `--offset`

`runs list`:

- `--limit` (default 10)
- `--order-by -start_date` (default)
- `--state failed` (repeatable)

## Clear / retry semantics

`runs clear` posts to `clearTaskInstances` with:

- `dag_run_id` set to the target run
- `reset_dag_runs: true`
- `only_failed: true` by default (`--no-only-failed` clears more broadly)
- optional repeated `--task-id` to limit which tasks clear

This is the Airflow 2.7 equivalent of “retry failed tasks for this run.”

## Inspect-failure playbook

1. `runs list <dag_id> --limit 5 --state failed` (or latest runs without state filter)
2. Pick `dag_run_id`
3. `tasks instances <dag_id> <dag_run_id>` — find `state=failed`
4. `tasks logs <dag_id> <dag_run_id> <task_id>` — summarize root cause
5. Owner: `runs clear ... --confirm-write` if a retry is requested

## DAG source layout

Repo: `/data/code/mono-pipeline`

- Active DAG Python files: `dags/*.py` (plus subfolders)
- Google Sheet ingest DAGs: `dags/gsheet_raw/`
- SQL/assets: `dags/query/`
- Archived: `dags/archived/`
- Infra/Helm notes: `.infrastructure/airflow/helm/airflow-dev-values.yaml`

`dag_id` usually matches the Python filename stem (shared files may define
multiple DAG IDs — see [DAGS.md](DAGS.md)).

For purpose/schedule of each **active** DAG without reading the repo, use
[DAGS.md](DAGS.md). Refresh with `scripts/generate_dag_catalog.py`.

## Error shapes

The helper prints JSON and exits non-zero on HTTP errors:

```json
{
  "error": true,
  "status": 401,
  "method": "GET",
  "path": "/api/v1/dags",
  "detail": { "...": "..." }
}
```

| Status | Likely cause |
|---|---|
| 401 | Bad/missing Basic Auth secrets |
| 403 HTML Cloudflare Access | Host IP no longer allowlisted |
| 404 | Wrong `dag_id` / `dag_run_id` / `task_id` |
| 409 | Trigger conflict (duplicate run id) |

## Credential rotation

Overwrite the secret files (one line each, no quotes), then `chmod 600`:

- `~/.openclaw/secrets/airflow-api-username.txt`
- `~/.openclaw/secrets/airflow-api-password.txt`

Prefer a dedicated Airflow RBAC user instead of shared `admin` when possible.
