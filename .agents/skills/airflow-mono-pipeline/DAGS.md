# Erudifi Airflow DAG catalog (mono-pipeline)

Catalog of DAGs with Airflow `is_active=true` on `https://airflow.erudifi.com`.
Generated **2026-07-31** · **137** active DAG IDs (77 unpaused, 60 paused).

Use this file to answer what a DAG does without re-reading the repo. Confirm live run/pause status with `scripts/airflow_api.py` when operating on production.

**Source repo:** `/data/code/mono-pipeline`  
**Refresh:** `python3 .agents/skills/airflow-mono-pipeline/scripts/generate_dag_catalog.py`

Schedules are Airflow-stored values; many DAG files use timezone `Asia/Jakarta`.

## Quick index (unpaused only)

- [`activations_ftl_targets_ph`](#activations_ftl_targets_ph) — Daily Google Sheet ingest for `activations_ftl_targets_ph` into Athena Iceberg `integrated` (Bash → codes E...
- [`activations_mip_targets_ph`](#activations_mip_targets_ph) — Daily Google Sheet ingest for `activations_mip_targets_ph` into Athena Iceberg `integrated` (Bash → codes E...
- [`athena_borrower_base`](#athena_borrower_base) — Rebuilds Athena Iceberg `summaries.borrower_base` daily (write-truncate) from datamart SQL.
- [`athena_borrower_demography`](#athena_borrower_demography) — Rebuilds Athena Iceberg `summaries.borrower_demography` daily from datamart SQL.
- [`athena_bukas_daily_accounting_repayment`](#athena_bukas_daily_accounting_repayment) — Builds/updates Athena `summaries.bukas_daily_accounting_repayment` (bukas daily accounting repayment).
- [`athena_bukas_daily_accounting_repayment_clean`](#athena_bukas_daily_accounting_repayment_clean) — Builds/updates Athena `summaries.bukas_daily_accounting_repayment_clean` (bukas daily accounting repayment ...
- [`athena_cash_on_cash_id`](#athena_cash_on_cash_id) — Builds/updates Athena `summaries.cash_on_cash_id` (cash on cash id).
- [`athena_cash_on_cash_id_clean`](#athena_cash_on_cash_id_clean) — Manual/clean rebuild for cash on cash id clean in Athena `summaries`.
- [`athena_cash_on_cash_ph`](#athena_cash_on_cash_ph) — Builds/updates Athena `summaries.cash_on_cash_ph` (cash on cash ph).
- [`athena_cash_on_cash_ph_clean`](#athena_cash_on_cash_ph_clean) — Manual/clean rebuild for cash on cash ph clean in Athena `summaries`.
- [`athena_daily_accounting_repayment`](#athena_daily_accounting_repayment) — Builds/updates Athena `summaries.daily_accounting_repayment` (daily accounting repayment).
- [`athena_daily_accounting_repayment_clean`](#athena_daily_accounting_repayment_clean) — Builds/updates Athena `summaries.daily_accounting_repayment_clean` (daily accounting repayment clean).
- [`athena_daily_deliquent_loan`](#athena_daily_deliquent_loan) — Builds/updates Athena `integrated.daily_deliquent_loan` (daily deliquent loan).
- [`athena_daily_dim_product`](#athena_daily_dim_product) — Builds/updates Athena `integrated.dim_product` (daily dim product).
- [`athena_daily_erudifi_loanbook`](#athena_daily_erudifi_loanbook) — Builds/updates Athena `integrated.daily_erudifi_loanbook` (daily erudifi loanbook).
- [`athena_daily_fact_loan`](#athena_daily_fact_loan) — Builds/updates Athena `integrated.fact_loan` (daily fact loan).
- [`athena_daily_group_npl_date`](#athena_daily_group_npl_date) — Write-truncate rebuild for daily group npl date in Athena `summaries`.
- [`athena_daily_loan_activation`](#athena_daily_loan_activation) — Builds/updates Athena `summaries.daily_loan_activation` (daily loan activation).
- [`athena_daily_loanbook_id`](#athena_daily_loanbook_id) — Builds daily Danacita ID loanbook snapshot in Athena `summaries` (can trigger cash-on-cash).
- [`athena_daily_loanbook_ph`](#athena_daily_loanbook_ph) — Builds daily Bukas/PH loanbook snapshot in Athena `summaries`.
- [`athena_danacita_portfolio_monthly`](#athena_danacita_portfolio_monthly) — Builds/updates Athena `summaries.portfolio_monthly_update` (danacita portfolio monthly).
- [`athena_danacita_portfolio_weekly`](#athena_danacita_portfolio_weekly) — Builds/updates Athena `summaries.portfolio_weekly_update` (danacita portfolio weekly).
- [`athena_dim_partner_institution`](#athena_dim_partner_institution) — Builds/updates Athena `integrated.dim_partner_institution` (dim partner institution).
- [`athena_erudifi_loanbook_monthend_snapshot`](#athena_erudifi_loanbook_monthend_snapshot) — Write-truncate rebuild for erudifi loanbook monthend snapshot in Athena `summaries`.
- [`athena_loanbook_monthend_six`](#athena_loanbook_monthend_six) — Write-truncate rebuild for loanbook monthend six in Athena `summaries`.
- [`athena_ojk_master_daily_v2`](#athena_ojk_master_daily_v2) — Builds/updates Athena `reports.ojk_monthly_v2` (ojk master daily v2).
- [`athena_ojk_master_v2_clean`](#athena_ojk_master_v2_clean) — Builds/updates Athena `reports.ojk_master_v2_clean` (ojk master v2 clean).
- [`athena_portfolio_daily_update`](#athena_portfolio_daily_update) — Write-truncate rebuild for portfolio daily update in Athena `summaries`.
- [`athena_portfolio_monthly_snapshot`](#athena_portfolio_monthly_snapshot) — Scheduled snapshot build for portfolio monthly snapshot in Athena `summaries`.
- [`athena_portfolio_weekly_snapshot`](#athena_portfolio_weekly_snapshot) — Scheduled snapshot build for portfolio weekly snapshot in Athena `summaries`.
- [`athena_pusdafil_report_am`](#athena_pusdafil_report_am) — Morning Pusdafil regulatory report build into Athena `reports` (Athena + BigQuery operators).
- [`athena_pusdafil_report_pm`](#athena_pusdafil_report_pm) — Evening Pusdafil regulatory report build into Athena `reports` (Athena + BigQuery operators).
- [`athena_saved_queries_sync_to_variables`](#athena_saved_queries_sync_to_variables) — Syncs Athena named/saved queries into Airflow Variables (`athena_sql_*`) to reduce API throttling.
- [`athena_school_population`](#athena_school_population) — Builds/updates Athena `summaries.school_population` (school population).
- [`athena_summaries_daily_update`](#athena_summaries_daily_update) — Daily write-truncate rebuild of many Athena `summaries` tables (lenders, collections, growth, portfolio_dai...
- [`bsi_recontest_batch_1`](#bsi_recontest_batch_1) — Daily Google Sheet ingest for `bsi_recontest_batch_1` into Athena Iceberg `integrated` (Bash → codes ETL).
- [`bsi_recontest_batch_2`](#bsi_recontest_batch_2) — Daily Google Sheet ingest for `bsi_recontest_batch_2` into Athena Iceberg `integrated` (Bash → codes ETL).
- [`bukas_parquet_to_iceberg`](#bukas_parquet_to_iceberg) — Loads Bukas Parquet into Athena Iceberg tables.
- [`daily_raw_bukas`](#daily_raw_bukas) — Daily raw Bukas ingest orchestration (lakehouse/GCS path).
- [`daily_raw_dc`](#daily_raw_dc) — Daily raw Danacita ingest orchestration (lakehouse/GCS path).
- [`daily_slik_closed_loans`](#daily_slik_closed_loans) — Daily SLIK closed-loans extract into Athena `reports` with Slack notify.
- [`deduct_disbursement`](#deduct_disbursement) — Daily Google Sheet ingest for `deduct_disbursement` into Athena Iceberg `integrated` (Bash → codes ETL).
- [`disbursements_ftl_targets_ph`](#disbursements_ftl_targets_ph) — Daily Google Sheet ingest for `disbursements_ftl_targets_ph` into Athena Iceberg `integrated` (Bash → codes...
- [`disbursements_mip_targets_ph`](#disbursements_mip_targets_ph) — Daily Google Sheet ingest for `disbursements_mip_targets_ph` into Athena Iceberg `integrated` (Bash → codes...
- [`erudifi_targets_monthly`](#erudifi_targets_monthly) — Daily Google Sheet ingest for `erudifi_targets_monthly` into Athena Iceberg `integrated` (Bash → codes ETL).
- [`etl_test_loans`](#etl_test_loans) — Daily Google Sheet ingest for `etl_test_loans` into Athena Iceberg `integrated` (Bash → codes ETL).
- [`ewoff_list`](#ewoff_list) — Daily Google Sheet ingest for `ewoff_list` into Athena Iceberg `integrated` (Bash → codes ETL).
- [`finops_lender_mapping`](#finops_lender_mapping) — Daily Google Sheet ingest for `finops_lender_mapping` into Athena Iceberg `integrated` (Bash → codes ETL).
- [`fx_rate`](#fx_rate) — Daily Google Sheet ingest for `fx_rate` into Athena Iceberg `integrated` (Bash → codes ETL).
- [`general_courses_formal_id`](#general_courses_formal_id) — Daily Google Sheet ingest for `general_courses_formal_id` into Athena Iceberg `integrated` (Bash → codes ETL).
- [`general_courses_formal_ph`](#general_courses_formal_ph) — Daily Google Sheet ingest for `general_courses_formal_ph` into Athena Iceberg `integrated` (Bash → codes ETL).
- [`growth_analysis`](#growth_analysis) — Daily Google Sheet ingest for `growth_analysis` into Athena Iceberg `integrated` (Bash → codes ETL).
- [`institution_targets_disb_id`](#institution_targets_disb_id) — Daily Google Sheet ingest for `institution_targets_disb_id` into Athena Iceberg `integrated` (Bash → codes ...
- [`loan_products_id`](#loan_products_id) — Daily Google Sheet ingest for `loan_products_id` into Athena Iceberg `integrated` (Bash → codes ETL).
- [`loan_products_ph`](#loan_products_ph) — Daily Google Sheet ingest for `loan_products_ph` into Athena Iceberg `integrated` (Bash → codes ETL).
- [`loanbook_id`](#loanbook_id) — Daily Google Sheet ingest for `loanbook_id` into Athena Iceberg `integrated` (Bash → codes ETL).
- [`loanbook_ph`](#loanbook_ph) — Daily Google Sheet ingest for `loanbook_ph` into Athena Iceberg `integrated` (Bash → codes ETL).
- [`manual_adjustments`](#manual_adjustments) — Daily Google Sheet ingest for `manual_adjustments` into Athena Iceberg `integrated` (Bash → codes ETL).
- [`monthly_slik_active_loans`](#monthly_slik_active_loans) — Monthly SLIK active-loans report into Athena `reports` with Slack notify.
- [`new_target_2024`](#new_target_2024) — Daily Google Sheet ingest for `new_target_2024` into Athena Iceberg `integrated` (Bash → codes ETL).
- [`ojk_account_eca`](#ojk_account_eca) — Daily Google Sheet ingest for `ojk_account_eca` into Athena Iceberg `integrated` (Bash → codes ETL).
- [`ojk_gender_mapping`](#ojk_gender_mapping) — Daily Google Sheet ingest for `ojk_gender_mapping` into Athena Iceberg `integrated` (Bash → codes ETL).
- [`ojk_province_mapping`](#ojk_province_mapping) — Daily Google Sheet ingest for `ojk_province_mapping` into Athena Iceberg `integrated` (Bash → codes ETL).
- [`parquet_to_iceberg`](#parquet_to_iceberg) — Manual Parquet→Athena Iceberg load for core tables.
- [`parquet_to_iceberg_datamart`](#parquet_to_iceberg_datamart) — Loads Parquet into Athena Iceberg (`parquet_to_iceberg_datamart`).
- [`parquet_to_iceberg_datamart_v2`](#parquet_to_iceberg_datamart_v2) — Loads Parquet into Athena Iceberg (`parquet_to_iceberg_datamart_v2`).
- [`parquet_to_iceberg_datamart_v3`](#parquet_to_iceberg_datamart_v3) — Loads Parquet into Athena Iceberg (`parquet_to_iceberg_datamart_v3`).
- [`parquet_to_iceberg_v2`](#parquet_to_iceberg_v2) — Loads Parquet into Athena Iceberg (`parquet_to_iceberg_v2`).
- [`partner_base_id`](#partner_base_id) — Daily Google Sheet ingest for `partner_base_id` into Athena Iceberg `integrated` (Bash → codes ETL).
- [`partner_base_ph`](#partner_base_ph) — Daily Google Sheet ingest for `partner_base_ph` into Athena Iceberg `integrated` (Bash → codes ETL).
- [`partner_enrolment_ph`](#partner_enrolment_ph) — Daily Google Sheet ingest for `partner_enrolment_ph` into Athena Iceberg `integrated` (Bash → codes ETL).
- [`partners_calender_2023_ph`](#partners_calender_2023_ph) — Daily Google Sheet ingest for `partners_calender_2023_ph` into Athena Iceberg `integrated` (Bash → codes ETL).
- [`registration_targets_2023_ph`](#registration_targets_2023_ph) — Daily Google Sheet ingest for `registration_targets_2023_ph` into Athena Iceberg `integrated` (Bash → codes...
- [`report_date_adjustment`](#report_date_adjustment) — Daily Google Sheet ingest for `report_date_adjustment` into Athena Iceberg `integrated` (Bash → codes ETL).
- [`submit_ftl_targets_ph`](#submit_ftl_targets_ph) — Daily Google Sheet ingest for `submit_ftl_targets_ph` into Athena Iceberg `integrated` (Bash → codes ETL).
- [`submit_mip_targets_ph`](#submit_mip_targets_ph) — Daily Google Sheet ingest for `submit_mip_targets_ph` into Athena Iceberg `integrated` (Bash → codes ETL).
- [`tkb_landing_page`](#tkb_landing_page) — Daily Google Sheet ingest for `tkb_landing_page` into Athena Iceberg `integrated` (Bash → codes ETL).

## Athena / datamart & summaries

### `athena_borrower_base`
- **Purpose:** Rebuilds Athena Iceberg `summaries.borrower_base` daily (write-truncate) from datamart SQL.
- **Schedule:** `0 7 * * *`
- **Paused:** no
- **Source:** `dags/athena_borrower_base.py`
- **Tags:** datamart, daily, Write_truncate, Athena

### `athena_borrower_demography`
- **Purpose:** Rebuilds Athena Iceberg `summaries.borrower_demography` daily from datamart SQL.
- **Schedule:** `0 7 * * *`
- **Paused:** no
- **Source:** `dags/athena_ borrower_demography.py`
- **Tags:** daily, Write_truncate, Athena, datamart

### `athena_cash_on_cash_id`
- **Purpose:** Builds/updates Athena `summaries.cash_on_cash_id` (cash on cash id).
- **Schedule:** `15 7 * * *`
- **Paused:** no
- **Source:** `dags/athena_cash_on_cash_id.py`
- **Tags:** daily, Athena, snapshot, Danacita, datamart

### `athena_cash_on_cash_id_clean`
- **Purpose:** Manual/clean rebuild for cash on cash id clean in Athena `summaries`.
- **Schedule:** None (manual / no schedule)
- **Paused:** no
- **Source:** `dags/athena_cash_on_cash_id_clean.py`
- **Tags:** daily, Write_truncate, Athena, datamart

### `athena_cash_on_cash_ph`
- **Purpose:** Builds/updates Athena `summaries.cash_on_cash_ph` (cash on cash ph).
- **Schedule:** `15 7 * * *`
- **Paused:** no
- **Source:** `dags/athena_cash_on_cash_ph.py`
- **Tags:** daily, Athena, datamart, Danacita, snapshot

### `athena_cash_on_cash_ph_clean`
- **Purpose:** Manual/clean rebuild for cash on cash ph clean in Athena `summaries`.
- **Schedule:** None (manual / no schedule)
- **Paused:** no
- **Source:** `dags/athena_cash_on_cash_ph_clean.py`
- **Tags:** daily, Write_truncate, Athena, datamart

### `athena_daily_accounting_repayment`
- **Purpose:** Builds/updates Athena `summaries.daily_accounting_repayment` (daily accounting repayment).
- **Schedule:** `15 7 * * *`
- **Paused:** no
- **Source:** `dags/athena_daily_accounting_repayment.py`
- **Tags:** snapshot, Athena, datamart, daily, Danacita

### `athena_daily_accounting_repayment_clean`
- **Purpose:** Builds/updates Athena `summaries.daily_accounting_repayment_clean` (daily accounting repayment clean).
- **Schedule:** None (manual / no schedule)
- **Paused:** no
- **Source:** `dags/athena_daily_accounting_repayment_clean.py`
- **Tags:** snapshot, Athena, datamart, daily, Danacita

### `athena_daily_deliquent_loan`
- **Purpose:** Builds/updates Athena `integrated.daily_deliquent_loan` (daily deliquent loan).
- **Schedule:** `30 6 * * *`
- **Paused:** no
- **Source:** `dags/athena_daily_deliquent_loan.py`
- **Tags:** snapshot, Athena, Integrated, datamart, daily, Danacita

### `athena_daily_dim_product`
- **Purpose:** Builds/updates Athena `integrated.dim_product` (daily dim product).
- **Schedule:** `30 6 * * *`
- **Paused:** no
- **Source:** `dags/athena_daily_dim_product.py`
- **Tags:** snapshot, Athena, Integrated, datamart, daily, Danacita

### `athena_daily_erudifi_loanbook`
- **Purpose:** Builds/updates Athena `integrated.daily_erudifi_loanbook` (daily erudifi loanbook).
- **Schedule:** `30 6 * * *`
- **Paused:** no
- **Source:** `dags/athena_daily_erudifi_loanbook.py`
- **Tags:** snapshot, Athena, Integrated, datamart, daily, Danacita

### `athena_daily_fact_loan`
- **Purpose:** Builds/updates Athena `integrated.fact_loan` (daily fact loan).
- **Schedule:** `30 6 * * *`
- **Paused:** no
- **Source:** `dags/athena_daily_fact_loan.py`
- **Tags:** snapshot, Athena, Integrated, datamart, daily, Danacita

### `athena_daily_group_npl_date`
- **Purpose:** Write-truncate rebuild for daily group npl date in Athena `summaries`.
- **Schedule:** `0 9 * * *`
- **Paused:** no
- **Source:** `dags/athena_daily_group_npl_date.py`
- **Tags:** metabase-layer, Athena, Write_truncate, datamart, daily

### `athena_daily_loan_activation`
- **Purpose:** Builds/updates Athena `summaries.daily_loan_activation` (daily loan activation).
- **Schedule:** `0 7 * * *`
- **Paused:** no
- **Source:** `dags/athena_daily_loan_activation.py`
- **Tags:** Athena, snapshot, daily, datamart

### `athena_daily_loanbook_id`
- **Purpose:** Builds daily Danacita ID loanbook snapshot in Athena `summaries` (can trigger cash-on-cash).
- **Schedule:** `15 7 * * *`
- **Paused:** no
- **Source:** `dags/athena_daily_loanbook_id.py`
- **Tags:** daily, Athena, snapshot, Danacita, datamart

### `athena_daily_loanbook_ph`
- **Purpose:** Builds daily Bukas/PH loanbook snapshot in Athena `summaries`.
- **Schedule:** `30 7 * * *`
- **Paused:** no
- **Source:** `dags/athena_daily_loanbook_ph.py`
- **Tags:** daily, Athena, snapshot, Danacita, datamart

### `athena_danacita_portfolio_monthly`
- **Purpose:** Builds/updates Athena `summaries.portfolio_monthly_update` (danacita portfolio monthly).
- **Schedule:** `0 2 2 * *`
- **Paused:** no
- **Source:** `dags/athena_danacita_portfolio_monthly.py`
- **Tags:** snapshot, Athena, datamart, danacita, daily

### `athena_danacita_portfolio_weekly`
- **Purpose:** Builds/updates Athena `summaries.portfolio_weekly_update` (danacita portfolio weekly).
- **Schedule:** `45 7 * * TUE`
- **Paused:** no
- **Source:** `dags/athena_danacita_portfolio_weekly.py`
- **Tags:** weekly, snapshot, Athena, datamart, danacita

### `athena_dim_partner_institution`
- **Purpose:** Builds/updates Athena `integrated.dim_partner_institution` (dim partner institution).
- **Schedule:** None (manual / no schedule)
- **Paused:** no
- **Source:** `dags/athena_daily_ dim_partner_institution.py`
- **Tags:** snapshot, daily, Athena, datamart

### `athena_erudifi_loanbook_monthend_snapshot`
- **Purpose:** Write-truncate rebuild for erudifi loanbook monthend snapshot in Athena `summaries`.
- **Schedule:** `@monthly`
- **Paused:** no
- **Source:** `dags/athena_erudifi_loanbook_monthend.py`
- **Tags:** metabase-layer, Athena, Write_truncate, datamart, daily

### `athena_loanbook_monthend_six`
- **Purpose:** Write-truncate rebuild for loanbook monthend six in Athena `summaries`.
- **Schedule:** `@monthly`
- **Paused:** no
- **Source:** `dags/athena_loanbook_monthend_snapshot_six.py`
- **Tags:** metabase-layer, Athena, Write_truncate, datamart, daily

### `athena_monthly_loanbook_monthend`
- **Purpose:** Builds/updates Athena `summaries.monthly_loanbook_monthend_snapshot` (monthly loanbook monthend).
- **Schedule:** `0 7 1 * *`
- **Paused:** yes
- **Source:** `dags/athena_monthly_loanbook_monthend.py`
- **Tags:** snapshot, Athena, datamart, daily, Danacita

### `athena_monthly_partner_base`
- **Purpose:** Builds/updates Athena `summaries.partner_institution_datamart` (monthly partner base).
- **Schedule:** None (manual / no schedule)
- **Paused:** yes
- **Source:** `dags/athena_monthly_partner_base.py`
- **Tags:** monthly, datamart, snapshot, Danacita, Athena

### `athena_portfolio_daily_update`
- **Purpose:** Write-truncate rebuild for portfolio daily update in Athena `summaries`.
- **Schedule:** `0 9 * * *`
- **Paused:** no
- **Source:** `dags/athena_portfolio_daily copy.py` (deployed path; may be missing/renamed in local checkout)
- **Tags:** metabase-layer, Athena, Write_truncate, datamart, daily

### `athena_portfolio_monthly_snapshot`
- **Purpose:** Scheduled snapshot build for portfolio monthly snapshot in Athena `summaries`.
- **Schedule:** `0 2 2 * *`
- **Paused:** no
- **Source:** `dags/athena_portfolio_monthly_snapshot.py` (deployed path; may be missing/renamed in local checkout)
- **Tags:** Athena, Summaries, weekly, snapshot, Danacita, datamart

### `athena_portfolio_weekly_snapshot`
- **Purpose:** Scheduled snapshot build for portfolio weekly snapshot in Athena `summaries`.
- **Schedule:** `0 23 * * MON`
- **Paused:** no
- **Source:** `dags/athena_portfolio_weekly_snapshot.py` (deployed path; may be missing/renamed in local checkout)
- **Tags:** Athena, Summaries, weekly, snapshot, Danacita, datamart

### `athena_saved_queries_sync_to_variables`
- **Purpose:** Syncs Athena named/saved queries into Airflow Variables (`athena_sql_*`) to reduce API throttling.
- **Schedule:** `0 4 * * *`
- **Paused:** no
- **Source:** `dags/athena_saved_queries_sync_to_variables.py`
- **Tags:** sync, utility, athena

### `athena_school_population`
- **Purpose:** Builds/updates Athena `summaries.school_population` (school population).
- **Schedule:** `0 7 * * *`
- **Paused:** no
- **Source:** `dags/athena_school_population.py`
- **Tags:** snapshot, Athena, datamart, danacita, daily

### `athena_summaries_daily_snapshot`
- **Purpose:** Builds/updates Athena `summaries.bukas_daily_accounting_repayment` (summaries daily snapshot).
- **Schedule:** None (manual / no schedule)
- **Paused:** yes
- **Source:** `dags/athena_summaries_daily_snapshot.py`
- **Tags:** snapshot, datamart, daily, Athena

### `athena_summaries_daily_update`
- **Purpose:** Daily write-truncate rebuild of many Athena `summaries` tables (lenders, collections, growth, portfolio_daily_update, projections, etc.).
- **Schedule:** `0 7 * * *`
- **Paused:** no
- **Source:** `dags/athena_summaries_daily_update.py`
- **Tags:** datamart, daily, Write_truncate, Athena

## Athena / Bukas

### `athena_bukas_daily_accounting_repayment`
- **Purpose:** Builds/updates Athena `summaries.bukas_daily_accounting_repayment` (bukas daily accounting repayment).
- **Schedule:** `15 7 * * *`
- **Paused:** no
- **Source:** `dags/athena_bukas_daily_accounting_repayment.py`
- **Tags:** datamart, snapshot, daily, Athena, bukas

### `athena_bukas_daily_accounting_repayment_clean`
- **Purpose:** Builds/updates Athena `summaries.bukas_daily_accounting_repayment_clean` (bukas daily accounting repayment clean).
- **Schedule:** None (manual / no schedule)
- **Paused:** no
- **Source:** `dags/athena_bukas_darc.py`
- **Tags:** snapshot, Athena, bukas, datamart, daily

## Athena / OJK & Pusdafil

### `athena_ojk_master_daily_v2`
- **Purpose:** Builds/updates Athena `reports.ojk_monthly_v2` (ojk master daily v2).
- **Schedule:** `45 7 * * *`
- **Paused:** no
- **Source:** `dags/athena_ojk_master_daily_v2.py`
- **Tags:** snapshot, OJK, Athena, reports, datamart, daily

### `athena_ojk_master_v2_clean`
- **Purpose:** Builds/updates Athena `reports.ojk_master_v2_clean` (ojk master v2 clean).
- **Schedule:** None (manual / no schedule)
- **Paused:** no
- **Source:** `dags/athena_ojk_master_daily_v2_clean.py`
- **Tags:** snapshot, OJK, Athena, reports, datamart, daily

### `athena_ojk_monthly_master`
- **Purpose:** Scheduled snapshot build for ojk monthly master in Athena `reports`.
- **Schedule:** `0 2 2 * *`
- **Paused:** yes
- **Source:** `dags/athena_ojk_monthly_master.py` (deployed path; may be missing/renamed in local checkout)
- **Tags:** snapshot, OJK, Athena, reports, datamart, daily

### `athena_pusdafil_report_am`
- **Purpose:** Morning Pusdafil regulatory report build into Athena `reports` (Athena + BigQuery operators).
- **Schedule:** `0 9 * * *`
- **Paused:** no
- **Source:** `dags/athena_daily_pusdafil_am.py`
- **Tags:** daily, reports, athena, pusdafil

### `athena_pusdafil_report_pm`
- **Purpose:** Evening Pusdafil regulatory report build into Athena `reports` (Athena + BigQuery operators).
- **Schedule:** `30 21 * * *`
- **Paused:** no
- **Source:** `dags/athena_daily_pusdafil_pm.py`
- **Tags:** daily, pusdafil, reports, athena

## Daily facts / BigQuery layer & other

### `backfill_fact_loan`
- **Purpose:** Pipeline `backfill_fact_loan`. Tags: integration-layer.
- **Schedule:** None (manual / no schedule)
- **Paused:** yes
- **Source:** `dags/daily_fact_loan_backfill.py`
- **Tags:** integration-layer

### `bi_query_datamart`
- **Purpose:** Pipeline `bi_query_datamart`. Tags: datamart-layer.
- **Schedule:** `0 8 * * *`
- **Paused:** yes
- **Source:** `dags/bi_query_datamart.py` (deployed path; may be missing/renamed in local checkout)
- **Tags:** datamart-layer

### `daily_borrower_base_snapshot`
- **Purpose:** Pipeline `daily_borrower_base_snapshot`. Tags: metabase-layer.
- **Schedule:** `0 7 * * *`
- **Paused:** yes
- **Source:** `dags/daily_borrower_base.py` (deployed path; may be missing/renamed in local checkout)
- **Tags:** metabase-layer

### `daily_erudifi_job`
- **Purpose:** Pipeline `daily_erudifi_job`. Tags: integration-layer.
- **Schedule:** `30 7 * * *`
- **Paused:** yes
- **Source:** `dags/daily_erudifi_job.py`
- **Tags:** integration-layer

### `daily_ga_data_normalize`
- **Purpose:** Pipeline `daily_ga_data_normalize`. Tags: ga-data.
- **Schedule:** `@daily`
- **Paused:** yes
- **Source:** `dags/daily_ga_data.py` (deployed path; may be missing/renamed in local checkout)
- **Tags:** ga-data

### `daily_group_npl_date`
- **Purpose:** Pipeline `daily_group_npl_date`. Tags: metabase-layer.
- **Schedule:** `0 9 * * *`
- **Paused:** yes
- **Source:** `dags/daily_group_npl_date.py` (deployed path; may be missing/renamed in local checkout)
- **Tags:** metabase-layer

### `daily_loan_activation`
- **Purpose:** Pipeline `daily_loan_activation`. Tags: metabase-layer.
- **Schedule:** `0 7 * * *`
- **Paused:** yes
- **Source:** `dags/daily_loan_activation.py`
- **Tags:** metabase-layer

### `daily_loan_outstanding`
- **Purpose:** Pipeline `daily_loan_outstanding`. Tags: integration-layer.
- **Schedule:** `0 3 * * *`
- **Paused:** yes
- **Source:** `dags/daily_loan_outstanding.py`
- **Tags:** integration-layer

### `daily_loanbook_projections_base`
- **Purpose:** Loanbook materialization pipeline (`daily_loanbook_projections_base`).
- **Schedule:** `50 22 * * *`
- **Paused:** yes
- **Source:** `dags/daily_projection_base.py`
- **Tags:** integration-layer

### `daily_school_population`
- **Purpose:** Pipeline `daily_school_population`. Tags: metabase-layer.
- **Schedule:** `0 7 * * *`
- **Paused:** yes
- **Source:** `dags/daily_school_population.py`
- **Tags:** metabase-layer

### `danacita_portfolio_daily`
- **Purpose:** Portfolio snapshot/update pipeline (`danacita_portfolio_daily`).
- **Schedule:** `0 7 * * *`
- **Paused:** yes
- **Source:** `dags/portfolio_daily.py`
- **Tags:** integration-layer

### `danacita_portfolio_monthly`
- **Purpose:** Portfolio snapshot/update pipeline (`danacita_portfolio_monthly`).
- **Schedule:** `0 2 2 * *`
- **Paused:** yes
- **Source:** `dags/portfolio_monthly.py`
- **Tags:** integration-layer

### `danacita_portfolio_weekly`
- **Purpose:** Portfolio snapshot/update pipeline (`danacita_portfolio_weekly`).
- **Schedule:** `0 23 * * MON`
- **Paused:** yes
- **Source:** `dags/portfolio_weekly.py`
- **Tags:** integration-layer

### `data_bank_weekly_snapshot`
- **Purpose:** Pipeline `data_bank_weekly_snapshot`. Tags: FINANCE, DATA-BANK.
- **Schedule:** `0 22 * * MON`
- **Paused:** yes
- **Source:** `dags/data_bank_weekly_snapshot.py` (deployed path; may be missing/renamed in local checkout)
- **Tags:** FINANCE, DATA-BANK

### `dc_mktg_raw`
- **Purpose:** Pipeline `dc_mktg_raw`.
- **Schedule:** `0 6,12,22 * * *`
- **Paused:** yes
- **Source:** `dags/dc_mktg_raw.py` (deployed path; may be missing/renamed in local checkout)
- **Tags:** _(none)_

### `loanbook_monthend_six`
- **Purpose:** Loanbook materialization pipeline (`loanbook_monthend_six`).
- **Schedule:** `0 7 6 * *`
- **Paused:** yes
- **Source:** `dags/monthend_erudifi_job_enhance.py`
- **Tags:** integration-layer

### `monthend_borrower_base`
- **Purpose:** Pipeline `monthend_borrower_base`. Tags: metabase-layer.
- **Schedule:** `0 7 1 * *`
- **Paused:** yes
- **Source:** `dags/monthend_borrower_base.py`
- **Tags:** metabase-layer

### `monthend_erudifi_job`
- **Purpose:** Pipeline `monthend_erudifi_job`. Tags: integration-layer.
- **Schedule:** `@monthly`
- **Paused:** yes
- **Source:** `dags/monthend_erudifi_job.py`
- **Tags:** integration-layer

### `monthly_erudifi_job`
- **Purpose:** Pipeline `monthly_erudifi_job`. Tags: integration-layer.
- **Schedule:** `@monthly`
- **Paused:** yes
- **Source:** `dags/monthly_erudifi_job.py`
- **Tags:** integration-layer

### `monthly_loanbook_monthend`
- **Purpose:** Loanbook materialization pipeline (`monthly_loanbook_monthend`).
- **Schedule:** `0 7 1 * *`
- **Paused:** yes
- **Source:** `dags/monthly_loanbook_monthend.py`
- **Tags:** loanbook_monthend

### `postgres_to_bigquery_pipeline_v2`
- **Purpose:** Pipeline `postgres_to_bigquery_pipeline_v2`.
- **Schedule:** None (manual / no schedule)
- **Paused:** yes
- **Source:** `dags/test_dag_v2.py`
- **Tags:** _(none)_

## Accounting / finance

### `bukas_daily_accounting_repayment`
- **Purpose:** Accounting repayment fact/snapshot pipeline (`bukas_daily_accounting_repayment`).
- **Schedule:** `0 7 * * *`
- **Paused:** yes
- **Source:** `dags/bukas_daily_accounting_repayment.py`
- **Tags:** metabase-layer

### `bukas_daily_accounting_repayment_clean`
- **Purpose:** Accounting repayment fact/snapshot pipeline (`bukas_daily_accounting_repayment_clean`).
- **Schedule:** None (manual / no schedule)
- **Paused:** yes
- **Source:** `dags/bukas_daily_darc.py`
- **Tags:** metabase-layer

### `click_monthly_report`
- **Purpose:** Pipeline `click_monthly_report`. Tags: datamart-layer.
- **Schedule:** `0 23 1 * *`
- **Paused:** yes
- **Source:** `dags/click_monthly_data.py`
- **Tags:** datamart-layer

### `daily_accounting_repayment`
- **Purpose:** Accounting repayment fact/snapshot pipeline (`daily_accounting_repayment`).
- **Schedule:** `0 7 * * *`
- **Paused:** yes
- **Source:** `dags/daily_accounting_repayment.py`
- **Tags:** metabase-layer

### `daily_accounting_repayment_bukas`
- **Purpose:** Accounting repayment fact/snapshot pipeline (`daily_accounting_repayment_bukas`).
- **Schedule:** `0 7 * * *`
- **Paused:** yes
- **Source:** `dags/daily_accounting_repayment_bukas.py`
- **Tags:** snapshot, datamart, daily, Athena

### `daily_accounting_repayment_clean`
- **Purpose:** Accounting repayment fact/snapshot pipeline (`daily_accounting_repayment_clean`).
- **Schedule:** None (manual / no schedule)
- **Paused:** yes
- **Source:** `dags/daily_accounting_repayment_clean.py`
- **Tags:** metabase-layer

### `exchange_currency`
- **Purpose:** Pipeline `exchange_currency`. Tags: raw-layer.
- **Schedule:** `0 */6 * * *`
- **Paused:** yes
- **Source:** `dags/currency_exchange.py` (deployed path; may be missing/renamed in local checkout)
- **Tags:** raw-layer

### `monthly_risk_share_reflect_loan_tape_ph`
- **Purpose:** PH risk-share / reflect loan-tape pipeline (`monthly_risk_share_reflect_loan_tape_ph`).
- **Schedule:** `0 7 1 * *`
- **Paused:** yes
- **Source:** `dags/monthly_risk_share_reflect_loan_tape_ph_.py`
- **Tags:** integration-layer

### `weekly_risk_share_reflect_loan_tape_ph`
- **Purpose:** PH risk-share / reflect loan-tape pipeline (`weekly_risk_share_reflect_loan_tape_ph`).
- **Schedule:** `0 7 * * MON`
- **Paused:** yes
- **Source:** `dags/weekly_risk_share_reflect_loan_tape_ph.py`
- **Tags:** integration-layer

## BigQuery ↔ Parquet ↔ Iceberg

### `arrow_bq_to_parquet`
- **Purpose:** Exports BigQuery tables to Parquet for lakehouse (`arrow_bq_to_parquet`).
- **Schedule:** None (manual / no schedule)
- **Paused:** yes
- **Source:** `dags/bq_to_parquet_arrow.py`
- **Tags:** Parquet, Backfill, Raw, BigQuery

### `bq_to_iceberg_parquet`
- **Purpose:** Loads Parquet into Athena Iceberg (`bq_to_iceberg_parquet`).
- **Schedule:** None (manual / no schedule)
- **Paused:** yes
- **Source:** `dags/bq_to_parquet_v2.py` (deployed path; may be missing/renamed in local checkout)
- **Tags:** iceberg, bigquery, parquet

### `bq_to_parquet_datamart_v1`
- **Purpose:** Exports BigQuery tables to Parquet for lakehouse (`bq_to_parquet_datamart_v1`).
- **Schedule:** None (manual / no schedule)
- **Paused:** yes
- **Source:** `dags/bq_to_parquet_datamart.py`
- **Tags:** Backfill, BigQuery, Raw, Parquet

### `bq_to_parquet_datamart_v2`
- **Purpose:** Exports BigQuery tables to Parquet for lakehouse (`bq_to_parquet_datamart_v2`).
- **Schedule:** None (manual / no schedule)
- **Paused:** yes
- **Source:** `dags/bq_to_parquet_datamart_v2.py`
- **Tags:** BigQuery, Raw, Backfill, Parquet

### `bq_to_parquet_v1`
- **Purpose:** Exports BigQuery tables to Parquet for lakehouse (`bq_to_parquet_v1`).
- **Schedule:** None (manual / no schedule)
- **Paused:** yes
- **Source:** `dags/bq_to_parquet_v1.py`
- **Tags:** BigQuery, Raw, Parquet, Backfill

### `bukas_bq_to_parquet_v1`
- **Purpose:** Exports BigQuery tables to Parquet for lakehouse (`bukas_bq_to_parquet_v1`).
- **Schedule:** None (manual / no schedule)
- **Paused:** yes
- **Source:** `dags/bukas_bq_to_parquet_v1.py`
- **Tags:** BigQuery, Raw, Parquet, Backfill

### `bukas_parquet_to_iceberg`
- **Purpose:** Loads Bukas Parquet into Athena Iceberg tables.
- **Schedule:** None (manual / no schedule)
- **Paused:** no
- **Source:** `dags/bukas_parquet_to_iceberg.py`
- **Tags:** parquet, iceberg, Athena

### `parquet_to_iceberg`
- **Purpose:** Manual Parquet→Athena Iceberg load for core tables.
- **Schedule:** None (manual / no schedule)
- **Paused:** no
- **Source:** `dags/parquet_to_iceberg.py`
- **Tags:** parquet, iceberg, Athena

### `parquet_to_iceberg_datamart`
- **Purpose:** Loads Parquet into Athena Iceberg (`parquet_to_iceberg_datamart`).
- **Schedule:** None (manual / no schedule)
- **Paused:** no
- **Source:** `dags/parquet_to_iceberg_datamart.py`
- **Tags:** iceberg, parquet, Athena

### `parquet_to_iceberg_datamart_v2`
- **Purpose:** Loads Parquet into Athena Iceberg (`parquet_to_iceberg_datamart_v2`).
- **Schedule:** None (manual / no schedule)
- **Paused:** no
- **Source:** `dags/parquet_to_iceberg_datamart_v2.py`
- **Tags:** parquet, iceberg, Athena

### `parquet_to_iceberg_datamart_v3`
- **Purpose:** Loads Parquet into Athena Iceberg (`parquet_to_iceberg_datamart_v3`).
- **Schedule:** None (manual / no schedule)
- **Paused:** no
- **Source:** `dags/parquet_to_iceberg_datamart_v3.py`
- **Tags:** Athena, iceberg, parquet

### `parquet_to_iceberg_v2`
- **Purpose:** Loads Parquet into Athena Iceberg (`parquet_to_iceberg_v2`).
- **Schedule:** None (manual / no schedule)
- **Paused:** no
- **Source:** `dags/parquet_to_iceberg_v2.py`
- **Tags:** Athena, parquet, iceberg

## Gsheet raw → Athena integrated

### `activations_ftl_targets_ph`
- **Purpose:** Daily Google Sheet ingest for `activations_ftl_targets_ph` into Athena Iceberg `integrated` (Bash → codes ETL).
- **Schedule:** `0 6 * * *`
- **Paused:** no
- **Source:** `dags/gsheet_raw/activations_targets_ph.py`
- **Tags:** Gsheet, Daily, Integrated, Athena

### `activations_mip_targets_ph`
- **Purpose:** Daily Google Sheet ingest for `activations_mip_targets_ph` into Athena Iceberg `integrated` (Bash → codes ETL).
- **Schedule:** `0 6 * * *`
- **Paused:** no
- **Source:** `dags/gsheet_raw/activations_targets_ph.py`
- **Tags:** Gsheet, Daily, Integrated, Athena

### `bsi_recontest_batch_1`
- **Purpose:** Daily Google Sheet ingest for `bsi_recontest_batch_1` into Athena Iceberg `integrated` (Bash → codes ETL).
- **Schedule:** `0 6 * * *`
- **Paused:** no
- **Source:** `dags/gsheet_raw/bsi_recontest_batch.py`
- **Tags:** Athena, Daily, Gsheet, Integrated

### `bsi_recontest_batch_2`
- **Purpose:** Daily Google Sheet ingest for `bsi_recontest_batch_2` into Athena Iceberg `integrated` (Bash → codes ETL).
- **Schedule:** `0 6 * * *`
- **Paused:** no
- **Source:** `dags/gsheet_raw/bsi_recontest_batch.py`
- **Tags:** Athena, Daily, Gsheet, Integrated

### `deduct_disbursement`
- **Purpose:** Daily Google Sheet ingest for `deduct_disbursement` into Athena Iceberg `integrated` (Bash → codes ETL).
- **Schedule:** `0 6 * * *`
- **Paused:** no
- **Source:** `dags/gsheet_raw/deduct_disbursement.py`
- **Tags:** Athena, Daily, Gsheet, Integrated

### `disbursements_ftl_targets_ph`
- **Purpose:** Daily Google Sheet ingest for `disbursements_ftl_targets_ph` into Athena Iceberg `integrated` (Bash → codes ETL).
- **Schedule:** `0 6 * * *`
- **Paused:** no
- **Source:** `dags/gsheet_raw/disbursements_targets_ph.py`
- **Tags:** Gsheet, Daily, Integrated, Athena

### `disbursements_mip_targets_ph`
- **Purpose:** Daily Google Sheet ingest for `disbursements_mip_targets_ph` into Athena Iceberg `integrated` (Bash → codes ETL).
- **Schedule:** `0 6 * * *`
- **Paused:** no
- **Source:** `dags/gsheet_raw/disbursements_targets_ph.py`
- **Tags:** Gsheet, Daily, Integrated, Athena

### `erudifi_targets_monthly`
- **Purpose:** Daily Google Sheet ingest for `erudifi_targets_monthly` into Athena Iceberg `integrated` (Bash → codes ETL).
- **Schedule:** `0 6 * * *`
- **Paused:** no
- **Source:** `dags/gsheet_raw/erudifi_targets_monthly.py`
- **Tags:** Gsheet, Daily, Integrated, Athena

### `etl_test_loans`
- **Purpose:** Daily Google Sheet ingest for `etl_test_loans` into Athena Iceberg `integrated` (Bash → codes ETL).
- **Schedule:** `0 6 * * *`
- **Paused:** no
- **Source:** `dags/gsheet_raw/test_loans.py`
- **Tags:** Daily, Integrated, Gsheet, Athena

### `ewoff_list`
- **Purpose:** Daily Google Sheet ingest for `ewoff_list` into Athena Iceberg `integrated` (Bash → codes ETL).
- **Schedule:** `0 6 * * *`
- **Paused:** no
- **Source:** `dags/gsheet_raw/ewoff_list.py`
- **Tags:** Gsheet, Daily, Integrated, Athena

### `finops_lender_mapping`
- **Purpose:** Daily Google Sheet ingest for `finops_lender_mapping` into Athena Iceberg `integrated` (Bash → codes ETL).
- **Schedule:** `0 6 * * *`
- **Paused:** no
- **Source:** `dags/gsheet_raw/finops_lender_mapping.py`
- **Tags:** Daily, Gsheet, Integrated, Athena

### `fx_rate`
- **Purpose:** Daily Google Sheet ingest for `fx_rate` into Athena Iceberg `integrated` (Bash → codes ETL).
- **Schedule:** `0 6 * * *`
- **Paused:** no
- **Source:** `dags/gsheet_raw/fx_rate.py`
- **Tags:** Gsheet, Daily, Integrated, Athena

### `general_courses_formal_id`
- **Purpose:** Daily Google Sheet ingest for `general_courses_formal_id` into Athena Iceberg `integrated` (Bash → codes ETL).
- **Schedule:** `0 6 * * *`
- **Paused:** no
- **Source:** `dags/gsheet_raw/general_courses_formal.py`
- **Tags:** Daily, Integrated, Gsheet, Athena

### `general_courses_formal_ph`
- **Purpose:** Daily Google Sheet ingest for `general_courses_formal_ph` into Athena Iceberg `integrated` (Bash → codes ETL).
- **Schedule:** `0 6 * * *`
- **Paused:** no
- **Source:** `dags/gsheet_raw/general_courses_formal.py`
- **Tags:** Daily, Integrated, Gsheet, Athena

### `growth_analysis`
- **Purpose:** Daily Google Sheet ingest for `growth_analysis` into Athena Iceberg `integrated` (Bash → codes ETL).
- **Schedule:** `0 6 * * *`
- **Paused:** no
- **Source:** `dags/gsheet_raw/growth_analysis.py`
- **Tags:** Gsheet, Daily, Integrated, Athena

### `institution_targets_disb_id`
- **Purpose:** Daily Google Sheet ingest for `institution_targets_disb_id` into Athena Iceberg `integrated` (Bash → codes ETL).
- **Schedule:** `0 6 * * *`
- **Paused:** no
- **Source:** `dags/gsheet_raw/institution_targets_disb_id.py`
- **Tags:** Gsheet, Daily, Integrated, Athena

### `loan_products_id`
- **Purpose:** Daily Google Sheet ingest for `loan_products_id` into Athena Iceberg `integrated` (Bash → codes ETL).
- **Schedule:** `0 6 * * *`
- **Paused:** no
- **Source:** `dags/gsheet_raw/loan_products.py`
- **Tags:** Daily, Integrated, Gsheet, Athena

### `loan_products_ph`
- **Purpose:** Daily Google Sheet ingest for `loan_products_ph` into Athena Iceberg `integrated` (Bash → codes ETL).
- **Schedule:** `0 6 * * *`
- **Paused:** no
- **Source:** `dags/gsheet_raw/loan_products.py`
- **Tags:** Daily, Integrated, Gsheet, Athena

### `loanbook_id`
- **Purpose:** Daily Google Sheet ingest for `loanbook_id` into Athena Iceberg `integrated` (Bash → codes ETL).
- **Schedule:** `0 6 * * *`
- **Paused:** no
- **Source:** `dags/gsheet_raw/loanbook.py`
- **Tags:** Gsheet, Daily, Integrated, Athena

### `loanbook_ph`
- **Purpose:** Daily Google Sheet ingest for `loanbook_ph` into Athena Iceberg `integrated` (Bash → codes ETL).
- **Schedule:** `0 6 * * *`
- **Paused:** no
- **Source:** `dags/gsheet_raw/loanbook.py`
- **Tags:** Gsheet, Daily, Integrated, Athena

### `manual_adjustments`
- **Purpose:** Daily Google Sheet ingest for `manual_adjustments` into Athena Iceberg `integrated` (Bash → codes ETL).
- **Schedule:** `0 6 * * *`
- **Paused:** no
- **Source:** `dags/gsheet_raw/manual_adjustments.py`
- **Tags:** Integrated, Daily, Athena, Gsheet

### `new_target_2024`
- **Purpose:** Daily Google Sheet ingest for `new_target_2024` into Athena Iceberg `integrated` (Bash → codes ETL).
- **Schedule:** `0 6 * * *`
- **Paused:** no
- **Source:** `dags/gsheet_raw/new_target_2024.py`
- **Tags:** Integrated, Daily, Athena, Gsheet

### `ojk_account_eca`
- **Purpose:** Daily Google Sheet ingest for `ojk_account_eca` into Athena Iceberg `integrated` (Bash → codes ETL).
- **Schedule:** `0 6 * * *`
- **Paused:** no
- **Source:** `dags/gsheet_raw/ojk_references.py`
- **Tags:** Gsheet, Daily, Integrated, Athena

### `ojk_gender_mapping`
- **Purpose:** Daily Google Sheet ingest for `ojk_gender_mapping` into Athena Iceberg `integrated` (Bash → codes ETL).
- **Schedule:** `0 6 * * *`
- **Paused:** no
- **Source:** `dags/gsheet_raw/ojk_references.py`
- **Tags:** Gsheet, Daily, Integrated, Athena

### `ojk_province_mapping`
- **Purpose:** Daily Google Sheet ingest for `ojk_province_mapping` into Athena Iceberg `integrated` (Bash → codes ETL).
- **Schedule:** `0 6 * * *`
- **Paused:** no
- **Source:** `dags/gsheet_raw/ojk_references.py`
- **Tags:** Gsheet, Daily, Integrated, Athena

### `partner_base_id`
- **Purpose:** Daily Google Sheet ingest for `partner_base_id` into Athena Iceberg `integrated` (Bash → codes ETL).
- **Schedule:** `0 6 * * *`
- **Paused:** no
- **Source:** `dags/gsheet_raw/partner_base.py`
- **Tags:** Gsheet, Daily, Integrated, Athena

### `partner_base_ph`
- **Purpose:** Daily Google Sheet ingest for `partner_base_ph` into Athena Iceberg `integrated` (Bash → codes ETL).
- **Schedule:** `0 6 * * *`
- **Paused:** no
- **Source:** `dags/gsheet_raw/partner_base.py`
- **Tags:** Gsheet, Daily, Integrated, Athena

### `partner_enrolment_ph`
- **Purpose:** Daily Google Sheet ingest for `partner_enrolment_ph` into Athena Iceberg `integrated` (Bash → codes ETL).
- **Schedule:** `0 6 * * *`
- **Paused:** no
- **Source:** `dags/gsheet_raw/partner_enrolment_ph.py`
- **Tags:** Gsheet, Daily, Integrated, Athena

### `partners_calender_2023_ph`
- **Purpose:** Daily Google Sheet ingest for `partners_calender_2023_ph` into Athena Iceberg `integrated` (Bash → codes ETL).
- **Schedule:** `0 6 * * *`
- **Paused:** no
- **Source:** `dags/gsheet_raw/partners_calender_ph.py`
- **Tags:** Gsheet, Daily, Integrated, Athena

### `registration_targets_2023_ph`
- **Purpose:** Daily Google Sheet ingest for `registration_targets_2023_ph` into Athena Iceberg `integrated` (Bash → codes ETL).
- **Schedule:** `0 6 * * *`
- **Paused:** no
- **Source:** `dags/gsheet_raw/registration_targets_ph.py`
- **Tags:** Gsheet, Daily, Integrated, Athena

### `report_date_adjustment`
- **Purpose:** Daily Google Sheet ingest for `report_date_adjustment` into Athena Iceberg `integrated` (Bash → codes ETL).
- **Schedule:** `0 6 * * *`
- **Paused:** no
- **Source:** `dags/gsheet_raw/report_date_adjustment.py`
- **Tags:** Integrated, Daily, Athena, Gsheet

### `submit_ftl_targets_ph`
- **Purpose:** Daily Google Sheet ingest for `submit_ftl_targets_ph` into Athena Iceberg `integrated` (Bash → codes ETL).
- **Schedule:** `0 6 * * *`
- **Paused:** no
- **Source:** `dags/gsheet_raw/submit_ftl.py`
- **Tags:** Gsheet, Daily, Integrated, Athena

### `submit_mip_targets_ph`
- **Purpose:** Daily Google Sheet ingest for `submit_mip_targets_ph` into Athena Iceberg `integrated` (Bash → codes ETL).
- **Schedule:** `0 6 * * *`
- **Paused:** no
- **Source:** `dags/gsheet_raw/submit_ftl.py`
- **Tags:** Gsheet, Daily, Integrated, Athena

### `tkb_landing_page`
- **Purpose:** Daily Google Sheet ingest for `tkb_landing_page` into Athena Iceberg `integrated` (Bash → codes ETL).
- **Schedule:** `0 6 * * *`
- **Paused:** no
- **Source:** `dags/gsheet_raw/tkb_landing_page.py`
- **Tags:** Gsheet, Daily, Integrated, Athena

## OJK / Pusdafil / SLIK (BQ & reports)

### `daily_pusdafil_report_am`
- **Purpose:** Pusdafil regulatory report pipeline (`daily_pusdafil_report_am`).
- **Schedule:** `0 9 * * *`
- **Paused:** yes
- **Source:** `dags/archived/daily_pusdafil_am.py`
- **Tags:** pusdafil

### `daily_pusdafil_report_debug`
- **Purpose:** Pusdafil regulatory report pipeline (`daily_pusdafil_report_debug`).
- **Schedule:** `0 9 * * *`
- **Paused:** yes
- **Source:** `dags/daily_pusdafil_debug.py`
- **Tags:** pusdafil

### `daily_pusdafil_report_pm`
- **Purpose:** Pusdafil regulatory report pipeline (`daily_pusdafil_report_pm`).
- **Schedule:** `30 21 * * *`
- **Paused:** yes
- **Source:** `dags/archived/daily_pusdafil_pm.py`
- **Tags:** pusdafil

### `daily_slik_closed_loans`
- **Purpose:** Daily SLIK closed-loans extract into Athena `reports` with Slack notify.
- **Schedule:** `0 9 * * *`
- **Paused:** no
- **Source:** `dags/daily_slik_closed_loans.py`
- **Tags:** daily, athena, slik, closed-loans, reports

### `daily_slik_loans_closed`
- **Purpose:** SLIK reporting pipeline (`daily_slik_loans_closed`) into Athena reports.
- **Schedule:** `0 9 * * *`
- **Paused:** yes
- **Source:** `dags/daily_slik_loans_closed.py` (deployed path; may be missing/renamed in local checkout)
- **Tags:** slik, daily, athena, closed-loans, reports

### `monthly_slik_active_loans`
- **Purpose:** Monthly SLIK active-loans report into Athena `reports` with Slack notify.
- **Schedule:** `0 9 1 * *`
- **Paused:** no
- **Source:** `dags/monthly_slik_active_loans.py`
- **Tags:** athena, slik, reports, active-loans, monthly

### `ojk_master_daily_v2`
- **Purpose:** OJK master/report pipeline (`ojk_master_daily_v2`).
- **Schedule:** `45 7 * * *`
- **Paused:** yes
- **Source:** `dags/ojk_master_daily_v2.py`
- **Tags:** Metabase, OJK, integration-layer

### `ojk_master_daily_v2_clean`
- **Purpose:** OJK master/report pipeline (`ojk_master_daily_v2_clean`).
- **Schedule:** None (manual / no schedule)
- **Paused:** yes
- **Source:** `dags/ojk_master_daily_v2_clean.py`
- **Tags:** Metabase, OJK

### `ojk_master_monthly`
- **Purpose:** OJK master/report pipeline (`ojk_master_monthly`).
- **Schedule:** `0 2 2 * *`
- **Paused:** yes
- **Source:** `dags/ojk_master_monthly.py` (deployed path; may be missing/renamed in local checkout)
- **Tags:** integration-layer

### `ojk_master_monthly_v2`
- **Purpose:** OJK master/report pipeline (`ojk_master_monthly_v2`).
- **Schedule:** `0 2 2 * *`
- **Paused:** yes
- **Source:** `dags/ojk_master_monthly_v2.py` (deployed path; may be missing/renamed in local checkout)
- **Tags:** integration-layer

## Bukas & Danacita raw ingest

### `daily_raw_bukas`
- **Purpose:** Daily raw Bukas ingest orchestration (lakehouse/GCS path).
- **Schedule:** `30 5,22 * * *`
- **Paused:** no
- **Source:** `dags/daily_raw_bukas.py`
- **Tags:** Raw Data, Athena, bukas, Daily

### `daily_raw_dc`
- **Purpose:** Daily raw Danacita ingest orchestration (lakehouse/GCS path).
- **Schedule:** `0 5,12,23 * * *`
- **Paused:** no
- **Source:** `dags/daily_raw_dc.py`
- **Tags:** Raw Data, Athena, danacita, Daily

### `raw_bukas_daily`
- **Purpose:** Raw data ingest pipeline (`raw_bukas_daily`).
- **Schedule:** `30 5,22 * * *`
- **Paused:** yes
- **Source:** `dags/raw_bukas_daily.py`
- **Tags:** Raw Data, bukas, Daily, BQ

### `raw_data_danacita_1`
- **Purpose:** Raw data ingest pipeline (`raw_data_danacita_1`).
- **Schedule:** `30 2,22 * * *`
- **Paused:** yes
- **Source:** `dags/raw_data_danacita_stage_1.py` (deployed path; may be missing/renamed in local checkout)
- **Tags:** Raw Data, Daily, danacita

### `raw_data_danacita_chunked`
- **Purpose:** Raw data ingest pipeline (`raw_data_danacita_chunked`).
- **Schedule:** `30 5,20 * * *`
- **Paused:** yes
- **Source:** `dags/raw_data_danacita_chunked.py`
- **Tags:** Raw Data, Daily

### `raw_dc_daily`
- **Purpose:** Raw data ingest pipeline (`raw_dc_daily`).
- **Schedule:** `0 5,12,23 * * *`
- **Paused:** yes
- **Source:** `dags/raw_data_danacita_refactored.py`
- **Tags:** Raw Data, Daily, danacita, BQ

### `raw_dc_daily_2`
- **Purpose:** Raw data ingest pipeline (`raw_dc_daily_2`).
- **Schedule:** `0 5,12,23 * * *`
- **Paused:** yes
- **Source:** `dags/raw_data_danacita_stage_2.py`
- **Tags:** Raw Data, Daily, danacita, BQ

## Partner feeds

### `helicap_data_daily`
- **Purpose:** Pipeline `helicap_data_daily`. Tags: helicap-data.
- **Schedule:** `15 6,22 * * *`
- **Paused:** yes
- **Source:** `dags/helicap_data_daily.py` (deployed path; may be missing/renamed in local checkout)
- **Tags:** helicap-data

### `lendeast_data_daily`
- **Purpose:** Pipeline `lendeast_data_daily`. Tags: lendeast-data.
- **Schedule:** None (manual / no schedule)
- **Paused:** yes
- **Source:** `dags/lendeast_data_daily.py` (deployed path; may be missing/renamed in local checkout)
- **Tags:** lendeast-data

## Core ETL / governance / monitoring

### `airflow_monitoring`
- **Purpose:** Composer/Airflow liveness prober for environment health.
- **Schedule:** None (manual / no schedule)
- **Paused:** yes
- **Source:** `dags/airflow_monitoring.py`
- **Tags:** _(none)_

### `data_quality`
- **Purpose:** Pipeline `data_quality`. Tags: data-quality.
- **Schedule:** None (manual / no schedule)
- **Paused:** yes
- **Source:** `dags/data_quality.py`
- **Tags:** data-quality

### `erudifi_core_etl`
- **Purpose:** Pipeline `erudifi_core_etl`. Tags: raw-layer.
- **Schedule:** `0 2,4,8,11,15,19,22 * * *`
- **Paused:** yes
- **Source:** `dags/erudifi_etl.py` (deployed path; may be missing/renamed in local checkout)
- **Tags:** raw-layer

### `erudifi_data_governance`
- **Purpose:** Hourly data-governance SQL checks in BigQuery (`query/gov/*`) with Slack notify.
- **Schedule:** `@hourly`
- **Paused:** yes
- **Source:** `dags/data_gov.py`
- **Tags:** raw-layer

### `erudifi_prod_core_etl`
- **Purpose:** Pipeline `erudifi_prod_core_etl`. Tags: raw-layer.
- **Schedule:** `30 6,9,12,22 * * *`
- **Paused:** yes
- **Source:** `dags/erudifi_prod_etl.py` (deployed path; may be missing/renamed in local checkout)
- **Tags:** raw-layer

