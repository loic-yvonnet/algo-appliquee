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


M = [
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

parcours_en_largeur(M, print)