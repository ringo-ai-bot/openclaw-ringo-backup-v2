---
name: loan-application-decision-notes
description: >-
  Assess loan applications against prompt-based credit criteria and produce
  Decision Notes (strengths, weaknesses, approve/reject suggestion). Use for
  credit review, analisa aplikasi, layak approve/reject, DBR, CLIK/FDC, or
  Decision Notes requests. Advisory only — does not change application status.
---

# Loan application Decision Notes

Evaluate a loan application against a **JSON criteria pack** and output
**Decision Notes**. Criteria are file-based for now (demo); core-loans DB packs
will replace this later.

## When to use

- User asks to assess / review / analisa a loan application for approve vs reject
- User wants Decision Notes, credit checklist, DBR / CLIK / FDC judgment
- User pastes application facts or gives `reference_code` / application id

## When not to use

- Portfolio analytics or general Metabase questions → `metabase-core-loans`
- Production data fixes → `core-loans-tech-intervention`
- Fetching private files only → `core-loans-s3-presign`

## Access control (required)

Before loading criteria or fetching facts, resolve the requester through
`access-control.json` and enforce `use_loan_application_decision_notes` in
`access-actions.json`.

- **Owner**: allow.
- **Trusted**: allow for work-related, read-only assessment.
- **Chat-only**, **Blocked**, unknown, or ambiguous identity: deny.

If using Metabase for facts, also enforce `use_metabase_core_loans`.

## Criteria source

Default pack:

```text
.agents/skills/loan-application-decision-notes/criteria/danacita-demo-v1.json
```

(or the mirrored path under `skills/loan-application-decision-notes/criteria/`).

- Always **read the JSON file** before evaluating (do not rely on memory of criteria).
- If the user names another file under `criteria/`, use that pack instead.
- Pack `locale` drives Decision Notes language (demo pack is `id`).

## Workflow

Copy this checklist and track progress:

```
- [ ] 1. Enforce use_loan_application_decision_notes
- [ ] 2. Load criteria JSON pack; note id, version, locale, decision_policy
- [ ] 3. Resolve Danacita vs Bukas (ask if unclear and it affects facts)
- [ ] 4. Gather facts lazily per criterion (Metabase if app id / reference_code; else pasted facts)
- [ ] 4b. For FDC: use canonical SQL in field-hints; if Found but query fails, retry then escalate (do not fake insufficient_data)
- [ ] 5. Evaluate criteria in sort_order; on first hard fail stop (stop_on_hard_fail) and skip the rest
- [ ] 6. Emit Decision Notes in pack locale using the template
```

### Facts

1. **Metabase path** — user gives `reference_code` or application id: query via
   `metabase-core-loans` using [references/field-hints.md](references/field-hints.md).
   Minimal fields only; prefer **lazy** fetches per criterion in `sort_order`.
   When `stop_on_hard_fail` trips, do not query for skipped criteria. For DBR:
   recompute like core-loans `IdLoanApplication` (party by self-guaranteed;
   active installments by KTP + current `approved|requested_monthly_repayment`;
   verified/declared income) or accept admin Auto Approve Indicator DBR; do
   **not** look for stored `*_debt_burden_ratio` columns. For FDC: follow the
   **canonical FDC fact SQL** in field-hints (`inquiries_idinquirydata` by
   `loan_application_id` + `kind`); evaluate Written Off separately from Closed;
   never treat a failed FDC join as missing DPD when the log is Found.
2. **Paste path** — user provides CSV/JSON/chat facts: use those; do not invent
   missing values (`insufficient_data` instead). Admin-stated DBR counts as a fact.
3. If neither id nor usable facts: ask for one or the other before judging.

### Evaluate

Follow [references/evaluation-rubric.md](references/evaluation-rubric.md).

Per criterion: `pass` | `fail` | `insufficient_data` | `not_applicable` | `skipped` + evidence.

If `decision_policy.stop_on_hard_fail` is true: on the first **hard** `fail`,
stop evaluating; mark remaining criteria `skipped`; emit Notes with `reject`
when `reject_if_any_hard_fail` is true. Soft fails do not stop the run.

### Locale (required)

Write the **entire Decision Notes block** in pack `locale` (`id` | `en`):
headings, summary, strengths/weaknesses, evidence prose, suggestion/confidence
labels, next action. Do not mix languages inside the Notes. Outer chat may
follow the user.

### Output

Fill [assets/decision-notes.template.md](assets/decision-notes.template.md)
only. Include pack `id`, `version`, and `locale` in the header.

## Hard rules

- **Advisory only.** Never update application status, `decision_code`, or any
  core-loans / Metabase write.
- Do not invent bureau, income, or DBR figures.
- Minimize PII in Notes.
- Cite the criteria pack used.

## Additional resources

- [criteria/danacita-demo-v1.json](criteria/danacita-demo-v1.json) — default pack
- [assets/decision-notes.template.md](assets/decision-notes.template.md)
- [references/evaluation-rubric.md](references/evaluation-rubric.md)
- [references/field-hints.md](references/field-hints.md)
