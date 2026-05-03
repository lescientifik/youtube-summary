---
description: Synthèse de la vidéo "Mergeable by default: Building the context engine to save time and tokens — Peter Werry, Unblocked" — Pourquoi un moteur de contexte est devenu le vrai goulot d'étranglement des agents de code, et comment le construire au-delà du RAG naïf.
video_id: 5ID22ACI7IM
url: https://youtu.be/5ID22ACI7IM?is=cBqQ690YMG3ffDqF
title: 'Mergeable by default: Building the context engine to save time and tokens — Peter Werry, Unblocked'
author: 'AI Engineer'
source_transcript: ../transcripts/2026-05-03-mergeable-by-default-building-the-context-engine-to-save-tim-5ID22ACI7IM.md
created_on: 2026-05-03
---

# Mergeable by default: Building the context engine to save time and tokens

**Chaîne :** AI Engineer  •  **Lien :** https://youtu.be/5ID22ACI7IM?is=cBqQ690YMG3ffDqF

## TL;DR

Talk + atelier de Peter Werry (Unblocked) à AI Engineer London sur ce qu'est un *context engine* et pourquoi ni le RAG naïf, ni l'agrégation de serveurs MCP, ni l'extension de la fenêtre de contexte ne suffisent à le remplacer. Public visé : ingénieurs et architectes IA qui veulent passer d'agents pilotés à la main à des agents autonomes en arrière-plan sans tomber dans des *doom loops*. Thèse centrale : à mesure que les modèles deviennent quasi parfaits en intelligence de code (cf. Mythos), le goulot d'étranglement n'est plus le raisonnement mais la qualité du contexte injecté en amont — un bon contexte sur 90 % du chemin de l'agent, l'écriture du code n'étant que 10 %. Conclusions concrètes : un *context engine* doit comprendre les relations (pas juste indexer), arbitrer les conflits (et les *remonter* quand il échoue), respecter les ACL, et privilégier la direction *future* du code plutôt que sa version actuelle. Valeur d'apprentissage : retours d'expérience honnêtes sur ce qui ne marche pas (cache de réponses, biais sur la récence, RAG plat) + heuristiques pour construire le sien (graphe social, *bottling the expert*, distillation incrémentale).

## Points clés à retenir

- **Le contexte est le nouveau bottleneck**, pas l'intelligence du modèle. Les agents tombent en *doom loop* faute de comprendre l'historique, les décisions passées et les conventions de l'organisation.
- **Accès ≠ compréhension.** Câbler 15 MCP à un agent ne lui apprend pas comment les données sont liées entre elles ni *pourquoi* le code est ce qu'il est.
- **Satisfaction of search** (terme emprunté à la radiologie) : un agent s'arrête dès qu'il trouve quelque chose qui *ressemble* à la réponse, ratant le vrai gisement (vieux thread Slack, post-mortem d'incident, etc.).
- **Une plus grande fenêtre de contexte ne sauve pas la mise** : la plupart des organisations dépassent 1 M tokens de contexte pertinent, et les modèles restent mauvais pour raisonner *à travers* sources hétérogènes.
- **Surfacer les conflits plutôt que les masquer.** Les premières heuristiques naïves (biais récence, biais branche `main`) cachent des conflits non résolus ; mieux vaut les exposer à l'utilisateur pour apprendre.
- **Ne JAMAIS cacher les réponses du moteur** pour les resservir : régression vers la moyenne et pollution du contexte garanties.
- **La direction future > l'état actuel.** Sur une tâche, ce que veut l'agent c'est savoir où le code *va*, pas seulement où il est ; le passé sert surtout à dire ce qu'il *ne faut pas* refaire.
- **Le graphe social comme pivot de retrieval.** Identifier les experts par zone de code permet de "déboucher" leurs apprentissages distillés (PR, Slack, décisions) comme contexte de seed pour l'agent.
- **Les tokens de sortie tirent la latence vers le bas**, pas les tokens d'entrée — donc fournir un contexte *dense* est doublement gagnant.
- **Compartimentage strict des ACL** dans la synthèse de données : approche group-ID, jamais de graph RAG global qui empile des résumés à travers les frontières d'accès.

## Développement

### Pourquoi le *context engine* émerge maintenant [2:26]
Il y a quatre ans, c'est l'humain qui était le moteur de contexte : il sélectionnait le ticket, le code pertinent, et corrigeait l'agent quand celui-ci partait à côté. Avec la montée en puissance des agents parallèles et des background agents en YOLO mode, l'humain devient le goulot — context-switching épuisant, supervision impossible. Werry cite Karpathy sur l'idée que les systèmes deviennent intelligents (Mythos est mentionné comme "quasi parfait") : à partir de là, c'est la qualité du contexte qui détermine si l'agent termine en 25 minutes ou en 2h30.

### Les trois mythes [10:48]
1. **"Le RAG naïf sur mes docs = un context engine."** Faux : sans personnalisation par utilisateur, sans résolution de conflits, et sans signal sur quels repos sont pertinents pour *cette* personne, le RAG plat empire le problème dans les grandes orgas.
2. **"Brancher plein de MCP = un context engine."** Faux : ça maximise au contraire la *satisfaction of search*. L'agent s'arrête au premier indice plausible et rate le contenu vraiment décisif.
3. **"Une fenêtre de contexte plus large résoudra tout."** Faux : les orgas dépassent largement 1 M tokens de contexte utile, et même avec 50 M, le problème de discriminer le vrai du faux et de raisonner cross-source reste entier.

### Les six exigences d'un vrai moteur [15:48]
- **Unified system contexts** : construire des relations *sémantiques* (motivations, best practices distillées de PR comments répétés) et pas juste des liens triviaux (ex. PR → Slack qui le mentionne).
- **Conflict resolution** : la première version d'Unblocked biaisait sur la récence ; insuffisant, parce que des docs ou des chats peuvent contredire le code. Deuxième tentative : biais sur `main`. Toujours faux, parce que l'utilisateur veut souvent aller *contre* le code actuel. Solution finale : combiner ranking au moment de l'ingestion + LLM-as-judge au moment du runtime + **remonter les conflits non résolus à l'humain**.
- **Targeted retrieval + personal relevance** : utiliser le nombre de PR par repo pour pondérer le retrieval vectoriel — recherche profonde sur les repos focus de l'utilisateur, recherche large ailleurs.
- **Data governance** : flow up des ACL, en particulier pour Slack (canaux privés) et les repos confidentiels. Synthèse compartimentée par repo, group-ID sur les memories qui traversent.
- **Right context at the right time** : token efficiency.

### Leçons apprises (les ratés assumés) [23:23]
- "On a optimisé pour l'accès et pas la compréhension" : un knowledge graph + des outils de retrieval ne suffisent pas, il faut des couches de distillation au-dessus.
- "On cachait les conflits au lieu de les surfacer" : on essayait de les résoudre silencieusement avec des heuristiques naïves. Erreur.
- "On a essayé de cacher les réponses pour resservir" : double piège — le code change, et utiliser les anciennes réponses comme contexte fait régresser le modèle vers ses propres erreurs.

### Où le moteur apporte le plus de valeur [25:36]
Par ordre décroissant de ROI : **planification** (de loin le meilleur ratio), **revue de code** (le modèle voit la motivation, pas juste les bugs), **enrichissement de ticket**, **triage d'incidents**, **gestion d'incidents** (Sentry + Datadog branchés permettent de corréler signaux ↔ code ↔ post-mortems passés), et — surprise commerciale — **support engineering / customer success** : les channels Slack de support deviennent auto-répondants.

### Architecture interne [38:00]
Trois couches de retrieval empilées :
1. Knowledge graph procédural (style PageRank sur les entités).
2. Recherche vectorielle classique sur le code et les documents.
3. **Memories distillées** + *bottling the expert* : on agrège PR comments, conversations Slack, décisions d'un individu pour produire un "expert en bouteille" qui sert de *seed context* à l'agent quand il travaille sur la zone de code de cet expert. Le graphe social sert de pivot pour savoir *quel* expert déboucher.

### Pourquoi le graphe social ne se résume pas à des stats [1:08:50]
Première version : ratio PR contribuées / PR reviewées par personne — clusters d'équipe inexacts. Deuxième : algorithmes de réseau classiques (montrés dans l'atelier). Troisième couche, propre à Unblocked : clusters par proximité vectorielle dans le code source + distillation LLM des conversations passées. Sur Teams/SharePoint, plus de signal PR → on bascule sur fréquence par canal, vectorisation des résumés de canal, puis recoupement avec le SCM pour filtrer le "junior bruyant" (volume haut, signal bas).

### Le vrai bottleneck de latence : les output tokens [1:30:38]
Werry insiste : sur un agent en boucle, ~90 % du temps est consommé par la collecte de contexte et seulement ~10 % par l'écriture. Et au sein du LLM, le coût dominant est le débit en *sortie*, pas en *entrée* — donc densifier le contexte (input plus gros mais mieux ciblé) est doublement gagnant : moins d'allers-retours et moins de tokens en sortie.

### Métriques mesurées [22:13][1:31:35]
Sur l'implémentation de l'*adaptive thinking* d'Anthropic :
- Sans context engine (Claude + MCP GitHub + Slack vanille) : **2h25 wall clock, 21 M tokens**, 4 boucles de correction humaines parce que la première sortie était fausse.
- Avec Unblocked seul branché (mêmes prompts, même accès) : **25 min, 10 M tokens**, première sortie correcte.

Score de satisfaction interne (équivalent NPS adapté) : ~60 sur une échelle [-100, 100], soit ~0.75–0.8 normalisé.

### L'humain reste dans la boucle, mais comme oracle [40:07]
Quand le moteur n'arrive pas à arbitrer un conflit, il *expose* les références à l'humain dans l'UI. L'humain peut répondre "pas correct" + raison ; ces signaux pondèrent une *task memory*. Détail important : le poids du feedback dépend de la position de l'utilisateur dans le graphe social — un expert reconnu sur la zone pèse plus qu'un nouvel arrivant.

### Distinction avec les LLM wikis et les exploratory agents [33:29][58:23]
Un wiki traversable (façon Karpathy : "le wiki comme un filesystem") est un composant utile, mais pas un moteur de contexte : il manque la distillation des best practices répétées, le graphe d'experts, la gestion d'ACL et la résolution de conflits multi-sources. De même, un sub-agent exploratoire pourrait reconstruire un graphe social, mais (a) il devrait le refaire à chaque fois, (b) il doit *écrire du code* pour le calculer — autant pré-calculer et offrir l'artefact.

### Roadmap & vision [1:02:24]
Cap mis sur les agents fully-autonomous. Conséquence contre-intuitive : la latence des MCP devient *moins* critique, ce qui compte est qu'ils donnent la *bonne* réponse — parce que le coût d'une mauvaise réponse en mode autonome est colossal (doom loop sans humain pour rattraper). Roadmap court-terme orientée API et CLI.

## Citations marquantes

> "Access doesn't equal understanding." — Peter Werry, [8:31]

> "Where you've been helps it understand what not to do. Where you're going helps it understand what you should do." — Peter Werry, [20:48] (sur le biais récence/main vs. direction future)

> "AI generated code should just feel like it was written by someone that's been in your team for 20 years." — Peter Werry, [31:14]

> "Agent context collection is probably close to 90%. The actual code writing part is really really fast." — Peter Werry, [1:30:42]

## Ce que je peux appliquer

- **Avant d'investir dans plus de MCP, vérifier la satisfaction of search** : instrumenter mes agents pour voir s'ils s'arrêtent au premier match plausible, et ajouter un protocole anti-arrêt-prématuré inspiré de la radiologie.
- **Surfacer les conflits non résolus** dans l'UI agent au lieu de les arbitrer silencieusement par heuristique récence ou "main wins".
- **Ne pas cacher les réponses du système RAG pour les resservir.** Si on garde une trace, c'est pour audit, pas pour réinjection en contexte.
- **Pondérer le retrieval vectoriel par les repos où l'utilisateur a le plus de PR** — gain immédiat de pertinence pour quasi rien.
- **Distiller les PR comments répétés en "memories"** réutilisables par l'agent au moment du planning : c'est probablement le levier ROI le plus élevé.
- **Mesurer en wall clock + tokens totaux**, pas seulement en latence par appel : la métrique qui compte est "minutes pour merger" et "tokens pour merger".
- **Densifier le contexte en entrée pour réduire la sortie** : un input plus gros mais bien ciblé bat un input minimaliste qui force l'agent à reboucler.
- **Compartimenter la synthèse cross-source par groupID** dès le départ ; ne jamais empiler des résumés graph-RAG qui traversent les frontières d'ACL.

## Références mentionnées

- **Mythos** (modèle de code récemment annoncé) — cité comme exemple d'intelligence de code "quasi parfaite".
- **Andrej Karpathy** — sur l'idée du wiki traité comme un filesystem traversable par l'agent.
- **Vimath / Vim** — courbe d'adoption des agents de code (autocomplete → agentic IDE → parallel agents → background agents).
- **Boris Cherny** (créateur de Claude Code) — interview sur la mesure du succès par le "vibes / sentiment" et les benchmarks comme `talk`.
- **Satisfaction of search** — concept emprunté à la radiologie médicale.
- **Sentry, Datadog** — intégrations Unblocked pour incident management.
- **Composio** — cité comme exemple d'agrégateur de tool use à très haute consommation de tokens.
- **Graph RAG** — cité comme contre-exemple architectural à cause de l'empilement de résumés à travers les ACL.
