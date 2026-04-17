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

## OpenCode AI Coding Agent

- OpenCode binary is **installed locally but not on PATH**
- Binary path: `~/.opencode/bin/opencode`
- OpenCode home/install dir: `~/.opencode`
- OpenCode config dir: `~/.config/opencode`
- Main config file: `~/.config/opencode/opencode.json`
- Local package metadata exists in both:
  - `~/.opencode/package.json`
  - `~/.config/opencode/package.json`
- Installed plugin dependency seen locally: `@opencode-ai/plugin@1.2.24`
- Current configured model: `azure/gpt-5.3-codex`
- Current configured provider: `azure`
- Current permissions in config:
  - `write = allow`
  - `edit = allow`
  - `bash = allow`
- Current config also includes MCP entries for:
  - `linear`
  - `sentry`
- Important: do **not** copy API keys/secrets from `~/.config/opencode/opencode.json` into workspace files or chat replies
- When using OpenCode directly, prefer the explicit binary path:
  - `~/.opencode/bin/opencode`
- If PATH convenience is needed later, add `~/.opencode/bin` to shell PATH instead of duplicating binaries
- Before future OpenCode troubleshooting, check these first:
  - binary presence at `~/.opencode/bin/opencode`
  - config at `~/.config/opencode/opencode.json`
  - whether shell PATH includes `~/.opencode/bin`

Add whatever helps you do your job. This is your cheat sheet.
