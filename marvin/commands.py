
from datetime import datetime
from marvin.command_aliases import trouver_commande


def execute_command(commande, nom, nombre_commandes):
    """Exécute une commande reconnue par MARVIN."""

    nom_commande = trouver_commande(commande)

    if nom_commande == "quitter":
        print(f"À bientôt {nom} !")
        return "quitter"

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
