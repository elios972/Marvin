from marvin.commands import execute_command


def run():
    print("=" * 32)
    print("Bienvenue dans MARVIN")
    print("Version : 0.0.0.2")
    print("=" * 32)

    nom = input("Comment tu t'appelles ? ").strip()

    if nom == "":
        nom = "Flo"

    print(f"Enchanté, {nom} !")
    print("Je suis prêt à t'aider.")
    print("Tape 'aide' pour voir les commandes disponibles.")
    nombre_commandes = 0

    while True:
        commande = input("MARVIN > ").strip().lower()
    
        if execute_command(commande, nom, nombre_commandes):
            nombre_commandes += 1

        if commande in ["quitter", "bye", "ciao", "a +"]:
            print(f"À bientôt {nom} !")
            break