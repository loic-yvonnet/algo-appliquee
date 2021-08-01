"""Simple calculatrice avec PySimpleGUIQt

Cette calculatrice est utilisée pour le TP concernant la gestion des erreurs.
"""

# On indique ici que l'on utilise PySimpleGUIQt.
# Nous reviendrons dans un prochain cours sur l'utilisation de bibliothèques,
# les modules Pythons et les gestionnaires de paquets.
import PySimpleGUIQt as sg

def affiche_erreur(texte):
    """Affiche le texte d'erreur en entrée dans un popup"""

    sg.popup_ok(texte)

#--------------------------------------------------------------------------------------------------------
#                      GESTION DES FONCTIONS MATHEMATIQUES
#
# Votre travail consiste à implémenter et documenter les fonction suivantes.
#--------------------------------------------------------------------------------------------------------

def somme(valeur0, valeur1):
    pass

def soustraction(valeur0, valeur1):
    pass

def multiplication(valeur0, valeur1):
    pass

def division(valeur0, valeur1):
    pass

def racine_carree(valeur1):
    pass

def puissance(valeur0, valeur1):
    pass

def pourcent(valeur1):
    pass

def cosinus(valeur1):
    pass

def sinus(valeur1):
    pass

def gere_operation_unaire(op, valeur1):
    """Redirige vers pourcent, racine_carre, cosinus ou sinus."""
    pass

def gere_operation_binaire(op, valeur0, valeur1):
    """Gère les opérations mathématiques avec 2 arguments"""
    pass

#--------------------------------------------------------------------------------------------------------
#                      GESTION DE L'INTERFACE UTILISATEUR
#
# Vous n'avez pas besoin de modifier le code ci-dessous pour terminer le TP.
# A moins que vous ne maîtrisiez déjà les interfaces utilisateurs, il est
# déconseillé de modifier le code ci-dessous.
#--------------------------------------------------------------------------------------------------------

def ajoute_a_la_valeur(ajout, valeur1):
    """Ajoute la valeur ajout a valeur1."""

    if valeur1 == "0":
        valeur1 = ajout
    else:
        valeur1 += ajout

    return valeur1

def supprime_dernier_caractere(valeur1):
    """Supprime le dernier caractère dans la valeur1."""

    if len(valeur1) > 1:
        return valeur1[:len(valeur1) - 1]
    else:
        return "0"

def ajoute_virgule(valeur1):
    """Ajoute une virgule, s'il n'y en a pas déjà."""

    if valeur1.find(".") == -1:
        return valeur1 + "."
    else:
        return valeur1

def enregistre_operation(op, valeur1):
    """Mémorise l'opération en vu d'un futur clic sur le bouton '='."""
    return valeur1, "0", op

def reinitialise():
    """Réinitialise l'ancienne valeur0, la valeur1 courante, et l'opération."""
    return "", "0", ""

def gere_evenement(evenement, valeur0, valeur1, op, resultat):
    """Gestionnaire principal d'évéments."""

    if evenement in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}:
        valeur1 = ajoute_a_la_valeur(evenement, valeur1)
    elif evenement == ".":
        valeur1 = ajoute_virgule(valeur1)
    elif evenement == "«":
        valeur1 = supprime_dernier_caractere(valeur1)
    elif evenement == "C":
        valeur0, valeur1, op = reinitialise()
    elif evenement in {"+", "-", "*", "/", "^"}:
        valeur0, valeur1, op = enregistre_operation(evenement, valeur1)
    elif evenement in {"%", "cos", "sin", "√"}:
        valeur1 = gere_operation_unaire(evenement, valeur1)
    elif evenement == "=":
        valeur1 = gere_operation_binaire(op, valeur0, valeur1)
    
    resultat.Update(valeur1)

    return valeur0, valeur1, op

def gui():
    """Gestion de l'interface utilisateur graphique.
    
    GUI = Graphical User Interface.
    """

    # Disposition des elements de l'interface utilisateur : texte et boutons.
    # Il s'agit d'une simple liste de listes. Les listes internes correspondent à
    # des lignes de l'interface utilisateur.
    disposition = [
        [sg.Input("0", key="resultat", justification="right")],
        [sg.Button("7"), sg.Button("8"), sg.Button("9"), sg.Button("/"), sg.Button("«"), sg.Button("C")],
        [sg.Button("4"), sg.Button("5"), sg.Button("6"), sg.Button("*"), sg.Button("^"), sg.Button("√")],
        [sg.Button("1"), sg.Button("2"), sg.Button("3"), sg.Button("-"), sg.Button("cos"), sg.Button("sin")],
        [sg.Button("0"), sg.Button("."), sg.Button("%"), sg.Button("+"), sg.Button("="),],
    ]

    # Création de la fenêtre en spécifiant la disposition à utiliser
    fenetre = sg.FlexForm("Calculatrice",
                          default_button_element_size = (5, 1),
                          auto_size_buttons = False)
    fenetre.Layout(disposition)

    # Représente l'opération à effectuer
    op = ""

    # Représente la valeur précédente
    valeur0 = ""

    # Représente la valeur actuelle
    valeur1 = "0"

    # Représente le widget qui permet d'afficher la valeur actuelle et le résultat
    resultat = fenetre.FindElement('resultat')

    # Gestion de la boucle des événements
    while True:
        # Lecture du dernier événement
        evenement, _ = fenetre.read()
        if evenement == sg.WIN_CLOSED:
            break

        valeur0, valeur1, op = gere_evenement(evenement, valeur0, valeur1, op, resultat)

    # Lorsque la boucle de gestion des événements est terminée, cela signifie
    # que l'utilisateur a cliqué sur le bouton de fermeture de l'application.
    # On pourrait avoir à effectuer des opérations supplémentaires dans notre
    # application : par exemple, proposer à l'utilisateur de sauvegarder un 
    # travail inachevé. Nous devons donc fermer la fenêtre explicitement quand
    # on est prêt, ce qui est le cas ici.
    fenetre.close()

if __name__ == "__main__":
    gui()