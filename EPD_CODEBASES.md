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
- Ownership hints below are inferred from repo structure, docs, branding, and module names unless explicit ownership metadata exists.

## Rich Repository Map

### atlas
- **Path:** `/data/code/atlas`
- **Origin:** `git@github.com:erudifi/atlas.git`
- **Branch seen:** `master`
- **Product/domain:** Borrower-facing web apps for Bukas (PH) and Danacita (ID); shared frontend monorepo
- **Classification:** Frontend monorepo
- **Language/framework:** TypeScript/JavaScript; Next.js + React + Turborepo + PNPM
- **Key entrypoints:** `package.json`, `bukas/package.json`, `danacita/package.json`, `bukas/next.config.js`, `danacita/next.config.js`, shared code in `libs/`
- **Likely ownership hints:** Borrower experience / product engineering / growth-facing frontend team
- **Notes:** README explicitly ties it to Danacita and Bukas; env names imply dependencies on backend, CMS/marketing, and GenAI services

### cic-loantape
- **Path:** `/data/code/cic-loantape`
- **Origin:** `git@github.com:erudifi/cic-loantape.git`
- **Branch seen:** `master`
- **Product/domain:** Loan tape export/API service for CIC reporting, encryption, and optional FTP upload
- **Classification:** Backend service / reporting utility
- **Language/framework:** Python; Flask + SQLAlchemy
- **Key entrypoints:** `app.py`, `loan_tape.py`, `models/`, `records/`
- **Likely ownership hints:** Finance / Ops / Compliance / Data Engineering
- **Notes:** Strongly specialized internal reporting service; handles GPG encryption and file export/upload flows

### core-loans
- **Path:** `/data/code/core-loans`
- **Origin:** `git@github.com:erudifi/core-loans.git`
- **Branch seen:** `feature/lend-3370`
- **Product/domain:** Primary monolithic lending backend serving admin, borrower app APIs, and partner APIs for Bukas and Danacita
- **Classification:** Backend monolith + workers
- **Language/framework:** Python; Django + DRF + Celery + Postgres + Redis
- **Key entrypoints:** `manage.py`, `app/wsgi.py`, `gunicorn.py`, domain modules under `loans/`, `payments/`, `partners/`, `credit_line/`, `e_kyc/`, `integrations/`, `notifications/`, adapters under `api/atlas`, `api/hooli`, `api/integration_app`
- **Likely ownership hints:** Core lending / platform backend team
- **Notes:** Looks like the central system of record for lending operations; many other repos likely depend on it

### findyouruni
- **Path:** `/data/code/findyouruni`
- **Origin:** `git@github.com:erudifi/findyouruni.git`
- **Branch seen:** `master`
- **Product/domain:** University/course matching or lead-generation web app
- **Classification:** Frontend web app
- **Language/framework:** TypeScript; Next.js 16 + React 19 + Tailwind
- **Key entrypoints:** `package.json`, `app/page.tsx`, `app/wizard/`, `lib/matching`, `lib/validation`, `data/courses.json`, `data/partners.json`
- **Likely ownership hints:** Growth / marketing / admissions-partnerships product team
- **Notes:** Domain inference is weaker because repo-level docs are thin; treat this mapping as medium confidence

### genai-service
- **Path:** `/data/code/genai-service`
- **Origin:** `git@github.com:erudifi/genai-service.git`
- **Branch seen:** `master`
- **Product/domain:** Generative AI platform for Erudifi customer-support and agent workflows across Bukas and Danacita
- **Classification:** Backend service + async workers
- **Language/framework:** Python; Django + Celery + Django Ninja + LangChain/PydanticAI + Postgres/pgvector + Redis
- **Key entrypoints:** `manage.py`, `genai_service/wsgi.py`, `genai_service/asgi.py`, agent logic in `jared/`, country modules in `bukas/` and `jared/danacita/`, integrations in `front/`, `qontak/`, `slack/`, `verifi/`
- **Likely ownership hints:** AI / automation / support tooling team
- **Notes:** Clear multi-agent and support-integration service; likely relevant for chat/agent workflow requests

### hooli
- **Path:** `/data/code/hooli`
- **Origin:** `git@github.com:erudifi/hooli.git`
- **Branch seen:** `master`
- **Product/domain:** Public marketing websites / homepage stack for Bukas and Danacita
- **Classification:** Full-stack web/CMS monolith
- **Language/framework:** Python + JavaScript; Django + Wagtail CMS + Celery + React/Webpack/Tailwind
- **Key entrypoints:** `manage.py`, `app/wsgi.py`, `package.json`, `webpack.config.js`, content apps like `blog/`, `help_center/`, `partner/`, `study_abroad/`, `course/`
- **Likely ownership hints:** Marketing / web / CMS team
- **Notes:** Explicitly positioned as the Bukas/Danacita website/homepage system

### integrations-app
- **Path:** `/data/code/integrations-app`
- **Origin:** `git@github.com:erudifi/integrations-app.git`
- **Branch seen:** `master`
- **Product/domain:** Payment/integration-facing web app, likely including embedded flows/widgets and partner-facing payment interactions
- **Classification:** Frontend web app
- **Language/framework:** TypeScript/JavaScript; Next.js 12 + React 18 + Tailwind + Parcel
- **Key entrypoints:** `package.json`, `next.config.js`, `src/pages`, `src/lite/widget.tsx`, `src/services`
- **Likely ownership hints:** Payments / integrations / product engineering team
- **Notes:** Hostnames and widget build suggest both full app and embeddable payment flow use cases

### mono-pipeline
- **Path:** `/data/code/mono-pipeline`
- **Origin:** `git@github.com:erudifi/mono-pipeline.git`
- **Branch seen:** `main`
- **Product/domain:** Data pipeline/orchestration repo for analytics, scheduled jobs, and data movement
- **Classification:** Data engineering platform / orchestration service
- **Language/framework:** Python; Apache Airflow + CeleryExecutor + Postgres + Redis
- **Key entrypoints:** `docker-compose.yaml`, `dags/`, `scripts/`, `codes/`
- **Likely ownership hints:** Data engineering / analytics engineering / BI
- **Notes:** DAG names suggest broad coverage: loanbooks, accounting, portfolio, OJK, partner dimensions, and reporting feeds

### partner-dashboard
- **Path:** `/data/code/partner-dashboard`
- **Origin:** `git@github.com:erudifi/partner-dashboard.git`
- **Branch seen:** `master`
- **Product/domain:** Partner-facing dashboard for Bukas/Danacita partners
- **Classification:** Frontend web app
- **Language/framework:** TypeScript; React + CRA/custom overrides + Ant Design
- **Key entrypoints:** `package.json`, `src/index.tsx`, `src/App.tsx`, `src/pages`, `src/services`
- **Likely ownership hints:** Partnerships / B2B product engineering
- **Notes:** Likely consumes APIs from `core-loans`

### prosperity
- **Path:** `/data/code/prosperity`
- **Origin:** `git@github.com:erudifi/prosperity.git`
- **Branch seen:** `fix/extend-rollover-window-to-d45`
- **Product/domain:** Investment/investor management platform covering investments, ledgers, organizations, payments, and users
- **Classification:** Backend web app / service
- **Language/framework:** Python; Django + likely DRF + Celery
- **Key entrypoints:** `manage.py`, `app/wsgi.py`, `app/asgi.py`, major domains in `investments/`, `investors/`, `ledgers/`, `payments/`, `organizations/`, `users/`
- **Likely ownership hints:** Investment / treasury / finance product team
- **Notes:** High-confidence investment-domain structure, but docs surfaced during scan were limited

### qa-automation
- **Path:** `/data/code/qa-automation`
- **Origin:** `git@github.com:erudifi/qa-automation.git`
- **Branch seen:** `master`
- **Product/domain:** Automated QA test suite spanning web, mobile, and load/browser flows
- **Classification:** QA / test automation repo
- **Language/framework:** JavaScript + Robot Framework + k6 scripting; Cypress + Robot Framework + k6/browser
- **Key entrypoints:** `cypress/cypress.config.js`, suites under `mobile/` and `web/`, performance/browser scripts under `k6Browser/`
- **Likely ownership hints:** QA / test engineering
- **Notes:** Useful when requests are about automation coverage, regression flows, or E2E investigation

### ralph-test
- **Path:** `/data/code/ralph-test`
- **Origin:** _none configured_
- **Branch seen:** `master`
- **Product/domain:** Minimal scratch/test repo
- **Classification:** Prototype / personal test repo
- **Language/framework:** Python; plain Python
- **Key entrypoints:** `hello.py`
- **Likely ownership hints:** Unclear; likely individual experimentation
- **Notes:** Too little structure to treat as a real product codebase

### sukat-backend
- **Path:** `/data/code/sukat-backend`
- **Origin:** `git@github.com:erudifi/sukat-backend.git`
- **Branch seen:** `main`
- **Product/domain:** Backend for Sukat, apparently an education/classroom/curriculum platform
- **Classification:** Backend service + workers
- **Language/framework:** Python; Django + Celery + DRF-style API structure
- **Key entrypoints:** `manage.py`, `config/wsgi.py`, `config/asgi.py`, domain apps in `apps/` including `assignments`, `classrooms`, `curriculum`, `schools`, `users`, `api`
- **Likely ownership hints:** Sukat product/backend team
- **Notes:** Looks like a separate product family from the Bukas/Danacita lending stack

### sukat-frontend
- **Path:** `/data/code/sukat-frontend`
- **Origin:** `git@github.com:erudifi/sukat-frontend.git`
- **Branch seen:** `master`
- **Product/domain:** Frontend for Sukat education/classroom platform
- **Classification:** Frontend web app
- **Language/framework:** TypeScript; Next.js + React
- **Key entrypoints:** `package.json`, `next.config.ts`, app code under `src/app`, shared UI in `src/components`, utilities in `src/lib`
- **Likely ownership hints:** Sukat product/frontend team
- **Notes:** Natural frontend pair to `sukat-backend`

## Separate / Non-EPD Utility Repos Under `/data/code`

These are present under the same filesystem root but should not be assumed to be current EPD product repos unless explicitly requested.

### openclaw
- **Path:** `/data/code/openclaw`
- **Origin:** `git@github.com:openclaw/openclaw.git`
- **Branch seen:** `main`
- **Product/domain:** OpenClaw personal AI assistant platform with multi-channel clients, gateway, skills, and UI
- **Classification:** Full-stack platform/monorepo
- **Language/framework:** TypeScript plus native/mobile code; Node.js monorepo + PNPM workspace + web UI + apps/extensions
- **Key entrypoints:** Root `package.json`, `src/`, `ui/package.json`, `apps/`, `extensions/`, `skills/`
- **Likely ownership hints:** OpenClaw core platform / open-source maintainers

### ringo / openclaw-analysis
- **Path:** `/data/code/ringo/openclaw-analysis`
- **Origin:** _not mapped as a normal repo root in the current scan_
- **Product/domain:** OpenClaw analysis/design documentation rather than a normal application codebase
- **Classification:** Research / documentation repo
- **Language/framework:** Markdown / docs
- **Key entrypoints:** `SUMMARY.md`, architecture docs, PRD, TODO-style documents
- **Likely ownership hints:** Architecture / research / product exploration

## Working Heuristics

- **Core lending stack:** `core-loans`, `atlas`, `partner-dashboard`, `hooli`, `integrations-app`, `genai-service`, `mono-pipeline`, `cic-loantape`
- **Investment / finance platform:** `prosperity`
- **QA / automation:** `qa-automation`
- **Education product family:** `sukat-backend`, `sukat-frontend`
- **Low-confidence / utility:** `findyouruni`, `ralph-test`, `openclaw`, `ringo/openclaw-analysis`

## Ambiguities to Confirm When Needed

- `findyouruni` has weak repo-level documentation; product/domain mapping is inferred from structure and data files
- `prosperity` appears investment-focused from structure, but surfaced docs were limited
- Ownership hints are mostly inferred; no strong CODEOWNERS-style source was found during the scan
- If a feature request could plausibly touch multiple repos, confirm the target repo instead of assuming the nearest-sounding name
