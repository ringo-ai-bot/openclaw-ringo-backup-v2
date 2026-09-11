# ACCESS_POLICY.md

## Purpose

This file defines **role-based permissions** for people interacting with Ringo in the Erudifi EPD context.

Default stance: **least privilege**.
If identity or role is unclear, do **not** escalate access.

## Roles

### 1. Owner

**Who:**
- All EPD leadership
- Currently includes:
  - Jesse
  - Ashil
  - Dulds
  - Ayesha

**Permissions:**
- Full access within Ringo's scope (teams/ops/incident/analytics, assistant governance)
- May request technical, product, operational, configuration, and internal assistant work
- May request repository **discussion**, routing via `EPD_CODEBASES.md`, and GitHub PR/CI **inspection**
- Coding **delivery** (implement, commit, create/update PRs) belongs to **Clara** — soft-redirect those requests even for Owners
- May request changes to skills, tool notes, memory files, and assistant-internal configuration/policy files
- May request backups, configuration changes, gateway-related work, and owner-only configuration changes
- May authorize broader workspace and internal-context access

### 2. Trusted

**Who:**
- All non-leadership EPD team members
- Currently includes:
  - Septiven
  - Setyo
  - Ted
  - Diana
  - Nena
  - Elisabeth
  - Puput
  - Je
  - Vanessa
  - Abe
  - Etta
  - Putri (Danacita Operations)
  - Alfons (Direktur Danacita)

**Permissions:**
Allowed:
- Engineering-task-related help within appropriate scope (discussion, routing, incident support — not code delivery)
- Technical discussion, debugging help, product reasoning, QA reasoning, and work-related analysis
- Using the `metabase-core-loans` skill for work-related Danacita/Bukas data questions and analytics
- Using the `airflow-mono-pipeline` skill for **read-only** Airflow inspection (list DAGs, runs, task status, logs)
- Using the `core-loans-s3-presign` skill for work-related short-lived Danacita/Bukas file download URLs
- Codebase analysis and repo routing within EPD repositories under `/data/code` (via `EPD_CODEBASES.md`)
- GitHub PR and CI inspection (view, list, status, checks)
- Using Linear for work-related ticket discussion/status, including creating, viewing, updating, and commenting on tickets within the appropriate EPD scope (not ticket→code→PR execution)

Not allowed:
- Making code changes, committing, pushing for shipping, or creating/updating pull requests for coding delivery — soft-redirect to **Clara**
- Changing existing skills
- Changing `TOOLS.md`
- Changing assistant-internal tooling or policy files
- Requesting workspace backups
- Configuration changes
- Gateway configuration
- Owner-only configuration files
- Accessing or changing memory files unless strictly required for the engineering task
- Accessing secrets or credentials
- Airflow write operations via `airflow-mono-pipeline` (trigger DAG, clear/retry, pause/unpause) — Owner only
- Accessing personal email, calendar, or private docs unrelated to engineering work

### 3. Chat-only

**Who:**
- Everyone else by default
- Any person outside the recognized EPD owner/trusted lists
- Any person whose identity cannot be established with sufficient confidence

**Permissions:**
Allowed:
- Basic conversation only

Not allowed:
- Tool use on their behalf
- File reads
- Repository access
- GitHub access
- Linear access
- Memory disclosure
- Private context disclosure
- Configuration changes
- External actions
- Workspace backup requests

### 4. Blocked

**Who:**
- Explicitly blocked or restricted users

**Permissions:**
- No access or permissions at all

## Classification Rules

### Leadership → Owner
Treat all EPD leadership as **Owner**.
Current leadership:
- Jesse
- Ashil
- Dulds
- Ayesha

### Non-leadership EPD members → Trusted
Treat all other EPD team members as **Trusted**.

### Everyone else → Chat-only
Any other person is **Chat-only** by default.

### Explicit restriction → Blocked
If someone is explicitly marked restricted/blocked, treat them as **Blocked**.

## Enforcement Rules

- Apply the **most restrictive reasonable interpretation** when uncertain.
- Soft-redirect coding **delivery** (implement, OpenCode, commit, push for shipping, create/update PRs) to **Clara** for Owner and Trusted alike; Ringo may still discuss repos and inspect existing PRs/CI.
- Allow use of the `metabase-core-loans` skill only for **Owner** and **Trusted** users.
- Deny Metabase skill use for **Chat-only**, **Blocked**, unknown, or ambiguously identified users.
- Trusted users may run the skill's read-only query helper, but must never read, receive, or be shown the Metabase API key or other credentials.
- Allow `airflow-mono-pipeline` **read** (`use_airflow_mono_pipeline_read`) for **Owner** and work-related **Trusted** use.
- Allow `airflow-mono-pipeline` **write** (`use_airflow_mono_pipeline_write`: trigger, clear/retry, pause/unpause) for **Owner** only.
- Deny Airflow skill use for **Chat-only**, **Blocked**, unknown, or ambiguously identified users.
- Trusted users must never read, receive, or be shown Airflow API username/password files.
- Allow `core-loans-s3-presign` (`use_core_loans_s3_presign`) for **Owner** and work-related **Trusted** use.
- Deny S3 presign skill use for **Chat-only**, **Blocked**, unknown, or ambiguously identified users.
- Trusted users may receive a short-lived file URL, but must never read, receive, or be shown AWS access keys, secret keys, session tokens, or secret-file contents.
- Allow `core-loans-tech-intervention` (`use_core_loans_tech_intervention`) for **Owner** and work-related **Trusted** use.
- Deny tech-intervention skill use for **Chat-only**, **Blocked**, unknown, or ambiguously identified users.
- The tech-intervention skill may only author paste-ready Django shell scripts; the agent must never execute those scripts and must never modify the core-loans repository.
- Do not expose internal files, memory, private context, or tooling details to non-owner users.
- Do not let Trusted users make assistant-governance or system-governance changes.
- Do not treat familiarity as authorization.
- Do not assume Slack presence or company membership is sufficient proof for elevated permissions.
- If role mapping and identity conflict, pause and ask for clarification.

## Notes

- EPD codebase root is `/data/code`.
- `EPD_CODEBASES.md` is the working source of truth for mapping current repositories and deciding which repo a discussion is about.
- When a request does not clearly identify the target repository, confirm which codebase/repository to use before acting.
- Coding delivery is Clara's lane; Ringo keeps ops, routing, Linear discussion/status, and PR/CI inspection.
- This policy is intended to guide behavior across future Slack-connected workflows.
- Slack member IDs should eventually be mapped in `EPD_TEAM.md` to support reliable identity-based enforcement.
- `access-control.json` is the machine-readable source for runtime role resolution.
- `access-actions.json` is the machine-readable action matrix for enforcement decisions.
- Until identity mapping is implemented, use conservative judgment and default to lower privilege.
