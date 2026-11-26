
from marvin.commands import execute_command
from marvin.state import charger_memoire, sauvegarder_memoire


def run():
    print("=" * 32)
    print("Bienvenue dans MARVIN")
    print("Version : 0.0.0.2")
    print("=" * 32)

    memoire = charger_memoire()
    nom = memoire.get("nom", "")

    if nom == "":
        nom = input("Comment tu t'appelles ? ").strip()

        if nom == "":
            nom = "User"

        memoire["nom"] = nom
        sauvegarder_memoire(memoire)
        print(f"Enchanté, {nom} !")
        
    else:
        print(f"Content de te revoir, {nom} !")

    print("Je suis prêt à t'aider.")
    print("Tape 'aide' pour voir les commandes disponibles.")

    nombre_commandes = memoire.get("nombre_commandes", 0)

    while True:
        commande = input("MARVIN > ").strip().lower().rstrip("!?.,;:").strip()

        resultat = execute_command(
            commande, nom, nombre_commandes
        )

        if resultat == "quitter":
            break

        if resultat is True:
            nombre_commandes += 1
            memoire["nombre_commandes"] = nombre_commandes
            sauvegarder_memoire(memoire)
