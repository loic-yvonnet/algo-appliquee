---
title: "Travail Dirigé 3 - Opérations matricielles classiques"
summary: "Travaux Dirigés : Implémenter les opérations matricielles les plus classiques (addition, multiplication scalaire, calcul de déterminant, multiplication matricielle)."
category: 05-structures-donnees
permalink: "{{ category }}/td-03-op-matricielles.html"
url: "{{ url_prefix }}/{{ permalink }}"
layout: layouts/site.njk
---

Ce travail dirigé va vous amener à écrire des fonctions de calcul matriciel.

## Exercice 1 - Affichage de matrices

En utilisant des caractères unicodes pour les bordures et un alignement avec f-string pour que ce soit lisible, écrivez une fonction `affiche_vecteur` telle que :

```py
vecteur = [1, 2, 3]
affiche_vecteur(vecteur)
```

doit afficher :
```
╭       ╮
│   1   │
│   2   │
│   3   │
╰       ╯
```

De même, écrivez une fonction `affiche_matrice` telle que :

```py
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
affiche_matrice(matrice)
```

doit afficher :
```
╭               ╮
│   1   2   3   │
│   4   5   6   │
│   7   8   9   │
╰               ╯
```

*Astuces* :
* Les caractères spéciaux sont `"╭"`, `"╮"`, `"╯"`, `"╰"` et `"│"`.
* Avec une première boucle qui parcourt tous les éléments de la matrice, convertissez chaque élément avec `str` puis calculez sa taille avec `len`. Conservez la taille du plus grand élément `taille_max`.
* La taille d'une ligne de texte est égale à `2` caractères unicode spéciaux + `(taille_max + 3) * len(matrice[0])` + `3` espaces avant le dernier caractère spécial.
* Il est possible d'afficher `N` fois un caractère `"a"` avec `print(N * "a")`. Cela fonctionne aussi avec une f-string : `print(f"Beaucoup de a : {N * 'a'}.")`.
* On peut aligner à droite un nombre `N` dans une f-string de la manière suivante : `print(f"{N:>{taille_max + 3}}")`.

## Exercice 2 - Addition de vecteurs

Ecrivez une fonction `ajoute_vecteurs` qui prend 2 listes `v1` et `v2` en entrée et telle que :

```py
v1 = [1, 2, 3, 4, 5, 6]
v2 = [6, 5, 4, 3, 2, 1]
v3 = ajoute_vecteurs(v1, v2)
affiche_vecteur(v3)
```

doit afficher :
```
╭       ╮
│   7   │
│   7   │
│   7   │
│   7   │
│   7   │
│   7   │
╰       ╯
```

tandis que :
```py
v4 = [1, 2]
v5 = [1, 2, 3]
v6 = ajoute_vecteurs(v4, v5)
affiche_vecteur(v6)
```

doit afficher :
```
Erreur : les vecteurs n'ont pas la même dimension !
```

## Exercice 3 - Addition de matrices

Ecrivez une fonction `ajoute_matrices` qui prend 2 listes `m1` et `m2` en entrée et telle que :

```py
m1 = [
    [ 1,  2,  3],
    [ 4,  5,  6],
    [ 7,  8,  9],
    [10, 11, 12]
]
m2 = [
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3],
    [4, 4, 4]
]
m3 = ajoute_matrices(m1, m2)
affiche_matrice(m3)
```

doit afficher :
```
╭                  ╮
│    2    3    4   │
│    6    7    8   │
│   10   11   12   │
│   14   15   16   │
╰                  ╯
```

tandis que :
```py
m4 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]
m5 = [
    [1, 5],
    [2, 6],
    [3, 7],
    [4, 8]
]
m6 = ajoute_matrices(m4, m5)
affiche_matrice(m6)
```

doit afficher :
```
Erreur : les matrices n'ont pas les mêmes dimensions !
```

## Exercice 4 - Multiplication d'une matrice par un scalaire

Ecrivez une fonction `multiplie_scalaire_matrice` qui prend un nombre `s` et une liste `m` en entrée et telle que :

```py
scalaire = 3
m1 = [
    [ 1,  2,  3],
    [ 4,  5,  6],
    [ 7,  8,  9]
]
m2 = multiplie_scalaire_matrice(scalaire, m1)
affiche_matrice(m2)
```

doit afficher :
```
╭                  ╮
│    3    6    9   │
│   12   15   18   │
│   21   24   27   │
╰                  ╯
```

## Exercice 5 - Dimensions d'une matrice

Ecrivez une fonction `dimensions` qui prend une liste `m` en entrée et telle que :
```py
matrice2x2 = [
    [1, 2],
    [3, 4]
]
lignes, colonnes = dimensions(matrice2x2)
print(f"La matrice2x2 a pour dimensions ({lignes}, {colonnes}).")

matrice3x2 = [
    [1, 2],
    [3, 4],
    [5, 6]
]
lignes, colonnes = dimensions(matrice3x2)
print(f"La matrice3x2 a pour dimensions ({lignes}, {colonnes}).")

matrice2x3 = [
    [1, 2, 3],
    [4, 5, 6]
]
lignes, colonnes = dimensions(matrice2x3)
print(f"La matrice2x3 a pour dimensions ({lignes}, {colonnes}).")
```

doit afficher :
```
La matrice2x2 a pour dimensions (2, 2).
La matrice3x2 a pour dimensions (3, 2).
La matrice2x3 a pour dimensions (2, 3).
```

tandis que :
```py
matrice2x1 = [
    [1],
    [3]
]
if est_carree(matrice2x1):
    print("C'est une matrice carrée.")
else:
    print("Ce n'est pas une matrice carrée.")
```

doit afficher :
```
Ce n'est pas une matrice carrée.
```

## Exercice 6 - Calcul du déterminant d'une matrice carrée

### Exercice 6.1 - Matrice carrée

Ecrivez une fonction `est_carree` qui prend une liste `m` en entrée et telle que :
```py
matrice2x2 = [
    [1, 2],
    [3, 4]
]
if est_carree(matrice2x2):
    print("C'est une matrice carrée.")
else:
    print("Ce n'est pas une matrice carrée.")
```

doit afficher :
```
C'est une matrice carrée.
```

tandis que :
```py
matrice2x1 = [
    [1],
    [3]
]
if est_carree(matrice2x1):
    print("C'est une matrice carrée.")
else:
    print("Ce n'est pas une matrice carrée.")
```

doit afficher :
```
Ce n'est pas une matrice carrée.
```

### Exercice 6.2 - Déterminant d'une matrice 2x2 (2 lignes et 2 colonnes)

Soit la matrice $M_{2 \times 2}$ telle que :

$$
M_{2 \times 2} =
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
$$

On note $\left| M_{2 \times 2} \right|$ le déterminant de $M_{2 \times 2}$, qui se calcule par un simple produit en croix :

$$
\left| M_{2 \times 2} \right|
=
\left|
    \begin{pmatrix}
    a & b \\
    c & d
    \end{pmatrix}
\right|
=
\left|
    \begin{matrix}
    a & b \\
    c & d
    \end{matrix}
\right|
=
ad - cb
$$

Ecrivez une fonction `determinant_2x2` qui prend une liste `m` en entrée et telle que :

```py
matrice2x2 = [
    [1, 2],
    [3, 4]
]
d = determinant_2x2(matrice2x2)
print(f"Le déterminant vaut {d}.")
```

doit afficher :
```
Le déterminant vaut -2.
```

### Exercice 6.3 - Déterminant d'une matrice 3x3

Soit la matrice $M_{3 \times 3}$ telle que :

$$
M_{3 \times 3} =
\begin{pmatrix}
a & b & c \\
d & e & f \\
g & h & i
\end{pmatrix}
$$

On note $\left| M_{3 \times 3} \right|$ le déterminant de $M_{3 \times 3}$, qui se calcule de la manière suivante :

$$
\left| M_{3 \times 3} \right|
=
\left|
    \begin{matrix}
    a & b & c \\
    d & e & f \\
    g & h & i
    \end{matrix}
\right|
=
a
\left|
    \begin{matrix}
    e & f \\
    h & i
    \end{matrix}
\right|
- b
\left|
    \begin{matrix}
    d & f \\
    g & i
    \end{matrix}
\right|
+ c
\left|
    \begin{matrix}
    e & f \\
    h & i
    \end{matrix}
\right|
=
a(ei − fh) − b(di − fg) + c(dh − eg)
$$

Ecrivez une fonction `determinant_3x3` qui prend une liste `m` en entrée et telle que :

```py
matrice3x3 = [
    [ 1,  2,  3],
    [ 4,  5,  6],
    [ 7,  8,  9]
]
d = determinant_3x3(matrice3x3)
print(f"Le déterminant vaut {d}.")
```

doit afficher :
```
Le déterminant vaut 0.
```

### Exercice 6.4 - Généralisation du calcul d'un déterminant

La généralisation du calcul d'un déterminant peut s'effectuer de manière récursive.

Etant donné $M$, une matrice carrée de dimension $n \times n$ : pour tout $i$ et $j$, on note $M_{i,j}$ la matrice obtenue en **enlevant** à $M$ sa ligne $i$ et sa colonne $j$. Regardez au milieu de la matrice suivante et observez qu'il y a un saut d'indices :

$$
M_{i,j} =
\begin{pmatrix}
    m_{1,1}   & \dots & m_{1,j-1}   & m_{1,j+1}   & \dots & m_{1,n}   \\
    \vdots    &       & \vdots      & \vdots      &       & \vdots    \\
    m_{i-1,1} & \dots & m_{i-1,j-1} & m_{i-1,j+1} & \dots & m_{i-1,n} \\
    m_{i+1,1} & \dots & m_{i+1,j-1} & m_{i+1,j+1} & \dots & m_{i+1,n} \\
    \vdots    &       & \vdots      & \vdots      &       &\vdots     \\
    m_{n,1}   & \dots & m_{n,j-1}   & m_{n,j+1}   & \dots & m_{n,n}
\end{pmatrix}
$$

On passe de $i-1$ à $i+1$, et de $j-1$ à $j+1$ et donc on *saute* $i$ et $j$.

Ecrivez une fonction `enleve_ligne_et_colonne` qui prend une liste `m` et 2 entiers `i` et `j` en entrée et telle que :
```py
M = [
    [ 1,  2,  3],
    [ 4,  5,  6],
    [ 7,  8,  9]
]
M11 = enleve_ligne_et_colonne(M, 1, 1)
M12 = enleve_ligne_et_colonne(M, 1, 2)
print("M11 =")
affiche_matrice(M11)
print("M12 =")
affiche_matrice(M12)
```

doit afficher :
```
M11 =
╭           ╮
│   5   6   │
│   8   9   │
╰           ╯
M12 =
╭           ╮
│   4   6   │
│   7   9   │
╰           ╯
```

*Astuce* : En informatique, on utilise des index à partir de 0, tandis qu'en algèbre, on utilise des index à partir de 1. Donc l'indice 1 en entrée de la fonction `enleve_ligne_et_colonne` correspond à l'indice 0 dans la liste.

On peut alors développer le calcul du déterminant de $M$ suivant une ligne. Pour le calcul du déterminant d'une matrice 3x3 avec une matrice 2x2, on a suivi la 1ière ligne. On peut faire de même ainsi :

$$
\left| M \right|
=
\sum_{j=1}^{n} m_{1,j} (-1)^{1+j} \left| M_{1,j} \right|
$$

Pour implémenter cette version généralisée, on devrait utiliser la récursivité en vérifiant les dimensions des sous-matrices et en appelant au final `determinant_2x2` et/ou `determinant_3x3`. Nous gardons cet exercice pour plus tard.

## Exercice 7 - Multiplication matricielle

### Exercice 7.1 - Est-ce multipliable ?

Soit 1 matrice $M_{L \times C}$ de dimension $L \times C$, et une matrice $N_{R \times K}$ de dimension $R \times K$.

Il n'est possible de multiplier $M_{L \times C}$ par $N_{R \times K}$ que si et seulement si `C == R`.

Ecrivez une fonction `est_multipliable` qui prend 2 listes `m` et `n` en entrée et telles que :

```py
M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
N = [
    [1],
    [2],
    [3]
]
MxN = est_multipliable(M, N)
if MxN:
    print("On peut multiplier M par N.")
else:
    print("On ne peut pas multiplier M par N.")

NxM = est_multipliable(N, M)
if NxM:
    print("On peut multiplier N par M.")
else:
    print("On ne peut pas multiplier N par M.")
```

doit afficher :
```
On peut multiplier M par N.
On ne peut pas multiplier N par M.
```

On voit au passage que la multiplication matricielle n'est pas *commutative* : $M \cdot N \neq N \cdot M$.

### Exercice 7.2 - Implémentation de la multiplication matricielle

Le principe général de la multiplication matricielle consiste à faire la somme des produits des lignes de la première matrice par les colonnes de la deuxième matrice.

La matrice résultat $Z_{L \times K} = M_{L \times C} \cdot N_{R \times K}$ a pour dimension $L \times K$. Autrement dit, on prend le nombre de lignes à gauche, et le nombre de colonnes à droite.

De manière plus formelle :

$$
M =
\begin{pmatrix}
     m_{1,1} & m_{1,2} & \cdots & m_{1,C} \\
     m_{2,1} & m_{2,2} & \cdots & m_{2,C} \\
    \vdots   & \vdots  & \ddots & \vdots  \\
     m_{L,1} & m_{L,2} & \cdots & m_{L,C} \\
\end{pmatrix},
N =
\begin{pmatrix}
     n_{1,1} & n_{1,2} & \cdots & n_{1,K} \\
     n_{2,1} & n_{2,2} & \cdots & n_{2,K} \\
    \vdots   & \vdots  & \ddots & \vdots  \\
     n_{R,1} & n_{R,2} & \cdots & n_{R,K} \\
\end{pmatrix}
$$

Si on note le résultat ainsi :

$$
Z =
\begin{pmatrix}
     z_{1,1} & z_{1,2} & \cdots & z_{1,K} \\
     z_{2,1} & z_{2,2} & \cdots & z_{2,K} \\
    \vdots   & \vdots  & \ddots & \vdots  \\
     z_{L,1} & z_{L,2} & \cdots & z_{L,K} \\
\end{pmatrix}
$$

On peut calculer chacun de ses éléments de la manière suivante :

$$
z_{i,j} = m_{i,1}n_{1,j} + m_{i,2}n_{2,j} + \cdots + m_{i,C}n_{C,j}
        = \sum_{x=1}^C m_{i,x}n_{x,j}
$$

Ce qui donne au final la matrice suivante :

$$
Z =
\begin{pmatrix}
    \sum_{x=1}^C m_{1,x}n_{x,1} && \sum_{x=1}^C m_{1,x}n_{x,2} && \cdots && \sum_{x=1}^C m_{1,x}n_{x,K} \\ \\
    \sum_{x=1}^C m_{2,x}n_{x,1} && \sum_{x=1}^C m_{2,x}n_{x,2} && \cdots && \sum_{x=1}^C m_{2,x}n_{x,K} \\ \\
    \vdots                      && \vdots                      && \ddots && \vdots                      \\ \\
    \sum_{x=1}^C m_{L,x}n_{x,1} && \sum_{x=1}^C m_{L,x}n_{x,2} && \cdots && \sum_{x=1}^C m_{L,x}n_{x,K}
\end{pmatrix}
$$

Ecrivez une fonction `multiplie_matrices` qui prend en entrée 2 listes `m1` et `m2` et telle que :
```py
M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
N = [
    [1],
    [1],
    [1]
]
Z = multiplie_matrices(M, N)
print("Z =")
affiche_matrice(Z)

I = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]
M2 = multiplie_matrices(M, I)
print("M2 =")
affiche_matrice(M2)
```

doit afficher :
```
Z =
╭        ╮
│    6   │
│   15   │
│   24   │
╰        ╯
M2 =
╭               ╮
│   1   2   3   │
│   4   5   6   │
│   7   8   9   │
╰               ╯
```
