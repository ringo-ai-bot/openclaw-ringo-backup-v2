# Field hints (demo)

Map `evidence_hints` / user language to where facts usually live. Prefer Metabase read-only queries via `metabase-core-loans` when an application id / `reference_code` is given. Confirm column names in that skill’s schema references before querying.

## Application identity

- `reference_code`, status, product, partner → `loans_loanapplication` / `loans_idloanapplication`
- Guarantor type → application / profile fields used in ID admin

## Borrower blacklist / watchlist

Admin labels in **ID loanapplication changeview → User and Profile Details** are
**computed**, not stored columns. Replicate the same core-loans logic so Metabase
facts match the Yes/No shown in Django admin.

### core-loans display path (source of truth)

| Admin field | Code path |
|---|---|
| **Borrower is blacklisted** | `IdLoanApplicationChildAdmin.borrower_is_blacklisted` → `loan_app.borrower.profile.is_blacklisted()` → `IDProfileCheckerV2.is_blacklisted` → tag **`APPUPT`** in `profile.tags.names()` |
| **Borrower is watchlisted** | `IdLoanApplicationChildAdmin.borrower_is_watchlisted` → `loan_app.borrower.profile.is_in_watchlist()` → `IDWatchlistProfileChecker.is_blacklisted` → tag **`PPATK`** in `profile.tags.names()` |
| **Borrower datetime profile check** | `loan_app.borrower.profile.datetime_profile_check` (`users_profile.datetime_profile_check`) |

Key files under `/data/code/core-loans`:

- `loans/admin/views/id_loan_application_child_admin.py` (admin methods + fieldset)
- `users/models/profile.py` (`is_blacklisted` / `is_in_watchlist`)
- `users/models/impls/id.py` (`BaseIdProfileChecker.is_blacklisted`, tags `APPUPT` / `PPATK`)
- `users/models/id_profile.py` (`profile_checker = IDProfileCheckerV2`, `watchlist_checker = IDWatchlistProfileChecker`)
- `users/admin/utils.py` (`_blacklisted_display`: True → Yes, else No)

Boolean rule (exact tag name membership — **not** prefix):

- `borrower_is_blacklisted` = profile has taggit tag named exactly `APPUPT`
- `borrower_is_watchlisted` = profile has taggit tag named exactly `PPATK`
- Method tags like `APPUPT:FM` / `PPATK:FN+DOB` are **extra** match labels; they alone do
  **not** drive the admin Yes/No (admin checks the base tag only). Do not use
  `BlacklistFullMatchAutoRejector` FM-tag rules for this criterion.

Do **not** re-run live matching against `users_blacklistedprofile` /
`users_riskyprofile` for Decision Notes parity — admin Yes/No reflects
**persisted profile tags** from the last profile check. Quote
`datetime_profile_check` as supporting evidence when present.

### Metabase / SQL (same result as admin)

Join: `loans_loanapplication.borrower_id` → `users_profile.user_id` → profile `id`
as `taggit_taggeditem.object_id`.

| hint | Meaning |
|---|---|
| `borrower_is_blacklisted` | `EXISTS` taggit row for profile with `taggit_tag.name = 'APPUPT'` |
| `borrower_is_watchlisted` | `EXISTS` taggit row for profile with `taggit_tag.name = 'PPATK'` |
| `datetime_profile_check` | `users_profile.datetime_profile_check` |
| `profile_id` | `users_profile.id` (borrower's profile; taggit `object_id`) |
| `profile_tags` | Optional: list `taggit_tag.name` for the profile (evidence / debugging) |

Example read-only pattern (confirm `django_content_type` availability; if present,
prefer filtering `app_label = 'users'` and `model = 'profile'`):

```sql
SELECT
  la.reference_code,
  p.id AS profile_id,
  p.datetime_profile_check,
  EXISTS (
    SELECT 1
    FROM taggit_taggeditem ti
    JOIN taggit_tag t ON t.id = ti.tag_id
    WHERE ti.object_id = p.id
      AND t.name = 'APPUPT'
  ) AS borrower_is_blacklisted,
  EXISTS (
    SELECT 1
    FROM taggit_taggeditem ti
    JOIN taggit_tag t ON t.id = ti.tag_id
    WHERE ti.object_id = p.id
      AND t.name = 'PPATK'
  ) AS borrower_is_watchlisted
FROM loans_loanapplication la
JOIN users_profile p ON p.user_id = la.borrower_id
WHERE la.reference_code = {{reference_code}}
```

Paste/admin screenshot values (Yes/No) are also valid facts. If either flag is
true/Yes → criterion `borrower_not_blacklisted_or_watchlisted` **fail** (hard
reject when `reject_if_any_hard_fail` is on).

## Underwriting rating

Admin source: **ID loanapplication changeview → Loan Information Notes →
Underwriting Rating** (`IdUnderwritingLoanAppFieldset` in
`loans/admin/fieldsets/loan_application_underwriting_fieldsets.py`).

| Admin / field | Code path |
|---|---|
| **Underwriting Rating** | `LoanApplicationChildAdmin.underwriting_rating_with_status` → `loan.get_underwriting_display()["rating"]` |
| Stored value | `loans_loanapplication.underwriting_rating` (`LoanUnderwritingMixin`) |

Key files under `/data/code/core-loans`:

- `loans/admin/fieldsets/loan_application_underwriting_fieldsets.py` — `IdUnderwritingLoanAppFieldset` (“Loan Information Notes”)
- `loans/admin/views/loan_application_child_admin.py` — `underwriting_rating_with_status`
- `loans/mixins/loan_underwriting.py` — `underwriting_rating`, `get_underwriting_display`
- `underwriting/impls/underwriters.py` — scorecard rating assignment (R1–R10)

**Pack rule (hard)**

- Pass: `R1` … `R7`
- Fail → hard reject: `R8`, `R9`, `R10`
- Missing / blank / `-` → `insufficient_data`

Normalize display prefixes: prefs may replace `R` with `A` or `M` in admin
display only; Metabase/DB usually keeps `R*`. Treat `A8`/`M8` like `R8` (use the
numeric rank 1–10).

| hint | Meaning |
|---|---|
| `underwriting_rating` | `loans_loanapplication.underwriting_rating` (preferred) |
| `underwriting_rating_with_status` | Admin display string, may append `(Unverified)` |
| `underwriting_verified` | `underwriting_verified` boolean (supporting) |
| `underwriting_decision` | Accept / Manual Decision / Reject text (supporting; do not substitute for rating) |
| `underwriting_version` / `underwriting_datetime_computed` | Supporting context |

```sql
SELECT
  la.reference_code,
  la.underwriting_rating,
  la.underwriting_verified,
  la.underwriting_decision,
  la.underwriting_version,
  la.underwriting_datetime_computed
FROM loans_loanapplication la
WHERE la.reference_code = {{reference_code}};
```

## Restricted occupation (hard reject)

Check the **relevant party's** job fields on the ID loan application. Party follows
`guarantor_type` (same as income/DBR):

- `"Self Guaranteed"` → **borrower** employment fields
- otherwise → **guarantor** employment fields

| Field | Borrower | Guarantor | Admin section |
|---|---|---|---|
| Employment status | `borrower_employment_status` (+ `_text`) | `guarantor_employment_status` (+ `_text`) | Borrower / Guarantor Income Information |
| Industry | `borrower_industry` → `users_employmentindustry` | `guarantor_industry` | same |
| Position | `borrower_position` | `guarantor_position` | same |

Key files under `/data/code/core-loans`:

- `loans/mixins/loan_profile_info.py` — borrower/guarantor employment status FKs
- `loans/mixins/loan_guarantor.py` — `guarantor_industry`, `guarantor_position`, `is_self_guaranteed`
- `loans/models/loan_application.py` — `borrower_industry`, `borrower_position`
- `loans/admin/views/id_loan_application_child_admin.py` — Borrower Income Information fieldset
- `users/models/employment_status.py`, `users/models/employment_industry.py`

**Hard-reject categories** (match if **any** of status name, industry name, or
position text indicates the category — case-insensitive / fuzzy):

| Category | Typical `users_employmentstatus.name` | Typical `users_employmentindustry.name` | Position / free-text cues |
|---|---|---|---|
| TNI / military | `Militer` | `Pemerintah/Pertahanan` | TNI, tentara, militer |
| POLRI / police | `Polisi` | `Keamanan/Penegakan Hukum` | POLRI, polisi |
| Lawyer | `Pengacara / Notaris` | `Legal/Hukum` | pengacara, advokat, notaris, lawyer |
| Journalist | — | `Hiburan/Media/Jurnalisme` | jurnalis, wartawan, journalist |
| Collection agency | — | — | collection, debt collector, penagihan, collection agency |
| Security | `Pengamanan` | `Keamanan/Penegakan Hukum` | satpam, security, keamanan, pengamanan |

| hint | Meaning |
|---|---|
| `guarantor_type` / `is_self_guaranteed` | Which party's job fields to evaluate |
| `*_employment_status` / `*_employment_status_text` | FK / denormalized status name |
| `*_industry` / `employment_industry_name` | FK → `users_employmentindustry.name` |
| `*_position` | Free-text job title |

```sql
SELECT
  la.reference_code,
  la.guarantor_type,
  bes.name AS borrower_employment_status,
  bi.name AS borrower_industry,
  la.borrower_position,
  ges.name AS guarantor_employment_status,
  gi.name AS guarantor_industry,
  la.guarantor_position
FROM loans_loanapplication la
LEFT JOIN loans_idloanapplication ida ON ida.loanapplication_ptr_id = la.id
LEFT JOIN users_employmentstatus bes ON bes.id = ida.borrower_employment_status_id
LEFT JOIN users_employmentindustry bi ON bi.id = la.borrower_industry_id
LEFT JOIN users_employmentstatus ges ON ges.id = ida.guarantor_employment_status_id
LEFT JOIN users_employmentindustry gi ON gi.id = la.guarantor_industry_id
WHERE la.reference_code = {{reference_code}};
```

(Confirm whether employment status FKs live on `loans_idloanapplication` vs
`loans_loanapplication` in Metabase before querying.) Any restricted match →
criterion `restricted_occupation_hard_reject` **fail**. All three relevant fields
empty → `insufficient_data`.

## Affordability / DBR

**Critical:** ID DBR is a **runtime `@property`** on `IdLoanApplication` — not a DB /
Metabase column. Do **not** `SELECT borrower_debt_burden_ratio` /
`guarantor_debt_burden_ratio` (those names are Python properties only). Absence of
a stored DBR column is **not** `insufficient_data`.

### core-loans display + formula (source of truth)

Admin: **ID loanapplication changeview → Auto Approve Indicator → Debt burden ratio**
(`IdLoanApplicationChildAdmin.debt_burden_ratio`).

| Admin / property | Code path |
|---|---|
| **Debt burden ratio** | Self guaranteed → `borrower_debt_burden_ratio`; else → `guarantor_debt_burden_ratio` |
| **Max DBR deviation** | `max_dbr_deviation` via `IdProfile.get_max_dbr_deviation_by_income` + `DebtBurdenRatioDeviationTier` |
| **Is within DBR deviation** | `is_within_max_dbr_deviation` (`DBR <= max_dbr_deviation`) |

Key files under `/data/code/core-loans`:

- `loans/models/id_loan_application.py` — `borrower_debt_burden_ratio`, `guarantor_debt_burden_ratio`, `*_current_total_installment`, `get_total_installment_by_ktp_card_number`, `max_dbr_deviation`, `is_within_max_dbr_deviation`
- `loans/admin/views/id_loan_application_child_admin.py` — Auto Approve Indicator fieldset
- `loans/mixins/loan_guarantor.py` — `SELF_GUARANTEED = "Self Guaranteed"`, `is_self_guaranteed`
- `users/models/id_profile.py` — `get_max_dbr_deviation_by_income`
- `users/models/auto_top_up_config.py` — `DebtBurdenRatioDeviationTier`
- `loans/managers/loan.py` — `Loan.objects.active()` statuses

**Party**

- `guarantor_type == "Self Guaranteed"` (`is_self_guaranteed`) → **borrower** DBR
- otherwise → **guarantor** DBR

**Formula (single-party DBR shown in admin)**

\[
\mathrm{DBR} = \frac{\text{active installments by KTP} + \text{current app installment}}{\text{verified income OR declared income OR } 1}
\]

**Numerator**

1. **Active loans** (`get_total_installment_by_ktp_card_number`):
   - `loans_loan.status IN ('Agreement Activated', 'Written Off', 'For Pre Termination')`
   - KTP matches as **borrower** (`loans_idloanapplication.ktp_id_card_number`) **or** as **guarantor** (`guarantor_ktp_id_card_number`)
   - Exclude current application (`loan_application_id != this app`)
   - Sum `loans_loan.approved_monthly_repayment`
   - If party KTP missing → active portion **0**
2. **Current application installment**:
   - `approved_monthly_repayment OR requested_monthly_repayment` on this loan application
   - (Not `*_total_monthly_payment`)

**Denominator**

- Borrower: `borrower_verified_monthly_income or borrower_monthly_income or 1`
- Guarantor: `guarantor_verified_monthly_income or guarantor_monthly_income or 1`
- Core uses `or 1` to avoid div-by-zero for admin display. For Decision Notes: if
  relevant income is missing **and** no admin DBR was pasted → `insufficient_data`
  (do not silently use denominator `1` to invent a tiny/huge DBR for approve/reject).

**Do not** use profile `total_active_installment` for this criterion — that uses a
different status set than Auto Approve DBR.

### Evidence hints

| hint | Meaning |
|---|---|
| `dbr` / `dbr_runtime` / `debt_burden_ratio` | Admin Auto Approve Indicator value, or recompute with formula above |
| `guarantor_type` / `is_self_guaranteed` | `"Self Guaranteed"` → borrower party; else guarantor |
| `ktp_id_card_number` / `guarantor_ktp_id_card_number` | KTP used to sum active installments for the party |
| `active_monthly_installments` | Σ `approved_monthly_repayment` on `Loan.objects.active()` matched by party KTP (borrower or guarantor role), excluding this app |
| `application_monthly_installment` | This app: `approved_monthly_repayment or requested_monthly_repayment` |
| `borrower_verified_monthly_income` / `guarantor_verified_monthly_income` | Preferred denominator |
| `borrower_monthly_income` / `guarantor_monthly_income` | Declared fallback denominator |
| `relevant_monthly_income` | Income for min-income criterion (≥ 3_000_000); same party rule as DBR |
| `max_dbr_deviation` / `debt_burden_ratio_max_deviation` | Income-band cap from `users_debtburdenratiodeviationtier` (supporting; Auto Approve uses `DBR <= max`) |
| `is_within_max_dbr_deviation` | Admin “Is within DBR deviation”; supporting context |
| `dual_income_debt_burden_ratio` | Separate property when primary income provider is Both; **not** the main admin Debt burden ratio |
| `requested_loan_amount`, `tenor` | Affordability narrative inputs |

### How to resolve DBR for Decision Notes

1. Prefer **pasted/admin** Auto Approve Indicator → Debt burden ratio when given
   (authoritative runtime value).
2. Else recompute with the core-loans formula above via Metabase inputs.
3. Missing active-loan rows → treat active Σ as **0** (still add current app
   installment). Never `insufficient_data` only because no other active loans exist
   or because Metabase has no `*_debt_burden_ratio` column.
4. Pack hard rule remains **DBR < 50%**. Also quote `max_dbr_deviation` when known
   (Auto Approve gate is `DBR <= max_dbr_deviation`, often stricter than 50% at
   lower incomes).
5. Quote observed DBR as a percentage (e.g. 12.85% vs threshold 50%).

### Metabase / SQL sketch (inputs only; DBR computed in skill)

```sql
-- Party KTP + incomes + this-app installment
SELECT
  la.reference_code,
  la.guarantor_type,
  ida.ktp_id_card_number,
  ida.guarantor_ktp_id_card_number,
  la.borrower_verified_monthly_income,
  la.borrower_monthly_income,
  la.guarantor_verified_monthly_income,
  la.guarantor_monthly_income,
  la.approved_monthly_repayment,
  la.requested_monthly_repayment
FROM loans_loanapplication la
JOIN loans_idloanapplication ida ON ida.loanapplication_ptr_id = la.id
WHERE la.reference_code = {{reference_code}};

-- Active installments by a KTP (borrower OR guarantor role), exclude this app
SELECT COALESCE(SUM(l.approved_monthly_repayment), 0) AS active_monthly_installments
FROM loans_loan l
JOIN loans_idloanapplication ida
  ON ida.loanapplication_ptr_id = l.loan_application_id
WHERE l.status IN ('Agreement Activated', 'Written Off', 'For Pre Termination')
  AND l.loan_application_id <> {{loan_application_id}}
  AND (
    ida.ktp_id_card_number = {{party_ktp}}
    OR ida.guarantor_ktp_id_card_number = {{party_ktp}}
  );
```

## CLIK / FDC

Primary bureau for ID Decision Notes is **FDC**. CLIK requires a **human
trigger** in admin (`credit_report_inquiry`) — the agent must **not** query or
evaluate CLIK. If FDC is **Not Found**, note that the user/ops should manually
check CLIK, and prefer suggestion **`escalate`**.

### Reliability rules (mandatory)

1. Use the **canonical FDC fact SQL** below first. Prefer
   `inquiries_idinquirydata.loan_application_id` + `kind` — do **not** depend
   only on the M2M `idinquirydata_fdc_inquiries` join (easy to break).
2. If `IdInquiryLog.status = Found` for the relevant party `kind`, facility rows
   are expected. A failed/empty facility query is a **tooling problem**, not
   “DPD unavailable”:
   - Retry the canonical SQL once.
   - If still failing: suggestion **`escalate`**, confidence **`low`**, do **not**
     publish medium-confidence Notes that mark active/closed/WO as
     `insufficient_data` as if bureau data were missing.
3. Phone mismatch is a **soft** history fail only. It must **not** stop fetching
   or evaluating DPD / Written Off criteria.
4. `status_pinjaman` buckets (AFPI → core-loans `convert_status_pinjaman`):
   - Active DPD rule: **`Agreement Activated`** only (`O`)
   - Closed max-DPD rule: **`Closed`** only (`L`)
   - Written Off hard rule: **`Written Off`** / **`Written Off Closed`** (`W`/`S`/`F`)
   - Never treat Written Off as Closed.

### FDC (agent evaluates)

Admin: loan application / profile **FDC Summary** + `InquiryFDCLogsInline` /
`InquiryFDCInline`.

| hint | Meaning |
|---|---|
| `fdc` | Fintech Data Center inquiry |
| `inquiry_status` | `Found` / `Not Found` / `Failed` on `IdInquiryLog.status` |
| `inquiry_kind` | Borrower vs Guarantor (`log.kind` / `IdInquiryData.kind`) |
| `fdc_mobile_number` | `inquiries_idinquirydata.mobile_number` (AFPI `no_hp`) |
| `fdc_phone_match_count` / `fdc_phone_mismatch_count` | Counts after normalize |
| `borrower_mobile_number` | `users_user.username` |
| `guarantor_mobile_number` | `loans_loanapplication.guarantor_mobile_number` |
| `guarantor_type` / `is_self_guaranteed` | Party for phone + facility `kind` |
| `status_pinjaman` | Facility status string after convert |
| `fdc_active_max_dpd` / `current_dpd` | Worst DPD among **Agreement Activated** (must be 0) |
| `fdc_closed_max_dpd` / `max_dpd` | Worst max DPD among **Closed** (must be ≤ 30) |
| `fdc_written_off_count` / `fdc_written_off_max_dpd` | WO / WO Closed presence + worst DPD |
| `outstanding_amount` | Supporting evidence on WO rows |

**Party `kind`:** Self Guaranteed → `Borrower`; else → `Guarantor`.

**Phone match (`fdc_credit_history` when Found)**

1. Party phone: Self Guaranteed → borrower username; else → `guarantor_mobile_number`.
2. Compare to every non-empty `mobile_number` on facility rows for that `kind`.
3. Normalize `+62` / `62` / `08` before compare.
4. Evidence **must** quote: party phone source, match count, mismatch count, and
   distinct FDC mobiles (**masked**, e.g. `+628***851`).
5. All match → pass. Any mismatch → soft **fail**. Missing party phone or all
   FDC mobiles blank → `insufficient_data`.

### When FDC = Not Found (human CLIK only)

1. Do **not** SELECT/evaluate `credit_report_*` / CLIK.
2. Soft history → `insufficient_data`; active/closed/WO DPD criteria →
   `not_applicable`.
3. Notes/next action: user must **manually** run/review CLIK.
4. Prefer suggestion **`escalate`**.

If FDC = **Failed** → `insufficient_data` (retry FDC); do not auto-check CLIK.

### Canonical FDC fact SQL (use this)

```sql
-- 1) Latest log per kind for this application
SELECT id, status, kind, datetime_created, reason
FROM inquiries_idinquirylog
WHERE loan_application_id = {{loan_application_id}}
ORDER BY datetime_created DESC;

-- 2) Facilities for the relevant party (PRIMARY path — prefer this)
SELECT
  d.id,
  d.kind,
  d.status_pinjaman,
  d.current_dpd,
  d.max_dpd,
  d.outstanding_amount,
  d.mobile_number,
  d.past_due_bucket,
  d.name
FROM inquiries_idinquirydata d
WHERE d.loan_application_id = {{loan_application_id}}
  AND d.kind = {{party_kind}}  -- 'Borrower' or 'Guarantor'
ORDER BY d.status_pinjaman, d.max_dpd DESC NULLS LAST;

-- 3) Party phone for match
SELECT
  la.reference_code,
  la.guarantor_type,
  u.username AS borrower_mobile_number,
  la.guarantor_mobile_number
FROM loans_loanapplication la
JOIN users_user u ON u.id = la.borrower_id
WHERE la.id = {{loan_application_id}};
```

Optional summary aggregates after fetch:

| Metric | Definition |
|---|---|
| active worst DPD | `MAX(current_dpd)` where `status_pinjaman = 'Agreement Activated'` |
| closed worst max DPD | `MAX(max_dpd)` where `status_pinjaman = 'Closed'` |
| WO count | rows where `status_pinjaman IN ('Written Off','Written Off Closed')` |
| WO worst max DPD | `MAX(max_dpd)` on those WO rows |

Core-loans: `inquiries/models.py` (`IdInquiryLog`, `IdInquiryData`,
`convert_status_pinjaman`); `afpi/businesses.py` (`no_hp` → `mobile_number`).

## Partner priority

| hint | Meaning |
|---|---|
| `partner_name` | School / partner display name on the application |
| `partner_type` | Formal vs non-formal if available |
| `loan_product` / `product_name` | Needed for RevoU SNPL exclusion |

Match allowlist names fuzzily (e.g. UBSI ↔ Universitas Bina Sarana Informatika). RevoU with product SNPL fails the priority-partner criterion.

## Privacy

Return only fields needed for criteria. Mask phones/emails. Do not dump KTP or full addresses into Decision Notes.
