#!/usr/bin/env python3
"""Generate DAGS.md for active Airflow DAGs (mono-pipeline).

Fetches is_active=true DAGs from the company Airflow API, enriches with local
source hints under /data/code/mono-pipeline, and writes DAGS.md next to SKILL.md.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parents[1]
AIRFLOW_API = SKILL_DIR / "scripts" / "airflow_api.py"
REPO_ROOT = Path("/data/code/mono-pipeline")
DAGS_ROOT = REPO_ROOT / "dags"
OUT_PATH = SKILL_DIR / "DAGS.md"

PURPOSE_OVERRIDES = {
    "airflow_monitoring": "Composer/Airflow liveness prober for environment health.",
    "athena_borrower_base": "Rebuilds Athena Iceberg `summaries.borrower_base` daily (write-truncate) from datamart SQL.",
    "athena_borrower_demography": "Rebuilds Athena Iceberg `summaries.borrower_demography` daily from datamart SQL.",
    "athena_summaries_daily_update": "Daily write-truncate rebuild of many Athena `summaries` tables (lenders, collections, growth, portfolio_daily_update, projections, etc.).",
    "athena_saved_queries_sync_to_variables": "Syncs Athena named/saved queries into Airflow Variables (`athena_sql_*`) to reduce API throttling.",
    "athena_pusdafil_report_am": "Morning Pusdafil regulatory report build into Athena `reports` (Athena + BigQuery operators).",
    "athena_pusdafil_report_pm": "Evening Pusdafil regulatory report build into Athena `reports` (Athena + BigQuery operators).",
    "athena_daily_loanbook_id": "Builds daily Danacita ID loanbook snapshot in Athena `summaries` (can trigger cash-on-cash).",
    "athena_daily_loanbook_ph": "Builds daily Bukas/PH loanbook snapshot in Athena `summaries`.",
    "daily_raw_bukas": "Daily raw Bukas ingest orchestration (lakehouse/GCS path).",
    "daily_raw_dc": "Daily raw Danacita ingest orchestration (lakehouse/GCS path).",
    "daily_slik_closed_loans": "Daily SLIK closed-loans extract into Athena `reports` with Slack notify.",
    "monthly_slik_active_loans": "Monthly SLIK active-loans report into Athena `reports` with Slack notify.",
    "bukas_parquet_to_iceberg": "Loads Bukas Parquet into Athena Iceberg tables.",
    "parquet_to_iceberg": "Manual Parquet→Athena Iceberg load for core tables.",
    "erudifi_data_governance": "Hourly data-governance SQL checks in BigQuery (`query/gov/*`) with Slack notify.",
}

GROUP_ORDER = [
    "Athena / datamart & summaries",
    "Athena / Bukas",
    "Athena / OJK & Pusdafil",
    "Daily facts / BigQuery layer & other",
    "Accounting / finance",
    "BigQuery ↔ Parquet ↔ Iceberg",
    "Gsheet raw → Athena integrated",
    "OJK / Pusdafil / SLIK (BQ & reports)",
    "Bukas & Danacita raw ingest",
    "Partner feeds",
    "Core ETL / governance / monitoring",
    "Archived (still active in Airflow)",
]


def fetch_active_dags() -> list[dict]:
    offset = 0
    limit = 100
    all_dags: list[dict] = []
    while True:
        out = subprocess.check_output(
            [
                sys.executable,
                str(AIRFLOW_API),
                "dags",
                "list",
                "--only-active",
                "--limit",
                str(limit),
                "--offset",
                str(offset),
            ],
            text=True,
        )
        data = json.loads(out)
        batch = data.get("dags") or []
        all_dags.extend(batch)
        total = data.get("total_entries", len(all_dags))
        offset += limit
        if offset >= total or not batch:
            break
    return all_dags


def schedule_str(sched) -> str:
    if sched is None:
        return "None (manual / no schedule)"
    if isinstance(sched, dict):
        if sched.get("__type") == "CronExpression":
            return f"`{sched.get('value')}`"
        return json.dumps(sched)
    return str(sched)


def to_local(fileloc: str | None) -> Path | None:
    if not fileloc:
        return None
    m = re.search(r"/dags/repo/dags/(.+)$", fileloc)
    if m:
        p = DAGS_ROOT / m.group(1)
        return p if p.is_file() else None
    m = re.search(r"/dags/(.+)$", fileloc)
    if m:
        p = DAGS_ROOT / m.group(1)
        return p if p.is_file() else None
    return None


def extract_hints(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    hints: dict = {}
    m = re.match(r'\s*"""(.*?)"""', text, re.S)
    if m:
        hints["module_doc"] = " ".join(m.group(1).strip().split())[:300]
    m = re.search(r'SQL_PATH\s*=\s*f?["\']([^"\']+)["\']', text)
    if m:
        hints["sql_path"] = m.group(1)
    for key in ("ATHENA_DB", "ATHENA_DATABASE"):
        m = re.search(rf'{key}\s*=\s*["\']([^"\']+)["\']', text)
        if m:
            hints["athena_db"] = m.group(1)
    m = re.search(r'description\s*=\s*["\']([^"\']+)["\']', text)
    if m:
        hints["dag_description"] = m.group(1)[:300]
    m = re.search(r'ICEBERG_TABLE\s*=\s*["\']([^"\']+)["\']', text)
    if m:
        hints["iceberg_table"] = m.group(1)
    tables = re.findall(r"\b(?:summaries|integrated|reports|raw)\.[a-zA-Z0-9_]+\b", text)
    if tables:
        hints["tables"] = sorted(set(tables))[:8]
    return hints


def enrich(dags: list[dict]) -> list[dict]:
    rows = []
    for d in dags:
        local = to_local(d.get("fileloc"))
        tags = [
            t.get("name") if isinstance(t, dict) else t for t in (d.get("tags") or [])
        ]
        row = {
            "dag_id": d.get("dag_id"),
            "is_paused": d.get("is_paused"),
            "description": d.get("description"),
            "fileloc": d.get("fileloc"),
            "tags": tags,
            "schedule": schedule_str(d.get("schedule_interval")),
            "local_path": str(local.relative_to(REPO_ROOT)) if local else None,
            "hints": extract_hints(local) if local else {},
        }
        rows.append(row)
    return rows


def group_for(r: dict) -> str:
    dag_id = r["dag_id"]
    tags = [t.lower() for t in (r.get("tags") or [])]
    path = r.get("local_path") or ""
    if path.startswith("dags/gsheet_raw") or "gsheet" in tags:
        return "Gsheet raw → Athena integrated"
    if dag_id.startswith("athena_") and ("ojk" in dag_id or "pusdafil" in dag_id):
        return "Athena / OJK & Pusdafil"
    if dag_id.startswith("athena_") and "bukas" in dag_id:
        return "Athena / Bukas"
    if dag_id.startswith("athena_"):
        return "Athena / datamart & summaries"
    if (
        "parquet" in dag_id
        or "iceberg" in dag_id
        or "bq_to_" in dag_id
        or dag_id.startswith("arrow_")
    ):
        return "BigQuery ↔ Parquet ↔ Iceberg"
    if "slik" in dag_id or "pusdafil" in dag_id or dag_id.startswith("ojk_"):
        return "OJK / Pusdafil / SLIK (BQ & reports)"
    if dag_id.startswith("raw_") or dag_id.startswith("daily_raw_"):
        return "Bukas & Danacita raw ingest"
    if "helicap" in dag_id or "lendeast" in dag_id:
        return "Partner feeds"
    if (
        any(x in dag_id for x in ("monitoring", "governance", "data_quality"))
        or "data_gov" in path
        or "_etl" in dag_id
        or dag_id.endswith("_etl")
    ):
        return "Core ETL / governance / monitoring"
    if path.startswith("dags/archived"):
        return "Archived (still active in Airflow)"
    if any(
        x in dag_id
        for x in ("risk_share", "click_monthly", "exchange_currency", "accounting")
    ):
        return "Accounting / finance"
    return "Daily facts / BigQuery layer & other"


def purpose_for(r: dict) -> str:
    dag_id = r["dag_id"]
    if dag_id in PURPOSE_OVERRIDES:
        return PURPOSE_OVERRIDES[dag_id]
    hints = r.get("hints") or {}
    tags = r.get("tags") or []
    tags_l = [t.lower() for t in tags]
    path = r.get("local_path") or ""
    athena_db = hints.get("athena_db")
    tables = hints.get("tables") or []
    iceberg = hints.get("iceberg_table")
    desc = r.get("description") or hints.get("dag_description") or hints.get("module_doc")

    if path.startswith("dags/gsheet_raw"):
        return (
            f"Daily Google Sheet ingest for `{dag_id}` into Athena Iceberg "
            "`integrated` (Bash → codes ETL)."
        )

    if dag_id.startswith("athena_"):
        pretty = dag_id[len("athena_") :].replace("_", " ")
        db = athena_db or (
            "reports"
            if any(x in dag_id for x in ("ojk", "pusdafil", "slik"))
            else "summaries"
        )
        if iceberg:
            return f"Builds/updates Athena `{db}.{iceberg}` ({pretty})."
        if tables:
            tlist = ", ".join(f"`{t}`" for t in tables[:3])
            verb = (
                "Manual/clean rebuild of"
                if "clean" in dag_id or str(r.get("schedule", "")).startswith("None")
                else "Builds/updates"
            )
            return f"{verb} {tlist} in Athena `{db}`."
        if "clean" in dag_id:
            return f"Manual/clean rebuild for {pretty} in Athena `{db}`."
        if str(r.get("schedule", "")).startswith("None"):
            return f"Manual Athena job for {pretty} (db `{db}`)."
        if "snapshot" in tags_l:
            return f"Scheduled snapshot build for {pretty} in Athena `{db}`."
        if "Write_truncate" in tags or "write_truncate" in tags_l:
            return f"Write-truncate rebuild for {pretty} in Athena `{db}`."
        return f"Athena pipeline for {pretty} targeting `{db}`."

    if "parquet" in dag_id and "iceberg" in dag_id:
        return f"Loads Parquet into Athena Iceberg (`{dag_id}`)."
    if (
        "bq_to_parquet" in dag_id
        or dag_id.startswith("arrow_")
        or "bukas_bq_to_parquet" in dag_id
    ):
        return f"Exports BigQuery tables to Parquet for lakehouse (`{dag_id}`)."
    if "pusdafil" in dag_id:
        return f"Pusdafil regulatory report pipeline (`{dag_id}`)."
    if "slik" in dag_id:
        return f"SLIK reporting pipeline (`{dag_id}`) into Athena reports."
    if dag_id.startswith("ojk_"):
        return f"OJK master/report pipeline (`{dag_id}`)."
    if dag_id.startswith("raw_") or dag_id.startswith("daily_raw_"):
        return f"Raw data ingest pipeline (`{dag_id}`)."
    if "risk_share" in dag_id:
        return f"PH risk-share / reflect loan-tape pipeline (`{dag_id}`)."
    if "portfolio" in dag_id:
        return f"Portfolio snapshot/update pipeline (`{dag_id}`)."
    if "loanbook" in dag_id:
        return f"Loanbook materialization pipeline (`{dag_id}`)."
    if "accounting_repayment" in dag_id:
        return f"Accounting repayment fact/snapshot pipeline (`{dag_id}`)."
    if desc:
        return desc if desc.endswith(".") else desc + "."
    tagbit = f" Tags: {', '.join(tags[:5])}." if tags else ""
    return f"Pipeline `{dag_id}`.{tagbit}"


def render(rows: list[dict]) -> str:
    groups: dict[str, list] = defaultdict(list)
    for r in sorted(rows, key=lambda x: x["dag_id"]):
        groups[group_for(r)].append(r)

    unpaused = sum(1 for r in rows if not r["is_paused"])
    paused = sum(1 for r in rows if r["is_paused"])
    today = date.today().isoformat()

    lines = [
        "# Erudifi Airflow DAG catalog (mono-pipeline)",
        "",
        "Catalog of DAGs with Airflow `is_active=true` on `https://airflow.erudifi.com`.",
        f"Generated **{today}** · **{len(rows)}** active DAG IDs "
        f"({unpaused} unpaused, {paused} paused).",
        "",
        "Use this file to answer what a DAG does without re-reading the repo. "
        "Confirm live run/pause status with `scripts/airflow_api.py` when operating "
        "on production.",
        "",
        "**Source repo:** `/data/code/mono-pipeline`  ",
        "**Refresh:** `python3 .agents/skills/airflow-mono-pipeline/scripts/generate_dag_catalog.py`",
        "",
        "Schedules are Airflow-stored values; many DAG files use timezone `Asia/Jakarta`.",
        "",
        "## Quick index (unpaused only)",
        "",
    ]
    for r in sorted(rows, key=lambda x: x["dag_id"]):
        if r["is_paused"]:
            continue
        purpose = purpose_for(r)
        short = purpose if len(purpose) <= 110 else purpose[:107] + "..."
        lines.append(f"- [`{r['dag_id']}`](#{r['dag_id']}) — {short}")
    lines.append("")

    for g in GROUP_ORDER:
        items = groups.get(g) or []
        if not items:
            continue
        lines.append(f"## {g}")
        lines.append("")
        for r in items:
            dag_id = r["dag_id"]
            src = r.get("local_path")
            if src:
                src_disp = f"`{src}`"
            else:
                fl = r.get("fileloc") or ""
                rel = fl.split("/repo/")[-1] if "/repo/" in fl else fl
                src_disp = (
                    f"`{rel}` (deployed path; may be missing/renamed in local checkout)"
                )
            tags = r.get("tags") or []
            tag_s = ", ".join(tags) if tags else "_(none)_"
            lines.append(f"### `{dag_id}`")
            lines.append(f"- **Purpose:** {purpose_for(r)}")
            lines.append(f"- **Schedule:** {r.get('schedule')}")
            lines.append(f"- **Paused:** {'yes' if r.get('is_paused') else 'no'}")
            lines.append(f"- **Source:** {src_disp}")
            lines.append(f"- **Tags:** {tag_s}")
            lines.append("")
    return "\n".join(lines) + "\n"


def main() -> None:
    if not AIRFLOW_API.is_file():
        raise SystemExit(f"Missing helper: {AIRFLOW_API}")
    dags = fetch_active_dags()
    rows = enrich(dags)
    text = render(rows)
    OUT_PATH.write_text(text, encoding="utf-8")
    print(f"Wrote {OUT_PATH} ({len(rows)} DAGs, {len(text)} chars)")


if __name__ == "__main__":
    main()
