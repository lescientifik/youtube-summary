---
description: Synthèse de la vidéo "DjangoCon 2022 | Quality Assurance in Django - Testing what matters" — pourquoi il faut arrêter de tester boîte par boîte et privilégier des tests d'intégration qui rejouent les parcours utilisateurs.
video_id: PChaEAIsQls
url: https://youtu.be/PChaEAIsQls?is=Bvi8BdYUPaICjzgI
title: 'DjangoCon 2022 | Quality Assurance in Django - Testing what matters'
author: 'DjangoCon Europe'
source_transcript: ../transcripts/2026-05-05-djangocon-2022-quality-assurance-in-django-testing-what-matt-PChaEAIsQls.md
created_on: 2026-05-05
---

# DjangoCon 2022 | Quality Assurance in Django - Testing what matters

**Chaîne :** DjangoCon Europe  •  **Lien :** https://youtu.be/PChaEAIsQls?is=Bvi8BdYUPaICjzgI

## TL;DR

Talk de Radoslav Georgiev (CEO de HackSoft) destiné aux développeurs Django qui se demandent *quoi* tester et pas seulement *comment*. Sa thèse : la culture du test unitaire poussée par défaut conduit à un « busy work » qui valide surtout que Django fonctionne, sans capturer de vraie régression. La stratégie qu'il défend est d'écrire d'abord des tests d'intégration qui partent d'un endpoint (API/vue) et rejouent un *user journey* complet — Django sert alors de framework d'automatisation de test, avec accès direct à la base pour les assertions. Les tests unitaires sont réservés aux zones pures (utilitaires, validateurs, logique métier découplée du modèle). Conclusion pratique : remplacer la pyramide des tests par un « gâteau » plus épais en intégration, et se rappeler que la QA dépasse les tests (style guide, mypy, archi).

## Points clés à retenir

- **« Tester boîte par boîte » est un piège** — Choisir les feuilles du graphe d'appels (utils, modèles) garantit du vert mais ne protège quasiment de rien : on teste l'ORM de Django, pas l'application.
- **Maximiser la couverture des *code pathways* avec un minimum de tests** — un test qui part de l'API traverse vues, sérialiseurs, business logic, ORM, callbacks ; un test unitaire ne traverse qu'une feuille.
- **Le point d'entrée naturel d'une app Django, c'est la vue/l'API** — c'est là qu'il faut commencer à écrire des tests, pas dans `utils/`.
- **Penser *user journeys*, pas *fonctions*** — décrire en docstring les étapes (« user starts verification → tries wrong code → tries correct code → obtains token → logs out → token revoked »), puis implémenter chaque étape.
- **Django EST un framework d'automatisation de test** — l'accès direct à la base permet d'asserter l'état interne après un appel d'API, ce qu'un test E2E externe ne fait pas aussi facilement.
- **L'abstraction `given_a_user(...)`** rend les tests lisibles et découple l'implémentation (factory, ORM direct, autre user journey…) du test lui-même.
- **Couvrir aussi Celery et les transaction callbacks** — exécuter Celery en mémoire dans les tests, mocker les vrais services externes (S3, etc.), capturer les `on_commit` (désormais natif dans Django).
- **Garder les tests unitaires purs pour la logique sans I/O** — ex. tester une méthode `clean()` d'un modèle sans toucher la DB, valider en mémoire.
- **Pyramide → « test cake »** — dans le contexte Django (front exclu), on autorise plus de poids sur l'intégration ; les tests sont plus lents mais bien plus utiles.
- **La QA, ce n'est pas que les tests** — un style guide interne, `mypy`, l'expérience développeur, l'architecture et le déploiement sont aussi des leviers de qualité.

## Développement

### Pourquoi on écrit des tests, vraiment [1:02]
Le pitch d'ouverture est volontairement banal : pousser en prod, ça marche « la plupart du temps » — sauf quand ça casse, et là le mème du chien dans la pièce en feu (« this is fine ») prend tout son sens. Tester manuellement (cliquer, appeler une CLI/API) ne passe pas l'échelle et est sujet à l'erreur humaine et à la fatigue. La QA est définie ici comme le processus qui vise à *réduire la fréquence* du « this is fine » et à attraper les régressions (« mais ça marchait la semaine dernière »).

### Le piège du « DAG des modules » [4:55]
Sur un schéma classique Django (vues/API → forms/serializers → business logic → ORM → DB, plus Celery, Redis, intégrations tierces), le réflexe du développeur est de partir des feuilles : `utils/`. Ça donne une boucle de feedback rapide et documente l'usage — c'est légitime pour une fonction pure. Mais en avançant on tombe sur :
- des utilitaires qui touchent la DB (ex. wrapper de `get_object_or_404` qui catche l'exception) → il faut déjà passer de `unittest.TestCase` au `TestCase` de Django ;
- des tests de modèles qui ne font que vérifier que **l'ORM de Django fonctionne** — ce que Django teste déjà chez lui. Vert au CI, valeur quasi nulle.

Si on persiste dans cette voie, on entre dans la « forêt dense » : tout devient un *unit*, on commence à mocker, un mois plus tard on revient repenser la stratégie. Beaucoup de lignes ajoutées en PR, peu de confiance gagnée.

### Reposer la bonne question [11:36]
Avant d'écrire un test, demander : *qu'est-ce que je veux obtenir ?* Les bonnes réponses sont :
- plus de confiance pour livrer (réduire l'anxiété qu'un changement casse autre chose ailleurs) ;
- attraper les régressions ;
- réduire le « user-driven development » (= la prod casse, l'utilisateur signale) ;
- éviter le busy work ;
- rester en contexte Django (pas de Selenium/E2E client ici).

### La stratégie : couvrir un maximum de chemins [13:27]
Les utilisateurs traversent des *code pathways*. Un bon test simule ce parcours et fait des assertions à la fin. Conséquence : commencer par tester les **points d'entrée** (vues/API), parce qu'ils déclenchent tout le reste en aval.

Forme concrète d'un tel test :
- une `TestCase` Django (besoin de la DB) ;
- une **docstring qui décrit le user journey** étape par étape ;
- l'implémentation utilise Faker pour les données, envoie des requêtes HTTP, asserte les réponses ET asserte l'état interne (queries directes en DB).

Ce style mélange test d'intégration et BDD. Sa puissance vient de ce qu'il **exerce simultanément le code framework et le code métier dans leur intégration** — chose impossible avec des tests unitaires isolés.

### Django comme framework d'automatisation de test [19:02]
Dans le monde QA classique, on construit (ou on achète) des *test automation frameworks*. Pour une app Django, Django joue déjà ce rôle : on attaque l'API comme un utilisateur final, mais on a un accès direct à l'ORM pour asserter l'état interne. C'est strictement plus puissant qu'un test E2E pur, qui ne voit que la sortie.

### Le helper `given_a_user(...)` [19:45]
Pour tester l'expiration d'un token : `given_a_user(...)` retourne un user prêt à l'emploi, on appelle des endpoints, on overwrite les settings, on asserte. La force de cette convention : **l'implémentation de `given_*` est libre** — replay d'un autre user journey via API, factory_boy, ORM direct… Le test reste lisible et découplé de la mécanique de fixture.

### Couvrir encore plus de terrain : Celery et `on_commit` [21:24]
Pour se rapprocher d'un E2E sans en payer le prix :
- exécuter Celery **en mémoire** (`CELERY_TASK_ALWAYS_EAGER` ou équivalent) ;
- mocker les sorties externes (S3, providers SMS…) ;
- capturer les `on_commit` callbacks — outil désormais intégré à Django.

Le pattern récapitulatif : *given un état → rejouer un user journey → utiliser Django comme framework d'automatisation → asserter l'état interne → couvrir un maximum de terrain*.

### Le coût et l'exception qui justifie l'unitaire [22:55]
Trade-off assumé : ces tests sont plus lents, le CI plus long. Si on hérite d'un projet à 0 % de couverture à maintenir, c'est quand même là qu'il faut investir d'abord — on peut écrire ces tests sans même connaître le projet, juste en partant des points d'entrée et des user journeys.

À l'inverse, si on a une `clean()` sur un modèle ou une fonction de validation pure, l'attaquer via un test d'API serait du gaspillage. Un test unitaire focalisé fait mieux le job — sans même persister le modèle en base.

### Pyramide vs « test cake » [24:14]
La pyramide classique (beaucoup d'unitaires, peu d'intégration, encore moins d'E2E) est ici remplacée par un *test cake* (avec une cerise sur le dessus) : on exclut le E2E (front hors scope), on autorise une part importante d'intégration. Le slide clé pour Radoslav : sur le schéma de l'app Django, identifier ce qui doit aller à droite (intégration : vues, API, business logic + DB) vs à gauche (unitaire : utils, business logic découplée), et la zone grise au milieu (validation, etc.) qui peut tomber des deux côtés selon l'intention.

### La QA dépasse les tests [26:34]
On peut **augmenter la qualité d'un projet sans écrire un seul test** :
- un *style guide* interne (HackSoft a publié son [HackSoft Django Style Guide](https://github.com/HackSoftware/Django-Styleguide) — auquel l'orateur fait implicitement référence) ;
- `mypy` comme outil de QA (idem TypeScript côté front) ;
- l'expérience développeur, l'architecture, le pipeline de déploiement.

## Citations marquantes

> "We will start with tests that cover as many code pathways as possible with as little tests as possible." — Radoslav Georgiev, [14:04]

> "Django itself has tests like this that make sure that the framework is working." — Radoslav Georgiev, [9:29] *(à propos des tests qui ne valident en réalité que l'ORM)*

> "You can assure a decent amount of quality on a project without writing a single line of tests." — Radoslav Georgiev, [26:58]

## Ce que je peux appliquer

- **Sur un projet legacy à faible couverture :** commencer par lister les points d'entrée (URLconf, endpoints DRF) et écrire un test d'intégration par user journey critique avant de descendre dans l'unitaire.
- **Renommer ses fichiers de tests autour des journeys** (ex. `test_account_recovery_journey.py`) plutôt qu'autour des modules de code (`test_views.py`).
- **Standardiser un helper `given_a_user(...)`** dans une `tests/factories.py` ou `tests/given.py` partagée, à implémentation libre, pour découpler le *quoi* du *comment*.
- **Pour Celery dans les tests :** activer l'exécution synchrone en mémoire et capturer les callbacks `on_commit` plutôt que de mocker tâche par tâche.
- **Garder l'unitaire pour le pur** : `clean()`, validateurs custom, pure business logic — ne pas instancier la DB pour ça.
- **Compléter la batterie de tests par du `mypy` strict et un style guide écrit** — c'est de la QA aussi, et souvent à meilleur ROI qu'une nouvelle classe de tests.

## Références mentionnées

- HackSoft — entreprise de l'orateur, basée en Bulgarie.
- HackSoft Django Style Guide — style guide interne cité comme outil de QA.
- `mypy` — type-checker Python utilisé comme outil d'assurance qualité.
- `factory_boy` — l'orateur renvoie à un autre talk DjangoCon 2022 sur le sujet plutôt que de le couvrir lui-même.
- Faker — pour la génération de données de test.
- Django `on_commit` / capture des transaction callbacks (anciennement package externe, désormais intégré).
