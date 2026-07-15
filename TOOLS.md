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

## GitHub

- GitHub username: `ringo-ai-bot`
- GitHub CLI auth (`gh`) is configured and working for this machine
- Preferred Git transport for GitHub repos: SSH
- GitHub SSH identity for this machine: `~/.ssh/id_ed25519_ringo`
- SSH public key label/comment: `ringo@erudifi.com`
- SSH config pins `github.com` to use `~/.ssh/id_ed25519_ringo`
- Verified SSH auth message: `Hi ringo-ai-bot! You've successfully authenticated, but GitHub does not provide shell access.`
- Verified repo access over SSH against Erudifi remotes
- Recommended git commit identity for this machine:
  - `user.name = Ringo AI Bot`
  - `user.email = ringo@erudifi.com`
- Use this account/setup as the default reference for future GitHub actions unless Ashil says otherwise

## Skill Creation

- When asked to create a skill, install/create it in the real skills directory if requested or appropriate
- Also **always mirror every created skill into the workspace** for durable backup/reference
- Workspace mirror location convention: `skills/<skill-name>/SKILL.md`
- Treat the workspace copy as the versioned backup/reference copy unless Ashil says otherwise
- If a skill is created outside the workspace, follow up by writing the mirrored workspace copy in the same turn

## OpenCode AI Coding Agent

- OpenCode is installed locally and **now available on PATH**
- Verified command resolution: `opencode` → `~/.opencode/bin/opencode`
- Verified version: `1.4.3`
- OpenCode home/install dir: `~/.opencode`
- OpenCode config dir: `~/.config/opencode`
- Main config file: `~/.config/opencode/opencode.json`
- Local package metadata exists in both:
  - `~/.opencode/package.json`
  - `~/.config/opencode/package.json`
- Installed plugin dependency seen locally: `@opencode-ai/plugin@1.2.24`
- Current configured model: `azure/gpt-5.6-terra`
- Current configured provider: `azure`
- Current permissions in config:
  - `write = allow`
  - `edit = allow`
  - `bash = allow`
- Current config also includes MCP entries for:
  - `linear`
  - `sentry`
- PATH convenience was added by appending this line to `~/.bashrc`:
  - `export PATH="$HOME/.opencode/bin:$PATH"`
- Important: do **not** copy API keys/secrets from `~/.config/opencode/opencode.json` into workspace files or chat replies
- Direct invocation options:
  - `opencode`
  - `~/.opencode/bin/opencode`
- **PTY / TTY requirement:** `opencode run` should be executed with a TTY/PTY in this environment
- OpenClaw execution rule for OpenCode:
  - set `pty=true` on `exec` calls that run OpenCode interactively or via `opencode run`
- Shell fallback wrappers when a PTY is needed:
  - `script -q -c '<command>' /dev/null`
  - `tmux` or another TTY-providing wrapper
- Reliable PTY validation pattern that worked here:
  - `script -q -c '~/.opencode/bin/opencode run "Respond with exactly OPENCODE_OK and nothing else."' /dev/null`
- Verified PTY validation result: `OPENCODE_OK`
- Before future OpenCode troubleshooting, check these first:
  - `command -v opencode`
  - `opencode --version`
  - config at `~/.config/opencode/opencode.json`
  - whether shell PATH includes `~/.opencode/bin`
  - whether the command was launched with a PTY
- Usage guidance:
  - Use **OpenCode** for heavier coding tasks where an autonomous coding agent can inspect, refactor, and iterate inside a repo
  - Use **direct workspace edits / shell** for small, surgical changes where spawning another coding flow would be slower than just doing the work
  - Use **ACP harness sessions** when the user explicitly asks for Codex / Claude Code / Cursor / Gemini-style harness behavior
  - For repo work that is ambiguous, still confirm the target repo first using `EPD_CODEBASES.md`
  - After OpenCode-driven repo edits, still review diffs, run relevant checks, and commit intentionally rather than trusting blind output

## Hourly `/data/code` sync

- Script: `/home/jesse/.openclaw/workspace/scripts/sync-codebases.sh`
- Cron job name: `Hourly codebase sync` (id: `885913c4-4844-49d1-8a5b-2bc73eea0e45`)
- Schedule: every `1h` via OpenClaw gateway cron (isolated, light-context, no Slack deliver)
- Behavior: fetches each top-level `/data/code/*` git repo; fast-forwards local `main`/`master` to `origin` without clobbering dirty or feature-branch checkouts
- Last-run log: `/home/jesse/.openclaw/workspace/memory/codebase-sync-last.json`
- Manual script run: `bash /home/jesse/.openclaw/workspace/scripts/sync-codebases.sh`
- Inspect job: `openclaw cron list` / `openclaw cron runs --id 885913c4-4844-49d1-8a5b-2bc73eea0e45`
- Force run now: `openclaw cron run 885913c4-4844-49d1-8a5b-2bc73eea0e45`

Add whatever helps you do your job. This is your cheat sheet.
