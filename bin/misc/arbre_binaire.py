# Bibliothèque standard
from dataclasses import dataclass

# Bibliothèque externe
import pygraphviz as pgv

@dataclass
class Noeud:
    """Noeud d'un arbre binaire."""
    valeur = None
    gauche = None
    droite = None

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
        G.add_edge()

    parcourt_arbre(arbre, ajoute_noeud)