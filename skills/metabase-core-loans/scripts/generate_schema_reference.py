#!/usr/bin/env python3
"""Generate reference/tables-reference.md from Metabase database metadata.

Both DanaCita v2 (13) and Bukas v2 (12) share the same Django schema from
core-loans; by default we snapshot DanaCita v2.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

METABASE_URL = "https://bob.danacita.co.id"
API_KEY_PATH = Path.home() / ".openclaw" / "secrets" / "metabase-api-key.txt"
DEFAULT_DB_ID = 13
SKILL_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = SKILL_ROOT / "reference" / "tables-reference.md"


def load_api_key() -> str:
    if not API_KEY_PATH.is_file():
        raise SystemExit(f"API key file not found: {API_KEY_PATH}")
    key = API_KEY_PATH.read_text(encoding="utf-8").strip()
    if not key:
        raise SystemExit(f"API key file is empty: {API_KEY_PATH}")
    return key


def fetch_metadata(db_id: int, api_key: str) -> dict:
    url = f"{METABASE_URL}/api/database/{db_id}/metadata?include_hidden=false"
    req = urllib.request.Request(
        url,
        headers={
            "x-api-key": api_key,
            "User-Agent": "openclaw-metabase-core-loans/1.0",
            "Accept": "application/json",
        },
        method="GET",
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise SystemExit(f"Metabase HTTP {e.code}: {body[:2000]}") from e


def app_prefix(table_name: str) -> str:
    if "_" not in table_name:
        return table_name
    return table_name.split("_", 1)[0]


def shorten_type(base_type: str | None) -> str:
    if not base_type:
        return ""
    return base_type.replace("type/", "")


def render_markdown(meta: dict, db_id: int) -> str:
    db_name = (meta.get("name") or f"database {db_id}").strip()
    tables = sorted(
        meta.get("tables") or [],
        key=lambda t: ((t.get("schema") or ""), t.get("name") or ""),
    )
    by_app: dict[str, list] = defaultdict(list)
    for t in tables:
        by_app[app_prefix(t.get("name") or "")].append(t)

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines: list[str] = [
        f"# core-loans Metabase table reference",
        "",
        f"_Auto-generated from `{db_name}` (database_id={db_id}) on {now}._",
        "",
        "Applies to both **DanaCita v2** (id 13) and **Bukas v2** (id 12) —",
        "same Django schema from `/data/code/core-loans`.",
        "",
        "Regenerate with:",
        "",
        "```bash",
        "python3 scripts/generate_schema_reference.py",
        "```",
        "",
        f"**Tables:** {len(tables)}",
        "",
        "## App summary",
        "",
        "| App prefix | Tables |",
        "|---|---:|",
    ]
    for app in sorted(by_app, key=lambda a: (-len(by_app[a]), a)):
        lines.append(f"| `{app}` | {len(by_app[app])} |")

    lines.extend(["", "## Tables", ""])

    for app in sorted(by_app):
        lines.append(f"### `{app}_*`")
        lines.append("")
        for t in sorted(by_app[app], key=lambda x: x.get("name") or ""):
            name = t.get("name") or ""
            schema = t.get("schema") or "public"
            desc = (t.get("description") or "").strip()
            fields = sorted(
                t.get("fields") or [],
                key=lambda f: (f.get("position") is None, f.get("position") or 0, f.get("name") or ""),
            )
            lines.append(f"#### `{schema}.{name}`")
            lines.append("")
            if desc:
                lines.append(desc)
                lines.append("")
            lines.append(f"_Fields: {len(fields)}_")
            lines.append("")
            if fields:
                lines.append("| Field | Type | Description |")
                lines.append("|---|---|---|")
                for f in fields:
                    fname = f.get("name") or ""
                    ftype = shorten_type(f.get("base_type"))
                    fdesc = (f.get("description") or "").replace("|", "\\|").replace("\n", " ")
                    lines.append(f"| `{fname}` | {ftype} | {fdesc} |")
                lines.append("")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db-id", type=int, default=DEFAULT_DB_ID)
    parser.add_argument(
        "--out",
        type=Path,
        default=DEFAULT_OUT,
        help=f"Output path (default: {DEFAULT_OUT})",
    )
    args = parser.parse_args()

    api_key = load_api_key()
    print(f"Fetching metadata for database_id={args.db_id}...", file=sys.stderr)
    meta = fetch_metadata(args.db_id, api_key)
    md = render_markdown(meta, args.db_id)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(md, encoding="utf-8")
    n_tables = len(meta.get("tables") or [])
    print(f"Wrote {args.out} ({n_tables} tables)", file=sys.stderr)


if __name__ == "__main__":
    main()
