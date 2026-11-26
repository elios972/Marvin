import json
from pathlib import Path


FICHIER_MEMOIRE = Path(__file__).parent / "memory.json"


def charger_memoire():
    """Charge la mémoire de MARVIN ou crée des valeurs par défaut."""

    if not FICHIER_MEMOIRE.exists():
        return {
            "nom": "",
            "nombre_commandes": 0,
        }

    try:
        with FICHIER_MEMOIRE.open("r", encoding="utf-8") as fichier:
            return json.load(fichier)

    except (json.JSONDecodeError, OSError):
        return {
            "nom": "",
            "nombre_commandes": 0,
        }


def sauvegarder_memoire(memoire):
    """Enregistre la mémoire de MARVIN dans un fichier JSON."""

    with FICHIER_MEMOIRE.open("w", encoding="utf-8") as fichier:
        json.dump(memoire, fichier, ensure_ascii=False, indent=4)