from dataclasses import dataclass, field
from typing import Any, List

@dataclass
class Noeud:
    """Noeud d'un arbre n-aire."""
    valeur: Any = None
    descendants: List = field(default_factory=list)

roue_arriere_gauche = Noeud(valeur="roue gauche")
roue_arriere_droite = Noeud(valeur="roue droite")

roue_avant_gauche = Noeud(valeur="roue gauche")
roue_avant_droite = Noeud(valeur="roue droite")

planche = Noeud(valeur="planche")

essieu_arriere = Noeud(valeur="essieu arrière", descendants=[
    roue_arriere_gauche,
    roue_arriere_droite
])

essieu_avant = Noeud(valeur="essieu avant", descendants=[
    roue_avant_gauche,
    roue_avant_droite
])

skateboard = Noeud(valeur="skateboard", descendants=[
    planche,
    essieu_arriere,
    essieu_avant
])