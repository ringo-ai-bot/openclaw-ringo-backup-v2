# core-loans Metabase table reference

_Auto-generated from `DanaCita v2` (database_id=13) on 2026-07-17 05:09 UTC._

Applies to both **DanaCita v2** (id 13) and **Bukas v2** (id 12) —
same Django schema from `/data/code/core-loans`.

Regenerate with:

```bash
python3 scripts/generate_schema_reference.py
```

**Tables:** 325

## App summary

| App prefix | Tables |
|---|---:|
| `loans` | 68 |
| `partners` | 41 |
| `users` | 28 |
| `accounting` | 12 |
| `notifications` | 11 |
| `reports` | 11 |
| `lenders` | 10 |
| `payables` | 10 |
| `e` | 9 |
| `contracts` | 8 |
| `django` | 8 |
| `forms` | 8 |
| `banners` | 7 |
| `credit` | 7 |
| `integrations` | 6 |
| `regions` | 6 |
| `escrow` | 5 |
| `payments` | 5 |
| `rewards` | 5 |
| `survey` | 5 |
| `collection` | 4 |
| `leads` | 4 |
| `logs` | 4 |
| `socialaccount` | 4 |
| `customer` | 3 |
| `inquiries` | 3 |
| `insights` | 3 |
| `pefindos` | 3 |
| `account` | 2 |
| `digital` | 2 |
| `dynamic` | 2 |
| `offer` | 2 |
| `referrals` | 2 |
| `shortlinks` | 2 |
| `stamps` | 2 |
| `taggit` | 2 |
| `token` | 2 |
| `authtoken` | 1 |
| `event` | 1 |
| `midtrans` | 1 |
| `offline` | 1 |
| `ops` | 1 |
| `rest` | 1 |
| `scores` | 1 |
| `simple` | 1 |
| `underwriting` | 1 |

## Tables

### `account_*`

#### `public.account_emailaddress`

_Fields: 5_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `email` | Text |  |
| `verified` | Boolean |  |
| `primary` | Boolean |  |
| `user_id` | Integer |  |

#### `public.account_emailconfirmation`

_Fields: 5_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `created` | DateTimeWithLocalTZ |  |
| `sent` | DateTimeWithLocalTZ |  |
| `key` | Text |  |
| `email_address_id` | Integer |  |


### `accounting_*`

#### `public.accounting_collection`

_Fields: 24_

| Field | Type | Description |
|---|---|---|
| `transaction_ptr_id` | Integer |  |
| `channel` | Text |  |
| `correlator_code` | Text |  |
| `reference_code` | Text |  |
| `paid_penalty` | Decimal |  |
| `paid_interest` | Decimal |  |
| `paid_principal` | Decimal |  |
| `status` | Text |  |
| `date_posted` | Date |  |
| `datetime_processed` | DateTimeWithLocalTZ |  |
| `payment_receipt_file` | Text |  |
| `batch_id` | Integer |  |
| `loan_id` | Integer |  |
| `paid_excess` | Decimal |  |
| `paid_platform_fee` | Decimal |  |
| `paid_lender_return` | Decimal |  |
| `sub_channel` | Text |  |
| `kind` | Text |  |
| `paid_insurance_fee` | Decimal |  |
| `actual_cancellation_fee` | Decimal |  |
| `actual_disbursed_refund_amount` | Decimal |  |
| `payment_id` | BigInteger |  |
| `receivable_document_id` | Integer |  |
| `paid_processing_fee` | Decimal |  |

#### `public.accounting_collectionbatch`

_Fields: 11_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `uuid` | UUID |  |
| `collection_file` | Text |  |
| `status` | Text |  |
| `type` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `datetime_deleted` | DateTimeWithLocalTZ |  |
| `datetime_processed` | DateTimeWithLocalTZ |  |
| `datetime_ingested` | DateTimeWithLocalTZ |  |
| `error_file` | Text |  |

#### `public.accounting_credit`

_Fields: 11_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `uuid` | UUID |  |
| `amount` | Decimal |  |
| `reference_code_allocation` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_allocated` | DateTimeWithLocalTZ |  |
| `status` | Text |  |
| `borrower_id` | Integer |  |
| `datetime_refunded` | DateTimeWithLocalTZ |  |
| `loan_source_id` | Integer |  |
| `collection_source_id` | Integer |  |

#### `public.accounting_dragonpaycollection`

_Fields: 5_

| Field | Type | Description |
|---|---|---|
| `collection_ptr_id` | Integer |  |
| `provider_status` | Text |  |
| `message` | Text |  |
| `fee` | Decimal |  |
| `payment_mode` | Text |  |

#### `public.accounting_midtranscollection`

_Fields: 8_

| Field | Type | Description |
|---|---|---|
| `collection_ptr_id` | Integer |  |
| `transaction_status` | Text |  |
| `fraud_status` | Text |  |
| `fee` | Decimal |  |
| `payment_channel` | Text |  |
| `message` | Text |  |
| `snap_token` | Text |  |
| `finish_redirect_url` | Text |  |

#### `public.accounting_reasoncode`

_Fields: 4_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `code` | Text |  |
| `name` | Text |  |
| `description` | Text |  |

#### `public.accounting_rebate`

_Fields: 10_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `amount` | Decimal |  |
| `type` | Text |  |
| `status` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_expiry` | DateTimeWithLocalTZ |  |
| `collection_id` | Integer |  |
| `user_id` | Integer |  |
| `content_type_id` | Integer |  |
| `object_id` | Integer |  |

#### `public.accounting_receivabledocument`

_Fields: 6_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `transaction_type` | Text |  |
| `description` | Text |  |
| `date_posted` | Date |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `reason_code_id` | Integer |  |

#### `public.accounting_receivabletransaction`

_Fields: 13_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `date_due` | Date |  |
| `charge_type` | Text |  |
| `amount` | Decimal |  |
| `is_reversed` | Boolean |  |
| `date_cleared` | Date |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `borrower_id` | Integer |  |
| `clearing_document_id` | Integer |  |
| `loan_id` | Integer |  |
| `receivable_document_id` | Integer |  |
| `reference_document_id` | Integer |  |
| `repayment_id` | Integer |  |

#### `public.accounting_repayment`

_Fields: 58_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `period` | Integer |  |
| `reference_code` | Text |  |
| `scheduled_penalty` | Decimal |  |
| `scheduled_principal` | Decimal |  |
| `scheduled_interest` | Decimal |  |
| `scheduled_principal_balance` | Decimal |  |
| `scheduled_remaining_principal` | Decimal |  |
| `paid_penalty` | Decimal |  |
| `paid_interest` | Decimal |  |
| `paid_principal` | Decimal |  |
| `waived_penalty_rate` | Decimal |  |
| `waived_penalty` | Decimal |  |
| `past_due_total` | Decimal |  |
| `scheduled_total` | Decimal |  |
| `penalty_total` | Decimal |  |
| `paid_total` | Decimal |  |
| `due_total` | Decimal |  |
| `days_in_arrears` | Integer |  |
| `date_due` | Date |  |
| `date_paid` | Date |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `datetime_deleted` | DateTimeWithLocalTZ |  |
| `status` | Text |  |
| `borrower_id` | Integer |  |
| `loan_id` | Integer |  |
| `previous_repayment_id` | Integer |  |
| `paid_excess` | Decimal |  |
| `scheduled_excess` | Decimal |  |
| `actual_principal_balance` | Decimal |  |
| `interest_income_current_month` | Decimal |  |
| `interest_income_previous_month` | Decimal |  |
| `date_waived` | Date |  |
| `discount_scheduled_balance` | Decimal |  |
| `discount_scheduled_income` | Decimal |  |
| `scheduled_platform_fee` | Decimal |  |
| `scheduled_lender_return` | Decimal |  |
| `discount_paid_principal` | Decimal |  |
| `discount_scheduled_principal` | Decimal |  |
| `outstanding_net_principal` | Decimal |  |
| `outstanding_revenue` | Decimal |  |
| `paid_revenue` | Decimal |  |
| `datetime_late_payment_waived` | Date |  |
| `paid_insurance_fee` | Decimal |  |
| `scheduled_insurance_fee` | Decimal |  |
| `lender_return_rate` | Decimal |  |
| `is_paid_after_cut_off` | Boolean |  |
| `risk_share_payment` | Decimal |  |
| `risk_share_status` | Text |  |
| `paid_total_with_risk_share` | Decimal |  |
| `scheduled_lender_interest` | Decimal |  |
| `scheduled_lender_principal` | Decimal |  |
| `is_buyback` | Boolean |  |
| `lender_return_status` | Text |  |
| `split_revenue_id` | Integer |  |
| `paid_processing_fee` | Decimal |  |
| `scheduled_processing_fee` | Decimal |  |

#### `public.accounting_repaymentrecovery`

_Fields: 9_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `period` | Integer |  |
| `scheduled_total` | Decimal |  |
| `paid_total` | Decimal |  |
| `due_total` | Decimal |  |
| `status` | Text |  |
| `date_due` | Date |  |
| `date_paid` | Date |  |
| `loan_id` | Integer |  |

#### `public.accounting_transaction`

_Fields: 7_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `uuid` | UUID |  |
| `amount` | Decimal |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `datetime_deleted` | DateTimeWithLocalTZ |  |
| `polymorphic_ctype_id` | Integer |  |


### `authtoken_*`

#### `public.authtoken_token`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `key` | Text |  |
| `created` | DateTimeWithLocalTZ |  |
| `user_id` | Integer |  |


### `banners_*`

#### `public.banners_imagebanner`

_Fields: 19_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `target_loan_status` | Text |  |
| `target_profile_status` | Text |  |
| `is_active` | Boolean |  |
| `date_start` | Date |  |
| `date_end` | Date |  |
| `name` | Text |  |
| `title` | Text |  |
| `redirect_to` | Text |  |
| `cta_label` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `image_file` | Text |  |
| `content` | Text |  |
| `hide_from_rejected_users` | Boolean |  |
| `target_loan_app_status` | Text |  |
| `datetime_end` | DateTimeWithLocalTZ |  |
| `datetime_start` | DateTimeWithLocalTZ |  |
| `show_only_to_old_android_app_users` | Boolean |  |

#### `public.banners_imagebanner_target_partners`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `imagebanner_id` | Integer |  |
| `partner_id` | Integer |  |

#### `public.banners_multibanner`

_Fields: 15_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `target_loan_status` | Text |  |
| `target_profile_status` | Text |  |
| `is_active` | Boolean |  |
| `date_start` | Date |  |
| `date_end` | Date |  |
| `name` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `show_in` | Text |  |
| `hide_from_rejected_users` | Boolean |  |
| `target_loan_app_status` | Text |  |
| `datetime_end` | DateTimeWithLocalTZ |  |
| `datetime_start` | DateTimeWithLocalTZ |  |
| `show_only_to_old_android_app_users` | Boolean |  |

#### `public.banners_multibanner_target_partners`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `multibanner_id` | Integer |  |
| `partner_id` | Integer |  |

#### `public.banners_multibanneritem`

_Fields: 6_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `name` | Text |  |
| `redirect_to` | Text |  |
| `content` | Text |  |
| `image_file` | Text |  |
| `multi_banner_id` | Integer |  |

#### `public.banners_textbanner`

_Fields: 19_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `target_loan_status` | Text |  |
| `target_profile_status` | Text |  |
| `is_active` | Boolean |  |
| `date_start` | Date |  |
| `date_end` | Date |  |
| `name` | Text |  |
| `title` | Text |  |
| `redirect_to` | Text |  |
| `cta_label` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `content` | Text |  |
| `hide_from_rejected_users` | Boolean |  |
| `target_loan_app_status` | Text |  |
| `show_in` | Text |  |
| `datetime_end` | DateTimeWithLocalTZ |  |
| `datetime_start` | DateTimeWithLocalTZ |  |
| `show_only_to_old_android_app_users` | Boolean |  |

#### `public.banners_textbanner_target_partners`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `textbanner_id` | Integer |  |
| `partner_id` | Integer |  |


### `collection_*`

#### `public.collection_operations_ecaagreementdocument`

_Fields: 6_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `type` | Text |  |
| `agreement_document_file` | Text |  |
| `valid_start_date` | Date |  |
| `valid_end_date` | Date |  |
| `partner_id` | Integer |  |

#### `public.collection_operations_externalcollectionagency`

_Fields: 6_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `name` | Text |  |
| `error_file` | Text |  |
| `loan_assignment_file` | Text |  |
| `uuid` | UUID |  |
| `loan_unassignment_file` | Text |  |

#### `public.collection_operations_externalcollectionagencylog`

_Fields: 5_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `assigned_at` | DateTimeWithLocalTZ |  |
| `external_collection_agency_id` | Integer |  |
| `loan_id` | Integer |  |
| `days_past_due` | Integer |  |

#### `public.collection_operations_externalcollectionagencyreport`

_Fields: 8_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `uuid` | UUID |  |
| `date_of_file` | Date |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `ECA_report_file` | Text |  |
| `external_collection_agency_id` | Integer |  |
| `end_date` | Date |  |
| `start_date` | Date |  |


### `contracts_*`

#### `public.contracts_clausedefinition`

_Fields: 11_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `code` | Text |  |
| `title` | Text |  |
| `contract_type` | Text |  |
| `description` | Text |  |
| `configuration_schema` | JSON |  |
| `default_parameters` | JSON |  |
| `is_required` | Boolean |  |
| `is_active` | Boolean |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |

#### `public.contracts_contract`

_Fields: 14_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `uuid` | UUID |  |
| `title` | Text |  |
| `contract_type` | Text |  |
| `source_system` | Text |  |
| `subject_type` | Text |  |
| `subject_id` | Text |  |
| `subject_snapshot` | JSON |  |
| `partner_id` | Integer |  |
| `product_code` | Text |  |
| `lifecycle_state` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `active_version_id` | Integer |  |

#### `public.contracts_contractartifact`

_Fields: 11_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `kind` | Text |  |
| `display_name` | Text |  |
| `storage_uri` | Text |  |
| `checksum` | Text |  |
| `metadata` | JSON |  |
| `is_signed` | Boolean |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `contract_id` | Integer |  |
| `contract_version_id` | Integer |  |

#### `public.contracts_contracttemplate`

_Fields: 22_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `key` | Text |  |
| `name` | Text |  |
| `contract_type` | Text |  |
| `partner_id` | Integer |  |
| `product_code` | Text |  |
| `description` | Text |  |
| `default_terms_payload` | JSON |  |
| `default_clause_payloads` | JSON |  |
| `is_active` | Boolean |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `body_html` | Text |  |
| `layout_settings` | JSON |  |
| `footer_html` | Text |  |
| `header_html` | Text |  |
| `active_published_version_id` | Integer |  |
| `rule_interest_rate` | Text |  |
| `rule_is_restructured` | Boolean |  |
| `rule_lender_name` | Text |  |
| `rule_lender_type` | Text |  |
| `rule_loan_type` | Text |  |

#### `public.contracts_contracttemplatesourceartifact`

_Fields: 11_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `kind` | Text |  |
| `original_filename` | Text |  |
| `storage_uri` | Text |  |
| `content_type` | Text |  |
| `checksum` | Text |  |
| `metadata` | JSON |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `template_id` | Integer |  |
| `template_version_id` | Integer |  |

#### `public.contracts_contracttemplateversion`

_Fields: 23_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `version_number` | Integer |  |
| `status` | Text |  |
| `contract_type` | Text |  |
| `rule_loan_type` | Text |  |
| `rule_lender_type` | Text |  |
| `rule_lender_name` | Text |  |
| `rule_interest_rate` | Text |  |
| `rule_is_restructured` | Boolean |  |
| `header_html` | Text |  |
| `body_html` | Text |  |
| `footer_html` | Text |  |
| `layout_settings` | JSON |  |
| `default_terms_payload` | JSON |  |
| `default_clause_payloads` | JSON |  |
| `change_summary` | Text |  |
| `comments` | Text |  |
| `published_at` | DateTimeWithLocalTZ |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `published_by_id` | Integer |  |
| `supersedes_id` | Integer |  |
| `template_id` | Integer |  |

#### `public.contracts_contracttemplateversionclause`

_Fields: 11_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `clause_key` | Text |  |
| `title` | Text |  |
| `body_html` | Text |  |
| `sort_order` | Integer |  |
| `metadata` | JSON |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `parent_id` | Integer |  |
| `template_version_id` | Integer |  |
| `clause_definition_id` | Integer |  |

#### `public.contracts_contractversion`

_Fields: 17_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `version_number` | Integer |  |
| `template_key` | Text |  |
| `status` | Text |  |
| `effective_from` | Date |  |
| `effective_to` | Date |  |
| `clause_payloads` | JSON |  |
| `terms_payload` | JSON |  |
| `deviation_payloads` | JSON |  |
| `published_at` | DateTimeWithLocalTZ |  |
| `notes` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `contract_id` | Integer |  |
| `published_by_id` | Integer |  |
| `supersedes_id` | Integer |  |
| `template_version_id` | Integer |  |


### `credit_*`

#### `public.credit_line_creditline`

_Fields: 141_

| Field | Type | Description |
|---|---|---|
| `id` | BigInteger |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `revision_funnel_duration` | Integer |  |
| `underwriting_credit_score` | Integer |  |
| `underwriting_rating` | Text |  |
| `underwriting_type` | Text |  |
| `underwriting_risk_classification` | Text |  |
| `underwriting_decision` | Text |  |
| `underwriting_version` | Text |  |
| `underwriting_error` | Text |  |
| `underwriting_verified` | Boolean |  |
| `underwriting_datetime_computed` | DateTimeWithLocalTZ |  |
| `reference_code` | Text |  |
| `credit_line_expiration_date` | Date |  |
| `academic_term_needed` | Text |  |
| `purpose` | Text |  |
| `segment` | Text |  |
| `general_notes` | Text |  |
| `address_detail_notes` | Text |  |
| `borrower_information_notes` | Text |  |
| `borrower_and_coborrower_information_notes` | Text |  |
| `borrower_general_course` | Text |  |
| `borrower_school_assessment_file` | Text |  |
| `borrower_year_level` | Integer |  |
| `borrower_degree` | Text |  |
| `borrower_program` | Text |  |
| `student_id_number` | Text |  |
| `student_email` | Text |  |
| `valid_id_file` | Text |  |
| `valid_id_number` | Text |  |
| `valid_id_file_type` | Text |  |
| `selfie_file` | Text |  |
| `additional_borrower_id_file` | Text |  |
| `borrower_gender` | Text |  |
| `borrower_place_of_birth` | Text |  |
| `borrower_date_of_birth` | Date |  |
| `marital_status` | Text |  |
| `borrower_identity` | Text |  |
| `borrower_nearest_landmark` | Text |  |
| `borrower_school_assessment_file_notes` | Text |  |
| `borrower_address_line_1` | Text |  |
| `borrower_address_line_2` | Text |  |
| `student_proof_of_residence_file` | Text |  |
| `student_proof_of_residence_file_type` | Text |  |
| `is_borrower_pep` | Boolean |  |
| `is_borrower_related_to_pep` | Boolean |  |
| `income_details_information_notes` | Text |  |
| `primary_income_provider` | Text |  |
| `borrower_source_of_income` | Text |  |
| `borrower_monthly_income` | Decimal |  |
| `borrower_verified_monthly_income` | Decimal |  |
| `borrower_position` | Text |  |
| `borrower_job_start_date` | Date |  |
| `borrower_tenure` | Integer |  |
| `borrower_business_name` | Text |  |
| `borrower_business_address` | Text |  |
| `borrower_business_phone` | Text |  |
| `borrower_proof_of_income_file` | Text |  |
| `borrower_proof_of_income_file_type` | Text |  |
| `borrower_name_of_remitter` | Text |  |
| `borrower_tin_number` | Text |  |
| `borrower_sss_number` | Text |  |
| `remitter_relationship_with_borrower` | Text |  |
| `datetime_sent_last_guarantor_consent_sms` | DateTimeWithLocalTZ |  |
| `mobile_number_sent_last_guarantor_consent_sms` | Text |  |
| `alt_flow_guardian_consent_used` | Boolean |  |
| `alt_flow_guarantor_consent_used` | Boolean |  |
| `guarantor_has_accepted_privacy_policy` | Boolean |  |
| `guarantor_has_confirmed_identity` | Boolean |  |
| `valid_id_uploaded_by_guarantor_file` | Text |  |
| `valid_id_uploaded_by_guarantor_file_type` | Text |  |
| `selfie_with_valid_id_uploaded_by_guarantor_file` | Text |  |
| `guarantor_marital_status` | Text |  |
| `guarantor_relationship_to_borrower` | Text |  |
| `remitter_relationship_with_guarantor` | Text |  |
| `guarantor_relationship_to_student` | Text |  |
| `guarantor_relationship_to_borrower_other_data` | Text |  |
| `guarantor_first_name` | Text |  |
| `guarantor_last_name` | Text |  |
| `guarantor_email` | Text |  |
| `guarantor_gender` | Text |  |
| `guarantor_mobile_number` | Text |  |
| `guarantor_place_of_birth` | Text |  |
| `guarantor_date_of_birth` | Date |  |
| `additional_guarantor_id_file` | Text |  |
| `guarantor_proof_of_residence_file` | Text |  |
| `guarantor_proof_of_residence_file_type` | Text |  |
| `guarantor_address_line_1` | Text |  |
| `guarantor_address_line_2` | Text |  |
| `guarantor_nearest_landmark` | Text |  |
| `is_guarantor_address_same_as_borrower` | Boolean |  |
| `guarantor_name_of_remitter` | Text |  |
| `guarantor_source_of_income` | Text |  |
| `guarantor_monthly_income` | Decimal |  |
| `guarantor_verified_monthly_income` | Decimal |  |
| `guarantor_position` | Text |  |
| `guarantor_business_name` | Text |  |
| `guarantor_business_address` | Text |  |
| `guarantor_business_phone` | Text |  |
| `guarantor_job_start_date` | Date |  |
| `guarantor_tenure` | Integer |  |
| `guarantor_proof_of_income_file` | Text |  |
| `guarantor_proof_of_income_file_type` | Text |  |
| `guarantor_tin_number` | Text |  |
| `guarantor_sss_number` | Text |  |
| `is_guarantor_related_to_pep` | Boolean |  |
| `is_guarantor_pep` | Boolean |  |
| `guardian_first_name` | Text |  |
| `guardian_last_name` | Text |  |
| `guardian_relationship_to_student` | Text |  |
| `additional_guardian_id_file` | Text |  |
| `guardian_mobile_number` | Text |  |
| `guardian_email` | Text |  |
| `guardian_marital_status` | Text |  |
| `valid_id_uploaded_by_guardian_file` | Text |  |
| `valid_id_uploaded_by_guardian_file_type` | Text |  |
| `selfie_with_valid_id_uploaded_by_guardian_file` | Text |  |
| `guardian_has_accepted_privacy_policy` | Boolean |  |
| `guardian_has_confirmed_identity` | Boolean |  |
| `datetime_sent_last_guardian_consent_sms` | DateTimeWithLocalTZ |  |
| `guardian_has_consented_to_be_contacted` | Boolean |  |
| `mobile_number_sent_last_guardian_consent_sms` | Text |  |
| `status` | Text |  |
| `datetime_approved` | DateTimeWithLocalTZ |  |
| `datetime_submitted` | DateTimeWithLocalTZ |  |
| `datetime_rejected` | DateTimeWithLocalTZ |  |
| `datetime_canceled` | DateTimeWithLocalTZ |  |
| `datetime_renewed` | DateTimeWithLocalTZ |  |
| `datetime_completed_guarantor_edd` | DateTimeWithLocalTZ |  |
| `datetime_completed_guardian_edd` | DateTimeWithLocalTZ |  |
| `approved_credit_line_limit` | Decimal |  |
| `remaining_credit_line_limit` | Decimal |  |
| `borrower_id` | Integer |  |
| `borrower_city_id` | Integer |  |
| `borrower_industry_id` | Integer |  |
| `borrower_province_id` | Integer |  |
| `guarantor_city_id` | Integer |  |
| `guarantor_industry_id` | Integer |  |
| `guarantor_province_id` | Integer |  |
| `processor_id` | Integer |  |

#### `public.credit_line_creditlinedatasnapshot`

_Fields: 4_

| Field | Type | Description |
|---|---|---|
| `id` | BigInteger |  |
| `credit_line_data` | JSON |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `credit_line_id` | BigInteger |  |

#### `public.credit_report_creditreport`

_Fields: 40_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `CB_score` | Text |  |
| `CB_score_grade` | Text |  |
| `CB_score_description` | Text |  |
| `full_name` | Text |  |
| `name_as_id` | Text |  |
| `mothers_name` | Text |  |
| `place_of_birth` | Text |  |
| `date_of_birth` | Date |  |
| `gender` | Text |  |
| `marital_status` | Text |  |
| `educational_status` | Text |  |
| `resident` | Text |  |
| `subject_last_update_date` | Date |  |
| `address` | Text |  |
| `sub_district` | Text |  |
| `district` | Text |  |
| `city` | Text |  |
| `postal_code` | Text |  |
| `address_last_update_date` | Date |  |
| `identity_type` | Text |  |
| `identity_number` | Text |  |
| `phone_number` | Text |  |
| `cellphone_number` | Text |  |
| `email` | Text |  |
| `contact_last_update_date` | Date |  |
| `occupation` | Text |  |
| `employer_sector` | Text |  |
| `workplace` | Text |  |
| `workplace_address` | Text |  |
| `employment_last_update_date` | Date |  |
| `total_credit_limit` | Decimal |  |
| `total_potential_exposure` | Decimal |  |
| `total_debit_balance` | Decimal |  |
| `total_overdue` | Decimal |  |
| `contracts_number` | Integer |  |
| `providers_number` | Integer |  |
| `credit_report_log_id` | Integer |  |
| `notes` | Text |  |
| `province` | Text |  |

#### `public.credit_report_creditreportfile`

_Fields: 4_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `raw_data` | JSON |  |
| `formatted_file` | Text |  |
| `credit_report_log_id` | Integer |  |

#### `public.credit_report_creditreportlog`

_Fields: 13_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `provider_name` | Text |  |
| `cb_subject_code` | Text |  |
| `status` | Text |  |
| `purpose` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `loan_application_id` | Integer |  |
| `processor_id` | Integer |  |
| `profile_id` | Integer |  |
| `status_description` | Text |  |
| `provider_id` | Integer |  |
| `credit_line_id` | BigInteger |  |
| `is_billable` | Boolean |  |

#### `public.credit_report_creditreportprovider`

_Fields: 8_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `name` | Text |  |
| `enabled` | Boolean |  |
| `module` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_modified` | DateTimeWithLocalTZ |  |
| `preferred` | Boolean |  |
| `supports_non_installment_products` | Boolean |  |

#### `public.credit_report_creditreportunit`

_Fields: 16_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `cb_contract_code` | Text |  |
| `role` | Text |  |
| `contract_status` | Text |  |
| `contract_type` | Text |  |
| `contract_provider` | Text |  |
| `contract_provider_type` | Text |  |
| `past_due_status` | Text |  |
| `days_past_due` | Integer |  |
| `start_date` | Date |  |
| `due_date` | Date |  |
| `credit_limit` | Decimal |  |
| `debit_balance` | Decimal |  |
| `principal_overdue` | Decimal |  |
| `interest_overdue` | Decimal |  |
| `credit_report_id` | Integer |  |


### `customer_*`

#### `public.customer_success_dynamicgrouprevisiontype`

_Fields: 5_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `group_name` | Text |  |
| `group_type_fields` | Text |  |
| `default_revision_notes` | Text |  |
| `clear_revision_notes` | Boolean |  |

#### `public.customer_success_grouprevision`

_Fields: 9_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `status` | Text |  |
| `type` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_completed` | DateTimeWithLocalTZ |  |
| `object_id` | Integer |  |
| `content_type_id` | Integer |  |
| `processor_id` | Integer |  |
| `user_id` | Integer |  |

#### `public.customer_success_revision`

_Fields: 22_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `field` | Text |  |
| `notes` | Text |  |
| `old_value` | Text |  |
| `revised_value` | Text |  |
| `status` | Text |  |
| `type` | Text |  |
| `char_cache` | Text |  |
| `photo_cache` | Text |  |
| `file_cache` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_revised` | DateTimeWithLocalTZ |  |
| `datetime_verified` | DateTimeWithLocalTZ |  |
| `object_id` | Integer |  |
| `content_type_id` | Integer |  |
| `user_id` | Integer |  |
| `processor_id` | Integer |  |
| `purpose` | Text |  |
| `group_id` | Integer |  |
| `object_cache_content_type_id` | Integer |  |
| `object_cache_id` | Integer |  |
| `ocr_matching_notes` | Text |  |


### `digital_*`

#### `public.digital_signing_digitalsigningaccount`

_Fields: 18_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `registration_token` | Text |  |
| `account_id` | Text |  |
| `provider` | Text |  |
| `first_name` | Text |  |
| `last_name` | Text |  |
| `date_of_birth` | Date |  |
| `national_id_card_number` | Text |  |
| `email` | Text |  |
| `mobile_number` | Text |  |
| `status` | Text |  |
| `status_description` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `digital_signing_class` | Text |  |
| `cleaned_status_description` | Text |  |
| `selfie_file` | Text |  |
| `datetime_expired` | DateTimeWithLocalTZ |  |

#### `public.digital_signing_digitalsigningaccountinfo`

_Fields: 6_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `identity` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `digital_signing_account_id` | Integer |  |
| `loan_application_id` | Integer |  |


### `django_*`

#### `public.django_celery_beat_clockedschedule`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `clocked_time` | DateTimeWithLocalTZ |  |
| `enabled` | Boolean |  |

#### `public.django_celery_beat_crontabschedule`

_Fields: 7_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `minute` | Text |  |
| `hour` | Text |  |
| `day_of_week` | Text |  |
| `day_of_month` | Text |  |
| `month_of_year` | Text |  |
| `timezone` | Text |  |

#### `public.django_celery_beat_intervalschedule`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `every` | Integer |  |
| `period` | Text |  |

#### `public.django_celery_beat_periodictask`

_Fields: 23_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `name` | Text |  |
| `task` | Text |  |
| `args` | Text |  |
| `kwargs` | Text |  |
| `queue` | Text |  |
| `exchange` | Text |  |
| `routing_key` | Text |  |
| `expires` | DateTimeWithLocalTZ |  |
| `enabled` | Boolean |  |
| `last_run_at` | DateTimeWithLocalTZ |  |
| `total_run_count` | Integer |  |
| `date_changed` | DateTimeWithLocalTZ |  |
| `description` | Text |  |
| `crontab_id` | Integer |  |
| `interval_id` | Integer |  |
| `solar_id` | Integer |  |
| `one_off` | Boolean |  |
| `start_time` | DateTimeWithLocalTZ |  |
| `priority` | Integer |  |
| `headers` | Text |  |
| `expire_seconds` | Integer |  |
| `clocked_id` | Integer |  |

#### `public.django_celery_beat_periodictasks`

_Fields: 2_

| Field | Type | Description |
|---|---|---|
| `ident` | Integer |  |
| `last_update` | DateTimeWithLocalTZ |  |

#### `public.django_celery_beat_solarschedule`

_Fields: 4_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `event` | Text |  |
| `latitude` | Decimal |  |
| `longitude` | Decimal |  |

#### `public.django_fsm_log_statelog`

_Fields: 9_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `timestamp` | DateTimeWithLocalTZ |  |
| `state` | Text |  |
| `transition` | Text |  |
| `object_id` | Integer |  |
| `by_id` | Integer |  |
| `content_type_id` | Integer |  |
| `description` | Text |  |
| `source_state` | Text |  |

#### `public.django_migrations_backup`

_Fields: 4_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `app` | Text |  |
| `name` | Text |  |
| `applied` | DateTimeWithLocalTZ |  |


### `dynamic_*`

#### `public.dynamic_preferences_globalpreferencemodel`

_Fields: 4_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `section` | Text |  |
| `name` | Text |  |
| `raw_value` | Text |  |

#### `public.dynamic_preferences_users_userpreferencemodel`

_Fields: 5_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `section` | Text |  |
| `name` | Text |  |
| `raw_value` | Text |  |
| `instance_id` | Integer |  |


### `e_*`

#### `public.e_kyc_contactinquirylog`

_Fields: 21_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `transaction_id` | Text |  |
| `contact_point` | Text |  |
| `contact_type` | Text |  |
| `email_score` | Integer |  |
| `is_email_deliverable` | Boolean |  |
| `verification_type` | Text |  |
| `contactability` | Text |  |
| `is_whatsapp` | Boolean |  |
| `is_facebook` | Boolean |  |
| `is_telegram` | Boolean |  |
| `is_instagram` | Boolean |  |
| `is_viber` | Boolean |  |
| `is_github` | Boolean |  |
| `is_linkedin` | Boolean |  |
| `linkedin_company` | Text |  |
| `linkedin_title` | Text |  |
| `response_data` | JSON |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `loan_id` | Integer |  |
| `loan_app_id` | Integer |  |

#### `public.e_kyc_facecomparisontransaction`

_Fields: 11_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `transaction_id` | Text |  |
| `first_image_file` | Text |  |
| `second_image_file` | Text |  |
| `status` | Text |  |
| `score` | Float |  |
| `audit_log` | JSON |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `profile_id` | Integer |  |
| `identity` | Text |  |
| `loan_application_id` | Integer |  |

#### `public.e_kyc_h5livenesstransaction`

_Fields: 13_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `transaction_id` | Text |  |
| `url` | Text |  |
| `image_file` | Text |  |
| `score` | Integer |  |
| `status` | Text |  |
| `message` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `profile_id` | Integer |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `identity` | Text |  |
| `loan_application_id` | Integer |  |
| `historical_h5_token_data` | Text |  |

#### `public.e_kyc_incomeverificationlog`

_Fields: 7_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `status` | Text |  |
| `identity` | Text |  |
| `response_body` | JSON |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `loan_app_id` | Integer |  |

#### `public.e_kyc_livenessimage`

_Fields: 6_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `index` | Integer |  |
| `image_file` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `liveness_info_id` | Integer |  |

#### `public.e_kyc_livenessinfo`

_Fields: 9_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `identity` | Text |  |
| `provider` | Text |  |
| `score` | Float |  |
| `status` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `loan_application_id` | Integer |  |
| `profile_id` | Integer |  |

#### `public.e_kyc_livenesstransaction`

_Fields: 14_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `provider` | Text |  |
| `transaction_id` | Text |  |
| `identity` | Text |  |
| `token` | Text |  |
| `url` | Text |  |
| `image_1` | Text |  |
| `image_2` | Text |  |
| `score` | Float |  |
| `status` | Text |  |
| `raw_result` | JSON |  |
| `profile_id` | Integer |  |

#### `public.e_kyc_ocrtransaction`

_Fields: 12_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `transaction_id` | Text |  |
| `image_file` | Text |  |
| `image_type` | Text |  |
| `status` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `profile_id` | Integer |  |
| `tesseract_text` | Text |  |
| `loan_application_id` | Integer |  |
| `is_loan_application_data_matched` | Boolean |  |
| `ocr_data_matching_notes` | Text |  |
| `simplifi_entry_id` | Integer |  |

#### `public.e_kyc_privylivenesstransaction`

_Fields: 18_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `raw_result → face_1` | Text |  |
| `raw_result → face_2` | Text |  |
| `raw_result → fc_token` | Text |  |
| `raw_result → result` | Boolean |  |
| `raw_result → transaction_id` | Text |  |
| `transaction_id` | UUID |  |
| `identity` | Text |  |
| `token` | Text |  |
| `url` | Text |  |
| `image_1` | Text |  |
| `image_2` | Text |  |
| `score` | Float |  |
| `status` | Text |  |
| `raw_result` | JSON |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `profile_id` | Integer |  |


### `escrow_*`

#### `public.escrow_escrowprovider`

_Fields: 14_

| Field | Type | Description |
|---|---|---|
| `config_pack → api_key` | Text |  |
| `config_pack → internal_transfer_request_url` | Text |  |
| `config_pack → loan_disbursement_request_url` | Text |  |
| `config_pack → max_retries` | Integer |  |
| `config_pack → rdl_disbursement_request_url` | Text |  |
| `config_pack → webhook_token` | Text |  |
| `config_pack → withdrawal_request_url` | Text |  |
| `id` | Integer |  |
| `name` | Text |  |
| `enabled` | Boolean |  |
| `module` | Text |  |
| `config_pack` | JSON |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_modified` | DateTimeWithLocalTZ |  |

#### `public.escrow_escrowtransaction`

_Fields: 110_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `notification_data → account_number` | Text |  |
| `notification_data → amount` | Integer |  |
| `notification_data → annual_percentage_rate` | Integer |  |
| `notification_data → bank_code` | Text |  |
| `notification_data → bank_reference` | Text |  |
| `notification_data → borrower_id` | Text |  |
| `notification_data → business_id` | Text |  |
| `notification_data → created` | DateTime |  |
| `notification_data → customer_balance` | Integer |  |
| `notification_data → customer_id` | Text |  |
| `notification_data → description` | Text |  |
| `notification_data → destination_account_code` | Text |  |
| `notification_data → destination_account_holder_name` | Text |  |
| `notification_data → destination_account_number` | Text |  |
| `notification_data → expiration_date` | DateTime |  |
| `notification_data → external_id` | Text |  |
| `notification_data → failure_code` | Text |  |
| `notification_data → fee_amount` | Integer |  |
| `notification_data → id` | Text |  |
| `notification_data → investor_id` | Text |  |
| `notification_data → is_closed` | Boolean |  |
| `notification_data → is_direct` | Boolean |  |
| `notification_data → is_single_use` | Boolean |  |
| `notification_data → lenders` | Array |  |
| `notification_data → loan_id` | Text |  |
| `notification_data → loan_maturity_date` | DateTime |  |
| `notification_data → merchant_code` | Text |  |
| `notification_data → name` | Text |  |
| `notification_data → payment_type` | Text |  |
| `notification_data → principal_amount` | Integer |  |
| `notification_data → status` | Text |  |
| `notification_data → type` | Text |  |
| `notification_data → updated` | DateTime |  |
| `provider_response → account_number` | Text |  |
| `provider_response → amount` | Integer |  |
| `provider_response → bank_code` | Text |  |
| `provider_response → created` | DateTime |  |
| `provider_response → customer_id` | Text |  |
| `provider_response → data → amount` | Integer |  |
| `provider_response → data → annual_percentage_rate` | Integer |  |
| `provider_response → data → borrower_id` | Text |  |
| `provider_response → data → created` | DateTime |  |
| `provider_response → data → customer_id` | Text |  |
| `provider_response → data → description` | Text |  |
| `provider_response → data → destination_account_code` | Text |  |
| `provider_response → data → destination_account_holder_name` | Text |  |
| `provider_response → data → destination_account_number` | Text |  |
| `provider_response → data → error_code` | Text |  |
| `provider_response → data → external_id` | Text |  |
| `provider_response → data → fee_amount` | Integer |  |
| `provider_response → data → id` | Text |  |
| `provider_response → data → investor_id` | Text |  |
| `provider_response → data → is_direct` | Boolean |  |
| `provider_response → data → lenders` | Array |  |
| `provider_response → data → loan_id` | Text |  |
| `provider_response → data → loan_maturity_date` | DateTime |  |
| `provider_response → data → message` | Text |  |
| `provider_response → data → principal_amount` | Integer |  |
| `provider_response → data → status` | Text |  |
| `provider_response → data → type` | Text |  |
| `provider_response → data → updated` | DateTime |  |
| `provider_response → destination_account_code` | Text |  |
| `provider_response → destination_account_holder_name` | Text |  |
| `provider_response → destination_account_number` | Text |  |
| `provider_response → expiration_date` | DateTime |  |
| `provider_response → external_id` | Text |  |
| `provider_response → id` | Text |  |
| `provider_response → is_closed` | Boolean |  |
| `provider_response → is_direct` | Boolean |  |
| `provider_response → is_single_use` | Boolean |  |
| `provider_response → merchant_code` | Text |  |
| `provider_response → name` | Text |  |
| `provider_response → payment_type` | Text |  |
| `provider_response → response_code` | Integer |  |
| `provider_response → status` | Text |  |
| `provider_response → type` | Text |  |
| `provider_response → updated` | DateTime |  |
| `request_params → amount` | Integer |  |
| `request_params → annual_percentage_rate` | Integer |  |
| `request_params → bank_code` | Text |  |
| `request_params → borrower_id` | Text |  |
| `request_params → customer_id` | Text |  |
| `request_params → description` | Text |  |
| `request_params → destination_account_code` | Text |  |
| `request_params → destination_account_holder_name` | Text |  |
| `request_params → destination_account_number` | Text |  |
| `request_params → external_id` | Text |  |
| `request_params → lenders` | Array |  |
| `request_params → loan_id` | Text |  |
| `request_params → loan_maturity_date` | Text |  |
| `request_params → name` | Text |  |
| `request_params → payment_type` | Text |  |
| `request_params → type` | Text |  |
| `uuid` | UUID |  |
| `transaction_id` | Text |  |
| `amount` | Decimal |  |
| `status` | Text |  |
| `type` | Text |  |
| `notes` | Text |  |
| `request_params` | JSON |  |
| `provider_response` | JSON |  |
| `notification_data` | JSON |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `object_id` | Integer |  |
| `content_type_id` | Integer |  |
| `provider_id` | Integer |  |
| `receiver_id` | BigInteger |  |
| `sender_id` | BigInteger |  |

#### `public.escrow_splitrevenue`

_Fields: 11_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `uuid` | UUID |  |
| `status` | Text |  |
| `total_amount` | Decimal |  |
| `start_date_paid` | DateTimeWithLocalTZ |  |
| `end_date_paid` | DateTimeWithLocalTZ |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `calculator_type_class` | Text |  |
| `total_payment_outside_escrow` | Decimal |  |
| `repayment_report_file` | Text |  |
| `item_report_file` | Text |  |

#### `public.escrow_splitrevenue_lender`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `splitrevenue_id` | Integer |  |
| `user_id` | Integer |  |

#### `public.escrow_splitrevenueitem`

_Fields: 5_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `transaction_name` | Text |  |
| `amount` | Decimal |  |
| `payment_account_id` | BigInteger |  |
| `split_revenue_id` | Integer |  |


### `event_*`

#### `public.event_calenderevent`

_Fields: 5_

| Field | Type | Description |
|---|---|---|
| `id` | BigInteger |  |
| `month` | Integer |  |
| `is_enrollment` | Boolean |  |
| `remarks` | Text |  |
| `partner_id` | Integer |  |


### `forms_*`

#### `public.forms_generator_formfieldgenerator`

_Fields: 14_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `label` | Text |  |
| `help_text` | Text |  |
| `field_type` | Text |  |
| `required` | Boolean |  |
| `visible` | Boolean |  |
| `default_value` | Text |  |
| `data_field` | Boolean |  |
| `form_id` | Integer |  |
| `choices` | Text |  |
| `model_field_choices` | Text |  |
| `slug` | Text |  |
| `is_marketing_email` | Boolean |  |
| `is_readonly` | Boolean |  |

#### `public.forms_generator_formfieldleaddatamapping`

_Fields: 4_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `lead_field` | Text |  |
| `form_id` | Integer |  |
| `form_field_id` | Integer |  |

#### `public.forms_generator_formfileresponse`

_Fields: 6_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `slug` | Text |  |
| `file` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `data_id` | Integer |  |
| `form_id` | Integer |  |

#### `public.forms_generator_formgenerator`

_Fields: 30_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `uuid` | UUID |  |
| `name` | Text |  |
| `description` | Text |  |
| `footer` | Text |  |
| `footer_banner` | Text |  |
| `header_banner` | Text |  |
| `status` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `datetime_published` | DateTimeWithLocalTZ |  |
| `datetime_expiry` | DateTimeWithLocalTZ |  |
| `custom_code` | Text |  |
| `short_link_id` | Integer |  |
| `is_synced_to_leads` | Boolean |  |
| `lead_type` | Text |  |
| `school_id` | Integer |  |
| `form_submission_email_subject` | Text |  |
| `should_send_email_notification` | Boolean |  |
| `form_submission_template` | Text |  |
| `should_send_broadcast_notification` | Boolean |  |
| `broadcast_tags` | Text |  |
| `should_auto_publish_leads` | Boolean |  |
| `project_name` | Text |  |
| `include_quotation` | Boolean |  |
| `data_source` | Text |  |
| `show_quotation` | Boolean |  |
| `form_submission_email_attachment` | Text |  |
| `form_id` | Text |  |
| `header_full_banner` | Text |  |

#### `public.forms_generator_forminitialdata`

_Fields: 7_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `initial_data → email` | Text |  |
| `initial_data → nama-mahasiswa` | Text |  |
| `initial_data → nomor-ponsel` | Text |  |
| `initial_data` | JSON |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `form_id` | Integer |  |

#### `public.forms_generator_formresponse`

_Fields: 85_

| Field | Type | Description |
|---|---|---|
| `data → alamat-email` | Text |  |
| `data → apakah-ingin-kuliah-di-unesa-menggunakan-program-cicilan-danacita` | Boolean |  |
| `data → apakah-ingin-kuliah-di-universitas-atma-jaya-yogyakarta-menggunakan-program-cicilan-danacita` | Boolean |  |
| `data → apakah-ingin-kuliah-di-untar-menggunakan-program-cicilan-danacita` | Boolean |  |
| `data → apakah-kamu-calon-mahasiswa-ui` | Text |  |
| `data → apakah-kamu-calon-mahasiswamahasiswa-baru-ipb` | Text |  |
| `data → apakah-kamu-calon-mahasiswamahasiswa-baru-ugm` | Text |  |
| `data → apakah-kamu-calon-mahasiswamahasiswa-baru-ui` | Text |  |
| `data → apakah-kamu-calon-mahasiswamahasiswa-baru-uin-sunan-gunung-djati` | Text |  |
| `data → apakah-kamu-calon-mahasiswamahasiswa-baru-unpad` | Text |  |
| `data → apakah-kamu-calon-mahasiswamahasiswa-baru-uns` | Text |  |
| `data → batas-tanggal-pembayaran` | Text |  |
| `data → buat-akun-danacita` | Boolean |  |
| `data → bukti-tagihan` | Array |  |
| `data → cabang-ican-education` | Text |  |
| `data → cabang-idp` | Text |  |
| `data → daftarkan-saya-ke-danacita` | Boolean |  |
| `data → dari-1-10-seberapa-ingin-kamu-coba-danacita` | Text |  |
| `data → dengan-mengisi-form-ini-saya-setuju-untuk-mendapatkan-penawaran-dan-info-menarik-dari-tim-danacita` | Boolean |  |
| `data → dengan-mengisi-formulir-ini-saya-setuju-untuk-dihubungi-langsung-oleh-tim-danacita` | Boolean |  |
| `data → domisili` | Text |  |
| `data → domisili-tempat-tinggal` | Text |  |
| `data → e-mail` | Text |  |
| `data → email` | Text |  |
| `data → email-address` | Text |  |
| `data → estimasi-biaya-pendidikan-yang-dibutuhkan` | Float |  |
| `data → fakultas` | Text |  |
| `data → first-name` | Text |  |
| `data → jalur-penerimaan` | Text |  |
| `data → jenis-biaya-yang-dibutuhkan` | Text |  |
| `data → jenjang-pendidikan` | Text |  |
| `data → jika-bukan-cantumkan-kampus-kamu` | Text |  |
| `data → jurusan` | Text |  |
| `data → jurusan-prodi` | Text |  |
| `data → kampus-tujuan` | Text |  |
| `data → kapan-batas-akhir-pembayaran-dilakukan` | Text |  |
| `data → kode-referral-promo-code` | Text |  |
| `data → last-name` | Text |  |
| `data → mahasiswa-akti-yt` | Text |  |
| `data → mahasiswa-aktif` | Text |  |
| `data → mahasiswa-baru` | Text |  |
| `data → mahasiswa-baruaktif` | Text |  |
| `data → mendapatkan-informasi-danacita-dari` | Text |  |
| `data → mengetahui-informasi-danacita-dari-mana` | Text |  |
| `data → mengetahui-informasi-danacita-darimana` | Text |  |
| `data → menurut-kamu-apakah-danacita-cukup-membantu-mahasiswa-umby` | Text |  |
| `data → mobile-number` | Text |  |
| `data → nama` | Text |  |
| `data → nama-belakang` | Text |  |
| `data → nama-depan` | Text |  |
| `data → nama-lengkap-pelajar` | Text |  |
| `data → nama-mahasiswa` | Text |  |
| `data → nama-pelajar` | Text |  |
| `data → nama-sekolah-perguruan-tinggi` | Text |  |
| `data → name` | Text |  |
| `data → negara-tujuan` | Text |  |
| `data → no-hp` | Text |  |
| `data → nomer-hp` | Text |  |
| `data → nomor-hp` | Text |  |
| `data → nomor-hp-whatsapp-aktif` | Text |  |
| `data → nomor-ponsel` | Text |  |
| `data → nomor-teleponwhatsapp` | Text |  |
| `data → nomor-whatsapp` | Text |  |
| `data → nomor-whatsapp-aktif` | Text |  |
| `data → pendidikan-terakhir` | Text |  |
| `data → pertanyaan` | Text |  |
| `data → pilihan-cicilan` | Text |  |
| `data → pilihan-programkelas` | Text |  |
| `data → preferensi-tenor` | Integer |  |
| `data → rencana-mulai-perkuliahan` | Text |  |
| `data → saya-setuju-memberikan-data-ini-dan-dihubungi-oleh-tim-danacita` | Boolean |  |
| `data → saya-setuju-untuk-dihubungi-oleh-tim-terkait` | Boolean |  |
| `data → saya-setuju-untuk-memberikan-data-ini` | Boolean |  |
| `data → saya-setuju-untuk-memberikan-data-ini-ke-danacita` | Boolean |  |
| `data → saya-tertarik-menjadi-sahabat-danacita` | Boolean |  |
| `data → status-mahasiswa` | Text |  |
| `data → tau-informasi-danacita-ini-darimana` | Text |  |
| `data → tenor-cicilan` | Text |  |
| `data → umur` | Text |  |
| `id` | Integer |  |
| `data` | JSON |  |
| `form_id` | Integer |  |
| `content_type_id` | Integer |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `object_id` | Integer |  |

#### `public.forms_generator_formschoolgroup`

_Fields: 2_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `name` | Text |  |

#### `public.forms_generator_formschoolgroup_applicable_partners`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `formschoolgroup_id` | Integer |  |
| `partner_id` | Integer |  |


### `inquiries_*`

#### `public.inquiries_idinquirydata`

_Fields: 21_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `organizer_id` | Text |  |
| `type` | Text |  |
| `name` | Text |  |
| `ktp_number` | Text |  |
| `npwp_number` | Text |  |
| `contract_date` | Date |  |
| `disbursement_date` | Date |  |
| `reporting_date` | Date |  |
| `due_date` | Date |  |
| `applied_amount` | Decimal |  |
| `outstanding_amount` | Decimal |  |
| `past_due_bucket` | Text |  |
| `current_dpd` | Integer |  |
| `max_dpd` | Integer |  |
| `status_pinjaman` | Text |  |
| `profile_id` | Integer |  |
| `kind` | Text |  |
| `loan_application_id` | Integer |  |
| `mobile_number` | Text |  |
| `monthly_income` | Decimal |  |

#### `public.inquiries_idinquirydata_fdc_inquiries`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `idinquirydata_id` | Integer |  |
| `idinquirylog_id` | Integer |  |

#### `public.inquiries_idinquirylog`

_Fields: 37_

| Field | Type | Description |
|---|---|---|
| `full_response → historyInquiry → last3DaysInquiry` | Array |  |
| `full_response → historyInquiry → statistic → 180_hari` | Integer |  |
| `full_response → historyInquiry → statistic → 30_hari` | Integer |  |
| `full_response → historyInquiry → statistic → 360_hari` | Integer |  |
| `full_response → historyInquiry → statistic → 3_hari` | Integer |  |
| `full_response → historyInquiry → statistic → 7_hari` | Integer |  |
| `full_response → historyInquiry → statistic → 90_hari` | Integer |  |
| `full_response → historyInquiry → statistic → >360_hari` | Integer |  |
| `full_response → inquiryDate` | Text |  |
| `full_response → inquiryReason` | Text |  |
| `full_response → mail` | Text |  |
| `full_response → memberId` | Text |  |
| `full_response → memberName` | Text |  |
| `full_response → noHp` | Text |  |
| `full_response → noIdentitas` | Text |  |
| `full_response → pinjaman` | Array |  |
| `full_response → platformAktif → jumlahPlatformAktif` | Integer |  |
| `full_response → platformAktif → platform` | Array |  |
| `full_response → refferenceId` | Text |  |
| `full_response → status` | Text |  |
| `full_response → userId` | Text |  |
| `full_response → userName` | Text |  |
| `id` | Integer |  |
| `request_params → ktp_number` | Text |  |
| `request_params → reason` | Text |  |
| `request_params → reffid` | Text |  |
| `kind` | Text |  |
| `status` | Text |  |
| `reason` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `processor_id` | Integer |  |
| `profile_id` | Integer |  |
| `loan_application_id` | Integer |  |
| `full_response` | JSON |  |
| `request_params` | JSON |  |
| `status_description` | Text |  |
| `total_active_platform` | Integer |  |


### `insights_*`

#### `public.insights_clickevent`

_Fields: 9_

| Field | Type | Description |
|---|---|---|
| `id` | BigInteger |  |
| `ip` | IPAddress |  |
| `user_agent` | Text |  |
| `raw_user_agent` | Text |  |
| `location` | Text |  |
| `event_type` | Text |  |
| `timestamp` | DateTimeWithLocalTZ |  |
| `object_id` | Integer |  |
| `content_type_id` | Integer |  |

#### `public.insights_geolocation`

_Fields: 12_

| Field | Type | Description |
|---|---|---|
| `id` | BigInteger |  |
| `event` | Text |  |
| `ip` | IPAddress |  |
| `latitude` | Float |  |
| `longitude` | Float |  |
| `accuracy` | Float |  |
| `altitude` | Float |  |
| `heading` | Float |  |
| `speed` | Float |  |
| `loan_id` | Integer |  |
| `loan_application_id` | Integer |  |
| `user_id` | Integer |  |

#### `public.insights_uploadevent`

_Fields: 6_

| Field | Type | Description |
|---|---|---|
| `id` | BigInteger |  |
| `field` | Text |  |
| `upload_method` | Text |  |
| `timestamp` | DateTimeWithLocalTZ |  |
| `loan_application_id` | Integer |  |
| `user_id` | Integer |  |


### `integrations_*`

#### `public.integrations_integrationannouncement`

_Fields: 7_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `title` | Text |  |
| `content` | Text |  |
| `checkbox_text` | Text |  |
| `is_published` | Boolean |  |

#### `public.integrations_integrationannouncement_applicable_partners`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `integrationannouncement_id` | Integer |  |
| `partner_id` | Integer |  |

#### `public.integrations_integrationdataissue`

_Fields: 46_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `student_info_sent → address_line_1` | Text |  |
| `student_info_sent → address_line_2` | Text |  |
| `student_info_sent → course` | Text |  |
| `student_info_sent → current_due_total` | Text |  |
| `student_info_sent → date_due` | Text |  |
| `student_info_sent → date_of_birth` | Text |  |
| `student_info_sent → days_in_arrears` | Text |  |
| `student_info_sent → degree` | Text |  |
| `student_info_sent → digest` | Text |  |
| `student_info_sent → email` | Text |  |
| `student_info_sent → email_address` | Text |  |
| `student_info_sent → first_name` | Text |  |
| `student_info_sent → guardian_email` | Text |  |
| `student_info_sent → guardian_first_name` | Text |  |
| `student_info_sent → guardian_last_name` | Text |  |
| `student_info_sent → guardian_mobile_number` | Text |  |
| `student_info_sent → last_name` | Text |  |
| `student_info_sent → max_days_in_arrears` | Text |  |
| `student_info_sent → mobile_number` | Text |  |
| `student_info_sent → product` | Text |  |
| `student_info_sent → product_package` | Text |  |
| `student_info_sent → program` | Text |  |
| `student_info_sent → requested_principal_semester_1` | Text |  |
| `student_info_sent → requested_principal_semester_2` | Text |  |
| `student_info_sent → requested_principal_semester_3` | Text |  |
| `student_info_sent → requested_principal_semester_4` | Text |  |
| `student_info_sent → school` | Text |  |
| `student_info_sent → school_remaining_balance` | Text |  |
| `student_info_sent → source` | Text |  |
| `student_info_sent → student_id_number` | Text |  |
| `student_info_sent → submit.x` | Text |  |
| `student_info_sent → submit.y` | Text |  |
| `student_info_sent → year` | Text |  |
| `status` | Text |  |
| `reference_code` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_resolved` | DateTimeWithLocalTZ |  |
| `student_info_sent` | JSON |  |
| `digest_class_used` | Text |  |
| `error_level` | Text |  |
| `form_class_used` | Text |  |
| `integration_type` | Text |  |
| `notes` | Text |  |
| `school_id` | Integer |  |
| `source` | Text |  |

#### `public.integrations_paymentprofile`

_Fields: 43_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `first_name` | Text |  |
| `last_name` | Text |  |
| `email` | Text |  |
| `mobile_number` | Text |  |
| `school_remaining_balance` | Decimal |  |
| `current_due_total` | Decimal |  |
| `days_in_arrears` | Integer |  |
| `date_due` | Date |  |
| `is_preapproved` | Boolean |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `school_id` | Integer |  |
| `user_id` | Integer |  |
| `student_id_number` | Text |  |
| `uuid` | UUID |  |
| `loan_id` | Integer |  |
| `address_line_1` | Text |  |
| `address_line_2` | Text |  |
| `degree` | Text |  |
| `guardian_email` | Text |  |
| `guardian_first_name` | Text |  |
| `guardian_last_name` | Text |  |
| `guardian_mobile_number` | Text |  |
| `program` | Text |  |
| `year_level` | Integer |  |
| `checkout_attempts_count` | Integer |  |
| `beneficiary_account_number` | Text |  |
| `beneficiary_bank_name` | Text |  |
| `virtual_account_validity_date` | DateTimeWithLocalTZ |  |
| `product_id` | Integer |  |
| `product_package_id` | Integer |  |
| `requested_principal_semester_1` | Decimal |  |
| `requested_principal_semester_2` | Decimal |  |
| `requested_principal_semester_3` | Decimal |  |
| `requested_principal_semester_4` | Decimal |  |
| `datetime_user_guardian_consent` | DateTimeWithLocalTZ |  |
| `source` | Text |  |
| `guarantor_email` | Text |  |
| `guarantor_first_name` | Text |  |
| `guarantor_last_name` | Text |  |
| `guarantor_mobile_number` | Text |  |
| `guarantor_relationship_to_student` | Text |  |
| `loan_application_id` | Integer |  |

#### `public.integrations_wholesaleloansbatch`

_Fields: 11_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `uuid` | UUID |  |
| `status` | Text |  |
| `batch_file` | Text |  |
| `error_file` | Text |  |
| `batch_file_type` | Text |  |
| `processing_type` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `partner_id` | Integer |  |
| `datetime_user_guardian_consent` | DateTimeWithLocalTZ |  |

#### `public.integrations_wholesaleprofile`

_Fields: 47_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `uuid` | UUID |  |
| `email` | Text |  |
| `last_name` | Text |  |
| `first_name` | Text |  |
| `date_of_birth` | Date |  |
| `place_of_birth` | Text |  |
| `marital_status` | Text |  |
| `mobile_number` | Text |  |
| `sub_district` | Text |  |
| `address_line` | Text |  |
| `guardian_first_name` | Text |  |
| `guardian_last_name` | Text |  |
| `guardian_mobile_number` | Text |  |
| `student_id_number` | Text |  |
| `outstanding_balance_from_previous_term` | Decimal |  |
| `total_due_from_previous_term` | Decimal |  |
| `student_status` | Text |  |
| `max_days_in_arrears` | Integer |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `user_data` | JSON |  |
| `city_id` | Integer |  |
| `province_id` | Integer |  |
| `school_id` | Integer |  |
| `user_id` | Integer |  |
| `risk_tier` | Text |  |
| `current_due_total` | Decimal |  |
| `degree` | Text |  |
| `program` | Text |  |
| `balance_from_older_terms` | Decimal |  |
| `total_due_for_upcoming_term` | Decimal |  |
| `duplicates_addressed` | Boolean |  |
| `worst_performance_including_duplicates` | Integer |  |
| `has_duplicate_accounts` | Boolean |  |
| `checkout_attempts_count` | Integer |  |
| `is_eligible_to_apply` | Boolean |  |
| `datetime_user_guardian_consent` | DateTimeWithLocalTZ |  |
| `beneficiary_account_number` | Text |  |
| `beneficiary_bank_name` | Text |  |
| `product_id` | Integer |  |
| `product_package_id` | Integer |  |
| `requested_principal_semester_1` | Decimal |  |
| `requested_principal_semester_2` | Decimal |  |
| `requested_principal_semester_3` | Decimal |  |
| `requested_principal_semester_4` | Decimal |  |
| `virtual_account_validity_date` | DateTimeWithLocalTZ |  |
| `source` | Text |  |


### `leads_*`

#### `public.leads_leaddraft`

_Fields: 30_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `address` | Text |  |
| `first_name` | Text |  |
| `last_name` | Text |  |
| `email` | Text |  |
| `mobile_number` | Text |  |
| `degree` | Text |  |
| `course_name` | Text |  |
| `student_id_number` | Text |  |
| `city_id` | Integer |  |
| `product_id` | Integer |  |
| `province_id` | Integer |  |
| `school_id` | Integer |  |
| `lead_type` | Text |  |
| `borrower_id` | Integer |  |
| `data_source` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `student_status` | Text |  |
| `date_of_birth` | Date |  |
| `borrower_school_assessment_id` | Integer |  |
| `borrower_school_assessment_file` | Text |  |
| `is_assessed` | Boolean |  |
| `loan_application_id` | Integer |  |
| `payment_date_due` | Date |  |
| `payment_purpose` | Text |  |
| `requested_principal` | Decimal |  |
| `school_name` | Text |  |
| `is_non_segment` | Boolean |  |
| `school_country_id` | Integer |  |
| `school_type` | Text |  |

#### `public.leads_leadinteraction`

_Fields: 22_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `kind` | Text |  |
| `operation` | Text |  |
| `channel` | Text |  |
| `type` | Text |  |
| `description` | Text |  |
| `full_name` | Text |  |
| `contact_point` | Text |  |
| `identity` | Text |  |
| `datetime_interacted` | DateTimeWithLocalTZ |  |
| `rating` | Integer |  |
| `rating_context` | Text |  |
| `datetime_follow_up` | DateTimeWithLocalTZ |  |
| `batch_id` | Integer |  |
| `processor_id` | Integer |  |
| `result` | Text |  |
| `borrower_id` | Integer |  |
| `lead_draft_id` | Integer |  |
| `student_status` | Text |  |
| `country` | Text |  |
| `payment_date_due` | Date |  |
| `requested_principal` | Decimal |  |

#### `public.leads_leadinteractionbatch`

_Fields: 9_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `uuid` | UUID |  |
| `status` | Text |  |
| `interaction_file` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `datetime_deleted` | DateTimeWithLocalTZ |  |
| `datetime_ingested` | DateTimeWithLocalTZ |  |
| `error_file` | Text |  |

#### `public.leads_userleadsbatch`

_Fields: 14_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `uuid` | UUID |  |
| `batch_file` | Text |  |
| `batch_type` | Text |  |
| `error_file` | Text |  |
| `status` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `datetime_deleted` | DateTimeWithLocalTZ |  |
| `datetime_ingested` | DateTimeWithLocalTZ |  |
| `batch_file_type` | Text |  |
| `school_id` | Integer |  |
| `uploaded_by_id` | Integer |  |
| `data_source` | Text |  |


### `lenders_*`

#### `public.lenders_lendercommissionrate`

_Fields: 11_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `start_date` | Date |  |
| `end_date` | Date |  |
| `lender_return_rate` | Decimal |  |
| `commission_rate` | Decimal |  |
| `lender_contract_id` | Integer |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `previous_commission_rate_id` | Integer |  |
| `lender_id` | Integer |  |
| `lender_flat_interest_rate` | Decimal |  |

#### `public.lenders_lenderconfig`

_Fields: 8_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `config` | Text |  |
| `start_date` | Date |  |
| `end_date` | Date |  |
| `value` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `lender_id` | Integer |  |

#### `public.lenders_lendercontract`

_Fields: 13_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `uuid` | UUID |  |
| `reference_code` | Text |  |
| `lender_return_rate` | Decimal |  |
| `platform_rate` | Decimal |  |
| `is_active` | Boolean |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `datetime_deleted` | DateTimeWithLocalTZ |  |
| `lender_id` | Integer |  |
| `income_source` | Text |  |
| `commission` | Decimal |  |
| `maximum_financing_facility_amount` | Decimal |  |

#### `public.lenders_lenderoverview`

_Fields: 9_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `total_actual_disbursement_amount` | Decimal |  |
| `total_amount_deposited` | Decimal |  |
| `funding_balance` | Decimal |  |
| `total_repayment_received` | Decimal |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `datetime_deleted` | DateTimeWithLocalTZ |  |
| `lender_id` | Integer |  |

#### `public.lenders_lenderprofile`

_Fields: 44_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `type` | Text |  |
| `first_name` | Text |  |
| `last_name` | Text |  |
| `company_name` | Text |  |
| `email_of_poc` | Text |  |
| `mobile_number` | Text |  |
| `identity_card_number` | Text |  |
| `status` | Text |  |
| `user_id` | Integer |  |
| `bank_account_number` | Text |  |
| `bank_name` | Text |  |
| `business_license_file` | Text |  |
| `cert_of_incorporation_file` | Text |  |
| `address` | Text |  |
| `company_pic_identity_card_file` | Text |  |
| `identity_card_file` | Text |  |
| `privy_id` | Text |  |
| `uuid` | UUID |  |
| `va_number` | Text |  |
| `poa_file` | Text |  |
| `citizenship` | Text |  |
| `city_id` | Integer |  |
| `gender` | Text |  |
| `identity_card_type` | Text |  |
| `province_id` | Integer |  |
| `date_of_birth` | Date |  |
| `employment_industry_id` | Integer |  |
| `employment_status` | Text |  |
| `employment_tenure` | Integer |  |
| `last_educational_degree` | Text |  |
| `marital_status` | Text |  |
| `monthly_income` | Decimal |  |
| `place_of_birth` | Text |  |
| `postal_code` | Text |  |
| `religion` | Text |  |
| `agreement_letter_number` | Text |  |
| `amendment_deed_date` | Date |  |
| `amendment_deed_number` | Text |  |
| `date_of_incorporation` | Date |  |
| `place_of_incorporation` | Text |  |
| `agreement_letter_date` | Date |  |
| `lender_type` | Text |  |
| `business_registration_number` | Text |  |

#### `public.lenders_lenderreturntransaction`

_Fields: 8_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_processed_start` | DateTimeWithLocalTZ |  |
| `datetime_processed_end` | DateTimeWithLocalTZ |  |
| `datetime_lender_return_paid` | DateTimeWithLocalTZ |  |
| `status` | Text |  |
| `notes` | Text |  |
| `lender_id` | Integer |  |

#### `public.lenders_lenderriskassessment`

_Fields: 17_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `is_enabled` | Boolean |  |
| `min_approved_principal` | Decimal |  |
| `max_approved_principal` | Decimal |  |
| `min_debt_burden_ratio` | Decimal |  |
| `max_debt_burden_ratio` | Decimal |  |
| `lender_id` | Integer |  |
| `max_applicable_loan_tenor` | Integer |  |
| `min_applicable_loan_tenor` | Integer |  |
| `applicable_guarantor_type` | Text |  |
| `max_discount_rate` | Decimal |  |
| `min_discount_rate` | Decimal |  |
| `assignment_priority` | Integer |  |
| `need_clik_history_data` | Boolean |  |
| `need_fdc_history_data` | Boolean |  |
| `partner_type` | Text |  |
| `history_data_condition` | Text |  |

#### `public.lenders_lenderriskassessment_decision_code`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `lenderriskassessment_id` | Integer |  |
| `decisioncode_id` | Integer |  |

#### `public.lenders_lenderriskassessment_loan_products`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `lenderriskassessment_id` | Integer |  |
| `loanproduct_id` | Integer |  |

#### `public.lenders_lendertransaction`

_Fields: 10_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `uuid` | UUID |  |
| `amount_deposited` | Decimal |  |
| `cooperation_agreement_file` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `datetime_deleted` | DateTimeWithLocalTZ |  |
| `datetime_deposited` | DateTimeWithLocalTZ |  |
| `lender_id` | Integer |  |
| `notes` | Text |  |


### `loans_*`

#### `public.loans_assignment`

_Fields: 6_

| Field | Type | Description |
|---|---|---|
| `action` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `processor_id` | Integer |  |
| `loan_id` | Integer |  |
| `id` | Integer |  |
| `loan_app_id` | Integer |  |

#### `public.loans_availableprocessor`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `datetime_since` | DateTimeWithLocalTZ |  |
| `processor_id` | Integer |  |

#### `public.loans_beneficiaryinfo`

_Fields: 10_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `first_name` | Text |  |
| `last_name` | Text |  |
| `student_id_number` | Text |  |
| `mobile_number` | Text |  |
| `email` | Text |  |
| `loan_id` | Integer |  |
| `loan_application_id` | Integer |  |
| `school_id` | Integer |  |
| `student_email` | Text |  |

#### `public.loans_buybackloanbatch`

_Fields: 7_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `uuid` | UUID |  |
| `batch_file` | Text |  |
| `error_file` | Text |  |
| `status` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |

#### `public.loans_cashloanoffer`

_Fields: 17_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `raw_data` | JSON |  |
| `uuid` | UUID |  |
| `status` | Text |  |
| `valid_start_date` | DateTimeWithLocalTZ |  |
| `valid_end_date` | DateTimeWithLocalTZ |  |
| `requested_principal` | Decimal |  |
| `datetime_accepted` | DateTimeWithLocalTZ |  |
| `datetime_rejected` | DateTimeWithLocalTZ |  |
| `datetime_expired` | DateTimeWithLocalTZ |  |
| `batch_id` | Integer |  |
| `borrower_id` | Integer |  |
| `loan_application_id` | Integer |  |
| `product_id` | Integer |  |
| `show_homepage_banner` | Boolean |  |

#### `public.loans_cashloanoffer_products`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `cashloanoffer_id` | Integer |  |
| `loanproduct_id` | Integer |  |

#### `public.loans_cashloanofferbatch`

_Fields: 7_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `uuid` | UUID |  |
| `status` | Text |  |
| `batch_file` | Text |  |
| `error_file` | Text |  |

#### `public.loans_coborrowerinfo`

_Fields: 33_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `first_name` | Text |  |
| `last_name` | Text |  |
| `relationship_to_borrower` | Text |  |
| `relationship_to_beneficiary` | Text |  |
| `marital_status` | Text |  |
| `mobile_number` | Text |  |
| `email` | Text |  |
| `date_of_birth` | Date |  |
| `place_of_birth` | Text |  |
| `address_line_1` | Text |  |
| `address_line_2` | Text |  |
| `nearest_landmark` | Text |  |
| `barangay` | Text |  |
| `proof_of_residence_file` | Text |  |
| `proof_of_residence_file_type` | Text |  |
| `position` | Text |  |
| `business_name` | Text |  |
| `business_address` | Text |  |
| `job_start_date` | Date |  |
| `monthly_income` | Decimal |  |
| `tin_number` | Text |  |
| `sss_number` | Text |  |
| `source_of_income` | Text |  |
| `proof_of_income_file` | Text |  |
| `proof_of_income_file_type` | Text |  |
| `name_of_remitter` | Text |  |
| `industry_id` | Integer |  |
| `city_id` | Integer |  |
| `loan_id` | Integer |  |
| `loan_application_id` | Integer |  |
| `province_id` | Integer |  |
| `is_address_same_as_borrower` | Boolean |  |

#### `public.loans_cohort`

_Fields: 20_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `name` | Text |  |
| `slug` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `net_principal_of_npl_loans` | Decimal |  |
| `npl_percentage` | Decimal |  |
| `number_of_npl_loans` | Integer |  |
| `total_approved_principal` | Decimal |  |
| `total_number_of_loans` | Integer |  |
| `disbursement_cohort_end_date` | Date |  |
| `disbursement_cohort_start_date` | Date |  |
| `display_on_dashboard` | Boolean |  |
| `cohort_grouping_end_date` | Date |  |
| `cohort_grouping_start_date` | Date |  |
| `cohort_grouping_id` | Integer |  |
| `total_disbursed_amount` | Decimal |  |
| `cut_off_date` | Date |  |
| `risk_share_amount` | Decimal |  |
| `risk_share_percentage_cap` | Decimal |  |

#### `public.loans_cohort_applicable_partners`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `cohort_id` | Integer |  |
| `partner_id` | Integer |  |

#### `public.loans_cohortgrouping`

_Fields: 1_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |

#### `public.loans_cohortgrouping_partners`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `cohortgrouping_id` | Integer |  |
| `partner_id` | Integer |  |

#### `public.loans_cohortgroupingperiod`

_Fields: 5_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `date_start` | Date |  |
| `date_end` | Date |  |
| `cohort_grouping_id` | Integer |  |
| `loan_product_id` | Integer |  |

#### `public.loans_collectionlog`

_Fields: 21_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `kind` | Text |  |
| `operation` | Text |  |
| `channel` | Text |  |
| `type` | Text |  |
| `description` | Text |  |
| `full_name` | Text |  |
| `contact_point` | Text |  |
| `identity` | Text |  |
| `datetime_interacted` | DateTimeWithLocalTZ |  |
| `rating` | Integer |  |
| `rating_context` | Text |  |
| `datetime_follow_up` | DateTimeWithLocalTZ |  |
| `call_result_code` | Text |  |
| `RFD_code` | Text |  |
| `loan_id` | Integer |  |
| `processor_id` | Integer |  |
| `batch_id` | Integer |  |
| `collector_id` | Integer |  |
| `visit_picture` | Text |  |
| `is_pinned` | Boolean |  |

#### `public.loans_collectionlogbatch`

_Fields: 11_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `uuid` | UUID |  |
| `status` | Text |  |
| `collection_log_file` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `datetime_deleted` | DateTimeWithLocalTZ |  |
| `datetime_ingested` | DateTimeWithLocalTZ |  |
| `error_file` | Text |  |
| `invalid_entries` | Integer |  |
| `total_entries` | Integer |  |

#### `public.loans_collector`

_Fields: 2_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `name` | Text |  |

#### `public.loans_contractexpirationpolicy`

_Fields: 4_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `loan_status` | Text |  |
| `days_to_expiration` | Integer |  |
| `product_id` | Integer |  |

#### `public.loans_coordinationnote`

_Fields: 8_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `channel` | Text |  |
| `note` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `author_id` | Integer |  |
| `loan_id` | Integer |  |
| `loan_app_id` | Integer |  |

#### `public.loans_debtrelief`

_Fields: 9_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `relief_amount` | Decimal |  |
| `date_start` | Date |  |
| `tenor` | Integer |  |
| `datetime_activated` | DateTimeWithLocalTZ |  |
| `datetime_reverted` | DateTimeWithLocalTZ |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `loan_id` | Integer |  |

#### `public.loans_decisioncode`

_Fields: 7_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `type` | Text |  |
| `code` | Text |  |
| `name` | Text |  |
| `generic_code` | Text |  |
| `details` | Text |  |
| `time_auto_rejected` | Integer |  |

#### `public.loans_decisioncode_approvers`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `decisioncode_id` | Integer |  |
| `adminrole_id` | Integer |  |

#### `public.loans_employeecashloanoffer`

_Fields: 21_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `raw_data` | JSON |  |
| `uuid` | UUID |  |
| `status` | Text |  |
| `requested_principal` | Decimal |  |
| `employee_source_of_income` | Text |  |
| `employee_monthly_income` | Decimal |  |
| `employee_average_annual_income` | Decimal |  |
| `employee_tenure` | Integer |  |
| `employee_business_name` | Text |  |
| `employee_business_address` | Text |  |
| `employee_business_phone` | Text |  |
| `employee_bank_account_name` | Text |  |
| `employee_bank_account_number` | Text |  |
| `batch_id` | Integer |  |
| `borrower_id` | Integer |  |
| `employee_industry_id` | Integer |  |
| `loan_application_id` | Integer |  |
| `partner_id` | Integer |  |

#### `public.loans_employeecashloanoffer_applicable_products`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `employeecashloanoffer_id` | Integer |  |
| `loanproduct_id` | Integer |  |

#### `public.loans_employeecashloanofferbatch`

_Fields: 7_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `uuid` | UUID |  |
| `status` | Text |  |
| `batch_file` | Text |  |
| `error_file` | Text |  |

#### `public.loans_historicallog`

_Fields: 109_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `profile_data → acquisition_channel` | Text |  |
| `profile_data → address_line_2` | Text |  |
| `profile_data → address_rt` | Text |  |
| `profile_data → address_rw` | Text |  |
| `profile_data → borrower_industry` | Integer |  |
| `profile_data → borrower_npwp_number` | Text |  |
| `profile_data → borrower_position` | Text |  |
| `profile_data → borrower_tenure` | Integer |  |
| `profile_data → city` | Integer |  |
| `profile_data → connected_to_facebook` | Boolean |  |
| `profile_data → connected_to_instagram` | Boolean |  |
| `profile_data → connected_to_linkedin` | Boolean |  |
| `profile_data → connected_to_twitter` | Boolean |  |
| `profile_data → current_due_total` | Text |  |
| `profile_data → datetime_profile_check` | DateTime |  |
| `profile_data → days_in_arrears` | Integer |  |
| `profile_data → degree` | Text |  |
| `profile_data → guarantor_address` | Text |  |
| `profile_data → guarantor_address_rt` | Text |  |
| `profile_data → guarantor_address_rw` | Text |  |
| `profile_data → guarantor_business_name` | Text |  |
| `profile_data → guarantor_business_phone` | Text |  |
| `profile_data → guarantor_city` | Integer |  |
| `profile_data → guarantor_date_of_birth` | Text |  |
| `profile_data → guarantor_first_name` | Text |  |
| `profile_data → guarantor_gender` | Text |  |
| `profile_data → guarantor_job_start_date` | Text |  |
| `profile_data → guarantor_ktp_address_rt` | Text |  |
| `profile_data → guarantor_ktp_address_rw` | Text |  |
| `profile_data → guarantor_ktp_province` | Integer |  |
| `profile_data → guarantor_marital_status` | Text |  |
| `profile_data → guarantor_mobile_number` | Text |  |
| `profile_data → guarantor_monthly_income` | Text |  |
| `profile_data → guarantor_nationality` | Text |  |
| `profile_data → guarantor_npwp_number` | Text |  |
| `profile_data → guarantor_place_of_birth` | Text |  |
| `profile_data → guarantor_privy_id` | Text |  |
| `profile_data → guarantor_province` | Integer |  |
| `profile_data → guarantor_religion` | Text |  |
| `profile_data → guarantor_sub_district` | Integer |  |
| `profile_data → guarantor_tenure` | Integer |  |
| `profile_data → guarantor_type` | Text |  |
| `profile_data → guardian_last_name` | Text |  |
| `profile_data → guardian_mobile_number` | Text |  |
| `profile_data → guardian_province` | Integer |  |
| `profile_data → id` | Integer |  |
| `profile_data → instagram_url` | Text |  |
| `profile_data → internal_notes` | Text |  |
| `profile_data → is_deleted` | Boolean |  |
| `profile_data → is_employed` | Boolean |  |
| `profile_data → is_integrated` | Boolean |  |
| `profile_data → ktp_address` | Text |  |
| `profile_data → ktp_address_rt` | Text |  |
| `profile_data → ktp_city` | Integer |  |
| `profile_data → ktp_file_skip_status` | Boolean |  |
| `profile_data → ktp_id_card_number` | Text |  |
| `profile_data → ktp_ocr_file` | Text |  |
| `profile_data → ktp_postal_code` | Text |  |
| `profile_data → ktp_province` | Integer |  |
| `profile_data → ktp_sub_district` | Integer |  |
| `profile_data → marital_status` | Text |  |
| `profile_data → mothers_maiden_name` | Text |  |
| `profile_data → place_of_birth` | Text |  |
| `profile_data → polymorphic_ctype` | Integer |  |
| `profile_data → privy_id` | Text |  |
| `profile_data → privy_reject_reason` | Text |  |
| `profile_data → privy_user_token` | Text |  |
| `profile_data → program` | Text |  |
| `profile_data → province` | Integer |  |
| `profile_data → religion` | Text |  |
| `profile_data → residence_ownership` | Text |  |
| `profile_data → selfie_file` | Text |  |
| `profile_data → selfie_file_notes` | Text |  |
| `profile_data → selfie_file_status` | Text |  |
| `profile_data → status` | Text |  |
| `profile_data → student_status` | Text |  |
| `profile_data → sub_district` | Integer |  |
| `profile_data → user` | Integer |  |
| `profile_data → year_level` | Integer |  |
| `user_data → date_joined` | DateTime |  |
| `user_data → datetime_accept_terms_and_policy` | DateTime |  |
| `user_data → email` | Text |  |
| `user_data → entry_point` | Text |  |
| `user_data → existence_type` | Text |  |
| `user_data → google_account_id` | Text |  |
| `user_data → id` | Integer |  |
| `user_data → is_eligible_to_apply` | Boolean |  |
| `user_data → is_onboarding_modal_completed` | Boolean |  |
| `user_data → is_onboarding_modal_skip_later` | Boolean |  |
| `user_data → level` | Integer |  |
| `user_data → partner_assignments` | Array |  |
| `user_data → partner_role` | Text |  |
| `user_data → platform_entry_point` | Text |  |
| `user_data → referred_by` | Integer |  |
| `user_data → referrer_referral_code` | Text |  |
| `user_data → reward_account → account_name` | Text |  |
| `user_data → school` | Integer |  |
| `user_data → type` | Text |  |
| `user_data → username` | Text |  |
| `user_data → uuid` | Text |  |
| `is_first_loan` | Boolean |  |
| `datetime_created` | Time |  |
| `user_data` | JSON |  |
| `profile_data` | JSON |  |
| `loan_id` | Integer |  |
| `previous_log_id` | Integer |  |
| `profile_id` | Integer |  |
| `user_id` | Integer |  |

#### `public.loans_historicalnpl`

_Fields: 6_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `number_of_npl_loans` | Integer |  |
| `net_principal_of_npl_loans` | Decimal |  |
| `npl_percentage` | Decimal |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `cohort_id` | Integer |  |

#### `public.loans_idfintechdatacenterreport`

_Fields: 5_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `report` | Text |  |
| `version` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `filename` | Text |  |

#### `public.loans_idloanapplication`

_Fields: 102_

| Field | Type | Description |
|---|---|---|
| `loanapplication_ptr_id` | Integer |  |
| `academic_term_needed` | Text |  |
| `religion` | Text |  |
| `student_status` | Text |  |
| `student_proof_of_residence_file_type` | Text |  |
| `marital_status` | Text |  |
| `driver_license_card_file` | Text |  |
| `residence_ownership` | Text |  |
| `ktp_ocr_file` | Text |  |
| `ktp_id_card_number` | Text |  |
| `ktp_address` | Text |  |
| `ktp_address_rt` | Text |  |
| `ktp_address_rw` | Text |  |
| `student_ktp_same_as_current_address` | Boolean |  |
| `address_rt` | Text |  |
| `address_rw` | Text |  |
| `privy_id` | Text |  |
| `privy_oauth_email` | Text |  |
| `privy_oauth_mobile_number` | Text |  |
| `privy_registration_status` | Text |  |
| `privy_reject_reason` | Text |  |
| `privy_user_token` | Text |  |
| `virtual_account_validity_date` | Date |  |
| `virtual_account_borrower_notes` | Text |  |
| `guarantor_religion` | Text |  |
| `guarantor_marital_status` | Text |  |
| `guarantor_family_card_file` | Text |  |
| `guarantor_driver_license_card_file` | Text |  |
| `guarantor_address_rt` | Text |  |
| `guarantor_address_rw` | Text |  |
| `guarantor_residence_ownership` | Text |  |
| `guarantor_proof_of_residence_file_type` | Text |  |
| `guarantor_ktp_file` | Text |  |
| `guarantor_ktp_id_card_number` | Text |  |
| `guarantor_ktp_same_as_current_address` | Boolean |  |
| `guarantor_ktp_address` | Text |  |
| `guarantor_ktp_address_rt` | Text |  |
| `guarantor_ktp_address_rw` | Text |  |
| `guarantor_npwp_number` | Text |  |
| `guarantor_privy_id` | Text |  |
| `guarantor_privy_oauth_email` | Text |  |
| `guarantor_privy_oauth_mobile_number` | Text |  |
| `guarantor_privy_registration_status` | Text |  |
| `guarantor_privy_reject_reason` | Text |  |
| `guarantor_privy_user_token` | Text |  |
| `guarantor_employment_status_text` | Text |  |
| `guarantor_proof_of_income_file_type` | Text |  |
| `secondary_guarantor_id_file` | Text |  |
| `secondary_guarantor_id_file_notes` | Text |  |
| `secondary_guarantor_proof_of_income_file` | Text |  |
| `secondary_guarantor_proof_of_income_file_notes` | Text |  |
| `reference_has_confirmed` | Boolean |  |
| `district_id` | Integer |  |
| `guarantor_district_id` | Integer |  |
| `guarantor_ktp_city_id` | Integer |  |
| `guarantor_ktp_district_id` | Integer |  |
| `guarantor_ktp_province_id` | Integer |  |
| `guarantor_ktp_sub_district_id` | Integer |  |
| `guarantor_sub_district_id` | Integer |  |
| `ktp_city_id` | Integer |  |
| `ktp_district_id` | Integer |  |
| `ktp_province_id` | Integer |  |
| `ktp_sub_district_id` | Integer |  |
| `sub_district_id` | Integer |  |
| `is_offer_link_loan` | Boolean |  |
| `outstanding_loan_amount` | Decimal |  |
| `outstanding_principal_balance` | Decimal |  |
| `borrower_change_of_data_selfie_file` | Text |  |
| `borrower_change_of_data_selfie_file_notes` | Text |  |
| `guarantor_ktp_file_skip_status` | Boolean |  |
| `ktp_file_skip_status` | Boolean |  |
| `guarantor_change_of_data_selfie_file` | Text |  |
| `guarantor_change_of_data_selfie_file_notes` | Text |  |
| `guarantor_ktp_postal_code` | Text |  |
| `guarantor_last_educational_degree` | Text |  |
| `ktp_postal_code` | Text |  |
| `last_educational_degree` | Text |  |
| `borrower_digital_signing_account_id` | Integer |  |
| `guarantor_digital_signing_account_id` | Integer |  |
| `family_card_file` | Text |  |
| `referral_code` | Text |  |
| `borrower_employment_status_text` | Text |  |
| `borrower_npwp_number` | Text |  |
| `additional_proof_of_income_id` | Integer |  |
| `secondary_guarantor_proof_of_income_id` | Integer |  |
| `mothers_maiden_name` | Text |  |
| `borrower_identity` | Text |  |
| `borrower_relationship_to_student` | Text |  |
| `guarantor_relationship_to_borrower` | Text |  |
| `purpose` | Text |  |
| `borrower_number_of_dependents` | Integer |  |
| `guarantor_has_confirmed_number_of_ongoing_loans` | Boolean |  |
| `borrower_average_annual_income` | Decimal |  |
| `borrower_source_of_income` | Text |  |
| `guarantor_average_annual_income` | Decimal |  |
| `guarantor_source_of_income` | Text |  |
| `digital_signature_provider` | Text |  |
| `borrower_employment_status_id` | Integer |  |
| `guarantor_employment_status_id` | Integer |  |
| `guarantor_mothers_maiden_name` | Text |  |
| `is_recontest` | Boolean |  |
| `recontest_parent_loan_application_id` | Integer |  |

#### `public.loans_idmultisemesterloan`

_Fields: 4_

| Field | Type | Description |
|---|---|---|
| `idtuitionloan_ptr_id` | Integer |  |
| `semester_number` | Integer |  |
| `is_need_reconfirm_principal` | Boolean |  |
| `first_tranche_reference_code` | Text |  |

#### `public.loans_idmultisemesterloanapplication`

_Fields: 6_

| Field | Type | Description |
|---|---|---|
| `idloanapplication_ptr_id` | Integer |  |
| `semester_count` | Integer |  |
| `product_type` | Text |  |
| `current_loan_semester` | Integer |  |
| `product_package_id` | Integer |  |
| `subsequent_loan_activation_date` | Date |  |

#### `public.loans_idsyariahtuitionloan`

_Fields: 18_

| Field | Type | Description |
|---|---|---|
| `loan_ptr_id` | Integer |  |
| `privy_document_id` | Text |  |
| `privy_signing_status` | Text |  |
| `privy_document_url` | Text |  |
| `borrower_change_of_data_selfie_file` | Text |  |
| `borrower_change_of_data_selfie_file_notes` | Text |  |
| `guarantor_change_of_data_selfie_file` | Text |  |
| `guarantor_change_of_data_selfie_file_notes` | Text |  |
| `secondary_guarantor_id_file` | Text |  |
| `secondary_guarantor_id_file_notes` | Text |  |
| `secondary_guarantor_proof_of_income_file` | Text |  |
| `secondary_guarantor_proof_of_income_file_notes` | Text |  |
| `privy_document_sign_magic_link` | Text |  |
| `privy_guarantor_document_sign_magic_link` | Text |  |
| `privy_document_sign_magic_short_link` | Text |  |
| `privy_guarantor_document_sign_magic_short_link` | Text |  |
| `privy_borrower_signing_status` | Text |  |
| `privy_guarantor_signing_status` | Text |  |

#### `public.loans_idtuitionloan`

_Fields: 47_

| Field | Type | Description |
|---|---|---|
| `loan_ptr_id` | Integer |  |
| `borrower_kk` | Text |  |
| `borrower_school_bill` | Text |  |
| `academic_term_needed` | Text |  |
| `beneficiary_account_name` | Text |  |
| `beneficiary_account_number` | Text |  |
| `beneficiary_bank_name` | Text |  |
| `privy_document_id` | Text |  |
| `privy_signing_status` | Text |  |
| `privy_document_url` | Text |  |
| `lender_agreement_file` | Text |  |
| `privy_lender_agreement_document_id` | Text |  |
| `privy_lender_agreement_document_signing_status` | Text |  |
| `privy_lender_agreement_document_url` | Text |  |
| `borrower_change_of_data_selfie_file` | Text |  |
| `borrower_change_of_data_selfie_file_notes` | Text |  |
| `guarantor_change_of_data_selfie_file` | Text |  |
| `guarantor_change_of_data_selfie_file_notes` | Text |  |
| `secondary_guarantor_id_file` | Text |  |
| `secondary_guarantor_id_file_notes` | Text |  |
| `secondary_guarantor_proof_of_income_file` | Text |  |
| `secondary_guarantor_proof_of_income_file_notes` | Text |  |
| `beneficiary_account_number_revisions_needed` | Boolean |  |
| `beneficiary_account_number_revisions_notes` | Text |  |
| `beneficiary_account_number_status` | Text |  |
| `virtual_account_validity_date` | Date |  |
| `borrower_app_virtual_account_revision_needed` | Boolean |  |
| `virtual_account_borrower_notes` | Text |  |
| `privy_document_sign_magic_link` | Text |  |
| `privy_guarantor_document_sign_magic_link` | Text |  |
| `privy_document_sign_magic_short_link` | Text |  |
| `privy_guarantor_document_sign_magic_short_link` | Text |  |
| `privy_borrower_signing_status` | Text |  |
| `privy_guarantor_signing_status` | Text |  |
| `digital_signature_provider` | Text |  |
| `auto_signer_signing_status` | Text |  |
| `previous_lender_agreement_file` | Text |  |
| `datetime_statement_of_risk_awareness_signed` | DateTimeWithLocalTZ |  |
| `is_statement_of_risk_awareness_signed` | Boolean |  |
| `statement_of_risk_awareness_file` | Text |  |
| `datetime_auto_signer_signed` | DateTimeWithLocalTZ |  |
| `datetime_borrower_signed` | DateTimeWithLocalTZ |  |
| `datetime_guarantor_signed` | DateTimeWithLocalTZ |  |
| `lender_agreement_signing_error_detail` | JSON |  |
| `datetime_riplay_signed` | DateTimeWithLocalTZ |  |
| `is_riplay_signed` | Boolean |  |
| `riplay_file` | Text |  |

#### `public.loans_interaction`

_Fields: 19_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `type` | Text |  |
| `description` | Text |  |
| `loan_id` | Integer |  |
| `processor_id` | Integer |  |
| `channel` | Text |  |
| `datetime_follow_up` | DateTimeWithLocalTZ |  |
| `datetime_interacted` | DateTimeWithLocalTZ |  |
| `kind` | Text |  |
| `rating` | Integer |  |
| `rating_context` | Text |  |
| `contact_point` | Text |  |
| `full_name` | Text |  |
| `identity` | Text |  |
| `operation` | Text |  |
| `batch_id` | Integer |  |
| `collector_id` | Integer |  |
| `loan_application_id` | Integer |  |
| `collection_log_id` | Integer |  |

#### `public.loans_interactionbatch`

_Fields: 9_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `uuid` | UUID |  |
| `status` | Text |  |
| `interaction_file` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `datetime_deleted` | DateTimeWithLocalTZ |  |
| `datetime_ingested` | DateTimeWithLocalTZ |  |
| `error_file` | Text |  |

#### `public.loans_loan`

_Fields: 247_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `uuid` | UUID |  |
| `reference_code` | Text |  |
| `status` | Text |  |
| `student_id_number` | Text |  |
| `chosen_month_due_date` | Integer |  |
| `date_needed` | Date |  |
| `datetime_agreement_confirmed` | DateTimeWithLocalTZ |  |
| `general_notes` | Text |  |
| `borrower_information_notes` | Text |  |
| `rejection_notes` | Text |  |
| `past_due_bucket` | Text |  |
| `disbursed_amount` | Decimal |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `datetime_deleted` | DateTimeWithLocalTZ |  |
| `requested_principal` | Decimal |  |
| `requested_tenor` | Integer |  |
| `requested_total_origination_fee` | Decimal |  |
| `requested_total_interest_fee` | Decimal |  |
| `requested_total_transaction_fee` | Decimal |  |
| `requested_total_balance` | Decimal |  |
| `requested_total_interest_rate` | Decimal |  |
| `requested_effective_interest_rate` | Decimal |  |
| `requested_monthly_repayment` | Decimal |  |
| `requested_total_monthly_payment` | Decimal |  |
| `requested_total_principal_payment` | Decimal |  |
| `requested_total_interest_payment` | Decimal |  |
| `approved_principal` | Decimal |  |
| `approved_tenor` | Integer |  |
| `approved_total_origination_fee` | Decimal |  |
| `approved_total_interest_fee` | Decimal |  |
| `approved_total_transaction_fee` | Decimal |  |
| `approved_total_balance` | Decimal |  |
| `approved_total_interest_rate` | Decimal |  |
| `approved_effective_interest_rate` | Decimal |  |
| `approved_monthly_repayment` | Decimal |  |
| `approved_total_monthly_payment` | Decimal |  |
| `approved_total_principal_payment` | Decimal |  |
| `approved_total_interest_payment` | Decimal |  |
| `contract_file` | Text |  |
| `disclosure_statement_file` | Text |  |
| `datetime_approved` | DateTimeWithLocalTZ |  |
| `has_accepted_contract` | Boolean |  |
| `datetime_has_accepted_contract` | DateTimeWithLocalTZ |  |
| `has_accepted_one_and_the_same_clause` | Boolean |  |
| `datetime_has_accepted_one_and_the_same_clause` | DateTimeWithLocalTZ |  |
| `borrower_id` | Integer |  |
| `disbursement_id` | Integer |  |
| `partner_id` | Integer |  |
| `polymorphic_ctype_id` | Integer |  |
| `processor_id` | Integer |  |
| `product_id` | Integer |  |
| `batch_id` | Integer |  |
| `date_start` | Date |  |
| `datetime_disbursed` | DateTimeWithLocalTZ |  |
| `for_special_approval` | Boolean |  |
| `performance_score` | Integer |  |
| `approved_interest_rate` | Decimal |  |
| `requested_interest_rate` | Decimal |  |
| `approved_origination_rate` | Decimal |  |
| `requested_origination_rate` | Decimal |  |
| `approved_minimum_origination_fee` | Decimal |  |
| `approved_transaction_fee` | Decimal |  |
| `requested_minimum_origination_fee` | Decimal |  |
| `requested_transaction_fee` | Decimal |  |
| `approved_grace_period` | Integer |  |
| `requested_grace_period` | Integer |  |
| `actual_disbursed_amount` | Decimal |  |
| `approved_discount` | Decimal |  |
| `approved_discounted_principal` | Decimal |  |
| `requested_discount` | Decimal |  |
| `requested_discounted_principal` | Decimal |  |
| `partner_status` | Text |  |
| `datetime_woff_effectivity` | DateTimeWithLocalTZ |  |
| `datetime_written_off` | DateTimeWithLocalTZ |  |
| `datetime_submitted` | DateTimeWithLocalTZ |  |
| `total_exposure_value` | Decimal |  |
| `lender_id` | Integer |  |
| `has_insurance` | Boolean |  |
| `datetime_pre_terminated` | DateTimeWithLocalTZ |  |
| `borrower_course` | Text |  |
| `borrower_school_assessment_file` | Text |  |
| `borrower_school_assessment_file_status` | Text |  |
| `borrower_school_assessment_file_notes` | Text |  |
| `lender_contract_id` | Integer |  |
| `lender_total_platform_fee` | Decimal |  |
| `lender_total_return` | Decimal |  |
| `enhanced_due_diligence_email_sent` | Boolean |  |
| `is_cancelled_via_cron` | Boolean |  |
| `underwriting_confidence` | Decimal |  |
| `underwriting_decision` | Text |  |
| `underwriting_rating` | Text |  |
| `underwriting_version` | Text |  |
| `closure_certificate_file` | Text |  |
| `decision_code_id` | Integer |  |
| `outstanding_principal_balance` | Decimal |  |
| `datetime_canceled` | DateTimeWithLocalTZ |  |
| `datetime_closed` | DateTimeWithLocalTZ |  |
| `effective_past_due_bucket` | Text |  |
| `additional_borrower_id_file` | Text |  |
| `additional_borrower_id_file_notes` | Text |  |
| `additional_guarantor_id_file` | Text |  |
| `additional_guarantor_id_file_notes` | Text |  |
| `additional_guardian_id_file` | Text |  |
| `additional_guardian_id_file_notes` | Text |  |
| `additional_proof_of_income_file` | Text |  |
| `additional_proof_of_income_file_notes` | Text |  |
| `outstanding_loan_amount` | Decimal |  |
| `is_deferred_interest` | Boolean |  |
| `actual_effective_interest_rate` | Decimal |  |
| `aggregate_discount_scheduled_income` | Decimal |  |
| `most_recent_outstanding_net_principal` | Decimal |  |
| `most_recent_outstanding_revenue` | Decimal |  |
| `actual_days_past_due` | Integer |  |
| `datetime_expiration` | DateTimeWithLocalTZ |  |
| `datetime_rejected` | DateTimeWithLocalTZ |  |
| `datetime_withdrawn` | DateTimeWithLocalTZ |  |
| `is_in_eligibility_to_apply_lookup` | Boolean |  |
| `revision_funnel_duration` | Integer |  |
| `external_collection_agency_id` | Integer |  |
| `external_collection_operator_id` | Integer |  |
| `previous_external_collection_agency_id` | Integer |  |
| `underwriting_error` | Text |  |
| `overpayment` | Decimal |  |
| `cohort_id` | Integer |  |
| `previous_loan_id` | Integer |  |
| `close_code` | Text |  |
| `credit_limit` | Decimal |  |
| `for_restructuring` | Boolean |  |
| `is_restructured` | Boolean |  |
| `auto_reject_loan` | Boolean |  |
| `underwriting_verified` | Boolean |  |
| `written_off_batch_id` | Integer |  |
| `product_package_id` | Integer |  |
| `require_guardian_due_diligence` | Boolean |  |
| `student_portal_screenshot_file` | Text |  |
| `student_portal_screenshot_notes` | Text |  |
| `is_offer_link_loan` | Boolean |  |
| `has_scheduled_borrower_interview` | Boolean |  |
| `has_scheduled_with_additional_references_interview` | Boolean |  |
| `has_scheduled_with_guardian_interview` | Boolean |  |
| `has_edd_loan_revisions` | Boolean |  |
| `is_wholesale` | Boolean |  |
| `is_guarantor_phone_number_contactable` | Boolean |  |
| `is_guardian_phone_number_contactable` | Boolean |  |
| `is_user_phone_number_contactable` | Boolean |  |
| `date_priority` | Date |  |
| `approver_id` | Integer |  |
| `adjusted_npl_amount` | Decimal |  |
| `refund_amount` | Decimal |  |
| `withheld_disbursement_amount` | Decimal |  |
| `risk_share_coverage` | Decimal |  |
| `datetime_sent_last_guardian_consent_sms` | DateTimeWithLocalTZ |  |
| `edd_reference_email` | Text |  |
| `edd_reference_first_name` | Text |  |
| `edd_reference_last_name` | Text |  |
| `edd_reference_mobile_number` | Text |  |
| `edd_reference_relationship_to_student` | Text |  |
| `guardian_has_accepted_privacy_policy` | Boolean |  |
| `guardian_has_confirmed_identity` | Boolean |  |
| `valid_id_uploaded_by_guardian_file` | Text |  |
| `has_ever_been_hard_reset` | Boolean |  |
| `external_collection_agency_assignment_count` | Integer |  |
| `has_prior_activated_loan` | Boolean |  |
| `collection_activity` | Text |  |
| `datetime_field_collection_assigned` | DateTimeWithLocalTZ |  |
| `field_collection_assignment_count` | Integer |  |
| `is_partner_access_blocked` | Boolean |  |
| `partner_blocking_policy_days` | Integer |  |
| `has_exceeded_penalty_cap` | Boolean |  |
| `payment_deadline_date` | Date |  |
| `entry_point` | Text |  |
| `expiration_policy_date` | Date |  |
| `is_near_expiration_policy_date` | Boolean |  |
| `external_collection_agency_assignment_date` | Date |  |
| `internal_collection_activity` | Text |  |
| `loan_application_id` | Integer |  |
| `promise_to_pay_processor_id` | Integer |  |
| `borrower_school_assessment_file_skip_status` | Boolean |  |
| `lender_addendum_count` | Integer |  |
| `discounted_effective_interest_rate` | Decimal |  |
| `is_deleted` | Boolean |  |
| `discounted_xirr` | Decimal |  |
| `xirr` | Decimal |  |
| `underwriting_datetime_computed` | DateTimeWithLocalTZ |  |
| `datetime_sent_last_guarantor_consent_sms` | DateTimeWithLocalTZ |  |
| `guarantor_has_accepted_privacy_policy` | Boolean |  |
| `guarantor_has_confirmed_identity` | Boolean |  |
| `has_scheduled_with_guarantor_interview` | Boolean |  |
| `require_guarantor_due_diligence` | Boolean |  |
| `valid_id_uploaded_by_guarantor_file` | Text |  |
| `selfie_with_valid_id_uploaded_by_guarantor_file` | Text |  |
| `selfie_with_valid_id_uploaded_by_guardian_file` | Text |  |
| `valid_id_uploaded_by_guarantor_file_type` | Text |  |
| `valid_id_uploaded_by_guardian_file_type` | Text |  |
| `edd_borrower_has_confirmed_agreement` | Boolean |  |
| `guarantor_datetime_agreement_confirmed` | DateTimeWithLocalTZ |  |
| `guarantor_has_accepted_contract` | Boolean |  |
| `guarantor_has_accepted_one_and_the_same_clause` | Boolean |  |
| `is_disbursement_held` | Boolean |  |
| `is_npl_as_of_risk_share_cut_off` | Boolean |  |
| `datetime_refund_disbursed` | DateTimeWithLocalTZ |  |
| `refund_disbursement_id` | Integer |  |
| `date_recommendation` | Date |  |
| `is_pre_subsequent_loan` | Boolean |  |
| `date_recommendation_expiry` | Date |  |
| `date_recommendation_follow_up` | Date |  |
| `underwriting_risk_classification` | Text |  |
| `datetime_migrated` | DateTimeWithLocalTZ |  |
| `underwriting_credit_score` | Integer |  |
| `collection_notes` | Text |  |
| `is_risk_refund` | Boolean |  |
| `partner_access_blocked_datetime_start` | DateTimeWithLocalTZ |  |
| `is_include_in_blocking_access` | Boolean |  |
| `is_release_from_blocking_access` | Boolean |  |
| `early_written_off` | Boolean |  |
| `restructure_code` | Text |  |
| `borrower_school_assessment_id` | Integer |  |
| `underwriting_type` | Text |  |
| `has_ledger` | Boolean |  |
| `approved_total_origination_fee_one_time` | Decimal |  |
| `requested_total_origination_fee_one_time` | Decimal |  |
| `datetime_guarantor_signing_waived` | DateTimeWithLocalTZ |  |
| `pre_termination_date_due` | Date |  |
| `pre_termination_payable` | Decimal |  |
| `is_on_hold_for_payment` | Boolean |  |
| `mobile_number_sent_last_guarantor_consent_sms` | Text |  |
| `consecutive_on_time_repayment` | Integer |  |
| `restructure_activity` | Text |  |
| `credited_by_id` | Integer |  |
| `datetime_loan_credited` | DateTimeWithLocalTZ |  |
| `is_credited` | Boolean |  |
| `approved_grace_period_interest_rate` | Decimal |  |
| `requested_grace_period_interest_rate` | Decimal |  |
| `guardian_has_consented_to_be_contacted` | Boolean |  |
| `mobile_number_sent_last_guardian_consent_sms` | Text |  |
| `approved_buyback_principal` | Decimal |  |
| `approved_buyback_tenor` | Integer |  |
| `datetime_buyback` | DateTimeWithLocalTZ |  |
| `is_buyback` | Boolean |  |
| `previous_lender_id` | Integer |  |
| `previous_lender_contract_id` | Integer |  |
| `buyback_batch_id` | Integer |  |
| `is_repayment_reminders_disabled` | Boolean |  |
| `requested_discount_rate` | Decimal |  |
| `approved_discount_rate` | Decimal |  |

#### `public.loans_loan_lender_assignment`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `loan_id` | Integer |  |
| `lenderriskassessment_id` | Integer |  |

#### `public.loans_loanapplication`

_Fields: 273_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `underwriting_confidence` | Decimal |  |
| `underwriting_rating` | Text |  |
| `underwriting_decision` | Text |  |
| `credit_limit` | Decimal |  |
| `underwriting_version` | Text |  |
| `underwriting_error` | Text |  |
| `underwriting_verified` | Boolean |  |
| `auto_reject_loan` | Boolean |  |
| `status` | Text |  |
| `datetime_approved` | DateTimeWithLocalTZ |  |
| `datetime_submitted` | DateTimeWithLocalTZ |  |
| `datetime_rejected` | DateTimeWithLocalTZ |  |
| `datetime_canceled` | DateTimeWithLocalTZ |  |
| `guarantor_first_name` | Text |  |
| `guarantor_last_name` | Text |  |
| `guarantor_email` | Text |  |
| `guarantor_gender` | Text |  |
| `guarantor_mobile_number` | Text |  |
| `guarantor_place_of_birth` | Text |  |
| `guarantor_date_of_birth` | Date |  |
| `additional_guarantor_id_file` | Text |  |
| `additional_guarantor_id_file_notes` | Text |  |
| `guarantor_selfie_file` | Text |  |
| `guarantor_selfie_file_notes` | Text |  |
| `guarantor_selfie_file_status` | Text |  |
| `guarantor_address` | Text |  |
| `guarantor_proof_of_residence_file` | Text |  |
| `guarantor_proof_of_residence_file_notes` | Text |  |
| `guarantor_proof_of_residence_file_status` | Text |  |
| `guarantor_relationship_to_student` | Text |  |
| `guarantor_type` | Text |  |
| `guarantor_position` | Text |  |
| `guarantor_business_name` | Text |  |
| `guarantor_business_address` | Text |  |
| `guarantor_business_phone` | Text |  |
| `guarantor_job_start_date` | Date |  |
| `guarantor_tenure` | Integer |  |
| `guarantor_monthly_income` | Decimal |  |
| `guarantor_verified_monthly_income` | Decimal |  |
| `guarantor_proof_of_income_file` | Text |  |
| `guarantor_proof_of_income_file_notes` | Text |  |
| `guarantor_proof_of_income_file_status` | Text |  |
| `reference_code` | Text |  |
| `student_id_number` | Text |  |
| `borrower_course` | Text |  |
| `borrower_year_level` | Integer |  |
| `borrower_school_assessment_file` | Text |  |
| `borrower_school_assessment_file_notes` | Text |  |
| `borrower_address_line_1` | Text |  |
| `borrower_address_line_2` | Text |  |
| `borrower_degree` | Text |  |
| `borrower_level` | Integer |  |
| `borrower_program` | Text |  |
| `student_proof_of_residence_file` | Text |  |
| `student_proof_of_residence_file_notes` | Text |  |
| `student_proof_of_residence_file_status` | Text |  |
| `guardian_first_name` | Text |  |
| `guardian_last_name` | Text |  |
| `guardian_email` | Text |  |
| `guardian_mobile_number` | Text |  |
| `guardian_gender` | Text |  |
| `guardian_relationship_to_student` | Text |  |
| `reference_1_full_name` | Text |  |
| `reference_1_mobile_number` | Text |  |
| `reference_1_relationship_to_student` | Text |  |
| `reference_2_full_name` | Text |  |
| `reference_2_mobile_number` | Text |  |
| `reference_2_relationship_to_student` | Text |  |
| `general_notes` | Text |  |
| `rejection_notes` | Text |  |
| `borrower_information_notes` | Text |  |
| `date_start` | Date |  |
| `requested_principal` | Decimal |  |
| `requested_discount` | Decimal |  |
| `requested_discounted_principal` | Decimal |  |
| `requested_effective_interest_rate` | Decimal |  |
| `requested_grace_period` | Integer |  |
| `requested_interest_rate` | Decimal |  |
| `requested_monthly_repayment` | Decimal |  |
| `requested_origination_rate` | Decimal |  |
| `requested_tenor` | Integer |  |
| `requested_total_balance` | Decimal |  |
| `requested_total_interest_fee` | Decimal |  |
| `requested_total_interest_payment` | Decimal |  |
| `requested_total_interest_rate` | Decimal |  |
| `requested_total_monthly_payment` | Decimal |  |
| `requested_total_origination_fee` | Decimal |  |
| `requested_total_principal_payment` | Decimal |  |
| `approved_principal` | Decimal |  |
| `approved_discounted_principal` | Decimal |  |
| `is_deferred_interest` | Boolean |  |
| `is_cancelled_via_cron` | Boolean |  |
| `is_wholesale` | Boolean |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `approver_id` | Integer |  |
| `batch_id` | Integer |  |
| `borrower_id` | Integer |  |
| `borrower_city_id` | Integer |  |
| `borrower_province_id` | Integer |  |
| `decision_code_id` | Integer |  |
| `guarantor_city_id` | Integer |  |
| `guarantor_industry_id` | Integer |  |
| `guarantor_province_id` | Integer |  |
| `guardian_city_id` | Integer |  |
| `guardian_province_id` | Integer |  |
| `partner_id` | Integer |  |
| `polymorphic_ctype_id` | Integer |  |
| `processor_id` | Integer |  |
| `product_id` | Integer |  |
| `additional_borrower_id_file` | Text |  |
| `additional_borrower_id_file_notes` | Text |  |
| `additional_guardian_id_file` | Text |  |
| `additional_guardian_id_file_notes` | Text |  |
| `additional_proof_of_income_file` | Text |  |
| `additional_proof_of_income_file_notes` | Text |  |
| `borrower_school_assessment_file_status` | Text |  |
| `datetime_sent_last_guardian_consent_sms` | DateTimeWithLocalTZ |  |
| `edd_reference_email` | Text |  |
| `edd_reference_first_name` | Text |  |
| `edd_reference_last_name` | Text |  |
| `edd_reference_mobile_number` | Text |  |
| `edd_reference_relationship_to_student` | Text |  |
| `guardian_has_accepted_privacy_policy` | Boolean |  |
| `guardian_has_confirmed_identity` | Boolean |  |
| `has_edd_loan_revisions` | Boolean |  |
| `has_scheduled_borrower_interview` | Boolean |  |
| `has_scheduled_with_additional_references_interview` | Boolean |  |
| `has_scheduled_with_guardian_interview` | Boolean |  |
| `require_guardian_due_diligence` | Boolean |  |
| `revision_funnel_duration` | Integer |  |
| `selfie_file` | Text |  |
| `selfie_file_notes` | Text |  |
| `selfie_file_status` | Text |  |
| `student_portal_screenshot_file` | Text |  |
| `student_portal_screenshot_notes` | Text |  |
| `valid_id_uploaded_by_guardian_file` | Text |  |
| `enhanced_due_diligence_email_sent` | Boolean |  |
| `is_in_eligibility_to_apply_lookup` | Boolean |  |
| `requested_minimum_origination_fee` | Decimal |  |
| `previous_loan_id` | Integer |  |
| `entry_point` | Text |  |
| `requested_transaction_fee` | Decimal |  |
| `borrower_gender` | Text |  |
| `borrower_date_of_birth` | Date |  |
| `borrower_nearest_landmark` | Text |  |
| `borrower_place_of_birth` | Text |  |
| `approved_discount` | Decimal |  |
| `approved_effective_interest_rate` | Decimal |  |
| `approved_grace_period` | Integer |  |
| `approved_interest_rate` | Decimal |  |
| `approved_minimum_origination_fee` | Decimal |  |
| `approved_monthly_repayment` | Decimal |  |
| `approved_origination_rate` | Decimal |  |
| `approved_tenor` | Integer |  |
| `approved_total_balance` | Decimal |  |
| `approved_total_interest_fee` | Decimal |  |
| `approved_total_interest_payment` | Decimal |  |
| `approved_total_interest_rate` | Decimal |  |
| `approved_total_monthly_payment` | Decimal |  |
| `approved_total_origination_fee` | Decimal |  |
| `approved_total_principal_payment` | Decimal |  |
| `approved_transaction_fee` | Decimal |  |
| `deviant_fields` | Text |  |
| `datetime_deleted` | DateTimeWithLocalTZ |  |
| `is_deleted` | Boolean |  |
| `date_priority` | Date |  |
| `payment_deadline_date` | Date |  |
| `uuid` | UUID |  |
| `underwriting_datetime_computed` | DateTimeWithLocalTZ |  |
| `datetime_sent_last_guarantor_consent_sms` | DateTimeWithLocalTZ |  |
| `guarantor_has_accepted_privacy_policy` | Boolean |  |
| `guarantor_has_confirmed_identity` | Boolean |  |
| `has_scheduled_with_guarantor_interview` | Boolean |  |
| `require_guarantor_due_diligence` | Boolean |  |
| `valid_id_uploaded_by_guarantor_file` | Text |  |
| `has_prior_activated_loan` | Boolean |  |
| `selfie_with_valid_id_uploaded_by_guarantor_file` | Text |  |
| `selfie_with_valid_id_uploaded_by_guardian_file` | Text |  |
| `valid_id_uploaded_by_guarantor_file_type` | Text |  |
| `valid_id_uploaded_by_guardian_file_type` | Text |  |
| `edd_borrower_has_confirmed_agreement` | Boolean |  |
| `guarantor_datetime_agreement_confirmed` | DateTimeWithLocalTZ |  |
| `guarantor_has_accepted_contract` | Boolean |  |
| `guarantor_has_accepted_one_and_the_same_clause` | Boolean |  |
| `guarantor_proof_of_income_file_skip_status` | Boolean |  |
| `guarantor_selfie_file_skip_status` | Boolean |  |
| `selfie_file_skip_status` | Boolean |  |
| `borrower_school_assessment_file_skip_status` | Boolean |  |
| `is_employed` | Boolean |  |
| `guarantor_number_of_dependents` | Integer |  |
| `disbursement_type_class` | Text |  |
| `platform_entry_point` | Text |  |
| `emergency_contact_step_skip_status` | Boolean |  |
| `datetime_migrated` | DateTimeWithLocalTZ |  |
| `is_guarantor_phone_number_contactable` | Boolean |  |
| `is_guardian_phone_number_contactable` | Boolean |  |
| `is_user_phone_number_contactable` | Boolean |  |
| `is_k_12_application` | Boolean |  |
| `requested_product_id` | Integer |  |
| `verification_level_1_status` | Text |  |
| `verification_level_2_status` | Text |  |
| `verification_level_3_status` | Text |  |
| `underwriting_risk_classification` | Text |  |
| `student_email` | Text |  |
| `is_cancelled_for_edits` | Boolean |  |
| `underwriting_credit_score` | Integer |  |
| `borrower_home_address_json` | JSON |  |
| `borrower_home_address_details` | Text |  |
| `borrower_home_geolocation` | Text |  |
| `borrower_home_map_landmark` | Text |  |
| `borrower_home_pinned_address` | Text |  |
| `borrower_work_address_details` | Text |  |
| `borrower_work_address_json` | JSON |  |
| `borrower_work_geolocation` | Text |  |
| `borrower_work_map_landmark` | Text |  |
| `borrower_work_pinned_address` | Text |  |
| `coborrower_home_address_details` | Text |  |
| `coborrower_home_address_json` | JSON |  |
| `coborrower_home_geolocation` | Text |  |
| `coborrower_home_map_landmark` | Text |  |
| `coborrower_home_pinned_address` | Text |  |
| `coborrower_work_address_details` | Text |  |
| `coborrower_work_address_json` | JSON |  |
| `coborrower_work_geolocation` | Text |  |
| `coborrower_work_map_landmark` | Text |  |
| `coborrower_work_pinned_address` | Text |  |
| `is_pre_approval_flow` | Boolean |  |
| `failed_verification_notes` | Text |  |
| `additional_information` | Text |  |
| `is_gadget_loan_application` | Boolean |  |
| `borrower_nationality` | Text |  |
| `guarantor_nationality` | Text |  |
| `primary_income_provider` | Text |  |
| `borrower_business_address` | Text |  |
| `borrower_business_name` | Text |  |
| `borrower_business_phone` | Text |  |
| `borrower_industry_id` | Integer |  |
| `borrower_job_start_date` | Date |  |
| `borrower_monthly_income` | Decimal |  |
| `borrower_position` | Text |  |
| `borrower_proof_of_income_file` | Text |  |
| `borrower_tenure` | Integer |  |
| `borrower_verified_monthly_income` | Decimal |  |
| `borrower_proof_of_income_file_skip_status` | Boolean |  |
| `is_eligible_for_pre_approval` | Boolean |  |
| `cancellation_notes` | Text |  |
| `alt_flow_guarantor_consent_used` | Boolean |  |
| `alt_flow_guarantor_signing_used` | Boolean |  |
| `is_on_demand_application` | Boolean |  |
| `borrower_proof_of_income_id` | Integer |  |
| `borrower_school_assessment_id` | Integer |  |
| `guarantor_proof_of_income_id` | Integer |  |
| `underwriting_type` | Text |  |
| `is_cash_loan_application` | Boolean |  |
| `approved_total_origination_fee_one_time` | Decimal |  |
| `requested_total_origination_fee_one_time` | Decimal |  |
| `datetime_guarantor_edd_waived` | DateTimeWithLocalTZ |  |
| `alt_flow_guardian_consent_used` | Boolean |  |
| `is_b2c_application` | Boolean |  |
| `guarantor_nickname` | Text |  |
| `mobile_number_sent_last_guarantor_consent_sms` | Text |  |
| `guarantor_relationship_to_student_other_data` | Text |  |
| `approved_grace_period_interest_rate` | Decimal |  |
| `requested_grace_period_interest_rate` | Decimal |  |
| `guardian_has_consented_to_be_contacted` | Boolean |  |
| `mobile_number_sent_last_guardian_consent_sms` | Text |  |
| `is_employee_cash_loan_application` | Boolean |  |
| `is_invoice_financing_application` | Boolean |  |
| `requested_discount_rate` | Decimal |  |
| `approved_discount_rate` | Decimal |  |
| `is_b2c_cash_loan_application` | Boolean |  |

#### `public.loans_loanproduct`

_Fields: 55_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `name` | Text |  |
| `interest_rate` | Decimal |  |
| `origination_rate` | Decimal |  |
| `origination_fee` | Decimal |  |
| `transaction_rate` | Decimal |  |
| `transaction_fee` | Decimal |  |
| `penalty_rate` | Decimal |  |
| `penalty_fee` | Decimal |  |
| `type` | Text |  |
| `valid_start_date` | Date |  |
| `valid_end_date` | Date |  |
| `sign_off_page_content` | Text |  |
| `confirmation_page_content` | Text |  |
| `disburse_to_id` | Integer |  |
| `minimum_origination_fee` | Decimal |  |
| `product_group_id` | Integer |  |
| `tenor` | Integer |  |
| `grace_period` | Integer |  |
| `discount_rate` | Decimal |  |
| `is_deferred_interest` | Boolean |  |
| `is_in_eligibility_to_apply_lookup` | Boolean |  |
| `has_insurance_fee` | Boolean |  |
| `allowed_risk_tier` | Text |  |
| `is_expedited` | Boolean |  |
| `is_wholesale` | Boolean |  |
| `activation_date` | Date |  |
| `penalty_total_cap_rate` | Decimal |  |
| `exclude_from_recent_canceled_loan_lookup` | Boolean |  |
| `group_in_cohorts_upon_activation` | Boolean |  |
| `is_only_for_offerlink` | Boolean |  |
| `allowed_school_terms` | Text |  |
| `cohort_assignment` | Text |  |
| `user_existence_type` | Text |  |
| `is_template` | Boolean |  |
| `is_recommended` | Boolean |  |
| `is_recommended_for_quotation` | Boolean |  |
| `allowed_year_level` | Text |  |
| `recommended_loan_start_date` | Date |  |
| `disbursement_type_class` | Text |  |
| `is_auto_top_up_approval` | Boolean |  |
| `internal_name` | Text |  |
| `is_risk_sharing` | Boolean |  |
| `blocking_policy_start_date` | Date |  |
| `has_blocking_policy` | Boolean |  |
| `require_guarantor` | Boolean |  |
| `disbursement_timeline` | Text |  |
| `is_non_segment` | Boolean |  |
| `allowed_primary_income_provider` | Text |  |
| `risk_sharing_dpd_threshold` | Integer |  |
| `origination_config` | Text |  |
| `preterm_penalty_rate` | Decimal |  |
| `grace_period_interest_rate` | Decimal |  |
| `generate_fixed_va_required` | Boolean |  |
| `preterm_penalty_effective_date` | Date |  |

#### `public.loans_loanproduct_applicable_partners`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `loanproduct_id` | Integer |  |
| `partner_id` | Integer |  |

#### `public.loans_loanproductgroup`

_Fields: 8_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `name` | Text |  |
| `type` | Text |  |
| `description` | Text |  |
| `is_for_new_students` | Boolean |  |
| `is_gadget_product_group` | Boolean |  |
| `total_gadget_cost` | Decimal |  |
| `degree` | Text |  |

#### `public.loans_loanproductpackage`

_Fields: 6_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `name` | Text |  |
| `valid_start_date` | Date |  |
| `valid_end_date` | Date |  |
| `product_group_id` | Integer |  |
| `is_tranche_disbursement` | Boolean |  |

#### `public.loans_loanproductpackage_applicable_partners`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `loanproductpackage_id` | Integer |  |
| `partner_id` | Integer |  |

#### `public.loans_loanproductplatformconfig`

_Fields: 5_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `is_require_school_assessment_file` | Boolean |  |
| `platform` | Text |  |
| `product_id` | Integer |  |
| `is_listed` | Boolean |  |

#### `public.loans_loanproducttemplate`

_Fields: 2_

| Field | Type | Description |
|---|---|---|
| `loanproduct_ptr_id` | Integer |  |
| `readonly_fields` | Text |  |

#### `public.loans_multiproductconfig`

_Fields: 5_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `semester_number` | Integer |  |
| `agreement_signing_date` | Date |  |
| `product_id` | Integer |  |
| `product_package_id` | Integer |  |

#### `public.loans_multisemesterconfig`

_Fields: 5_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `requested_principal` | Decimal |  |
| `semester_number` | Integer |  |
| `loan_id` | Integer |  |
| `loan_application_id` | Integer |  |

#### `public.loans_offlineapplicationbatch`

_Fields: 7_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `uuid` | UUID |  |
| `status` | Text |  |
| `batch_file` | Text |  |
| `error_file` | Text |  |

#### `public.loans_ondemandapplicationbatch`

_Fields: 10_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `uuid` | UUID |  |
| `batch_file` | Text |  |
| `error_file` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `datetime_deleted` | DateTimeWithLocalTZ |  |
| `datetime_ingested` | DateTimeWithLocalTZ |  |
| `status` | Text |  |
| `partner_id` | Integer |  |

#### `public.loans_otherdocument`

_Fields: 7_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `name` | Text |  |
| `file` | Text |  |
| `loan_id` | Integer |  |
| `loan_application_id` | Integer |  |
| `metadata` | JSON |  |
| `simplifi_entry_id` | Integer |  |

#### `public.loans_phinternshiploan`

_Fields: 11_

| Field | Type | Description |
|---|---|---|
| `loan_ptr_id` | Integer |  |
| `itinerary_file` | Text |  |
| `internship_agency_id` | Integer |  |
| `internship_type` | Text |  |
| `itinerary_file_notes` | Text |  |
| `itinerary_file_status` | Text |  |
| `school_authorization` | Text |  |
| `school_authorization_notes` | Text |  |
| `school_authorization_status` | Text |  |
| `proof_of_down_payment_file` | Text |  |
| `proof_of_down_payment_file_notes` | Text |  |

#### `public.loans_phloanapplication`

_Fields: 56_

| Field | Type | Description |
|---|---|---|
| `loanapplication_ptr_id` | Integer |  |
| `academic_term_needed` | Text |  |
| `purpose` | Text |  |
| `segment` | Text |  |
| `student_proof_of_residence_file_type` | Text |  |
| `marital_status` | Text |  |
| `barangay` | Text |  |
| `borrower_school_id_file` | Text |  |
| `borrower_selfie_file` | Text |  |
| `borrower_selfie_file_notes` | Text |  |
| `borrower_selfie_file_status` | Text |  |
| `dorm_address` | Text |  |
| `student_mobile_number` | Text |  |
| `general_course` | Text |  |
| `valid_id_file` | Text |  |
| `valid_id_file_type` | Text |  |
| `proof_of_down_payment_file` | Text |  |
| `proof_of_down_payment_file_notes` | Text |  |
| `guardian_valid_id_file` | Text |  |
| `guardian_address_line` | Text |  |
| `guardian_marital_status` | Text |  |
| `guarantor_source_of_income` | Text |  |
| `guarantor_tin_number` | Text |  |
| `guarantor_sss_number` | Text |  |
| `guarantor_proof_of_income_file_type` | Text |  |
| `additional_proof_of_income_file_type` | Text |  |
| `guarantor_proof_of_residence_file_type` | Text |  |
| `identity` | Text |  |
| `report_card_file` | Text |  |
| `valid_id_file_status` | Text |  |
| `borrower_proof_of_income_file_type` | Text |  |
| `borrower_sss_number` | Text |  |
| `borrower_tin_number` | Text |  |
| `borrower_source_of_income` | Text |  |
| `borrower_identity` | Text |  |
| `is_student_legal_age` | Boolean |  |
| `borrower_name_of_remitter` | Text |  |
| `guarantor_address_line_1` | Text |  |
| `guarantor_address_line_2` | Text |  |
| `guarantor_name_of_remitter` | Text |  |
| `guarantor_nearest_landmark` | Text |  |
| `guarantor_relationship_to_borrower` | Text |  |
| `is_guarantor_address_same_as_borrower` | Boolean |  |
| `borrower_relationship_to_student` | Text |  |
| `guarantor_marital_status` | Text |  |
| `borrower_and_coborrower_information_notes` | Text |  |
| `borrower_id_and_liveness_notes` | Text |  |
| `income_details_information_notes` | Text |  |
| `remitter_relationship_with_borrower` | Text |  |
| `remitter_relationship_with_guarantor` | Text |  |
| `is_borrower_pep` | Boolean |  |
| `is_borrower_related_to_pep` | Boolean |  |
| `is_guarantor_pep` | Boolean |  |
| `is_guarantor_related_to_pep` | Boolean |  |
| `valid_id_number` | Text |  |
| `address_detail_notes` | Text |  |

#### `public.loans_phtuitionloan`

_Fields: 10_

| Field | Type | Description |
|---|---|---|
| `loan_ptr_id` | Integer |  |
| `academic_term_needed` | Text |  |
| `purpose` | Text |  |
| `borrower_selfie_file` | Text |  |
| `borrower_selfie_file_notes` | Text |  |
| `borrower_selfie_file_status` | Text |  |
| `borrower_school_id_file` | Text |  |
| `proof_of_down_payment_file` | Text |  |
| `proof_of_down_payment_file_notes` | Text |  |
| `additional_proof_of_income_file_type` | Text |  |

#### `public.loans_proofofincome`

_Fields: 4_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `file_count` | Integer |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `user_id` | Integer |  |

#### `public.loans_proofofincomefile`

_Fields: 5_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `order` | Integer |  |
| `file` | Text |  |
| `uploaded_at` | DateTimeWithLocalTZ |  |
| `proof_of_income_id` | Integer |  |

#### `public.loans_simplifientry`

_Fields: 7_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `uuid` | UUID |  |
| `requested_tenor` | Integer |  |
| `loan_application_id` | Integer |  |
| `partner_id` | Integer |  |
| `user_id` | Integer |  |
| `encoder_id` | Integer |  |

#### `public.loans_slikidebcreditdata`

_Fields: 5_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `credit_data` | JSON |  |
| `slik_ideb_id` | Integer |  |

#### `public.loans_slikidebupload`

_Fields: 6_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `file` | Text |  |
| `identity` | Text |  |
| `loan_application_id` | Integer |  |

#### `public.loans_sofaofflineapplicationpdf`

_Fields: 4_

| Field | Type | Description |
|---|---|---|
| `id` | UUID |  |
| `file` | Text |  |
| `installment_amount` | Decimal |  |
| `ocr_data` | JSON |  |

#### `public.loans_studentschoolassessment`

_Fields: 4_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `file_count` | Integer |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `user_id` | Integer |  |

#### `public.loans_studentschoolassessmentfile`

_Fields: 5_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `order` | Integer |  |
| `file` | Text |  |
| `uploaded_at` | DateTimeWithLocalTZ |  |
| `student_school_assessment_id` | Integer |  |

#### `public.loans_summarizerconfig`

_Fields: 7_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `name` | Text |  |
| `for_ftl` | Boolean |  |
| `for_mip` | Boolean |  |
| `enabled` | Boolean |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |

#### `public.loans_summarizerfield`

_Fields: 2_

| Field | Type | Description |
|---|---|---|
| `value` | Text |  |
| `label` | Text |  |

#### `public.loans_summarizeritem`

_Fields: 11_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `title` | Text |  |
| `help_text` | Text |  |
| `operator` | Text |  |
| `value` | Text |  |
| `value_type` | Text |  |
| `true_score` | Integer |  |
| `false_score` | Integer |  |
| `display_field_value` | Boolean |  |
| `config_id` | Integer |  |
| `field_id` | Text |  |

#### `public.loans_summary`

_Fields: 10_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `positives` | JSON |  |
| `total_positives` | Integer |  |
| `negatives` | JSON |  |
| `total_negatives` | Integer |  |
| `neutrals` | JSON |  |
| `datetime_generated` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `config_id` | Integer |  |
| `loan_app_id` | Integer |  |

#### `public.loans_tranchedisbursement`

_Fields: 18_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `uuid` | UUID |  |
| `status` | Text |  |
| `period` | Integer |  |
| `percentage` | Decimal |  |
| `npl_percentage_cap` | Decimal |  |
| `discount_percentage` | Decimal |  |
| `amount` | Decimal |  |
| `discount_amount` | Decimal |  |
| `final_amount` | Decimal |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_disbursed` | DateTimeWithLocalTZ |  |
| `cohort_id` | Integer |  |
| `update_periodically` | Boolean |  |
| `cut_off_date` | Date |  |
| `bank_reference_code` | Text |  |
| `expected_disbursement_date` | Date |  |
| `refund_amount` | Decimal |  |

#### `public.loans_virtualaccount`

_Fields: 18_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `date_of_expiry` | Date |  |
| `borrower_notes` | Text |  |
| `bank_name` | Text |  |
| `account_number` | Text |  |
| `amount_billed` | Decimal |  |
| `account_number_status` | Text |  |
| `borrower_app_revisions_needed` | Boolean |  |
| `partner_dashboard_revisions_needed` | Boolean |  |
| `revisions_notes` | Text |  |
| `loan_id` | Integer |  |
| `uuid` | UUID |  |
| `title` | Text |  |
| `partner_bank_id` | Integer |  |
| `account_name` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `loan_application_id` | Integer |  |

#### `public.loans_virtualaccountbatch`

_Fields: 7_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `uuid` | UUID |  |
| `status` | Text |  |
| `batch_file` | Text |  |
| `error_file` | Text |  |

#### `public.loans_writtenoffloanbatch`

_Fields: 10_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `uuid` | UUID |  |
| `batch_file` | Text |  |
| `error_file` | Text |  |
| `status` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `datetime_deleted` | DateTimeWithLocalTZ |  |
| `datetime_processed` | DateTimeWithLocalTZ |  |
| `datetime_ingested` | DateTimeWithLocalTZ |  |


### `logs_*`

#### `public.logs_callbacklog`

_Fields: 32_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `request_body → data → docTitle` | Text |  |
| `request_body → data → docToken` | Text |  |
| `request_body → data → documentStatus` | Text |  |
| `request_body → data → download → expiredAt` | DateTime |  |
| `request_body → data → download → url` | Text |  |
| `request_body → data → email` | Text |  |
| `request_body → data → envelope_id` | Text |  |
| `request_body → data → identity → nama` | Text |  |
| `request_body → data → identity → nik` | Text |  |
| `request_body → data → identity → tanggalLahir` | Text |  |
| `request_body → data → identity → tempatLahir` | Text |  |
| `request_body → data → phone` | Text |  |
| `request_body → data → privyId` | Text |  |
| `request_body → data → processedAt` | Text |  |
| `request_body → data → recipient_email` | Text |  |
| `request_body → data → recipients` | Array |  |
| `request_body → data → reject → code` | Text |  |
| `request_body → data → reject → handlers` | Array |  |
| `request_body → data → reject → reason` | Text |  |
| `request_body → data → status` | Text |  |
| `request_body → data → update_at` | DateTime |  |
| `request_body → data → userToken` | Text |  |
| `request_body → eventName` | Text |  |
| `request_body → event_type` | Text |  |
| `request_body → message` | Text |  |
| `request_body → urlReregister` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `url` | Text |  |
| `request_body` | JSON |  |
| `vendor` | Text |  |

#### `public.logs_otprequestlog`

_Fields: 10_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `mobile_number` | Text |  |
| `otp_channel` | Text |  |
| `otp_code` | Text |  |
| `ip_address` | IPAddress |  |
| `user_agent` | Text |  |
| `request_endpoint` | Text |  |
| `user_id` | Integer |  |

#### `public.logs_requestlog`

_Fields: 110_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `request_body → creator_email` | Text |  |
| `request_body → envelope_details` | Text |  |
| `request_body → identity` | Text |  |
| `request_body → language → code` | Text |  |
| `request_body → owner` | Text |  |
| `request_body → parameters → buttons` | Array |  |
| `request_body → templateId` | Text |  |
| `request_body → to_name` | Text |  |
| `request_body → to_number` | Text |  |
| `response_body → card → country` | Text |  |
| `response_body → card → isoAlpha2CountryCode` | Text |  |
| `response_body → card → type` | Text |  |
| `response_body → data → assessmentResults` | Array |  |
| `response_body → data → authenticationLevel` | Text |  |
| `response_body → data → certificate → detail` | Text |  |
| `response_body → data → certificate → level` | Integer |  |
| `response_body → data → channel_account_name` | Text |  |
| `response_body → data → channel_phone_number` | Text |  |
| `response_body → data → contact_id` | Text |  |
| `response_body → data → docToken` | Text |  |
| `response_body → data → email` | Text |  |
| `response_body → data → emeterai_balance_refund_status` | Text |  |
| `response_body → data → envelope_id` | Text |  |
| `response_body → data → envelope_status` | Text |  |
| `response_body → data → fraudAssessment` | Text |  |
| `response_body → data → message_status_count → delivered` | Integer |  |
| `response_body → data → message_status_count → failed` | Integer |  |
| `response_body → data → message_status_count → pending` | Integer |  |
| `response_body → data → message_status_count → sent` | Integer |  |
| `response_body → data → message_template → body` | Text |  |
| `response_body → data → message_template → external_id` | Text |  |
| `response_body → data → message_template → id` | Text |  |
| `response_body → data → message_template → is_request_phone_number` | Boolean |  |
| `response_body → data → message_template → language` | Text |  |
| `response_body → data → message_template → name` | Text |  |
| `response_body → data → message_template → need_review` | Boolean |  |
| `response_body → data → message_template → organization_id` | Text |  |
| `response_body → data → message_template → quality_rating_text` | Text |  |
| `response_body → data → message_template → status` | Text |  |
| `response_body → data → message_template → type` | Text |  |
| `response_body → data → message_template → waba_id` | Text |  |
| `response_body → data → organization_id` | Text |  |
| `response_body → data → parameters → body → 1` | Text |  |
| `response_body → data → parameters → buttons → 0 → value` | Text |  |
| `response_body → data → send_at` | DateTime |  |
| `response_body → data → sender_email` | Text |  |
| `response_body → data → sender_name` | Text |  |
| `response_body → data → status` | Text |  |
| `response_body → data → target_channel` | Text |  |
| `response_body → data → transactionId` | Text |  |
| `response_body → data → transactionType` | Text |  |
| `response_body → data → urlDocument` | Text |  |
| `response_body → data → userToken` | Text |  |
| `response_body → groupId` | Text |  |
| `response_body → imageQualityResult → blurriness → score` | Number |  |
| `response_body → imageQualityResult → cardDimension → card_height` | Integer |  |
| `response_body → imageQualityResult → cardDimension → card_width` | Integer |  |
| `response_body → imageQualityResult → lowLight → score` | Float |  |
| `response_body → imageQualityResult → lowLight → threshold` | Float |  |
| `response_body → imageQualityResult → overExposure → threshold` | Float |  |
| `response_body → message` | Text |  |
| `response_body → ocrResult → data → address → score` | Float |  |
| `response_body → ocrResult → data → address → threshold` | Float |  |
| `response_body → ocrResult → data → address → value` | Text |  |
| `response_body → ocrResult → data → bloodType → score` | Number |  |
| `response_body → ocrResult → data → bloodType → threshold` | Float |  |
| `response_body → ocrResult → data → bloodType → value` | Text |  |
| `response_body → ocrResult → data → city → threshold` | Float |  |
| `response_body → ocrResult → data → dob → threshold` | Float |  |
| `response_body → ocrResult → data → dob → value` | Text |  |
| `response_body → ocrResult → data → gender → score` | Number |  |
| `response_body → ocrResult → data → gender → threshold` | Float |  |
| `response_body → ocrResult → data → gender → value` | Text |  |
| `response_body → ocrResult → data → idNumber → threshold` | Float |  |
| `response_body → ocrResult → data → idNumber → value` | Text |  |
| `response_body → ocrResult → data → maritalStatus → score` | Number |  |
| `response_body → ocrResult → data → maritalStatus → threshold` | Float |  |
| `response_body → ocrResult → data → name → score` | Float |  |
| `response_body → ocrResult → data → name → threshold` | Float |  |
| `response_body → ocrResult → data → name → value` | Text |  |
| `response_body → ocrResult → data → nationality → threshold` | Float |  |
| `response_body → ocrResult → data → neighborhoodAssociationGroup → value` | Text |  |
| `response_body → ocrResult → data → occupation → score` | Float |  |
| `response_body → ocrResult → data → occupation → threshold` | Float |  |
| `response_body → ocrResult → data → occupation → value` | Text |  |
| `response_body → ocrResult → data → placeOfBirth → score` | Float |  |
| `response_body → ocrResult → data → placeOfBirth → threshold` | Float |  |
| `response_body → ocrResult → data → placeOfBirth → value` | Text |  |
| `response_body → ocrResult → data → province → score` | Float |  |
| `response_body → ocrResult → data → province → threshold` | Float |  |
| `response_body → ocrResult → data → religion → value` | Text |  |
| `response_body → ocrResult → data → subDistrict → score` | Float |  |
| `response_body → ocrResult → data → subDistrict → threshold` | Float |  |
| `response_body → ocrResult → data → validUntil → score` | Number |  |
| `response_body → ocrResult → data → validUntil → value` | Text |  |
| `response_body → ocrResult → data → village → score` | Float |  |
| `response_body → ocrResult → data → village → value` | Text |  |
| `response_body → status` | Text |  |
| `response_body → transactionId` | Text |  |
| `response_body → warnings` | Array |  |
| `vendor` | Text |  |
| `service_name` | Text |  |
| `timestamp` | DateTimeWithLocalTZ |  |
| `request_body` | JSON |  |
| `response_body` | JSON |  |
| `message_id` | Text |  |
| `status` | Text |  |
| `loan_app_id` | Integer |  |
| `user_id` | Integer |  |

#### `public.logs_webhooknotification`

_Fields: 25_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `request_data → amount` | Text |  |
| `request_data → date_submitted` | Text |  |
| `request_data → datetime_notification_sent` | DateTime |  |
| `request_data → product_interest_rate` | Text |  |
| `request_data → product_name` | Text |  |
| `request_data → product_origination_fee` | Text |  |
| `request_data → product_tenor` | Integer |  |
| `request_data → reference_code` | Text |  |
| `request_data → signature` | Text |  |
| `request_data → status` | Text |  |
| `request_data → student_id_number` | Text |  |
| `request_data → transaction_id` | Text |  |
| `response_data → code` | Integer |  |
| `response_data → error` | Text |  |
| `response_data → message` | Text |  |
| `response_data → messages` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `url` | Text |  |
| `request_data` | JSON |  |
| `response_status` | Integer |  |
| `response_data` | JSON |  |
| `is_successful` | Boolean |  |
| `is_json` | Boolean |  |


### `midtrans_*`

#### `public.midtrans_midtranspaymentshortlink`

_Fields: 11_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `loan_reference_code` | Text |  |
| `payment_channel` | Text |  |
| `amount_type` | Text |  |
| `custom_amount` | Decimal |  |
| `payment_amount` | Decimal |  |
| `original_url` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `midtrans_collection_id` | Integer |  |
| `payment_id` | BigInteger |  |


### `notifications_*`

#### `public.notifications_broadcastchannel`

_Fields: 6_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `name` | Text |  |
| `type` | Text |  |
| `target` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |

#### `public.notifications_broadcastnotification`

_Fields: 14_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `level` | Integer |  |
| `type` | Text |  |
| `template` | Text |  |
| `title` | Text |  |
| `short_description` | Text |  |
| `long_description` | Text |  |
| `cta_title` | Text |  |
| `cta_url` | Text |  |
| `target_receiver` | Integer |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `datetime_scheduled` | DateTimeWithLocalTZ |  |
| `datetime_executed` | DateTimeWithLocalTZ |  |

#### `public.notifications_devicetoken`

_Fields: 4_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `token` | Text |  |
| `active` | Boolean |  |
| `user_id` | Integer |  |

#### `public.notifications_notification`

_Fields: 42_

| Field | Type | Description |
|---|---|---|
| `context → approved_principal` | Text |  |
| `context → approved_tenor` | Integer |  |
| `context → borrower_first_name` | Text |  |
| `context → borrower_last_name` | Text |  |
| `context → borrower_mobile_number` | Text |  |
| `context → create_password_url` | Text |  |
| `context → current_due_total` | Text |  |
| `context → date_due` | Text |  |
| `context → day_due` | Text |  |
| `context → due_total` | Text |  |
| `context → expanded_date_due` | Text |  |
| `context → expanded_reference_code` | Text |  |
| `context → expired_date` | Text |  |
| `context → guarantor_consent_url` | Text |  |
| `context → guarantor_first_name` | Text |  |
| `context → guarantor_mobile_number` | Text |  |
| `context → guarantor_signing_url` | Text |  |
| `context → guardian_consent_url` | Text |  |
| `context → guardian_first_name` | Text |  |
| `context → guardian_mobile_number` | Text |  |
| `context → id` | Integer |  |
| `context → month` | Text |  |
| `context → partner_name` | Text |  |
| `context → password_setup_link` | Text |  |
| `context → product_name` | Text |  |
| `context → reference_code` | Text |  |
| `context → requested_principal` | Text |  |
| `context → scheduled_total` | Text |  |
| `context → uuid` | Text |  |
| `id` | Integer |  |
| `uuid` | UUID |  |
| `status` | Text |  |
| `sender` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_read` | DateTimeWithLocalTZ |  |
| `receiver_id` | Integer |  |
| `datetime_sent` | DateTimeWithLocalTZ |  |
| `template` | Text |  |
| `context` | JSON |  |
| `level` | Integer |  |
| `type` | Text |  |
| `broadcast_id` | Integer |  |

#### `public.notifications_smslog`

_Fields: 9_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `uuid` | UUID |  |
| `template` | Text |  |
| `message` | Text |  |
| `api_response` | Text |  |
| `sender` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_sent` | DateTimeWithLocalTZ |  |
| `receiver_id` | Integer |  |

#### `public.notifications_smsnotificationtemplate`

_Fields: 6_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `content` | Text |  |
| `template` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `title` | Text |  |
| `recipients` | Text |  |

#### `public.notifications_statusbroadcastconfig`

_Fields: 8_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `event_source` | Text |  |
| `target_status` | Text |  |
| `template` | Text |  |
| `enabled` | Boolean |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `channel_id` | Integer |  |

#### `public.notifications_whatsappcampaign`

_Fields: 47_

| Field | Type | Description |
|---|---|---|
| `api_response → data → channel_account_name` | Text |  |
| `api_response → data → channel_integration_id` | Text |  |
| `api_response → data → channel_phone_number` | Text |  |
| `api_response → data → contact_list_id` | Text |  |
| `api_response → data → created_at` | DateTime |  |
| `api_response → data → execute_status` | Text |  |
| `api_response → data → execute_type` | Text |  |
| `api_response → data → id` | Text |  |
| `api_response → data → message_broadcast_error` | Text |  |
| `api_response → data → message_status_count → delivered` | Integer |  |
| `api_response → data → message_status_count → failed` | Integer |  |
| `api_response → data → message_status_count → pending` | Integer |  |
| `api_response → data → message_status_count → read` | Integer |  |
| `api_response → data → message_status_count → sent` | Integer |  |
| `api_response → data → message_template → body` | Text |  |
| `api_response → data → message_template → buttons` | Array |  |
| `api_response → data → message_template → category` | Text |  |
| `api_response → data → message_template → header → example` | Text |  |
| `api_response → data → message_template → header → format` | Text |  |
| `api_response → data → message_template → id` | Text |  |
| `api_response → data → message_template → language` | Text |  |
| `api_response → data → message_template → name` | Text |  |
| `api_response → data → message_template → organization_id` | Text |  |
| `api_response → data → message_template → quality_rating_text` | Text |  |
| `api_response → data → message_template → status` | Text |  |
| `api_response → data → name` | Text |  |
| `api_response → data → organization_id` | Text |  |
| `api_response → data → parameters → body → 1` | Text |  |
| `api_response → data → parameters → body → 2` | Text |  |
| `api_response → data → parameters → header → format` | Text |  |
| `api_response → data → parameters → header → params → filename` | Text |  |
| `api_response → data → parameters → header → params → url` | Text |  |
| `api_response → data → send_at` | DateTime |  |
| `api_response → data → sender_email` | Text |  |
| `api_response → data → sender_name` | Text |  |
| `api_response → data → target_channel` | Text |  |
| `api_response → status` | Text |  |
| `id` | Integer |  |
| `uuid` | UUID |  |
| `title` | Text |  |
| `description` | Text |  |
| `api_response` | JSON |  |
| `sender` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_sent` | DateTimeWithLocalTZ |  |
| `contact_list_id` | Integer |  |
| `template_id` | Integer |  |

#### `public.notifications_whatsappcontactlist`

_Fields: 8_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `uuid` | UUID |  |
| `title` | Text |  |
| `contact_list_data` | JSON |  |
| `contact_list_file` | Text |  |
| `status` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_uploaded` | DateTimeWithLocalTZ |  |

#### `public.notifications_whatsappdirectbroadcastnotification`

_Fields: 13_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `uuid` | UUID |  |
| `title` | Text |  |
| `description` | Text |  |
| `api_response` | JSON |  |
| `sender` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_sent` | DateTimeWithLocalTZ |  |
| `receiver_id` | Integer |  |
| `template_id` | Integer |  |
| `body_parameters` | JSON |  |
| `receiver_name` | Text |  |
| `receiver_number` | Text |  |

#### `public.notifications_whatsapptemplate`

_Fields: 12_

| Field | Type | Description |
|---|---|---|
| `header → example` | Text |  |
| `header → format` | Text |  |
| `id` | Integer |  |
| `uuid` | UUID |  |
| `title` | Text |  |
| `language` | Text |  |
| `body` | Text |  |
| `buttons` | JSON |  |
| `status` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `header` | JSON |  |


### `offer_*`

#### `public.offer_link_offerlinkconfig`

_Fields: 13_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `uuid` | UUID |  |
| `name` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `datetime_expiry` | DateTimeWithLocalTZ |  |
| `product_package_id` | Integer |  |
| `school_id` | Integer |  |
| `product_id` | Integer |  |
| `product_group_id` | Integer |  |
| `is_requires_proof_of_income` | Boolean |  |
| `is_requires_school_assessment_file` | Boolean |  |
| `is_requires_guarantor_id` | Boolean |  |

#### `public.offer_link_offerlinkconfig_courses`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `offerlinkconfig_id` | Integer |  |
| `course_id` | Integer |  |


### `offline_*`

#### `public.offline_to_online_userloanbatch`

_Fields: 15_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `uuid` | UUID |  |
| `batch_file` | Text |  |
| `error_file` | Text |  |
| `status` | Text |  |
| `type` | Text |  |
| `date_start` | Date |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `datetime_deleted` | DateTimeWithLocalTZ |  |
| `datetime_ingested` | DateTimeWithLocalTZ |  |
| `partner_id` | Integer |  |
| `product_id` | Integer |  |
| `cohort_id` | Integer |  |
| `date_expiration` | Date |  |


### `ops_*`

#### `public.ops_admin_inboxnotification`

_Fields: 9_

| Field | Type | Description |
|---|---|---|
| `id` | BigInteger |  |
| `is_read` | Boolean |  |
| `is_done` | Boolean |  |
| `datetime_notified` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `message` | Text |  |
| `object_id` | Integer |  |
| `admin_user_id` | Integer |  |
| `content_type_id` | Integer |  |


### `partners_*`

#### `public.partners_admission`

_Fields: 19_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `first_name` | Text |  |
| `last_name` | Text |  |
| `email` | Text |  |
| `mobile_phone` | Text |  |
| `date_of_birth` | Date |  |
| `enrollment_type` | Text |  |
| `document_field` | Text |  |
| `has_selected_news_letter_toggle` | Boolean |  |
| `has_accepted_terms` | Boolean |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `school_id` | Integer |  |
| `program_study` | Text |  |
| `institution_id` | Integer |  |
| `has_selected_scholarship_financial_aid_toggle` | Boolean |  |
| `datetime_applied` | DateTimeWithLocalTZ |  |
| `previous_school` | Text |  |
| `shs_strand` | Text |  |

#### `public.partners_admissionbatch`

_Fields: 10_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `uuid` | UUID |  |
| `status` | Text |  |
| `admission_file` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `datetime_deleted` | DateTimeWithLocalTZ |  |
| `datetime_ingested` | DateTimeWithLocalTZ |  |
| `error_file` | Text |  |
| `uploaded_by_id` | Integer |  |

#### `public.partners_atfentry`

_Fields: 4_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `average_tuition_fee` | Decimal |  |
| `key_id` | Integer |  |
| `school_id` | Integer |  |

#### `public.partners_atfkey`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `name` | Text |  |
| `list_order` | Integer |  |

#### `public.partners_conversionrate`

_Fields: 8_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `lead_type` | Text |  |
| `leads` | Integer |  |
| `registrations` | Integer |  |
| `applications` | Integer |  |
| `activations` | Integer |  |
| `partner_id` | Integer |  |
| `amount_activated` | Decimal |  |

#### `public.partners_course`

_Fields: 7_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `type` | Text |  |
| `name` | Text |  |
| `degree` | Text |  |
| `is_visible_from_borrower_app` | Boolean |  |
| `general_course` | Text |  |
| `segment` | Text |  |

#### `public.partners_coursecategory`

_Fields: 2_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `name` | Text |  |

#### `public.partners_disbursement`

_Fields: 12_

| Field | Type | Description |
|---|---|---|
| `transaction_ptr_id` | Integer |  |
| `disbursement_report_file` | Text |  |
| `status` | Text |  |
| `partner_id` | Integer |  |
| `datetime_disbursed` | DateTimeWithLocalTZ |  |
| `actual_amount` | Decimal |  |
| `disbursement_report_spreadsheet_file` | Text |  |
| `is_report_file_downloaded` | Boolean |  |
| `is_send_disbursement_report_to_poc` | Boolean |  |
| `bank_reference_code` | Text |  |
| `bank_id` | Integer |  |
| `refund_amount` | Decimal |  |

#### `public.partners_disbursementreport`

_Fields: 4_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `report` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `partner_id` | Integer |  |

#### `public.partners_faculty`

_Fields: 2_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `name` | Text |  |

#### `public.partners_incomethresholdconfig`

_Fields: 2_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `income_document_threshold_prompt` | Decimal |  |

#### `public.partners_incomethresholdconfig_affected_partners`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `incomethresholdconfig_id` | Integer |  |
| `partner_id` | Integer |  |

#### `public.partners_institution`

_Fields: 2_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `name` | Text |  |

#### `public.partners_internshipagency`

_Fields: 1_

| Field | Type | Description |
|---|---|---|
| `partner_ptr_id` | Integer |  |

#### `public.partners_partner`

_Fields: 102_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `name` | Text |  |
| `address` | Text |  |
| `bank_name` | Text |  |
| `bank_account` | Text |  |
| `polymorphic_ctype_id` | Integer |  |
| `slug` | Text |  |
| `password` | Text |  |
| `institution_id` | Integer |  |
| `city_id` | Integer |  |
| `country_id` | Integer |  |
| `cover_photo_file` | Text |  |
| `is_primary_phone_verified` | Boolean |  |
| `primary_phone` | Text |  |
| `profile_photo_file` | Text |  |
| `province_id` | Integer |  |
| `is_active` | Boolean |  |
| `available_loan_status` | Text |  |
| `income_category` | Text |  |
| `require_guardian_due_diligence` | Boolean |  |
| `partner_type` | Text |  |
| `max_loan_amount` | Decimal |  |
| `min_loan_amount` | Decimal |  |
| `current_borrower_population` | Integer |  |
| `current_penetration_rate` | Decimal |  |
| `current_total_population` | Integer |  |
| `show_dashboard_disbursements_list_view` | Boolean |  |
| `tuition_fee_file` | Text |  |
| `school_billing_file` | Text |  |
| `student_id_file` | Text |  |
| `average_tuition_fee` | Decimal |  |
| `recovery_rate` | Decimal |  |
| `is_risk_sharing_module_enabled` | Boolean |  |
| `requested_principal_limit` | Decimal |  |
| `is_virtual_account_request_enabled` | Boolean |  |
| `facebook` | Text |  |
| `linkedin` | Text |  |
| `qs_rank` | Integer |  |
| `twitter` | Text |  |
| `website` | Text |  |
| `show_dashboard_applications_list_view` | Boolean |  |
| `show_metrics_applications_widget` | Boolean |  |
| `redirect_url` | Text |  |
| `disbursement_webhook` | Text |  |
| `is_listed` | Boolean |  |
| `show_student_required_revision` | Boolean |  |
| `is_admissions_module_enabled` | Boolean |  |
| `blocking_policy_days` | Integer |  |
| `has_blocking_policy` | Boolean |  |
| `contract_signed_webhook` | Text |  |
| `address_line_1` | Text |  |
| `address_line_2` | Text |  |
| `district` | Text |  |
| `borrower_app_virtual_account_request_enabled` | Boolean |  |
| `virtual_account_important_information` | Text |  |
| `primary_brochure` | Text |  |
| `secondary_brochure` | Text |  |
| `integration_type` | Text |  |
| `partner_age` | Text |  |
| `partner_priority` | Text |  |
| `enrollment_period_end_date` | Date |  |
| `is_secondary_education` | Boolean |  |
| `has_cancellation_policy` | Boolean |  |
| `is_redirect_flow_for_integrations` | Boolean |  |
| `agreement_expiration_date` | Date |  |
| `partner_segment` | Integer |  |
| `balance_to_due_threshold` | Decimal |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `cancellation_webhook` | Text |  |
| `retail_flow_is_open` | Boolean |  |
| `wholesale_url` | Text |  |
| `webhook_key` | Text |  |
| `require_guarantor_due_diligence` | Boolean |  |
| `is_msl` | Boolean |  |
| `loan_status_webhook` | Text |  |
| `disallow_self_guaranteed_applications` | Boolean |  |
| `market_type` | Text |  |
| `ownership` | Text |  |
| `risk_tierer_class` | Text |  |
| `is_recommending_loans` | Boolean |  |
| `date_start_risk_sharing_policy` | Date |  |
| `has_risk_sharing_policy` | Boolean |  |
| `is_international` | Boolean |  |
| `partner_score` | Integer |  |
| `is_lite_plus_integration_partner` | Boolean |  |
| `blocking_policy_start_date` | Date |  |
| `commission_eligible_lead_type` | Text |  |
| `has_commission_agreement` | Boolean |  |
| `application_approved_slack_webhook_url` | Text |  |
| `application_rejected_slack_webhook_url` | Text |  |
| `send_disbursement_report_email_on_disbursement_confirmation` | Boolean |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `allow_gadget_loans` | Boolean |  |
| `house_bank_id` | BigInteger |  |
| `enable_base64_encoded_webhook` | Boolean |  |
| `is_white_label_borrower_app` | Boolean |  |
| `is_crediting_feature_available_in_partner_dashboard` | Boolean |  |
| `send_periodic_partner_report_email` | Boolean |  |
| `active_for_crediting_reminders` | Boolean |  |
| `listed_in` | Text |  |
| `disbursement_method` | Text |  |
| `virtual_account_admin_fee` | Decimal |  |

#### `public.partners_partner_lender_assignment`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `partner_id` | Integer |  |
| `lenderriskassessment_id` | Integer |  |

#### `public.partners_partner_partner_courses`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `partner_id` | Integer |  |
| `course_id` | Integer |  |

#### `public.partners_partner_partner_faculties`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `partner_id` | Integer |  |
| `faculty_id` | Integer |  |

#### `public.partners_partneragreementdocument`

_Fields: 7_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `type` | Text |  |
| `agreement_document_file` | Text |  |
| `valid_start_date` | Date |  |
| `valid_end_date` | Date |  |
| `partner_id` | Integer |  |
| `agreement_number` | Text |  |

#### `public.partners_partnerbank`

_Fields: 8_

| Field | Type | Description |
|---|---|---|
| `bank_info → bank_code` | Text |  |
| `bank_info → bank_old_name` | Text |  |
| `bank_info → swift_code` | Text |  |
| `bank_info → three_digits_bank_code` | Text |  |
| `id` | Integer |  |
| `name` | Text |  |
| `bank_info` | JSON |  |
| `is_featured` | Boolean |  |

#### `public.partners_partnerbankaccount`

_Fields: 15_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `bank_name` | Text |  |
| `bank_account` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `partner_id` | Integer |  |
| `account_type` | Text |  |
| `bank_address` | Text |  |
| `bank_code` | Text |  |
| `beneficiary_account_number` | Text |  |
| `beneficiary_address` | Text |  |
| `beneficiary_code` | Text |  |
| `beneficiary_name` | Text |  |
| `payment_channel_code` | Text |  |
| `swift_code` | Text |  |

#### `public.partners_partnercontactemail`

_Fields: 5_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `email` | Text |  |
| `label` | Text |  |
| `is_verified` | Boolean |  |
| `partner_id` | Integer |  |

#### `public.partners_partnercontactnumber`

_Fields: 5_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `phone` | Text |  |
| `label` | Text |  |
| `is_verified` | Boolean |  |
| `partner_id` | Integer |  |

#### `public.partners_partnercontactperson`

_Fields: 6_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `name` | Text |  |
| `position` | Text |  |
| `mobile_number` | Text |  |
| `email` | Text |  |
| `partner_id` | Integer |  |

#### `public.partners_partnercourseprice`

_Fields: 6_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `start_date` | Date |  |
| `end_date` | Date |  |
| `price` | Decimal |  |
| `course_id` | Integer |  |
| `partner_id` | Integer |  |

#### `public.partners_partnercoursesbatch`

_Fields: 7_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `uuid` | UUID |  |
| `status` | Text |  |
| `course_file` | Text |  |
| `partner_id` | Integer |  |
| `error_file` | Text |  |
| `course_file_type` | Text |  |

#### `public.partners_partnerdataentry`

_Fields: 6_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `date` | Date |  |
| `borrower_population` | Integer |  |
| `total_population` | Integer |  |
| `penetration_rate` | Decimal |  |
| `partner_id` | Integer |  |

#### `public.partners_partnerfilterpreset`

_Fields: 9_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `parameters → loanStatus` | Array |  |
| `parameters → partnerName` | Array |  |
| `module` | Text |  |
| `title` | Text |  |
| `parameters` | JSON |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `user_id` | Integer |  |

#### `public.partners_partnerfilterpreset_institutions`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `partnerfilterpreset_id` | Integer |  |
| `institution_id` | Integer |  |

#### `public.partners_partnerinternalfinancingprograms`

_Fields: 6_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `name` | Text |  |
| `tenor` | Text |  |
| `interest_rate` | Text |  |
| `partner_id` | Integer |  |
| `fee` | Text |  |

#### `public.partners_partnerpaymentdeadline`

_Fields: 8_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `name` | Text |  |
| `minimum_required_payment` | Text |  |
| `valid_start_date` | Date |  |
| `valid_end_date` | Date |  |
| `partner_id` | Integer |  |
| `course_id` | Integer |  |
| `product_group_id` | Integer |  |

#### `public.partners_partnerpaymentpolicies`

_Fields: 4_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `question` | Text |  |
| `answer` | Boolean |  |
| `partner_id` | Integer |  |

#### `public.partners_partnerstockphoto`

_Fields: 4_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `image_file` | Text |  |
| `index` | Integer |  |
| `partner_id` | Integer |  |

#### `public.partners_personofcontact`

_Fields: 7_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `email` | Text |  |
| `first_name` | Text |  |
| `last_name` | Text |  |
| `position` | Text |  |
| `partner_id` | Integer |  |
| `type` | Text |  |

#### `public.partners_quicklink`

_Fields: 6_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `text` | Text |  |
| `link` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `partner_id` | Integer |  |

#### `public.partners_school`

_Fields: 4_

| Field | Type | Description |
|---|---|---|
| `partner_ptr_id` | Integer |  |
| `academic_terms` | Integer |  |
| `income_document_threshold_prompt` | Decimal |  |
| `can_update_mobile_number` | Boolean |  |

#### `public.partners_segmentassignment`

_Fields: 4_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `segment` | Text |  |
| `category_id` | Integer |  |
| `school_id` | Integer |  |

#### `public.partners_specialevent`

_Fields: 6_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `name` | Text |  |
| `event_type` | Text |  |
| `datetime_start` | DateTimeWithLocalTZ |  |
| `datetime_end` | DateTimeWithLocalTZ |  |
| `partner_id` | Integer |  |

#### `public.partners_specificpartnercourse`

_Fields: 13_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `degree_accreditation` | Text |  |
| `general_course` | Text |  |
| `shs_strand` | Text |  |
| `tuition_per_term` | Decimal |  |
| `course_length_in_months` | Integer |  |
| `months_per_term` | Integer |  |
| `terms_per_year` | Integer |  |
| `course_id` | Integer |  |
| `partner_id` | Integer |  |
| `average_tuition` | Decimal |  |
| `development_fee` | Decimal |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |

#### `public.partners_unlistedinstitution`

_Fields: 4_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `name` | Text |  |
| `email` | Text |  |
| `mobile_number` | Text |  |

#### `public.partners_unlistedschool`

_Fields: 4_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `name` | Text |  |
| `email` | Text |  |
| `mobile_number` | Text |  |


### `payables_*`

#### `public.payables_cashjournal`

_Fields: 5_

| Field | Type | Description |
|---|---|---|
| `id` | BigInteger |  |
| `amount` | Decimal |  |
| `bank_id` | BigInteger |  |
| `payable_document_id` | BigInteger |  |
| `loan_id` | Integer |  |

#### `public.payables_housebank`

_Fields: 7_

| Field | Type | Description |
|---|---|---|
| `id` | BigInteger |  |
| `bank_name` | Text |  |
| `account` | Text |  |
| `gl_account_number` | Text |  |
| `internal_name` | Text |  |
| `slug` | Text |  |
| `swift_code` | Text |  |

#### `public.payables_partnerledger`

_Fields: 15_

| Field | Type | Description |
|---|---|---|
| `id` | BigInteger |  |
| `date_due` | Date |  |
| `gross_amount` | Decimal |  |
| `discount` | Decimal |  |
| `net_amount` | Decimal |  |
| `datetime_cleared` | DateTimeWithLocalTZ |  |
| `report_file` | Text |  |
| `clearing_document_id` | BigInteger |  |
| `partner_id` | Integer |  |
| `partner_bank_id` | Integer |  |
| `payable_document_id` | BigInteger |  |
| `is_report_file_downloaded` | Boolean |  |
| `loan_id` | Integer |  |
| `cohort_id` | Integer |  |
| `is_reversed` | Boolean |  |

#### `public.payables_payabledocument`

_Fields: 14_

| Field | Type | Description |
|---|---|---|
| `id` | BigInteger |  |
| `uuid` | UUID |  |
| `document_type` | Text |  |
| `status` | Text |  |
| `transaction_type` | Text |  |
| `datetime_posted` | DateTimeWithLocalTZ |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `reference_code` | Text |  |
| `description` | Text |  |
| `date_start` | Date |  |
| `payment_term_id` | BigInteger |  |
| `posted_by_id` | Integer |  |
| `cohort_id` | Integer |  |
| `created_by_id` | Integer |  |

#### `public.payables_payableitem`

_Fields: 9_

| Field | Type | Description |
|---|---|---|
| `id` | BigInteger |  |
| `gross_amount` | Decimal |  |
| `discount` | Decimal |  |
| `net_amount` | Decimal |  |
| `datetime_cleared` | DateTimeWithLocalTZ |  |
| `clearing_document_id` | BigInteger |  |
| `loan_id` | Integer |  |
| `partner_id` | Integer |  |
| `payable_document_id` | BigInteger |  |

#### `public.payables_paymentterm`

_Fields: 2_

| Field | Type | Description |
|---|---|---|
| `id` | BigInteger |  |
| `name` | Text |  |

#### `public.payables_paymenttermline`

_Fields: 5_

| Field | Type | Description |
|---|---|---|
| `id` | BigInteger |  |
| `period` | Integer |  |
| `percentage` | Decimal |  |
| `discount_percentage` | Decimal |  |
| `payment_term_id` | BigInteger |  |

#### `public.payables_paymenttermpartner`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | BigInteger |  |
| `partner_id` | Integer |  |
| `payment_term_id` | BigInteger |  |

#### `public.payables_paymenttermproduct`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | BigInteger |  |
| `payment_term_id` | BigInteger |  |
| `product_id` | Integer |  |

#### `public.payables_supportingdocument`

_Fields: 7_

| Field | Type | Description |
|---|---|---|
| `id` | BigInteger |  |
| `uuid` | UUID |  |
| `name` | Text |  |
| `file` | Text |  |
| `metadata` | JSON |  |
| `payable_document_id` | BigInteger |  |
| `type` | Text |  |


### `payments_*`

#### `public.payments_payment`

_Fields: 90_

| Field | Type | Description |
|---|---|---|
| `channel_response → data → redirect_url` | Text |  |
| `channel_response → data → token` | Text |  |
| `channel_response → response_code` | Integer |  |
| `id` | BigInteger |  |
| `notification_data → acquirer` | Text |  |
| `notification_data → bill_key` | Text |  |
| `notification_data → biller_code` | Text |  |
| `notification_data → currency` | Text |  |
| `notification_data → customer_details → full_name` | Text |  |
| `notification_data → expiry_time` | DateTime |  |
| `notification_data → fraud_status` | Text |  |
| `notification_data → gross_amount` | Text |  |
| `notification_data → issuer` | Text |  |
| `notification_data → merchant_id` | Text |  |
| `notification_data → order_id` | Text |  |
| `notification_data → payment_amounts` | Array |  |
| `notification_data → payment_code` | Text |  |
| `notification_data → payment_option_type` | Text |  |
| `notification_data → payment_type` | Text |  |
| `notification_data → pop_id` | Text |  |
| `notification_data → reference_id` | Text |  |
| `notification_data → settlement_time` | DateTime |  |
| `notification_data → shopeepay_reference_number` | Text |  |
| `notification_data → signature_key` | Text |  |
| `notification_data → status_code` | Text |  |
| `notification_data → status_message` | Text |  |
| `notification_data → store` | Text |  |
| `notification_data → transaction_id` | Text |  |
| `notification_data → transaction_status` | Text |  |
| `notification_data → transaction_time` | DateTime |  |
| `notification_data → transaction_type` | Text |  |
| `notification_data → va_numbers` | Array |  |
| `query_response → acquirer` | Text |  |
| `query_response → actions` | Array |  |
| `query_response → bill_key` | Text |  |
| `query_response → biller_code` | Text |  |
| `query_response → currency` | Text |  |
| `query_response → expiry_time` | DateTime |  |
| `query_response → fraud_status` | Text |  |
| `query_response → gross_amount` | Text |  |
| `query_response → id` | Text |  |
| `query_response → merchant_id` | Text |  |
| `query_response → order_id` | Text |  |
| `query_response → payment_amounts` | Array |  |
| `query_response → payment_code` | Text |  |
| `query_response → payment_type` | Text |  |
| `query_response → reference_id` | Text |  |
| `query_response → settlement_time` | DateTime |  |
| `query_response → signature_key` | Text |  |
| `query_response → status_code` | Text |  |
| `query_response → status_message` | Text |  |
| `query_response → store` | Text |  |
| `query_response → transaction_id` | Text |  |
| `query_response → transaction_status` | Text |  |
| `query_response → transaction_time` | DateTime |  |
| `query_response → va_numbers` | Array |  |
| `request_params → alfamart → alfamart_free_text_1` | Text |  |
| `request_params → callbacks → finish` | Text |  |
| `request_params → cstore → alfamart_free_text_1` | Text |  |
| `request_params → cstore → alfamart_free_text_2` | Text |  |
| `request_params → customer_details → first_name` | Text |  |
| `request_params → customer_details → last_name` | Text |  |
| `request_params → enabled_payments` | Array |  |
| `request_params → gopay → callback_url` | Text |  |
| `request_params → gopay → enable_callback` | Boolean |  |
| `request_params → item_details` | Array |  |
| `request_params → shopeepay → callback_url` | Text |  |
| `request_params → transaction_details → gross_amount` | Text |  |
| `request_params → transaction_details → order_id` | Text |  |
| `uuid` | UUID |  |
| `reference_code` | Text |  |
| `amount` | Decimal |  |
| `confirmed_amount` | Decimal |  |
| `status` | Text |  |
| `request_params` | JSON |  |
| `channel_response` | JSON |  |
| `notification_data` | JSON |  |
| `redirect_url` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `borrower_id` | Integer |  |
| `channel_id` | BigInteger |  |
| `query_response` | JSON |  |
| `subchannel_id` | BigInteger |  |
| `transaction_id` | Text |  |
| `extra_charges_amount` | Decimal |  |
| `net_confirmed_amount` | Decimal |  |
| `va_number` | Text |  |
| `datetime_expired` | DateTimeWithLocalTZ |  |
| `datetime_paid` | DateTimeWithLocalTZ |  |

#### `public.payments_paymentaccount`

_Fields: 82_

| Field | Type | Description |
|---|---|---|
| `channel_response → account_balance` | Integer |  |
| `channel_response → account_number` | Text |  |
| `channel_response → account_status` | Text |  |
| `channel_response → account_type` | Text |  |
| `channel_response → actions` | Array |  |
| `channel_response → branch_opening_location_code` | Text |  |
| `channel_response → business_id` | Text |  |
| `channel_response → capture_method` | Text |  |
| `channel_response → channel_code` | Text |  |
| `channel_response → channel_properties → display_name` | Text |  |
| `channel_response → channel_properties → expires_at` | Text |  |
| `channel_response → country` | Text |  |
| `channel_response → created` | DateTime |  |
| `channel_response → currency` | Text |  |
| `channel_response → data → created` | DateTime |  |
| `channel_response → data → current_balance` | Integer |  |
| `channel_response → data → customer_accounts` | Array |  |
| `channel_response → data → customer_escrow_id` | Text |  |
| `channel_response → data → email` | Text |  |
| `channel_response → data → external_id` | Text |  |
| `channel_response → data → given_name` | Text |  |
| `channel_response → data → id` | Text |  |
| `channel_response → data → ktp_number` | Text |  |
| `channel_response → data → mobile_number` | Text |  |
| `channel_response → data → status` | Text |  |
| `channel_response → data → surname` | Text |  |
| `channel_response → data → type` | Text |  |
| `channel_response → data → updated` | DateTime |  |
| `channel_response → description` | Text |  |
| `channel_response → email` | Text |  |
| `channel_response → event` | Text |  |
| `channel_response → external_id` | Text |  |
| `channel_response → id` | Text |  |
| `channel_response → id_issuing_city` | Text |  |
| `channel_response → id_number` | Text |  |
| `channel_response → last_name` | Text |  |
| `channel_response → latest_payment_id` | Text |  |
| `channel_response → mobile_phone_number` | Text |  |
| `channel_response → payment_request_id` | Text |  |
| `channel_response → reference_id` | Text |  |
| `channel_response → source_of_fund` | Text |  |
| `channel_response → status` | Text |  |
| `channel_response → type` | Text |  |
| `channel_response → updated` | DateTime |  |
| `id` | BigInteger |  |
| `request_params → account_number` | Text |  |
| `request_params → account_type` | Text |  |
| `request_params → branch_opening_location_code` | Text |  |
| `request_params → channel_code` | Text |  |
| `request_params → channel_properties → display_name` | Text |  |
| `request_params → channel_properties → expires_at` | DateTime |  |
| `request_params → country` | Text |  |
| `request_params → currency` | Text |  |
| `request_params → customer_accounts` | Array |  |
| `request_params → description` | Text |  |
| `request_params → email` | Text |  |
| `request_params → external_id` | Text |  |
| `request_params → given_name` | Text |  |
| `request_params → id_issuing_city` | Text |  |
| `request_params → id_number` | Text |  |
| `request_params → ktp_number` | Text |  |
| `request_params → last_name` | Text |  |
| `request_params → mobile_number` | Text |  |
| `request_params → mobile_phone_number` | Text |  |
| `request_params → reference_id` | Text |  |
| `request_params → source_of_fund` | Text |  |
| `request_params → surname` | Text |  |
| `request_params → type` | Text |  |
| `account_id` | Text |  |
| `status` | Text |  |
| `request_params` | JSON |  |
| `channel_response` | JSON |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `user_id` | Integer |  |
| `channel_id` | BigInteger |  |
| `payout_destination_account_id` | Integer |  |
| `fixed_virtual_account_id` | Integer |  |
| `investor_id` | Text |  |
| `datetime_expired` | DateTimeWithLocalTZ |  |
| `loan_id` | Integer |  |
| `uuid` | UUID |  |

#### `public.payments_paymentchannel`

_Fields: 20_

| Field | Type | Description |
|---|---|---|
| `config_pack → api_key` | Text |  |
| `config_pack → escrow_provider_id` | Integer |  |
| `config_pack → fixed_va_payment_request_url` | Text |  |
| `config_pack → is_production` | Boolean |  |
| `config_pack → max_retries` | Integer |  |
| `config_pack → minimum_amount` | Integer |  |
| `config_pack → payment_account_request_url` | Text |  |
| `config_pack → payment_request_url` | Text |  |
| `config_pack → server_key` | Text |  |
| `config_pack → webhook_token` | Text |  |
| `id` | BigInteger |  |
| `name` | Text |  |
| `enabled` | Boolean |  |
| `disabled_reason` | Text |  |
| `module` | Text |  |
| `ui_pack` | JSON |  |
| `config_pack` | JSON |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_modified` | DateTimeWithLocalTZ |  |
| `requires_subchannel` | Boolean |  |

#### `public.payments_paymentshortlink`

_Fields: 11_

| Field | Type | Description |
|---|---|---|
| `id` | BigInteger |  |
| `loan_reference_code` | Text |  |
| `amount_type` | Text |  |
| `custom_amount` | Decimal |  |
| `payment_amount` | Decimal |  |
| `original_url` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `channel_id` | BigInteger |  |
| `payment_id` | BigInteger |  |
| `subchannel_id` | BigInteger |  |

#### `public.payments_subchannel`

_Fields: 18_

| Field | Type | Description |
|---|---|---|
| `config_pack → callback_url` | Text |  |
| `config_pack → enabled_payments` | Array |  |
| `config_pack → expiry_time` | Integer |  |
| `config_pack → extra_payload → alfamart_free_text_1` | Text |  |
| `config_pack → extra_payload → callback_url` | Text |  |
| `config_pack → extra_payload → enable_callback` | Boolean |  |
| `config_pack → notification_base_url` | Text |  |
| `config_pack → service_charge` | Text |  |
| `config_pack → service_charge_type` | Text |  |
| `config_pack → success_url` | Text |  |
| `id` | BigInteger |  |
| `name` | Text |  |
| `enabled` | Boolean |  |
| `ui_pack` | JSON |  |
| `config_pack` | JSON |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_modified` | DateTimeWithLocalTZ |  |
| `channel_id` | BigInteger |  |


### `pefindos_*`

#### `public.pefindos_pefindo`

_Fields: 11_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `relation_report` | Text |  |
| `individual_report` | Text |  |
| `contract_report` | Text |  |
| `company_report` | Text |  |
| `collateral_report` | Text |  |
| `header_file` | Text |  |
| `batch_file` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `date_of_file` | Date |  |
| `is_for_testing` | Boolean |  |

#### `public.pefindos_pefindoinquirydata`

_Fields: 17_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `name` | Text |  |
| `ktp_number` | Text |  |
| `phone_number` | Text |  |
| `role_of_client` | Text |  |
| `organizer_type` | Text |  |
| `type_of_contract` | Text |  |
| `contract_date` | Date |  |
| `contract_status` | Text |  |
| `total_amount` | Decimal |  |
| `outstanding_amount` | Decimal |  |
| `past_due_amount` | Decimal |  |
| `past_due_days` | Integer |  |
| `currency_of_contract` | Text |  |
| `profile_id` | Integer |  |
| `inquiry_log_id` | Integer |  |
| `loan_application_id` | Integer |  |

#### `public.pefindos_pefindoinquirylog`

_Fields: 12_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `pefindo_id` | Text |  |
| `report_reference_number` | Text |  |
| `status` | Text |  |
| `reason` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `processor_id` | Integer |  |
| `profile_id` | Integer |  |
| `loan_application_id` | Integer |  |
| `CB_score` | Text |  |
| `CB_score_grade` | Text |  |
| `probability_failed_to_pay` | Decimal |  |


### `referrals_*`

#### `public.referrals_referral`

_Fields: 7_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `code` | Text |  |
| `redirect_to` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `datetime_expiry` | DateTimeWithLocalTZ |  |
| `referrer_id` | Integer |  |

#### `public.referrals_referralresponse`

_Fields: 7_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `ip_address` | IPAddress |  |
| `user_agent` | Text |  |
| `action` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `referee_id` | Integer |  |
| `referral_id` | Integer |  |


### `regions_*`

#### `public.regions_city`

_Fields: 9_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `reporting_code → new_ojk_code` | Integer |  |
| `reporting_code → old_ojk_code` | Text |  |
| `reporting_code → pefindo_code` | Text |  |
| `name` | Text |  |
| `province_id` | Integer |  |
| `ojk_code` | Text |  |
| `pefindo_code` | Text |  |
| `reporting_code` | JSON |  |

#### `public.regions_country`

_Fields: 2_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `name` | Text |  |

#### `public.regions_district`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `name` | Text |  |
| `city_id` | Integer |  |

#### `public.regions_province`

_Fields: 6_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `name` | Text |  |
| `country_id` | Integer |  |
| `ojk_code` | Text |  |
| `apu_ppt_risk_profile` | Integer |  |
| `region_id` | Integer |  |

#### `public.regions_region`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `name` | Text |  |
| `country_id` | Integer |  |

#### `public.regions_subdistrict`

_Fields: 4_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `name` | Text |  |
| `district_id` | Integer |  |
| `postal_code` | Text |  |


### `reports_*`

#### `public.reports_accessblockingreport`

_Fields: 6_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `report_file` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_generated` | DateTimeWithLocalTZ |  |
| `partner_id` | Integer |  |
| `institution_id` | Integer |  |

#### `public.reports_creditbureaureport`

_Fields: 8_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `type` | Text |  |
| `sub_type` | Text |  |
| `provider` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `date_of_file` | Date |  |
| `version` | Text |  |
| `report_file` | Text |  |

#### `public.reports_failedpusdafilreport`

_Fields: 5_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `error_message` | Text |  |
| `report_name` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `report_batch_id` | Integer |  |

#### `public.reports_lenderchannelingreport`

_Fields: 8_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `type` | Text |  |
| `channel` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `date_of_file` | Date |  |
| `version` | Text |  |
| `report_file` | Text |  |
| `sub_type` | Text |  |

#### `public.reports_metabasecard`

_Fields: 7_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `title` | Text |  |
| `slug` | Text |  |
| `card_id` | Integer |  |
| `card_url` | Text |  |

#### `public.reports_pusdafilreport`

_Fields: 13_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `status` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_generated` | DateTimeWithLocalTZ |  |
| `date_of_file` | Date |  |
| `reg_pengguna_file` | Text |  |
| `reg_lender_file` | Text |  |
| `reg_borrower_file` | Text |  |
| `pengajuan_pinjaman_file` | Text |  |
| `pengajuan_pemberian_pinjaman_file` | Text |  |
| `transaksi_pinjam_meminjam_file` | Text |  |
| `pembayaran_pinjaman_file` | Text |  |
| `response_file` | Text |  |

#### `public.reports_repaymentanalyticsreport`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `snapshot_start_date` | Date |  |
| `snapshot_end_date` | Date |  |

#### `public.reports_repaymentanalyticsrow`

_Fields: 30_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `snapshot_date` | Date |  |
| `date_disbursed` | DateTimeWithLocalTZ |  |
| `loan_id` | Integer |  |
| `user_id` | Integer |  |
| `amount_disbursed` | Decimal |  |
| `total_scheduled_revenue` | Decimal |  |
| `funding_cost` | Decimal |  |
| `net_interest_margin` | Decimal |  |
| `npl_net_principal` | Decimal |  |
| `npl_unearned_revenue` | Decimal |  |
| `writeoff_net_principal` | Decimal |  |
| `writeoff_unearned_revenue` | Decimal |  |
| `unit_econs_currency` | Decimal |  |
| `outstanding_net_principal` | Decimal |  |
| `unearned_revenue` | Decimal |  |
| `past_due_bucket` | Text |  |
| `loan_status` | Text |  |
| `country` | Text |  |
| `partner_id` | Integer |  |
| `partner_name` | Text |  |
| `product_id` | Integer |  |
| `tenor` | Integer |  |
| `grace_period` | Integer |  |
| `interest_rate` | Decimal |  |
| `discount` | Decimal |  |
| `origination_fee` | Decimal |  |
| `effective_interest_rate` | Decimal |  |
| `repayment_id` | Integer |  |
| `report_id` | Integer |  |

#### `public.reports_treasurydisbursementreport`

_Fields: 5_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `type` | Text |  |
| `report_file` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_generated` | DateTimeWithLocalTZ |  |

#### `public.reports_uniqueborrowersreport`

_Fields: 31_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `loan_id` | Text |  |
| `datetime_logged` | DateTimeWithLocalTZ |  |
| `datetime_original_disbursemt` | DateTimeWithLocalTZ |  |
| `actual_disbursement_amount` | Decimal |  |
| `net_principal` | Decimal |  |
| `past_due_bucket` | Text |  |
| `days_past_due` | Integer |  |
| `user_id` | Text |  |
| `loan_status` | Text |  |
| `total_due_to_date` | Decimal |  |
| `total_paid_to_date` | Decimal |  |
| `income_recognised` | Decimal |  |
| `accrued_income_to_date` | Decimal |  |
| `credit_loss_from_interest` | Decimal |  |
| `credit_loss_allowance_BS` | Decimal |  |
| `credit_loss_expense_IS` | Decimal |  |
| `payment_status` | Text |  |
| `total_payment_made` | Decimal |  |
| `total_payment_due` | Decimal |  |
| `interest_due` | Decimal |  |
| `principal_due` | Decimal |  |
| `discount_amortised` | Decimal |  |
| `country` | Text |  |
| `partner_id` | Text |  |
| `product_id` | Text |  |
| `grace_period` | Integer |  |
| `tenor` | Integer |  |
| `interest_rate` | Decimal |  |
| `discount` | Decimal |  |
| `origination_fee` | Decimal |  |

#### `public.reports_writtenoffreport`

_Fields: 7_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `datetime_as_of` | DateTimeWithLocalTZ |  |
| `report_file` | Text |  |
| `datetime_generated` | DateTimeWithLocalTZ |  |
| `written_off_count` | Integer |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `status` | Text |  |


### `rest_*`

#### `public.rest_framework_api_key_apikey`

_Fields: 7_

| Field | Type | Description |
|---|---|---|
| `id` | Text |  |
| `created` | DateTimeWithLocalTZ |  |
| `name` | Text |  |
| `revoked` | Boolean |  |
| `expiry_date` | DateTimeWithLocalTZ |  |
| `hashed_key` | Text |  |
| `prefix` | Text |  |


### `rewards_*`

#### `public.rewards_cashrewarddisbursement`

_Fields: 7_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `amount` | Integer |  |
| `datetime_disbursed` | DateTimeWithLocalTZ |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `status` | Text |  |
| `user_id` | Integer |  |

#### `public.rewards_cashrewardpromo`

_Fields: 10_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `title` | Text |  |
| `promo_code` | Text |  |
| `description` | Text |  |
| `max_redemptions_per_user` | Integer |  |
| `amount` | Integer |  |
| `for_profile_status` | Text |  |
| `for_loan_status` | Text |  |
| `voucher_expiration_date` | Date |  |
| `total_max_redemptions` | Integer |  |

#### `public.rewards_cashrewardpromo_for_school`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `cashrewardpromo_id` | Integer |  |
| `partner_id` | Integer |  |

#### `public.rewards_cashrewardvoucher`

_Fields: 15_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `uuid` | UUID |  |
| `valid_start_date` | Date |  |
| `valid_end_date` | Date |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `status` | Text |  |
| `disbursement_id` | Integer |  |
| `promo_id` | Integer |  |
| `user_id` | Integer |  |
| `account_name` | Text |  |
| `account_number` | Text |  |
| `bank_name` | Text |  |
| `bank_branch` | Text |  |
| `bank_code` | Text |  |

#### `public.rewards_rewarduser`

_Fields: 8_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `bank_name` | Text |  |
| `account_name` | Text |  |
| `account_number` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `is_active` | Boolean |  |
| `user_id` | Integer |  |


### `scores_*`

#### `public.scores_score`

_Fields: 14_

| Field | Type | Description |
|---|---|---|
| `id` | BigInteger |  |
| `type` | Text |  |
| `score` | Integer |  |
| `rating` | Text |  |
| `version` | Text |  |
| `description` | Text |  |
| `error` | Text |  |
| `datetime_computed` | DateTimeWithLocalTZ |  |
| `object_id` | Integer |  |
| `content_type_id` | Integer |  |
| `user_id` | Integer |  |
| `reference_date` | Date |  |
| `decision` | Text |  |
| `probability` | Decimal |  |


### `shortlinks_*`

#### `public.shortlinks_shortlink`

_Fields: 15_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `original_url` | Text |  |
| `is_active` | Boolean |  |
| `num_clicks` | Integer |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `datetime_expiry` | DateTimeWithLocalTZ |  |
| `affiliate_id` | Text |  |
| `campaign` | Text |  |
| `content` | Text |  |
| `custom_code` | Text |  |
| `medium` | Text |  |
| `source` | Text |  |
| `title` | Text |  |
| `batch_id` | Integer |  |

#### `public.shortlinks_shortlinkbatch`

_Fields: 10_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `uuid` | UUID |  |
| `batch_file` | Text |  |
| `error_file` | Text |  |
| `status` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `datetime_deleted` | DateTimeWithLocalTZ |  |
| `datetime_ingested` | DateTimeWithLocalTZ |  |
| `results_file` | Text |  |


### `simple_*`

#### `public.simple_email_confirmation_emailaddress`

_Fields: 6_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `email` | Text |  |
| `key` | Text |  |
| `set_at` | DateTimeWithLocalTZ |  |
| `confirmed_at` | DateTimeWithLocalTZ |  |
| `user_id` | Integer |  |


### `socialaccount_*`

#### `public.socialaccount_socialaccount`

_Fields: 7_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `provider` | Text |  |
| `uid` | Text |  |
| `last_login` | DateTimeWithLocalTZ |  |
| `date_joined` | DateTimeWithLocalTZ |  |
| `extra_data` | Text |  |
| `user_id` | Integer |  |

#### `public.socialaccount_socialapp`

_Fields: 6_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `provider` | Text |  |
| `name` | Text |  |
| `client_id` | Text |  |
| `secret` | Text |  |
| `key` | Text |  |

#### `public.socialaccount_socialapp_sites`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `socialapp_id` | Integer |  |
| `site_id` | Integer |  |

#### `public.socialaccount_socialtoken`

_Fields: 6_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `token` | Text |  |
| `token_secret` | Text |  |
| `expires_at` | DateTimeWithLocalTZ |  |
| `account_id` | Integer |  |
| `app_id` | Integer |  |


### `stamps_*`

#### `public.stamps_stamp`

_Fields: 13_

| Field | Type | Description |
|---|---|---|
| `id` | BigInteger |  |
| `name` | Text |  |
| `label` | Text |  |
| `condition` | Text |  |
| `background_color` | Text |  |
| `text_color` | Text |  |
| `custom_css` | Text |  |
| `priority` | Integer |  |
| `is_active` | Boolean |  |
| `created_at` | DateTimeWithLocalTZ |  |
| `updated_at` | DateTimeWithLocalTZ |  |
| `exclude_condition` | Text |  |
| `target_content_type_id` | Integer |  |

#### `public.stamps_statusstampconfig`

_Fields: 8_

| Field | Type | Description |
|---|---|---|
| `id` | BigInteger |  |
| `status` | Text |  |
| `background_color` | Text |  |
| `text_color` | Text |  |
| `custom_css` | Text |  |
| `priority` | Integer |  |
| `enabled` | Boolean |  |
| `target_content_type_id` | Integer |  |


### `survey_*`

#### `public.survey_choice`

_Fields: 4_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `value` | Text |  |
| `question_id` | Integer |  |
| `label` | Text |  |

#### `public.survey_question`

_Fields: 9_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `status` | Text |  |
| `type` | Text |  |
| `query` | Text |  |
| `context` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_published` | DateTimeWithLocalTZ |  |
| `datetime_closed` | DateTimeWithLocalTZ |  |
| `survey_id` | Integer |  |

#### `public.survey_response`

_Fields: 11_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `status` | Text |  |
| `type` | Text |  |
| `channel` | Text |  |
| `query` | Text |  |
| `answer` | Text |  |
| `datetime_opened` | DateTimeWithLocalTZ |  |
| `datetime_answered` | DateTimeWithLocalTZ |  |
| `datetime_unanswered` | DateTimeWithLocalTZ |  |
| `borrower_id` | Integer |  |
| `question_id` | Integer |  |

#### `public.survey_survey`

_Fields: 14_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `status` | Text |  |
| `context` | Text |  |
| `for_profile_status` | Text |  |
| `for_loan_status` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_published` | DateTimeWithLocalTZ |  |
| `datetime_closed` | DateTimeWithLocalTZ |  |
| `date_to_publish` | Date |  |
| `date_to_close` | Date |  |
| `nudge_point` | Text |  |
| `for_past_due_bucket` | Text |  |
| `headline` | Text |  |
| `sub_headline` | Text |  |

#### `public.survey_survey_for_school`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `survey_id` | Integer |  |
| `partner_id` | Integer |  |


### `taggit_*`

#### `public.taggit_tag`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `name` | Text |  |
| `slug` | Text |  |

#### `public.taggit_taggeditem`

_Fields: 4_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `object_id` | Integer |  |
| `content_type_id` | Integer |  |
| `tag_id` | Integer |  |


### `token_*`

#### `public.token_blacklist_blacklistedtoken`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `blacklisted_at` | DateTimeWithLocalTZ |  |
| `token_id` | Integer |  |

#### `public.token_blacklist_outstandingtoken`

_Fields: 6_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `token` | Text |  |
| `created_at` | DateTimeWithLocalTZ |  |
| `expires_at` | DateTimeWithLocalTZ |  |
| `user_id` | Integer |  |
| `jti` | Text |  |


### `underwriting_*`

#### `public.underwriting_interimschoolsummary`

_Fields: 4_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `school` | Text |  |
| `general_course` | Text |  |
| `tuition_year` | Decimal |  |


### `users_*`

#### `public.users_accountdeletion`

_Fields: 15_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `loan_info → loan_applications` | Array |  |
| `loan_info → loans` | Array |  |
| `user_info → ktp_id_card_number` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `username` | Text |  |
| `first_name` | Text |  |
| `last_name` | Text |  |
| `email` | Text |  |
| `user_info` | JSON |  |
| `loan_info` | JSON |  |
| `status` | Text |  |
| `user_id` | Integer |  |
| `purpose` | Text |  |

#### `public.users_adminrole`

_Fields: 16_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `name` | Text |  |
| `display_label` | Text |  |
| `rank` | Integer |  |
| `principal_limit` | Decimal |  |
| `exposure_deviation_limit` | Decimal |  |
| `exposure_limit` | Decimal |  |
| `mip_principal_limit` | Decimal |  |
| `approvals` | Boolean |  |
| `rejections` | Boolean |  |
| `special_approvals` | Boolean |  |
| `underwriting` | Boolean |  |
| `is_human_agent` | Boolean |  |
| `max_assessment_limit` | Decimal |  |
| `min_assessment_limit` | Decimal |  |
| `department` | Text |  |

#### `public.users_autotopupconfig`

_Fields: 2_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |

#### `public.users_blacklistedprofile`

_Fields: 8_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `name` | Text |  |
| `date_of_birth` | Date |  |
| `id_number` | Text |  |
| `id_type` | Text |  |
| `id_type_notes` | Text |  |
| `general_notes` | Text |  |
| `name_order_eastern` | Boolean |  |

#### `public.users_blacklistedprofilebatch`

_Fields: 8_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `file_hash` | Text |  |
| `status` | Text |  |
| `blacklist_file` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `datetime_ingested` | DateTimeWithLocalTZ |  |
| `valid_entries` | Integer |  |

#### `public.users_corporatemanagement`

_Fields: 8_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `position` | Text |  |
| `ownership_share` | Decimal |  |
| `is_active` | Boolean |  |
| `corporate_id` | Integer |  |
| `manager_id` | Integer |  |

#### `public.users_debtburdenratiodeviationtier`

_Fields: 5_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `min_declared_income` | Decimal |  |
| `max_declared_income` | Decimal |  |
| `debt_burden_ratio_max_deviation` | Decimal |  |
| `auto_top_up_config_id` | Integer |  |

#### `public.users_employmentindustry`

_Fields: 7_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `name` | Text |  |
| `ojk_code` | Text |  |
| `ojk_name` | Text |  |
| `desirable` | Boolean |  |
| `apu_ppt_risk_profile` | Integer |  |
| `reporting_code` | JSON |  |

#### `public.users_employmentstatus`

_Fields: 7_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `reporting_code → slik_code` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `name` | Text |  |
| `apu_ppt_risk_profile` | Integer |  |
| `reporting_code` | JSON |  |

#### `public.users_enlistment`

_Fields: 11_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `is_main_school` | Boolean |  |
| `year_level` | Integer |  |
| `general_course` | Text |  |
| `degree` | Text |  |
| `program` | Text |  |
| `institution_id` | Integer |  |
| `school_id` | Integer |  |
| `student_id` | Integer |  |
| `id_number` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |

#### `public.users_grade`

_Fields: 7_

| Field | Type | Description |
|---|---|---|
| `uuid` | UUID |  |
| `year_level` | Integer |  |
| `subject_name` | Text |  |
| `score` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `profile_id` | Integer |  |

#### `public.users_guardianfinancialobligation`

_Fields: 4_

| Field | Type | Description |
|---|---|---|
| `id` | UUID |  |
| `name` | Text |  |
| `monthly_repayment` | Decimal |  |
| `profile_id` | Integer |  |

#### `public.users_historicaleligibilitytoapply`

_Fields: 6_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `source_state` | Boolean |  |
| `state` | Boolean |  |
| `reason` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `profile_id` | Integer |  |

#### `public.users_idprofile`

_Fields: 92_

| Field | Type | Description |
|---|---|---|
| `profile_ptr_id` | Integer |  |
| `ktp_ocr_file` | Text |  |
| `ktp_id_card_number` | Text |  |
| `religion` | Text |  |
| `marital_status` | Text |  |
| `district_id` | Integer |  |
| `sub_district_id` | Integer |  |
| `guarantor_number_of_dependents` | Integer |  |
| `selfie_file` | Text |  |
| `selfie_file_notes` | Text |  |
| `selfie_file_status` | Text |  |
| `address_rt` | Text |  |
| `address_rw` | Text |  |
| `ktp_address` | Text |  |
| `ktp_address_rt` | Text |  |
| `ktp_address_rw` | Text |  |
| `ktp_city_id` | Integer |  |
| `ktp_district_id` | Integer |  |
| `ktp_province_id` | Integer |  |
| `ktp_sub_district_id` | Integer |  |
| `residence_ownership` | Text |  |
| `guarantor_privy_id` | Text |  |
| `guarantor_privy_registration_status` | Text |  |
| `guarantor_privy_reject_reason` | Text |  |
| `guarantor_privy_user_token` | Text |  |
| `privy_id` | Text |  |
| `privy_registration_status` | Text |  |
| `privy_reject_reason` | Text |  |
| `privy_user_token` | Text |  |
| `student_status` | Text |  |
| `driver_license_card_file` | Text |  |
| `family_card_file` | Text |  |
| `guarantor_address_rt` | Text |  |
| `guarantor_address_rw` | Text |  |
| `guarantor_district_id` | Integer |  |
| `guarantor_employment_status_text` | Text |  |
| `guarantor_ktp_address` | Text |  |
| `guarantor_ktp_address_rt` | Text |  |
| `guarantor_ktp_address_rw` | Text |  |
| `guarantor_ktp_city_id` | Integer |  |
| `guarantor_ktp_district_id` | Integer |  |
| `guarantor_ktp_file` | Text |  |
| `guarantor_ktp_id_card_number` | Text |  |
| `guarantor_ktp_province_id` | Integer |  |
| `guarantor_ktp_sub_district_id` | Integer |  |
| `guarantor_marital_status` | Text |  |
| `guarantor_npwp_number` | Text |  |
| `guarantor_religion` | Text |  |
| `guarantor_residence_ownership` | Text |  |
| `guarantor_sub_district_id` | Integer |  |
| `guarantor_driver_license_card_file` | Text |  |
| `guarantor_family_card_file` | Text |  |
| `acquisition_channel` | Text |  |
| `acquisition_channel_other` | Text |  |
| `guarantor_proof_of_income_file_type` | Text |  |
| `guarantor_proof_of_residence_file_type` | Text |  |
| `guarantor_ktp_same_as_current_address` | Boolean |  |
| `student_ktp_same_as_current_address` | Boolean |  |
| `student_proof_of_residence_file_type` | Text |  |
| `reference_has_confirmed` | Boolean |  |
| `guarantor_privy_oauth_email` | Text |  |
| `guarantor_privy_oauth_mobile_number` | Text |  |
| `privy_oauth_email` | Text |  |
| `privy_oauth_mobile_number` | Text |  |
| `is_guarantor_mobile_number_match_with_pefindo` | Boolean |  |
| `is_mobile_number_match_with_pefindo` | Boolean |  |
| `is_pefindo_inquiry_triggered_within_30_days` | Boolean |  |
| `guarantor_ktp_file_skip_status` | Boolean |  |
| `ktp_file_skip_status` | Boolean |  |
| `guarantor_ktp_postal_code` | Text |  |
| `guarantor_last_educational_degree` | Text |  |
| `ktp_postal_code` | Text |  |
| `last_educational_degree` | Text |  |
| `borrower_employment_status_text` | Text |  |
| `borrower_npwp_number` | Text |  |
| `mothers_maiden_name` | Text |  |
| `borrower_number_of_dependents` | Integer |  |
| `borrower_average_annual_income` | Decimal |  |
| `borrower_nationality` | Text |  |
| `borrower_source_of_income` | Text |  |
| `guarantor_average_annual_income` | Decimal |  |
| `guarantor_nationality` | Text |  |
| `guarantor_source_of_income` | Text |  |
| `borrower_employment_status_id` | Integer |  |
| `guarantor_employment_status_id` | Integer |  |
| `guarantor_mothers_maiden_name` | Text |  |
| `corporate_type` | Text |  |
| `deed_of_establishment_date` | Date |  |
| `deed_of_establishment_number` | Text |  |
| `latest_deed_of_establishment_date` | Date |  |
| `latest_deed_of_establishment_number` | Text |  |
| `place_of_establishment` | Text |  |

#### `public.users_maxinstallmentbracket`

_Fields: 4_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `floor` | Decimal |  |
| `ceiling` | Decimal |  |
| `max_installment` | Decimal |  |

#### `public.users_phprofile`

_Fields: 51_

| Field | Type | Description |
|---|---|---|
| `profile_ptr_id` | Integer |  |
| `dorm_address` | Text |  |
| `guardian_address_line` | Text |  |
| `guardian_tenure` | Integer |  |
| `guardian_has_other_loans` | Boolean |  |
| `guardian_valid_id_file` | Text |  |
| `identity` | Text |  |
| `photo_file` | Text |  |
| `barangay` | Text |  |
| `guarantor_tin_number` | Text |  |
| `guarantor_sss_number` | Text |  |
| `marital_status` | Text |  |
| `student_mobile_number` | Text |  |
| `guarantor_source_of_income` | Text |  |
| `general_course` | Text |  |
| `segment` | Text |  |
| `acquisition_channel` | Text |  |
| `acquisition_channel_other` | Text |  |
| `guarantor_proof_of_income_file_type` | Text |  |
| `guarantor_proof_of_residence_file_type` | Text |  |
| `selfie_file` | Text |  |
| `selfie_file_status` | Text |  |
| `valid_id_file` | Text |  |
| `valid_id_file_status` | Text |  |
| `valid_id_file_type` | Text |  |
| `student_proof_of_residence_file_type` | Text |  |
| `guardian_marital_status` | Text |  |
| `first_name_verification_status` | Text |  |
| `last_name_verification_status` | Text |  |
| `guardian_first_name_verification_status` | Text |  |
| `guardian_last_name_verification_status` | Text |  |
| `deprecated_borrower_monthly_income` | Decimal |  |
| `deprecated_borrower_proof_of_income_file` | Text |  |
| `borrower_proof_of_income_file_type` | Text |  |
| `deprecated_borrower_business_address` | Text |  |
| `deprecated_borrower_business_name` | Text |  |
| `deprecated_borrower_industry_id` | Integer |  |
| `deprecated_borrower_job_start_date` | Date |  |
| `deprecated_borrower_position` | Text |  |
| `borrower_sss_number` | Text |  |
| `borrower_tin_number` | Text |  |
| `borrower_source_of_income` | Text |  |
| `deprecated_borrower_business_phone` | Text |  |
| `deprecated_borrower_tenure` | Integer |  |
| `deprecated_borrower_verified_monthly_income` | Decimal |  |
| `remitter_relationship_with_borrower` | Text |  |
| `remitter_relationship_with_guarantor` | Text |  |
| `is_borrower_pep` | Boolean |  |
| `is_borrower_related_to_pep` | Boolean |  |
| `is_guarantor_pep` | Boolean |  |
| `is_guarantor_related_to_pep` | Boolean |  |

#### `public.users_profile`

_Fields: 131_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `date_of_birth` | Date |  |
| `verification_level_1_status` | Text |  |
| `verification_level_1_notes` | Text |  |
| `address_line_1` | Text |  |
| `guardian_first_name` | Text |  |
| `guardian_last_name` | Text |  |
| `guardian_email` | Text |  |
| `guardian_mobile_number` | Text |  |
| `degree` | Text |  |
| `program` | Text |  |
| `verification_level_2_status` | Text |  |
| `verification_level_2_notes` | Text |  |
| `connected_to_facebook` | Boolean |  |
| `connected_to_instagram` | Boolean |  |
| `connected_to_twitter` | Boolean |  |
| `connected_to_linkedin` | Boolean |  |
| `verification_level_3_status` | Text |  |
| `verification_level_3_notes` | Text |  |
| `guarantor_business_name` | Text |  |
| `guarantor_business_address` | Text |  |
| `guarantor_monthly_income` | Decimal |  |
| `guarantor_proof_of_income_file` | Text |  |
| `guarantor_proof_of_residence_file` | Text |  |
| `verification_level_4_status` | Text |  |
| `verification_level_4_notes` | Text |  |
| `city_id` | Integer |  |
| `guardian_city_id` | Integer |  |
| `guardian_province_id` | Integer |  |
| `polymorphic_ctype_id` | Integer |  |
| `province_id` | Integer |  |
| `user_id` | Integer |  |
| `verification_level_5_notes` | Text |  |
| `verification_level_5_status` | Text |  |
| `address_line_2` | Text |  |
| `nearest_landmark` | Text |  |
| `status` | Text |  |
| `internal_notes` | Text |  |
| `facebook_url` | Text |  |
| `place_of_birth` | Text |  |
| `year_level` | Integer |  |
| `guarantor_first_name` | Text |  |
| `guarantor_last_name` | Text |  |
| `guarantor_email` | Text |  |
| `guarantor_mobile_number` | Text |  |
| `guarantor_type` | Text |  |
| `report_card_file` | Text |  |
| `gender` | Text |  |
| `guardian_gender` | Text |  |
| `is_employed` | Boolean |  |
| `guarantor_proof_of_income_file_status` | Text |  |
| `guarantor_proof_of_income_file_notes` | Text |  |
| `guarantor_proof_of_residence_file_status` | Text |  |
| `guarantor_proof_of_residence_file_notes` | Text |  |
| `guarantor_industry_id` | Integer |  |
| `guarantor_address` | Text |  |
| `guarantor_business_phone` | Text |  |
| `guarantor_city_id` | Integer |  |
| `guarantor_date_of_birth` | Date |  |
| `guarantor_gender` | Text |  |
| `guarantor_place_of_birth` | Text |  |
| `guarantor_position` | Text |  |
| `guarantor_province_id` | Integer |  |
| `guarantor_selfie_file` | Text |  |
| `guarantor_selfie_file_notes` | Text |  |
| `guarantor_selfie_file_status` | Text |  |
| `guarantor_tenure` | Integer |  |
| `instagram_url` | Text |  |
| `student_proof_of_residence_file` | Text |  |
| `student_proof_of_residence_file_notes` | Text |  |
| `student_proof_of_residence_file_status` | Text |  |
| `linkedin_url` | Text |  |
| `twitter_url` | Text |  |
| `is_eligible_to_apply_override` | Boolean |  |
| `is_eligible_to_apply_override_notes` | Text |  |
| `guardian_relationship_to_student` | Text |  |
| `guarantor_relationship_to_student` | Text |  |
| `revision_funnel_duration` | Integer |  |
| `guarantor_verified_monthly_income` | Decimal |  |
| `reference_1_full_name` | Text |  |
| `reference_1_mobile_number` | Text |  |
| `reference_1_relationship_to_student` | Text |  |
| `reference_2_full_name` | Text |  |
| `reference_2_mobile_number` | Text |  |
| `reference_2_relationship_to_student` | Text |  |
| `guarantor_job_start_date` | Date |  |
| `processor_id` | Integer |  |
| `additional_borrower_id_file` | Text |  |
| `additional_borrower_id_file_notes` | Text |  |
| `current_due_total` | Decimal |  |
| `date_due` | Date |  |
| `days_in_arrears` | Integer |  |
| `school_remaining_balance` | Decimal |  |
| `datetime_profile_check` | DateTimeWithLocalTZ |  |
| `is_integrated` | Boolean |  |
| `guardian_has_accepted_privacy_policy` | Boolean |  |
| `guardian_has_confirmed_identity` | Boolean |  |
| `valid_id_uploaded_by_guardian_file` | Text |  |
| `edd_reference_first_name` | Text |  |
| `edd_reference_mobile_number` | Text |  |
| `edd_reference_relationship_to_student` | Text |  |
| `edd_reference_email` | Text |  |
| `edd_reference_last_name` | Text |  |
| `datetime_sent_last_guardian_consent_sms` | DateTimeWithLocalTZ |  |
| `guarantor_proof_of_income_file_skip_status` | Boolean |  |
| `guarantor_selfie_file_skip_status` | Boolean |  |
| `selfie_file_skip_status` | Boolean |  |
| `datetime_deleted` | DateTimeWithLocalTZ |  |
| `is_deleted` | Boolean |  |
| `student_email` | Text |  |
| `date_start_rejection_count` | Date |  |
| `last_conversation_emotion` | Text |  |
| `last_conversation_hostility` | Text |  |
| `last_conversation_sentiment` | Text |  |
| `borrower_business_address` | Text |  |
| `borrower_business_name` | Text |  |
| `borrower_business_phone` | Text |  |
| `borrower_industry_id` | Integer |  |
| `borrower_job_start_date` | Date |  |
| `borrower_monthly_income` | Decimal |  |
| `borrower_position` | Text |  |
| `borrower_proof_of_income_file` | Text |  |
| `borrower_tenure` | Integer |  |
| `borrower_verified_monthly_income` | Decimal |  |
| `borrower_proof_of_income_file_skip_status` | Boolean |  |
| `primary_income_provider` | Text |  |
| `borrower_proof_of_income_id` | Integer |  |
| `guarantor_proof_of_income_id` | Integer |  |
| `nickname` | Text |  |
| `guarantor_nickname` | Text |  |
| `guarantor_relationship_to_student_other_data` | Text |  |

#### `public.users_profiletagbatch`

_Fields: 9_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `uuid` | UUID |  |
| `status` | Text |  |
| `profile_tag_file` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `datetime_deleted` | DateTimeWithLocalTZ |  |
| `datetime_ingested` | DateTimeWithLocalTZ |  |
| `error_file` | Text |  |

#### `public.users_riskrating`

_Fields: 8_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `reference_date` | Date |  |
| `tier` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `profile_id` | Integer |  |
| `decision` | Text |  |
| `rating` | Text |  |

#### `public.users_riskyprofile`

_Fields: 10_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `name` | Text |  |
| `date_of_birth` | Date |  |
| `id_number` | Text |  |
| `id_type` | Text |  |
| `id_type_notes` | Text |  |
| `place_of_birth` | Text |  |
| `general_notes` | Text |  |
| `name_order_eastern` | Boolean |  |
| `risk_level` | Text |  |

#### `public.users_user`

_Fields: 75_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `password` | Text |  |
| `last_login` | DateTimeWithLocalTZ |  |
| `is_superuser` | Boolean |  |
| `username` | Text |  |
| `first_name` | Text |  |
| `last_name` | Text |  |
| `email` | Text |  |
| `is_staff` | Boolean |  |
| `is_active` | Boolean |  |
| `date_joined` | DateTimeWithLocalTZ |  |
| `uuid` | UUID |  |
| `accept_terms_and_policy` | Boolean |  |
| `is_mobile_phone_verified` | Boolean |  |
| `origin` | Text |  |
| `level` | Integer |  |
| `aggregate_loan_performance_score` | Integer |  |
| `credit_limit` | Decimal |  |
| `school_id` | Integer |  |
| `batch_id` | Integer |  |
| `referred_by_id` | Integer |  |
| `type` | Text |  |
| `verified_level` | Integer |  |
| `erudifi_score` | Integer |  |
| `profile_application_score` | Integer |  |
| `institution_id` | Integer |  |
| `version` | Text |  |
| `is_test_account` | Boolean |  |
| `partner_role` | Text |  |
| `guarantor_total_approved_monthly_installment` | Decimal |  |
| `guarantor_total_outstanding_loan_amount` | Decimal |  |
| `user_total_active_loans` | Integer |  |
| `user_total_approved_monthly_installment` | Decimal |  |
| `user_total_loans` | Integer |  |
| `user_total_outstanding_loan_amount` | Decimal |  |
| `guarantor_active_total_exposure_value` | Decimal |  |
| `user_active_total_exposure_value` | Decimal |  |
| `lead_type` | Text |  |
| `overall_revision_funnel_duration` | Integer |  |
| `external_collection_agency_id` | Integer |  |
| `has_received_partnership_survey_invitation` | Boolean |  |
| `is_partner_profile_poc` | Boolean |  |
| `user_has_restructured_loan` | Boolean |  |
| `auto_reject_date_end` | Date |  |
| `reject_forever` | Boolean |  |
| `data_source` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `can_receive_otp_on_dev` | Boolean |  |
| `notes` | Text |  |
| `number_of_sent_sms` | Integer |  |
| `assisted_by_cs` | Boolean |  |
| `is_onboarding_modal_completed` | Boolean |  |
| `is_onboarding_modal_skip_later` | Boolean |  |
| `added_by_id` | Integer |  |
| `keycloak_id` | UUID |  |
| `entry_point` | Text |  |
| `platform_entry_point` | Text |  |
| `datetime_deleted` | DateTimeWithLocalTZ |  |
| `is_deleted` | Boolean |  |
| `datetime_accept_terms_and_policy` | DateTimeWithLocalTZ |  |
| `has_subsequent_loan_offer` | Boolean |  |
| `student_status` | Text |  |
| `lite` | Text |  |
| `lite_datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_email_verification_expiry` | DateTimeWithLocalTZ |  |
| `datetime_email_verification_sent` | DateTimeWithLocalTZ |  |
| `datetime_email_verified` | DateTimeWithLocalTZ |  |
| `email_verification_token` | Text |  |
| `last_otp_sent_at` | DateTimeWithLocalTZ |  |
| `google_account_id` | Text |  |
| `datetime_last_consented_to_share_data` | DateTimeWithLocalTZ |  |
| `is_whatsapp_available` | Boolean |  |
| `referrer_referral_code` | Text |  |
| `is_white_label_borrower_app` | Boolean |  |
| `borrower_type` | Text |  |

#### `public.users_user_groups`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `user_id` | Integer |  |
| `group_id` | Integer |  |

#### `public.users_user_partner_assignments`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `user_id` | Integer |  |
| `partner_id` | Integer |  |

#### `public.users_user_roles`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `user_id` | Integer |  |
| `adminrole_id` | Integer |  |

#### `public.users_user_user_permissions`

_Fields: 3_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `user_id` | Integer |  |
| `permission_id` | Integer |  |

#### `public.users_userrecommendedinstitution`

_Fields: 8_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `is_subscribe_notification` | Boolean |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `unlisted_institution_id` | Integer |  |
| `user_id` | Integer |  |
| `pic_mobile_number` | Text |  |
| `pic_name` | Text |  |
| `pic_position` | Text |  |

#### `public.users_userrelation`

_Fields: 16_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `is_guardian` | Boolean |  |
| `is_guarantor` | Boolean |  |
| `is_reference` | Boolean |  |
| `is_emergency_contact` | Boolean |  |
| `relationship` | Text |  |
| `other_relationship` | Text |  |
| `priority` | Integer |  |
| `verified` | Boolean |  |
| `verification_code` | Text |  |
| `verification_otp` | Text |  |
| `datetime_verification` | DateTimeWithLocalTZ |  |
| `active` | Boolean |  |
| `contact_id` | Integer |  |
| `user_id` | Integer |  |
| `verification_link` | Text |  |

#### `public.users_watchlistedprofilebatch`

_Fields: 9_

| Field | Type | Description |
|---|---|---|
| `id` | Integer |  |
| `file_hash` | Text |  |
| `status` | Text |  |
| `file` | Text |  |
| `datetime_created` | DateTimeWithLocalTZ |  |
| `datetime_updated` | DateTimeWithLocalTZ |  |
| `datetime_ingested` | DateTimeWithLocalTZ |  |
| `valid_entries` | Integer |  |
| `notes` | Text |  |
