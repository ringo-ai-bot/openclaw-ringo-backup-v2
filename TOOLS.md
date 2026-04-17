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
- Current configured model: `azure/gpt-5.3-codex`
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
- Before future OpenCode troubleshooting, check these first:
  - `command -v opencode`
  - `opencode --version`
  - config at `~/.config/opencode/opencode.json`
  - whether shell PATH includes `~/.opencode/bin`
- Usage guidance:
  - Use **OpenCode** for heavier coding tasks where an autonomous coding agent can inspect, refactor, and iterate inside a repo
  - Use **direct workspace edits / shell** for small, surgical changes where spawning another coding flow would be slower than just doing the work
  - Use **ACP harness sessions** when the user explicitly asks for Codex / Claude Code / Cursor / Gemini-style harness behavior
  - For repo work that is ambiguous, still confirm the target repo first using `EPD_CODEBASES.md`
  - After OpenCode-driven repo edits, still review diffs, run relevant checks, and commit intentionally rather than trusting blind output

Add whatever helps you do your job. This is your cheat sheet.
