# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

## Slack thread parent

- Applies to **channel and DM** threads. DM replies with `threadId` are often folded into `slack:direct:<user>` and still need the parent fetch.
- Fetch **only** the parent with `message` `action=read`, `messageId=<threadId>`. `target` is the channel `C…` or DM `D…` / `user:U…`.
- `read` with `threadId` (no `messageId`) omits the parent on purpose.
- Outbound DMs sent from another person’s session are not copied into the recipient session; Slack parent read is the source of truth.
- Do **not** set `channels.slack.thread.inheritParent` — that copies the full channel transcript into every new thread session.
- Skill: `skills/slack-thread-parent/SKILL.md`

## Media

- Inbound attachments: `/home/jesse/.openclaw/media/inbound` (`~/.openclaw/media/inbound`)
- Outbound / generated deliverables: `/home/jesse/.openclaw/media/outbound` (`~/.openclaw/media/outbound`)
- Follow the `media-files` skill when generating or attaching files; do not leave finals in the workspace root

## GitHub

- GitHub username: `ringo-ai-bot`
- GitHub CLI auth (`gh`) is configured and working for this machine
- Preferred Git transport for GitHub repos: SSH
- GitHub SSH identity for this machine: `~/.ssh/id_ed25519_ringo`
- SSH public key label/comment: `ringo@erudifi.com`
- SSH config pins `github.com` to use `~/.ssh/id_ed25519_ringo`
- Verified SSH auth message: `Hi ringo-ai-bot! You've successfully authenticated, but GitHub does not provide shell access.`
- Verified repo access over SSH against Erudifi remotes
- Recommended git commit identity for this machine (host default; Clara owns coding delivery commits):
  - `user.name = Ringo AI Bot`
  - `user.email = ringo@erudifi.com`
- Ringo may **check** PRs and CI with `gh` (view, list, status, checks, read review comments).
- Coding delivery writes (create/update PRs, commits, push for shipping) belong to **Clara** — soft-redirect those requests.
- Use this account/setup as the default reference for GitHub **inspection** unless Ashil says otherwise

## Skill Creation

- When asked to create a skill, install/create it in the real skills directory if requested or appropriate
- Also **always mirror every created skill into the workspace** for durable backup/reference
- Workspace mirror location convention: `skills/<skill-name>/SKILL.md`
- Treat the workspace copy as the versioned backup/reference copy unless Ashil says otherwise
- If a skill is created outside the workspace, follow up by writing the mirrored workspace copy in the same turn

## Hourly `/data/code` sync

- Script: `/home/jesse/.openclaw/workspace/scripts/sync-codebases.sh`
- Cron job name: `Hourly codebase sync` (id: `885913c4-4844-49d1-8a5b-2bc73eea0e45`)
- Schedule: every `1h` via OpenClaw gateway cron (isolated, light-context, no Slack deliver)
- Behavior: fetches each top-level `/data/code/*` git repo; fast-forwards local `main`/`master` to `origin` without clobbering dirty or feature-branch checkouts
- Last-run log: `/home/jesse/.openclaw/workspace/memory/codebase-sync-last.json`
- Manual script run: `bash /home/jesse/.openclaw/workspace/scripts/sync-codebases.sh`
- Inspect job: `openclaw cron list` / `openclaw cron runs --id 885913c4-4844-49d1-8a5b-2bc73eea0e45`
- Force run now: `openclaw cron run 885913c4-4844-49d1-8a5b-2bc73eea0e45`

## Airflow (mono-pipeline)

- Skill: `airflow-mono-pipeline` (`.agents/skills/airflow-mono-pipeline/`, mirrored under `skills/`)
- Prod URL: `https://airflow.erudifi.com` (Airflow 2.7.2, REST `/api/v1`)
- DAG repo: `/data/code/mono-pipeline`
- Cloudflare Access: this host public IP `20.195.24.194` is allowlisted (service token not required while allowlist holds)
- Secret paths (do not commit or echo values):
  - `~/.openclaw/secrets/airflow-api-username.txt`
  - `~/.openclaw/secrets/airflow-api-password.txt`
- Helper: `python3 .agents/skills/airflow-mono-pipeline/scripts/airflow_api.py ...`
- DAG catalog: `.agents/skills/airflow-mono-pipeline/DAGS.md` (all `is_active` DAGs; refresh via `scripts/generate_dag_catalog.py`)
- Access: Trusted may read; Owner-only for trigger/clear/pause (`--confirm-write`)

Add whatever helps you do your job. This is your cheat sheet.
