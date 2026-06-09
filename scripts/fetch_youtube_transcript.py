#!/usr/bin/env python3
"""Fetch a YouTube transcript into transcripts/youtube/.

Designed to be run from Andre's local PC/network when the VPS is blocked by
YouTube. The VPS currently receives RequestBlocked from youtube_transcript_api.

Usage:
    python scripts/fetch_youtube_transcript.py 2WZAcWtwoDI --out transcripts/youtube
    python scripts/fetch_youtube_transcript.py https://www.youtube.com/watch?v=2WZAcWtwoDI --langs en es
"""
from __future__ import annotations

import argparse
import re
from datetime import datetime, timezone
from pathlib import Path

from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(value: str) -> str:
    value = value.strip()
    patterns = [
        r"(?:v=)([A-Za-z0-9_-]{6,})",
        r"youtu\.be/([A-Za-z0-9_-]{6,})",
        r"youtube\.com/shorts/([A-Za-z0-9_-]{6,})",
        r"^([A-Za-z0-9_-]{6,})$",
    ]
    for pattern in patterns:
        match = re.search(pattern, value)
        if match:
            return match.group(1)
    raise SystemExit(f"Could not extract YouTube video id from: {value}")


def clean_filename(text: str) -> str:
    text = re.sub(r"[^A-Za-z0-9_-]+", "_", text).strip("_")
    return text[:90] or "youtube_transcript"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("video", help="YouTube video ID or URL")
    parser.add_argument("--out", default="transcripts/youtube", help="Output directory")
    parser.add_argument("--langs", nargs="+", default=["en", "es"], help="Preferred transcript languages")
    parser.add_argument("--title", default="", help="Optional title for filename/header")
    parser.add_argument("--channel", default="", help="Optional channel for header")
    args = parser.parse_args()

    video_id = extract_video_id(args.video)
    api = YouTubeTranscriptApi()
    transcript = api.fetch(video_id, languages=args.langs)

    title_part = clean_filename(args.title) if args.title else video_id
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{video_id}_{title_part}.txt"

    lines = [
        f"Video URL: https://www.youtube.com/watch?v={video_id}",
        f"Video ID: {video_id}",
        f"Title: {args.title or ''}",
        f"Channel: {args.channel or ''}",
        f"Date downloaded: {datetime.now(timezone.utc).isoformat()}",
        f"Language requested: {', '.join(args.langs)}",
        "",
        "Transcript:",
    ]
    lines.extend(item.text.replace("\n", " ").strip() for item in transcript if item.text.strip())
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(out_path)


if __name__ == "__main__":
    main()
