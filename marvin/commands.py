
from datetime import datetime
from marvin.command_aliases import trouver_commande, extraire_argument
from marvin.state import sauvegarder_memoire


def execute_command(commande, nom, nombre_commandes, profil=None, memoire=None, texte_brut=None):
    """Exécute une commande reconnue par MARVIN."""

    nom_commande = trouver_commande(commande)

    if nom_commande == "quitter":
        print(f"À bientôt {nom} !")
        return "quitter"

    elif nom_commande == "renommer":
        nouveau_nom = extraire_argument(texte_brut, "renommer")

        if not nouveau_nom:
            print("Utilisation : appelle-moi suivi de ton nom.")
            return False

        if profil is None or memoire is None:
            print("Il n'y a pas de profil actif.")
            return False

        profil["nom"] = nouveau_nom
        sauvegarder_memoire(memoire)

        print(f"D'accord, je t'appellerai {nouveau_nom} désormais.")

    elif nom_commande == "bonjour":
        print(f"Bonjour {nom} !")

    elif nom_commande == "heure":
        heure_actuelle = datetime.now().strftime("%H:%M:%S")
        print(f"Il est actuellement {heure_actuelle}.")

    elif nom_commande == "aide":
        print(
            "Commandes disponibles : bonjour, heure, aide, "
            "combien de commandes, quitter"
        )

    elif nom_commande == "compteur":
        print(
            f"Sans cette commande, j'en suis à la numéro "
            f"{nombre_commandes}."
        )

    else:
        print("Je ne connais pas cette commande. Tape 'aide'.")
        return False

    return True
