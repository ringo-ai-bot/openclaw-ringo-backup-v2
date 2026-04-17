# EPD_CODEBASES.md

Canonical map of current EPD code repositories under `/data/code`.

## Operating Rules

- Primary EPD code root: `/data/code`
- Owners and Trusted EPD users may ask for:
  - codebase analysis
  - feature/code discovery
  - code changes
  - commits
  - pull request creation on GitHub
- If a request does not clearly identify the right repository, confirm which codebase to use before making assumptions.
- Repository actions should stay scoped to the relevant repo unless the user explicitly asks for cross-repo work.

## Current Repository Map

- `atlas`
  - Path: `/data/code/atlas`
  - Default branch: `master`
  - Origin: `git@github.com:erudifi/atlas.git`

- `cic-loantape`
  - Path: `/data/code/cic-loantape`
  - Default/current branch: `master`
  - Origin: `git@github.com:erudifi/cic-loantape.git`

- `core-loans`
  - Path: `/data/code/core-loans`
  - Current branch: `feature/lend-3370`
  - Origin: `git@github.com:erudifi/core-loans.git`

- `findyouruni`
  - Path: `/data/code/findyouruni`
  - Default/current branch: `master`
  - Origin: `git@github.com:erudifi/findyouruni.git`

- `genai-service`
  - Path: `/data/code/genai-service`
  - Default/current branch: `master`
  - Origin: `git@github.com:erudifi/genai-service.git`

- `hooli`
  - Path: `/data/code/hooli`
  - Default/current branch: `master`
  - Origin: `git@github.com:erudifi/hooli.git`

- `integrations-app`
  - Path: `/data/code/integrations-app`
  - Default/current branch: `master`
  - Origin: `git@github.com:erudifi/integrations-app.git`

- `mono-pipeline`
  - Path: `/data/code/mono-pipeline`
  - Default/current branch: `main`
  - Origin: `git@github.com:erudifi/mono-pipeline.git`

- `partner-dashboard`
  - Path: `/data/code/partner-dashboard`
  - Default/current branch: `master`
  - Origin: `git@github.com:erudifi/partner-dashboard.git`

- `prosperity`
  - Path: `/data/code/prosperity`
  - Current branch: `fix/extend-rollover-window-to-d45`
  - Origin: `git@github.com:erudifi/prosperity.git`

- `qa-automation`
  - Path: `/data/code/qa-automation`
  - Default/current branch: `master`
  - Origin: `git@github.com:erudifi/qa-automation.git`

- `ralph-test`
  - Path: `/data/code/ralph-test`
  - Default/current branch: `master`
  - Origin: _none configured_

- `sukat-backend`
  - Path: `/data/code/sukat-backend`
  - Default/current branch: `main`
  - Origin: `git@github.com:erudifi/sukat-backend.git`

- `sukat-frontend`
  - Path: `/data/code/sukat-frontend`
  - Default/current branch: `master`
  - Origin: `git@github.com:erudifi/sukat-frontend.git`

## Non-EPD / Separate Utility Repos Present Under `/data/code`

These exist under the same root but should not be assumed to be EPD product repos unless explicitly requested:

- `openclaw` → `/data/code/openclaw`
- `ringo/openclaw-analysis` → `/data/code/ringo/openclaw-analysis`

## Notes

- This map is a discovery index, not a product/domain taxonomy yet.
- If needed later, enrich this file with product ownership, service boundaries, tech stack, and feature keywords for faster routing.
