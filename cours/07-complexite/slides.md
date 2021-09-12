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
* **Cas moyen** : temps moyen pour des entrées classiques (par exemple, 90% des cas).
* **Loi de Murphy** : si un problème peut survenir, il surviendra. On se concentre donc sur le pire cas.

---

<!-- _class: title-section -->

# Réflexion sur la complexité temporelle et spatiale

---

# Complexité temporelle

* C'est le type de complexité algorithmique que nous avons discuté jusqu'à présent.
* On s'attache à évaluer le temps d'exécution sur une machine théorique.

---

# Complexité spatiale

* La **complexité spatiale** s'attache à déterminer la place mémoire nécessaire pour la résolution d'un algorithme.
* Il s'agit d'une fonction des entrées de l'algorithme étudié.

---

# Temporel et spatial

* On se focalise d'abord sur la complexité temporelle.
* Si 2 algorithmes ont la même complexité temporelle, on compare leurs complexités spatiales.

---

<!-- _class: title-section -->

# Notation $O(...)$

---

# Notation asymptotique

* **Notation asymptotique** : manière formelle de relier le temps d'exécution à la taille des entrées.
* On s'intéresse au cas où la taille des entrées approche l'**infini**.

<!--
On va prendre un exemple.
-->

---

# Exemple (1/2)

```python
def f(x):
    y = 0
    for i in range(x):
        for j in range(x):
            y += 1
            y += 1

    for i in range(x):
        y += 1

    for i in range(99):
        y += 1

    return y
```

On a $2x^2 + x + 100$ instructions.

<!--
Dans la boucle imbriquée, on a 2 additions, d'où le 2x^2.
La dernière boucle va de 0 à 98 : 99 instructions.
On y ajoute l'initialisation de y à la première ligne du corps de la fonction f => 100 instructions constantes.
-->

---

# Exemple (2/2)

* Pour $x = 3$, on a $2 \cdot 3^2 + 3 + 100 = 121$ instructions. On est dominé par le **facteur constant**.
* Pour $x = 10$, on a 310 instructions, dont 200 dans la première boucle imbriquée.
* Pour $x = 100$, la première boucle imbriquée **écrase** les autres : 20000 instructions contre seulement 200.

---

# Conclusions

- L'exemple précédent montre qu'asymptotiquement, quand x tend vers l'infini, **seul le terme de rang le plus élevé compte** : $2x^2$.
- On peut même dire que la croissance dépend essentiellement de $x^2$.
- Nous souhaitons simplifier l'étude de la complexité des algorithmes en **éliminant les termes insignifiants**.

---

# Notation $\thicksim$

##### Approximation tilde

* Soit $f(n)$ et $g(n)$ deux suites positives indexées sur $\mathbb{N}$.
* On dit que $g \thicksim f$, si $\lim\limits_{\infty} \frac{g}{f} = 1$.
* $f$ et $g$ sont **asymptotiquement égaux**.

---

# Exemples avec $\thicksim$

| Fonction                   | Approximation $\thicksim$ |
|----------------------------|:-------------------------:|
| $2x^2 + x + 100$           |      $\thicksim 2x^2$     |
| $3x^3 + 3000x + 10000000$  |     $\thicksim 3x^3$      |
| $\log(x) + 100000$         |    $\thicksim \log(x)$    |
| $300$                      |      $\thicksim 300$      |

---

# Notation Grand O (1/2)

* On l'appelle **notation de Landau**.
* Il s'agit de la **notation la plus utilisée** en algorithmique pour comparer des algorithmes.
* Cette notation se lit : **Grand O de [...]**.
* On l'appelle également **ordre de grandeur**, ou ordre de croissance.

<!--
Edmund Georg Hermann LANDAU est un mathématicien berlinois renvoyé en 1934 de l'université par les nazis.
Il décède en 1938.
-->

---

# Notation Grand O (2/2)

* Soit $f(n)$ et $g(n)$ deux suites positives indexées sur $\mathbb{N}$.
* On dit que $g = O(f)$ s'il existe $n_0$ et $C > 0$ tels que pour tout $n > n_0$, on a $g(n) \le C f(n).
* Autrement dit, $g$ est dominé par $f$ à partir d'un certain rang.


---

# Exemples avec $\thicksim$ et O

| Fonction          | Approximation $\thicksim$ |       Grand O     |
|-------------------|:-------------------------:|:-----------------:|
| $2N^2 + N + 100$  |      $\thicksim 2N^2$     |       O($N^2$)    |
| $3N^3 + 3N + 3$   |     $\thicksim 3N^3$      |       O($N^3$)    |
| $\log(N) + 10$    |    $\thicksim \log(N)$    |     O($\log(N)$)  |
| $300$             |      $\thicksim 300$      |         O(1)      |

---

# Notation petit o

* On dit que $g = o(f)$ si pour tout $\varepsilon > 0$, il existe $n_{\varepsilon}$ tel que si $n > n_{\varepsilon}$, alors $g(n) \le \varepsilon f(n)$.
* Cette notation se lit : **g est un petit o de f**.
* Autrement dit, g est négligable devant f.
* Si $f(n) \ne 0$, alors $\lim\limits_{\infty} \frac{g}{f} = 0$.
* C'est tout simplement l'**inverse de Grand O**.
* Notation alternative : $g = o(f) \Longleftrightarrow g = \Omega(f)$.

<!--
La notation alternative se dit Grand Oméga de [...].
En mathématiques, on utilise peut-être plus la notation "petit o", et en information, la notation "Grand Oméga".
En pratique, dans l'industrie, cette notation est très rarement utilisée (sauf exception).
-->

---

# Notation $\asymp$

* On dit que $g \asymp f$, s'il existe $n_0$ et $C_1, C_2 > 0$ tels que si $n > n_0$, alors $C_1 f(n) \le g(n) \le C_2 f(n)$.
* $f$ et $g$ sont **comparables**.
* Notation alternative : $g \asymp f \Longleftrightarrow g = \Theta(f)$.

<!--
De la même manière, la notation asymptotique est peut-être plus utilisée en mathématiques, tandis que la notation Grand Théta est probablement plus utilisée en algorithmique.
-->

---

<!-- _class: smaller-text -->

# Comparaison

|                  |  Approximation Tilde  |      Grand O     |    Grand Oméga   |  Grand Théta |
|------------------|:---------------------:|:----------------:|:----------------:|:------------:|
| Notation algo    |      $\thicksim$      |         O        |     $\Omega$     |   $\Theta$   |
| Notation maths   |      $\thicksim$      |         O        |          o       |   $\asymp$   |
| Définition       | Asymptotiquement égal | Borne supérieure | Borne inférieure | Borne serrée |
| Utilité pratique |       Très rare       |  **Très élevée** |     Très rare    |    Elevée    |

---

# Abus de langage fréquent

On utilise si souvent la notation Grand O qu'on l'utilise parfois en lieu et place de Grand $\Theta$.

---

<!-- _class: title-section -->

# Classes de complexité

##### Constante, logarithmique, linéaire, linéarithmique, polynomiale

---


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
