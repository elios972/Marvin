# MARVIN

MARVIN est un assistant personnel développé en Python, conçu pour évoluer progressivement vers un assistant intelligent capable de comprendre les demandes de son utilisateur, d'utiliser des outils et d'exécuter différentes tâches.

Le projet avance étape par étape afin de construire une architecture modulaire, fiable et facile à faire évoluer.

## Fonctionnalités actuelles

- Dialogue en ligne de commande.
- Personnalisation du dialogue avec le prénom de l'utilisateur.
- Reconnaissance de commandes textuelles et de leurs alias.
- Salutations personnalisées.
- Affichage de l'heure actuelle.
- Aide listant les commandes disponibles.
- Comptage des commandes reconnues.
- Modification et sauvegarde du prénom de l'utilisateur avec la commande `renommer`.
- Sauvegarde persistante des données.
- Structure de mémoire préparée pour prendre en charge plusieurs profils.
- Normalisation des commandes, notamment pour les accents et la ponctuation.

## Technologies utilisées

- **Python 3.14**
- Modules natifs de Python : `datetime`, `json`, `pathlib`, `re` et `unicodedata`.
- Git et GitHub pour le suivi des versions.

## Installation et lancement

### Prérequis

Python doit être installé sur la machine.

### Lancer MARVIN

Depuis le dossier racine du projet, exécuter :

```bash
python main.py
```

## Commandes disponibles

| Commande | Description |
|---|---|
| `bonjour` | Saluer MARVIN |
| `heure` | Afficher l'heure actuelle |
| `aide` | Afficher les commandes disponibles |
| `combien de commandes` | Afficher le nombre de commandes reconnues |
| `renommer` | Modifier le prénom utilisé par MARVIN |
| `quitter` | Fermer MARVIN |

## Structure du projet

```text
MARVIN/
├── main.py
├── README.md
├── .gitignore
└── marvin/
    ├── __init__.py
    ├── assistant.py
    ├── commands.py
    ├── command_aliases.py
    └── state.py
```

## Principes d'architecture

- **Modularité :** séparer le cœur de MARVIN, la mémoire, l'IA et les outils pour les faire évoluer indépendamment.
- **IA locale privilégiée :** limiter la dépendance aux services distants et préserver la confidentialité des données.
- **Bibliothèque d'outils extensible :** pouvoir ajouter, remplacer et découvrir des capacités sans réécrire le cœur de MARVIN.
- **Autonomie contrôlée :** permettre la planification et l'enchaînement de tâches tout en encadrant les permissions et les actions sensibles.
- **Fiabilité :** gérer les erreurs et vérifier les résultats lorsque c'est possible.
- **Évolution durable :** conserver les fonctionnalités opérationnelles et éviter les changements technologiques inutiles.

Les modèles d'IA et leurs fichiers volumineux seront séparés du code source. Le traitement local ne garantit la confidentialité que si les autres composants utilisés respectent également ce principe.

## Roadmap

Les étapes suivantes sont des objectifs de développement, pas des fonctionnalités déjà disponibles. Leur ordre pourra être adapté si des contraintes techniques le justifient.

### Phase 1 — Fondations

1. **Gestion multi-profils :** créer des profils, passer de l'un à l'autre, isoler leurs données et préparer différents niveaux d'autorisation.
2. **Mémoire persistante avancée :** organiser, retrouver et faire évoluer les informations mémorisées pour chaque profil.
3. **Architecture modulaire et bibliothèque d'outils :** définir un système commun pour répertorier, ajouter, remplacer et utiliser les outils de MARVIN.

### Phase 2 — Capacités opérationnelles

4. **Lecture et analyse de fichiers — niveau A :** lire des documents, comparer des fichiers Excel et analyser des présentations PowerPoint, y compris les formats courants OpenDocument (`.ods`, `.odp`, `.odt`). Aucune modification de fichier à cette étape.
5. **Recherche de solutions et de dépendances :** rechercher des outils compatibles, vérifier leur provenance, leurs licences et leurs risques, puis demander les autorisations nécessaires. Si aucune solution n'est disponible, expliquer le blocage et proposer des alternatives.
6. **Assistance documentaire — niveau B :** détecter des erreurs et proposer des corrections ou des modifications en expliquant les changements envisagés.
7. **Outils pratiques et raisonnement :** calculs, conversions, comparaisons, analyse de données et enchaînement de plusieurs opérations.
8. **Modification et création de fichiers — niveau C :** appliquer les modifications validées, créer des documents, préserver les originaux par défaut et vérifier les résultats autant que possible.

### Phase 3 — Intelligence

9. **IA locale :** intégrer un modèle de langage exécuté sur la machine, interchangeable et adapté aux ressources disponibles.
10. **Compréhension du langage naturel :** comprendre les demandes ordinaires, identifier les intentions et les paramètres, et demander des précisions lorsque nécessaire.
11. **Orchestration et vérification :** planifier des tâches, sélectionner les outils adaptés, enchaîner les opérations, gérer les erreurs et contrôler les résultats. L'IA planifie ; MARVIN encadre l'exécution.

### Phase 4 — Extension

12. **Interface graphique :** développer une interface de bureau simple, dont le design sera défini ultérieurement.
13. **Compatibilité multiplateforme :** rendre MARVIN utilisable sous Windows, Linux et macOS, en anticipant la portabilité dès les premières étapes.
14. **Recherche Web et comparaisons :** rechercher des informations actuelles, comparer des produits, prix, vendeurs et frais de livraison, et présenter les sources.
15. **Compréhension vocale avancée :** comprendre la parole malgré les accents, le bruit, les hésitations et une diction imparfaite.

## État du projet

**Version affichée actuellement : 0.0.0.2**

MARVIN est en cours de développement. Les commandes de base, la mémoire persistante et la modification du prénom sont opérationnelles. La structure de mémoire évolue vers le multi-profils, dont la gestion complète reste à développer.

Chaque évolution doit être testée afin de préserver les fonctionnalités déjà opérationnelles.
