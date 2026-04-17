# EPD Codebases Enriched Draft

## atlas
- **Product/domain:** Borrower-facing web apps for Bukas (PH) and Danacita (ID); shared frontend monorepo.
- **Classification:** Frontend monorepo
- **Language/framework:** TypeScript/JavaScript; Next.js + React + Turborepo + PNPM
- **Key entrypoints:** Root: `package.json`; apps: `bukas/package.json`, `danacita/package.json`, `bukas/next.config.js`, `danacita/next.config.js`; shared UI in `libs/`.
- **Likely ownership hints:** Likely Growth/Product Engineering for borrower web/mobile-web experiences; Erudifi/Bukas/Danacita branding in README.
- **Notes / dependencies:** README explicitly says it serves Danacita and Bukas. Turbo envs mention `API_URL`, `WAGTAIL_API_URL`, `MARKETING_SERVICE_BASE_URL`, `GEN_AI_API_URL`, suggesting dependency on backend, website CMS, marketing, and genai services.

## cic-loantape
- **Product/domain:** Loan tape export/API service for CIC reporting, encryption, and optional FTP upload.
- **Classification:** Backend service / reporting utility
- **Language/framework:** Python; Flask + SQLAlchemy
- **Key entrypoints:** `app.py` (container CMD), `loan_tape.py`; models in `models/`, record mapping in `records/`, dump tooling via `flask makedump`.
- **Likely ownership hints:** Likely Finance/Ops/Compliance or Data Engineering supporting CIC regulatory reporting; README says ask Ted for creds.
- **Notes / dependencies:** Handles GPG encryption, Athena/BigQuery-style data access, CSV/XLSX/GPG output, and FTP upload. Strongly specialized internal service.

## core-loans
- **Product/domain:** Primary monolithic lending backend serving Gubat Admin, Borrower App APIs, and Partner Dashboard APIs for Bukas and Danacita.
- **Classification:** Backend monolith + workers
- **Language/framework:** Python; Django + DRF + Celery + Postgres + Redis
- **Key entrypoints:** `manage.py`, `app/wsgi.py`, `gunicorn.py`; key domains under `loans/`, `payments/`, `partners/`, `credit_line/`, `e_kyc/`, `integrations/`, `notifications/`; API adapters under `api/atlas`, `api/hooli`, `api/integration_app`.
- **Likely ownership hints:** Core lending/platform/backend team. Ownership hints split by domain modules; supports Bukas and Danacita country variants.
- **Notes / dependencies:** This appears to be the central system of record for lending operations. Docker compose includes country-specific backends plus Celery workers/beat and MinIO/S3-compatible storage.

## findyouruni
- **Product/domain:** University/course matching or lead-generation web app.
- **Classification:** Frontend web app
- **Language/framework:** TypeScript; Next.js 16 + React 19 + Tailwind
- **Key entrypoints:** `package.json`, `app/page.tsx`, `app/wizard/`, matching logic under `lib/matching`, validation under `lib/validation`, data in `data/courses.json` and `data/partners.json`.
- **Likely ownership hints:** Likely growth/marketing or admissions-partnerships team; repo is standalone and product-oriented rather than platform-oriented.
- **Notes / dependencies:** README is generic create-next-app, so product/domain inference comes mostly from folder names and local data files.

## genai-service
- **Product/domain:** Generative AI platform for Erudifi customer-support/agent workflows across Bukas and Danacita.
- **Classification:** Backend service + async workers
- **Language/framework:** Python; Django + Celery + Django Ninja + LangChain/PydanticAI + Postgres/pgvector + Redis
- **Key entrypoints:** `manage.py`, `genai_service/wsgi.py`, `genai_service/asgi.py`; agent logic in `jared/`, country modules in `bukas/` and `jared/danacita/`, channels/integrations in `front/`, `qontak/`, `slack/`, `verifi/`.
- **Likely ownership hints:** AI/automation team, likely customer support automation owners; “Jared” and “Dewi” agent naming suggests internal agent product ownership.
- **Notes / dependencies:** README clearly documents orchestration, help-center vector indexing, smoke tests against Front/Qontak/providers, and multi-agent pipelines.

## hooli
- **Product/domain:** Public marketing websites / homepage stack for Bukas and Danacita, formerly website_v3.
- **Classification:** Full-stack web/CMS monolith
- **Language/framework:** Python + JavaScript; Django + Wagtail CMS + Celery + React/Webpack/Tailwind
- **Key entrypoints:** `manage.py`, `app/wsgi.py`, frontend asset pipeline via root `package.json` and `webpack.config.js`; content apps include `blog/`, `help_center/`, `partner/`, `study_abroad/`, `course/`.
- **Likely ownership hints:** Marketing/web/CMS team; README explicitly says Bukas and Danacita www homepage.
- **Notes / dependencies:** Country-specific website containers (`website_bukas`, `website_danacita`) plus CMS/admin workflows, fixtures, and translation support.

## integrations-app
- **Product/domain:** Payment/integration-facing web app for Bukas and Danacita, likely embedded flows/widgets and partner-facing payment interactions.
- **Classification:** Frontend web app
- **Language/framework:** TypeScript/JavaScript; Next.js 12 + React 18 + Tailwind + Parcel (widget build)
- **Key entrypoints:** `package.json`, `next.config.js`, pages under `src/pages`, lightweight widget at `src/lite/widget.tsx`, services under `src/services`.
- **Likely ownership hints:** Payments/integrations/product engineering team. README hostnames use `pay.bukas.localhost` and `pay.danacita.localhost`.
- **Notes / dependencies:** Has dual-country env files and a separate parcel-built widget, suggesting both full app and embeddable/payment widget use cases.

## mono-pipeline
- **Product/domain:** Company data pipeline/orchestration repo for analytics, BigQuery/Athena jobs, and scheduled data movement.
- **Classification:** Data engineering service / orchestration platform
- **Language/framework:** Python; Apache Airflow + CeleryExecutor + Postgres + Redis
- **Key entrypoints:** `docker-compose.yaml`, DAGs in `dags/`, scripts in `scripts/`, helper code in `codes/`; many DAG names reference Bukas/Danacita loanbooks, accounting, portfolio, OJK, partner dimensions.
- **Likely ownership hints:** Data engineering / analytics engineering / BI.
- **Notes / dependencies:** Very broad operational coverage across portfolio, accounting, raw data syncs, and regulatory/partner datasets.

## openclaw
- **Product/domain:** OpenClaw personal AI assistant platform with multi-channel clients, gateway, skills, and UI.
- **Classification:** Full-stack platform/monorepo
- **Language/framework:** TypeScript plus Swift/mobile platform code; Node.js monorepo + PNPM workspace; web UI/Vite; mobile apps; extensions
- **Key entrypoints:** Root `package.json`, `src/` for gateway/CLI/core, `ui/package.json` for frontend, native clients under `apps/`, extensions under `extensions/`, skills under `skills/`.
- **Likely ownership hints:** OpenClaw core platform team / open-source maintainers.
- **Notes / dependencies:** Large multi-surface product: CLI, gateway, channels, apps, docs, and plugins/extensions.

## partner-dashboard
- **Product/domain:** Partner-facing dashboard for Bukas/Danacita partners.
- **Classification:** Frontend web app
- **Language/framework:** TypeScript; React + CRA/custom overrides + Ant Design
- **Key entrypoints:** `package.json`, `src/index.tsx`, `src/App.tsx`, pages under `src/pages`, services under `src/services`.
- **Likely ownership hints:** Partnerships / B2B product engineering; likely consumes APIs from `core-loans`.
- **Notes / dependencies:** Repo name and core-loans README both explicitly tie this app to partner operations.

## prosperity
- **Product/domain:** Investment/investor management platform covering investments, ledgers, organizations, payments, and users.
- **Classification:** Backend web app / service
- **Language/framework:** Python; Django + likely DRF + Celery
- **Key entrypoints:** `manage.py`, `app/wsgi.py`, `app/asgi.py`; major domains in `investments/`, `investors/`, `ledgers/`, `payments/`, `organizations/`, `users/`.
- **Likely ownership hints:** Investment/treasury/finance product team.
- **Notes / dependencies:** README was not surfaced in scan, so domain inference is from app names and structure. Looks like an internal/admin-heavy system rather than a public frontend.

## qa-automation
- **Product/domain:** Automated QA test suite spanning web, mobile, and load/browser flows.
- **Classification:** QA/test automation repo
- **Language/framework:** JavaScript, Robot Framework, k6 scripting; Cypress + Robot Framework + k6/browser
- **Key entrypoints:** `cypress/cypress.config.js`, robot suites under `mobile/` and `web/`, performance/browser scripts under `k6Browser/`.
- **Likely ownership hints:** QA / test engineering.
- **Notes / dependencies:** Contains Danacita login robot test and multiple channel-specific test assets.

## ralph-test
- **Product/domain:** Minimal scratch/test repo.
- **Classification:** Prototype / personal test repo
- **Language/framework:** Python; Plain Python
- **Key entrypoints:** `hello.py`.
- **Likely ownership hints:** Unclear; likely individual experimentation (possibly Ralph based on repo name).
- **Notes / dependencies:** Too little structure to infer a real product or production role.

## ringo
- **Product/domain:** Repository of OpenClaw analysis/design documentation rather than an application codebase.
- **Classification:** Research/documentation repo
- **Language/framework:** Markdown; N/A
- **Key entrypoints:** `openclaw-analysis/SUMMARY.md`, architecture docs, PRD, TODO.
- **Likely ownership hints:** Likely architecture/research owner for OpenClaw-related exploration.
- **Notes / dependencies:** No obvious runnable app/manifests at root; appears to be notes and technical analysis.

## sukat-backend
- **Product/domain:** Backend for Sukat, apparently an education/classroom/curriculum platform.
- **Classification:** Backend service + workers
- **Language/framework:** Python; Django + Celery + DRF-style API structure
- **Key entrypoints:** `manage.py`, `config/wsgi.py`, `config/asgi.py`; domain apps under `apps/` including `assignments`, `classrooms`, `curriculum`, `schools`, `users`, and `api`.
- **Likely ownership hints:** Sukat product/backend team; education domain suggested by module names.
- **Notes / dependencies:** Includes deployment docs (`DOKPLOY.md`), API docs, Docker/nginx, and standard Django app layout.

## sukat-frontend
- **Product/domain:** Frontend for Sukat education/classroom platform.
- **Classification:** Frontend web app
- **Language/framework:** TypeScript; Next.js + React
- **Key entrypoints:** `package.json`, `next.config.ts`, app code under `src/app`, shared UI in `src/components`, utilities in `src/lib`.
- **Likely ownership hints:** Sukat product/frontend team.
- **Notes / dependencies:** Paired clearly with `sukat-backend`; presence of API docs and app-router layout suggests active product frontend.
