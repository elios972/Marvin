
from marvin.commands import execute_command
from marvin.state import charger_memoire, sauvegarder_memoire


def run():
    print("=" * 32)
    print("Bienvenue dans MARVIN")
    print("Version : 0.0.0.2")
    print("=" * 32)

    memoire = charger_memoire()

    # Sauvegarde le nouveau format de mémoire.
    sauvegarder_memoire(memoire)

    profil_actif = memoire["profil_actif"]
    profil = memoire["profils"][profil_actif]

    nom = profil.get("nom", "User")

    if nom == "User":
        nouveau_nom = input(
            "Comment tu veux que MARVIN t'appelle ? "
        ).strip()

        if nouveau_nom != "":
            nom = nouveau_nom
            profil["nom"] = nom
            sauvegarder_memoire(memoire)

        print(f"Enchanté, {nom} !")

    else:
        print(f"Content de te revoir, {nom} !")

    print("Je suis prêt à t'aider.")
    print("Tape 'aide' pour voir les commandes disponibles.")

    nombre_commandes = profil.get("nombre_commandes", 0)

    while True:
        texte_brut = input("MARVIN > ").strip()

        commande = (
            texte_brut
            .lower()
            .rstrip("!?.,;:")
            .strip()
        )

        resultat = execute_command(
            commande, nom, nombre_commandes, profil, memoire, texte_brut
        )
        nom = profil.get("nom", nom)

        if resultat == "quitter":
            break

        if resultat is True:
            nombre_commandes += 1
            profil["nombre_commandes"] = nombre_commandes
            sauvegarder_memoire(memoire)