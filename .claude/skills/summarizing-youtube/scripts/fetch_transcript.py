"""Fetch a YouTube video transcript in its original language and save it as markdown.

Usage:
    uv run python .claude/skills/summarizing-youtube/scripts/fetch_transcript.py <url> [--force]

Prints the absolute path of the saved transcript file to stdout on success.
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import requests
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.proxies import GenericProxyConfig  # noqa: F401  (kept for future proxy support)


PROJECT_ROOT = Path(__file__).resolve().parents[4]
TRANSCRIPTS_DIR = PROJECT_ROOT / "transcripts"


def extract_video_id(url: str) -> str:
    """Extract the 11-char video id from any common YouTube URL form."""
    parsed = urlparse(url)
    host = (parsed.hostname or "").lower().lstrip("www.")

    if host == "youtu.be":
        candidate = parsed.path.lstrip("/").split("/")[0]
    elif host.endswith("youtube.com"):
        if parsed.path == "/watch":
            candidate = parse_qs(parsed.query).get("v", [""])[0]
        else:
            # /shorts/<id>, /embed/<id>, /v/<id>, /live/<id>
            parts = [p for p in parsed.path.split("/") if p]
            candidate = parts[1] if len(parts) >= 2 else ""
    else:
        candidate = url  # last-ditch: assume the user passed a raw id

    if not re.fullmatch(r"[A-Za-z0-9_-]{11}", candidate):
        raise ValueError(f"Could not extract a valid YouTube video id from: {url!r}")
    return candidate


def fetch_metadata(url: str) -> dict[str, str]:
    """Fetch title + author via YouTube's public oEmbed endpoint (no API key)."""
    resp = requests.get(
        "https://www.youtube.com/oembed",
        params={"url": url, "format": "json"},
        timeout=15,
    )
    resp.raise_for_status()
    data = resp.json()
    return {
        "title": data.get("title", "Unknown title"),
        "author": data.get("author_name", "Unknown channel"),
    }


def slugify(text: str, max_len: int = 60) -> str:
    """Conservative ASCII slug for filenames."""
    normalized = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    normalized = re.sub(r"[^a-zA-Z0-9]+", "-", normalized).strip("-").lower()
    return normalized[:max_len].rstrip("-") or "video"


def pick_original_transcript(video_id: str):
    """Pick the transcript in the video's original language.

    Heuristic: prefer the first manually-created transcript (uploaders typically
    create captions in the original language). Fallback to the first
    auto-generated one. Skip translation-only entries.
    """
    transcript_list = YouTubeTranscriptApi().list(video_id)
    manual = [t for t in transcript_list if not t.is_generated]
    if manual:
        return manual[0]
    generated = [t for t in transcript_list if t.is_generated]
    if generated:
        return generated[0]
    raise RuntimeError(f"No transcript available for video {video_id}")


def format_timestamp(seconds: float) -> str:
    """Format seconds as H:MM:SS or M:SS."""
    total = int(seconds)
    h, rem = divmod(total, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def render_markdown(
    *,
    url: str,
    video_id: str,
    title: str,
    author: str,
    language_code: str,
    is_generated: bool,
    snippets,
) -> str:
    """Build the transcript markdown: YAML frontmatter + timestamped lines.

    Each snippet keeps its `[H:MM:SS]` prefix so the summary writer can cite
    timestamps and the user can jump directly to a section in the video. The
    total duration is also exposed in the frontmatter for length-scaling.
    """
    snippet_list = list(snippets)
    duration_sec = (snippet_list[-1].start + snippet_list[-1].duration) if snippet_list else 0.0
    duration_str = format_timestamp(duration_sec)
    today = date.today().isoformat()

    frontmatter = (
        "---\n"
        f'description: Transcription brute de la vidéo YouTube "{title}".\n'
        f"video_id: {video_id}\n"
        f"url: {url}\n"
        f"title: {title!r}\n"
        f"author: {author!r}\n"
        f"language: {language_code}\n"
        f"auto_generated: {str(is_generated).lower()}\n"
        f"duration: {duration_str}\n"
        f"fetched_on: {today}\n"
        "---\n\n"
    )

    body_lines = [
        f"# {title}",
        "",
        f"**Chaîne :** {author}  ",
        f"**URL :** {url}  ",
        f"**Durée :** {duration_str}",
        "",
        "## Transcription",
        "",
    ]
    for snip in snippet_list:
        text = snip.text.strip()
        if text:
            body_lines.append(f"[{format_timestamp(snip.start)}] {text}")
    return frontmatter + "\n".join(body_lines) + "\n"


def existing_path_for(video_id: str) -> Path | None:
    """Return existing transcript path for this video id, if any."""
    matches = list(TRANSCRIPTS_DIR.glob(f"*-{video_id}.md"))
    return matches[0] if matches else None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("--force", action="store_true", help="Re-fetch even if a transcript already exists")
    args = parser.parse_args()

    TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)

    try:
        video_id = extract_video_id(args.url)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if not args.force:
        existing = existing_path_for(video_id)
        if existing:
            print(existing)
            return 0

    try:
        meta = fetch_metadata(args.url)
    except requests.RequestException as exc:
        print(f"ERROR: failed to fetch video metadata: {exc}", file=sys.stderr)
        return 3

    try:
        transcript = pick_original_transcript(video_id)
        fetched = transcript.fetch()
    except Exception as exc:
        print(f"ERROR: could not fetch transcript: {exc}", file=sys.stderr)
        return 4

    markdown = render_markdown(
        url=args.url,
        video_id=video_id,
        title=meta["title"],
        author=meta["author"],
        language_code=transcript.language_code,
        is_generated=transcript.is_generated,
        snippets=fetched,
    )

    filename = f"{date.today().isoformat()}-{slugify(meta['title'])}-{video_id}.md"
    out_path = TRANSCRIPTS_DIR / filename
    out_path.write_text(markdown, encoding="utf-8")
    print(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
