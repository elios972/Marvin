# MARVIN

**MARVIN** est un assistant personnel développé en Python, conçu pour évoluer progressivement vers un assistant intelligent capable d'interagir avec son utilisateur et d'exécuter différentes tâches.

Le projet est développé étape par étape afin de construire une base solide, modulaire et facile à faire évoluer.

## Fonctionnalités actuelles

- Dialogue en ligne de commande.
- Personnalisation du dialogue avec le prénom de l'utilisateur.
- Reconnaissance de commandes textuelles.
- Salutations personnalisées.
- Affichage de l'heure actuelle.
- Aide listant les commandes disponibles.
- Comptage des commandes reconnues.
- Fermeture de l'assistant avec une commande de sortie.

## Technologies utilisées

- **Python 3.14**
- Modules natifs de Python : `datetime`

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
| `bonjour`, `salut`, `hello`, `coucou`, `yo` | Saluer MARVIN |
| `heure` | Afficher l'heure actuelle |
| `aide` | Afficher les commandes disponibles |
| `combien de commandes` | Afficher le nombre de commandes reconnues précédemment |
| `quitter`, `bye`, `ciao`, `a +` | Fermer MARVIN |

## Structure du projet

```text
MARVIN/
├── main.py
├── README.md
├── .gitignore
└── marvin/
    ├── __init__.py
    ├── assistant.py
    └── commands.py
```

## État du projet

**Version actuelle : 0.0.0.2**

Le projet est en cours de développement. L'objectif est d'améliorer progressivement son architecture, ses capacités de compréhension et le nombre de tâches qu'il peut effectuer.

## Objectifs futurs

- Améliorer la compréhension des commandes.
- Ajouter de nouvelles fonctionnalités.
- Développer une mémoire pour conserver des informations utiles.
- Explorer l'intégration de capacités d'intelligence artificielle.
