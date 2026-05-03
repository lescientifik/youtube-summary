---
description: Synthèse de la vidéo "Context Is the New Code — Patrick Debois, Tessl" — décliner le cycle DevOps sur le contexte (générer, tester, distribuer, observer) pour industrialiser le coding agentique.
video_id: bSG9wUYaHWU
url: https://youtu.be/bSG9wUYaHWU
title: 'Context Is the New Code — Patrick Debois, Tessl'
author: 'AI Engineer'
source_transcript: ../transcripts/2026-05-03-context-is-the-new-code-patrick-debois-tessl-bSG9wUYaHWU.md
created_on: 2026-05-03
---

# Context Is the New Code — Patrick Debois, Tessl

**Chaîne :** AI Engineer  •  **Lien :** https://youtu.be/bSG9wUYaHWU

## TL;DR

Talk de 27 min de **Patrick Debois** (l'inventeur du terme « DevOps » en 2009) à la conférence AI Engineer, qui propose de transposer le cycle DevOps au **contexte** : générer → tester → distribuer → observer → adapter. Thèse : maintenant que le code est généré à partir d'un contexte (prompts, `agent.md`, skills, MCP, specs), c'est ce contexte qui devient l'artefact à versionner, tester et déployer — et il mérite la même rigueur d'ingénierie qu'un code applicatif. Public : développeurs et architectes qui codent déjà avec un agent et veulent passer du « prompt + espoir » à un cycle de vie reproductible. Conclusions clés : (1) écrire des **evals comme on écrit des unit tests**, mais avec des **error budgets** pour absorber le non-déterminisme ; (2) le LLM est juste un moteur — la performance vient du carburant, donc du contexte ; (3) la vraie valeur émerge à l'échelle d'une équipe quand les logs d'agents et les feedbacks de PR alimentent un *flywheel* de contexte partagé.

## Points clés à retenir

- **Context Development Life Cycle (CDLC)** — boucle infinie calquée sur DevOps : *generate → test → distribute → observe → adapt*. C'est le squelette mental du talk.
- **Le code redevient du contexte.** Quand un bloc de code applicatif sert d'helper réutilisable, le transformer en *skill* (description + script + workflow) résout plus de cas qu'une implémentation explicite, parce que l'agent s'adapte (ex. détecter Python vs Node, choisir le bon package manager).
- **Evals = tests pour le contexte.** Quatre niveaux à empiler comme pour le code : *lint* (validation de format du skill), *Grammarly-like* (l'agent comprend-il ce qu'on a écrit ?), *LLM-as-judge* sur le code généré, *judge avec outils* pour des tests end-to-end (le juge `curl` réellement l'endpoint).
- **Error budgets, pas tests stricts.** Une eval n'est pas déterministe : il faut la lancer N fois (ex. 5) et accepter un taux d'échec borné, sinon le CI/CD devient impilotable.
- **La modification d'une seule ligne dans `agent.md` peut tout casser** — donc `agent.md` mérite des tests de régression au même titre qu'un fichier de config infra.
- **Skills, plugins, MCP convergent comme un format de package** pour distribuer du contexte (description + scripts + docs). Conséquence inévitable : registries, *dependency hell* et besoin d'un AI-SBOM.
- **99,9 % des skills publics sont mauvais** (jugement direct de Debois) — utiles à étudier, pas à installer aveuglément ; les entreprises voudront leur propre registry interne.
- **Les logs d'agents sont la mine d'or organisationnelle.** Si plusieurs devs voient leur agent réclamer la même info manquante, c'est un signal pour créer un contexte partagé qui bénéficie à tous d'un coup.
- **Tout feedback de PR humain est un feedback sur le contexte.** Plutôt que d'argumenter sur la PR, corriger la source : le contexte qui a généré le code.
- **Sandbox ≠ filtrage de contexte.** Un sandbox isole l'exécution mais l'agent charge `agent.md`/`skill.md` d'office — il faut un *context filter* dédié (équivalent WAF) contre les prompt injections.
- **Le LLM n'est qu'un moteur ; le contexte est le carburant.** Vous ne contrôlez pas le moteur, vous contrôlez le carburant.

## Développement

### La prémisse : le code se transforme en contexte [1:30–2:50]
Debois part d'une observation personnelle : il *vibe-code* — il ne touche presque plus au code, il décrit ce qu'il veut. Mieux, des morceaux de code qu'il maintenait (onboarding produit qui devait gérer Python, Node, plusieurs package managers) ont été convertis en *skill* : une simple instruction du type *« détermine le package manager, puis l'écosystème, puis enchaîne ces étapes avec l'utilisateur »* résout plus de cas que tout l'arbre de conditions qu'il aurait fallu coder. L'inversion s'opère : ce qui était logique impérative devient prompt déclaratif.

### Pourquoi un Context Development Life Cycle [2:55–3:50]
Parallèle explicite avec DevOps en 2009 : à l'époque, la question était *« et si l'ops ressemblait au dev ? »*. Aujourd'hui : *« et si on traitait le contexte comme du code ? »*. D'où la boucle infinie : on **génère** du contexte, on le **teste**, on le **distribue** à l'équipe, on **observe** son comportement en usage réel, on **adapte**, et on recommence.

### Generate : ce que tout le monde fait déjà [3:50–6:10]
Cinq sources de contexte vont du plus naïf au plus structuré : (1) le prompt humain typé à la volée ; (2) les **prompts réutilisables** standardisés sous forme `agent.md` (Debois pique au passage Anthropic pour s'obstiner avec `Claude.md`) ; (3) la **doc de bibliothèques tirée à la demande** parce que les LLMs hallucinent les versions ; (4) le **MCP** qui pompe du contexte de GitHub, Slack, Jira ; (5) le **spec-driven development** où la spec se découpe automatiquement en plan d'exécution.

### Test : reproduire la pyramide de tests, version contexte [6:15–13:50]
Le constat d'entrée est brutal : changer deux lignes dans `Claude.md`, est-ce *YOLO, looks good to me* ? Non. Il faut tester. Quatre couches empilables :
- **Linter de contexte** : valider que le skill respecte le schéma (description présente, longueur max, etc.).
- **Vérification de compréhension** ("Grammarly du contexte") : demander à un LLM si le contexte est interprétable, complet, non ambigu. Debois note qu'il code **à la voix** parce qu'il devient plus verbeux qu'au clavier — et un contexte plus verbeux est mieux compris.
- **LLM-as-judge** : exemple concret. Règle : *tout endpoint doit être préfixé `/awesome/`*. On prompte *« ajoute un endpoint pour sauver un user »*, puis on demande à un autre LLM si le code généré commence par `/awesome/`. Sans la règle dans le contexte, aucun LLM ne préfixerait jamais ainsi — c'est la signature qu'on teste bien la valeur ajoutée du contexte d'entreprise.
- **Judge avec tools** : le juge devient agent, dispose d'un sandbox, exécute `curl` sur l'endpoint réellement déployé. On bascule de l'unit test vers le test end-to-end, pour un commit donné × un contexte donné.

Et la subtilité critique du CI/CD pour evals : **non-déterminisme**. Lancer une eval une seule fois ne signifie rien. Lancer 5 fois, mesurer le taux de réussite, et raisonner en **error budgets** par suite (les tests critiques doivent réussir 100 %, d'autres acceptent un budget plus large). Tester du contexte n'est pas tester du code — il faut adapter le mental model.

### Distribute : des skills aux registries [13:55–17:40]
Première étape, triviale : commiter le contexte dans le repo. Au-delà : si le contexte se réutilise entre projets/équipes, c'est une **bibliothèque**, ce qui implique un **format de package** (skills/plugins, possiblement avec MCP embarqué) et des **registries**. Tessl a un marketplace, Anthropic a un registry de skills. Verdict frontal : *« 99.9% of the skills is crap »* — utiles à lire, peu à installer en l'état. Les entreprises iront vers des registries privés. Conséquences inévitables qu'on connaît du monde NPM : **dependency hell** (un skill front conflictue avec un skill React), **versioning** mirroir des libs, et **sécurité** (Snyk scanne déjà le contexte pour des credentials, des dépendances tierces). D'où un **AI SBOM** : qui a écrit ce skill, avec quel modèle, à partir de quel contexte ?

### Observe : la mine d'or des logs et des feedbacks [17:45–22:30]
Quand on publie une lib de contexte, comment savoir si elle marche encore ? Les **logs d'agents** (un standard émerge, *agentd*) deviennent le canal d'observabilité : si l'agent d'un dev signale *« il manque telle info »*, c'est utilisable individuellement. Mais à l'échelle d'une organisation, on **agrège** : *plusieurs* agents demandent la même chose ⇒ on génère un contexte partagé et on le pousse à tout le monde. Effet d'amélioration multiplicatif.

Idem pour les **PR** : un commentaire de revue est un feedback indirect sur le contexte qui a produit le code. Au lieu de re-débattre PR après PR, on **corrige le contexte** une fois. Et en **prod** : un wrapper d'instrumentation détecte les échecs sur du code généré par un contexte donné, propose de transformer l'incident en cas de test pour la prochaine itération.

Côté sécurité runtime : un sandbox isole l'exécution, mais ne filtre **pas** ce que l'agent ingère — `agent.md` et `skill.md` se chargent automatiquement. Debois recommande un **context filter** distinct, pensé comme un WAF qui inspecte les patterns d'injection avant qu'ils n'atteignent l'agent.

### Trois boucles imbriquées [22:30–24:10]
Conclusion en couches :
1. **Boucle solo** — auteur de skill : créer, tester, raffiner son markdown.
2. **Boucle bibliothèque** — publier, observer l'usage, corriger.
3. **Boucle organisationnelle** — *flywheel* : un fix dans une équipe bénéficie à toutes les autres, comme un sonar CI/CD pour le contexte d'entreprise.

### La métaphore qui clôt [24:10–24:30]
*« LLMs and coding agents — they're just the engine. If you give the engine the wrong fuel, which is context, they're not going to perform. »* On ne peut pas modifier le moteur, on peut maîtriser le carburant. Le métier devient l'ingénierie du contexte, pas la rédaction de code.

### Q&A : le coût caché [25:50–26:45]
Question d'un participant sur des formes plus exotiques de contexte (consistency check : générer N définitions en parallèle, mesurer la convergence pour décider si la spec initiale est assez crispée). Debois ne tranche pas le cas exotique mais conclut sur le **vrai prix** de la méthode : *« vous pensiez gagner du temps en écrivant du contexte au lieu de code — mais si vous le faites rigoureusement, vous passerez beaucoup de temps à écrire les bons evals »*. Les pratiquants avancés bâtissent leur propre process de génération d'evals adapté à leur métier.

## Citations marquantes

> "Context is the new code." — Patrick Debois, [0:50]

> "You change two lines in your Claude.md. Do you know the impact? Is it like YOLO, looks good to me?" — Patrick Debois, [6:16]

> "99.9%, and I mean that in a very sincere way, of the skills is crap." — Patrick Debois, [15:09]

> "If you give the engine the wrong fuel, which is context, they're not going to perform." — Patrick Debois, [23:48]

> "You thought you were going to save time by writing your context instead of all your code, but if you take this rigorously, you're going to spend time on writing the right evals." — Patrick Debois, [26:15]

## Ce que je peux appliquer

- **Versionner `agent.md`/`CLAUDE.md` avec des evals dédiées.** Dès qu'on modifie une convention (ex. règle de nommage, choix de stack), faire passer une suite d'evals "LLM-as-judge" qui vérifie qu'un nouveau code généré respecte bien la règle.
- **Adopter le mental model `error budget` pour les evals.** Lancer chaque eval N=5 fois, paramétrer un seuil de réussite par suite, refuser le merge en dessous du seuil — ne jamais traiter une eval comme un test déterministe.
- **Construire un mini-pipeline de quatre niveaux** : (1) lint sur le format des skills, (2) compréhensibilité (un LLM relit), (3) LLM-as-judge sur le code généré, (4) end-to-end avec tools.
- **Logger les agents et chercher les patterns de "contexte manquant"** récurrents → générer un skill/contexte partagé pour résoudre l'ensemble d'un coup.
- **Convertir les feedbacks de revue de code en patches de contexte**, pas seulement en patches de code. La même remarque qui revient ⇒ règle dans `agent.md`.
- **Ajouter un context filter** (équivalent WAF) avant l'agent pour bloquer les prompt injections, en plus du sandbox d'exécution.
- **Tenir un AI-SBOM** des skills installés : auteur, modèle de génération, version, dépendances — surtout pour les skills tirés de registries publics.

## Références mentionnées

- **DevOps (2009)** — analogie directrice de tout le talk
- **Skills / Plugins** (Anthropic, autres coding agents) — format émergent de package de contexte
- **agent.md** (vs `Claude.md`) — standardisation des prompts réutilisables
- **MCP (Model Context Protocol)** — récupération de contexte depuis GitHub, GitLab, Slack
- **Snyk** — scanner de sécurité étendu au contexte (credentials, dépendances tierces)
- **AI SBOM** — extension du SBOM logiciel au contexte / skills
- **Tessl** — entreprise de Patrick Debois ; registry de skills et marketplace
- **AI DevCon** — conférence curatée par Debois, Londres, 1-2 juin
- **agentd** (mentionné comme standard émergent pour les logs d'agents)
- **LLM-as-a-judge** — pattern d'évaluation
