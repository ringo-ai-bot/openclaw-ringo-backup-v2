---
name: "linear-ticket-workflow"
description: "Canonical hardened workflow for Linear-backed code and pull request work."
---

# Linear Ticket Workflow

Use this skill for authorized Linear-ticket code or pull-request work. It is mandatory whenever a recognizable Linear issue identifier is paired with implementation, bug-fix, repository-change, branch, commit, or PR intent.

## Scope and authorization

- Only proceed with repository, code, GitHub, or Linear state-changing actions for an authorized requester under workspace policy.
- Read `ACCESS_POLICY.md` as needed. When the target repository is unclear, read `EPD_CODEBASES.md`.
- Use the configured Linear MCP tools (`linear__*`) for ticket lookup, discussion, status-only changes, and planning-only requests; do not force this full workflow for those requests.
- Linear access is scoped to the **Erudifi** workspace. Before state changes, verify the target issue/project belongs to that workspace.
- MCP is the only Linear transport. Do not use a `linear` skill, `linear-cli.js`, `LINEAR_API_KEY`, direct GraphQL/REST calls, or any legacy Linear script.
- Permitted Linear mutations are creating/updating issues and creating comments. Do not attempt deletes, attachments, label administration, or document/project/initiative/milestone/release/status-update writes, even if a tool later becomes available; those require an explicit policy change.
- Do not begin code changes until the ticket, repository, and expected outcome are sufficiently clear to explain the plan.

## 1. Intake and preflight

1. Use `linear__get_issue` and related read-only `linear__*` MCP tools to fetch the issue, including description, acceptance criteria, linked work, discussions, labels, assignee, state, project/cycle, and existing PR links. Use `linear__list_comments` for discussions when needed.
2. Confirm the issue identifier, intended outcome, and affected repository. If the repository is ambiguous, identify candidates and ask before changing code.
3. Surface missing acceptance criteria, assumptions, dependencies, rollout implications, migration requirements, and risks. Ask concise clarification questions when they materially affect the implementation.
4. Before branching or handing work to OpenCode, verify:
   - the canonical repo path under `/data/code/<repo>` is accessible;
   - primary-checkout dirtiness, non-default branch, or other worktrees are noted as **context only** — never a reason to pause, stash, reset, switch branches, or ask to clear them; leave the primary checkout untouched and proceed via an isolated worktree;
   - the remote and actual default branch are known;
   - the matching GitHub repository is known;
   - likely validation commands and Docker support are discovered where relevant;
   - no existing branch or PR already implements the issue, unless the requested work is to continue it (in that case reuse that issue’s existing worktree/branch instead of creating a duplicate).
5. Once scope, repository, and plan are understood, use `linear__save_issue` to update Linear to **In Progress** if the workflow/state model supports it. Do not mark an issue Done just because a PR was opened.

## 2. Plan and working record

Create `/data/linear-plan/<ISSUE-ID>.md`. First verify that `/data/linear-plan/` exists or can be created and is writable.

The plan is a **supervisor-only** working record; update it with implementation evidence, validation, PR URL, and cleanup outcome before completing the workflow. Never instruct OpenCode to open, read, or update `/data/linear-plan/<ISSUE-ID>.md` — that path is outside the isolated worktree and will be denied. Before invoking OpenCode, the plan content used for implementation must already be complete enough to paste into the handoff.

Use this structure:

```md
# <ISSUE-ID> — <ticket title>

## Ticket facts
- Linear URL:
- Requested outcome:
- Acceptance criteria:

## Repository and base branch
- Repository:
- Remote/default branch:
- Worktree path:
- Issue branch:
- Base commit / default branch used:
- Existing work/PRs:

## Assumptions and open questions

## Proposed approach

## Affected files and systems

## Non-goals

## Risk, rollout, and migration notes

## Validation plan
- Focused test path(s) (module.Class.method):
- Docker context (danacita/bukas) and warm-stack notes (--keep-up / --keepdb):

- [ ] Preflight complete
- [ ] Worktree and issue branch created
- [ ] Implementation complete
- [ ] Diff reviewed
- [ ] Validation complete / skipped with reason
- [ ] Commit created and pushed
- [ ] Pull request created
- [ ] Linear updated
- [ ] Cleanup complete / blocker recorded

## Evidence and links
- Worktree path:
- Branch:
- Base commit / default branch used:
- Commit(s):
- Validation:
- Pull request:
- Cleanup:
```

Produce a short, credible plan before editing code. Include the impacted systems, focused validation, migration/config concerns, non-goals, and rollback/rollout concerns when applicable.

## 3. Branch and OpenCode implementation

1. Always isolate Linear issue work in a dedicated git worktree. Never implement in the primary checkout, and never switch branches, stash, reset, or discard changes there or in unrelated worktrees. Never implement directly on the default branch.
   - In the **canonical** repo (`/data/code/<repo>`), resolve the remote and actual default branch (`main`/`master` via `origin/HEAD`, falling back to `main`, then `master`).
   - Fetch the default branch tip. Derive the issue branch name from Erudifi conventions in the `create-branch` skill (`feat|fix|ref|chore|docs|misc/<issue-id-kebab>`, e.g. `feat/oi-1880`), including collision suffixes (`-2`, `-3`, …) when needed. **Do not** follow create-branch’s in-place rules (branch-from-current or `git checkout -b` in the primary tree).
   - Create the worktree and branch from the freshly updated remote default tip:

```bash
mkdir -p /data/code/.worktrees
git -C /data/code/<repo> fetch <remote> <default>
git -C /data/code/<repo> worktree add -b <type>/<issue-id> \
  /data/code/.worktrees/<repo>-<issue-id-kebab> \
  <remote>/<default>
```

   - If continuing an existing issue branch/PR, reuse that issue’s worktree/branch instead of creating a duplicate.
   - Hand OpenCode and all later commit/PR/validation steps the **worktree path**, not the primary checkout.
   - For `core-loans`, pass that worktree to `core-loans-docker` via `--repo`.
2. Act as OpenCode's supervisor. Do not directly make repository code changes unless the requester explicitly overrides this rule.
3. Do not start OpenCode until the embedded ticket scope is present and self-contained. Invoke OpenCode with a PTY in this environment and provide a structured handoff containing:
   - issue ID and Linear URL;
   - worktree path and issue branch;
   - the **full** plan body embedded inline in the prompt (ticket facts, acceptance criteria, proposed approach, affected files/systems, non-goals, risk/rollout/migration notes, validation plan, and any resolved assumptions) — OpenCode must not need to read `/data/linear-plan` or any other path outside the worktree;
   - explicit instruction to stay inside the worktree only — do not access `/data/linear-plan`, the primary checkout, or other paths outside the worktree;
   - explicit instruction to make the smallest complete change and preserve project conventions;
   - requirement to stop and surface blockers rather than guess;
   - focused validation requirements;
   - For `core-loans`, invoke `core-loans-docker` for all validation commands (with `--repo` pointing at the worktree). Follow that skill’s **multi-step ticket validation** pattern: warm once with `--keep-up up`, then `--keep-up --no-up` (+ `--keepdb` for tests) for reruns, and tear down once at cleanup — do not cold-start/tear-down the stack on every command;
   - rule not to run migrations against staging or production, deploy, or perform other external side effects without explicit approval.
4. OpenCode should use its RTK integration for concise routine command output, but must retain or recover precise raw diagnostics whenever filtered output is insufficient to troubleshoot a failure.
5. Allow targeted, evidence-driven investigation during implementation when it is needed to resolve blockers, validate OpenCode's approach, assess risk, or review unexpected changes. Do not expand scope into unrelated exploration/refactoring.
6. Review OpenCode's changed-file scope, `git diff`, `git status`, test/lint/typecheck output, dependency/config changes, and generated artifacts. Steer or reject drift, unrelated refactors, surprise dependency upgrades, secret exposure, or unsafe configuration changes.
7. Tests:
   - Do not add speculative tests solely to increase coverage.
   - Add or update focused tests when changed behavior, acceptance criteria, or regression risk warrants them.
   - If focused tests are not added where they might reasonably be expected, record why in the plan/PR.
   - When validating, run the **narrowest** failing/relevant test path first (`module.Class.method`), then widen only if needed. Prefer `--keepdb` when schema did not change.
   - Do not busy-poll background jobs with zero-timeout `process.poll` loops; use one blocking command or a single long wait.
8. Migrations and Docker:
   - Prefer repository-supported Docker workflows for local tests and migration validation (`core-loans-docker` for `core-loans`).
   - Only run migrations against explicitly approved local, development, or test environments.
   - For multi-command validation on `core-loans`, keep the compose stack warm for the ticket session (`--keep-up` / `--no-up`); tear down once in cleanup.
   - Record every container started specifically by this workflow; do not claim ownership of pre-existing/shared containers.
   - If Docker or migration validation is unavailable, record the reason.

Do not proceed until changes are applied, todos are completed or explicitly incomplete, the diff is reviewed, validation is run or skipped with reason, and the branch is ready for a commit.

## 4. Commit, pull request, and Linear updates

1. Use the `commit` skill for every commit.
2. Use the `github` skill to inspect repository and PR state.
3. Use the `pr-writer` skill to create or update the pull request; do not improvise a PR description.
4. The PR must clearly tie to the Linear issue and include problem, solution, acceptance-criteria evidence, validation, risk/rollout/migration notes, and known follow-ups.
5. Before reporting success, confirm the branch is pushed, the PR exists, and record its URL.
6. Update the plan record with worktree path, branch, base commit, commits, changed systems, validation evidence, PR URL, and known risks.
7. Use `linear__save_comment` to add the PR URL and a concise implementation/validation note. Follow the calling rules below. Use `linear__save_issue` to move the ticket to **In Review** only after the PR succeeds and the workflow/state model supports it.

### `linear__save_comment` calling rules

Pass only the fields you mean to use. Omit unused optional fields entirely — never send empty strings.

For a new issue comment, pass exactly:

```json
{ "issueId": "OI-1234", "body": "..." }
```

Do not include `id`, `projectId`, `initiativeId`, `documentId`, `milestoneId`, `parentId`, `statusUpdateId`, or `statusUpdateType` unless they are required for that specific action.

Known failure mode: sending `statusUpdateType` (e.g. `"project"`) with an empty or missing `statusUpdateId` fails with `` `statusUpdateType` is only valid together with `statusUpdateId` ``. Those fields are only for commenting on a status update, and both must be real values together. Issue comments must not set them.

## 5. Safe cleanup and definition of done

After confirming the PR exists:

1. Leave the primary checkout exactly as found. Never switch, discard, reset, stash, or overwrite uncommitted work there or in unrelated worktrees.
2. After PR success, remove only the workflow-owned issue worktree when safe (`git worktree remove` on that path). If it is dirty or locked, leave it unchanged and report the blocker. Never delete unrelated worktrees.
3. Stop only workflow-owned Docker containers that are still running (including any stack left up via `core-loans-docker --keep-up`). Never stop shared, pre-existing, or unidentified containers, and never remove containers unless explicitly asked.
4. The workflow is done only when the following have evidence or an explicit exception:
   - acceptance criteria mapped to implementation/validation evidence;
   - code changes and todo outcome recorded;
   - changed-file scope/diff reviewed;
   - focused validation run, or skipped with reason;
   - no unintended files, generated artifacts, dependency changes, or secret/config exposure remain;
   - commits pushed and PR URL recorded;
   - Linear updated appropriately;
   - plan updated with final evidence (including worktree path and cleanup outcome);
   - cleanup finished or its blockers reported.
5. Notify the requester with the PR link, a concise change/validation summary, remaining risks, and cleanup status.

## Companion tools and skills

- Configured Linear MCP (`linear__*`) — ticket details, linked context, permitted Linear updates
- `create-branch` — Erudifi branch **naming** conventions only; for this workflow, create the issue branch via **worktree from the remote default**, overriding create-branch’s in-place checkout / branch-from-current behavior
- `commit` — required commit workflow
- `github` — GitHub/PR inspection
- `pr-writer` — PR creation or updates
- `core-loans-docker` — required for all core-loans local validation (tests, migrations, scripts, formatters); pass the issue worktree with `--repo`; use warm-stack `--keep-up` / `--no-up` and focused `--keepdb` tests during iterative validation

## Enforcement routing rule

For any request containing a recognizable Linear issue identifier plus an intent to implement, fix, modify repository code, create a branch, commit, or create/update a PR, invoke `linear-ticket-workflow` before repository changes. Do not bypass it unless the requester explicitly narrows the request to ticket lookup, discussion, status-only work, or planning only.
