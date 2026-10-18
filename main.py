from datetime import datetime
APP_NAME = "MARVIN"
VERSION = "0.0.0.2"


def main():
    print("=" * 32)
    print(f"Bienvenue dans {APP_NAME}")
    print(f"Version : {VERSION}")
    print("=" * 32)

    nom = input("Comment tu t'appelles ? ").strip()

    if nom == "":
        nom = "utilisateur"

    print(f"Enchanté, {nom} !")
    print("Je suis prêt à t'aider.")
    print("Tape 'aide' pour voir les commandes disponibles.")

    while True:
        commande = input("MARVIN > ").strip().lower()

        if commande == "bonjour":
            print(f"Bonjour {nom} !")

        elif commande == "aide":
            print("Commandes disponibles : bonjour, aide, quitter, heure")

        elif commande == "quitter":
            print(f"À bientôt {nom} !")
            break
        
        elif commande == "heure":
            heure_actuelle = datetime.now().strftime("%H:%M:%S")
            print(f"Il est actuellement {heure_actuelle}.")
            
        else:
            print("Je ne connais pas cette commande. Tape 'aide'.")


if __name__ == "__main__":
    main()