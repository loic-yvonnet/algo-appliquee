---
title: "Travail Dirigé 2 - Fonctions géométriques simples"
summary: "Travaux Dirigés : Ecrire des fonctions de calcul de périmètre, aire et volume selon les spécifications fournies.."
category: 04-fonctions
permalink: "{{ category }}/td-02-fonctions-geom.html"
url: "{{ url_prefix }}/{{ permalink }}"
layout: layouts/site.njk
---

Ce 2ième TD va vous emmener vers l'implémentation, sur papier, de quelques algorithmes géométriques simples.

## Exercice 1 - Calcul de périmètre d'un rectangle

On a L et l en entrée. Easy.

## Exercice 2 - Cacul d'aire d'un cercle

On a le rayon en entrée.

## Exercice 3 - Calcul de volume d'une sphère

Idem, le rayon en entrée.

## Exercice 4 - Algorithme AABB

On a en entrée un nombre variable de points dans l'espace 3D. L'objectif de l'algorithme AABB est de déterminer une boîte englobante minimale qui regroupe l'ensemble des points.

## Exercice 5 - Calcul d'un cosinus à l'aide d'une série

On peut calculer le cosinus de `x` à l'aide d'une série infinie :

$$
\begin{align}
\cos x & = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \cdots \\[6mu]
& = \sum_{n=0}^\infty \frac{(-1)^n x^{2n}}{(2n)!}.
\end{align}
$$

Plutôt que d'avoir une boucle infinie, on va à nouveau calculer la différence entre 2 résultats consécutifs et s'arrêter lorsque cette différence est inférieur à $\varepsilon < 10^{-9}$.

## Exercice 6 - Collision d'une sphère et d'un plan

Le plan `P` est défini par 3 points `A`, `B` et `C` non alignés.
La sphère `S` est défini par son centre `O` et son rayon `R`.

L'objectif est de déterminer si la sphère est en collision avec le plan. Ce genre de fonction est importante par exemple dans un jeu vidéo

### Exercice 6.1 - Normalisation de vecteur

Ecrivez une fonction qui calcul un vecteur à partir de 2 points (6 arguments et 3 valeurs de retour via tuple).
Ecrivez une fonction qui calcul la norme d'un vecteur
Ecrivez une fonction qui normalise un vecteur

### Exercice 6.2 - Produit vectoriel (cross product)

Ecrivez une fonction qui calcule le cross product de 2 vecteurs (6 arguments et 3 valeurs de retour)

### Exercice 6.3 - Création d'une base O(i, j, k) à partir de 3 points non-alignés

O = A
i = AB normalisé
k = AC noramlisé (cross product) AB
j = i (cross product) k

### Exercice 6.4 - Projection du centre de la sphère sur le plan

Produit scalaire et calcul de S'

### Exercice 6.5 - Calcul de la norme du vecteur du centre de la sphère à son projeté

Calcul vecteur SS' et calcul norme `Dist`

### Exercice 6.6 - Prise en compte des erreurs numériques

Comparaison de `Dist` à `R` en utilisant `abs`.