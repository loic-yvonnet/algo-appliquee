# Bibliothèque standard
from dataclasses import dataclass, field
from typing import Any, List

# Bibliothèques externes
import pygraphviz as pgv

def predecesseurs(m, s):
    """Renvoie les prédécesseurs du sommet s de la matrice d'adjacence m.
    
    Les prédécesseurs se lisent sur la colonne s de m.
    """
    pred = []
    for i in range(len(m)):
        if m[i][s] == 1:
            pred.append(i)

    return pred

def successeurs(m, s):
    """Renvoie les successeurs du sommet s de la matrice d'adjacence m.
    
    Les successeurs se lisent sur la ligne s de m.
    """
    succ = []
    for j in range(len(m[s])):
        if m[s][j] == 1:
            succ.append(j)

    return succ

def parcours_sommets(m, f):
    """La fonction f est appelée sur chaque sommet."""
    for i in range(len(m)):
        f(i)

def parcours_arcs(m, f):
    """La fonction f est appelée avec les couples de sommets formant des arcs."""
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 1:
                f(i, j)

def parcours_en_largeur(m, f):
    """Applique la fonction f à chaque sommet du graphe.
    
    m - matrice d'adjacence.
    f - fonction prenant un sommet en argument.
    """
    marque = [] # On ne souhaite pas traiter plusieurs fois un sommet
    queue = []  # On utilise une queue pour traiter d'abord les plus proches
    for s in range(len(m)): # Visite chaque sommet pour les graphes non-connexes
        if s not in marque: # Evite de traiter 2 fois un sommet
            marque.append(s)    # Marque le sommet courant à traiter
            queue.append(s)     # Empile dans la queue des sommets à traiter
            while len(queue) != 0:              # Tant que la queue est non vide
                s_i = queue.pop(0)              # On prend le 1er sommet
                f(s_i)                          # On traite s_i
                suivants = successeurs(m, s_i)  # On prend les successeurs
                for suivant in suivants:        # On parcourt les successeurs
                    if suivant not in marque:   # Les successeurs non marqués
                        marque.append(suivant)  # sont marqués
                        queue.append(suivant)   # et empilés.

def parcours_en_profondeur(m, f):
    """Applique la fonction f à chaque sommet du graphe.
    
    m - matrice d'adjacence.
    f - fonction prenant un sommet en argument.
    """
    def parcours_successeurs(m, s, f, marque):
        """Traitement récursif."""
        if s not in marque:
            marque.append(s)
            f(s)
            suivants = successeurs(m, s)
            for suivant in suivants:
                parcours_successeurs(m, suivant, f, marque)

    marque = []
    for s in range(len(m)):
        parcours_successeurs(m, s, f, marque)

def affiche_arc(i, j):
    print(f"{i} -> {j}")

def convertir_matrice_adjacence_vers_graphviz(m, G):
    """Convertie une matrice d'adjacence en graphe GraphViz."""
    def ajoute_noeud(s):
        G.add_node(s, shape="circle")

    def ajoute_arete(s, t):
        G.add_edge(s, t)

    parcours_sommets(m, ajoute_noeud)
    parcours_arcs(m, ajoute_arete)

def identifie_cycle_dans_chemin(m, s, marque, chemin):
    """Retourne le 1er cycle trouvé dans le chemin.
    
    m - matrice d'adjacence.
    s - sommet à visiter.
    marque - liste de sommets marqués.
    chemin - chemin jusqu'à s.
    """
    nouveau_chemin = chemin + [s]

    # Si un cycle est identifié dans le chemin, on le renvoie
    if s in chemin:
        return nouveau_chemin

    # Parcours en profondeur
    if s not in marque:
        marque.append(s)
        suivants = successeurs(m, s)
        for suivant in suivants:
            # On vérifie les sous-chemins
            cycle = identifie_cycle_dans_chemin(m, suivant, marque, nouveau_chemin)
            
            # Si un cycle a été identifié dans un sous-chemin, on le renvoie
            if cycle != None:
                return cycle

    # Pas de cycle identifié
    return None

def identifie_cycle(m):
    """Retourne le premier cycle identifié ou None."""
    marque = []
    for s in range(len(m)):
        cycle = identifie_cycle_dans_chemin(m, s, marque, [])
        if cycle != None:
            return cycle

    return None

@dataclass
class Sommet:
    """Sommet d'un graphe."""
    label: int = 0

@dataclass
class Arc:
    """Arc d'un graphe orienté"""
    origine: int = 0
    but: int = 0
    valeur: float = 0.

@dataclass
class GraphePondere:
    """Graphe orienté pondéré."""
    sommets: List = field(default=list)
    arcs: List = field(default=list)

def tests():
    M = [
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    print(predecesseurs(M, 4))
    print("---")
    print(successeurs(M, 1))
    print("---")
    parcours_sommets(M, print)
    print("---")
    parcours_arcs(M, affiche_arc)
    print("---")
    parcours_en_largeur(M, print)
    print("---")
    parcours_en_profondeur(M, print)
    print("---")
    print(identifie_cycle(M))
    print("---")
    G = [
        [ # 0 -> 1 (poids = 42)
            [1, 42]
        ],      
        [ # 1 -> 3 (poids = 21), 1 -> 4 (poids = -56.7)
            [3, 21],
            [4, -56.7]
        ],
        [ # 2 -> 4 (poids = 7)
            [4, 7]
        ],
        [ # 3 -> 0 (poids = 3.14), 3 -> 2 (poids = -8)
            [0, 3.14],
            [2, -8]
        ],
        [] # aucun
    ]
    print(G)
    print("---")
    s0 = Sommet(0)
    s1 = Sommet(1)
    s2 = Sommet(2)
    s3 = Sommet(3)
    s4 = Sommet(4)
    a0 = Arc(origine=0, but=1, valeur=42)
    a1 = Arc(origine=1, but=3, valeur=21)
    a2 = Arc(origine=1, but=4, valeur=-56.7)
    a3 = Arc(origine=2, but=4, valeur=7)
    a4 = Arc(origine=3, but=2, valeur=-8)
    a5 = Arc(origine=3, but=0, valeur=3.14)
    G = GraphePondere(sommets=[s0, s1, s2, s3, s4],
                      arcs=[a0, a1, a2, a3, a4, a5])
    print(G)

if __name__ == "__main__":
    tests()