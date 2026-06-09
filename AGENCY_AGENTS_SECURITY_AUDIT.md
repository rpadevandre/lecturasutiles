# Security Audit — msitarzewski/agency-agents

Date: 2026-06-09
Repo audited: `https://github.com/msitarzewski/agency-agents`
Local audit path: `/tmp/agency-agents-audit`
Commit audited: `a077c9a`

## Executive verdict

The repo appears to be a large collection of agent/persona Markdown files plus installer/converter scripts. I did **not** find obvious malicious prompt-injection payloads such as instructions to ignore system/developer messages, exfiltrate secrets, or bypass guardrails.

However, it should **not** be installed wholesale into Hermes/AION. Many files are broad personas, some include external publishing workflows, security/pentest workflows, tool permissions, and memory instructions that are not tailored to Andre's operating model. The safe path is to **adapt selected agents into AION-specific skills** instead of copying everything as-is.

## What was inspected

- 275 Markdown files.
- Top-level docs and integration docs.
- `scripts/install.sh` and conversion/install surface at a high level.
- Focused review of relevant agents for Andre:
  - `sales/sales-offer-lead-gen-strategist.md`
  - `sales/sales-outbound-strategist.md`
  - `marketing/marketing-email-strategist.md`
  - `specialized/business-strategist.md`
  - `engineering/engineering-codebase-onboarding-engineer.md`
  - `engineering/engineering-minimal-change-engineer.md`
  - `engineering/engineering-prompt-engineer.md`
  - `testing/testing-reality-checker.md`
  - `testing/testing-evidence-collector.md`
  - `product/product-feedback-synthesizer.md`
  - `product/product-sprint-prioritizer.md`

## Automated scan results

### Direct prompt injection patterns

Searched for patterns like:

```text
ignore previous instructions
forget prior instructions
you are now
developer message
system prompt
```

Result: no malicious direct payload found.

Relevant hits were benign/defensive, e.g. `engineering-prompt-engineer.md` mentions testing adversarial inputs like `Ignore all previous instructions`, and `meeting-notes-specialist.md` explicitly says pasted content is data, not instructions.

### Dangerous shell patterns

Searched for destructive shell patterns, pipes to shell, and obvious dangerous commands.

Result: no critical destructive-shell pattern found in agent Markdown.

### Secret-like strings

Searched for common secret/token/private-key patterns.

Result: 2 private-key-like hits, but both are examples in a SecOps file showing what to detect, not real secrets:

```text
security/security-senior-secops.md lines 46-47
-----BEGIN RSA PRIVATE KEY-----
-----BEGIN EC PRIVATE KEY-----
```

### External publishing/actions

There are agents related to marketing, social publishing, email, sales, and automation. These are not necessarily malicious, but they are risky if copied as active instructions because AION should not email, DM, publish, trade, or post without Andre's explicit approval.

## Main risks if installed wholesale

### 1. Context dilution

There are 200+ personas. Installing many will bloat context and reduce AION's focus. Andre needs a repo-first business operator, not a giant generic agency roster.

### 2. Tool mismatch

Some files include Claude/Cursor/Gemini-style tool metadata (`Read`, `Write`, `Edit`, `WebFetch`, etc.) that does not map cleanly to Hermes skills.

### 3. External action risk

Marketing/sales/social agents discuss posting, outreach, campaign execution, distribution, and social platforms. These must be adapted with AION's rule:

```text
Draft/prepare/review only. No external sending or posting without human approval.
```

### 4. Overconfidence/persona claims

Several agents are written as strong expert personas with success metrics. Useful as inspiration, but AION should keep evidence-first status labels: `scaffold`, `draft`, `usable`, `tested`, `ready`.

### 5. Security/pentest agents

Security skills may contain dual-use workflows. They are useful for defensive review, but should be imported only with strict scope: owned repos only, no unauthorized testing, no exploit execution unless explicitly approved.

## Recommended additions for AION

### High priority — adapt into skills

1. `sales/sales-offer-lead-gen-strategist.md`
   - Why: directly improves Andre's incubator businesses.
   - Use for: offer blueprint, lead magnets, channel choice, validation sequence.
   - AION adaptation: add cold-email safety gate and EN-first/ES-second positioning.

2. `sales/sales-outbound-strategist.md`
   - Why: improves cold outreach strategy by using signals, not spam volume.
   - Use for: ICP, triggers, account tiering, personalization.
   - AION adaptation: never send; only prepare lead research/copy/tracking until approved.

3. `marketing/marketing-email-strategist.md`
   - Why: strong deliverability/compliance/lifecycle thinking.
   - Use for: sender readiness, exit conditions, opt-out, segmentation.
   - AION adaptation: focus on small validation batches, not marketing automation blasts.

4. `specialized/business-strategist.md`
   - Why: helps avoid random idea-chasing and forces market/competitive tradeoffs.
   - Use for: business ranking, TAM/SAM/SOM, competitive analysis, what-not-to-do.
   - AION adaptation: require evidence from repo/web/user context.

5. `testing/testing-reality-checker.md`
   - Why: matches Andre's desire for honesty and no fantasy approvals.
   - Use for: judging whether projects are truly ready.
   - AION adaptation: remove tool-specific commands, keep evidence-first status labels.

6. `testing/testing-evidence-collector.md`
   - Why: useful for frontend/admin QA with screenshots and visual proof.
   - Use for: landing pages/admin panels/demos.
   - AION adaptation: use Hermes browser/screenshot tools and repo-specific acceptance criteria.

7. `engineering/engineering-codebase-onboarding-engineer.md`
   - Why: improves repo-first reading and factual orientation.
   - Use for: reading Nexbody/reference repos/business repos.
   - AION adaptation: read-only mode unless user asks for implementation.

8. `engineering/engineering-minimal-change-engineer.md`
   - Why: reduces overbuilding and scope creep.
   - Use for: bug fixes and repo edits.
   - AION adaptation: pair with incubator workflow; do not block intentional scaffolding.

### Medium priority

9. `engineering/engineering-prompt-engineer.md`
   - Useful for creating prompt tests and injection-resistant workflows.
   - Needs adaptation because it includes chain-of-thought scaffolding examples not appropriate to expose in final outputs.

10. `product/product-sprint-prioritizer.md`
    - Useful for one-week/one-business focus.
    - Needs adaptation to Andre's solo-builder reality.

11. `product/product-feedback-synthesizer.md`
    - Useful after real customer replies/interviews exist.
    - Not urgent until outreach/feedback begins.

12. `security/security-appsec-engineer.md` or `security/security-architect.md`
    - Useful for defensive security checklists across FastAPI/Mongo/frontend/admin.
    - Only adapt defensively.

### Avoid for now

- Broad social auto-publisher agents.
- Region-specific marketing agents not relevant to Andre's target markets.
- Pentesting/exploit-heavy agents unless a defensive owned-scope task is defined.
- Game/GIS/Roblox/Unity/etc. agents unless a specific project needs them.
- Full installer scripts that copy hundreds of agents into active agent directories.

## Safe import plan

Do not run `scripts/install.sh` for this repo.

Instead:

1. Create AION-native skills under `~/.hermes/skills/` one by one.
2. Convert each selected agent into a Hermes skill with:
   - trigger conditions
   - exact workflow
   - explicit safety rules
   - validation steps
   - no external action without approval
   - references to Andre's repos/workflows
3. Start with 3 skills:
   - `aion-offer-lead-gen-strategy`
   - `aion-outbound-readiness`
   - `aion-reality-checker`
4. Test each skill on current incubator repo before adding more.

## Recommended first 3 imports

### 1. AION Offer & Lead Gen Strategy

Source: `sales/sales-offer-lead-gen-strategist.md`

Purpose:

Improve each incubated business by producing:

- ICP
- dream outcome
- lead magnet
- offer blueprint
- value equation
- validation channel
- next smallest validation action

### 2. AION Outbound Readiness

Sources:

- `sales/sales-outbound-strategist.md`
- `marketing/marketing-email-strategist.md`

Purpose:

Before any cold outreach, verify:

- landing page exists
- sender domain/email exists
- opt-out language exists
- lead list quality
- signal/persona fit
- approved CTA
- tracking sheet

### 3. AION Reality Checker

Sources:

- `testing/testing-reality-checker.md`
- `testing/testing-evidence-collector.md`

Purpose:

Prevent fantasy status reports. Every project/output must be labeled honestly:

```text
scaffold / draft / usable / tested / ready
```

and claims must be backed by evidence:

```text
file path
screenshot
test result
command output
Git commit
```

## Final recommendation

The repo is useful, but it should be treated as **source material**, not as trusted active instructions. I recommend adapting only a small curated set into AION-native skills, starting with offer/outbound/reality-checking because those directly improve Andre's money-oriented incubator workflow.
