# YouTube Download Queue for AION Knowledge Base

Purpose: keep a clean categorized queue of YouTube videos whose transcripts should be downloaded locally and added to this repo so AION can learn from them.

## Current reality

The VPS/cloud IP is blocked by YouTube transcript access. Transcript extraction with `youtube_transcript_api` returned `RequestBlocked` for priority videos.

So the reliable workflow is:

1. Andre downloads/transcribes from local PC/network.
2. Save transcript files into `transcripts/youtube/<category>/`.
3. Commit/push the transcript files to this repo.
4. AION reads the new transcripts, creates summaries, updates `INDEX.md`, and applies lessons into repo artifacts/workflows.

## Where transcripts should go

```text
transcripts/youtube/hermes/
transcripts/youtube/business/
transcripts/youtube/cronjobs/
transcripts/youtube/cold_outreach/
transcripts/youtube/seo_distribution/
transcripts/youtube/polymarket_trading/
transcripts/youtube/design_frontend/
```

Each transcript file should start with this header:

```text
Video URL:
Video ID:
Title:
Channel:
Category:
Date downloaded:
Language:

Transcript:
...
```

---

# Category: Hermes / AION / AIOS

Goal: improve AION as an operating agent: skills, memory, goals, cronjobs, Kanban, delegation, MCP, Telegram/Discord, long-running workflows.

- [ ] [5 Ways I Make Money With Hermes Agent](https://www.youtube.com/watch?v=2WZAcWtwoDI)
  - Channel: Sharbel A.
  - Why: Hermes as junior operator, productized services, human-in-the-loop monetization.
  - Target: `transcripts/youtube/hermes/2WZAcWtwoDI_5_Ways_I_Make_Money_With_Hermes_Agent.txt`

- [ ] [The 7 Levels of Hermes Agent Explained](https://www.youtube.com/watch?v=G47mnkGkYwQ)
  - Channel: David Ondrej
  - Why: Hermes setup, skills, cronjobs, Kanban, memory, MCP.
  - Target: `transcripts/youtube/hermes/G47mnkGkYwQ_The_7_Levels_of_Hermes_Agent_Explained.txt`

- [ ] [I Built the Ultimate Multi-Agent Workflow w/ Hermes Agent Kanban Board](https://www.youtube.com/watch?v=EKVRqcpTT6s)
  - Channel: Tonbi's AI Garage
  - Why: Kanban as multi-agent coordination layer.
  - Target: `transcripts/youtube/hermes/EKVRqcpTT6s_I_Built_the_Ultimate_Multi_Agent_Workflow_w_Hermes_Agent_Kanban_Board.txt`

- [ ] [100 hours of Hermes Agent lessons in 23 minutes](https://www.youtube.com/watch?v=k5NhsF7t68M)
  - Why: concentrated Hermes usage lessons.
  - Target: `transcripts/youtube/hermes/k5NhsF7t68M_100_hours_of_Hermes_Agent_lessons.txt`

- [ ] [Hermes /goal is insane… just watch](https://www.youtube.com/watch?v=9oOZ3PB6n4Y)
  - Why: persistent goals and long-running objectives.
  - Target: `transcripts/youtube/hermes/9oOZ3PB6n4Y_Hermes_goal_is_insane.txt`

- [ ] [The Only Hermes Agent Tutorial You'll Need in 2026](https://www.youtube.com/watch?v=8bYMgvJt5Ws)
  - Why: broad Hermes tutorial.
  - Target: `transcripts/youtube/hermes/8bYMgvJt5Ws_Only_Hermes_Agent_Tutorial_2026.txt`

- [ ] [Hermes Agent Tutorial for Beginners - Crash Course](https://www.youtube.com/watch?v=6QZBep7mW0c)
  - Why: beginner setup and fundamentals.
  - Target: `transcripts/youtube/hermes/6QZBep7mW0c_Hermes_Agent_Crash_Course.txt`

- [ ] [Hermes Agent - Full Course & Setup Guide](https://www.youtube.com/watch?v=mTYxpIRK7xA)
  - Why: complete setup/reference course.
  - Target: `transcripts/youtube/hermes/mTYxpIRK7xA_Hermes_Full_Course_Setup_Guide.txt`

- [ ] [I gave my Hermes Agent a phone number](https://www.youtube.com/watch?v=zHE434sBw2U)
  - Why: phone/voice integration patterns.
  - Target: `transcripts/youtube/hermes/zHE434sBw2U_Hermes_Agent_phone_number.txt`

- [ ] [Stop Prompting Claude. Use Karpathy's Method Instead.](https://www.youtube.com/watch?v=7zZy1QTvokM)
  - Channel: Austin Marchese
  - Why: spec/verifier/environment method for better Claude/AI-agent work; directly relevant to AION standards, project specs, QA loops, and reducing vague prompts.
  - Target: `transcripts/youtube/hermes/7zZy1QTvokM_Stop_Prompting_Claude_Use_Karpathy_Method.txt`

---

# Category: Business / founder knowledge

Goal: improve offer selection, strategy, brand, pricing, customer psychology, and business judgment.

- [ ] [30 Years of Business Knowledge in 2hrs 26mins](https://www.youtube.com/watch?v=9VlvbpXwLJs)
  - Channel: Simon Squibb
  - Why: business fundamentals, brand, purpose, sales, delayed gratification.
  - Target: `transcripts/youtube/business/9VlvbpXwLJs_30_Years_of_Business_Knowledge_in_2hrs_26mins.txt`

- [ ] [Alex Hormozi — search/query: Grand Slam Offers / $100M Leads / No BS Business Advice](https://www.youtube.com/@AlexHormozi)
  - Why: offers, acquisition, pricing, sales psychology.
  - Target: `transcripts/youtube/business/<video_id>_alex_hormozi_offer_or_leads.txt`

- [ ] [Simon Squibb channel](https://www.youtube.com/@SimonSquibb/videos)
  - Why: founder mindset, company building, brand.
  - Target: `transcripts/youtube/business/<video_id>_simon_squibb_business.txt`

- [ ] [How to Build & Sell AI Agents in 2026: Ultimate Beginner's Guide](https://www.youtube.com/watch?v=AYQtRqW1xX4)
  - Channel: Liam Ottley
  - Why: AI automation agency and selling AI-agent services.
  - Target: `transcripts/youtube/business/AYQtRqW1xX4_Build_Sell_AI_Agents_2026.txt`

- [ ] [The #1 Claude AI Side Hustle Nobody Is Talking About](https://www.youtube.com/watch?v=uJeHGmMir5Q)
  - Channel: Patrick Dang
  - Why: B2B AI service monetization.
  - Target: `transcripts/youtube/business/uJeHGmMir5Q_Claude_AI_Side_Hustle.txt`

---

# Category: Cron jobs / productized recurring services

Goal: discover recurring reports/services AION can run as subscriptions or internal operating loops.

- [ ] [How to Automate Jobs with Hermes Agent](https://www.youtube.com/watch?v=Y8sPYVZ5n58)
  - Why: Hermes job automation patterns.
  - Target: `transcripts/youtube/cronjobs/Y8sPYVZ5n58_How_to_Automate_Jobs_with_Hermes_Agent.txt`

- [ ] [Hermes /goal is insane… just watch](https://www.youtube.com/watch?v=9oOZ3PB6n4Y)
  - Why: goals vs cron jobs and long-running tasks.
  - Target: `transcripts/youtube/cronjobs/9oOZ3PB6n4Y_Hermes_goal_is_insane.txt`

- [ ] [Fully Automate Social Media with Claude Code in 5 Minutes](https://www.youtube.com/watch?v=UNKNOWN_FULLY_AUTOMATE_SOCIAL_MEDIA)
  - Why: social/content cron job ideas; replace UNKNOWN with exact link.
  - Target: `transcripts/youtube/cronjobs/<video_id>_fully_automate_social_media.txt`

---

# Category: Cold outreach / B2B sales

Goal: learn deliverability, safe sending, offer testing, personalization, follow-up, and conversion.

- [ ] [This Cold Email Strategy Makes $160k/mo for My SaaS](https://www.youtube.com/watch?v=ACMED_IDZb8)
  - Why: SaaS cold email strategy.
  - Target: `transcripts/youtube/cold_outreach/ACMED_IDZb8_Cold_Email_Strategy_SaaS.txt`

- [ ] [How To Use AI to Automate Cold Email Outreach](https://www.youtube.com/watch?v=6eLWP3a-9Uo)
  - Why: AI-assisted outreach workflow.
  - Target: `transcripts/youtube/cold_outreach/6eLWP3a-9Uo_AI_Automate_Cold_Email_Outreach.txt`

- [ ] [How I grew my SaaS to $4,000 MRR with cold emails](https://www.youtube.com/watch?v=KJb_nfR6gJk)
  - Why: realistic small SaaS validation via email.
  - Target: `transcripts/youtube/cold_outreach/KJb_nfR6gJk_SaaS_4000_MRR_Cold_Emails.txt`

---

# Category: SEO / distribution / content engines

Goal: make repo-built products discoverable and validate via search/content.

- [ ] [Claude Code SEO: How I Got 50,000 Clicks Per Month](https://www.youtube.com/watch?v=4IyJm1i__ag)
  - Channel: Jono Catliff
  - Why: programmatic SEO and service pages.
  - Target: `transcripts/youtube/seo_distribution/4IyJm1i__ag_Claude_Code_SEO_50000_Clicks.txt`

- [ ] [This Boring Website Earns $6M/Year. Here's How to Clone it](https://www.youtube.com/watch?v=nQOGK72IHx8)
  - Channel: Jonathan's Jam
  - Why: utility sites and boring profitable niches.
  - Target: `transcripts/youtube/seo_distribution/nQOGK72IHx8_Boring_Website_6M_Year.txt`

- [ ] [How selling Ebooks with Claude changed my life](https://www.youtube.com/watch?v=nmRWmF2Umes)
  - Channel: Molly Keyser
  - Why: lead magnet → email list → pre-sell flow.
  - Target: `transcripts/youtube/seo_distribution/nmRWmF2Umes_Selling_Ebooks_With_Claude.txt`

---

# Category: Polymarket / trading / prediction systems

Goal: improve alerting, paper trading, risk controls, smart-money tracking, and research automation.

- [ ] [Using the New Hermes Agent to Track Polymarket "Smart Money"](https://www.youtube.com/watch?v=UNKNOWN_SMART_MONEY_HERMES)
  - Why: wallet tracking and signal generation; replace UNKNOWN with exact link.
  - Target: `transcripts/youtube/polymarket_trading/<video_id>_Hermes_Polymarket_Smart_Money.txt`

- [ ] [Polymarket 5 Min Claude Code Bot are NUTS](https://www.youtube.com/watch?v=UNKNOWN_POLYMARKET_5MIN_BOT)
  - Why: rapid feedback markets and bot patterns; replace UNKNOWN with exact link.
  - Target: `transcripts/youtube/polymarket_trading/<video_id>_Polymarket_5_Min_Bot.txt`

- [ ] [I Built an AI Agent to Find Hidden Polymarket Alpha](https://www.youtube.com/watch?v=UNKNOWN_HIDDEN_POLYMARKET_ALPHA)
  - Why: alpha discovery research process; replace UNKNOWN with exact link.
  - Target: `transcripts/youtube/polymarket_trading/<video_id>_Hidden_Polymarket_Alpha.txt`

---

# Category: Design / frontend / web productization

Goal: improve landing pages, admin panels, demos, brand trust, and product presentation.

- [ ] [Páginas Web ANIMADAS de $10,000 con Claude Design](https://www.youtube.com/watch?v=UNKNOWN_CLAUDE_DESIGN_10000)
  - Why: high-value web presentation and design process; replace UNKNOWN with exact link.
  - Target: `transcripts/youtube/design_frontend/<video_id>_Claude_Design_10000_Websites.txt`

- [ ] [Claude Code + Playwright Crea Agentes de IA Web](https://www.youtube.com/watch?v=UNKNOWN_CLAUDE_PLAYWRIGHT_WEB_AGENTS)
  - Why: browser/web automation testing patterns; replace UNKNOWN with exact link.
  - Target: `transcripts/youtube/design_frontend/<video_id>_Claude_Playwright_Web_Agents.txt`

- [ ] [New BEST local AI image generator is here! Free & offline — Ideogram 4](https://youtu.be/OA4gchz1Zcs?si=Qzp4KoYqDoU8t5cR)
  - Channel: AI Search
  - Why: Ideogram 4 local/offline image generation via ComfyUI; strong prompt adherence, text rendering, bounding-box/canvas layout control. Useful for improving AION visual workflows beyond generic one-shot image prompts.
  - Target: `transcripts/youtube/design_frontend/OA4gchz1Zcs_Ideogram_4_Local_AI_Image_Generator.txt`

---

# Local download options

## Option A — using `yt-dlp`

```bash
mkdir -p transcripts/youtube/hermes
yt-dlp --skip-download --write-auto-subs --write-subs --sub-langs "en,es" --convert-subs srt -o "transcripts/youtube/hermes/%(id)s_%(title).80s.%(ext)s" "YOUTUBE_URL"
```

## Option B — using Python transcript API from local PC

```bash
pip install youtube-transcript-api
python scripts/fetch_youtube_transcript.py VIDEO_ID --out transcripts/youtube/hermes --title "Exact Title" --channel "Exact Channel"
```

## After adding transcripts

Run or ask AION to run:

```text
Read new transcript → create/update summary → update INDEX.md → produce applied synthesis → update workflow/skill/repo artifacts.
```
