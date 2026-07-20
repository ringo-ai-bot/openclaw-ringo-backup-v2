#!/usr/bin/env python3
"""Run read-only native SQL against company Metabase (Danacita / Bukas v2)."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

METABASE_URL = "https://bob.danacita.co.id"
API_KEY_PATH = Path.home() / ".openclaw" / "secrets" / "metabase-api-key.txt"

CONTEXTS = {
    "danacita": {"db_id": 13, "label": "DanaCita v2"},
    "bukas": {"db_id": 12, "label": "Bukas v2"},
}

DEFAULT_LIMIT = 500
MAX_LIMIT = 5000

# Forbidden as whole SQL words (case-insensitive). Comments are stripped first.
WRITE_KEYWORDS = re.compile(
    r"\b("
    r"INSERT|UPDATE|DELETE|DROP|ALTER|CREATE|TRUNCATE|REPLACE|MERGE|"
    r"GRANT|REVOKE|COPY|CALL|EXECUTE|DO|VACUUM|ANALYZE|REINDEX|"
    r"COMMENT\s+ON|SET\s+ROLE|RESET\s+ROLE"
    r")\b",
    re.IGNORECASE,
)

COMMENT_RE = re.compile(r"/\*.*?\*/|--.*?$", re.DOTALL | re.MULTILINE)


def load_api_key() -> str:
    if not API_KEY_PATH.is_file():
        raise SystemExit(
            f"API key file not found: {API_KEY_PATH}\n"
            "Create it with the Metabase API key (one line, no quotes)."
        )
    key = API_KEY_PATH.read_text(encoding="utf-8").strip()
    if not key:
        raise SystemExit(f"API key file is empty: {API_KEY_PATH}")
    return key


def strip_comments(sql: str) -> str:
    return COMMENT_RE.sub(" ", sql)


def validate_readonly(sql: str) -> str:
    cleaned = strip_comments(sql).strip().rstrip(";")
    if not cleaned:
        raise SystemExit("Empty SQL.")

    # Single statement only
    if ";" in cleaned:
        raise SystemExit("Only a single SQL statement is allowed (no semicolons).")

    if WRITE_KEYWORDS.search(cleaned):
        raise SystemExit(
            "Rejected: only read-only SELECT / WITH queries are allowed. "
            "Write/DDL keywords are blocked."
        )

    first = cleaned.lstrip().split(None, 1)[0].upper()
    if first not in {"SELECT", "WITH", "EXPLAIN", "SHOW", "VALUES"}:
        raise SystemExit(
            f"Rejected: query must start with SELECT or WITH (got '{first}')."
        )

    return cleaned


def ensure_limit(sql: str, limit: int) -> str:
    """Wrap in a subquery with LIMIT if the SQL does not already limit rows."""
    if re.search(r"\bLIMIT\b", sql, re.IGNORECASE):
        return sql
    return f"SELECT * FROM (\n{sql}\n) AS _metabase_skill_q LIMIT {limit}"


def run_query(db_id: int, sql: str, api_key: str) -> dict:
    payload = json.dumps(
        {
            "database": db_id,
            "type": "native",
            "native": {"query": sql},
        }
    ).encode("utf-8")
    req = urllib.request.Request(
        f"{METABASE_URL}/api/dataset",
        data=payload,
        headers={
            "Content-Type": "application/json",
            "x-api-key": api_key,
            "User-Agent": "openclaw-metabase-core-loans/1.0",
            "Accept": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise SystemExit(f"Metabase HTTP {e.code}: {body[:2000]}") from e
    except urllib.error.URLError as e:
        raise SystemExit(f"Metabase request failed: {e}") from e


def extract_result(data: dict) -> tuple[list[str], list[list]]:
    if data.get("error"):
        raise SystemExit(f"Metabase query error: {data['error']}")
    payload = data.get("data") or {}
    cols = [c.get("display_name") or c.get("name") for c in payload.get("cols", [])]
    rows = payload.get("rows") or []
    return cols, rows


def print_table(cols: list[str], rows: list[list]) -> None:
    if not cols:
        print("(no columns)")
        return
    str_rows = [["" if v is None else str(v) for v in row] for row in rows]
    widths = [len(c) for c in cols]
    for row in str_rows:
        for i, cell in enumerate(row):
            if i < len(widths):
                widths[i] = max(widths[i], min(len(cell), 60))
    fmt = " | ".join(f"{{:<{w}}}" for w in widths)
    print(fmt.format(*cols))
    print("-+-".join("-" * w for w in widths))
    for row in str_rows:
        clipped = [
            (cell[:57] + "...") if len(cell) > 60 else cell for cell in row
        ]
        # pad short rows
        while len(clipped) < len(cols):
            clipped.append("")
        print(fmt.format(*clipped[: len(cols)]))
    print(f"\n{len(rows)} row(s)")


def print_csv(cols: list[str], rows: list[list]) -> None:
    writer = csv.writer(sys.stdout)
    writer.writerow(cols)
    for row in rows:
        writer.writerow(row)


def print_json(cols: list[str], rows: list[list]) -> None:
    records = [dict(zip(cols, row)) for row in rows]
    json.dump(records, sys.stdout, indent=2, default=str)
    sys.stdout.write("\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run read-only SQL against Metabase (Danacita or Bukas v2)."
    )
    parser.add_argument(
        "--context",
        "-c",
        required=True,
        choices=sorted(CONTEXTS),
        help="danacita (DB 13) or bukas (DB 12)",
    )
    parser.add_argument(
        "--sql",
        "-s",
        help="SQL to run. If omitted, read from stdin.",
    )
    parser.add_argument(
        "--limit",
        "-n",
        type=int,
        default=DEFAULT_LIMIT,
        help=f"Max rows when SQL has no LIMIT (default {DEFAULT_LIMIT}, max {MAX_LIMIT})",
    )
    parser.add_argument(
        "--format",
        "-f",
        choices=["table", "csv", "json"],
        default="table",
        help="Output format (default: table)",
    )
    parser.add_argument(
        "--no-wrap-limit",
        action="store_true",
        help="Do not wrap the query with an outer LIMIT",
    )
    args = parser.parse_args()

    limit = max(1, min(args.limit, MAX_LIMIT))
    sql_raw = args.sql if args.sql is not None else sys.stdin.read()
    sql = validate_readonly(sql_raw)
    if not args.no_wrap_limit:
        sql = ensure_limit(sql, limit)

    ctx = CONTEXTS[args.context]
    api_key = load_api_key()
    result = run_query(ctx["db_id"], sql, api_key)
    cols, rows = extract_result(result)

    if args.format == "table":
        print(f"# {ctx['label']} (database_id={ctx['db_id']})")
        print_table(cols, rows)
    elif args.format == "csv":
        print_csv(cols, rows)
    else:
        print_json(cols, rows)


if __name__ == "__main__":
    main()
