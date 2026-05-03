"""Insert (or refresh) a row in INDEX.md for a given summary file.

Usage:
    uv run python .claude/skills/summarizing-youtube/scripts/update_index.py <summary.md>

- Creates INDEX.md with the proper header if it does not exist.
- New rows are inserted at the TOP of the table (most recent first).
- If a row for the same video_id already exists, it is replaced in place
  (no duplicates, no reordering of unrelated rows).

Reads from the summary's YAML frontmatter:
    created_on, title, author, url, video_id, description.
The hook column is derived from the `description` field (everything after
the em dash, or the full description if none).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[4]
INDEX_PATH = PROJECT_ROOT / "INDEX.md"
SUMMARIES_DIR = PROJECT_ROOT / "summaries"

INDEX_HEADER = (
    "# Index des vidéos synthétisées\n"
    "\n"
    "| Date | Titre | Chaîne | TL;DR | Synthèse |\n"
    "|------|-------|--------|-------|----------|\n"
)


def parse_frontmatter(text: str) -> dict[str, str]:
    """Extract YAML-ish key/value pairs from a markdown frontmatter block.

    Intentionally minimal: handles `key: value` lines, strips matching
    surrounding quotes from values. Does not support nested structures —
    the summary frontmatter is flat by design.
    """
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        raise ValueError("Summary file has no YAML frontmatter")

    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        fields[key] = value
    return fields


def extract_hook(description: str) -> str:
    """Pull the post-em-dash hook out of a description like
    `Synthèse de la vidéo "..." — <hook>`. Falls back to the full description.
    """
    for sep in (" — ", " - ", " – "):
        if sep in description:
            return description.split(sep, 1)[1].rstrip(".").strip()
    return description.rstrip(".").strip()


def relative_to_root(path: Path) -> str:
    """Return a forward-slash path relative to PROJECT_ROOT."""
    return path.resolve().relative_to(PROJECT_ROOT).as_posix()


def build_row(*, summary_path: Path, fields: dict[str, str]) -> str:
    """Render a single markdown table row for a summary file."""
    rel_path = relative_to_root(summary_path)
    title = fields.get("title", "Sans titre").replace("|", "\\|")
    author = fields.get("author", "—").replace("|", "\\|")
    date_str = fields.get("created_on", "")
    hook = extract_hook(fields.get("description", "")).replace("|", "\\|").replace("\n", " ")
    return f"| {date_str} | [{title}]({rel_path}) | {author} | {hook} | [📄]({rel_path}) |\n"


def video_id_in_row(row: str, video_id: str) -> bool:
    """Detect rows that reference this video id (matches against the file path)."""
    return f"-{video_id}.md" in row


def upsert_row(existing: str, new_row: str, video_id: str) -> str:
    """Insert new_row at the top of the table, replacing any pre-existing row
    for the same video id. Preserves header, separator, and trailing content.
    """
    lines = existing.splitlines(keepends=True)

    # Find the table separator line (|---|---|...)
    sep_idx = next(
        (i for i, line in enumerate(lines) if re.match(r"^\|\s*-+", line)),
        None,
    )
    if sep_idx is None:
        # Malformed index — rebuild from scratch
        return INDEX_HEADER + new_row

    # Drop any existing row for the same video id (rows live after the separator)
    body_start = sep_idx + 1
    kept = [line for line in lines[body_start:] if not video_id_in_row(line, video_id)]
    return "".join(lines[: body_start]) + new_row + "".join(kept)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("summary", type=Path, help="Path to the summary markdown file")
    args = parser.parse_args()

    summary_path: Path = args.summary
    if not summary_path.is_absolute():
        summary_path = (Path.cwd() / summary_path).resolve()
    if not summary_path.is_file():
        print(f"ERROR: summary file not found: {summary_path}", file=sys.stderr)
        return 2

    text = summary_path.read_text(encoding="utf-8")
    try:
        fields = parse_frontmatter(text)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 3

    video_id = fields.get("video_id")
    if not video_id:
        print("ERROR: summary frontmatter is missing `video_id`", file=sys.stderr)
        return 3

    new_row = build_row(summary_path=summary_path, fields=fields)

    if INDEX_PATH.exists():
        updated = upsert_row(INDEX_PATH.read_text(encoding="utf-8"), new_row, video_id)
    else:
        updated = INDEX_HEADER + new_row

    INDEX_PATH.write_text(updated, encoding="utf-8")
    print(INDEX_PATH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
