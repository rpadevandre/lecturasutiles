# YouTube Download Queue for AION Knowledge Base

Purpose: keep a clean queue of YouTube videos whose transcripts should be downloaded locally and added to this repo so AION can learn from them.

## Why this file exists

The VPS/cloud IP is currently blocked by YouTube transcript access. Attempted transcript extraction with `youtube_transcript_api` returned `RequestBlocked` for priority videos. The reliable workflow is:

1. Andre downloads/transcribes from local PC/network.
2. Save transcript files into `transcripts/youtube/`.
3. Run/import summaries into `summaries/`.
4. AION reads `INDEX.md` + new summaries and converts them into workflows/artifacts.

## Priority 1 — already useful / AION operating system

- [ ] [30 Years of Business Knowledge in 2hrs 26mins](https://www.youtube.com/watch?v=9VlvbpXwLJs)
  - Channel: Simon Squibb
  - Why: business fundamentals, brand, purpose, sales, delayed gratification.
  - Target file: `transcripts/youtube/9VlvbpXwLJs_30_Years_of_Business_Knowledge_in_2hrs_26mins.txt`

- [ ] [5 Ways I Make Money With Hermes Agent](https://www.youtube.com/watch?v=2WZAcWtwoDI)
  - Channel: Sharbel A.
  - Why: Hermes as junior operator, productized services, human-in-the-loop monetization.
  - Target file: `transcripts/youtube/2WZAcWtwoDI_5_Ways_I_Make_Money_With_Hermes_Agent.txt`

- [ ] [The 7 Levels of Hermes Agent Explained](https://www.youtube.com/watch?v=G47mnkGkYwQ)
  - Channel: David Ondrej
  - Why: Hermes setup, skills, cronjobs, Kanban, memory, MCP.
  - Target file: `transcripts/youtube/G47mnkGkYwQ_The_7_Levels_of_Hermes_Agent_Explained.txt`

- [ ] [I Built the Ultimate Multi-Agent Workflow w/ Hermes Agent Kanban Board](https://www.youtube.com/watch?v=EKVRqcpTT6s)
  - Channel: Tonbi's AI Garage
  - Why: multi-agent coordination, Kanban as operating layer.
  - Target file: `transcripts/youtube/EKVRqcpTT6s_I_Built_the_Ultimate_Multi_Agent_Workflow_w_Hermes_Agent_Kanban_Board.txt`

## Priority 2 — Hermes / AI agents to process next

- [ ] [100 hours of Hermes Agent lessons in 23 minutes](https://www.youtube.com/watch?v=k5NhsF7t68M)
  - Why: concentrated Hermes usage lessons.

- [ ] [Hermes /goal is insane… just watch](https://www.youtube.com/watch?v=9oOZ3PB6n4Y)
  - Why: persistent goals / long-running objectives.

- [ ] [The Only Hermes Agent Tutorial You'll Need in 2026](https://www.youtube.com/watch?v=8bYMgvJt5Ws)
  - Why: broad Hermes setup/use tutorial.

- [ ] [Hermes Agent Tutorial for Beginners - Crash Course](https://www.youtube.com/watch?v=6QZBep7mW0c)
  - Why: setup fundamentals, useful for Andre-side environment.

- [ ] [Hermes Agent - Full Course & Setup Guide](https://www.youtube.com/watch?v=mTYxpIRK7xA)
  - Why: full Hermes course/setup.

- [ ] [I gave my Hermes Agent a phone number](https://www.youtube.com/watch?v=zHE434sBw2U)
  - Why: voice/phone agent integration patterns.

## Priority 3 — business, sales and productized services

- [ ] [How to Build & Sell AI Agents in 2026: Ultimate Beginner's Guide](https://www.youtube.com/watch?v=AYQtRqW1xX4)
  - Channel: Liam Ottley
  - Why: AI automation agency / productized AI agents.

- [ ] [The #1 Claude AI Side Hustle Nobody Is Talking About](https://www.youtube.com/watch?v=uJeHGmMir5Q)
  - Channel: Patrick Dang
  - Why: B2B AI services, LinkedIn/outreach, selling expertise.

- [ ] [She Made $1.2M Selling AI Agents](https://www.youtube.com/watch?v=UNKNOWN_SHE_MADE_12M_AI_AGENTS)
  - Why: packaging AI-agent services; replace UNKNOWN if local search finds exact ID.

- [ ] [Claude Code SEO: How I Got 50,000 Clicks Per Month](https://www.youtube.com/watch?v=4IyJm1i__ag)
  - Channel: Jono Catliff
  - Why: SEO as distribution engine for incubated businesses.

- [ ] [This Boring Website Earns $6M/Year. Here's How to Clone it](https://www.youtube.com/watch?v=nQOGK72IHx8)
  - Channel: Jonathan's Jam
  - Why: utility site / boring business / SEO monetization model.

- [ ] [How selling Ebooks with Claude changed my life](https://www.youtube.com/watch?v=nmRWmF2Umes)
  - Channel: Molly Keyser
  - Why: lead magnet → email list → pre-sell flow.

## Priority 4 — cold email / outbound to research

These are not yet canonical. Use local YouTube search and replace/add exact links if better videos are found.

- [ ] [This Cold Email Strategy Makes $160k/mo for My SaaS](https://www.youtube.com/watch?v=ACMED_IDZb8)
  - Why: SaaS cold email strategy.

- [ ] [How To Use AI to Automate Cold Email Outreach](https://www.youtube.com/watch?v=6eLWP3a-9Uo)
  - Why: AI-assisted outreach workflow.

- [ ] [How I grew my SaaS to $4,000 MRR with cold emails](https://www.youtube.com/watch?v=KJb_nfR6gJk)
  - Why: realistic small-SaaS cold email validation.

## Local download options

### Option A — using `yt-dlp`

```bash
mkdir -p transcripts/youtube
yt-dlp --skip-download --write-auto-subs --write-subs --sub-langs "en,es" --convert-subs srt -o "transcripts/youtube/%(id)s_%(title).80s.%(ext)s" "YOUTUBE_URL"
```

Then convert `.srt` to `.txt` if needed.

### Option B — using Python transcript API from local PC

```bash
pip install youtube-transcript-api
python scripts/fetch_youtube_transcript.py VIDEO_ID --out transcripts/youtube
```

## Import convention

Transcript files should include:

```text
Video URL:
Channel:
Title:
Date downloaded:
Language:

Transcript:
...
```

## What AION should do after transcripts are added

For each transcript:

1. Generate/update `summaries/<clean_title>.md`.
2. Update `INDEX.md` with tags, purpose, useful/not useful.
3. Generate a synthesis if 3+ videos share a theme.
4. Extract durable procedures into skills only when actionable.
5. Apply insights to repo artifacts, not only notes.
