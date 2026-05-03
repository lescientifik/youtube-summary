# YouTube Summary

Synthèses structurées de vidéos YouTube à partir de leurs transcriptions audio, en français.

L'objectif : transformer une URL YouTube en un fichier markdown qui me permet de **décider en 15 secondes** si la vidéo m'intéresse (TLDR), puis **d'apprendre l'essentiel sans la regarder** (synthèse structurée avec timestamps).

## Comment ça marche

Tout est packagé dans un skill Claude Code local : [`.claude/skills/summarizing-youtube/`](./.claude/skills/summarizing-youtube/SKILL.md). Dans une session Claude Code lancée à la racine de ce repo :

```
> Synthétise cette vidéo : https://www.youtube.com/watch?v=...
```

Claude :

1. exécute `fetch_transcript.py` qui récupère le transcript dans la langue originale et l'écrit dans `transcripts/` ;
2. lit le transcript ;
3. écrit une synthèse française dans `summaries/` (TLDR, points clés, développement par section avec timestamps, citations, ce que je peux appliquer, références) ;
4. exécute `update_index.py` qui ajoute une ligne en haut de [`INDEX.md`](./INDEX.md).

## Structure

```
.
├── .claude/skills/summarizing-youtube/
│   ├── SKILL.md                 # Workflow et template de synthèse
│   └── scripts/
│       ├── fetch_transcript.py  # URL → transcripts/<date>-<slug>-<id>.md
│       └── update_index.py      # summaries/*.md → row dans INDEX.md
├── transcripts/                 # Transcriptions brutes avec timestamps
├── summaries/                   # Synthèses françaises structurées
├── INDEX.md                     # Index de toutes les vidéos synthétisées
└── pyproject.toml               # uv project (youtube-transcript-api, requests)
```

## Utilisation directe des scripts

```bash
# Récupérer un transcript (idempotent ; --force pour re-télécharger)
uv run python .claude/skills/summarizing-youtube/scripts/fetch_transcript.py "<URL>"

# Mettre à jour l'index après création/édition d'une synthèse
uv run python .claude/skills/summarizing-youtube/scripts/update_index.py summaries/<file>.md
```

## Conventions

- **Synthèses en français**, indépendamment de la langue de la vidéo.
- **Transcript dans la langue originale** uniquement (pas de traduction auto).
- Chaque transcript et chaque synthèse partagent le même nom de fichier : `YYYY-MM-DD-<slug>-<videoId>.md`.
- Les timestamps `[H:MM:SS]` sont conservés dans les transcripts et utilisés dans les synthèses pour les citations et les ancres de section, afin de pouvoir sauter directement au passage qui m'intéresse.
