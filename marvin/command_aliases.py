import re
import unicodedata



ALIASES = {
    "bonjour": ["bonjour", "salut", "hello", "coucou", "yo"],
    "heure": ["heure", "quelle heure", "donne-moi l'heure"],
    "aide": ["aide", "aide-moi", "commandes", "que sais-tu faire"],
    "compteur": ["combien de commandes", "t'en es a ou", "nombre de commandes", "cbn de commandes"],
    "quitter": ["quitter", "bye", "ciao", "a +"],
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

    texte = normaliser_texte(texte)

    for nom_commande, alias in ALIASES.items():
        alias_normalises = [
            normaliser_texte(variante)
            for variante in alias
        ]

        if texte in alias_normalises:
            return nom_commande

    return None