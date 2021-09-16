---
marp: true
title: "Algorithmique Appliquée - Recherche et tri"
description: "Cours d'Algorithmique Appliquée avec Python"
author: "Loïc Yvonnet"
keywords: "Algorithmique, Algorithme, Python, Introduction, Débutant"
lang: "fr"
url: "https://loic-yvonnet.github.io/algo-appliquee/09-recherche-et-tri/"
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

### Algorithmes de recherche et de tri

---

# Plan

- Algorithmiques classiques
- Recherche en Python
- Recherche linéaire
- Recherche binaire
- Tri en Python
- Algorithmes de tri en $O(N^2)$
- Partition
- Tri Rapide
- Tri Fusion

---

<!-- _class: title-section -->

# <!--fit--> Correction du travail à la maison

---

### DM : Retour sur la complexité et les tests

[**Lien** vers le sujet de DM](../08-tests/dm-04.html).

---

<!-- _class: title-section -->

### Retour sur les classes de problèmes usuelles en algorithmique

---

### Familles d'algorithmes classiques

| Famille d'algorithmes | Exemple de problème              | Exemple d'algorithme |
|-----------------------|----------------------------------|----------------------|
| Recherche             | Trouver un nombre dans une liste | Recherche binaire    |
| Tri                   | Trier une liste                  | Tri Fusion           |
| Graphes               | Trouver le plus court chemin     | Bellman-Ford         |
| Chaînes de caractères | Trouver une sous-chaîne          | Boyer-Moore          |

<!--
Tout bon livre ou cours d'algorithmique se doit d'aborder ces algorithmes fondamentaux.
Les chaînes de caractères sont un cas particulier.
On manipule tellement de chaînes de caractères que des algorithmes dédiés existent.
Nous avons vu un exemple en TP concernant le tri de chaînes de caractères.
-->

---

# Intérêt

* De nombreux problèmes peuvent se décomposer en **sous-problèmes**.
* Ces sous-problèmes se ramènent souvent à ceux **résolus par les algorithmes classiques**.

---

# Exemples d'autres problèmes

* Optimisation :
    * Graphes, Tri, Recherche.
* Décision :
    * Graphes, Tri, Recherche.
* Classification :
    * Graphes, Tri, Recherche.
* Résolution d'équations (solver :uk:)

<!--
Comme indiqué, de nombreux problèmes peuvent se décomposer en d'autres familles de problèmes pour lesquels des algorithmes efficaces sont connus.
Les algorithmes de résolutions d'équation appartiennent à une autre famille.
Lors d'un cours précédent, nous avons abordé l'algorithme de l'élimination de Gauss-Jordan, qui est un exemple classique dans cette famille.
-->

---

<!-- _class: title-section -->

# <!--fit--> Recherche en Python

---

# Opérateur `in`

```python
L = [1, 4, 8, 62]
if 4 in L:
    print("On a trouvé 4")
```

:arrow_down:

```
On a trouvé 4
```

<!--
Par conséquent, rechercher un élément dans une liste est très simple en Python.
-->

---

### Egalement pour les `set` et `tuple`

```python
S = {1, 4, 8, 62}
if 4 in S:
    print("On a trouvé 4")

T = (1, 4, 8, 62)
if 4 in T:
    print("On a trouvé 4")
```

:arrow_down:

```
On a trouvé 4
On a trouvé 4
```

<!--
Le même opérateur in peut être utilisé sur d'autres types de collections.
-->

---

### Chaînes de caractères

```python
Ch = "1, 4, 8, 62"
if "4" in Ch:
    print("On a trouvé 4")
```

:arrow_down:

```
On a trouvé 4
```

<!--
Cela fonctionne aussi avec les chaînes de caractères.
-->

---

## Dictionnaires

```python
D = {"un": 1, "quatre": 4, "huit": 8, "soixante deux": 62}
if "quatre" in D:
    print("On a trouvé quatre")

if 4 in D.values():
    print("On a trouvé 4")
```

:arrow_down:

```
On a trouvé quatre
On a trouvé 4
```

<!--
Pour les dictionnaires, on peut rechercher soit par clé, soit par valeur.
-->

---

## Valeur par défaut

```python
resultat = D.get("trois", -1)
print(resultat)
```

:arrow_down:

```
-1
```

<!--
Lorsque l'on travaille avec des dictionnaires, il n'est pas rare que l'on souhaite obtenir la valeur d'un clé, si elle existe, et une valeur par défaut, sinon.
La méthode get rempli ce rôle.
-->

---

<!-- _class: title-section -->

# <!--fit--> Recherche linéaire

---

<!-- _class: title-section -->

# <!--fit--> Recherche binaire

##### Binary search

---

<!-- _class: title-section -->

# TP : Recherche dans une collection

---

### TP : Recherche dans une collection

[**Lien** vers le sujet de TP](./tp-14-recherche.html).

---

<!-- _class: title-section -->

# Tri en Python

##### `sort` et `sorted`

---

<!-- _class: title-section -->

# <!--fit--> Algorithmes de tri naïfs


##### Bubble Sort, Insertion Sort, Selection Sort

---

<!-- _class: title-section -->

# <!--fit--> Partition : diviser et conquérir

##### Divide-and-Conquer

---

<!-- _class: title-section -->

# Tri Rapide

##### Quick Sort

---

<!-- _class: title-section -->

# Tri Fusion

##### Merge Sort

---

<!-- _class: title-section -->

# TP : Tri de collections

---

### TP : Tri de collections

[**Lien** vers le sujet de TP](./tp-15-tri.html).
