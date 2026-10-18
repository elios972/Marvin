
from datetime import datetime


def execute_command(commande, nom, nombre_commandes):
    """Exécute une commande reconnue par MARVIN."""

    if commande in ["bonjour", "salut", "hello", "coucou", "yo"]:
        print(f"Bonjour {nom} !")

    elif commande == "heure":
        heure_actuelle = datetime.now().strftime("%H:%M:%S")
        print(f"Il est actuellement {heure_actuelle}.")

    elif commande == "aide":
        print("Commandes disponibles : bonjour, aide, heure, quitter, combien de commandes")
    
    elif commande == "combien de commandes":
        print(f"Sans cette commande j'en suis à la numéro {nombre_commandes}.")

    else:
        print("Je ne connais pas cette commande. Tape 'aide'.")
        return False
    return True
