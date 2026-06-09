# YouTube Transcript Extraction Status

Last checked: 2026-06-09

## VPS status

Transcript extraction from this VPS is currently blocked by YouTube.

Tested with `youtube_transcript_api` against priority videos, including:

- `9VlvbpXwLJs` — 30 Years of Business Knowledge in 2hrs 26mins
- `2WZAcWtwoDI` — 5 Ways I Make Money With Hermes Agent
- `G47mnkGkYwQ` — The 7 Levels of Hermes Agent Explained
- `EKVRqcpTT6s` — I Built the Ultimate Multi-Agent Workflow w/ Hermes Agent Kanban Board

Observed error:

```text
RequestBlocked
YouTube is blocking requests from your IP / cloud provider.
```

## Current solution

Use `YOUTUBE_DOWNLOAD_QUEUE.md` as the source of truth for links to download locally.

Local transcript files should be committed under:

```text
transcripts/youtube/<category>/
```

Categories currently created:

```text
hermes
business
cronjobs
cold_outreach
seo_distribution
polymarket_trading
design_frontend
```

## Local command examples

```bash
pip install youtube-transcript-api
python scripts/fetch_youtube_transcript.py 2WZAcWtwoDI \
  --out transcripts/youtube/hermes \
  --title "5 Ways I Make Money With Hermes Agent" \
  --channel "Sharbel A."
```

Or with `yt-dlp`:

```bash
yt-dlp --skip-download --write-auto-subs --write-subs --sub-langs "en,es" --convert-subs srt \
  -o "transcripts/youtube/hermes/%(id)s_%(title).80s.%(ext)s" \
  "https://www.youtube.com/watch?v=2WZAcWtwoDI"
```

## What AION will do after transcripts are pushed

1. Read new transcript files.
2. Create summaries in `summaries/`.
3. Update `INDEX.md`.
4. Create applied synthesis files.
5. Convert durable procedures into skills/workflows when useful.
