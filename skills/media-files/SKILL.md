---
name: media-files
description: Store and attach agent-generated deliverables under OpenClaw outbound media. Use when generating, saving, exporting, or attaching files (PDF, images, docs, sample contracts, reports, exports); when the user asks for a file to download or send; or when writing MEDIA: replies.
---

# Media files

## Paths

| Role | Directory |
|------|-----------|
| Inbound (received) | `~/.openclaw/media/inbound` |
| Outbound (generated / to send) | `~/.openclaw/media/outbound` |

Absolute equivalents on this host:

- `/home/jesse/.openclaw/media/inbound`
- `/home/jesse/.openclaw/media/outbound`

## When to use outbound

**Write to outbound:** PDFs, images, exports, sample contracts, reports, or any file meant to share or send to the user.

**Do not write to outbound:** source code, skills, memory files, config, or normal workspace docs.

**Never** leave final deliverables in the workspace root (`~/.../workspace/*.pdf`, etc.).

## Workflow

1. Ensure the outbound directory exists:
   ```bash
   mkdir -p ~/.openclaw/media/outbound
   ```
2. Build intermediates anywhere convenient (often `/tmp/...`).
3. Place the **final** file at:
   ```text
   ~/.openclaw/media/outbound/<descriptive-name>.<ext>
   ```
   Use a stable, human-readable name (e.g. `LEND-3487-sample-tuition-contract.pdf`).
4. When sending in chat, attach with an absolute path:
   ```text
   MEDIA:/home/jesse/.openclaw/media/outbound/<descriptive-name>.<ext>
   ```

OpenClaw may still create UUID-suffixed delivery copies in the same outbound directory; that is expected. Your source of truth for the human-facing file remains the stable name you wrote.
