#!/usr/bin/env python3
"""Generate short-lived S3 presigned GET URLs for core-loans files."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import boto3
from botocore.config import Config
from botocore.exceptions import BotoCoreError, ClientError

SECRET_PATH = Path.home() / ".openclaw" / "secrets" / "aws-s3-presign.json"
DEFAULT_REGION = "ap-southeast-1"
DEFAULT_EXPIRES = 600
MAX_EXPIRES = 900


def load_config(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise SystemExit(
            f"Secret file not found: {path}\n"
            "Owner setup required. Do not paste AWS credentials into chat."
        )
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in secret file: {path} ({exc})") from exc
    if not isinstance(data, dict):
        raise SystemExit(f"Secret file must contain a JSON object: {path}")
    return data


def get_context_config(config: dict[str, Any], context: str) -> dict[str, Any]:
    contexts = config.get("contexts")
    if not isinstance(contexts, dict):
        raise SystemExit("Secret file must define a 'contexts' object.")
    ctx = contexts.get(context)
    if not isinstance(ctx, dict):
        raise SystemExit(f"Context '{context}' not configured in {SECRET_PATH}.")
    return ctx


def first_nonempty(*values: Any) -> str | None:
    for value in values:
        if isinstance(value, str) and value.strip():
            return value.strip()
    return None


def normalize_key(raw: str, bucket: str, location: str) -> tuple[str, str]:
    value = raw.strip()
    if not value:
        raise SystemExit("Key/URL input is empty.")

    parsed = urlparse(value)
    if parsed.scheme == "s3":
        parsed_bucket = parsed.netloc.strip()
        parsed_key = parsed.path.lstrip("/")
        if not parsed_bucket or not parsed_key:
            raise SystemExit("Invalid s3:// URL; expected s3://bucket/key")
        return parsed_bucket, parsed_key

    if parsed.scheme in {"http", "https"}:
        host = parsed.netloc
        path = parsed.path.lstrip("/")
        if not path:
            raise SystemExit("HTTPS URL does not contain an object path.")
        virtual_host_suffixes = (
            ".s3.amazonaws.com",
            ".s3.ap-southeast-1.amazonaws.com",
        )
        for suffix in virtual_host_suffixes:
            if host.endswith(suffix):
                return host[: -len(suffix)], path
        return bucket, path

    key = value.lstrip("/")
    location = location.strip("/")
    if location and key != location and not key.startswith(location + "/"):
        key = f"{location}/{key}"
    return bucket, key


def build_session(
    config: dict[str, Any], context_config: dict[str, Any], region: str
) -> boto3.session.Session:
    access_key = first_nonempty(
        context_config.get("aws_access_key_id"), config.get("aws_access_key_id")
    )
    secret_key = first_nonempty(
        context_config.get("aws_secret_access_key"),
        config.get("aws_secret_access_key"),
    )
    session_token = first_nonempty(
        context_config.get("aws_session_token"), config.get("aws_session_token")
    )

    if access_key and secret_key:
        return boto3.Session(
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            aws_session_token=session_token,
            region_name=region,
        )

    # Fallback to the default boto3 chain if the host is configured later.
    return boto3.Session(region_name=region)


def assume_role_session(
    base_session: boto3.session.Session,
    region: str,
    role_arn: str,
    external_id: str | None,
    role_session_name: str,
) -> boto3.session.Session:
    sts = base_session.client("sts", region_name=region)
    kwargs: dict[str, Any] = {
        "RoleArn": role_arn,
        "RoleSessionName": role_session_name,
    }
    if external_id:
        kwargs["ExternalId"] = external_id
    try:
        response = sts.assume_role(**kwargs)
    except (BotoCoreError, ClientError) as exc:
        raise SystemExit(f"Failed to assume role: {exc}") from exc

    creds = response["Credentials"]
    return boto3.Session(
        aws_access_key_id=creds["AccessKeyId"],
        aws_secret_access_key=creds["SecretAccessKey"],
        aws_session_token=creds["SessionToken"],
        region_name=region,
    )


def verify_credentials(session: boto3.session.Session, region: str) -> None:
    try:
        session.client("sts", region_name=region).get_caller_identity()
    except (BotoCoreError, ClientError) as exc:
        raise SystemExit(f"No usable AWS credentials found: {exc}") from exc


def generate_url(
    session: boto3.session.Session, region: str, bucket: str, key: str, expires: int
) -> str:
    client = session.client(
        "s3",
        region_name=region,
        endpoint_url=f"https://s3.{region}.amazonaws.com",
        config=Config(signature_version="s3v4"),
    )
    try:
        return client.generate_presigned_url(
            "get_object",
            Params={"Bucket": bucket, "Key": key},
            ExpiresIn=expires,
        )
    except (BotoCoreError, ClientError) as exc:
        raise SystemExit(f"Failed to generate presigned URL: {exc}") from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate short-lived S3 GET presigned URLs for core-loans files."
    )
    parser.add_argument(
        "--context",
        "-c",
        choices=["danacita", "bukas"],
        required=True,
        help="Which product context to use.",
    )
    parser.add_argument(
        "--key",
        "-k",
        required=True,
        help="FileField value, object key, s3:// URL, or HTTPS S3 URL.",
    )
    parser.add_argument(
        "--expires",
        "-e",
        type=int,
        default=DEFAULT_EXPIRES,
        help=f"Expiry in seconds (default {DEFAULT_EXPIRES}, max {MAX_EXPIRES}).",
    )
    parser.add_argument(
        "--secret-file",
        default=str(SECRET_PATH),
        help="Path to aws-s3-presign.json (default: ~/.openclaw/secrets/aws-s3-presign.json).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Resolve bucket/key/role without calling AWS.",
    )
    parser.add_argument(
        "--format",
        choices=["json"],
        default="json",
        help="Output format.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    expires = max(1, min(args.expires, MAX_EXPIRES))

    config = load_config(Path(args.secret_file).expanduser())
    context_config = get_context_config(config, args.context)

    region = first_nonempty(
        context_config.get("aws_region"),
        config.get("aws_region"),
        DEFAULT_REGION,
    )
    bucket = first_nonempty(context_config.get("bucket"))
    location = first_nonempty(context_config.get("location"), "")
    if not bucket:
        raise SystemExit(f"Context '{args.context}' is missing 'bucket'.")

    role_arn = first_nonempty(context_config.get("role_arn"), config.get("role_arn"))
    external_id = first_nonempty(
        context_config.get("external_id"), config.get("external_id")
    )
    role_session_name = first_nonempty(
        context_config.get("role_session_name"),
        config.get("role_session_name"),
        f"openclaw-s3-presign-{args.context}",
    )

    resolved_bucket, resolved_key = normalize_key(args.key, bucket, location or "")

    payload: dict[str, Any] = {
        "context": args.context,
        "bucket": resolved_bucket,
        "key": resolved_key,
        "region": region,
        "expires_in": expires,
        "used_assume_role": bool(role_arn),
    }
    if role_arn:
        payload["role_arn"] = role_arn

    if args.dry_run:
        json.dump(payload, sys.stdout, indent=2)
        sys.stdout.write("\n")
        return

    base_session = build_session(config, context_config, region)
    verify_credentials(base_session, region)
    session = base_session
    if role_arn:
        session = assume_role_session(
            base_session=base_session,
            region=region,
            role_arn=role_arn,
            external_id=external_id,
            role_session_name=role_session_name,
        )

    url = generate_url(
        session=session,
        region=region,
        bucket=resolved_bucket,
        key=resolved_key,
        expires=expires,
    )
    payload["url"] = url
    payload["expires_at"] = (
        datetime.now(UTC) + timedelta(seconds=expires)
    ).isoformat()
    json.dump(payload, sys.stdout, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
