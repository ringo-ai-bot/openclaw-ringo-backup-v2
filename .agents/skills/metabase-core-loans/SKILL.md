---
name: metabase-core-loans
description: >-
  Query Erudifi lending data via Metabase API (DanaCita v2 / Bukas v2) with
  read-only SQL against the core-loans Postgres schema. Use automatically for
  data-related inquiries, analytics questions, metrics, trends, counts, lists,
  borrower lookups, loan lookups, repayments, collections, written-off / bad
  debt, recoveries, portfolio health, partner/school performance, and any
  Danacita or Bukas business-data question answerable from Metabase.
---

# Metabase core-loans

Answer lending analytics questions by running **read-only native SQL** against
company Metabase, using the `core-loans` schema.

## When to use

- Business / ops / product questions about Danacita or Bukas loan data
- Examples: written-off borrowers who paid back, bad-debt recovery trends,
  delinquency, disbursements, repayment performance, partner metrics

## Access control (required)

Before reading schema files or running any query, resolve the requester through
`access-control.json` and enforce the `use_metabase_core_loans` action in
`access-actions.json`.

- **Owner**: allow.
- **Trusted**: allow for work-related, read-only data questions.
- **Chat-only**, **Blocked**, unknown, or ambiguous identity: deny without
  reading schema files or invoking the query helper.
- Trusted users may use the helper, but must never receive or inspect the API
  key. The script handles authentication internally.

## Configuration

| Item | Value |
|---|---|
| Metabase URL | `https://bob.danacita.co.id` |
| API key file | `~/.openclaw/secrets/metabase-api-key.txt` |
| Danacita context | database **DanaCita v2**, id **13** |
| Bukas context | database **Bukas v2**, id **12** |
| Schema source | `/data/code/core-loans` (Django models) |

Never print, log, or commit the API key.

## Context selection (required)

Map the question to a Metabase database:

- **Danacita / Indonesia / ID / DC** → `--context danacita` (db 13)
- **Bukas / Philippines / PH** → `--context bukas` (db 12)

**If you cannot tell which context the user means, ask before querying.**
Do not guess. Do not query both unless the user asks for a comparison.

## Workflow

Copy this checklist and track progress:

```
- [ ] 1. Resolve Danacita vs Bukas (ask if unclear)
- [ ] 2. Consult SCHEMA.md for the right tables / joins
- [ ] 3. Confirm exact column names in reference/tables-reference.md if needed
- [ ] 4. Write a single read-only SELECT / WITH
- [ ] 5. Run scripts/query.py
- [ ] 6. Summarize in plain language for a non-technical audience
```

### Step details

1. **Context** — see above.
2. **Schema** — read [SCHEMA.md](SCHEMA.md) first (curated analytics guide).
3. **Field lookup** — if a column is missing or unfamiliar, search
   [reference/tables-reference.md](reference/tables-reference.md)
   (all 325 tables + fields). Regenerate with
   `python3 scripts/generate_schema_reference.py` if it looks stale.
4. **SQL** — one statement, `SELECT` or `WITH` only. Prefer explicit filters:
   - exclude soft deletes: `datetime_deleted IS NULL` when the column exists
   - exclude test users: `users_user.is_test_account = false` (or `IS NULL`)
   - prefer `accounting_collection.status = 'Processed'` for real payments
5. **Run**:

```bash
python3 .agents/skills/metabase-core-loans/scripts/query.py \
  --context danacita \
  --sql "SELECT ..."
```

Or pipe SQL:

```bash
python3 .agents/skills/metabase-core-loans/scripts/query.py --context bukas --format json <<'SQL'
SELECT ...
SQL
```

Useful flags: `--limit N`, `--format table|csv|json`, `--no-wrap-limit`.

6. **Answer** — lead with the takeaway, then supporting numbers. State context,
   date range, and definition (e.g. what counts as a “recovery”). Keep currency
   and units clear. Offer a short follow-up slice (by month, partner, status)
   when useful.

## Safety rules

- **Read-only only.** `query.py` rejects INSERT/UPDATE/DELETE/DDL and multi-statements.
- Do not attempt to change Metabase cards, dashboards, permissions, or databases.
- Do not dump PII wholesale — return aggregates or the minimum borrower fields needed.
- Never echo the API key.

## Goal-question starters

These map to worked examples in [SCHEMA.md](SCHEMA.md):

| User ask | Approach |
|---|---|
| “Who among our written-off borrowers decided to pay back?” | WOFF loans (`datetime_written_off IS NOT NULL`) with processed collections on/after write-off date → example **A** |
| “What's the trend in bad debt recoveries?” | Monthly sum of those post-WOFF collections → example **B**; optionally debt-relief schedule → example **C** |

## Scripts

| Script | Purpose |
|---|---|
| `scripts/query.py` | Execute read-only SQL against Metabase |
| `scripts/generate_schema_reference.py` | Refresh `reference/tables-reference.md` from live metadata |

Requires Python 3 stdlib only (no pip packages).

## Additional resources

- [SCHEMA.md](SCHEMA.md) — curated table explanations + example SQL
- [reference/tables-reference.md](reference/tables-reference.md) — full auto-generated field reference
- Metabase API docs: https://www.metabase.com/docs/latest/api
