"""Fallback transcript fetcher: uses yt-dlp + curl_cffi to bypass IP-level blocks.

Use this when `fetch_transcript.py` fails because YouTube returns
RequestBlocked / IpBlocked (typical from cloud-provider IPs). This script
goes through yt-dlp's InnerTube extractors (ios / tv / web_safari / mweb),
which are more permissive than the HTML/consent route used by
`youtube-transcript-api`. It then downloads the timedtext caption track
directly with a Chrome-impersonating curl_cffi session.

Usage:
    uv run --with "yt-dlp[default,curl-cffi]" --with curl-cffi \
        python .claude/skills/summarizing-youtube/scripts/fetch_transcript_ytdlp.py <url> [--lang en] [--force]

Prints the absolute path of the saved transcript on stdout on success.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
import unicodedata
from datetime import date
from pathlib import Path
from urllib.parse import parse_qs, urlparse

PROJECT_ROOT = Path(__file__).resolve().parents[4]
TRANSCRIPTS_DIR = PROJECT_ROOT / "transcripts"

PLAYER_CLIENTS = "ios,tv,web_safari,mweb"


def extract_video_id(url: str) -> str:
    parsed = urlparse(url)
    host = (parsed.hostname or "").lower().lstrip("www.")
    if host == "youtu.be":
        candidate = parsed.path.lstrip("/").split("/")[0]
    elif host.endswith("youtube.com"):
        if parsed.path == "/watch":
            candidate = parse_qs(parsed.query).get("v", [""])[0]
        else:
            parts = [p for p in parsed.path.split("/") if p]
            candidate = parts[1] if len(parts) >= 2 else ""
    else:
        candidate = url
    if not re.fullmatch(r"[A-Za-z0-9_-]{11}", candidate):
        raise ValueError(f"Could not extract a valid YouTube video id from: {url!r}")
    return candidate


def slugify(text: str, max_len: int = 60) -> str:
    norm = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    norm = re.sub(r"[^a-zA-Z0-9]+", "-", norm).strip("-").lower()
    return norm[:max_len].rstrip("-") or "video"


def fmt_ts(seconds: float) -> str:
    total = int(seconds)
    h, rem = divmod(total, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def run_ytdlp_info(url: str, work_dir: Path) -> dict:
    """Invoke yt-dlp to dump the player's info.json (no media download)."""
    cmd = [
        "yt-dlp",
        "--skip-download",
        "--write-info-json",
        "--no-write-subs",
        "--impersonate", "chrome",
        "--extractor-args", f"youtube:player_client={PLAYER_CLIENTS}",
        "--ignore-no-formats-error",
        "-o", "%(id)s.%(ext)s",
        url,
    ]
    proc = subprocess.run(cmd, cwd=work_dir, capture_output=True, text=True)
    if proc.returncode not in (0,):
        sys.stderr.write(proc.stderr)
        raise RuntimeError(f"yt-dlp failed (rc={proc.returncode})")
    info_files = list(work_dir.glob("*.info.json"))
    if not info_files:
        raise RuntimeError("yt-dlp produced no info.json")
    return json.loads(info_files[0].read_text())


def pick_caption_url(info: dict, preferred_lang: str | None) -> tuple[str, str, bool]:
    """Return (timedtext_url, language_code, is_generated).

    Order of preference:
      1. Manual subtitles in `preferred_lang`
      2. Automatic captions in `<preferred_lang>-orig` (true ASR original)
      3. Automatic captions in `preferred_lang`
      4. Any `*-orig` automatic caption (original language ASR)
      5. First available caption
    """
    subs = info.get("subtitles") or {}
    auto = info.get("automatic_captions") or {}

    def best_url(tracks: list[dict]) -> str | None:
        for t in tracks:
            if t.get("ext") == "json3":
                return t["url"]
        return tracks[0]["url"] if tracks else None

    candidates: list[tuple[str, list[dict], bool]] = []
    if preferred_lang:
        if preferred_lang in subs:
            candidates.append((preferred_lang, subs[preferred_lang], False))
        orig_key = f"{preferred_lang}-orig"
        if orig_key in auto:
            candidates.append((preferred_lang, auto[orig_key], True))
        if preferred_lang in auto:
            candidates.append((preferred_lang, auto[preferred_lang], True))

    for lang, tracks in auto.items():
        if lang.endswith("-orig"):
            candidates.append((lang.removesuffix("-orig"), tracks, True))

    for lang, tracks in subs.items():
        if lang == "live_chat":
            continue
        candidates.append((lang, tracks, False))

    for lang, tracks in auto.items():
        candidates.append((lang, tracks, True))

    for lang, tracks, generated in candidates:
        url = best_url(tracks)
        if url:
            return url, lang, generated
    raise RuntimeError("No caption track found in info.json")


def fetch_caption_json3(url: str) -> dict:
    """Download a json3 timedtext file with Chrome impersonation."""
    from curl_cffi import requests as curl_requests

    s = curl_requests.Session(impersonate="chrome120")
    r = s.get(url, timeout=30)
    r.raise_for_status()
    return json.loads(r.content)


def lines_from_json3(caps: dict) -> list[tuple[float, str]]:
    """Convert a json3 ASR caption dump into [(seconds, text), ...].

    json3 emits a rolling caption window: many events use `aAppend=1` to add
    words to the current line. We treat events without `aAppend` as line
    starts and concatenate appended segments. We then drop lines that are
    strict prefixes of the next line (the rolling rebuilds the same sentence).
    """
    raw: list[tuple[float, str]] = []
    current_text: list[str] = []
    current_start: float | None = None

    for e in caps.get("events", []):
        if "segs" not in e:
            continue
        text = "".join(seg.get("utf8", "") for seg in e["segs"])
        if e.get("aAppend"):
            current_text.append(text)
            continue
        if current_start is not None:
            joined = re.sub(r"\s+", " ", "".join(current_text)).strip()
            if joined:
                raw.append((current_start, joined))
        current_start = (e.get("tStartMs") or 0) / 1000.0
        current_text = [text]

    if current_start is not None:
        joined = re.sub(r"\s+", " ", "".join(current_text)).strip()
        if joined:
            raw.append((current_start, joined))

    deduped: list[tuple[float, str]] = []
    for i, (start, text) in enumerate(raw):
        if i + 1 < len(raw) and raw[i + 1][1].startswith(text):
            continue
        deduped.append((start, text))
    return deduped


def render_markdown(
    *,
    url: str,
    video_id: str,
    title: str,
    author: str,
    language_code: str,
    is_generated: bool,
    duration_sec: float,
    lines: list[tuple[float, str]],
) -> str:
    duration_str = fmt_ts(duration_sec or (lines[-1][0] if lines else 0))
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
    body = [
        f"# {title}",
        "",
        f"**Chaîne :** {author}  ",
        f"**URL :** {url}  ",
        f"**Durée :** {duration_str}",
        "",
        "## Transcription",
        "",
    ]
    for start, text in lines:
        body.append(f"[{fmt_ts(start)}] {text}")
    return frontmatter + "\n".join(body) + "\n"


def existing_path_for(video_id: str) -> Path | None:
    matches = list(TRANSCRIPTS_DIR.glob(f"*-{video_id}.md"))
    return matches[0] if matches else None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("--lang", default=None, help="Preferred caption language code (e.g. en, fr)")
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

    with tempfile.TemporaryDirectory() as tmp:
        work_dir = Path(tmp)
        try:
            info = run_ytdlp_info(args.url, work_dir)
        except Exception as exc:
            print(f"ERROR: yt-dlp info extraction failed: {exc}", file=sys.stderr)
            return 4

    title = info.get("title") or "Unknown title"
    author = info.get("uploader") or info.get("channel") or "Unknown channel"
    duration_sec = float(info.get("duration") or 0)

    try:
        cap_url, language_code, is_generated = pick_caption_url(info, args.lang)
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 4

    try:
        caps = fetch_caption_json3(cap_url)
    except Exception as exc:
        print(f"ERROR: failed to download captions: {exc}", file=sys.stderr)
        return 4

    lines = lines_from_json3(caps)
    if not lines:
        print("ERROR: caption file parsed but produced no lines", file=sys.stderr)
        return 4

    markdown = render_markdown(
        url=args.url,
        video_id=video_id,
        title=title,
        author=author,
        language_code=language_code,
        is_generated=is_generated,
        duration_sec=duration_sec,
        lines=lines,
    )
    filename = f"{date.today().isoformat()}-{slugify(title)}-{video_id}.md"
    out_path = TRANSCRIPTS_DIR / filename
    out_path.write_text(markdown, encoding="utf-8")
    print(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
