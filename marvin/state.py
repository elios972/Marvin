import json
import re
import unicodedata
from pathlib import Path


FICHIER_MEMOIRE = Path(__file__).parent / "memory.json"


def creer_profil(nom):
    """Crée la mémoire individuelle d'un utilisateur."""

    return {
        "nom": nom,
        "nombre_commandes": 0,
        "souvenirs": [],
    }


def creer_memoire():
    """Crée une mémoire contenant le profil initial de MARVIN."""

    return {
        "profil_actif": "user",
        "profils": {
            "user": creer_profil("user"),
        },
    }


def normaliser_identifiant(nom):
    """Transforme un nom en identifiant utilisable."""

    texte = unicodedata.normalize("NFKD", nom)

    texte = "".join(
        caractere
        for caractere in texte
        if not unicodedata.combining(caractere)
    )

    texte = texte.casefold()
    texte = re.sub(r"[^a-z0-9]+", "_", texte)

    return texte.strip("_")


def charger_memoire():
    """Charge la mémoire et convertit l'ancien format si nécessaire."""

    if not FICHIER_MEMOIRE.exists():
        return creer_memoire()

    try:
        with FICHIER_MEMOIRE.open("r", encoding="utf-8") as fichier:
            donnees = json.load(fichier)

    except (json.JSONDecodeError, OSError):
        return creer_memoire()

    if not isinstance(donnees, dict):
        return creer_memoire()

    if "profils" in donnees and "profil_actif" in donnees:
        return donnees

    nom = donnees.get("nom") or "User"
    identifiant = "user"

    profil = creer_profil(nom)
    profil["nombre_commandes"] = donnees.get(
        "nombre_commandes", 0
    )

    return {
        "profil_actif": identifiant,
        "profils": {
            identifiant: profil,
        },
    }


def sauvegarder_memoire(memoire):
    """Enregistre la mémoire de MARVIN dans un fichier JSON."""

    with FICHIER_MEMOIRE.open("w", encoding="utf-8") as fichier:
        json.dump(
            memoire,
            fichier,
            ensure_ascii=False,
            indent=4,
        )