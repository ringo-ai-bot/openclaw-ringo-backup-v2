# core-loans S3 presign reference

## Purpose

This skill generates **short-lived S3 presigned GET URLs** for private
`core-loans` files in Danacita and Bukas.

## Storage model

`core-loans` stores Django `FileField` names, not signed URLs.

Typical DB value:

```text
e0877114-7f28-40e4-8054-47a1f7dfd043/e0877114-7f28-40e4-8054-47a1f7dfd043/i4vHvNJ-OnlWDVmSbH3sZ.jpeg
```

Production object key:

```text
core-loans/e0877114-7f28-40e4-8054-47a1f7dfd043/e0877114-7f28-40e4-8054-47a1f7dfd043/i4vHvNJ-OnlWDVmSbH3sZ.jpeg
```

## Context map

| Context | Bucket | Location | Region |
|---|---|---|---|
| `danacita` | `danacita-private` | `core-loans` | `ap-southeast-1` |
| `bukas` | `bukas-private` | `core-loans` | `ap-southeast-1` |

## Accepted inputs

The helper accepts:

- raw FileField names: `uuid/.../file.jpeg`
- keys with prefix: `core-loans/uuid/...`
- S3 URLs: `s3://bucket/key`
- HTTPS URLs: `https://bucket.s3.amazonaws.com/key?...`

Normalization rules:

1. `s3://bucket/key` uses the bucket from the URL directly.
2. HTTPS URLs use the bucket from the hostname when it matches S3 virtual-host
   patterns.
3. Bare FileField values are prefixed with the context location, usually
   `core-loans/`.

## Secret file

Create `~/.openclaw/secrets/aws-s3-presign.json` with mode `600`.

Preferred shape with separate credentials per context:

```json
{
  "aws_region": "ap-southeast-1",
  "contexts": {
    "danacita": {
      "bucket": "danacita-private",
      "location": "core-loans",
      "aws_access_key_id": "REPLACE_ME",
      "aws_secret_access_key": "REPLACE_ME",
      "role_arn": "arn:aws:iam::DC_ACCOUNT:role/ringo-s3-readonly",
      "external_id": "optional-if-required",
      "role_session_name": "openclaw-s3-presign-danacita"
    },
    "bukas": {
      "bucket": "bukas-private",
      "location": "core-loans",
      "aws_access_key_id": "REPLACE_ME",
      "aws_secret_access_key": "REPLACE_ME",
      "role_arn": "arn:aws:iam::BK_ACCOUNT:role/ringo-s3-readonly",
      "external_id": "optional-if-required",
      "role_session_name": "openclaw-s3-presign-bukas"
    }
  }
}
```

Fallback shape if both contexts later share the same base credentials:

```json
{
  "aws_region": "ap-southeast-1",
  "aws_access_key_id": "REPLACE_ME",
  "aws_secret_access_key": "REPLACE_ME",
  "role_arn": "arn:aws:iam::ACCOUNT:role/ringo-s3-readonly",
  "contexts": {
    "danacita": {
      "bucket": "danacita-private",
      "location": "core-loans"
    },
    "bukas": {
      "bucket": "bukas-private",
      "location": "core-loans"
    }
  }
}
```

Never paste real credentials into chat, Slack, git, or docs.

## IAM setup

### Preferred: STS AssumeRole

Use one access key pair per context, or a shared base credential if allowed,
where the base principal has only `sts:AssumeRole` on the readonly role.

Base principal policy example:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sts:AssumeRole",
      "Resource": [
        "arn:aws:iam::DC_ACCOUNT:role/ringo-s3-readonly",
        "arn:aws:iam::BK_ACCOUNT:role/ringo-s3-readonly"
      ]
    }
  ]
}
```

Readonly role policy example:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": [
        "arn:aws:s3:::danacita-private/core-loans/*",
        "arn:aws:s3:::bukas-private/core-loans/*"
      ]
    }
  ]
}
```

### Fallback: direct GetObject credentials

If AssumeRole is not available yet, the access key itself may carry the
`s3:GetObject` permissions above. This is less preferred because the credentials
are long-lived.

## Command examples

Presign a raw FileField value:

```bash
python3 .agents/skills/core-loans-s3-presign/scripts/presign.py \
  --context danacita \
  --key "e0877114-.../i4vHvNJ-OnlWDVmSbH3sZ.jpeg"
```

Resolve only, without calling AWS:

```bash
python3 .agents/skills/core-loans-s3-presign/scripts/presign.py \
  --context bukas \
  --key "https://bukas-private.s3.amazonaws.com/core-loans/example.pdf?Expires=123" \
  --dry-run
```

## Failure modes

- Missing secret file: owner setup required
- Missing context config: `danacita` or `bukas` not defined in secret JSON
- No AWS credentials: no configured key pair and no usable boto3 default chain
- STS failure: base principal cannot assume the configured role
- S3 presign failure: invalid bucket/key or denied access
