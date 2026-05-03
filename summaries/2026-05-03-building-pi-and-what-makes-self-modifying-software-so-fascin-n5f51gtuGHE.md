---
description: Synthèse de la vidéo "Building Pi, and what makes self-modifying software so fascinating" — pourquoi un agent de code minimaliste auto-modifiable change la donne, et critique de l'industrie du vibe-coding.
video_id: n5f51gtuGHE
url: https://www.youtube.com/watch?v=n5f51gtuGHE&t=86s
title: 'Building Pi, and what makes self-modifying software so fascinating'
author: 'The Pragmatic Engineer'
source_transcript: ../transcripts/2026-05-03-building-pi-and-what-makes-self-modifying-software-so-fascin-n5f51gtuGHE.md
created_on: 2026-05-03
---

# Building Pi, and what makes self-modifying software so fascinating

**Chaîne :** The Pragmatic Engineer • **Lien :** https://www.youtube.com/watch?v=n5f51gtuGHE&t=86s

## TL;DR

Mario Zechner (créateur de **Pi**, l'agent de code derrière OpenClaw) et Armin Ronacher (créateur de Flask) discutent de pourquoi un agent de code minimaliste **auto-modifiable** est plus puissant qu'un agent monolithique, et pourquoi l'industrie est en train de produire massivement du code de mauvaise qualité avec des agents. Thèses centrales : (1) les agents n'éprouvent pas la *douleur* d'un codebase complexe, donc ils n'ont aucun réflexe de refactoring — c'est aux humains de l'imposer ; (2) les bonnes équipes ont besoin de *frictions délibérées*, pas d'autoroutes vers la prod ; (3) MCP est mal pensé pour l'usage dev, le futur c'est la génération de code (CLI + scripts) ; (4) il faut « slow the f down » au lieu d'empiler des armées d'agents (« dark factories »). Vidéo de 1h33 dense en opinions tranchées et concrètes — recommandée si vous travaillez avec des agents de code, maintenez un projet open source, ou réfléchissez à ce que devient le métier d'ingé logiciel.

## Points clés à retenir

- **L'auto-modification est le vrai unlock.** Pi expose ~6 outils (read, write, edit, bash) + un système de hooks TypeScript ; tout le reste — MCP, plan mode, UI custom — se construit en demandant à Pi de se modifier lui-même. Pas besoin de fork.
- **Un bon ingé dit « non » souvent ; un agent dit toujours « oui ».** D'où l'explosion de complexité dans les codebases pilotés par agents.
- **Les agents ne ressentent pas la douleur** d'un mauvais code. Ils ne déclenchent pas de refactor spontané. Conséquence : la dette technique s'accumule sans signal, jusqu'à ce que l'agent lui-même ne s'en sorte plus (saturation du contexte).
- **Le « biais d'automatisation » est le piège n°1** : un agent peut produire du code parfait pendant 5 minutes puis du déchet juste après — et vous ne le verrez pas si vous arrêtez de relire.
- **La friction délibérée** (revues multi-niveaux, SLO, sign-off de directeur sur les tiers critiques) n'est pas de la bureaucratie : c'est ce qui force à se demander « est-ce qu'on veut vraiment faire ça ? ». Les agents poussent à tout supprimer pour aller vite — c'est dangereux.
- **MCP a un problème de composabilité** : impossible de pipe deux serveurs MCP sans repasser par le contexte du modèle. Un CLI fait ça nativement (`|`). Les modèles sont *excellents* pour écrire du code, donc autant leur donner des CLI plutôt que des outils JSON.
- **Les pull requests d'agents accumulent sans intentionnalité.** Mario auto-close toutes les PR de comptes inconnus avec un message demandant d'abord d'ouvrir une issue *en voix humaine*. Les agents ne lisent pas le commentaire → filtre efficace.
- **Le « refactoring impitoyable » est ce qui maintient la qualité de Pi.** Refactorer force Mario à re-lire et comprendre la structure du code — ce qu'aucun agent ne fera spontanément.
- **« Best possible spec is the software itself. »** Toute spec laisse des trous, et le modèle les remplit avec la moyenne de son training data — c'est-à-dire de la médiocrité.
- **L'open source ne meurt pas, le bruit augmente.** Le nombre de projets sérieusement maintenus à long terme est inchangé ; ce qui change c'est le volume de slop éphémère.

## Développement

### Pourquoi Pi existe : l'usure de Claude Code et d'Open Code [32:30]
Mario était fan de Claude Code jusqu'à l'été 2025, où l'équipe a commencé à *dogfooder* à pleine vitesse : modifications silencieuses du system prompt, injection de "system reminders" invisibles dans l'UI, comportement non-déterministe d'une release à l'autre. Il veut un outil « comme un marteau, qui ne casse pas à un endroit différent chaque jour ». Il a même rétro-ingénieré Claude Code pour tracker l'évolution du system prompt (`cc-history`).

Il essaie alors les alternatives commerciales (AMP, Droid) — bonnes mais incompatibles avec son abonnement Claude. Puis Open Code — open source mais qui fait aussi des choses « dans son dos » : pruning des résultats d'outils, appel au LSP server après chaque edit (qui renvoie évidemment des erreurs puisque le modèle n'a pas fini d'écrire). « Devoir forker pour modifier ne devrait pas être nécessaire ». Donc il construit Pi.

### Le design de Pi : minimal + extensible [37:35]
Composants :
- Une abstraction maison sur les APIs des providers LLM (il n'aime pas le SDK Vercel).
- Une boucle d'agent générique (tool calling, streaming).
- Une TUI bespoke qui ne flicker pas.
- 4 outils (read, write, edit, bash). C'est tout.

Tout le reste passe par des *hooks TypeScript* chargés dans le même process Node : tools custom, compaction custom, refonte complète de la TUI, etc. Exemples vus dans la communauté :
- Quelqu'un a re-implémenté MCP par-dessus Pi parce que Pi ne l'a pas en natif.
- Armin a essayé 5 implémentations de plan mode, puis conclu que le plan mode est inutile.
- Quelqu'un a transformé Pi en environnement RL pour entraîner des modèles open weights.
- Mario lui-même n'a que 2 extensions : un widget GitHub qui affiche le titre d'une issue/PR quand il colle un lien.

Idée centrale : « les meilleurs agents seront *spécialisés*, pas généralistes. Comme sur un chantier — tu n'utilises pas le marteau pour tout. »

### Pourquoi les codebases pilotés par agents pourrissent [17:30 — 22:30]
Récit fondateur de Mario sur le matchmaker de *Halo Master Chief Collection* : 16 booléens dans une « emergence state machine » avec 6 états valides en théorie mais des milliers en pratique. Le code généré par agent ressemble à ça, en pire : au lieu de planter (« config invalide → on stop »), l'agent rajoute un fallback (« on charge la config par défaut »), donc le code devient plus complexe et accumule des chemins de récupération illégitimes.

Trois forces à l'œuvre :
1. **Les agents disent toujours oui.** Comme l'utilisateur n'a pas à taper le code lui-même, il ne s'auto-censure plus. « Je veux ça, et ça, et ça. » → complexité explosive.
2. **Les agents n'ont pas de mémoire de la douleur.** Un humain qui a souffert d'un codebase pourri prend des décisions structurantes pour éviter de revivre ça. Un agent ne retient rien entre les sessions, même avec un système de mémoire.
3. **Biais d'automatisation.** Le code paraît bon → on relit moins → la qualité chute sans signal.

### Le rôle des ingés seniors devient plus dur, pas plus facile [22:00 — 24:30]
Avant : le senior dit non, point. Maintenant : 48 h plus tard, le junior revient avec une *defense complète* générée par l'agent qui justifie l'inverse. Comparaison frappante d'Armin : « comme les patients qui arrivent chez le médecin avec une impression ChatGPT en disant *vous feriez mieux de prescrire ça* ». L'autorité du senior s'érode parce que le junior a maintenant un accès gratuit à du *world knowledge* synthétisé.

### Non-ingés dans le pipeline de code [24:40]
Le marketing pousse des features sur le site, le sales build une démo qui montre une fonctionnalité qui n'existe pas et personne ne s'en rend compte. C'est *empowering* (la designer peut transformer son Figma en clickable), mais on a oublié les garde-fous. « Tout le monde peut tout faire » nécessite des *process*, pas leur abolition.

### Le concept de "prompt request" et pourquoi Armin n'est pas d'accord [27:20]
Peter Steinberger propose qu'on lui envoie le *prompt* plutôt que la PR. Mario et Armin sont nuancés :
- L'acte de générer du code clarifie ce qu'on veut → précieux.
- Mais voir une *implémentation merdique* permet à Mario d'éviter de tester lui-même cette voie. C'est de la « valuable garbage ».
- Donc PRs d'agents ≠ bullshit pur, mais doivent être *filtrées*.

### La friction comme feature, pas comme bug [1:06:30 — 1:09:30]
Anecdote déclic : Armin voit une boîte qui a un incident de sécurité après un changement de config. Le tagline de la boîte : *« ship without friction »*. La friction n'est pas toujours une mauvaise chose :
- Tier 1 service → 2-3 reviews + sign-off d'un directeur. Pas pour ralentir, mais pour *forcer la pause* sur les actions destructrices (drop DB, migration avec lock, etc.).
- L'incentive : « est-ce que je *veux vraiment* mettre ça dans ce codebase si je sais que ça va devoir traverser tout ce process ? »

L'industrie supprime ces frictions pour permettre aux agents de tourner en parallèle. Mario : « c'est faux d'opposer friction et productivité — la friction te permet de dormir la nuit. »

### CLI vs MCP [1:16:00 — 1:23:30]
Critique technique fine de MCP, à plusieurs niveaux :
- **Origine** : MCP a été conçu pour brancher des services externes à des chats consumer (Gmail, OneDrive…). Ce use case est légitime — « je ne veux pas que ma mère écrive du code pour appeler une API ». Mais il a été détourné par les devs.
- **Composabilité nulle** : pour combiner deux outils MCP, il faut faire passer leurs sorties par le contexte du modèle. Comparé à un pipe shell (`|`) qui ne pollue pas le contexte, c'est une régression.
- **Mauvais MCP servers** : des grosses boîtes mappent leur OpenAPI spec entière en N tools → garbage.
- **Solutions intéressantes** : *Code Mode* de Cloudflare, qui expose les MCPs comme des fonctions TypeScript et laisse le modèle écrire du code de composition. Stainless qui génère des SDKs depuis OpenAPI specs.
- **Mario** : « les modèles ne vont nulle part ailleurs que vers la génération de code pour tout ce qui est agentic — il y a juste trop de training data dans cette direction. »
- L'auth reste le vrai problème non résolu pour les CLIs en environnement enterprise.

### Le « dark factory » et la guerre du débit [1:11:50 — 1:16:00]
Hypothèse de l'industrie : 100 agents en parallèle + spec → produit fini. Réfutation de Mario :
- Si l'agent a *la moitié* du taux d'erreur d'un humain mais produit *10×* plus de code, il génère *5× plus de bugs*.
- Aucun humain ne peut reviewer 10 000 lignes/jour.
- La *meilleure spec possible est le logiciel lui-même*. Toute autre spec a des trous → l'agent les remplit avec la *moyenne du training data* → médiocrité.

### Bottlenecks pour l'open source [54:00 — 1:00:00]
Pi & OpenClaw reçoivent un déluge de PRs auto-générées sans *intentionnalité* derrière. Solution de Mario :
- Workflow GitHub : si l'auteur n'est pas dans un fichier whitelist du repo, sa PR est auto-fermée.
- Commentaire automatique : « Merci, ouvre d'abord une issue en voix humaine, max une page d'écran. Si je dis LGTM, je t'ajoute à la whitelist. »
- **Bonus inattendu** : les agents ne lisent pas ce commentaire et n'y répondent pas. Filtre humain/agent gratuit.
- Pour les issues : Mario a construit un outil qui visualise issues+PRs dans un *espace 3D* pour clusteriser les doublons et bulk-fermer.

Armin contredit l'idée que l'open source est mort : le nombre de projets long-terme bien maintenus n'a pas changé. Ce qui a changé c'est le volume de projets éphémères (« slop »), surtout dans le méta-tooling agentic (« ouroboros »).

### Hygiène mentale [1:28:00 — 1:31:00]
- Ne pas vivre à San Francisco.
- Avoir des enfants, sortir, grimper aux arbres, faire du patin à glace.
- Ignorer les notifications. Si c'est important, ça reviendra.
- Stratégie d'Armin sur Twitter : attendre 3 semaines. Si le sujet est encore là, alors c'est probablement réel.
- « Une période de hype où on se prend des œillères, c'est normal. Puis on overcorrect, puis on se cale. »

## Citations marquantes

> « I personally think a good engineer is an engineer that says no a lot, and "I don't need this" a lot. […] If you're using agents, the exact opposite happens. You say yes, I want this and that, because I don't have to type it myself. » — Mario, [21:50]

> « Agents don't feel pain. And I think that's one of the defining things about humans. Eventually, if the pain gets too big, you as a human are incentivized to fix the cause of your pain. » — Mario, [21:27]

> « All the companies claiming that all of their code is now written by agents — yes, we know the quality is garbage. We feel it in our bones when we use your products. It's garbage. » — Mario, [1:14:02]

> « The best possible spec is the software itself. » — Mario, [1:15:31]

> « I want it [my dev tool] to be a stable, reliable thing like a hammer. I don't want my hammer to break at a different spot every day. » — Mario, [34:34]

> « It turns out that passage of time sometimes clarifies stuff a lot. If it's really necessary, it's going to reach you again. » — Armin, [1:29:00]

## Ce que je peux appliquer

- **Refactorer impitoyablement les parties critiques de mon code**, *moi-même*, pour me forcer à comprendre la structure. Laisser l'agent gérer les bouts non-critiques (export HTML, glue code, etc.).
- **Identifier les tiers de mon code** : où la friction est nécessaire (auth, paiement, données utilisateurs) vs où elle est juste de la dette de DX. Mettre des gates explicites sur les premiers.
- **Pour mes repos open source : auto-fermer les PRs de comptes inconnus** avec un message demandant d'abord une issue humaine. Filtre agent/humain gratuit.
- **Préférer les CLIs scriptables** aux MCPs pour les workflows où je veux composer plusieurs outils.
- **Quand je donne une spec à un agent, accepter qu'elle a des trous et que l'agent les remplira avec la médiocrité moyenne.** Soit je remplis les trous moi-même, soit j'accepte le résultat avec recul.
- **Discipline d'attention** : attendre 3 semaines avant de me prononcer sur la dernière hype.
- **Garder la boucle humaine** : le fait que l'agent puisse valider tout seul ne me dispense pas d'être impliqué — c'est même *là* que les meilleurs résultats émergent (cf. anecdote de Pi qui montre des screenshots dans la TUI pour le jeu).

## Références mentionnées

- **Pi** — agent de code minimaliste auto-modifiable de Mario Zechner.
- **OpenClaw** — assistant personnel WhatsApp/IA de Peter Steinberger, basé sur Pi.
- **`cc-history` (Mario.at)** — service de Mario qui track l'évolution du system prompt et des tool definitions de Claude Code.
- **Cloudflare Code Mode** — expose les serveurs MCP comme des fonctions TypeScript.
- **Stainless** — générateur de SDKs à partir d'OpenAPI specs.
- **Vercel AI SDK** — abstraction multi-provider que Mario et Armin n'aiment pas.
- **Article « We all need to slow the f down »** — blog post de Mario.
- **Idée du « prompt request »** — Peter Steinberger.
- **Livre *Code* (Charles Petzold)** — recommandation de Mario.
- **Livre *Breakneck*** — recommandation d'Armin (sur la Chine vs Europe/USA).
- **Kell Henderson** — cité par Armin pour « do the dumbest solution first until it doesn't work anymore ».
- **Sentry** — Armin y a travaillé 10 ans avant de partir en avril dernier.
- **Flask** — créé par Armin.
