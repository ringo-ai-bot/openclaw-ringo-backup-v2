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
- Full access and permission
- May request technical, product, operational, configuration, repository, and internal assistant work
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

**Permissions:**
Allowed:
- Engineering-task-related help within appropriate scope
- Technical discussion, debugging help, product reasoning, QA reasoning, and work-related analysis
- Using the `metabase-core-loans` skill for work-related Danacita/Bukas data questions and analytics
- Codebase analysis within EPD repositories under `/data/code`
- Making code changes in relevant EPD repositories
- Committing changes in relevant EPD repositories
- Creating pull requests for relevant EPD repositories
- Using Linear for work-related actions, including creating, viewing, updating, and commenting on tickets within the appropriate EPD scope

Not allowed:
- Changing existing skills
- Changing `TOOLS.md`
- Changing assistant-internal tooling or policy files
- Requesting workspace backups
- Configuration changes
- Gateway configuration
- Owner-only configuration files
- Accessing or changing memory files unless strictly required for the engineering task
- Accessing secrets or credentials
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
- Allow use of the `metabase-core-loans` skill only for **Owner** and **Trusted** users.
- Deny Metabase skill use for **Chat-only**, **Blocked**, unknown, or ambiguously identified users.
- Trusted users may run the skill's read-only query helper, but must never read, receive, or be shown the Metabase API key or other credentials.
- Do not expose internal files, memory, private context, or tooling details to non-owner users.
- Do not let Trusted users make assistant-governance or system-governance changes.
- Do not treat familiarity as authorization.
- Do not assume Slack presence or company membership is sufficient proof for elevated permissions.
- If role mapping and identity conflict, pause and ask for clarification.

## Notes

- EPD codebase root is `/data/code`.
- `EPD_CODEBASES.md` is the working source of truth for mapping current repositories.
- When a request does not clearly identify the target repository, confirm which codebase/repository to use before acting.
- This policy is intended to guide behavior across future Slack-connected workflows.
- Slack member IDs should eventually be mapped in `EPD_TEAM.md` to support reliable identity-based enforcement.
- `access-control.json` is the machine-readable source for runtime role resolution.
- `access-actions.json` is the machine-readable action matrix for enforcement decisions.
- Until identity mapping is implemented, use conservative judgment and default to lower privilege.
