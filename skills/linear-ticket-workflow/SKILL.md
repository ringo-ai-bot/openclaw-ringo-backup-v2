---
name: linear-ticket-workflow
description: Work on Linear tickets inside a code repository from intake through implementation and PR creation. Use when an authorized owner or trusted user asks to "work on a Linear ticket", "implement a Linear ticket", "take ownership of a Linear ticket", or otherwise wants end-to-end execution for a specific Linear issue that requires clarification, planning, code changes, and a GitHub pull request.
---

# Linear Ticket Workflow

Use this skill to execute a Linear ticket end to end inside the correct repository.

## Authorization

Only proceed with code/repo/GitHub actions when the requester is authorized under workspace policy.

- Allow **Owner** users.
- Allow **Trusted** users.
- If the requester is **Chat-only** or authorization is unclear, stop and ask for clarification or decline the repo-changing action.

Read the workspace policy files only as needed:

- `ACCESS_POLICY.md` for permission rules
- `EPD_CODEBASES.md` when the target repository is unclear

## Workflow

Run these phases in order unless the user explicitly narrows the scope.

1. **Clarification / Information Gathering**
   - Use the `linear` skill to fetch the relevant Linear ticket details first.
   - Confirm the exact Linear ticket identifier and expected outcome.
   - Gather the ticket context, constraints, acceptance criteria, linked discussions, and affected repository.
   - Determine which repository the ticket maps to.
   - If the repository is ambiguous, identify candidate repos and confirm the target before changing code.
   - Verify that you have access to the target repository before planning implementation.
   - Ask the requester for clarification when any part of the ticket, expected behavior, constraints, or acceptance criteria is still unclear.
   - Surface missing information, hidden assumptions, dependencies, rollout concerns, and risk areas early.

2. **Planning**
   - Use the `linear` skill again during planning if you need to confirm ticket details, linked context, or status before implementation.
   - During planning, inspect enough of the codebase to determine the correct repository, identify likely impacted files or subsystems, and produce a credible implementation plan.
   - Beyond this planning-level inspection, do not do extra independent codebase investigation yourself during implementation unless the user explicitly asks.
   - Produce a short implementation plan before editing code.
   - Call out impacted files or subsystems, tests to update, migration or config concerns, and validation steps.
   - If the ticket is underspecified, state what can be done now versus what needs product or engineering clarification.
   - Create a temporary markdown planning file in `/data/linear-plan/` during this step.
   - Before writing the file, verify that `/data/linear-plan/` exists or can be created and that it is writable from the current environment.
   - Name the file with the Linear ticket / issue ID, for example `/data/linear-plan/OI-2931.md`.
   - Include the Linear ticket / issue ID in both the filename and the markdown content.
   - The planning file should contain the work/ticket context, implementation plan, todo list, and any other relevant notes.

3. **Code Changes Implementation**
   - Use the `create-branch` skill to create the ticket branch from the updated default branch.
   - Act as a supervisor for OpenCode during this phase.
   - Do not implement code changes directly in the repository yourself unless the user explicitly overrides this rule.
   - Use OpenCode for all repository code changes in this phase.
   - When invoking OpenCode from OpenClaw, remember that `opencode run` requires a PTY in this environment.
   - Pass the approved work plan to OpenCode using a structured handoff based on the planning file. The handoff should include:
     - Linear ticket / issue ID
     - repository path
     - planning file path in `/data/linear-plan/`
     - ticket context / problem summary
     - expected outcome
     - constraints and non-goals
     - impacted files or subsystems if already known
     - todo list / checklist
     - branch rule: update the repository default branch from remote first, then create a separate ticket branch from that freshly updated default branch
     - validation expectations, including Docker preference for tests or migrations when supported
     - instruction not to create new unit tests unless explicitly requested or clearly required by the ticket
     - instruction to stop and surface blockers or ambiguity instead of guessing
   - Before implementation starts, make sure the relevant repository default branch is up to date with the remote (for example `main` or `master`).
   - Perform Linear-ticket-related code changes in a separate branch, not directly on the default branch.
   - Create the ticket branch from the freshly updated default branch so implementation starts from the latest base.
   - Instruct OpenCode to make the smallest set of changes that fully satisfies the ticket.
   - Instruct OpenCode to preserve existing conventions, patterns, and architecture unless the ticket requires otherwise.
   - Monitor OpenCode progress, review its outputs and diffs, and steer it if the implementation drifts or misses requirements.
   - Do not create new unit tests by default unless the requester explicitly asks for them or the ticket clearly requires them.
   - If tests need to be run or migrations need to be created/applied as part of validation, prefer running them through Docker when the repository supports that workflow.
   - If Docker-based validation or migration execution is unavailable or fails due to environment limitations, clearly note that it was skipped and why.
   - Ensure OpenCode runs relevant tests, linters, or focused validation whenever practical.
   - Do not proceed to later workflow steps until all of these done criteria are satisfied or explicitly called out as incomplete:
     - code changes applied
     - todos completed or explicitly marked incomplete
     - diffs reviewed
     - validation run or skipped with reason
     - branch state is clean enough for commit / PR
   - Summarize what changed, what was verified, and any remaining risks.

4. **Creating GitHub Pull Request**
   - Use the `commit` skill for any git commit needed before opening the pull request.
   - Use the `github` skill when checking repository or pull request state on GitHub.
   - Prepare the branch and commit history cleanly.
   - Create or update the pull request with a clear title and body tied to the Linear ticket.
   - Include problem, solution, validation, and follow-up notes.
   - Use the `pr-writer` skill for creating or updating the pull request instead of improvising the PR text.
   - After successfully creating the pull request, notify the requester that the PR is ready and include the pull request link.

## Companion Skills Quick Cheat Sheet

- `linear` — read ticket details and clarify scope
- `create-branch` — create the ticket branch from the updated default branch
- `commit` — create commits using the required commit workflow
- `github` — inspect GitHub repository / PR state when needed
- `pr-writer` — create or update the pull request

## Working Rules

- Do not start coding before understanding the ticket well enough to explain the plan.
- Push back on weak requirements, missing acceptance criteria, or risky shortcuts.
- Prefer direct evidence from the repo, ticket, and linked context over assumptions.
- Keep the user updated at phase boundaries for longer tasks.
- If external side effects are needed beyond normal repo work, ask first when policy requires it.

Keep this skill lean. Add detailed playbooks, templates, and ticket/PR examples later in `references/` as the workflow hardens.
