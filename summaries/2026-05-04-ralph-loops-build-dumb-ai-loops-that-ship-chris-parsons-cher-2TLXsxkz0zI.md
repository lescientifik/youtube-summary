---
description: Synthèse de la vidéo "Ralph Loops: Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick" — comment remplacer les workflows complexes par de simples boucles dans lesquelles l'IA pioche la tâche suivante.
video_id: 2TLXsxkz0zI
url: https://www.youtube.com/watch?v=2TLXsxkz0zI
title: 'Ralph Loops: Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick'
author: 'AI Engineer'
source_transcript: ../transcripts/2026-05-04-ralph-loops-build-dumb-ai-loops-that-ship-chris-parsons-cher-2TLXsxkz0zI.md
created_on: 2026-05-04
---

# Ralph Loops: Build Dumb AI Loops That Ship

**Chaîne :** AI Engineer  •  **Lien :** https://www.youtube.com/watch?v=2TLXsxkz0zI

## TL;DR

Workshop de Chris Parsons (CTO, ex-fondateur, consultant adoption IA) sur les
"Ralph loops" — pattern minimaliste où on relance la même invite jusqu'à ce que
l'agent ait épuisé un backlog. La thèse : avec les modèles récents
(GPT 5.12+, Claude Opus/Sonnet 4.6+), une simple boucle qui dit "prends le
prochain ticket le plus important" surpasse les orchestrations complexes type
n8n ou les graphes de dépendances pré-spécifiés (qui recréent l'enfer du
waterfall). La vraie valeur n'est pas la parallélisation, c'est le séquentiel
non-stop : le goulot devient l'humain, pas le modèle. Public visé : ingénieurs
qui automatisent déjà avec Claude Code/Codex et veulent passer du copilote au
"travailleur de fond". Conclusion existentielle : si tout devient une boucle,
la question n'est plus "que peut faire l'IA ?" mais "quelle partie du travail
veux-tu réellement garder ?".

## Points clés à retenir

- **Une Ralph loop est juste une boucle `while`.** Aucune magie : tu rappelles l'agent avec la même intention. Tout l'art est dans le prompt et les feedback loops.
- **Ne pré-spécifie pas les dépendances entre tickets.** Demande "prends le prochain ticket le plus important" et laisse l'IA décider à la volée — c'est exactement ce qu'elle fait bien.
- **Oublie la parallélisation au début.** Une seule boucle séquentielle suffit ; toi tu n'arriveras déjà pas à suivre.
- **`/loop` dans Claude Code** déclenche un cron interne ("toutes les minutes / heures, fais X") — mécanisme natif pour boucler sans script bash externe.
- **Skills > workflows.** Un skill empaquette contexte + scripts ; il s'invoque à la demande. Préférer un skill versionné à un workflow n8n fragile.
- **Sub-agents pour la validation.** Un sub-agent démarre avec un contexte vide et trouve les défauts qu'un agent qui a écrit le code ratifie en se félicitant lui-même (`simplify` skill comme exemple).
- **Règle de garde : "réversible sans embarras ?"** Si non, l'agent prépare et te rend la main ; si oui, il exécute (envoyer un email = non, créer un brouillon = oui).
- **Théorie des contraintes (Goldratt).** Si ton équipe ralentit avec l'IA, c'est que le vrai goulot est ailleurs (revue, release, coordination) — l'IA expose les inefficacités, ne les comble pas.
- **CI/CD, linting, tests = nourriture de l'IA.** Donne-lui les mêmes outils qu'à un humain : elle s'en sert mieux que tu ne le crois.
- **Lethal trifecta (Simon Willison)** : tokens non-fiables + accès internet + données sensibles = fuite garantie. Sandboxer (Docker sandbox, VPS dédié, clés séparées, permissions fines).

## Développement

### De n8n aux loops [3:14]
Parsons décrivait son workflow n8n hebdomadaire pour générer une newsletter :
brittle, échec presque tous les lundis 14h. Il a copié-collé le JSON n8n dans
Claude Code en lui demandant d'en faire un *skill*. Résultat : meilleure sortie,
zéro maintenance — il demande juste à Claude de mettre à jour le skill en fin
de session. Le constat : les workflows orchestrés sont une étape transitoire ;
les agents tournent intrinsèquement déjà en boucle (lire → décider → outil →
recommencer).

### Origine : Ralph Wiggum [9:00]
Le nom vient du personnage des Simpsons qui essaie la même chose en boucle
jusqu'à ce que ça marche. Idée originale de **Jeffrey Huntley** (~juin 2025) :
après chaque exécution de l'agent, relance le même prompt. L'IA review son code
et complète ce qu'elle a oublié. Avec les modèles d'aujourd'hui, ce premier
niveau (relancer un ticket unique) est devenu inutile — les modèles savent
finir. Mais le pattern reste vivant.

### Le vrai déclic : pointer la loop sur un backlog [22:25]
Parsons raconte son échec : avoir cassé un gros projet en tickets, dépendances,
graphe d'orchestration, 6-7 agents parallèles → contention massive, deux Claude
qui implémentent le même ticket "partagé". Il avait recréé le **waterfall des
années 90**.

La solution est ridicule : `implement the next most important ticket using TDD
principles from doc/tickets, commit when done`. L'IA lit l'ensemble, choisit
l'ordre selon les dépendances qu'elle déduit en regardant le code à l'instant t,
fait le ticket, marque "done", recommence. Démo live sur un Pomodoro CLI.

### `/loop` natif et l'idée que tout est une boucle [41:09]
Plutôt qu'un `while true; do claude -p ...`, Claude Code expose `/loop every 1
minute build the next ticket from doc/tickets`. Sous le capot : un `cron_create`
qui ré-attaque la même invite. Variante puissante : `loop every 1 hour check
linear for new bug reports from test`. Parsons étend ça à toute sa vie pro :

- **morning loop** (6h) : briefing du jour
- **heartbeat loop** (15 min) : check calendrier/email, notif Telegram
- **worker loop** : pioche le prochain pas de chaque projet de son vault Obsidian
- **startup skill** : tente de piloter une startup en boucle (a écrit spontanément un *investor update deck* qu'on ne lui avait pas demandé)

### Construire un *bon* prompt de Ralph loop [49:55]
Parsons montre son skill `ralph` réel. Quelques éléments clés du prompt :

- rôle explicite : "tu es un ingénieur dans une équipe de relais — fais *un* changement, drop le contexte, stop"
- check du `git state` avant de commencer
- recovery : working tree dirty + tests verts → probablement fini ; tests rouges → mid-flight cassé, à jeter
- "passing tests is not enough — verify actual behavior"
- run hook après ticket : `run simplify when finished and ensure you refactor to reduce duplication`

Conseil : ne copie pas son skill, demande à Claude de l'adapter à ton projet et
fais-le évoluer au fil des sessions.

### Sandboxing & sécurité [52:14]
- Code sur un **VPS séparé** de la machine perso, avec ses propres clés API (audit trail).
- **Permissions Claude fines** : ne *jamais* laisser envoyer un email — uniquement *drafter*.
- **Docker sandbox** (nouveau) pour isoler le FS.
- **Lethal trifecta** : si les trois (untrusted tokens, internet, données sensibles) coexistent dans un contexte, fuite garantie — minimiser les intersections.
- Parsons développe un projet **lockbox** pour bloquer les accès FS après lecture de tokens non fiables.

### Sub-agents pour la validation [55:54]
Un participant rapporte que passer la *validation* à un sub-agent au lieu de
l'agent principal a *immédiatement* fait remonter des bugs auparavant masqués.
Raison : un agent qui a écrit le code souffre d'un biais de confirmation
("je viens de checker, c'est bon"). Le sub-agent démarre vide → vraie revue.
C'est exactement ce que fait le skill `simplify` (Anthropic) : 3 sub-agents
parallèles sur le diff récent.

### Spec-driven : prudence [56:30]
Parsons est sceptique sur le spec-driven extrême (Kira-style) : risque de
fossiliser un process qui marche en 2026 mais sera obsolète quand les modèles
suivants (Mythos) arriveront. Préférer des **specs *just-in-time***, itératives,
écrites au moment où on en a besoin.

### Le vrai goulot, c'est toi [1:36:00, et passim]
Théorie des contraintes appliquée : si une équipe ralentit avec l'IA, c'est
que le bottleneck était la review, la release, ou la coordination — pas la
vitesse de codage. L'IA ne fait qu'exposer ces inefficacités. Corollaire :
ne pas multiplier les agents tant que tu es toi-même le goulot ; investis
dans ta capacité à *spécifier* et *évaluer*, ou dans des feedback loops
automatiques (tests E2E, screenshots avec Claude+Chrome, simulation d'audience
avec personas).

### Crise existentielle [58:34, 1:08:00]
Si tout devient une boucle, qu'est-ce qui reste à l'humain ? Parsons a basculé
d'une question "*que peut faire l'IA ?*" à "*quelle partie de mon travail je
veux garder ?*". Pour lui : la stratégie, oui ; la review d'emails draftés,
non — il préfère que l'IA lui *donne l'info brute* et qu'il fasse lui-même
le travail qu'il aime, plutôt que de devenir un "reviewer de drafts AI".

## Citations marquantes

> "The dumbest Ralph loop is literally that — just a `while` loop and it goes through and implements stuff." — Chris Parsons, [18:30]

> "If humans can't do waterfall, how was AI supposed to do any better?" — Chris Parsons, [26:25]

> "The bottleneck is usually not the number of agents. It's usually you, just keeping up with the AI." — Chris Parsons, [27:25]

> "Is this reversible without embarrassment to me? If the answer is no, don't do it." — Chris Parsons, [1:07:30]

> "AI can do all of the rubbish work, but it can't and it shouldn't do the work that I'm uniquely good at." — Chris Parsons, [1:08:50]

## Ce que je peux appliquer

- **Démarrer un skill `ralph` perso** : prompt = rôle de relais, prend le prochain ticket le plus important, TDD, commit, simplify, stop. Le faire évoluer session après session.
- **Tickets en flat files markdown** dans `doc/tickets/` (suffisant ; pas besoin de Linear/Jira pour démarrer). Migrer plus tard vers `beads` si pertinent.
- **`/loop` natif** plutôt qu'un wrapper bash : moins de plomberie, contexte continu.
- **Sub-agent pour la review**, jamais l'agent qui a écrit le code. Ajouter un step `delegate review to sub-agent` dans tout skill de loop sérieux.
- **Heuristique "réversible sans embarras"** : codifier dans `CLAUDE.md` ce que l'agent peut *exécuter* vs ce qu'il doit seulement *préparer*.
- **Investir dans les feedback loops automatiques** avant la parallélisation : tests E2E (Playwright), screenshots, lint strict, CI/CD verte. C'est là que se gagne la confiance.
- **Audit personnel** : lister mon flux de travail, identifier ce que je veux garder vs ce que je délègue à une boucle. Cette décision est plus importante que le tooling.
- **Vault Obsidian + embeddings (Leanne)** comme base de connaissance unifiée — un fichier par pensée, projets séparés, transcripts de calls dedans, AI cherche en RAG.

## Références mentionnées

- **Jeffrey Huntley** — créateur du concept Ralph loop (~juin 2025).
- **Matt PCO** — vidéo YouTube qui a popularisé la version "next most important ticket".
- **Simon Willison** — "lethal trifecta" (untrusted tokens × internet × sensitive data).
- **Eliyahu Goldratt — *The Goal* (1984)** — théorie des contraintes.
- **Andrej Karpathy** — article récent "LM as a wiki" sur la gestion de connaissances.
- **Steve Yegge — beads** — système de tickets local par fichiers.
- **Ash Maurya** — auteur de référence pour le skill `startup`.
- **Outils** : Claude Code (`/loop`, skills, sub-agents), Codex, Cursor, n8n (référence repoussoir), Docker sandbox, Obsidian, Leanne (CLI embeddings), Nano Banana Pro (slides), Cambban vibe-codé maison, agent-mail MCP (mentionné en Q&A), GLM/ZAI (alternative open récente).
- **Concepts** : Zettelkasten, cognitive debt, adversarial review, simulate audience.
