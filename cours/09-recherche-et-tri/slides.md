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

# Implémentation itérative

```python
def recherche_lineaire(collection, cle):
    for i in range(len(collection)):
        if collection[i] == cle:
            return i
    return -1
```

<!--
Vous avez déjà implémenté cet algorithme.
En pratique, utilisez plutôt l'opérateur in en Python.
Cet algorithme peut être utile si vous implémentez vos propres structures de données.
-->

---

# Preuve d'algorithme

### Preuve triviale

* On parcourt chaque élément de la collection une unique fois, donc l'algorithme s'arrête quand chaque élément est traité.
* Chaque élément est comparé à la clé.
* Donc si un élément est égal à la clé, il sera trouvé.

---

# Complexité

* $O(N)$ : on parcourt chaque élément une fois.
* $\Omega(1)$ : si le 1er élément est égal à la clé, l'algorithme s'arrête immédiatement.

<!--
Rappelez-vous que c'est le Grand O le plus important.
Le Grand Oméga est donné à titre indicatif ici.
-->

---

# Implémentation récursive

```python
def recherche_lineaire(collection, cle):
    def recherche_lineaire_impl(collection, cle, index):
        if index == len(collection):
            return -1
        if collection[index] == cle:
            return index
        return recherche_lineaire_impl(collection, cle, index + 1)
    
    return recherche_lineaire_impl(collection, cle, 0)
```

<!--
Utilisez plutôt la version itérative de l'algorithme.
-->

---

### Preuve de la version récursive

* L'index est incrémenté à chaque récursion.
* La récursion s'arrête lorsque l'index est égal à la taille de la collection.
* A chaque récursion, on teste l'élément à l'index actuel.
* La récursion s'arrête si l'élément à l'index actuel est égal à la clé.
* On parcourt donc chaque élémént une fois et le reste est identique à la version itérative.

---

<!-- _class: title-section -->

# <!--fit--> Recherche binaire

##### Binary search :uk:

---

# Implémentation itérative

```python
def recherche_binaire(collection, cle):
    debut = 0
    fin = len(collection) - 1

    while debut <= fin:
        milieu = debut + (fin - debut) // 2
        actuel = collection[milieu]

        if cle < actuel:
            fin = milieu - 1
        elif cle > actuel:
            debut = milieu + 1
        else:
            return milieu

    return -1
```

<!--
C'est identique à une dichotomie.
-->

---

# Illustration de l'exécution

##### Recherche du chiffre 9

![](./assets/recherche-binaire-tableau.png)

<!--
Le principe est encore mieux visible sous forme d'arbre.
-->

---


# <!--fit--> Exécution sous forme d'arbre (1/4)

##### Recherche du chiffre 9

![](./assets/recherche-binaire-00.png)

---

# <!--fit--> Exécution sous forme d'arbre (2/4)

##### Recherche du chiffre 9

![](./assets/recherche-binaire-01.png)

---

# <!--fit--> Exécution sous forme d'arbre (3/4)

##### Recherche du chiffre 9

![](./assets/recherche-binaire-02.png)

---

# <!--fit--> Exécution sous forme d'arbre (4/4)

##### Recherche du chiffre 9

![](./assets/recherche-binaire-03.png)

---

## Preuve d'algorithme

* A chaque itération :
    * Soit on trouve la clé et l'algorithme s'arrête.
    * Soit l'interval de recherche est réduit de moitié et converge vers la clé car la collection est triée :
        * Soit la borne de fin va au milieu,
        * Soit la borne de début va au milieu.

---

# Complexité

* $O(\log N)$ : on parcourt chaque étage de l'arbre binaire une fois au maximum.
* $\Omega(1)$ : si l'élément du milieu est égal à la clé, l'algorithme s'arrête immédiatement.

<!--
On va prouver la complexité en 0(log N) en établissant le rapport entre la profondeur de l'arbre et le nombre maximal de noeud dans cet arbre.
-->

---

## Profondeur de l'arbre (1/6)

* A la racine de l'arbre (profondeur $p = 1$), on a un seul noeud.
* A chaque niveau, on multiplie le nombre de noeuds par 2.
* A un niveau donné, on a donc $2^{p-1}$ noeuds.

<!--
Le tableau sur la diapositive suivante illustre cette relation.
-->

---

## Profondeur de l'arbre (2/6)

![](./assets/arbre-binaire-profondeur.png)


---

## Profondeur de l'arbre (3/6)

Donc le nombre total maximal de noeuds $N$ est relié à la profondeur $p$ :

$$
N = \sum_{i = 0}^{p - 1} 2^i
$$

<!--
A noter qu'il s'agit là d'une valeur maximale puisque le nombre de valeurs dans l'espace de recherche n'est pas nécessairement une puissance de 2.
Il nous reste à exprimer p en fonction de N.
-->

---

## Profondeur de l'arbre (4/6)

##### Un peu d'arithmétique

$$
\begin{align*}
    2^p &= 2^p \times 1 \\
        &= 2^p \times (2 - 1) \\
        &= 2^{p + 1} - 2^{p}
\end{align*}
$$

<!--
On va utiliser cette astuce pour simplifier la somme de la diapositive précédente.
-->

---

## Profondeur de l'arbre (5/6)

##### Application à la somme des profondeurs

$$
\begin{align*}
N = \sum_{i = 0}^{p - 1} 2^i &= 2^{p-1} + 2^{p-2} + \cdots + 2^0 \\
                             &= (2^{p} - 2^{p-1}) + (2^{p-1} - 2^{p-2}) + \cdots + (2^2 - 2^1) + (2^1 - 2^0) \\
                             &= 2^{p} + (- 2^{p-1} + 2^{p-1}) + \cdots + (- 2^1 + 2^1) - 2^0 \\
                             &= 2^{p} - 2^0 \\
                             &= 2^{p} - 1
\end{align*}
$$

<!--
A la 2e ligne, on applique simplement la relation trouvée sur la diapositive précédente.
Puis on élimine chaque composante 2 à 2.
Il nous reste au final N = 2^p - 1.
-->

---

## Profondeur de l'arbre (6/6)

##### Retour sur le logarithme

$$
\begin{align*}
2^p - 1 &= N \\
2^p &= N + 1 \\
\log_2(2^p) &= \log_2(N + 1) \\
p\log_2(2) &= \log_2(N + 1) \\
p &= \log_2(N + 1)
\end{align*}
$$

<!--
On exprime donc la profondeur de l'arbre en fonction du logarithme du nombre maximal de noeud dans l'arbre binaire.
-->

---

## Preuve de la complexité

$$
\begin{align*}
O(p) &= O(\log_2(N + 1)) \\
     &= O(\log(N))
\end{align*}
$$

On avait vu que la complexité de la recherche binaire était proportionnelle à la profondeur $p$ de l'arbre, c'est-à-dire $O(p)$ soit $O(\log N)$.

<!--
Comprendre cette preuve est importante car on peut souvent la réutiliser pour des algorithmes logarithmiques ou linéarithmiques.
-->

---

<!-- _class: smaller-text -->

# Implémentation récursive

```python
def recherche_binaire(collection, cle):
    def recherche_binaire_impl(collection, cle, debut, fin):
        if fin < debut:
            return -1

        milieu = debut + (fin - debut) // 2
        actuel = collection[milieu]

        if cle < actuel:
            return recherche_binaire_impl(collection, cle, debut, milieu - 1)
        elif cle > actuel:
            return recherche_binaire_impl(collection, cle, milieu + 1, fin)
        else:
            return milieu

    debut = 0
    fin = len(collection) - 1       

    return recherche_binaire_impl(collection, cle, debut, fin)
```

<!--
Attention, il s'agit de code qui doit tenir sur une diapositive de cours.
Dans un contexte industriel, il vaudrait mieux avoir 2 fonctions séparées et correctement documentées.
-->

---

## Relation de récurrence

* Une autre manière de prouver la complexité serait d'utiliser une **relation de récurrence**.
* On pose que le nombre maximal de comparaisons $C$ pour $N = 1$ est $C(1) = 1$.
* On établi alors que $C(N) = 1 + C(\frac{N}{2})$.
* La résolution de la relation de récurrence donne également $O(\log_2(N))$.

<!--
Les détails concernant la relation de récurrence sont considérés comme trop avancés pour ce cours.
Retenez simplement qu'elle existe et offre une base mathématiques pour prouver la complexité d'algorithmes qui peuvent être exprimés de manière récursive.
-->

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

# <!--fit--> Algorithmes de tri en $O(N^2)$


##### Bubble Sort, Insertion Sort, Selection Sort :uk:

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
