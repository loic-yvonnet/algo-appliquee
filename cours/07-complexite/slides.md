---
marp: true
title: "Algorithmique Appliquée - Complexité"
description: "Cours d'Algorithmique Appliquée avec Python"
author: "Loïc Yvonnet"
keywords: "Algorithmique, Algorithme, Python, Introduction, Débutant"
lang: "fr"
url: "https://loic-yvonnet.github.io/algo-appliquee/09-complexite/"
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

## Introduction à la complexité d'algorithme

<!--
Partie complexe du cours mais totalement fondamentale.
Branchez vos neurones et c'est parti !
-->

---

<!-- _class: smaller-text -->

# Plan

- Intuition sur la complexité
- Complexité temporelle et spatiale
- Notation $O(...)$
- Classes de complexité
- Comparaison des classes de complexité
- Problèmes NP-complet
- Limites de l'étude de complexité
- Approche pragmatique
- Discussion concernant la parallélisation
- Discussion sur la distribution
- Discussion sur les machines quantiques

---

<!-- _class: title-section -->

# <!--fit--> Correction du travail à la maison

---

### DM : Ensembles et calcul matriciel

[**Lien** vers le sujet de DM](../06-problemes-classiques/dm-03.html).

---

<!-- _class: title-section -->

# <!--fit--> Intuition sur la complexité

---

### Complexité conceptuelle et complexité algorithmique

* La **complexité conceptuelle** d'un algorithme est la difficulté à le comprendre.
* La **complexité algorithmique** s'intéresse à l'**efficacité** d'un algorithme.
* Un algorithme plus efficace peut être plus difficile à comprendre. 
* Il s'agit d'un **compromis** entre la complexité conceptuelle et la complexité algorithmique.

---

### Recherche linéaire et dichotomique

* Une recherche linéaire est **très simple à comprendre**.
* Une recherche dichotomique est plus complexe à comprendre.
* Une recherche dichotomique est **plus efficace** qu'une recherche linéaire.
* On dit que la recherche dichotomique a une **meilleure complexité algorithmique**.

---

# Approximation

* Combien de temps va prendre mon programme ?
* Objectif : **comparer** les algorithmes **indépendemment d'une machine**.
* La comparaison ne doit pas se baser sur des mesures.
* Approximation : **compter le nombre d'instructions**.

---

# Instruction

* Dans ce modèle :
    * Une instruction (ou étape) prend un **temps fixe**.
    * Toute instruction prend le **même temps**.
* Une instruction peut être aussi bien :
    * Une opération arithmétique.
    * Assignation d'une variable.
    * Effectuer une comparaison.
    * Etc.

---

# Fonction des entrées

* Dans ce modèle, le **temps d'exécution** est fonction du **nombre d'instructions**.
* Si le nombre d'instructions varie avec la taille d'une entrée, alors le temps d'exécution est fonction de la **taille des entrées**.

---

# <!--fit--> Exemple : recherche linéaire

```python
def recherche(liste, x):
    for element in liste:
        if element == x:
            return True
    return False
```

Si la taille de la liste est de 10 éléments on aura au maximum 10 comparaisons.
Si la taille de la liste est de 1 000 000 éléments on aura au maximum 1 000 000 comparaisons.

---

# <!--fit--> Exemple : déterminant de rang 25 (1/2)

- Soit $m_{i,j}$, $1 \le i,j \le 25$, les éléments d'une matrice $M$ dont on cherche le déterminant :

$$
\left|M\right| =
\sum_{\sigma \in S_{25}} \varepsilon(\sigma) m_{1,\sigma(1)} m_{2,\sigma(2)} \dots m_{25,\sigma(25)}
$$

- $S_{25}$ désigne l'ensemble des permutations de $\{1;2;\dots;25\}$.
- $\varepsilon(\sigma)$ désigne la signature de la permution $\sigma$.
- La signature d'une permutation vaut $\pm 1$.

<!--
Il s'agit de la formule de Leibniz.
Dans le cours précédent, nous avons vu la formule de l'expansion de Laplace.
La formule de Leibniz est simplement une autre manière de calculer un déterminant.
Pour N=3, on a 3! = 6 permutations :
{1, 2, 3} => (-1)^0 * m_{1, 1} * m_{1, 2} * m_{1, 3}
{1, 3, 2} => (-1)^1 * m_{1, 1} * m_{1, 3} * m_{1, 2}
{3, 2, 1} => (-1)^2 * m_{1, 3} * m_{1, 2} * m_{1, 1}
{2, 1, 3} => (-1)^3 * m_{1, 2} * m_{1, 2} * m_{1, 3}
{3, 1, 2} => (-1)^4 * m_{1, 3} * m_{1, 1} * m_{1, 2}
{2, 3, 1} => (-1)^5 * m_{1, 2} * m_{1, 3} * m_{1, 1}
-->

---

# <!--fit--> Exemple : déterminant de rang 25 (2/2)

* Il y a autant de produits à 25 termes à calculer que de permutations.
* C'est à dire $25!$.
* Formule de Stirling : $n! \approx (\frac{n}{e})^n \sqrt{2 \pi n}$.
* Cela implique donc environ $1.5 \cdot 10^{25}$ instructions.
* Avec un processeur qui exécute 10 milliards de produits par secondes, il faudra environ **50 millions d'années** pour calculer ces produits.

<!--
Heureusement, il existe d'autres algorithmes plus efficaces pour calculer un déterminant.
En particulier, l'algorithme de Strassen, en O(N^3) implique une résolution pour N=25 en moins de 25^3 = 15625 multiplications.
Sur le même processeur, il faut moins d'une seconde à cet algorithme pour obtenir le résultat.
Nous n'étudierons pas l'algorithme de Strassen dans ce cours, mais on peut ressentir la différence entre moins d'une seconde et 50 millions d'années pour résoudre le même problème.
-->

---

# Loi de Murphy

* **Cas favorable** : le minimum d'instruction est exécuté.
    * Exemple : l'élément recherché est en 1er.
* **Pire cas** : le maximum d'instructions est exécuté.
    * Exemple : l'élément recherché est à la fin.
* **Cas moyen** : 
* **Loi de Murphy** : on considère généralement le pire cas uniquement.

---

<!-- _class: title-section -->

# <!--fit--> Réflexion sur la complexité temporelle et spatiale

---

<!-- _class: title-section -->

# Notation $O(...)$

---

<!-- _class: title-section -->

# Classes de complexité

##### Constante, logarithmique, linéaire, log-linéaire, polynomiale

---

<!-- _class: title-section -->

# <!--fit--> Comparaison des classes de complexité

---

<!-- _class: title-section -->

# TD : Evaluation de compléxité

---

### TD : Evaluation de compléxité

[**Lien** vers le sujet de TD](./td-04-eval-complexite.html).

---

<!-- _class: title-section -->

# <!--fit--> Problèmes NP-complet

##### Intuition et exemple

---

<!-- _class: title-section -->

# <!--fit--> Limites de l'étude de complexité

##### Architecture matérielle moderne (CPU)

---

<!-- _class: title-section -->

# Approche pragmatique

##### Mesures et benchmarks

---

<!-- _class: title-section -->

# <!--fit--> Discussion concernant la parallélisation

##### CPU et GPU

---

<!-- _class: title-section -->

# <!--fit--> Discussion sur la distribution de calcul

##### Cluster et sur le Cloud

---

<!-- _class: title-section -->

# <!--fit--> Discussion sur les machines quantiques

##### Qubit

---

<!-- _class: title-section -->

# TP : Benchmark et complexité

---

### TP : Benchmark et complexité

[**Lien** vers le sujet de TP](./tp-11-bench-complexite.html).
