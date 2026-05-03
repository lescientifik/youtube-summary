---
description: Synthèse de la vidéo "How Senior Engineers Actually Build With AI in 2026" — méthodologie spec-driven et système de 6 fichiers de contexte pour empêcher l'agent de dériver sur un projet full-stack réel.
video_id: 14RP8liACqo
url: https://youtu.be/14RP8liACqo?is=yxAQ9eRbfddp4_la
title: 'How Senior Engineers Actually Build With AI in 2026 | Build a Full Stack Systems Architecture App'
author: 'JavaScript Mastery'
source_transcript: ../transcripts/2026-05-03-how-senior-engineers-actually-build-with-ai-in-2026-build-a-14RP8liACqo.md
created_on: 2026-05-03
---

# How Senior Engineers Actually Build With AI in 2026

**Chaîne :** JavaScript Mastery  •  **Lien :** https://youtu.be/14RP8liACqo?is=yxAQ9eRbfddp4_la

## TL;DR

Build tutorial de ~4 h qui sert surtout de prétexte à enseigner une méthodologie : le **spec-driven agentic development** opposé au *vibe coding*. L'auteur construit Ghost AI (canvas collaboratif temps réel pour designer une architecture système avec un agent IA) sans écrire une ligne de code, mais en investissant des heures en amont dans un **système à six fichiers de contexte** qui empêchent l'agent de dériver sur un projet long. Public visé : devs juniors/intermédiaires qui se font « éjecter » par l'IA parce qu'ils prompt sans penser système. La thèse centrale : la valeur du dev en 2026 n'est plus de taper du code mais de **prendre les décisions architecturales avant que l'agent n'écrive quoi que ce soit**, puis de découper le build en unités scopées de la taille d'une session focalisée. Stack production réutilisable (Next.js 15, Clerk, Liveblocks, Trigger.dev, Prisma, Vercel Blob) avec des invariants explicites entre couches.

## Points clés à retenir

- **Le système à six fichiers de contexte** est le cœur de la méthode : `project-overview`, `architecture`, `code-standards`, `ai-workflow-rules`, `ui-context`, `progress-tracker` — tous lus par l'agent avant chaque prompt via `agents.md`/`CLAUDE.md` à la racine.
- **Le `progress-tracker.md` est le seul fichier vivant** : c'est la mémoire externe qui permet à l'agent de reprendre exactement où on s'était arrêté, même 6 mois plus tard, en un seul prompt.
- **Spec par unité, pas par feature globale.** Chaque unité tient dans une session focalisée, a un objectif, des décisions de design, des dépendances et **une checklist de "done"** vérifiable.
- **Ne jamais mélanger frontend et backend dans un même prompt** — même feature, deux specs séparées. Donne à l'agent moins de surface pour faire des suppositions.
- **Définir explicitement le hors-scope** dans le `project-overview` (billing, permissions enterprise, history…) empêche l'agent de partir en vrille sur des features non demandées.
- **Nommer la stack à l'avance avec son rôle** : "trigger.dev pour les jobs >60s", "liveblocks pour le multiplayer". Sinon l'agent réinvente une implémentation custom (ex. websocket maison) là où l'outil existe déjà.
- **Les invariants architecturaux** ("les request handlers ne font jamais de longs jobs IA", "ownership vérifié à chaque mutation") sont écrits dans le contexte et survivent à toutes les sessions.
- **Le code IA produit 1,7× plus de problèmes par PR** (étude citée) — d'où l'ajout systématique d'une revue automatisée (CodeRabbit) avant chaque merge.
- **Les "agent skills" publiés par les vendors** (Clerk, Liveblocks, Trigger.dev) deviennent une primitive : on installe le skill, l'agent sait immédiatement implémenter le SDK correctement.
- **Sonnet 4.6 + bon contexte ≈ Opus sans contexte.** Le contexte structuré est ce qui permet d'utiliser un modèle moins cher sans dégrader la sortie.

## Développement

### La thèse : penser comme un senior, exécuter à la vitesse d'un agent [2:00–7:00]
Le marché du dev s'est durci : le travail entry-level est automatisé, les freelances sur tâches simples sont concurrencés par les clients eux-mêmes, et les "prompteurs sans pensée système" inondent l'offre. L'auteur fait un parallèle avec Google/Amazon/Netflix où les seniors passent **des semaines à écrire des design docs / RFC** avant de coder, et parfois des mois sans écrire de code de production. L'ingénierie logicielle n'a jamais été une affaire de lignes par jour — l'IA a juste rendu cette discipline **brusquement obligatoire** au lieu d'optionnelle.

### Vibe coding vs spec-driven [7:00–13:00]
Démonstration par deux prompts pour la même feature : *"Build me a SaaS app with auth and a real-time canvas"* vs *"I'm adding a Liveblocks RoomProvider to the workspace route. Auth is already handled by Clerk middleware. The canvas uses React Flow. Room tokens should be issued only after verifying project membership. Wire the provider into the existing workspace layout without touching the sidebar or navbar."* Même intention, mais le second **communique des décisions, pas des souhaits**. L'IA n'est pas plus intelligente — le dev l'est. Vibe coding marche pour un weekend prototype, s'effondre dès qu'il faut maintenir.

### Le système à six fichiers de contexte [9:00–13:00, 21:00–39:00]
Tout est rangé dans `context/`. Avant d'écrire la moindre ligne, l'agent lit les six fichiers dans l'ordre :

1. **`project-overview.md`** — résumé une-page, objectifs **mesurables** (pas "build a good canvas" mais "let auth users create and manage architecture projects"), user flow complet pour que l'agent connaisse la séquence logique, features avec **technologies nommées**, sections in-scope / **out-of-scope**, success criteria.
2. **`architecture.md`** — tech stack avec rôle, frontières entre couches, modèle de stockage (ici **hybride** : Postgres pour métadata, Vercel Blob pour les gros artefacts markdown — décision senior pour garder la DB lean), interactions entre outils (ex. Clerk vérifie l'appartenance avant que Liveblocks n'émette un token), invariants jamais à violer.
3. **`code-standards.md`** — strict mode, pas de `any`, `'use client'` uniquement si interactivité browser, tokens Tailwind via utilitaires (jamais de hex en dur), conventions Next.js… c'est ce qui empêche la feature 16 d'être stylée différemment de la feature 5.
4. **`ai-workflow-rules.md`** — la règle reine : *one feature unit at a time*. Ne pas mélanger des frontières système non liées dans une même implémentation.
5. **`ui-context.md`** — tokens de design (palette dark-only, fonts, radii), conventions de composants. Généré en conversation avec une IA en partant d'un *feel* ("dark, technical, precise, like an engineering tool").
6. **`progress-tracker.md`** — phase courante, en cours, terminé, décisions prises. **Le seul fichier mis à jour en permanence par l'agent**. Résout le problème de l'absence de mémoire entre sessions.

Plus un `agents.md` (alias `CLAUDE.md`) à la racine, qui n'instructionne qu'une chose : *lis les 6 fichiers en ordre avant de toucher à quoi que ce soit, et mets à jour le progress tracker après chaque change*.

### Le découpage en unités et le workflow par spec [12:00–14:00, 40:00 et suivants]
Le build de Ghost AI est cassé en `context/feature-specs/NN-name.md` (ex. `01-design-system`, `02-editor`, `06-projects-rest-api`, `07-wire-editor-home`, `08-editor-workspace-shell`, …). Chaque spec contient : but, décisions, détails d'implémentation, dépendances, **checklist de validation** ("toutes les routes existent", "401/403 sont retournés", "le build passe"). Le prompt envoyé à l'agent est toujours le même template :

> Read the agents file. Read `NN-feature.md`. Update the progress tracker to mark this in progress. Implement exactly as specified.

Quand l'agent dévie, **prompt correctif focalisé** : ce qui ne va pas, ce qui est attendu, fix uniquement ça. Pas de refonte globale.

### Pourquoi séparer frontend et backend dans deux specs [1:46:50–1:47:45]
Sur la feature CRUD projets, l'auteur fait délibérément deux specs : `06-projects-api.md` (juste les 4 routes REST) puis `07-wire-editor-home.md` (data fetching côté server component + hook côté client + branchement UI). Justification : *combining them gives the agent too much surface area to make assumptions across*. Deux prompts focalisés = deux résultats propres, pas de bug entre couches.

### La stack et pourquoi [22:00–37:00]
- **Clerk** pour l'auth — "nowadays, the speed of shipping matters more than anything", construire l'auth from scratch prend des semaines même avec IA et ne sera jamais aussi sûr. Bonus : MCP, CLI, et **agent skills** Clerk → l'agent devient compétent sur le SDK instantanément.
- **Liveblocks** pour le real-time (curseurs live, présence, edits collaboratifs sur React Flow) **et pour son AI assistant** intégré qui peut générer des nodes directement dans le canvas. Skills agents disponibles aussi.
- **React Flow** pour le canvas (la version "agentic" sortie récemment).
- **Trigger.dev** pour tout job >60 s : les API routes Next.js timeout en prod sur Vercel, Trigger gère retries, status, et reporting au front pour ne pas bloquer l'UI pendant qu'un agent IA génère une longue spec.
- **Prisma + Postgres** pour la métadata, **Vercel Blob** pour les gros markdown générés (hybrid storage).

### Garde-fous de production [45:00, 2:00:00, 3:54:00]
- **CodeRabbit sur chaque PR** dès la fonctionnalité 1, branche `dev` puis merge sur `main` — pratique copiée d'équipes type Nvidia. Plusieurs bugs réels attrapés en direct (ex. `import type` qui efface le namespace value, dialogue qui se ferme même quand l'API échoue).
- **Switch dev → prod** en fin de build : nouvelles clés Clerk/Liveblocks/Trigger, env Vercel, deux échecs de déploiement classiques résolus en direct (`package-lock.json` corrompu → suppression ; Prisma → ajouter `postinstall: prisma generate`).

### Petits détails de productivité
- **Whisper Flow** (dictée vocale) pour écrire les prompts plus vite que de taper.
- Choisir Sonnet 4.6 plutôt que Opus 4.7 quand le contexte est bien fait — c'est exactement le rôle des 6 fichiers : compenser un modèle moins cher.

## Citations marquantes

> "Senior engineers aren't really writing code anymore. They design the systems and let AI handle the implementation. And the gap between developers who can do that and developers who can't is dividing the industry right now." — [0:00]

> "Both developers want roughly the same thing, but the second prompt reveals a developer who knows their auth layer, understands their component boundaries… The AI isn't smarter when it reads the second prompt. The developer is." — [8:00]

> "The time you save by skipping this is the time you'll lose in week three debugging AI output that's drifted away from anything coherent." — [14:14]

> "Combining them gives the agent too much surface area to make assumptions across." — [1:46:34] *(sur le fait de séparer specs front et back)*

## Ce que je peux appliquer

- **Créer un dossier `context/` avec les 6 fichiers** sur le prochain projet sérieux, et ajouter un `CLAUDE.md` à la racine qui force leur lecture + maj du progress tracker.
- **Commencer chaque projet par une conversation avec une IA de planification** (sans coder) pour pressure-tester l'archi jusqu'à ce que le système soit clair en tête, puis cristalliser en 6 fichiers.
- **Définir explicitement le `OUT OF SCOPE`** dans le project overview — c'est ce qui empêche le scope creep IA-induit.
- **Découper en specs de la taille d'une session focalisée**, jamais en phases vagues type "build the dashboard". Chaque spec = un objectif + des dépendances + une checklist.
- **Séparer frontend et backend dans deux prompts différents** même pour la même feature.
- **Nommer la stack avec le rôle de chaque outil** ("Trigger.dev pour les jobs >60s") dans `architecture.md` pour éviter que l'agent réinvente une implémentation custom.
- **Écrire les invariants** ("auth vérifié à chaque mutation", "request handlers jamais de long-running") une seule fois dans le contexte.
- **Ajouter une revue automatique** (CodeRabbit ou équivalent) sur chaque PR — le code IA introduit ~1,7× plus de bugs.
- **Installer les agent skills** publiés par les vendors qu'on utilise (Clerk, Liveblocks, Trigger.dev) plutôt que de re-prompter le SDK à chaque fois.
- **Maintenir un `progress-tracker.md` vivant** — c'est ce qui rend l'onboarding mono-prompt possible après une pause.

## Références mentionnées

- **Ghost AI** — l'app construite, canvas collaboratif d'architecture système.
- **Clerk** — auth, MCP, CLI, agent skills.
- **Liveblocks** — multiplayer + AI assistant intégré, agent skills.
- **Trigger.dev** — background jobs longs, monitoring, agent skills.
- **React Flow** — canvas (version récemment sortie pour le contexte agentic).
- **Prisma + Postgres**, **Vercel Blob** — stockage hybride.
- **shadcn/ui**, **Tailwind v4**, **Lucide** — design system.
- **CodeRabbit** — revue de code automatique (utilisée par des équipes type Nvidia).
- **Whisper Flow** — dictée vocale pour prompter.
- **Claude Code (Opus 4.7 / Sonnet 4.6)**, **Codex** — agents utilisés en alternance.
- Étude citée : "AI code creates 1.7× more problems per PR" (non sourcée explicitement).
- **Spec-driven agentic development course** (en cours de production par l'auteur, JS Mastery).
