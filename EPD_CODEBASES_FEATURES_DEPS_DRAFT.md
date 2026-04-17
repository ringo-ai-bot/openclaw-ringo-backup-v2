# EPD Codebases — Feature Keywords & Likely Dependencies (Draft)

Generated from repo README/spec files, env examples, compose/docs references, package/import signals, and obvious API/base URL conventions. This is an inference map, not a guaranteed architecture diagram.

## Conventions
- **Features** = short keywords describing user/business/technical capabilities present in repo docs/code.
- **Likely depends on** = services/repos this repo appears to call, embed, proxy, consume, or require to be useful.
- **Likely used by / provides to** = downstream consumers when evidence suggests the repo is a provider.
- **Confidence** = High / Medium / Low based on explicitness of evidence.

---

## atlas
- **Type**: frontend monorepo (TurboRepo / Next.js)
- **Features**:
  - borrower web app
  - Bukas frontend
  - Danacita frontend
  - Next.js SSR/SPA
  - shared UI/config packages
  - local docker frontend stack
- **Likely depends on**:
  - `core-loans` API backend for borrower app flows (**Medium**; repo purpose is borrower-facing frontend, backend not hard-linked in sampled files)
  - shared auth/content/config services via env not fully inspected (**Low**)
- **Likely used by / provides to**:
  - end users for Bukas/Danacita web/mobile-web experience
- **Evidence**:
  - README names apps `bukas` and `danacita`, shared libs/configs, local hosts `m.bukas.localhost` / `m.danacita.localhost`.

## cic-loantape
- **Type**: Python service / reporting export utility
- **Features**:
  - CIC loan tape generation
  - authenticated API
  - snapshot export
  - GPG encryption
  - FTP upload
  - XLSX / CSV / ZIP / GPG outputs
  - GCP credentials usage
- **Likely depends on**:
  - production/source loans database, probably `core-loans` data or its replica (**Medium**; loan-tape domain strongly overlaps but repo docs do not explicitly name source app)
  - CIC external systems / FTP endpoint (**High**)
  - GCP auth / cloud storage tooling (**Medium**)
- **Likely used by / provides to**:
  - compliance / reporting operations
  - external CIC submissions
- **Ambiguity**:
  - Source database is not explicitly named in sampled docs.

## core-loans
- **Type**: primary monolithic backend (Python/Django)
- **Features**:
  - borrower API/backend
  - partner dashboard backend/API
  - admin/Gubat admin
  - loans / underwriting / payments
  - referrals / rewards
  - offline applications
  - webhook/test endpoints
  - shortlinks / forms
  - Celery async jobs
  - country-specific Bukas / Danacita modes
  - extensive integrations surface
- **Likely depends on**:
  - PostgreSQL (`DATABASE_URL`) (**High**)
  - Redis / Celery broker (`CELERY_BROKER_URL`) (**High**)
  - Google credentials / GCP (`GOOGLE_APPLICATION_CREDENTIALS`) (**High**)
  - marketing service (`MARKETING_SERVICE_BASE_URL`, `MARKETING_SERVICE_*`) — possibly separate internal service, possibly in `hooli` or another repo (**Medium**)
  - `partner-dashboard` conventions/renderers via `PARTNER_DASHBOARD_*` env and partner dashboard API role (**Medium**; likely frontend/backend contract more than code dependency)
  - external vendors mentioned in env summary: Privy, Vida, Qontak, Metabase, etc. (**Medium**)
- **Likely used by / provides to**:
  - `atlas` borrower-facing frontend (**Medium**)
  - legacy/other frontends such as `integrations-app` and `partner-dashboard` via API URLs (**Medium**)
  - data pipelines such as `mono-pipeline` from operational DBs (**Medium**)
  - reporting/export tools such as `cic-loantape` from operational data (**Medium**)
- **Evidence**:
  - README: serves Gubat Admin, Borrower App backend/API, Partner Dashboard backend/API.
  - Env: `BASE_URL=http://api.danacita.localhost`, partner dashboard renderer settings, marketing service base URL.

## findyouruni
- **Type**: lead-generation / recommendation frontend app
- **Features**:
  - student lead capture
  - multi-step wizard
  - school/course recommendation
  - tuition/cost transparency
  - financing pathway positioning
  - partner school marketplace/catalog
- **Likely depends on**:
  - lead capture / CRM / backend API not identified in sampled spec (**Low**)
  - likely Bukas ecosystem APIs or data feeds for school/program/lead submission (**Low-Medium**)
- **Likely used by / provides to**:
  - Bukas marketing / lead-gen funnel
  - partner schools as lead destination
- **Ambiguity**:
  - Only business spec was sampled; technical dependencies remain mostly unknown.

## genai-service
- **Type**: AI platform / Django service
- **Features**:
  - generative AI deployment platform
  - agent evaluations
  - help-center ingestion
  - vector database indexing
  - conversational troubleshooting/support tooling
  - country-specific Bukas/Danacita references
- **Likely depends on**:
  - PostgreSQL with vector extension / pgvector-style storage (**High**; README explicitly says Postgres vector database)
  - help-center HTML dumps from `hooli` / website pod (`website-v3-deployment`) (**High**)
  - Kubernetes-deployed website content source (**High**)
  - LLM/provider APIs not sampled but implied (**Medium**)
- **Likely used by / provides to**:
  - support/chat/agent experiences for Bukas and Danacita (**Medium**)
  - potentially `core-loans`, `hooli`, or customer support channels via GenAI integrations (**Low-Medium**)
- **Strong cross-repo signal**:
  - README instructs dumping help-center articles from website pod, which strongly suggests dependency on `hooli` content.

## hooli
- **Type**: website / homepage repo (`website_v3`)
- **Features**:
  - Bukas and Danacita website/homepage
  - country-specific sites
  - dockerized local web stack
  - likely CMS/content and marketing pages
  - migration commands indicate backend/CMS component, not just static frontend
- **Likely depends on**:
  - PostgreSQL or similar DB for website/CMS migrations (**Medium**)
  - GCP / deployment infra in some environments (**Low-Medium**)
  - possibly marketing/help-center publishing workflows consumed by `genai-service` (**High as provider relationship**)
- **Likely used by / provides to**:
  - `genai-service` as source of help-center article dumps (**High**)
  - marketing acquisition funnel for Bukas/Danacita
  - maybe referral/marketing touchpoints referenced from `core-loans` marketing envs (**Low-Medium**)
- **Ambiguity**:
  - Whether this repo itself is the `marketing service` named in `core-loans` env is not proven.

## integrations-app
- **Type**: Node app for payment/integration surfaces
- **Features**:
  - Bukas/Danacita integrations app
  - payment-domain local hosts (`pay.bukas.localhost`, `pay.danacita.localhost`)
  - country-specific runtime modes
  - Docker and local dev modes
- **Likely depends on**:
  - backend API configured by `API_URL` (**High**)
  - likely `core-loans` API for payment/application data (**Medium-High**)
  - payment providers / callbacks not fully sampled (**Medium**)
- **Likely used by / provides to**:
  - payment/integration user journeys under pay.* domains
- **Evidence**:
  - `.env.example` contains `API_URL`; README centers on pay domains.

## mono-pipeline
- **Type**: Airflow data pipeline / analytics ETL repo
- **Features**:
  - Airflow orchestration
  - BigQuery ETL
  - Slack alerting
  - raw-data stage pipelines
  - portfolio reporting
  - Athena / Iceberg references
  - Bukas / Danacita analytical data movement
- **Likely depends on**:
  - GCP BigQuery (**High**)
  - Airflow (**High**)
  - Slack webhooks (**High**)
  - operational source databases for Bukas/Danacita, likely including `core-loans` replicas/slaves (**Medium-High**)
  - AWS Athena / Iceberg for some pipelines (**High**)
  - Metabase-adjacent downstream analytics consumption in some archived DAG comments (**Medium**)
- **Likely used by / provides to**:
  - analytics / BI stakeholders
  - possibly `cic-loantape` or other reporting processes indirectly via warehouse outputs (**Low-Medium**)
- **Evidence**:
  - README covers Airflow + BigQuery setup; DAGs mention BigQuery, Slack, Athena, Danacita Postgres slave.

## openclaw
- **Type**: OpenClaw agent tooling repo
- **Features**:
  - AI agent runtime/tooling
  - workspace automation
  - not obviously part of EPD product estate
- **Likely depends on**:
  - none relevant to EPD application graph from current inspection
- **Likely used by / provides to**:
  - developer/operator workflows
- **Ambiguity**:
  - Excluded from product dependency graph unless explicitly needed.

## partner-dashboard
- **Type**: React frontend for partners
- **Features**:
  - partner dashboard UI
  - leads/applications views
  - documentation links
  - Firebase analytics/auth/config
  - GTM support
  - SWR data fetching
- **Likely depends on**:
  - `core-loans` partner dashboard API (`REACT_APP_API_URL`) (**High**)
  - Wagtail/content API (`REACT_APP_API_WAGTAIL_URL`) (**Medium-High**)
  - Firebase (**High**)
  - GTM (**Medium**)
- **Likely used by / provides to**:
  - partners/banks/schools using lead/application dashboards
- **Evidence**:
  - README not sampled, but env file clearly shows API URL, Wagtail URL, Firebase config, docs URLs.

## prosperity
- **Type**: Django app/service (likely standalone internal product)
- **Features**:
  - API service under `api.prosperity.erudifi.localhost`
  - seeded development data
  - GCP credentials
  - Dockerized app
- **Likely depends on**:
  - GCP credentials (`gcp-creds.json`) (**High**)
  - database backing store for Django app (**Medium**)
- **Likely used by / provides to**:
  - unclear from sampled docs
- **Ambiguity**:
  - Product purpose and cross-repo ties were not explicit in sampled files.

## qa-automation
- **Type**: test automation repo
- **Features**:
  - automated QA / regression testing (inferred from name)
- **Likely depends on**:
  - target apps under test, probably `core-loans`, `atlas`, `partner-dashboard`, `hooli`, or pay flows (**Low-Medium**)
- **Likely used by / provides to**:
  - engineering QA workflows
- **Ambiguity**:
  - Not deeply inspected in retained evidence, so dependency mapping is weak.

## sukat-backend
- **Type**: Django backend
- **Features**:
  - accounts/auth API
  - school/class/course/assignment flows
  - quiz generation and grading
  - async AI quiz jobs
  - Celery worker
  - Redis-backed background processing
  - Dokploy deployment model
- **Likely depends on**:
  - PostgreSQL (**High**)
  - Redis (`CELERY_BROKER_URL`) (**High**)
  - `sukat-frontend` as primary UI consumer (**High as provider relationship**)
  - AI model/provider for quiz generation/grading (**Medium**; strongly implied by API docs)
- **Likely used by / provides to**:
  - `sukat-frontend` over `/api/*` (**High**)
- **Evidence**:
  - README and API docs explicitly describe backend API, Celery worker, async AI generation, CORS for frontend domain.

## sukat-frontend
- **Type**: Next.js frontend
- **Features**:
  - school/teacher/student UI
  - login/accounts/assignments/quizzes flows
  - API proxy/fallback logic
  - explicit API contract docs
  - frontend/backend origin handling
- **Likely depends on**:
  - `sukat-backend` (`API_BASE_URL`, `NEXT_PUBLIC_API_BASE_URL`) (**High**)
  - CORS-enabled backend deployment (**High**)
- **Likely used by / provides to**:
  - Sukat end users (teachers/students/principals)
- **Evidence**:
  - `src/lib/api-url.ts` and env docs directly describe backend base URL handling.

---

## Likely Cross-Repo / Service Dependency Graph

### High-confidence links
- `sukat-frontend` -> `sukat-backend`
- `partner-dashboard` -> `core-loans`
- `genai-service` -> `hooli` (help-center/article dump source)
- `mono-pipeline` -> BigQuery / Airflow / Slack / AWS Athena
- `cic-loantape` -> CIC external FTP / GPG / reporting destination
- `integrations-app` -> backend API via `API_URL`

### Medium-confidence links
- `atlas` -> `core-loans`
- `integrations-app` -> `core-loans`
- `mono-pipeline` -> `core-loans` data replicas/slaves
- `cic-loantape` -> `core-loans` data or replica
- `core-loans` -> marketing service (possibly separate repo/service; not confirmed)
- `core-loans` -> external providers (Privy, Vida, Qontak, Metabase, etc.)
- `partner-dashboard` -> Wagtail/content service (repo not identified from current sample)

### Low-confidence / unresolved links
- `findyouruni` -> Bukas/core lead intake backend
- `prosperity` -> other EPD services
- `qa-automation` -> exact repos under test
- whether `hooli` is the same thing as `marketing service` referenced by `core-loans`

---

## Candidate Shared Infra / External Services Seen Across Repos
- PostgreSQL
- Redis
- Celery
- Docker / docker-compose
- GCP / service-account credentials
- BigQuery
- AWS Athena / Iceberg
- Slack webhook alerts
- Firebase
- GTM
- CIC FTP + GPG
- likely payment/signing/comms vendors: Privy, Vida, Qontak, Midtrans, Metabase

---

## Ambiguity Notes / Caveats
1. The prior `EPD_CODEBASES_MAP_DRAFT.md` referenced in task context was not present, so this draft is standalone rather than a strict enrichment patch.
2. Several links are inferred from env variable names (`API_URL`, `MARKETING_SERVICE_BASE_URL`, `PARTNER_DASHBOARD_*`) rather than direct import-level coupling.
3. `core-loans` appears to be the central operational backend, but sampled evidence does not prove every frontend/service points to it.
4. `hooli` clearly supplies help-center content to `genai-service`; its relationship to the `marketing service` named in `core-loans` remains unconfirmed.
5. `findyouruni`, `prosperity`, and `qa-automation` need deeper code/config inspection for stronger dependency mapping.
