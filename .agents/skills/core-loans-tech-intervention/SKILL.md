---
name: core-loans-tech-intervention
description: >-
  Author paste-ready Django shell scripts for core-loans production tech
  interventions (data fixes, adjustments, backfills) in Danacita or Bukas.
  Use automatically when the user asks to create an intervention script, tech
  intervention, Django shell / manage.py shell script, or a CLI Python snippet
  to update or correct production core-loans data. Never execute the script and
  never modify the core-loans repository.
---

# core-loans tech intervention

Author **paste-ready Django shell scripts** for production data interventions
against `/data/code/core-loans`. The agent only writes the script in chat; the
human runs it.

## When to use

- User asks to "create an intervention script" or "tech intervention"
- User wants a Django shell / `manage.py shell` / `django-admin shell` snippet
- User needs a one-off production data fix, adjustment, correction, or backfill
  for core-loans / Danacita / Bukas
- User asks for a CLI Python script to update loans, applications, repayments,
  collections, partners, or related core-loans models in prod

## Access control (required)

Before drafting any script, resolve the requester through `access-control.json`
and enforce `use_core_loans_tech_intervention` in `access-actions.json`.

- **Owner**: allow.
- **Trusted**: allow for work-related intervention script authorship.
- **Chat-only**, **Blocked**, unknown, or ambiguous identity: deny.

## Hard rules (non-negotiable)

- **DO NOT execute any script.** Do not run the generated code, `manage.py`,
  `django-admin`, Django shell, Docker exec into prod, or any equivalent.
- **DO NOT make code changes in the core-loans repository.** No edits, patches,
  commits, file writes, or git operations under `/data/code/core-loans`.
- **Just create the requested script and return it to the user** in a
  copy-paste ready format.
- Read-only inspection of `/data/code/core-loans` models/settings is allowed
  so imports and field names are correct.
- Prefer explicit PKs / narrow filters. Never generate unbounded
  `Model.objects.all().update(...)` or similar.

## Context selection

Map the request when product context matters for models or assumptions:

- **Danacita / Indonesia / ID / DC** → Danacita
- **Bukas / Philippines / PH** → Bukas

**If you cannot tell which context the user means and it affects the script,
ask before drafting.** Do not guess.

## Workflow

Copy this checklist and track progress:

```
- [ ] 1. Enforce `use_core_loans_tech_intervention`
- [ ] 2. Resolve Danacita vs Bukas if needed
- [ ] 3. Confirm target entities/IDs and intended mutation
- [ ] 4. Read relevant Django models under /data/code/core-loans (read-only)
- [ ] 5. Author one paste-ready shell script using the mandatory template
- [ ] 6. Return the script + short run instructions only
```

### Step details

1. **Access** — deny early if role is insufficient.
2. **Scope** — get explicit IDs, fields, from→to values, and success criteria.
   If critical identifiers are missing, ask; do not invent production IDs.
3. **Models** — confirm model paths, field names, and related managers from
   `/data/code/core-loans` (read-only). Pair with `metabase-core-loans` only
   when a read-only lookup is needed first.
4. **Script** — follow the mandatory template below. Default `DRY_RUN = True`.
5. **Answer** — one fenced `python` block plus brief how-to-run notes. No repo
   diffs. Never claim the script was executed.

## Mandatory script template

Every intervention script must follow this shape (adapt imports/body; keep the
safety structure):

```python
from django.db import transaction

# --- config ---
DRY_RUN = True  # set False only after reviewing the dry-run output

# Explicit targets only (IDs / narrow filters)
TARGET_IDS = [...]  # fill from the request

# --- preview ---
qs = SomeModel.objects.filter(pk__in=TARGET_IDS)  # narrow filter
print("count:", qs.count())
for obj in qs:
    print("BEFORE", obj.pk, ...)  # relevant fields

if DRY_RUN:
    print("DRY_RUN=True — no writes performed")
else:
    with transaction.atomic():
        for obj in qs.select_for_update():
            # apply mutation
            obj.save(update_fields=[...])
            print("AFTER", obj.pk, ...)
    print("committed")
```

Required elements:

- `DRY_RUN = True` by default
- Print count and before-state for matched rows
- All writes inside `transaction.atomic()` when `DRY_RUN` is False
- Print after-state (or clear commit confirmation)
- Explicit PKs or equivalently narrow filters

## Response format

Return:

1. One copy-paste ready fenced `python` block (the full shell snippet).
2. Short run note, e.g. open a production shell with
   `python manage.py shell`, paste the snippet, review dry-run output, then
   set `DRY_RUN = False` and re-run only if correct.

Do not attach repo patches, do not write files into core-loans, and do not
execute anything.

## Intent mapping

| User ask | Action |
|---|---|
| “Create an intervention script to fix loan X status” | Draft DRY_RUN shell snippet for that loan PK |
| “Tech intervention: backfill field Y on these IDs” | Draft shell snippet with explicit ID list |
| “Django shell script to adjust repayment Z” | Draft paste-ready shell snippet |
| “Can you run this on prod?” | Refuse execution; return script for the human to run |
| “Commit this into core-loans” | Refuse repo changes; return chat script only |
