---
description: Synthèse de la vidéo "Pi Coding Agent (Free Course)" — tour complet de Pi, un agent de codage open source minimaliste (4 outils, system prompt < 1000 tokens) entièrement extensible en TypeScript.
video_id: BZ0w0JhPQ9o
url: https://www.youtube.com/watch?v=BZ0w0JhPQ9o
title: 'Pi Coding Agent (Free Course)'
author: 'Owain Lewis'
source_transcript: ../transcripts/2026-05-03-pi-coding-agent-free-course-BZ0w0JhPQ9o.md
created_on: 2026-05-03
---

# Pi Coding Agent (Free Course)

**Chaîne :** Owain Lewis  •  **Lien :** https://www.youtube.com/watch?v=BZ0w0JhPQ9o

## TL;DR

Cours complet sur **Pi**, un agent de codage CLI open source qui se positionne en alternative minimaliste à Claude Code et Codex : seulement quatre outils (`read`, `bash`, `edit`, `write`), un system prompt < 1000 tokens (vs ~14 000 pour Claude), aucun prompt de permission, et compatibilité avec tous les modèles (OpenAI, OpenRouter, Ollama, Anthropic via API). Sa vraie valeur est l'**extensibilité** : tout — UI, outils, workflows multi-étapes — se code en TypeScript dans `~/.pi/agent/extensions`, avec un mécanisme de `skills` séparé pour les procédures déclenchables à la demande. L'auteur démontre une extension `workflow` qui orchestre spec → code → review (contexte frais) → fix → tests → vérification de manière déterministe, sans avoir à reprompter l'agent. Verdict : excellent agent à adopter en complément de Claude Code, mais bloquant majeur si vous dépendez de l'abonnement Anthropic — Anthropic a banni le bridging vers Pi, il faut payer à l'API.

## Points clés à retenir

- **Philosophie minimaliste** — quatre outils seulement, le `bash` couvre tout le reste ; les LLM sont entraînés en RL sur bash et savent l'exploiter.
- **System prompt customisable** — `~/.pi/agent/system.md` remplace, `append_system.md` ajoute. Permet de spécialiser l'agent en dehors du codage.
- **Pas de permissions par défaut** — Pi tourne avec accès complet ; argument : les utilisateurs cliquent "Accept" mécaniquement de toute façon. Une extension peut réintroduire un gate.
- **Extensions = code TypeScript** auto-chargé depuis `~/.pi/agent/extensions/`. Hot-reload via `/reload`. C'est le différenciateur principal vs autres agents.
- **Workflows déterministes** — encoder un pipeline (spec → write → review → fix → test → verify) dans une extension élimine la boucle manuelle de reprompting.
- **Contextes séparés par étape** — l'extension peut demander à l'agent de flusher son contexte pour des étapes comme la code review, ce qui évite le biais de l'agent qui review son propre code.
- **Skills ≠ extensions** — extensions pour exécuter du code et modifier le comportement ; skills pour injecter des instructions sur des tâches spécifiques (review, refactor, plan, spec).
- **Repo externe pour les skills** — l'auteur garde ses skills dans un git repo référencé dans la config plutôt qu'éparpillés dans des dotfiles, retour d'expérience tiré de la pagaille avec Claude Code.
- **Compatibilité OpenRouter / Ollama** — un seul API key OpenRouter donne accès à tous les modèles ; Ollama pour le local. Attention au coût (l'auteur a brûlé 15 $ rapidement sur OpenRouter avec un top-tier).
- **Bloquant Anthropic** — impossible de brancher un abonnement Claude Pro/Max ; Anthropic a explicitement banni Pi. Il faut une clé API → plus cher.

## Développement

### Installation et premier contact [0:46]

Installation en une commande depuis `pi.dev`. Lancé via `pi`, login OAuth pour OpenAI / GitHub Copilot / Google Cloud / Anthropic. Sélection de modèle via `/model`, niveau de raisonnement réglable (l'auteur utilise `gpt-5.3 codex` en high reasoning). Pour OpenRouter, exporter `OPENROUTER_API_KEY` avant de lancer l'agent débloque l'accès à GLM 5, Qwen, modèles open source Google, etc.

### Anatomie du tooling [4:51]

Quatre outils uniquement : `read`, `bash`, `edit`, `write`. Le pari : `bash` couvre tout le reste car les modèles modernes sont massivement entraînés en RL sur cet outil. Aucune permission demandée à l'exécution — choix philosophique assumé. Hotkey utile : **Shift+Tab** cycle les niveaux de raisonnement, et un raccourci dédié exécute une commande bash arbitraire sans quitter l'agent (pratique pour ouvrir l'éditeur).

### Sessions et navigation [5:51]

`/export` produit un HTML de la session, `/import` la recharge. `/tree` affiche l'arbre de session, `/fork` permet de repartir d'un point antérieur quand l'agent a pris la mauvaise direction — évite de reprompter une longue conversation pour le ramener.

### Configuration [6:54]

Tout vit dans `~/.pi/`. `agent/agents.md` est lu à chaque démarrage (équivalent global du `CLAUDE.md`) ; un `agents.md` local au repo est aussi détecté. Settings en JSON dans le même dossier, plus les sous-dossiers `extensions/`, `sessions/`, `skills/`.

### System prompt customisable [8:10]

Le system prompt par défaut est minuscule (~"tu es un agent de codage qui aide en lisant, exécutant et éditant"). Deux mécanismes :
- `append_system.md` → ajoute des instructions au prompt par défaut.
- `system.md` → le remplace entièrement. Cas d'usage cité : utiliser Pi pour des tâches non-coding sans que le prompt commence par "you are a coding assistant".

### Extensions, le vrai différenciateur [9:22]

Fichiers TypeScript déposés dans `~/.pi/agent/extensions/`, auto-chargés. Conseil méthodologique de l'auteur : **utiliser Pi lui-même pour écrire ses extensions**, car il a accès à sa propre documentation et à son code source — il sait écrire des extensions pour lui-même.

**Démo simple [10:11]** — extension UI qui affiche le statut Git (branche, fichiers unstaged/untracked) en bas du terminal. Build → `/reload` → visible immédiatement.

**Démo non-triviale [12:18] — extension `workflow`** : encode un pipeline déterministe `spec → write → review → fix → test → verify`. Lancée sur une spec d'API CRUD FastAPI, l'agent traverse seul les six étapes en gérant son propre état via un outil `workflow.next` — sans intervention humaine entre les étapes. **Point clé [15:46]** : la review se fait avec un contexte frais, ce qui évite le biais où un agent valide complaisamment son propre code. L'auteur insiste : 20 minutes pour coder cette extension, gain énorme par rapport au reprompting manuel.

### Skills [18:04]

Procédures opératoires standard injectables à la demande via `/skill <nom>`. Stockables dans `~/.pi/agent/skills/` ou dans le projet. **Pratique recommandée** : tenir ses skills dans un git repo externe référencé dans la config, plutôt qu'éparpillés dans des dotfiles. L'auteur a transposé son workflow habituel : `spec`, `plan`, `task`, `review`, `refactor`, `debug`, `coverage`. Démo : skill `spec` génère un cahier des charges → skill `plan` le découpe en phases → implémentation phase par phase.

### Migration depuis Claude Code [22:47]

| Claude Code | Pi |
|---|---|
| `claude.md` | `agents.md` |
| Permission modes | Aucun (par défaut) |
| MCP servers | Pas natif → via extension |
| Hooks | Extensions |
| Sub-agents | Non supporté |
| Todo list tracking | Non |
| System prompt ~14k tokens | < 1k tokens, customisable |

Compaction : commande identique. Le gain en fenêtre de contexte est significatif.

### Modes avancés [24:15]

Mode one-shot (commande unique non-interactive), mode JSON (sortie structurée d'événements), SDK pour embarquer Pi dans une app, mode RPC. L'auteur ne les utilise pas personnellement mais signale leur existence.

### Verdict honnête [27:10]

Pi en complément de Claude Code, **pas en remplacement**. Seul vrai blocage : impossible d'utiliser son abonnement Anthropic (banni). Hors écosystème Anthropic, Pi serait son agent quotidien : minimalisme + customisation totale.

## Citations marquantes

> "Most permissions that you get with a tool like Claude code, people are just mindlessly clicking accept anyway, and so there isn't really any point to that." — Owain Lewis, [5:33]

> "What's really interesting about this agent, it can read its own documentation. […] It knows how to write extensions for itself." — Owain Lewis, [11:01]

> "We can implement [an entire AI coding workflow] in deterministic extensions, and I think this is such a powerful idea." — Owain Lewis, [16:01]

## Ce que je peux appliquer

- **Encoder mes boucles répétitives en extensions déterministes** plutôt que de reprompter manuellement le cycle write → review → fix → test. Le pattern est transférable à Claude Code via hooks/sub-agents.
- **Forcer un contexte frais pour la phase de review** (ou la déléguer à un sous-agent isolé) pour éviter le biais d'auto-validation par l'agent qui a écrit le code.
- **Garder mes skills dans un git repo dédié** référencé dans la config, pas dans `~/.claude/` éparpillé. Versionnable, partageable, swappable selon le contexte projet.
- **Tester Pi avec OpenRouter ou Ollama** comme bac à sable pour expérimenter des modèles non-Anthropic, sans toucher au workflow Claude Code principal.
- **Demander à un agent de lire sa propre doc** quand on construit une extension/plugin pour lui — pattern "agent extending itself".

## Références mentionnées

- **Pi** — agent de codage open source, `pi.dev`, repo `pi-mono/packages/coding-agent`
- **OpenRouter** — passerelle multi-modèles via une API unique
- **Ollama** — exécution de modèles locaux, compatible avec Pi
- **Claude Code** et **Codex** — agents concurrents servant de point de comparaison
- **Extensions personnelles de l'auteur** : `context-workflow` et `funny-status` (liens en description de la vidéo)
