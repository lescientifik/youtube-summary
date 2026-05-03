---
name: summarizing-youtube
description: Fetches a YouTube video transcript, saves it as markdown, then writes a structured French summary focused on learnings with a TLDR. Use whenever the user provides a YouTube URL (youtube.com/watch, youtu.be, /shorts) and asks for a summary, synthesis, "résumé", or "synthèse".
allowed-tools: Read, Write, Edit, Bash, Glob
---

# Summarizing YouTube videos

End-to-end workflow: from a YouTube URL → transcript file → structured French summary → updated index.

## Workflow

Task progress (run sequentially):

- [ ] 1. Fetch transcript via `scripts/fetch_transcript.py`
- [ ] 2. Read the transcript file
- [ ] 3. Write the summary to `summaries/<same-stem>.md`
- [ ] 4. Update `INDEX.md` with a one-line entry
- [ ] 5. Reply with the path to the summary

### 1. Fetch the transcript

Run from the project root:

```bash
uv run python .claude/skills/summarizing-youtube/scripts/fetch_transcript.py "<URL>"
```

The script prints the absolute path of the saved transcript on stdout. It is **idempotent** — if a transcript already exists for that video id, it returns the existing path instead of re-fetching. Pass `--force` to re-fetch.

If the script fails (private video, no captions, network error), report the error to the user verbatim and stop. Do not invent a summary.

### 2. Read the transcript

Read the file at the path returned by step 1. The file has YAML frontmatter (`title`, `author`, `url`, `language`, `auto_generated`, `duration`) followed by a `## Transcription` section with one `[H:MM:SS] text` line per snippet.

**Use the `duration` field to scale the summary.** Rough target: ~1 line of summary per minute of video, denser for short videos and tighter for long ones. Density beats length.

**Keep timestamps in the summary** for citations and section anchors (e.g. `### Architecture du modèle [12:30]`). They let the user jump straight to a specific point in the video when they want to re-watch.

### 3. Write the summary

Create `summaries/<same-stem>.md` (same filename as the transcript). The summary is **always in French**, regardless of the transcript language.

**Mandatory structure:**

```markdown
---
description: Synthèse de la vidéo "<titre>" — <hook en une phrase>.
video_id: <id>
url: <url>
title: '<titre>'
author: '<chaîne>'
source_transcript: ../transcripts/<même-stem>.md
created_on: <YYYY-MM-DD>
---

# <Titre de la vidéo>

**Chaîne :** <auteur>  •  **Lien :** <url>

## TL;DR

<3 à 6 phrases denses, type abstract médical : sujet de la vidéo, public cible
implicite, thèse principale, 1–2 conclusions clés, valeur d'apprentissage.
Doit permettre de décider en 15 secondes si la vidéo mérite d'être regardée.>

## Points clés à retenir

- **<concept 1>** — explication concise et actionnable.
- **<concept 2>** — …
- (5 à 10 puces, classées par importance, pas par ordre chronologique)

## Développement

### <Section thématique 1>
<Paragraphe(s) qui expliquent l'idée, donnent le contexte, citent les exemples
concrets de la vidéo. Si l'orateur cite une étude / un livre / un outil / une
personne, le mentionner explicitement.>

### <Section thématique 2>
…

## Citations marquantes

> "<citation textuelle>" — <Nom de l'orateur si identifié>, [H:MM:SS]

(0 à 5 citations. Garder seulement celles qui ont une vraie densité.)

## Ce que je peux appliquer

- <Action concrète, technique ou heuristique transposable>
- …

## Références mentionnées

- <Livre / article / outil / personne / lien — uniquement ce qui est cité dans la vidéo>

(Omettre la section si rien n'est cité.)
```

**Rules for writing the summary:**

- **Optimize for learning value.** The user cares most about what they can learn or apply. Cut anecdotes that don't carry an idea.
- **No filler.** Avoid "dans cette vidéo, l'auteur explique que…". Go straight to the substance.
- **Faithful to the source.** Don't add ideas that aren't in the transcript. If the video is light on substance, say so in the TL;DR rather than padding.
- **Length:** scale to the video using the `duration` frontmatter field. Roughly 1 line of summary per 1–2 minutes of content, but density beats length.
- **Timestamps:** use them in citations and, when useful, as section anchors (e.g. `### Architecture du modèle [12:30]`).
- **Auto-generated transcripts** (`auto_generated: true` in frontmatter) often have typos and missing punctuation — interpret charitably; don't quote verbatim if the line is garbled.

### 4. Update INDEX.md

Run the helper script — it parses the summary's frontmatter, inserts a new row at the **top** of the table (most recent first), creates `INDEX.md` with the proper header if it doesn't exist, and replaces any pre-existing row for the same `video_id` (idempotent):

```bash
uv run python .claude/skills/summarizing-youtube/scripts/update_index.py summaries/<file>.md
```

The script reads `created_on`, `title`, `author`, `url`, `video_id`, and `description` from the frontmatter — so make sure step 3 set them correctly. The hook column comes from the part of `description` after the em dash (`—`).

### 5. Reply to the user

Final reply format (concise):

```
Synthèse prête : summaries/<file>.md
TL;DR : <copie du TL;DR ou résumé en 1–2 phrases>
```

## Edge cases

- **URL already processed:** the fetch script returns the existing transcript path. Check whether `summaries/<same-stem>.md` exists. If yes, mention it to the user and ask whether to regenerate before overwriting.
- **Very long videos (>2h):** read the transcript in chunks if needed, but produce a single summary file. Prioritize the densest sections.
- **Video in a language other than French:** the transcript stays in the original language; only the summary is translated to French.
- **No transcript available:** report the error and stop. Do not fabricate.

## File layout reference

```
youtube_summary/
├── .claude/skills/summarizing-youtube/
│   ├── SKILL.md
│   └── scripts/
│       ├── fetch_transcript.py
│       └── update_index.py
├── transcripts/   # raw transcripts with frontmatter
├── summaries/     # French structured summaries
├── docs/          # research notes (if any)
└── INDEX.md       # table of all summarized videos
```
