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
            if m[i][j] != 0:
                f(i, j)

def parcours_arcs_ponderes(m, f):
    """La fonction f est appelée avec les couples de sommets formant des arcs,
    ainsi que le poids associé."""
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] != None:
                f(i, j, m[i][j])

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
    poids: float = 0.

@dataclass
class GraphePondere:
    """Graphe orienté pondéré."""
    sommets: List = field(default=list)
    arcs: List = field(default=list)

def adjacents(m, s):
    """Renvoie les arcs adjacents à s dans m."""
    adj = []
    for j in range(len(m[s])):
        if m[s][j] != None:
            adj.append(Arc(origine=s, but=j, poids=m[s][j]))

    return adj

def recalcule_bellman_ford(m, s, dist_a, arc_vers, queue):
    """Recalcule la distance minimale en considérant les successeurs de s.
    
    m - matrice d'adjacence pondérée.
    s - sommet dans les successeurs sont considérés.
    dist_a - liste des distances minimales aux autres sommets.
    arc_vers - liste des arcs conservés pour aller à un sommet donné.
    queue - queue pour le parcours en largeur.
    """
    adj = adjacents(m, s)
    for arc in adj:
        w = arc.but
        if dist_a[w] == None or dist_a[w] > dist_a[s] + arc.poids:
            dist_a[w] = dist_a[s] + arc.poids
            arc_vers[w] = arc
            if w not in queue:
                queue.append(w)

def bellman_ford_impl(m, s):
    """Implémentation de Bellman-Ford sans gestion de cycles négatifs.
    
    m - matrice d'adjacence pondérée.
    s - sommet de départ.
    Renvoie la liste des distances aux autres sommets et la liste des
    arcs constituant les plus courts chemins.
    """
    dist_a = [None for _ in range(len(m))]   # distances à l'infini
    dist_a[s] = 0                            # distance à lui-même
    arc_vers = [None for _ in range(len(m))] # résultat
    queue = [s]
    while len(queue) != 0:
        v = queue.pop(0)
        recalcule_bellman_ford(m, v, dist_a, arc_vers, queue)

    return dist_a, arc_vers

def bellman_ford(m, s):
    """Renvoie une matrice d'adjacence correspondant au shortest path
    tree (SPT) et la liste des distances minimales."""
    dist_a, arc_vers = bellman_ford_impl(m, s)
    spt = [[None for _ in range(len(m))] for _ in range(len(m))]
    for arc in arc_vers:
        if arc != None:
            spt[arc.origine][arc.but] = arc.poids

    return spt, dist_a

def affiche_sommet(i):
    """Aide pour les tests."""
    print(f"s{i} [label=\"{i}\", shape=\"circle\"];")

def affiche_arc_pondere(i, j, poids):
    """Aide pour les tests."""
    print(f"s{i} -> s{j} [label=\"{poids}\"];")

def oppose_poids(m):
    """Renvoie une matrice d'adjacence dont les poids sont opposés."""
    resultat = []

    for i in range(len(m)):
        ligne = []
        for j in range(len(m)):
            if m[i][j] == None:
                ligne.append(None)
            else:
                ligne.append(-m[i][j])
        resultat.append(ligne)

    return resultat

def chemin_vers(s, dist_a, arc_vers):
    """Renvoie le chemin vers le sommet s."""
    if dist_a[s] == None:
        return None

    chemin = []
    arc = arc_vers[s]
    while arc != None:
        predecesseur = arc.origine
        chemin.insert(0, predecesseur)
        arc = arc_vers[predecesseur]

    return chemin

def chemin_critique(m):
    """Renvoie le chemin critique en utilisant PERT.
    
    Utilise Bellman-Ford sur l'opposé de la matrice d'adjacence.
    La matrice d'adjacence doit représenter un DAG.
    Par convention, le début est supposé être le 1er sommer, et
    la fin est supoosée être le dernier sommet.
    """
    # Construit une matrice d'adjacence avec les poids opposés
    m_p = oppose_poids(m)

    # Calcule l'arbre des plus courts chemins
    dist_a, arc_vers = bellman_ford_impl(m_p, 0)

    # Le chemin vers la fin est le chemin critique
    fin = len(m) - 1
    chemin = chemin_vers(fin, dist_a, arc_vers)

    return chemin

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
    a0 = Arc(origine=0, but=1, poids=42)
    a1 = Arc(origine=1, but=3, poids=21)
    a2 = Arc(origine=1, but=4, poids=-56.7)
    a3 = Arc(origine=2, but=4, poids=7)
    a4 = Arc(origine=3, but=2, poids=-8)
    a5 = Arc(origine=3, but=0, poids=3.14)
    G = GraphePondere(sommets=[s0, s1, s2, s3, s4],
                      arcs=[a0, a1, a2, a3, a4, a5])
    print(G)
    print("---")
    M = [
        [None,   42, None, None,  None],
        [None, None, None,   21, -56.7],
        [None, None, None, None,   7  ],
        [3.14, None,   -8, None,  None],
        [None, None, None, None,  None]
    ]
    parcours_sommets(M, affiche_sommet)
    parcours_arcs_ponderes(M, affiche_arc_pondere)
    print("---")
    spt, dist = bellman_ford(M, 0)
    parcours_sommets(spt, affiche_sommet)
    parcours_arcs_ponderes(spt, affiche_arc_pondere)
    print(dist)
    print("---")
    M = [[None for _ in range(15)] for _ in range(15)]
    M[0][3] = 4; M[0][4] = 2
    M[1][0] = 1; M[1][5] = 2; M[1][6] = 15
    M[2][0] = 1; M[2][7] = 3
    M[3][2] = 5; M[3][8] = 9; M[3][9] = 8
    M[4][1] = 2; M[4][5] = 9; M[4][10] = 1; M[4][11] = 3
    M[5][11] = 1
    M[7][12] = 2; M[7][13] = 1; M[7][14] = 9
    M[8][7] = 1; M[8][9] = 3
    M[10][0] = 2
    M[11][6] = 3
    M[12][11] = 1
    M[13][14] = 1
    M[14][9] = 1
    parcours_sommets(M, affiche_sommet)
    parcours_arcs_ponderes(M, affiche_arc_pondere)
    print("---")
    spt, dist = bellman_ford(M, 0)
    parcours_sommets(spt, affiche_sommet)
    parcours_arcs_ponderes(spt, affiche_arc_pondere)
    print(dist)
    print("---")
    NA = None # Non Applicable
    M = [
        # 0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15
        [NA,  0,  0,  0, NA, NA, NA, NA, NA, NA, NA,  0, NA, NA, NA, NA], #  0
        [NA, NA, NA, NA,  2, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA], #  1
        [NA, NA, NA, NA, NA,  1, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA], #  2
        [NA, NA, NA, NA, NA, NA,  3, NA, NA, NA, NA, NA, NA, NA, NA, NA], #  3
        [NA, NA, NA, NA, NA, NA, NA,  0,  0, NA, NA, NA, NA, NA, NA, NA], #  4
        [NA, NA, NA, NA, NA, NA, NA, NA,  0, NA, NA, NA, NA, NA, NA, NA], #  5
        [NA, NA, NA, NA, NA, NA, NA, NA,  0, NA, NA, NA, NA, NA, NA, NA], #  6
        [NA, NA, NA, NA, NA, NA, NA, NA, NA,  5, NA, NA, NA, NA, NA, NA], #  7
        [NA, NA, NA, NA, NA, NA, NA, NA, NA, NA,  7, NA, NA, NA, NA, NA], #  8
        [NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA,  0, NA, NA], #  9
        [NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA,  0, NA, NA], # 10
        [NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA,  2, NA, NA, NA], # 11
        [NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA,  0, NA, NA], # 12
        [NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA,  3, NA], # 13
        [NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA,  0], # 14
        [NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA]  # 15
        # 0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15
    ]
    c = chemin_critique(M)
    print(c)

if __name__ == "__main__":
    tests()