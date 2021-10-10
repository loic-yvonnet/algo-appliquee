---
marp: true
title: "Algorithmique Appliquée - Graphes"
description: "Cours d'Algorithmique Appliquée avec Python"
author: "Loïc Yvonnet"
keywords: "Algorithmique, Algorithme, Python, Introduction, Débutant"
lang: "fr"
url: "https://loic-yvonnet.github.io/algo-appliquee/11-graphes/"
image: "{{ url }}/titre.jpeg"
theme: uncover
paginate: true
_paginate: false
style: |
  section {
    background-image: url("https://raw.githubusercontent.com/loic-yvonnet/algo-appliquee/master/assets/bg_normal.jpg");
  }

  section.title-section {
    background-image: url("https://raw.githubusercontent.com/loic-yvonnet/algo-appliquee/master/assets/bg_title.jpg");
    color: #fff;
  }

  section.smaller-text p, section.smaller-text pre, section.smaller-text ul, section.smaller-text table {
    font-size: 0.6em;
  }
---

<!-- _class: title-section -->

# <!--fit--> Algorithmique Appliquée

##### BTS SIO SISR

### Introduction à la théorie des graphes

<!--
Cours très important pour l'examen final mais également fondamental car il s'agit d'une introduction au domaine passionant de la recherche opérationnelle.
Soyez très attentifs et faites les TPs avec sérieux.
L'examen final contient en général des questions sur les algorithmes de tri, de calcul matriciel et de graphes.
-->

---

<!-- _class: smaller-text -->

# Plan

- Discussion sur les hiérarchies
- Arbre binaire
- Insertion et recherche
- Arbre N-aire
- Discussion concernant les graphes
- Théorie des graphes
- Digraph
- Identification d'un cycle
- Recherche en profondeur
- Recherche en largeur
- Graphe pondéré
- Recherche de chemin critique

---

<!-- _class: title-section -->

# <!--fit--> Correction du travail à la maison

---

### TP : Plus de modules

[**Lien** vers le sujet de DM](../10-python-avance/dm-04.html).

---

<!-- _class: title-section -->

# <!--fit--> Discussion sur les hiérarchies

---

### Hiérarchie en entreprise

![](./assets/001-hierarchie-entreprise.png)

---

### Structure produit

![](./assets/002-structure-produit.png)

---

### Compétition (1/2)

![w:1150](./assets/004-hierarchie-competition-inv.png)

Il est possible d'inverser la représentation pour obtenir une hiérarchie.

---

### Compétition (2/2)

![w:1150](./assets/003-hierarchie-competition.png)

---

<!-- _class: title-section -->

# <!--fit--> Arbre binaire : représentation

---

### Notion d'arbre

* Une **hiérarchie** peut être représentée sous la forme d'un **arbre**.
* Un **arbre binaire** ne comporte que **2 branches**.
* Chaque noeud peut avoir un sous-noeud à gauche et/ou à droite.

---

### Exemple avec 2 noeuds

![](./assets/arbre-binaire-2-noeuds.png)


---

### Exemple avec 3 noeuds

![](./assets/arbre-binaire-3-noeuds.png)

---

### Relation d'ordre

* La valeur du noeud à **gauche** est **plus petite** que celle du parent.
* La valeur du noeud à **droite** est **plus grande** que celle du parent.

---

### Exemple : $7 < 42 < 108$

![](./assets/arbre-binaire-exemple-slt-noeuds.png)

---

# <!--fit--> Structure de données

![bg right:30% 90%](./assets/arbre-binaire-noeud-repr.png)

```python
from dataclasses import dataclass
from typing import Any

@dataclass
class Noeud:
    """Noeud d'un arbre binaire."""
    valeur: Any = None
    gauche: Any = None
    droite: Any = None
```

---

# Noeud de départ

* Comment identifier le **noeud de départ** de l'arbre binaire ?
* On souhaite que chaque noeud ait la **même représentation**.
* On introduit un nouveau type, `ArbreBinaire`, qui référence le noeud de départ.
* Un `ArbreBinaire` **n'a pas de valeur**.

---

#### Noeud de départ identifié par l'`ArbreBinaire`

![](./assets/arbre-binaire-intro.png)

---

# <!--fit--> Structure de données

![bg right:30% 70%](./assets/arbre-binaire-repr.png)

```python
from dataclasses import dataclass

@dataclass
class ArbreBinaire:
    """Arbre binaire."""
    noeud: Noeud = None
```

---

### Exemple complet

![](./assets/arbre-binaire-exemple.png)

---

<!-- _class: title-section -->

# <!--fit--> Insertion et recherche dans un arbre binaire

---

<!-- _class: title-section -->

# <!--fit--> Arbre N-aire : représentation

---

<!-- _class: title-section -->

# TP : Arbres binaires

---

### TP : Arbres binaires

[**Lien** vers le sujet de TP](./tp-18-arbres.html).

---

<!-- _class: title-section -->

# <!--fit--> Discussion concernant les problèmes impliquant des graphes

###### GPS, réseaux sociaux, etc

---

<!-- _class: title-section -->

# <!--fit--> Introduction à la théorie des graphes

##### Sommet, arc, cycle, digraph

---

<!-- _class: title-section -->

# <!--fit--> Digraph : représentation

---

<!-- _class: title-section -->

# <!--fit--> Identification d'un cycle

---

<!-- _class: title-section -->

# <!--fit--> Recherche en profondeur

##### Depth-First Search

---

<!-- _class: title-section -->

# <!--fit--> Recherche en largeur

##### Breadth-First Search

---

<!-- _class: title-section -->

# <!--fit--> Graphe pondéré : représentation

---

<!-- _class: title-section -->

# <!--fit--> Recherche de chemin critique

---

<!-- _class: title-section -->

# TP : Graphes

---

### TP : Graphes

[**Lien** vers le sujet de TP](./tp-19-graphes.html).
