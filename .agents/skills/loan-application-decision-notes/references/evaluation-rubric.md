# Evaluation rubric

## Criterion results

For each criterion in pack order (`sort_order`):

| Result | When |
|---|---|
| `pass` | Facts satisfy the prompt / threshold |
| `fail` | Facts clearly violate the prompt / threshold |
| `insufficient_data` | Needed facts missing, null, or inquiry failed without usable data |
| `not_applicable` | Criterion does not apply to this application shape |
| `skipped` | Not evaluated because a prior **hard** `fail` triggered `stop_on_hard_fail` |

Never invent numbers. Prefer `insufficient_data` over guessing — **except** when a
Metabase/tool query failed while the bureau log says data should exist (see FDC
reliability). In that case prefer **retry → escalate**, not fake missing data.

## Short-circuit on hard fail (mandatory)

Evaluate criteria in pack `sort_order`. If
`decision_policy.stop_on_hard_fail` is true (demo pack default):

1. As soon as any **hard** criterion returns **`fail`**, **stop**. Do not evaluate
   later criteria. Do not fetch more facts solely for later criteria.
2. Emit Decision Notes immediately with suggestion **`reject`** when
   `reject_if_any_hard_fail` is true.
3. In the checklist: include results for criteria evaluated so far; mark all
   remaining criteria as **`skipped`** (not `pass` / `fail` /
   `insufficient_data` / `not_applicable`) with evidence like “dihentikan setelah
   hard fail pada `{criterion_id}`”.
4. Soft `fail` does **not** short-circuit — continue evaluating.
5. Hard `insufficient_data` / `not_applicable` do **not** short-circuit — continue.

Gather facts **lazily** when possible: only load what the current criterion needs.
After a hard fail, skip remaining Metabase queries for unchecked criteria.

## Threshold criteria

When `polarity` is `threshold` and `threshold` is set:

1. Resolve the metric from facts (see [field-hints.md](field-hints.md)).
2. Compare with `op` + `value` (`lt` `lte` `gt` `gte` `eq`).
3. Ratios: `0.5` means 50%. Quote both observed and threshold in evidence.

### DBR specifically

- Treat DBR as a **runtime** `IdLoanApplication` property (Gubat Auto Approve
  Indicator → Debt burden ratio), not a warehouse column. Recompute with the
  core-loans formula in [field-hints.md](field-hints.md) when admin value is
  not pasted.
- Party: Self Guaranteed → borrower; else guarantor.
- Numerator: active `approved_monthly_repayment` by party KTP (borrower **or**
  guarantor role on other apps; statuses Agreement Activated / Written Off /
  For Pre Termination) **plus** this app’s
  `approved_monthly_repayment or requested_monthly_repayment`.
- Denominator: verified income or declared income for that party.
- Never mark `insufficient_data` solely because Metabase has no
  `*_debt_burden_ratio` column **or** no other active loans (missing active Σ →
  **0**).
- `insufficient_data` if this application’s monthly repayment **or** relevant
  party income is unavailable (and no admin DBR was provided). Do not use
  core’s silent denominator `1` for Decision Notes judgment.
- Pack threshold remains DBR `< 50%`. Quote `max_dbr_deviation` when known
  (Auto Approve uses `DBR <= max_dbr_deviation`).

### FDC reliability + CLIK (human only)

Use the canonical FDC SQL in [field-hints.md](field-hints.md)
(`inquiries_idinquirydata` filtered by `loan_application_id` + `kind`).

| FDC log | Facilities fetched | History / phone | Active DPD | Closed max DPD | Written Off |
|---|---|---|---|---|---|
| Found | success, has rows | evaluate phone match | Agreement Activated only; else N/A | Closed only; else N/A | any WO/WO Closed → **hard fail** |
| Found | success, 0 rows for a bucket | — | N/A if no active | N/A if no closed | **pass** if no WO |
| Found | query **failed** / unexpectedly empty | do **not** invent missing DPD | retry → else **escalate**, confidence **low** | same | same |
| Not Found | — | `insufficient_data` + ask human CLIK | `not_applicable` | `not_applicable` | `not_applicable` |
| Failed | — | `insufficient_data` (retry FDC) | `insufficient_data` | `insufficient_data` | `insufficient_data` |

Additional FDC rules:

- Prefer **FDC** when Found; evaluate DPD/WO on FDC only.
- Phone match is required for soft `fdc_credit_history` when Found; evidence must
  include match/mismatch counts and masked FDC mobiles.
- Phone mismatch must **not** block DPD/WO evaluation.
- Never treat **Written Off** as **Closed**.
- If FDC is **Not Found**, do **not** query CLIK; ask user to check CLIK
  manually; prefer suggestion **`escalate`**.

## Narrative / prefer_true / prefer_false

Judge from `prompt` + facts + `notes`. State the observed evidence in the Notes language (pack `locale`).

## Decision policy → suggestion

Read pack `decision_policy`:

1. Evaluate in `sort_order`. On first **hard** `fail`, if `stop_on_hard_fail` →
   stop and go to step 2 (do not run remaining criteria).
2. If any evaluated **hard** criterion is `fail` and `reject_if_any_hard_fail`
   is true → `reject`.
3. Else if any evaluated criterion is `insufficient_data` that blocks a hard
   rule (or multiple soft gaps) → usually `request_more_info` (or pack
   `otherwise_suggestion`).
4. Else count evaluated **soft** `fail`s:
   - If soft fails ≤ `max_soft_fails_for_approve` and no hard fail → `approve`.
   - Else → pack `otherwise_suggestion` (demo default: `request_more_info`).
5. Prefer `escalate` when:
   - FDC is Not Found (ask user to manually check CLIK), **or**
   - FDC is Found but facility/DPD queries failed after retry, **or**
   - facts conflict / judgment is clearly above skill scope.

`informational` criteria never drive reject/approve alone; they may appear under strengths/weaknesses.
`skipped` criteria (after hard-fail short-circuit) never drive the suggestion.

## Confidence

- **high**: all material criteria have `pass` or `fail` with clear evidence
- **medium**: minor gaps or soft narrative judgment
- **low**: missing bureau / income / installment inputs needed for material
  criteria (not merely missing a stored DBR column), **or** any required
  Metabase/`query.py` call failed while assessing FDC/DBR/identity facts

Never publish **medium/high** confidence Decision Notes that claim FDC DPD is
unavailable when the only problem was a failed SQL join/query and the FDC log
is Found.

## Locale (required)

Pack `locale` controls the **entire Decision Notes block**:

- Section headings from the label map in [decision-notes.template.md](../assets/decision-notes.template.md)
- Summary, strengths, weaknesses, evidence prose, next action
- Localized suggestion and confidence labels

Do not mix languages inside the Notes. Chat framing outside the Notes block may follow the user.
