# Bibliothèque standard
from dataclasses import dataclass
from typing import Any

# Bibliothèque externe
import pygraphviz as pgv

@dataclass
class Noeud:
    """Noeud d'un arbre binaire."""
    valeur: Any = None
    gauche: Any = None
    droite: Any = None

@dataclass
class ArbreBinaire:
    """Arbre binaire."""
    noeud: Noeud = None

def trouve_valeur_dans_arbre_binaire(arbre, valeur):
    """Trouve une valeur dans l'arbre binaire."""
    noeud = arbre.noeud
    while noeud != None and noeud.valeur != valeur:
        if valeur < noeud.valeur:
            noeud = noeud.gauche
        else:
            noeud = noeud.droite

    return noeud

def insere_noeud_dans_arbre_binaire(arbre, valeur):
    """Insère un nouveau noeud dans un arbre binaire."""
    if arbre.noeud == None:
        arbre.noeud = Noeud(valeur=valeur)
        return arbre.noeud

    noeud = arbre.noeud
    while noeud.valeur != valeur:
        if valeur < noeud.valeur:
            if noeud.gauche == None:
                noeud.gauche = Noeud(valeur=valeur)
            noeud = noeud.gauche
        else:
            if noeud.droite == None:
                noeud.droite = Noeud(valeur=valeur)           
            noeud = noeud.droite

    return noeud

def creer_arbre_binaire_avec_liste(liste):
    """Convertie une liste en arbre binaire."""
    arbre = ArbreBinaire()
    for element in liste:
        insere_noeud_dans_arbre_binaire(arbre, element)

    return arbre

def parcourt_arbre(arbre, f):
    """Appelle f(noeud.valeur) pour chaque noeud de l'arbre."""
    def parcourt_arbre_recursif(noeud, f):
        if noeud != None:
            f(noeud.valeur)
            parcourt_arbre_recursif(noeud.gauche, f)
            parcourt_arbre_recursif(noeud.droite, f)

    parcourt_arbre_recursif(arbre.noeud, f)

def parcourt_arbre_avec_parent(arbre, f):
    """Appelle f(noeud_parent.valeur, noeud.valeur) pour chaque noeud
    de l'arbre à partir de la racine."""
    def parcourt_arbre_recursif(noeud_parent, noeud, f):
        if noeud != None:
            f(noeud_parent.valeur, noeud.valeur)
            parcourt_arbre_recursif(noeud, noeud.gauche, f)
            parcourt_arbre_recursif(noeud, noeud.droite, f)

    if arbre.noeud != None:
        parcourt_arbre_recursif(arbre.noeud, arbre.noeud.gauche, f)
        parcourt_arbre_recursif(arbre.noeud, arbre.noeud.droite, f)

def convertir_arbre_vers_graphviz(arbre, G):
    """Convertie un arbre binaire en graphe GraphViz"""
    def ajoute_noeud(valeur):
        G.add_node(valeur, shape="circle")

    def ajoute_arete(valeur_parent, valeur_enfant):
        G.add_edge(valeur_parent, valeur_enfant)

    parcourt_arbre(arbre, ajoute_noeud)
    parcourt_arbre_avec_parent(arbre, ajoute_arete)

def affiche_arrete(parent, enfant):
    """Aide pour la fonction de tests."""
    print(f"{parent} -> {enfant}")

def profondeur(noeud):
    """Renvoie la profondeur de l'arbre à partir du noeud."""
    if noeud == None:
        return 0

    return 1 + max(profondeur(noeud.gauche),
                   profondeur(noeud.droite))

def nb_descendants(noeud):
    """Renvoie le nombre de descendants à partir du noeud."""
    if noeud == None:
        return 0

    return 1 + nb_descendants(noeud.gauche) + nb_descendants(noeud.droite)

def fusionne_blocs(bloc1, bloc2):
    """Fusionne 2 blocs de texte."""
    resultat = ""
    max1, max2 = 0, 0

    # Fusionne les lignes
    while len(bloc1) > 0 and len(bloc2) > 0:
        i = bloc1.find("\n")
        resultat += bloc1[:i]
        max1 = max(max1, len(bloc1[:i]))
        bloc1 = bloc1[i+1:]
        
        i = bloc2.find("\n")
        resultat += bloc2[:i+1]
        max2 = max(max2, len(bloc2[:i]))
        bloc2 = bloc2[i+1:]

    # Restant à gauche
    while len(bloc1) > 0:
        i = bloc1.find("\n")
        resultat += bloc1[:i]
        resultat += max2 * " " + "\n"
        bloc1 = bloc1[i+1:]

    # Restant à droite
    while len(bloc2) > 0:
        i = bloc2.find("\n")
        resultat += max1 * " "
        resultat += bloc2[:i+1]
        bloc2 = bloc2[i+1:]

    return resultat

def serialise_noeud(noeud):
    """Sérialise récursivement l'arbre à partir du noeud.
    
    A chaque niveau, on créé un bloc de texte rectangulaire.
    On fusionne chaque bloc récursivement.
    """
    # Fin de la récursivité
    if noeud == None:
        return ""

    # Créé une chaîne de caractères pour chaque bloc
    bloc_gauche = serialise_noeud(noeud.gauche)
    bloc_droite = serialise_noeud(noeud.droite)

    # On calcule l'espacement
    i = bloc_gauche.find("\n")
    j = bloc_droite.find("\n")
    nb_espaces_gauche = len(bloc_gauche[:i]) if i > 0 else 0
    nb_espaces_droite = len(bloc_droite[:j]) if j > 0 else 0
    nb_espaces = nb_espaces_gauche + nb_espaces_droite
    nb_espaces = max(4, nb_espaces)

    # On rajoute le début du nouveau bloc
    resultat = str(noeud.valeur).center(nb_espaces) + "\n"
    if nb_espaces_gauche > 0:
        resultat += "/".center(nb_espaces_gauche)
    if nb_espaces_droite > 0:
        resultat += "\\".center(nb_espaces_droite)
    if nb_espaces_gauche > 0 or nb_espaces_droite > 0:
        resultat += "\n"

    # On fusionne les 2 sous-blocs
    resultat += fusionne_blocs(bloc_gauche, bloc_droite)

    return resultat

def affiche_arbre(arbre):
    """Affiche un arbre binaire."""
    chaine = serialise_noeud(arbre.noeud)
    print(chaine)

def tests():
    """Fonction de tests."""
    bloc1 =  "       5        \n"
    bloc1 += "    /     \\     \n"
    bloc1 += "  4         6   \n"
    bloc2 =  "       8        \n"
    bloc2 += "    /     \\     \n"
    bloc2 += "  7         9   \n"
    bloc2 += " /\\        /\\   \n"
    bloc2 += "0  1      2  3  \n"
    print(fusionne_blocs(bloc1, bloc2))
    print(fusionne_blocs(bloc2, bloc1))
    print("---")
    arbre = creer_arbre_binaire_avec_liste([5, 2, 6])
    affiche_arbre(arbre)
    print("---")
    arbre = creer_arbre_binaire_avec_liste([42, 7, 108, 21, 1, 88, 128, 50, 100, 0, 25, 256, 125, 3, 15])
    affiche_arbre(arbre)
    print("---")
    arbre = creer_arbre_binaire_avec_liste([5, 2, 6, 7, 8, 10, 15, 1, 3, 9])
    affiche_arbre(arbre)
    print("---")
    noeud = trouve_valeur_dans_arbre_binaire(arbre, 7)
    print(noeud.valeur)
    print("---")
    noeud = trouve_valeur_dans_arbre_binaire(arbre, -1)
    if noeud != None:
        raise ValueError("-1")
    print("-1")
    print("---")
    parcourt_arbre(arbre, print)
    print("---")
    parcourt_arbre_avec_parent(arbre, affiche_arrete)

if __name__ == "__main__":
    tests()