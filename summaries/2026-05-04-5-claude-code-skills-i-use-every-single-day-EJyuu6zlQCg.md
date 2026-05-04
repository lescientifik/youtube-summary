---
description: Synthèse de la vidéo "5 Claude Code skills I use every single day" — Cinq skills minimalistes qui transforment un agent amnésique en pipeline d'ingénierie discipliné, du design à l'implémentation TDD.
video_id: EJyuu6zlQCg
url: https://youtu.be/EJyuu6zlQCg?is=A8XMAq-r2wnEYpz0
title: '5 Claude Code skills I use every single day'
author: 'Matt Pocock'
source_transcript: ../transcripts/2026-05-04-5-claude-code-skills-i-use-every-single-day-EJyuu6zlQCg.md
created_on: 2026-05-04
---

# 5 Claude Code skills I use every single day

**Chaîne :** Matt Pocock  •  **Lien :** https://youtu.be/EJyuu6zlQCg?is=A8XMAq-r2wnEYpz0

## TL;DR

Matt Pocock présente cinq skills Claude Code qu'il utilise quotidiennement pour
contrer un défaut majeur des agents : ils sont compétents mais sans mémoire, et
exigent donc un *process* extrêmement strict. Les skills encodent ce process
sous forme de prompts courts et réutilisables, et forment une chaîne complète
allant de l'idée brute (`grill me`) au PRD, puis aux issues GitHub
(`PRD to issues`), à l'implémentation en TDD red-green-refactor, et enfin à
l'amélioration continue de l'architecture (`improve codebase architecture`).
Le message central : un skill n'a pas besoin d'être long pour être puissant —
trois phrases bien choisies peuvent forcer 30 à 50 questions et déboucher sur
un design solide. Public cible : développeurs qui veulent industrialiser leur
flow agentique au-delà du simple « vibe coding ».

## Points clés à retenir

- **Les agents sont des ingénieurs sans mémoire** — il faut donc des process écrits, déterministes, qu'on rejoue à chaque session.
- **Un bon skill peut tenir en trois phrases** — la concision et le choix des mots déclencheurs comptent plus que la longueur.
- **`grill me` force le shared understanding** avant tout plan, en parcourant l'« arbre de design » (Frederick P. Brooks, *The Design of Design*) branche par branche.
- **Le PRD décrit la destination, pas le chemin** — il doit rester durable, donc éviter les détails d'implémentation qui périment vite.
- **`PRD to issues` découpe en *vertical slices*** (analogie de la *tracer bullet*) qui traversent toutes les couches, jamais en tranches horizontales.
- **Prioriser les slices qui révèlent les *unknown unknowns*** : faire d'abord les intégrations risquées pour valider la faisabilité.
- **Établir des relations de blocage entre issues** permet d'exécuter en parallèle les tâches indépendantes (idéal pour des agents en background).
- **TDD red-green-refactor est le levier #1 pour la qualité** des sorties d'agents — mais le refactor est le maillon faible (les LLMs sont attachés au code dans leur contexte).
- **Deep modules > shallow modules** : moins de fichiers, mais des interfaces fines et stables — plus facile à tester et à naviguer pour l'IA.
- **Trois sub-agents en parallèle pour proposer des interfaces radicalement différentes** est une excellente méthode pour les refactors d'architecture.
- **Garbage in, garbage out** : un agent dans une codebase sale produira du code sale. Tenir l'archi rangée est un investissement direct sur la qualité IA.

## Développement

### Pourquoi des skills [0:00]

Matt commence par un constat : les agents ont accès à « une flotte d'ingénieurs
moyens à bons » mais sans mémoire entre les sessions. Le rôle du développeur
devient donc de fournir un *process* qui guide l'agent sur le bon chemin à
chaque exécution. Les skills sont sa manière d'encoder ce process — depuis
qu'il les utilise systématiquement, la qualité du code produit a fortement
augmenté.

### Skill 1 — `grill me` [1:19]

Le skill fait littéralement trois phrases : *« Interview me relentlessly about
every aspect of this plan… walk down each branch of the design tree… if a
question can be answered by exploring the codebase, explore the codebase
instead. »* L'idée d'arbre de design vient du livre **The Design of Design**
de Frederick P. Brooks : avant de coder, on parcourt toutes les branches de
décision (recherche simple vs avancée → si avancée, quels filtres, quels tris,
etc.) jusqu'à avoir une vue complète.

L'usage typique : Matt fournit un fichier markdown de recherche et tape
« Grill me ». Sur un cas concret (ajout d'un éditeur de document split-pane à
son éditeur vidéo), Claude lui a posé **16 questions enchaînées**, et il a
déjà eu des sessions de 30 à 50 questions sur des features complexes. Le
skill empêche Claude de cracher un plan trop tôt, ce qu'il a tendance à faire
en *plan mode*.

**Leçon transverse :** un skill court mais bien formulé peut transformer
radicalement le comportement de l'agent.

### Skill 2 — `write a PRD` [4:05]

Une fois le shared understanding atteint, on bascule en rédaction de PRD
(Product Requirements Document). Le skill autorise l'agent à sauter les
étapes déjà couvertes (par exemple le grilling). Ses étapes : description
détaillée → exploration du repo pour vérifier les assertions → grilling
relentless → esquisse des modules à créer/modifier → rédaction finale du PRD
**soumis comme issue GitHub**.

Structure clé du PRD : *problem statement*, *solution*, et surtout des
**user stories** (inspirées d'agile, possiblement en syntaxe Cucumber).
Matt insiste : les *implementation decisions* doivent rester légères pour
que le PRD reste durable même si le code dérive.

### Skill 3 — `PRD to issues` [6:24]

Le PRD décrit la destination ; il manque le voyage. Ce skill localise le PRD,
explore le codebase, puis **découpe le travail en vertical slices** selon
l'analogie de la *tracer bullet* : chaque issue traverse toutes les couches
d'intégration, plutôt que d'être une tranche horizontale d'une seule couche.
Le bon découpage est celui qui **flushe les *unknown unknowns* en premier**
— intégrations nouvelles, services jamais branchés, etc.

Sur le PRD d'éditeur split-pane, Claude a produit **4 slices** dont un moteur
d'édition en pure function avec tests, qui débloquait le reste. Le skill
établit aussi les **relations de blocage** entre issues, ce qui permet :
- d'exécuter en parallèle ce qui est indépendant (utile pour des agents
  background) ;
- d'ajouter ultérieurement des issues de QA qui se branchent dans le graphe.

Matt enchaîne ensuite avec une **Ralph loop** qui itère sur les issues et les
implémente une par une.

### Skill 4 — `TDD` [9:24]

C'est le seul skill volumineux : il contient en plus de la procédure des
notes sur le refactoring, le mocking et les *deep modules*. Matt affirme que
le TDD red-green-refactor est **le levier le plus consistant** pour améliorer
les sorties des agents.

Workflow imposé : confirmer les changements d'interface → confirmer quels
comportements tester → designer les interfaces pour la testabilité →
boucle stricte « un test à la fois, écrit avant le code ».

Anecdote critique sur le refactor : les LLMs sont *« reluctant to refactor
their own code »*. Tant que le code qu'ils viennent d'écrire est dans leur
contexte, ils y sont attachés. Vider le contexte aide à débloquer cette
réticence.

Petite digression sur les **interfaces et implémentations** : un agent
naviguant dans une codebase de mini-modules indifférenciés perd du temps à
comprendre les responsabilités, alors qu'avec quelques *deep modules* à
interface fine il s'oriente vite et peut tester aux frontières naturelles.

### Skill 5 — `improve codebase architecture` [12:32]

Le pendant amont du TDD : si la codebase est mal structurée, le TDD est
ingérable. Ce skill, langage-agnostique, fait :
1. **Explorer la codebase comme le ferait un agent** et noter les confusions
   (concepts qui obligent à sauter entre N petits fichiers, fonctions pures
   extraites *just for testability* alors que les bugs sont dans l'appelant,
   modules tightly coupled aux jointures risquées).
2. **Présenter une liste numérotée de *deepening opportunities*.**
3. L'utilisateur choisit un candidat.
4. **Spawner trois sub-agents en parallèle**, chacun produisant une interface
   *radicalement différente* pour le module à approfondir.
5. Comparer, recommander, éventuellement proposer un hybride.
6. Créer une **issue GitHub de RFC refactor** avec `gh issue create`, qu'on
   peut ensuite enchaîner avec `PRD to issues`.

À faire ~1 fois par semaine, ou après une vague rapide de nouvelles features,
pour empêcher la dérive d'archi.

### Méta-leçon [15:01]

Si on imprimait tous ces skills, on aurait *« un mini-livre markdown de
processes pour humains »*. C'est la thèse de Matt : la meilleure façon
d'obtenir du bon code des agents est de **les traiter comme des humains —
des humains avec des contraintes étranges**, sans mémoire et clonés à la
demande, mais des humains quand même.

## Citations marquantes

> "These engineers… have no memory. They do not remember things they've done before. And so you need extremely strict and well-defined processes to get those agents to actually do things that are useful." — Matt Pocock, [0:15]

> "Skills don't have to be long to be impactful. You've just got to choose the right words for the LLM at the right time." — Matt Pocock, [3:42]

> "Each issue is a thin vertical slice that cuts through all integration layers, not a horizontal slice of one layer." — Matt Pocock, [7:21]

> "If you have a garbage codebase, then the AI is going to produce garbage within that codebase." — Matt Pocock, [15:11]

> "The most successful way to get code quality up from agents is just to treat them like humans. Humans with weird constraints." — Matt Pocock, [15:27]

## Ce que je peux appliquer

- **Écrire un skill `grill me` de 3 phrases** et l'invoquer avant tout plan : forcer l'IA à interviewer plutôt qu'à proposer.
- **Standardiser un PRD léger** centré sur user stories, en gardant les détails d'implémentation hors du PRD pour qu'il reste durable.
- **Découper toute feature en *vertical slices* tracer-bullet**, en attaquant d'abord la slice qui flushe les inconnues techniques.
- **Encoder les blocages entre issues** dans GitHub pour permettre une exécution parallèle d'agents en background.
- **Imposer le red-green-refactor par skill TDD** et accepter que le refactor reste manuel/humain (les LLMs sont attachés à leur code en contexte).
- **Vider le contexte avant un refactor** pour casser l'attachement de l'LLM à son code.
- **Spawner 3 sub-agents en parallèle** pour explorer trois designs d'interface radicalement différents avant de choisir.
- **Faire passer un audit `improve codebase architecture` ~1 fois/semaine** ou après chaque vague de features pour éviter la dérive.

## Références mentionnées

- *The Design of Design* — Frederick P. Brooks (concept du *design tree*)
- *Tracer bullet* — analogie classique du découpage en vertical slices (issue de *The Pragmatic Programmer*, sans citation explicite dans la vidéo)
- Vidéo de l'auteur sur **interfaces vs implémentations** (sa propre chaîne)
- Vidéo de l'auteur sur **red-green-refactor**
- **Ralph loop** — pattern d'orchestration mentionné comme outil personnel de Matt
- Cours **Claude Code for Real Engineers** (cohorte de 2 semaines, lien en description de la vidéo)
