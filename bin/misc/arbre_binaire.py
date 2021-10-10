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
    if noeud == None:
        return 0

    return 1 + max(profondeur(noeud.gauche),
                   profondeur(noeud.droite))

def tests():
    """Fonction de tests."""
    arbre = creer_arbre_binaire_avec_liste([5, 2, 6, 7, 8, 10, 15, 1, 3, 9])
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