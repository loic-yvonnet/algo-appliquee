# Bibliothèque standard
from dataclasses import dataclass
from typing import Any

# Bibliothèque externe
import pygraphviz as pgv

ROUGE = True
NOIR = False

@dataclass
class Noeud:
    """Noeud d'un arbre rouge-noir."""
    valeur: Any = None
    gauche: Any = None
    droite: Any = None
    couleur: bool = NOIR

@dataclass
class ArbreRougeNoir:
    """Arbre rouge-noir (Red-Black Binary Search Tree)."""
    noeud: Noeud = None

def est_rouge(x):
    """Dit si le noeud x est rouge."""
    if x == None:
        return False

    return x.couleur == ROUGE

def rotation_gauche(noeud):
    """Le noeud à droite passe au-dessus."""
    droite = noeud.droite
    noeud.droite = droite.gauche
    droite.gauche = noeud
    droite.couleur = noeud.couleur
    noeud.couleur = ROUGE

    return droite

def rotation_droite(noeud):
    """Le noeud à gauche passe au-dessus."""
    gauche = noeud.gauche
    noeud.gauche = gauche.droite
    gauche.droite = noeud
    gauche.couleur = noeud.couleur
    noeud.couleur = ROUGE

    return gauche

def inverse_couleurs(noeud):
    """Inverse les couleurs pour converser un équilibre-noir parfait."""
    noeud.couleur = ROUGE
    noeud.gauche.couleur = NOIR
    noeud.droite.couleur = NOIR

def insere_recursif(noeud, valeur):
    """Rééquilibre l'arbre récursivement en insérant une nouvelle valeur."""
    # Fin de la récursion
    if noeud == None:
        return Noeud(valeur=valeur, couleur=ROUGE)

    # Recherche récursivement en rééquilibrant
    if valeur < noeud.valeur:
        noeud.gauche = insere_recursif(noeud.gauche, valeur)
    elif valeur > noeud.valeur:
        noeud.droite = insere_recursif(noeud.droite, valeur)

    # Rééquilibrage
    if est_rouge(noeud.droite) and (not est_rouge(noeud.gauche)):
        noeud = rotation_gauche(noeud)
    if est_rouge(noeud.gauche) and est_rouge(noeud.gauche.gauche):
        noeud = rotation_droite(noeud)
    if est_rouge(noeud.gauche) and est_rouge(noeud.droite):
        inverse_couleurs(noeud)

    return noeud

def insere_noeud_dans_arbre_rouge_noir(arbre, valeur):
    """Insère un nouveau noeud dans un arbre rouge-noir."""
    arbre.noeud = insere_recursif(arbre.noeud, valeur)
    arbre.noeud.couleur = NOIR

def creer_arbre_rouge_noir_avec_liste(liste):
    """Convertie une liste en arbre rouge-noir."""
    arbre = ArbreRougeNoir()
    for element in liste:
        insere_noeud_dans_arbre_rouge_noir(arbre, element)

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

def trouve_valeur_dans_arbre_rouge_noir(arbre, valeur):
    """Trouve une valeur dans l'arbre rouge-noir."""
    noeud = arbre.noeud
    while noeud != None and noeud.valeur != valeur:
        if valeur < noeud.valeur:
            noeud = noeud.gauche
        else:
            noeud = noeud.droite

    return noeud

def tests():
    """Fonction de tests."""
    arbre = creer_arbre_rouge_noir_avec_liste([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    noeud = trouve_valeur_dans_arbre_rouge_noir(arbre, 7)
    print(noeud.valeur)
    print("---")
    noeud = trouve_valeur_dans_arbre_rouge_noir(arbre, -1)
    if noeud != None:
        raise ValueError("-1")
    print("-1")
    print("---")
    parcourt_arbre(arbre, print)
    print("---")
    parcourt_arbre_avec_parent(arbre, affiche_arrete)

if __name__ == "__main__":
    tests()