def racine_carree(x, epsilon=0.000001):
    """Renvoie la racine carrée de x à epsilon près.

    Calcule la racine carrée d'un nombre x positif en employant
    l'algorithme de Newtown-Raphson.
    x - nombre flottant positif ou nul.
    epsilon - nombre flottant strictement positif.
    Retourne une valeur proche de la racine carrée de x, à plus
    ou moins epsilon près.
    """
    s = x / 2
    while abs(s ** 2 - x) >= epsilon:
        P = s ** 2 - x
        P_prime = 2 * s
        s = s - P / P_prime

    return s

def racine_cubique(x, epsilon=0.000001):
    """Renvoie la racine cubique de x à epsilon près.
    
    Calcule la racine cubique d'un nombre x en employant
    l'algorithme de Newtown-Raphson.
    x - nombre flottant.
    epsilon - nombre flottant strictement positif.
    Retourne une valeur proche de la racine cubique de x,
    à plus ou moins epsilon près.
    """
    positif = True
    if x < 0:
        positif = False
        x = -x
    s = x / 2
    while abs(s ** 3 - x) >= epsilon:
        P = s ** 3 - x
        P_prime = 3 * s ** 2
        s = s - P / P_prime
    if not positif:
        s = -s

    return s