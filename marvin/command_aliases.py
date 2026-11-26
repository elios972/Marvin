import re
import unicodedata



ALIASES = {
    "bonjour": ["bonjour", "salut", "hello", "coucou", "yo"],
    "heure": ["heure", "quelle heure", "donne-moi l'heure"],
    "aide": ["aide", "aide-moi", "commandes", "que sais-tu faire"],
    "compteur": ["combien de commandes", "t'en es a ou", "nombre de commandes", "cbn de commandes"],
    "quitter": ["quitter", "bye", "ciao", "a +"],
    "renommer": ["appelle-moi", "appelle moi", "change mon nom", "renomme-moi", "renomme moi"],
}


def normaliser_texte(texte):
    """Uniformise un texte pour faciliter sa comparaison."""

    texte = texte.replace("’", "'").replace("‘", "'")
    texte = unicodedata.normalize("NFD", texte)

    texte = "".join(
        caractere
        for caractere in texte
        if unicodedata.category(caractere) != "Mn"
    )

    texte = texte.casefold()
    texte = re.sub(r"\s+", " ", texte)

    return texte.strip()



def trouver_commande(texte):
    """Retourne le nom de référence correspondant à un alias."""

    texte_normalise = normaliser_texte(texte)

    for nom_commande, alias in ALIASES.items():
        alias_normalises = [
            normaliser_texte(variante)
            for variante in alias
        ]

        if texte_normalise in alias_normalises:
            return nom_commande

        if nom_commande == "renommer":
            for variante in alias_normalises:
                if texte_normalise.startswith(variante + " "):
                    return nom_commande

    return None


def extraire_argument(texte, nom_commande):
    """Extrait l'argument original associé à une commande."""

    for variante in ALIASES.get(nom_commande, []):
        longueur = len(variante)

        if normaliser_texte(texte[:longueur]) == normaliser_texte(variante):
            if len(texte) > longueur and texte[longueur].isspace():
                return texte[longueur:].strip()

    return None