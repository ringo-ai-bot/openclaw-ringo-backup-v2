---
name: pr-writer
description: ALWAYS use this skill when creating or updating pull requests — never create or edit a PR directly without it. Trigger on any create PR, open PR, submit PR, make PR, update PR title, update PR description, edit PR, push and create PR, prepare changes for review task, or request for a PR writer.
---

# PR Writer

Create pull requests following Erudifi's engineering practices.

**Requires**: GitHub CLI (`gh`) authenticated and available.

## Prerequisites

Before creating a PR, ensure all changes are committed. If there are uncommitted changes, run the `skills:commit` skill first to commit them properly.

```bash
# Check for uncommitted changes
git status --porcelain
```

If the output shows any uncommitted changes (modified, added, or untracked files that should be included), invoke the `skills:commit` skill before proceeding.

## Process

### Step 1: Verify Branch State

```bash
# Detect the default branch — note the output for use in subsequent commands
gh repo view --json defaultBranchRef --jq '.defaultBranchRef.name'
```

```bash
# Check current branch and status (substitute the detected branch name above for BASE)
git status
git log BASE..HEAD --oneline
```

Ensure:
- All changes are committed
- Branch is up to date with remote
- Changes are rebased on the base branch if needed

### Step 2: Analyze Changes

Review what will be included in the PR:

```bash
# See all commits that will be in the PR (substitute detected branch name for BASE)
git log BASE..HEAD

# See the full diff
git diff BASE...HEAD
```

Understand the scope and purpose of all changes before writing the description.

### Step 3: Write the PR Description

Use this structure for PR descriptions (ignoring any repository PR templates):

```markdown
<optional person name that requesting the changes>

<optional linear ticket or sentry issue for reference>

<brief description of whats changed in the pull request>

<any additional context reviewers need>
```

**Do NOT include:**
- "Test plan" sections
- Checkbox lists of testing steps
- Redundant summaries of the diff

**Do include:**
- Clear explanation of what and why
- Links to relevant issues or tickets
- Context that isn't obvious from the code
- Notes on specific areas that need careful review

### Step 4: Create the PR

```bash
gh pr create --draft --title "[<scope>] <type>: <short description>" --body "$(cat <<'EOF'
<description body here>
EOF
)"
```

**Title format** follows commit conventions: `[<scope>] <type>: <short description>`
- Include scope in title when the changes is related to a linear ticket, use the linear ticket ID as scope value

## PR Description Examples

### Linear ticket PR

```markdown
**Requested by**: Ashil
**Linear ticket**: [OI-2885](<linear ticket URL>)

## Summary
- Add credit line auto-submit functionality when loan applications are submitted.
- Add Credit Line to Gubat nav bar.

## Changes
1. Admin Navigation Enhancement (PH Only)
- Added "Credit Line" tab to Django admin top navigation bar (between Loans and Partners)
- Includes shortcuts to Credit Lines and Data Snapshots admin pages
- Only added to Bukas (PH) admin, not Danacita (ID)
2. Auto-Submit Credit Line on Loan Submission
- When a loan application is submitted, automatically submit the borrower's credit line (if status = NEW)
- Copies proof of income files from loan app to credit line if missing:
  - borrower_proof_of_income_file from loan app
  - guarantor_proof_of_income_file from borrower's profile
- Non-blocking: Loan submission always succeeds regardless of credit line auto-submit outcome
- Gracefully handles users without credit lines or credit lines in other statuses
```

### Sentry Error PR

```markdown
**Requested by**: Setyo
**Sentry error**: <sentry issue URL>

## Summary
- Fix some Archived Admin Error (ArchivedUser, ArchivedIdProfile, ArchivedIdLoanApplication)
- Adjust display for `archived_loans_by_student_nik` and others
```

## Guidelines

- **One PR per feature/fix** - Don't bundle unrelated changes
- **Keep PRs reviewable** - Smaller PRs get faster, better reviews
- **Explain the why** - Code shows what; description explains why
- **Mark WIP early** - Use draft PRs for early feedback

## Editing Existing PRs

If you need to update a PR after creation, use `gh api` instead of `gh pr edit`:

```bash
# Update PR description
gh api -X PATCH repos/{owner}/{repo}/pulls/PR_NUMBER -f body="$(cat <<'EOF'
Updated description here
EOF
)"

# Update PR title
gh api -X PATCH repos/{owner}/{repo}/pulls/PR_NUMBER -f title='new: Title here'

# Update both
gh api -X PATCH repos/{owner}/{repo}/pulls/PR_NUMBER \
  -f title='new: Title' \
  -f body='New description'
```

Note: `gh pr edit` is currently broken due to GitHub's Projects (classic) deprecation.
