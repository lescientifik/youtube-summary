---
description: Synthèse de la vidéo "Plan, Specify, and Implement with Spec Kit" — procédure complète du spec-driven development avec GitHub Spec Kit pour piloter un agent sans dériver.
video_id: VfBLlAN5zdQ
url: https://youtu.be/VfBLlAN5zdQ
title: 'Plan, Specify, and Implement with Spec Kit'
author: 'Microsoft Developer'
source_transcript: ../transcripts/2026-05-11-plan-specify-and-implement-with-spec-kit-VfBLlAN5zdQ.md
created_on: 2026-05-11
---

# Plan, Specify, and Implement with Spec Kit

**Chaîne :** Microsoft Developer  •  **Lien :** https://youtu.be/VfBLlAN5zdQ

## TL;DR

GitHub Spec Kit n'est pas un produit magique : c'est un ensemble de prompts et de scripts qui formalisent des garde-fous Markdown (constitution → spec → clarify → plan → tasks → implement) pour empêcher un agent de partir en vrille. La vidéo détaille la procédure complète et insiste sur deux choses peu évidentes : (1) découper en *features* numérotées (`specs/001-...`, `002-...`) plutôt que tout one-shotter dans un seul spec géant, et (2) la commande `clarify` qui force le LLM à poser 5 questions sur les ambiguïtés avant de coder. Spec et plan sont détachés, ce qui permet de *forker* le même spec vers plusieurs stacks (Hugo, Next.js…) via git worktrees et de comparer. Utile dès qu'on dépasse le vibe-coding et qu'on veut du code maintenable.

## Points clés à retenir

- **Spec Kit = prompts + scripts Markdown**, pas un package npm/pypi. Tu peux télécharger les templates directement depuis les releases GitHub si tu ne veux pas du CLI `specify`.
- **5 artefacts, dans cet ordre :** `constitution.md` (non-négociables) → `spec.md` (fonctionnel) → clarify (questions LLM) → `plan.md` (technique) → `tasks.md` (TODO parallélisables) → implement.
- **Une feature = un dossier numéroté** (`specs/001-podcast-website/`). Tu chunkes le contexte, l'agent reste focus.
- **`clarify` est l'étape la plus sous-estimée** : le LLM scanne le spec, génère un tableau de coverage (core goals / out of scope / personas / edge cases…) et te pose 5 questions une par une, avec options A/B/C/D. Les réponses sont injectées dans le spec.
- **Spec ↔ plan sont découplés.** Tu peux forker le même spec pour générer 2-3 implémentations rivales (Hugo vs Next.js) et benchmarker, tout en restant lié à la constitution.
- **Existing repo : ajouter Spec Kit en place** avec `specify init .` puis demander à l'agent d'inspecter le code avant de générer constitution/plan.
- **Les markdowns sont éditables à la main.** Pas besoin de re-prompter pour changer "3G → LTE" dans la constitution, ouvre le fichier.
- **Git-native workflow :** chaque phase crée une branche, on peut revert facilement. En v2 : auto-commit entre phases.
- **Choix de modèle empirique :** Claude (Opus/Sonnet) plus créatif pour spec/plan ; GPT-5 plus réservé et interrompt ("dois-je continuer ?") ; Sonnet bon en C#, GPT-5 souvent meilleur en TypeScript. Teste sur ta stack.

## Développement

### Pourquoi spec-driven plutôt que vibe-coding [2:00]

Le vibe-coding marche pour un proto, pas pour du logiciel maintenu. Sans rails, le modèle fait ses propres choix d'architecture (framework web, organisation CSS, libs) — choix réversibles en théorie mais qui te coincent quand tu veux ajouter un panier ou faire scaler. Spec-driven = front-loader la réflexion (avec l'aide du LLM) pour que les décisions soient explicites et que tout futur prompt ait le contexte. Origine interne : John Lamb (Microsoft) utilisait Claude Sonnet qui voulait "réécrire un framework web avant de faire un site" — la spec sert littéralement de muselière.

### Procédure d'installation [10:30]

```bash
# Global (recommandé : uv)
uvx specify init <project-name>          # nouveau projet
uvx specify init .                        # projet existant, dans le dossier courant
```

Le CLI demande : (1) l'agent cible (copilot, claude, gemini, codex, cursor…) et (2) le shell (bash/powershell). Il télécharge les templates correspondants dans `.github/`, `.specify/`, `.vscode/` (pour copilot). En v2, les scripts par agent disparaîtront — tout sera bundlé dans `specify` qui sera invoqué par l'agent.

### Étape 1 — La constitution [14:00]

Fichier de **non-négociables**, technique ET non-technique. Exemples concrets cités :
- "Toujours déployer sur Azure, jamais d'autres providers"
- "Toujours utiliser la dernière version de TypeScript"
- "Toujours utiliser ce package de logging"
- Contraintes de perf (Lighthouse score), YAGNI, "complexity must always be justified"
- Plateformes à tester (retirer Safari à la main si tu t'en fous)

Pour un repo existant : "go inspect this project and then create the constitution based on what I have". Spec Kit fusionne progressivement la constitution dans `agents.md` (standard supporté par Copilot, Claude Code, etc.).

### Étape 2 — Spec fonctionnel [18:50]

Prompt court ("I want to build a podcast website with featured episodes"). Le `/specify` agent génère un `spec.md` avec user stories, scénarios, edge cases, functional requirements — format type Product Manager. **Le spec ne contient AUCUN détail technique** (pas de framework, pas de lib). C'est ce qui permet la suite.

### Étape 3 — Clarify [22:42]

L'étape la plus rentable de la vidéo. Tu cliques `/clarify`, le LLM :
1. Génère un tableau "coverage" : core user goals / out of scope / user roles & personas / identity & uniqueness rules / edge cases — chaque ligne marquée "clear", "not defined", "partial".
2. Pose **5 questions ciblées** sur les "not defined", une par une, avec options A/B/C/D + recommandation. Exemples : "How will episode data be managed? A) RSS import B) Static JSON C) CMS…", "Expected catalog size?".
3. Tu réponds par une lettre OU un texte libre. La réponse est immédiatement écrite dans une section `## Clarifications` du spec ET propage la modif aux requirements concernés.

C'est l'équivalent du "questions before assumptions" de plan mode, mais figé en artefact versionné.

### Étape 4 — Plan technique [25:35]

Maintenant tu rentres la stack : "Hugo, Tailwind CSS, npm pour le build, deploy Azure Static Web Apps…". L'agent génère plusieurs fichiers dans le dossier feature :
- `plan.md` — contexte technique (Go templates, HTML5, target platform, scale)
- `research.md` — recherche faite par l'agent (corpus si pas d'accès web, sinon il browse — combinable avec un mode "beast" agentique pour Claude Code)
- `data-model.md` — entités (Podcast, Episode), champs requis/optionnels
- `contracts/` — interfaces
- `quickstart.md` — démarrage rapide
- **Constitutional check** dans le plan : confirme que la solution proposée respecte la constitution avant de continuer.

### Étape 5 — Tasks & implement [31:00]

`/tasks` casse le plan en liste de tâches granulaires, en marquant celles qui peuvent être parallélisées. Puis le bouton `/implement` (ou un agent en background) exécute. Tu peux pousser plusieurs sub-agents sur des branches/worktrees parallèles.

### Variations parallèles [28:40]

Le découplage spec/plan permet de "geler" le spec puis forker en plusieurs branches (`git worktree`) qui implémentent la même feature en stacks différentes (Hugo vs Next.js SSG). Tu compares perf, DX, fit avec ton cloud — la constitution garde tout le monde aligné sur les non-négociables. C'est le pattern le plus puissant de la vidéo pour l'agentic coding sérieux.

### Workflow incrémental [34:48]

Pour chaque nouvelle feature, tu sautes la constitution (déjà là) et tu recommences à `/specify`. Les dossiers s'incrémentent : `002-guest-page/`, `003-search/`… L'historique de raisonnement (spec + clarifications + plan + research) reste dans le repo et sert de contexte pour les futures modifs ("how did you think about the data model? where are episodes located?").

## Citations marquantes

> "It's essentially us formalizing the guard rails for AI models." — Dan, [1:54]

> "You haven't really given it the rails, the plan, the spec on how to do it." — James, [1:11]

> "Sonnet can get a little bit overeager — you ask it to build a website and it's going to go 'oh great, let me write a whole new web framework first'." — Dan, [7:26]

> "It's a markdown file. Just go change it yourself." — Dan, [17:30] (sur l'édition manuelle des artefacts)

## Ce que je peux appliquer

- **Pour tout projet sérieux : bootstrap avec `uvx specify init`** plutôt que de jeter des prompts au hasard. Même flow pour les repos existants avec `.` et un prompt "inspect first".
- **Écrire systématiquement une constitution courte** avant le premier prompt de code : 5-10 non-négociables (stack imposée, deploy target, packages obligatoires, YAGNI, niveau de tests). C'est l'antidote contre les "j'ai oublié de lui dire" qui font perdre des heures.
- **Toujours passer par `/clarify` avant `/plan`.** Les 5 questions coûtent 2 minutes et exposent des hypothèses cachées que je n'aurais jamais pensé à prompter.
- **Une feature = un dossier `specs/NNN-feature-name/`.** Ne pas mettre 4 features dans un seul spec.
- **Garder le spec technologie-agnostique**, mettre le stack dans le plan. Ça permet de re-générer un plan pour une autre stack sans tout refaire.
- **Utiliser git worktrees pour comparer 2-3 implémentations** d'une même feature quand la décision de stack n'est pas tranchée.
- **Éditer les `.md` directement** quand un détail change, plutôt que de re-prompter — gain de temps massif.
- **Tester Claude vs GPT-5 par étape** : Claude pour spec/clarify/plan (créatif), GPT-5 ou Sonnet pour l'implémentation selon le langage.
- **Activer l'auto-commit entre phases** dès que Spec Kit v2 sort (déjà branche-aware aujourd'hui, revert facile).

## Références mentionnées

- **GitHub Spec Kit** — https://github.com/github/spec-kit (53k+ stars)
- **specify CLI** — installable via `uvx` (Python, mais pas de requirement Python pour les projets cibles)
- **AGENTS.md** — standard supporté maintenant par Copilot CLI, VS Code, Claude Code, Gemini, Codex, Cursor
- **John Lamb** — origine du projet en interne chez Microsoft, à partir de l'usage de Claude Sonnet
- **Beast mode** (Burke Holland) — mode agentique web-research pour Claude Code, combinable avec la phase research
- **git worktree** — recommandé pour les implémentations parallèles à partir d'un même spec
- **Plan mode (VS Code)** — workflow similaire mais plus léger, mentionné comme complément
