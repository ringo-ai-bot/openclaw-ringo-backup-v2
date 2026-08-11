---
name: core-loans-s3-presign
description: >-
  Generate short-lived S3 download URLs for private core-loans FileField values
  in Danacita or Bukas. Use automatically when the user asks to retrieve, open,
  download, share, or refresh any private core-loans file or document,
  including loan application files, guarantor KTP or valid ID files, selfie
  files, `contract_file`, `riplay_file`, lender agreement files, and other
  core-loans FileField-backed documents.
---

# core-loans S3 presign

Generate **short-expiry presigned GET URLs** for private files stored by
`/data/code/core-loans`.

## When to use

- User asks to retrieve or open any core-loans file related to a borrower, loan,
  loan application, guarantor, contract, RIPLAY, or KYC document
- User already has a FileField value like `uuid/.../file.jpeg`
- User has a full/expired S3 URL and needs a fresh one
- User wants a download link for `contract_file`, `riplay_file`, KYC files, or
  similar private documents
- User mentions file fields like `guarantor_ktp_file`,
  `guarantor_selfie_file`, `valid_id_file`, `selfie_file`,
  `lender_agreement_file`, or similar document columns
- User wants to look up a file field in Metabase, then open it

## Access control (required)

Before using the helper, resolve the requester through `access-control.json` and
enforce `use_core_loans_s3_presign` in `access-actions.json`.

- **Owner**: allow.
- **Trusted**: allow for work-related file access help.
- **Chat-only**, **Blocked**, unknown, or ambiguous identity: deny.
- Trusted users may receive the short-lived URL, but must never read or inspect
  secret files or raw credentials.

## Configuration

| Item | Value |
|---|---|
| Secret file | `~/.openclaw/secrets/aws-s3-presign.json` |
| Region default | `ap-southeast-1` |
| Contexts | `danacita`, `bukas` |
| Helper script | `.agents/skills/core-loans-s3-presign/scripts/presign.py` |
| Schema source | `/data/code/core-loans` |

Never print, log, or commit AWS credentials. Treat signed URLs as sensitive and
short-lived.

## Context selection (required)

Map the request to a product context:

- **Danacita / Indonesia / ID / DC** → `--context danacita`
- **Bukas / Philippines / PH** → `--context bukas`

**If you cannot tell which context the user means, ask before presigning.**
Do not guess.

## Workflow

Copy this checklist and track progress:

```
- [ ] 1. Resolve Danacita vs Bukas
- [ ] 2. Enforce `use_core_loans_s3_presign`
- [ ] 3. Get the file value or S3 URL from the user, or look it up with `metabase-core-loans`
- [ ] 4. Run `scripts/presign.py`
- [ ] 5. Return the signed URL and clearly state its expiry
```

### Step details

1. **Context** — see above.
2. **Input** — the helper accepts:
   - raw FileField names like `uuid/.../file.jpeg`
   - keys with location prefix like `core-loans/uuid/...`
   - `s3://bucket/key`
   - full S3 HTTPS URLs, even if expired
3. **Metabase pairing** — if the user needs a DB lookup first, use
   [../metabase-core-loans/SKILL.md](../metabase-core-loans/SKILL.md) to fetch
   the file-field value, then presign that result.
4. **Run**:

```bash
python3 .agents/skills/core-loans-s3-presign/scripts/presign.py \
  --context danacita \
  --key "e0877114-.../i4vHvNJ-OnlWDVmSbH3sZ.jpeg"
```

Dry-run without calling AWS:

```bash
python3 .agents/skills/core-loans-s3-presign/scripts/presign.py \
  --context bukas \
  --key "core-loans/uuid/file.pdf" \
  --dry-run
```

Useful flags:
- `--expires SECONDS` default `600`, max `900`
- `--format json` for machine-readable output

5. **Answer** — return only the signed URL, context, object key, and expiry.
   Do not dump credentials, secret-file contents, or unrelated object metadata.

## Safety rules

- Presign **GET only**. Do not add upload/write support.
- Never echo key IDs, secrets, or secret-file contents.
- Reject expiry values above 900 seconds.
- If the helper reports a missing secret file, tell the user owner setup is
  required; do not ask them to paste credentials into chat.
- Do not store signed URLs in memory files, plans, or long-lived notes.

## Intent mapping

| User ask | Action |
|---|---|
| “Get the guarantor KTP file from this loan application” | Look up the file field if needed, then presign it |
| “Give me the S3 URL for this `contract_file`” | Presign the file field |
| “This S3 link expired, refresh it” | Parse URL → presign same object |
| “Find borrower X’s `riplay_file` and share it” | Use `metabase-core-loans` to look up the field, then presign |
| “Can you open this KYC file?” | Presign first, then share the short-lived URL |

## Scripts

| Script | Purpose |
|---|---|
| `scripts/presign.py` | Parse input, load per-context credentials, optionally assume role, and generate presigned GET URLs |

## Additional resources

- [reference.md](reference.md) — secret file format, IAM policy, parsing rules
- `core-loans` Django settings: `/data/code/core-loans/app/settings.py`
- `core-loans` upload path helpers: `/data/code/core-loans/loans/file_fields.py`
