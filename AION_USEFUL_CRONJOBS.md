# Useful Cron Jobs for AION / Hermes

Purpose: define recurring jobs that would be useful for Andre's AIOS, what they produce, and what AION needs before safely running them.

Status key:

- `ready_internal`: can run locally without external side effects.
- `needs_input`: needs transcripts, repo access, APIs, or config first.
- `needs_approval`: can affect reputation/money/customer-facing output; human approval required.
- `future`: good idea but not yet worth automating.

---

## 1. Daily AION Knowledge Intake

Status: `ready_internal` once transcripts exist.

Schedule idea:

```text
0 8 * * *
```

Goal:

Scan `lecturasutiles/transcripts/youtube/` and `summaries/` for new files, create summaries, update `INDEX.md`, and generate applied lessons for AION/business repos.

Output:

```text
outputs/daily_knowledge_intake/YYYY-MM-DD.md
```

Needs:

- New transcript files committed/pulled into repo.
- A consistent transcript header.
- Write access to `lecturasutiles`.

Safety:

- Internal-only.
- No external posting.
- Can auto-commit if Andre approves auto-commit behavior.

Recommended Hermes type:

```text
LLM-driven cronjob, not no_agent
```

Why:

Needs reasoning and synthesis.

---

## 2. Weekly Business Incubator Review

Status: `ready_internal` for current business repo.

Schedule idea:

```text
0 9 * * MON
```

Goal:

Review `output/businesses/` in the incubator repo and rank each business by:

- market pain
- MVP completeness
- frontend/backend/admin status
- validation readiness
- missing assets
- next best action

Output:

```text
output/reports/business_incubator_weekly/YYYY-MM-DD.md
```

Needs:

- Repo path: `/home/hermes/coleccion_trading_hermes_polymarket`
- Tests command confirmed.
- Push approval policy.

Safety:

- Internal-only.
- No outreach.
- No deploy.

Recommended Hermes type:

```text
LLM-driven cronjob
```

---

## 3. Cold Outreach Readiness Checker

Status: `ready_internal`; actual sending is `needs_approval`.

Schedule idea:

```text
0 10 * * WED
```

Goal:

Check if any business has the minimum assets before cold email:

- landing page
- sender identity
- basic social proof/profile
- offer
- CTA
- opt-out language
- lead list
- tracking sheet
- approved copy

Output:

```text
output/cold_mailing/readiness/YYYY-MM-DD.md
```

Needs:

- Business folder paths.
- Lead files.
- Landing/social asset convention.

Safety:

- Must never send emails automatically.
- Human approval required before any external contact.

Recommended Hermes type:

```text
LLM-driven cronjob
```

---

## 4. YouTube Download Queue Maintainer

Status: `ready_internal`, transcript fetching from VPS is `blocked`.

Schedule idea:

```text
0 11 * * SAT
```

Goal:

Maintain `YOUTUBE_DOWNLOAD_QUEUE.md`:

- detect missing transcript files
- group links by category
- mark processed videos
- suggest new videos based on current AION goals

Output:

```text
YOUTUBE_DOWNLOAD_QUEUE.md
outputs/youtube_queue/YYYY-MM-DD.md
```

Needs:

- `lecturasutiles` write access.
- User/local PC to actually download transcripts when YouTube blocks VPS.

Safety:

- Internal-only.

Recommended Hermes type:

```text
LLM-driven cronjob
```

---

## 5. Polymarket Paper Trading Report

Status: already partly active in the Polymarket repo.

Schedule idea:

```text
every 2h for quiet update
every 6h for research scan
```

Goal:

Monitor paper positions, scan markets, report signals, and keep real-money execution disabled.

Output:

```text
output/polymarket/reports/YYYY-MM-DD.md
```

Needs:

- Existing Polymarket repo scripts.
- Paper trading DB.
- Risk config.
- Human approval for anything real-money.

Safety:

- Read-only/paper only.
- No live trading without explicit human approval.
- Restore scoring thresholds before any production use.

Recommended Hermes type:

```text
script/no_agent for quiet metrics
LLM-driven for research synthesis
```

---

## 6. Weekly Repo Health / Test Runner

Status: `ready_internal`.

Schedule idea:

```text
0 7 * * SUN
```

Goal:

Run tests/build checks in selected repos and report breakage.

Output:

```text
outputs/repo_health/YYYY-MM-DD.md
```

Needs:

- Stable test commands per repo.
- Workdir per repo.
- Timeout policy.

Safety:

- Internal-only.
- No deploy.
- No destructive commands.

Recommended Hermes type:

```text
script/no_agent when only reporting test pass/fail
LLM-driven when summarizing failures and proposing fixes
```

---

## 7. Daily Founder Brief for Andre

Status: `needs_input`.

Schedule idea:

```text
0 8 * * *
```

Goal:

Send Andre a concise daily Telegram brief:

- what changed in repos
- what AION learned
- what business is closest to validation
- what one decision Andre should make today
- blockers/tools needed

Output:

```text
Telegram/origin + optional file
```

Needs:

- Agreed sources: business repo, lecturasutiles, Polymarket repo, cron outputs.
- Tone/length preference.
- Avoid notification spam.

Safety:

- Internal report only.

Recommended Hermes type:

```text
LLM-driven cronjob
```

---

## 8. Landing Page / Offer Gap Scanner

Status: `ready_internal`.

Schedule idea:

```text
0 13 * * TUE
```

Goal:

For every business, check whether public-facing assets answer:

- who is it for?
- painful problem?
- promised outcome?
- proof/mockup?
- CTA?
- pricing hypothesis?
- risk/compliance notes?

Output:

```text
output/businesses/<business>/MARKET_READINESS.md
```

Needs:

- Business folders.
- Public-content/landing conventions.

Safety:

- Internal-only.

Recommended Hermes type:

```text
LLM-driven cronjob
```

---

## 9. Social Content Draft Generator

Status: `needs_approval`.

Schedule idea:

```text
0 15 * * THU
```

Goal:

Draft social posts based on real repo progress and learnings.

Output:

```text
output/social_drafts/YYYY-MM-DD.md
```

Needs:

- Brand/persona rules.
- Platforms chosen.
- Human approval before posting.
- For Infinity Ascend, visual quality workflow first.

Safety:

- Draft only.
- No autoposting until approved.

Recommended Hermes type:

```text
LLM-driven cronjob
```

---

## 10. Client Ops Prototype Cron

Status: `future` until a specific client/workflow exists.

Schedule idea:

```text
0 17 * * FRI
```

Goal:

Demonstrate Hermes as a productized client-ops operator:

- parse meeting notes
- extract action items
- draft follow-up emails
- create reminders
- report open loops

Output:

```text
output/client_ops/YYYY-MM-DD.md
```

Needs:

- Example meeting notes.
- Client/project context.
- Approval before sending follow-ups.

Safety:

- Draft only.

Recommended Hermes type:

```text
LLM-driven cronjob
```

---

# Immediate cronjob recommendations

Do first:

1. `Weekly Business Incubator Review`
2. `YouTube Download Queue Maintainer`
3. `Daily Founder Brief`
4. `Cold Outreach Readiness Checker`

Do later:

1. `Social Content Draft Generator`
2. `Client Ops Prototype Cron`
3. Any external-facing automation.

# Things AION needs from Andre

## For knowledge cronjobs

- Local transcripts added to `transcripts/youtube/`.
- Permission to auto-commit summary/index updates, or keep as local reports only.

## For business cronjobs

- Decide priority business: likely `med-spa-lead-recovery` or `hvac-missed-call-recovery`.
- Define whether reports should push to GitHub automatically.

## For outreach cronjobs

- Domain/sender identity.
- Landing page.
- Social/profile presence.
- Opt-out/compliance rules.
- Human approval before sending.

## For Polymarket cronjobs

- Keep paper-only until explicitly approved.
- Risk limits confirmed.
- External data sources for weather/markets if needed.

## For social cronjobs

- Platform choice.
- Brand rules.
- Approval workflow.
- For Infinity Ascend: high-quality visual workflow before autoposting.
