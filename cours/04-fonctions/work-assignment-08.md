---
title: "Travail Dirigé 2 - Fonctions géométriques simples"
summary: "Travaux Dirigés : Ecrire des fonctions de calcul de périmètre, aire et volume selon les spécifications fournies."
category: 04-fonctions
permalink: "{{ category }}/td-02-fonctions-geom.html"
url: "{{ url_prefix }}/{{ permalink }}"
layout: layouts/site.njk
---

Ce 2ième TD va vous emmener vers l'implémentation, sur papier, de quelques algorithmes géométriques simples.

## Exercice 1 - Calcul de l'aire d'un rectangle

Ecrivez une fonction qui calcule l'aire d'un rectangle de longueur `L` et de largeur `l`.

Pour rappel, l'aire $A$ d'un rectangle se calcule de la manière suivante : $A = L \times l$.

```py
def calcule_aire_rectangle(L, l):
    """Renvoie l'aire du rectangle.

    L - longueur du rectangle (int ou float).
    l - largueur du rectangle (int ou float).
    Retourne l'aire.
    """
    pass
```

Ecrivez le code qui appelle cette fonction pour `L = 5` et `l = 2`, c'est à dire : `calcule_aire_rectangle(5, 2)`. Affichez dans la sortie standard `"L'aire pour L = 5 et l = 2 est de {valeur}"`, `valeur` était la valeur retournée par la fonction.

## Exercice 2 - Cacul de l'aire d'un cercle

Ecrivez une fonction qui calcule l'aire d'un cercle de rayon `r`.

Pour rappel, l'aire $A$ d'un cercle se calcule de la manière suivante : $A = \pi \times r^2$.

```py
from math import pi

def calcule_aire_cercle(r):
    """Renvoie l'aire du cercle.

    r - rayon du cercle (int ou float).
    Retourne l'aire.
    """
    pass
```

## Exercice 3 - Calcul du volume d'une sphère

Ecrivez une fonction qui calcule le volume d'une sphère de rayon `r`.

Pour rappel, le volume $V$ d'une sphère se calcule de la manière suivante : $V = \frac{4}{3} \times \pi \times r^3$.

```py
from math import pi

def calcule_volume_sphere(r):
    """Renvoie le volume de la sphere.

    r - rayon de la sphere (int ou float).
    Retourne le volume.
    """
    pass
```

## Exercice 4 - Algorithme AABB

On a en entrée un nombre variable de points dans l'espace 3D. L'objectif de l'algorithme AABB est de déterminer une boîte englobante minimale qui regroupe l'ensemble des points de cet espace 3D.

On se propose d'implémenter un algorithme équivalent dans l'espace 2D.

Soit un ensemble de points $P_1(x_1, y_1), P_2(x_2, y_2), \cdots, P_N(x_N, y_N)$, on défini le carré englobant AABB par 4 points :

$$
A_1
\begin{pmatrix} 
\min(x_1, x_2, \cdots, x_N) \\
\max(y_1, y_2, \cdots, y_N)
\end{pmatrix}
, A_2
\begin{pmatrix} 
\min(x_1, x_2, \cdots, x_N) \\
\min(y_1, y_2, \cdots, y_N)
\end{pmatrix}
, B_1
\begin{pmatrix} 
\max(x_1, x_2, \cdots, x_N) \\
\max(y_1, y_2, \cdots, y_N)
\end{pmatrix}
, B_2
\begin{pmatrix} 
\max(x_1, x_2, \cdots, x_N) \\
\min(y_1, y_2, \cdots, y_N)
\end{pmatrix}
$$

Il est à noter que 2 points sont suffisants pour déduire les 2 autres. Pourquoi ?

Ecrivez une fonction qui prend un nombre variable d'arguments. Le nombre d'arguments doit être un multiple de 2 pour représenter les coordonnées `x` et `y` des points. La fonction doit renvoyer 4 valeurs qui correspondent aux coordonnées de $A_2, et B_1$.

```py
def calcule_aabb(*args):
    """Calcule le carré englobant une liste variable de points.

    *args - les coordonnées x1, y1, x2, y2, x3, y3, ..., xN, yN.
    Retourne les coordonnées de 2 points englobants.
    """
    pass
```

*Astuce* : Vous pouvez utiliser une variable Booléenne nommée `drapeau_x`, initialisée à `True`, qui change de valeur à chaque itération en faisant `drapeau_x = not drapeau_x`.

## Exercice 5 - Calcul d'un cosinus à l'aide d'une série

On peut calculer le cosinus de `x` à l'aide d'une série infinie :

$$
\begin{aligned}
\cos x & = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \cdots \\[6mu]
       & = \sum_{n=0}^\infty \frac{(-1)^n x^{2n}}{(2n)!}
\end{aligned}
$$

Plutôt que d'avoir une boucle infinie, on va calculer la différence entre 2 résultats consécutifs et s'arrêter lorsque cette différence est inférieure à $\varepsilon = 10^{-9}$.

```py
def cosinus(nombre):
    """Calcule le cosinus du nombre passé en argument.

    nombre - nombre flottant (float).
    Retourne le cosinus du nombre en entrée.
    """
    pass
```

*Astuces* :
* Vous pouvez préalablement écrire une fonction `factorielle` qui renvoie la factorielle d'un nombre.
* Vous pouvez à nouveau utiliser une variable Booléenne pour ajouter puis soustraire une fois sur deux dans les itérations.
* Comparez votre résultat avec celui de `math.cos` (ajoutez `from math import cos`).

## Exercice 6 - Collision d'une sphère et d'un plan

Le plan $P$ est défini par 3 points $A$, $B$ et $C$ non alignés.
La sphère $S$ est définie par son centre $C_S$ et son rayon $R_S$.

L'objectif est de déterminer si la sphère $S$ est en collision avec le plan $P$. Ce genre de fonction est importante par exemple dans un jeu vidéo (jeu de tir à la 1ière personne, jeu de sport en équipe, etc.), ou dans un logiciel de modélisation 3D pour la conception assistée par ordinateur.

### Exercice 6.1 - Normalisation de vecteur

Ecrivez une fonction qui calcule un vecteur $\overrightarrow{P_1P_2}$ à partir de 2 points $P_1$ et $P_2$.

$$
\forall P_1
\begin{pmatrix} 
x_1 \\
y_1 \\
z_1
\end{pmatrix}
, P_2
\begin{pmatrix} 
x_2 \\
y_2 \\
z_2
\end{pmatrix}
, \overrightarrow{P_1P_2} =
\begin{pmatrix} 
x_2 - x_1 \\
y_2 - y_1 \\
z_2 - z_1
\end{pmatrix}
$$

```py
def vecteur(x1, y1, z1, x2, y2, z2):
    """Renvoie le vecteur P1P2.

    x1 - abscisse de P1 (float).
    y1 - ordonnée de P1 (float).
    z1 - profondeur de P1 (float).
    x2 - abscisse de P2 (float).
    y2 - ordonnée de P2 (float).
    z2 - profondeur de P2 (float).
    Retourne 3 floats x, y, z définissant le vecteur P1P2.
    """
    pass
```

Ecrivez une fonction qui calcul la norme $\left| \overrightarrow{V} \right|$ d'un vecteur $\overrightarrow{V}$.

$$
\forall \overrightarrow{V}
\begin{pmatrix} 
x \\
y \\
z
\end{pmatrix}
, \left| \overrightarrow{V} \right| = \sqrt{x^2 + y^2 + z^2}
$$

```py
def norme(x, y, z):
    """Renvoie la norme du vecteur V.

    x - abscisse de V (float).
    y - ordonnée de V (float).
    z - profondeur de V (float).
    Retourne la norme de V (1 float).
    """
    pass
```

Ecrivez une fonction qui normalise un vecteur. Si on note $n = \left| \overrightarrow{V} \right|$ la norme de $\overrightarrow{V}$, le vecteur normalisé $\overrightarrow{V'}$ se calcule par :

$$
\overrightarrow{V'}
\begin{pmatrix} 
x' \\
y' \\
z'
\end{pmatrix}
= \frac{1}{n}
\begin{pmatrix} 
x \\
y \\
z
\end{pmatrix}
=
\begin{pmatrix} 
\frac{1}{n} \times x \\ \\
\frac{1}{n} \times y \\ \\
\frac{1}{n} \times z
\end{pmatrix}
$$

```py
def normalise(x, y, z):
    """Calcule le vecteur normalisé V' à partir de V.

    x - abscisse de V (float).
    y - ordonnée de V (float).
    z - profondeur de V (float).
    Retourne 3 floats x, y, z correspondant au vecteur V'.
    """
    pass
```

### Exercice 6.2 - Produit scalaire et produit vectoriel

Ecrivez une fonction qui calcule le produit scalaire $PS$ de 2 vecteurs $\overrightarrow{V_1}$ et $\overrightarrow{V_2}$.

$$
\begin{aligned}
\forall \overrightarrow{V_1}
\begin{pmatrix} 
x_1 \\
y_1 \\
z_1
\end{pmatrix}
, \overrightarrow{V_2}
\begin{pmatrix} 
x_2 \\
y_2 \\
z_2
\end{pmatrix}
,
PS & = \overrightarrow{V_1} \cdot \overrightarrow{V_2} \\[6mu]
   & = \frac{1}{2} \left( 
            \left| \overrightarrow{V_1} + \overrightarrow{V_2} \right|^2 
          - \left| \overrightarrow{V_1} \right|^2 
          - \left| \overrightarrow{V_2} \right|^2  
       \right) \\[6mu]
   & = \frac{1}{2} \left(
            \left( \sqrt{(x_1 + x_2)^2 + (y_1 + y_2)^2 + (z_1 + z_2)^2}^2 \right)
          - \left( \sqrt{x_1^2 + y_1^2 + z_1^2}^2 \right)
          - \left( \sqrt{x_2^2 + y_2^2 + z_2^2}^2 \right)
        \right) \\[6mu]
   & = \frac{1}{2} \left(
            \left( (x_1 + x_2)^2 + (y_1 + y_2)^2 + (z_1 + z_2)^2 \right)
          - \left( x_1^2 + y_1^2 + z_1^2 \right)
          - \left( x_2^2 + y_2^2 + z_2^2 \right)
        \right) \\[6mu]
   & = \frac{1}{2} \left(
            (x_1 + x_2)^2 + (y_1 + y_2)^2 + (z_1 + z_2)^2
          - x_1^2 - y_1^2 - z_1^2
          - x_2^2 - y_2^2 - z_2^2
        \right) \\[6mu]
   & = \frac{1}{2} \left(
            2 x_1 x_2
          + 2 y_1 y_2
          + 2 z_1 z_2
        \right) \\[6mu]
   & = x_1 x_2 + y_1 y_2 + z_1 z_2
\end{aligned}
$$

```py
def produit_scalaire(x1, y1, z1, x2, y2, z2):
    """Calcule le produit scalaire de V1 et V2.

    x1 - abscisse de V1 (float).
    y1 - ordonnée de V1 (float).
    z1 - profondeur de V1 (float).
    x2 - abscisse de V2 (float).
    y2 - ordonnée de V2 (float).
    z2 - profondeur de V2 (float).
    Retourne le produit scalaire (1 float).
    """
    pass
```

Ecrivez une fonction qui calcule le produit vectoriel $PV$ de 2 vecteurs $\overrightarrow{V_1}$ et $\overrightarrow{V_2}$.

$$
\begin{aligned}
\forall \overrightarrow{V_1}
\begin{pmatrix} 
x_1 \\
y_1 \\
z_1
\end{pmatrix}
, \overrightarrow{V_2}
\begin{pmatrix} 
x_2 \\
y_2 \\
z_2
\end{pmatrix}
,
PV & = \overrightarrow{V_1} \wedge \overrightarrow{V_2} \\[6mu]
   & = \begin{pmatrix}
            y_1 z_2 - z_1 y_2 \\
            z_1 x_2 - x_1 z_2 \\
            x_1 y_2 - y_1 x_2
       \end{pmatrix}
\end{aligned}
$$

```py
def produit_vectoriel(x1, y1, z1, x2, y2, z2):
    """Calcule le produit vectoriel de V1 et V2.

    x1 - abscisse de V1 (float).
    y1 - ordonnée de V1 (float).
    z1 - profondeur de V1 (float).
    x2 - abscisse de V2 (float).
    y2 - ordonnée de V2 (float).
    z2 - profondeur de V2 (float).
    Retourne 3 floats x, y, z correspondant au produit vectoriel.
    """
    pass
```

### Exercice 6.3 - Création d'une base $O(\vec{i}, \vec{j}, \vec{k})$ à partir de 3 points non-alignés

Soit les 3 points non-alignés $A$, $B$ et $C$ :
$$
A
\begin{pmatrix} 
x_A \\
y_A \\
z_A
\end{pmatrix}
, B
\begin{pmatrix} 
x_B \\
y_B \\
z_B
\end{pmatrix}
, C
\begin{pmatrix} 
x_C \\
y_C \\
z_C
\end{pmatrix}
$$

On va construire la base $O(\vec{i}, \vec{j}, \vec{k})$ de la manière suivante :
* $O$ = $A$
* $\vec{i}$ = $\overrightarrow{AB}$ normalisé
* $\vec{k}$ = $\overrightarrow{AC}$ normalisé $\wedge \vec{i}$
* $\vec{j}$ = $\vec{i} \wedge \vec{k}$

Ecrivez la fonction `plan_origine` qui retourne tout simplement les coordonnées de A :
```py
def plan_origine(xA, yA, zA, xB, yB, zB, xC, yC, zC):
    """Calcule l'origine du plan.

    xA - abscisse de A (float).
    yA - ordonnée de A (float).
    zA - profondeur de A (float).
    xB - abscisse de B (float).
    yB - ordonnée de B (float).
    zB - profondeur de B (float).
    xC - abscisse de C (float).
    yC - ordonnée de C (float).
    zC - profondeur de C (float).
    Retourne xA, yA, zA.
    """
    pass
```

Ecrivez la fonction `plan_vecteur_i` qui retourne le vecteur $\vec{i}$ en calculant le vecteur $\overrightarrow{AB}$ grâce à la fonction `vecteur` puis en le normalisant en appelant la fonction `normalise`.
```py
def plan_vecteur_i(xA, yA, zA, xB, yB, zB, xC, yC, zC):
    """Calcule le vecteur i.

    xA - abscisse de A (float).
    yA - ordonnée de A (float).
    zA - profondeur de A (float).
    xB - abscisse de B (float).
    yB - ordonnée de B (float).
    zB - profondeur de B (float).
    xC - abscisse de C (float).
    yC - ordonnée de C (float).
    zC - profondeur de C (float).
    Retourne xI, yI, zI qui correspondent au vecteur i.
    """
    pass
```

Ecrivez la fonction `plan_vecteur_k` qui retourne le vecteur $\vec{k}$ en :
* calculant le vecteur $\overrightarrow{AC}$ grâce à la fonction `vecteur`,
* puis qui le normalise avec la fonction `normalise`, 
* puis récupère le vecteur $\vec{i}$ en appelant `plan_vecteur_i`,
* et enfin calcule le produit vectoriel $\overrightarrow{AC} \wedge \vec{i}$ en appelant `produit_vectoriel`.
```py
def plan_vecteur_k(xA, yA, zA, xB, yB, zB, xC, yC, zC):
    """Calcule le vecteur k.

    xA - abscisse de A (float).
    yA - ordonnée de A (float).
    zA - profondeur de A (float).
    xB - abscisse de B (float).
    yB - ordonnée de B (float).
    zB - profondeur de B (float).
    xC - abscisse de C (float).
    yC - ordonnée de C (float).
    zC - profondeur de C (float).
    Retourne xK, yK, zK qui correspondent au vecteur k.
    """
    pass
```

Ecrivez la fonction `plan_vecteur_j` qui retourne le vecteur $\vec{j}$ en :
* récupèrant le vecteur $\vec{i}$ en appelant `plan_vecteur_i`,
* récupèrant le vecteur $\vec{k}$ en appelant `plan_vecteur_k`,
* et enfin calcule le produit vectoriel $\vec{i} \wedge \vec{k}$ en appelant `produit_vectoriel`.
```py
def plan_vecteur_j(xA, yA, zA, xB, yB, zB, xC, yC, zC):
    """Calcule le vecteur j.

    xA - abscisse de A (float).
    yA - ordonnée de A (float).
    zA - profondeur de A (float).
    xB - abscisse de B (float).
    yB - ordonnée de B (float).
    zB - profondeur de B (float).
    xC - abscisse de C (float).
    yC - ordonnée de C (float).
    zC - profondeur de C (float).
    Retourne xJ, yJ, zJ qui correspondent au vecteur j.
    """
    pass
```

### Exercice 6.4 - Projection du centre de la sphère sur le plan

Le produit scalaire va nous permettre de déterminer très facilement la distance entre $C_S$, le centre de la sphère, et $O$, l'origine de notre plan (qui correspond en réalité au point $A$).

En effet, de manière générale, si le point $H$ est le projeté d'un point $C$ sur un vecteur $\overrightarrow{OK}$, alors :

$$
\overrightarrow{OK} \cdot \overrightarrow{OC} = 
    \left| \overrightarrow{OK} \right| \times \left| \overrightarrow{OH} \right|
$$

La norme $\left| \overrightarrow{OH} \right|$ correspond à la distance entre le point $C$ et son projeté $H$ sur le plan. Autrement dit, il s'agit de la distance qui nous intéresse.

Dans notre cas : 
* $C$ est le centre de la sphère $C_S$,
* $\overrightarrow{OK} = \vec{k}$.


Or par définition, on a $ \left| \vec{k} \right| = 1$ puisque $\vec{k}$ est normalisé et que la norme d'un vecteur normalisé est égale à 1.

On obtient donc directement la distance :
$$
\begin{aligned}
\overrightarrow{OK} \cdot \overrightarrow{OC} 
    & = \left| \overrightarrow{OK} \right| \times \left| \overrightarrow{OH} \right| \\[6mu]
\vec{k} \cdot \overrightarrow{OC_S}
    & = \left| \vec{k} \right| \times \left| \overrightarrow{OH} \right| \\[6mu]
\vec{k} \cdot \overrightarrow{AC_S}
    & = 1 \times \left| \overrightarrow{OH} \right| \\[6mu]
\left| \overrightarrow{OH} \right| & = \vec{k} \cdot \overrightarrow{AC_S}
\end{aligned}
$$

Ecrivez la fonction `distance` de la manière suivante :
* Appelez la fonction `plan_vecteur_k` pour obtenir $\vec{k}$.
* Appelez la fonction `vecteur` sur $A$ et $C_S$ pour obtenir $\overrightarrow{AC_S}$.
* Appelez la fonction `produit_scalaire` avec $\vec{k}$ et $\overrightarrow{AC_S}$.
* Si la valeur absolue du produit scalaire retourné est éloigné de 0, retournez celui-ci.
* Si le produit scalaire est proche de 0, cela signifie que le projeté $H$ est confondu avec $A$. Dans ce cas, il suffit de retourner la norme $\left| \overrightarrow{AC_S} \right|$.

```py
def distance(xA, yA, zA, xB, yB, zB, xC, yC, zC, xCS, yCS, zCS):
    """Calcule la distance entre point CS et le plan P(A, B, C).

    xA - abscisse de A (float).
    yA - ordonnée de A (float).
    zA - profondeur de A (float).
    xB - abscisse de B (float).
    yB - ordonnée de B (float).
    zB - profondeur de B (float).
    xC - abscisse de C (float).
    yC - ordonnée de C (float).
    zC - profondeur de C (float).
    xCS - abscisse de CS, le centre de la sphère (float).
    yCS - ordonnée de CS, le centre de la sphère (float).
    zCS - profondeur de CS, le centre de la sphère (float).
    Retourne 1 float qui correspond à la distance entre CS et le plan P(A, B, C).
    """
    pass
```

### Exercice 6.5 - Conclusion

Ecrivez la fonction `collision` qui renvoie `True` si la sphère $S(C_S, R_S)$ et le plan $P(A, B, C)$ sont en collision.

Faites attention aux erreurs numériques.

```py
def collision(xA, yA, zA, xB, yB, zB, xC, yC, zC, xCS, yCS, zCS, RS):
    """Dit s'il y a une collision entre le plan P(A, B, C) et la sphère S(CS, RS).

    xA - abscisse de A (float).
    yA - ordonnée de A (float).
    zA - profondeur de A (float).
    xB - abscisse de B (float).
    yB - ordonnée de B (float).
    zB - profondeur de B (float).
    xC - abscisse de C (float).
    yC - ordonnée de C (float).
    zC - profondeur de C (float).
    xCS - abscisse de CS, le centre de la sphère (float).
    yCS - ordonnée de CS, le centre de la sphère (float).
    zCS - profondeur de CS, le centre de la sphère (float).
    RS - rayon de la sphère (float).
    Retourne True s'il y a une collision, et False sinon.
    """
    pass
```