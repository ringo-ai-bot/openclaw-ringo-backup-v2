# core-loans schema guide (analytics)

Plain-language map of the tables you need for business questions against Metabase
**DanaCita v2** (db 13) / **Bukas v2** (db 12). Both databases mirror the Django
schema in `/data/code/core-loans`.

For exhaustive field lists, see [reference/tables-reference.md](reference/tables-reference.md).

## Mental model

```
users_user (borrower)
    └── loans_loan (one borrower, many loans)
            ├── accounting_repayment          (installment schedule)
            ├── accounting_collection         (money received)
            ├── accounting_repaymentrecovery  (debt-relief schedule)
            ├── loans_debtrelief              (debt-relief program)
            └── partners_partner              (school / partner)
```

Money amounts are decimals in the local currency (IDR for Danacita, PHP for Bukas).
Prefer filtering out soft-deleted rows (`datetime_deleted IS NULL`) and test
accounts (`users_user.is_test_account = false`) unless the user asks otherwise.

---

## 1. Borrowers & profiles

### `users_user`
The person (borrower, staff, partner user). Join key for loans via `loans_loan.borrower_id`.

| Column | Meaning |
|---|---|
| `id` | Primary key (join as `borrower_id`) |
| `first_name`, `last_name`, `email`, `username` | Identity |
| `is_active`, `is_test_account` | Filter real borrowers: `is_test_account = false` |
| `type`, `borrower_type` | User / borrower classification |
| `institution_id`, `school_id` | Linked school |
| `user_total_loans`, `user_total_outstanding_loan_amount` | Denormalized aggregates |
| `datetime_deleted`, `is_deleted` | Soft delete |

**Do not return password / token / OTP fields in answers.**

### `users_profile` / `users_idprofile` / `users_phprofile`
KYC / profile details. `users_idprofile` is Indonesia (Danacita);
`users_phprofile` is Philippines (Bukas). Join through profile polymorphism —
for most analytics you only need `users_user`.

---

## 2. Loans & applications

### `loans_loan`
The activated loan (system of record for portfolio, DPD, write-offs).

| Column | Meaning |
|---|---|
| `id` | Primary key |
| `reference_code` | Human-facing loan code |
| `status` | Lifecycle state (see below) |
| `borrower_id` | → `users_user.id` |
| `partner_id` | → `partners_partner.id` |
| `product_id` | → `loans_loanproduct.id` |
| `disbursed_amount`, `actual_disbursed_amount` | Disbursed principal |
| `outstanding_principal_balance`, `outstanding_loan_amount` | Outstanding |
| `datetime_disbursed`, `date_start` | When money went out / loan started |
| `datetime_written_off` | When loan was written off (NULL = not WOFF) |
| `datetime_woff_effectivity` | Accounting write-off effectivity date |
| `written_off_batch_id` | → `loans_writtenoffloanbatch.id` |
| `early_written_off` | Flag for early WOFF |
| `close_code` | Why closed (e.g. `Fully Paid`, `Written Off`) |
| `past_due_bucket`, `effective_past_due_bucket`, `actual_days_past_due` | Delinquency |
| `datetime_deleted`, `is_deleted` | Soft delete |

**Written-off statuses seen in production:** `Written Off`, `Written Off Closed`.
Safest written-off filter:

```sql
datetime_written_off IS NOT NULL
```

### `loans_loanapplication`
Pre-activation application funnel (underwriting, docs, approval). Use for
application / conversion questions, not portfolio outstanding.

### `loans_loanproduct`
Product terms: `name`, `interest_rate`, `tenor`, `type`, etc.

### `loans_writtenoffloanbatch`
Batch ingest/process of write-offs. Useful for ops audits; most analytics only
need `loans_loan.datetime_written_off`.

### `loans_debtrelief`
Debt-relief program attached to a loan (`loan_id`). Active when
`datetime_activated IS NOT NULL` and `datetime_reverted IS NULL`.
Recovery schedule for these loans lives in `accounting_repaymentrecovery`.

---

## 3. Repayments & accounting

### `accounting_repayment`
Installment schedule for a normal (non–debt-relief) loan.

| Column | Meaning |
|---|---|
| `loan_id`, `borrower_id` | Links |
| `period` | Installment number |
| `status` | `UNPAID`, `LATE`, `PAID`, `PARTIAL`, `CLOSED`, `PRE_TERMINATED`, `WAIVED`, `RESTRUCTURED` |
| `date_due`, `date_paid` | Schedule vs actual |
| `scheduled_*`, `paid_*`, `due_total`, `paid_total` | Amounts |
| `days_in_arrears` | Delinquency on this installment |
| `datetime_deleted` | Soft delete |

### `accounting_collection`
Inbound payment events applied to a loan.

| Column | Meaning |
|---|---|
| `loan_id` | Loan paid |
| `status` | Mostly `Processed` (success) or `New` |
| `date_posted`, `datetime_processed` | When payment landed / was applied |
| `paid_principal`, `paid_interest`, `paid_penalty`, `paid_excess` | Split |
| `channel`, `sub_channel`, `kind` | Payment rails / type |
| `reference_code`, `correlator_code` | Ops identifiers |

**For “money actually recovered” use `status = 'Processed'`.**

### `accounting_receivabletransaction`
Ledger of receivable charges / clearings (`charge_type`, `amount`, `date_due`,
`date_cleared`, `is_reversed`).

### `accounting_credit` / `accounting_rebate`
Credits and rebates allocated to borrowers / collections.

---

## 4. Bad debt & recoveries

Two related but different concepts:

| Concept | Where | Use when |
|---|---|---|
| **Write-off** | `loans_loan.datetime_written_off` | Loan marked as bad debt |
| **Post–write-off collections** | `accounting_collection` with `date_posted >= datetime_written_off::date` | “Did a WOFF borrower pay back?” / recovery trends |
| **Debt-relief schedule** | `accounting_repaymentrecovery` + `loans_debtrelief` | Loans on an active debt-relief plan (includes some WOFF loans) |

### `accounting_repaymentrecovery`
Installment schedule for debt-relief loans (not a generic “recovery ledger”).

| Column | Meaning |
|---|---|
| `loan_id` | Loan on debt relief |
| `period`, `status` | Same status vocabulary as repayments (`UNPAID`/`LATE`/`PAID`/`PARTIAL`) |
| `scheduled_total`, `paid_total`, `due_total` | Amounts |
| `date_due`, `date_paid` | Schedule vs actual |

---

## 5. Collections ops

### `collection_operations_externalcollectionagency`
External collection agencies. Loans may reference
`loans_loan.external_collection_agency_id`.

Related: `collection_operations_externalcollectionagencylog`,
`collection_operations_externalcollectionagencyreport`,
`collection_operations_ecaagreementdocument`.

---

## 6. Partners / institutions

### `partners_partner`
School or financing partner (`name`, `slug`, `is_active`, `partner_type`,
`institution_id`, …). Join from `loans_loan.partner_id`.

### `partners_institution`
Institution grouping (`id`, `name`).

Other useful: `partners_disbursement`, `partners_course`, `partners_faculty`.

---

## Example queries

Replace nothing — these are ready to run via `scripts/query.py --context danacita|bukas`.

### A. Written-off borrowers who paid something back

```sql
SELECT
  u.id AS borrower_id,
  u.first_name,
  u.last_name,
  u.email,
  l.reference_code,
  l.datetime_written_off::date AS written_off_on,
  COUNT(c.transaction_ptr_id) AS payments_after_woff,
  COALESCE(SUM(c.paid_principal + c.paid_interest + c.paid_penalty + c.paid_excess), 0)
    AS amount_recovered
FROM loans_loan l
JOIN users_user u ON u.id = l.borrower_id
JOIN accounting_collection c ON c.loan_id = l.id
WHERE l.datetime_written_off IS NOT NULL
  AND (l.datetime_deleted IS NULL)
  AND (u.is_test_account = false OR u.is_test_account IS NULL)
  AND c.status = 'Processed'
  AND c.date_posted >= l.datetime_written_off::date
GROUP BY 1, 2, 3, 4, 5, 6
ORDER BY amount_recovered DESC
```

### B. Monthly bad-debt recovery trend

```sql
SELECT
  date_trunc('month', c.date_posted)::date AS month,
  COUNT(DISTINCT l.id) AS loans_with_recovery,
  COUNT(c.transaction_ptr_id) AS payment_count,
  SUM(c.paid_principal + c.paid_interest + c.paid_penalty + c.paid_excess)
    AS amount_recovered
FROM accounting_collection c
JOIN loans_loan l ON l.id = c.loan_id
WHERE l.datetime_written_off IS NOT NULL
  AND c.status = 'Processed'
  AND c.date_posted >= l.datetime_written_off::date
  AND c.date_posted >= (CURRENT_DATE - INTERVAL '24 months')
GROUP BY 1
ORDER BY 1
```

### C. Debt-relief recovery payments (schedule-based)

```sql
SELECT
  date_trunc('month', rr.date_paid)::date AS month,
  COUNT(*) AS installments_paid,
  SUM(rr.paid_total) AS paid_total
FROM accounting_repaymentrecovery rr
JOIN loans_loan l ON l.id = rr.loan_id
WHERE rr.status IN ('PAID', 'PARTIAL')
  AND rr.date_paid IS NOT NULL
  AND rr.date_paid >= (CURRENT_DATE - INTERVAL '24 months')
GROUP BY 1
ORDER BY 1
```

### D. Portfolio snapshot by status

```sql
SELECT
  status,
  COUNT(*) AS loans,
  SUM(COALESCE(outstanding_loan_amount, 0)) AS outstanding
FROM loans_loan
WHERE datetime_deleted IS NULL
GROUP BY 1
ORDER BY loans DESC
```

---

## Answering tip for non-technical users

1. State the **context** (Danacita vs Bukas) and **time range**.
2. Lead with the headline number, then a short table of details.
3. Clarify definitions: e.g. “recovered” = processed collections posted on/after the write-off date.
4. Call out caveats (test accounts excluded, soft-deleted loans excluded, currency).
