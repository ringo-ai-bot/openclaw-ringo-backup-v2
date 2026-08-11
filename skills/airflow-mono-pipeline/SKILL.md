---
name: airflow-mono-pipeline
description: >-
  Operate Erudifi company Airflow (mono-pipeline) via the REST API at
  https://airflow.erudifi.com: list active DAGs, inspect DAG runs and task
  instances, read latest task logs, manually trigger DAG runs, clear/retry
  failed tasks, and pause/unpause DAGs. Includes a catalog of what each active
  DAG does. Use automatically for Airflow, DAG, pipeline, workflow, scheduler,
  task log, retry, rerun, mono-pipeline, or “what does this DAG do” questions.
---

# Airflow mono-pipeline

Operate the company Airflow deployment that runs DAGs from
`/data/code/mono-pipeline` using the Airflow 2.7.2 REST API.

## When to use

- List active / paused DAGs
- Explain what a DAG does (purpose, schedule, source) — use [DAGS.md](DAGS.md)
- Inspect latest DAG runs or task instance status
- Read task logs for a failed or recent run
- Manually trigger a DAG
- Clear / retry failed tasks for a DAG run
- Pause or unpause a DAG

## DAG catalog (preferred for “what does X do?”)

Before opening `/data/code/mono-pipeline`, look up the `dag_id` in
[DAGS.md](DAGS.md). It covers all Airflow `is_active=true` DAGs with purpose,
schedule, paused flag, source path, and tags.

- Start with the **Quick index (unpaused only)** for common operational DAGs
- Refresh when the catalog looks stale:
  `python3 .agents/skills/airflow-mono-pipeline/scripts/generate_dag_catalog.py`
- Still use `airflow_api.py` for live run state, logs, trigger, and pause

## Access control (required)

Before calling the helper, resolve the requester through `access-control.json`
and enforce the matching action in `access-actions.json`:

| Action | Who |
|---|---|
| `use_airflow_mono_pipeline_read` | Owner; Trusted (work-related) |
| `use_airflow_mono_pipeline_write` | **Owner only** |

- Read covers: health, dags list/get, runs list/get, tasks list/instances/logs
- Write covers: runs trigger, runs clear (retry), dags pause/unpause
- **Chat-only**, **Blocked**, unknown, or ambiguous identity: deny
- Trusted users may use read helpers but must never receive or inspect
  Airflow credentials. The script loads secrets internally.
- Write commands require `--confirm-write` on the CLI as an extra guard

## Configuration

| Item | Value |
|---|---|
| Airflow URL | `https://airflow.erudifi.com` |
| Airflow version | 2.7.2 |
| API prefix | `/api/v1` |
| Auth | HTTP Basic Auth |
| Username file | `~/.openclaw/secrets/airflow-api-username.txt` |
| Password file | `~/.openclaw/secrets/airflow-api-password.txt` |
| DAG source repo | `/data/code/mono-pipeline` |
| Host allowlist note | This OpenClaw host IP is allowlisted past Cloudflare Access |
| HTTP User-Agent | Helper uses `curl/8.5.0` (CF blocks default Python-urllib) |

Never print, log, or commit the username/password. Current credentials are a
temporary `admin` account — rotate to a dedicated API user when available.

## Workflow

```
- [ ] 1. Enforce access action (read vs write)
- [ ] 2. Identify dag_id (consult DAGS.md for purpose if explaining a DAG)
- [ ] 3. Run scripts/airflow_api.py for live status / logs / mutations
- [ ] 4. Summarize results; for logs, quote the failure cause
```

### Common commands

```bash
SCRIPT=.agents/skills/airflow-mono-pipeline/scripts/airflow_api.py

python3 $SCRIPT health
python3 $SCRIPT dags list --only-active --limit 50
python3 $SCRIPT dags get <dag_id>
python3 $SCRIPT runs list <dag_id> --limit 5
python3 $SCRIPT runs get <dag_id> <dag_run_id>
python3 $SCRIPT tasks list <dag_id>
python3 $SCRIPT tasks instances <dag_id> <dag_run_id>
python3 $SCRIPT tasks logs <dag_id> <dag_run_id> <task_id>

# Owner-only writes (require --confirm-write)
python3 $SCRIPT runs trigger <dag_id> --confirm-write
python3 $SCRIPT runs trigger <dag_id> --conf '{"key":"value"}' --confirm-write
python3 $SCRIPT runs clear <dag_id> <dag_run_id> --confirm-write
python3 $SCRIPT dags pause <dag_id> --confirm-write
python3 $SCRIPT dags unpause <dag_id> --confirm-write
```

## Intent mapping

| User ask | Command |
|---|---|
| What does DAG X do? | Read [DAGS.md](DAGS.md) entry for `X` |
| List active DAGs | `dags list --only-active` |
| Is DAG X paused? | `dags get X` → `is_paused` (or DAGS.md) |
| Latest runs for X | `runs list X --limit 5` |
| Why did X fail? | `runs list` → `tasks instances` → `tasks logs` on failed task |
| Start / trigger X | `runs trigger X --confirm-write` (Owner) |
| Retry / rerun failed tasks | `runs clear X <run_id> --confirm-write` (Owner) |
| Pause / unpause X | `dags pause\|unpause X --confirm-write` (Owner) |

## Safety rules

- Prefer read operations; ask before any write even for Owners when intent is unclear
- Always pass `--confirm-write` for mutations; never invent a bypass
- Do not dump full credentials or secret file contents
- For large log payloads, summarize the error and cite the key stack/log lines
- DAG code changes belong in `/data/code/mono-pipeline`, not via the API

## Scripts

| Script | Purpose |
|---|---|
| `scripts/airflow_api.py` | Authenticated Airflow REST CLI (stdlib only) |
| `scripts/generate_dag_catalog.py` | Regenerate [DAGS.md](DAGS.md) from live active DAGs |

## Additional resources

- [DAGS.md](DAGS.md) — purpose/schedule/source catalog for all active DAGs
- [reference.md](reference.md) — endpoint map and response tips
- DAG repo: `/data/code/mono-pipeline/dags/`
- Airflow 2.7 stable REST API:
  https://airflow.apache.org/docs/apache-airflow/2.7.2/stable-rest-api-ref.html
