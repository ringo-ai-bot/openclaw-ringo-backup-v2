#!/usr/bin/env python3
"""Erudifi Airflow REST helper (mono-pipeline / airflow.erudifi.com)."""

from __future__ import annotations

import argparse
import base64
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

AIRFLOW_URL = "https://airflow.erudifi.com"
API_PREFIX = "/api/v1"
USERNAME_PATH = Path.home() / ".openclaw" / "secrets" / "airflow-api-username.txt"
PASSWORD_PATH = Path.home() / ".openclaw" / "secrets" / "airflow-api-password.txt"


def load_secret(path: Path, label: str) -> str:
    if not path.is_file():
        raise SystemExit(f"{label} file not found: {path}")
    value = path.read_text(encoding="utf-8").strip()
    if not value:
        raise SystemExit(f"{label} file is empty: {path}")
    return value


def basic_auth_header(username: str, password: str) -> str:
    token = base64.b64encode(f"{username}:{password}".encode("utf-8")).decode("ascii")
    return f"Basic {token}"


def emit(data: Any) -> None:
    json.dump(data, sys.stdout, indent=2, default=str)
    sys.stdout.write("\n")


def request(
    method: str,
    path: str,
    *,
    query: dict[str, Any] | None = None,
    body: dict[str, Any] | None = None,
    auth: bool = True,
    accept: str = "application/json",
) -> Any:
    qs = ""
    if query:
        filtered: dict[str, Any] = {}
        for k, v in query.items():
            if v is None or v == "" or v == []:
                continue
            if isinstance(v, bool):
                filtered[k] = str(v).lower()
            elif isinstance(v, list):
                filtered[k] = v
            else:
                filtered[k] = v
        qs = "?" + urllib.parse.urlencode(filtered, doseq=True) if filtered else ""

    url = f"{AIRFLOW_URL}{path}{qs}"
    headers = {
        "Accept": accept,
        # Cloudflare blocks Python-urllib default UA (error 1010).
        "User-Agent": "curl/8.5.0",
    }
    data = None
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"
    if auth:
        username = load_secret(USERNAME_PATH, "Airflow API username")
        password = load_secret(PASSWORD_PATH, "Airflow API password")
        headers["Authorization"] = basic_auth_header(username, password)

    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            raw = resp.read()
            if not raw:
                return {"status": resp.status, "ok": True}
            text = raw.decode("utf-8", errors="replace")
            ctype = resp.headers.get("Content-Type", "")
            if "application/json" in ctype or text.lstrip()[:1] in ("{", "["):
                try:
                    return json.loads(text)
                except json.JSONDecodeError:
                    pass
            return {"content": text, "status": resp.status, "content_type": ctype}
    except urllib.error.HTTPError as exc:
        err_body = exc.read().decode("utf-8", errors="replace")
        try:
            parsed = json.loads(err_body) if err_body else {}
        except json.JSONDecodeError:
            parsed = {"raw": err_body}
        emit(
            {
                "error": True,
                "status": exc.code,
                "method": method,
                "path": path,
                "detail": parsed,
            }
        )
        raise SystemExit(1) from None
    except urllib.error.URLError as exc:
        emit({"error": True, "message": str(exc.reason)})
        raise SystemExit(1) from None


def cmd_health(_: argparse.Namespace) -> None:
    # Prefer authenticated API version + unauthenticated /health summary.
    version = request("GET", f"{API_PREFIX}/version")
    try:
        health = request("GET", "/health", auth=False)
    except SystemExit:
        health = request("GET", f"{API_PREFIX}/health")
    emit({"version": version, "health": health})


def cmd_dags_list(args: argparse.Namespace) -> None:
    query: dict[str, Any] = {
        "limit": args.limit,
        "offset": args.offset,
        "dag_id_pattern": args.pattern,
        "tags": args.tag,
    }
    if args.only_active:
        query["only_active"] = True
    if args.paused is not None:
        query["paused"] = args.paused
    emit(request("GET", f"{API_PREFIX}/dags", query=query))


def cmd_dags_get(args: argparse.Namespace) -> None:
    dag_id = urllib.parse.quote(args.dag_id, safe="")
    emit(request("GET", f"{API_PREFIX}/dags/{dag_id}"))


def cmd_dags_set_paused(args: argparse.Namespace, paused: bool) -> None:
    require_confirm_write(args)
    dag_id = urllib.parse.quote(args.dag_id, safe="")
    emit(
        request(
            "PATCH",
            f"{API_PREFIX}/dags/{dag_id}",
            body={"is_paused": paused},
        )
    )


def cmd_runs_list(args: argparse.Namespace) -> None:
    dag_id = urllib.parse.quote(args.dag_id, safe="")
    query: dict[str, Any] = {
        "limit": args.limit,
        "offset": args.offset,
        "order_by": args.order_by,
        "state": args.state,
    }
    emit(request("GET", f"{API_PREFIX}/dags/{dag_id}/dagRuns", query=query))


def cmd_runs_get(args: argparse.Namespace) -> None:
    dag_id = urllib.parse.quote(args.dag_id, safe="")
    run_id = urllib.parse.quote(args.dag_run_id, safe="")
    emit(request("GET", f"{API_PREFIX}/dags/{dag_id}/dagRuns/{run_id}"))


def cmd_runs_trigger(args: argparse.Namespace) -> None:
    require_confirm_write(args)
    dag_id = urllib.parse.quote(args.dag_id, safe="")
    body: dict[str, Any] = {"conf": {}}
    if args.conf:
        try:
            conf = json.loads(args.conf)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"Invalid --conf JSON: {exc}") from exc
        if not isinstance(conf, dict):
            raise SystemExit("--conf must be a JSON object")
        body["conf"] = conf
    if args.dag_run_id:
        body["dag_run_id"] = args.dag_run_id
    if args.logical_date:
        body["logical_date"] = args.logical_date
    if args.note:
        body["note"] = args.note
    emit(request("POST", f"{API_PREFIX}/dags/{dag_id}/dagRuns", body=body))


def cmd_runs_clear(args: argparse.Namespace) -> None:
    require_confirm_write(args)
    dag_id = urllib.parse.quote(args.dag_id, safe="")
    body: dict[str, Any] = {
        "dry_run": False,
        "reset_dag_runs": True,
        "only_failed": args.only_failed,
        "only_running": False,
        "include_subdags": True,
        "include_upstream": False,
        "include_downstream": False,
        "include_future": False,
        "include_past": False,
        "dag_run_id": args.dag_run_id,
    }
    if args.task_ids:
        body["task_ids"] = args.task_ids
    emit(request("POST", f"{API_PREFIX}/dags/{dag_id}/clearTaskInstances", body=body))


def cmd_tasks_list(args: argparse.Namespace) -> None:
    dag_id = urllib.parse.quote(args.dag_id, safe="")
    emit(request("GET", f"{API_PREFIX}/dags/{dag_id}/tasks"))


def cmd_tasks_instances(args: argparse.Namespace) -> None:
    dag_id = urllib.parse.quote(args.dag_id, safe="")
    run_id = urllib.parse.quote(args.dag_run_id, safe="")
    query: dict[str, Any] = {"limit": args.limit, "offset": args.offset}
    if args.state:
        query["state"] = args.state
    emit(
        request(
            "GET",
            f"{API_PREFIX}/dags/{dag_id}/dagRuns/{run_id}/taskInstances",
            query=query,
        )
    )


def cmd_tasks_logs(args: argparse.Namespace) -> None:
    dag_id = urllib.parse.quote(args.dag_id, safe="")
    run_id = urllib.parse.quote(args.dag_run_id, safe="")
    task_id = urllib.parse.quote(args.task_id, safe="")
    try_number = args.try_number
    if try_number is None:
        ti = request(
            "GET",
            f"{API_PREFIX}/dags/{dag_id}/dagRuns/{run_id}/taskInstances/{task_id}",
        )
        try_number = ti.get("try_number")
    # Airflow rejects try_number 0 for log fetch; treat as 1.
    if not try_number or int(try_number) < 1:
        try_number = 1
    emit(
        request(
            "GET",
            f"{API_PREFIX}/dags/{dag_id}/dagRuns/{run_id}/taskInstances/{task_id}/logs/{try_number}",
            query={"full_content": "true"},
            accept="*/*",
        )
    )


def require_confirm_write(args: argparse.Namespace) -> None:
    if not getattr(args, "confirm_write", False):
        raise SystemExit(
            "Refusing write operation without --confirm-write "
            "(Owner-only: trigger / clear / pause / unpause)."
        )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Erudifi Airflow API helper for mono-pipeline (airflow.erudifi.com)."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_health = sub.add_parser("health", help="Airflow version + health")
    p_health.set_defaults(func=cmd_health)

    p_dags = sub.add_parser("dags", help="DAG operations")
    dags_sub = p_dags.add_subparsers(dest="dags_command", required=True)

    p_dags_list = dags_sub.add_parser("list", help="List DAGs")
    p_dags_list.add_argument("--limit", type=int, default=100)
    p_dags_list.add_argument("--offset", type=int, default=0)
    p_dags_list.add_argument("--only-active", action="store_true")
    p_dags_list.add_argument(
        "--paused",
        choices=["true", "false"],
        default=None,
        help="Filter by paused state",
    )
    p_dags_list.add_argument("--pattern", help="dag_id_pattern filter")
    p_dags_list.add_argument("--tag", action="append", default=None)
    p_dags_list.set_defaults(func=cmd_dags_list)

    p_dags_get = dags_sub.add_parser("get", help="Get one DAG")
    p_dags_get.add_argument("dag_id")
    p_dags_get.set_defaults(func=cmd_dags_get)

    p_dags_pause = dags_sub.add_parser("pause", help="Pause a DAG (write)")
    p_dags_pause.add_argument("dag_id")
    p_dags_pause.add_argument("--confirm-write", action="store_true")
    p_dags_pause.set_defaults(func=lambda a: cmd_dags_set_paused(a, True))

    p_dags_unpause = dags_sub.add_parser("unpause", help="Unpause a DAG (write)")
    p_dags_unpause.add_argument("dag_id")
    p_dags_unpause.add_argument("--confirm-write", action="store_true")
    p_dags_unpause.set_defaults(func=lambda a: cmd_dags_set_paused(a, False))

    p_runs = sub.add_parser("runs", help="DAG run operations")
    runs_sub = p_runs.add_subparsers(dest="runs_command", required=True)

    p_runs_list = runs_sub.add_parser("list", help="List DAG runs")
    p_runs_list.add_argument("dag_id")
    p_runs_list.add_argument("--limit", type=int, default=10)
    p_runs_list.add_argument("--offset", type=int, default=0)
    p_runs_list.add_argument("--order-by", default="-start_date")
    p_runs_list.add_argument("--state", action="append", default=None)
    p_runs_list.set_defaults(func=cmd_runs_list)

    p_runs_get = runs_sub.add_parser("get", help="Get one DAG run")
    p_runs_get.add_argument("dag_id")
    p_runs_get.add_argument("dag_run_id")
    p_runs_get.set_defaults(func=cmd_runs_get)

    p_runs_trigger = runs_sub.add_parser("trigger", help="Trigger a DAG run (write)")
    p_runs_trigger.add_argument("dag_id")
    p_runs_trigger.add_argument("--conf", default=None, help='JSON object, e.g. \'{"k":"v"}\'')
    p_runs_trigger.add_argument("--dag-run-id", default=None)
    p_runs_trigger.add_argument("--logical-date", default=None)
    p_runs_trigger.add_argument("--note", default=None)
    p_runs_trigger.add_argument("--confirm-write", action="store_true")
    p_runs_trigger.set_defaults(func=cmd_runs_trigger)

    p_runs_clear = runs_sub.add_parser(
        "clear", help="Clear/retry task instances for a DAG run (write)"
    )
    p_runs_clear.add_argument("dag_id")
    p_runs_clear.add_argument("dag_run_id")
    p_runs_clear.add_argument(
        "--only-failed",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Clear only failed tasks (default: true)",
    )
    p_runs_clear.add_argument("--task-id", dest="task_ids", action="append", default=None)
    p_runs_clear.add_argument("--confirm-write", action="store_true")
    p_runs_clear.set_defaults(func=cmd_runs_clear)

    p_tasks = sub.add_parser("tasks", help="Task operations")
    tasks_sub = p_tasks.add_subparsers(dest="tasks_command", required=True)

    p_tasks_list = tasks_sub.add_parser("list", help="List tasks in a DAG")
    p_tasks_list.add_argument("dag_id")
    p_tasks_list.set_defaults(func=cmd_tasks_list)

    p_tasks_instances = tasks_sub.add_parser(
        "instances", help="List task instances for a DAG run"
    )
    p_tasks_instances.add_argument("dag_id")
    p_tasks_instances.add_argument("dag_run_id")
    p_tasks_instances.add_argument("--limit", type=int, default=100)
    p_tasks_instances.add_argument("--offset", type=int, default=0)
    p_tasks_instances.add_argument("--state", action="append", default=None)
    p_tasks_instances.set_defaults(func=cmd_tasks_instances)

    p_tasks_logs = tasks_sub.add_parser("logs", help="Fetch task logs")
    p_tasks_logs.add_argument("dag_id")
    p_tasks_logs.add_argument("dag_run_id")
    p_tasks_logs.add_argument("task_id")
    p_tasks_logs.add_argument(
        "--try-number",
        type=int,
        default=None,
        help="Defaults to the task instance try_number",
    )
    p_tasks_logs.set_defaults(func=cmd_tasks_logs)

    return parser


def normalize_paused(args: argparse.Namespace) -> None:
    if getattr(args, "paused", None) is not None:
        args.paused = args.paused == "true"


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    normalize_paused(args)
    args.func(args)


if __name__ == "__main__":
    main()
