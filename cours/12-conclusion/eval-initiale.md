---
title: Evaluation initiale
summary: Evaluation initiale pour l'Algorithmique Appliquée et le HTML/CSS.
url: "{{ url_prefix }}/eval-initiale.html"
layout: layouts/site.njk
---

![](../assets/entete-cci.png)

Cette évaluation initiale donnera lieu à une note sur 20. Cette note ne compte ni dans le contrôle continu, ni pour l'examen final.

Il s'agit simplement d'un moyen pour l'équipe pédagogique d'avoir un aperçu du niveau des apprenants à l'entrée du BTS SIO.

Vous avez 30 minutes pour répondre aux questions. Si vous ne connaissez pas la réponse à une question, passez directement à la question suivante.

## Partie 1 - Un peu de mathématiques <span class="fs-4 fw-lighter">(4 points)</span>

### Exercice 1.1 - Multiplication matricielle <span class="fs-5 fw-lighter">(2 points)</span>

Soit les matrices $A$ et $B$ :

$$
A =
\begin{pmatrix} 
     1 & 2 \\
    -1 & 3
\end{pmatrix},

B = 
\begin{pmatrix} 
    1 \\
    2
\end{pmatrix}
$$

Calculez $A \cdot B$ :

<div class="w-100 border rounded d-block mb-3 mt-0" style="height: 100px;"></div>

<!--
Réponse (1 point) :
m_{0,0} = 1 * 1 + 2 * 2 = 5
m_{1,0} = -1 * 1 + 3 * 2 = 5

Donc M = A * B =
\begin{pmatrix} 
    5 \\
    5
\end{pmatrix}
--->


Calculez le déterminant $\left| A \right|$ de la matrice $A$ :

<div class="w-100 border rounded d-block mb-3" style="height: 100px;"></div>

<!--
Réponse (1 point) : det A = 1 * 3 - (-1 * 2) = 3 + 2 = 5
-->

### Exercice 1.2 - Logique Booléenne <span class="fs-5 fw-lighter">(2 points)</span>

Soit $x, y, z \in \{ 0 ; 1 \}$, factorisez l'expression suivante :

$$
(x \land y) \vee (x \land z)
$$

<div class="w-100 border rounded d-block mb-3" style="height: 100px;"></div>

<!--
Réponse (1 point) :
x \land (y \vee z)
-->


Que vaut cette expression si $x = 0$ ?

<div class="w-100 border rounded d-block mb-3" style="height: 100px;"></div>

<!--
Réponse (1 point) : 0
En effet, \forall x, 0 \land x = 0
-->


## Partie 2 - Algorithmique <span class="fs-4 fw-lighter">(8 points)</span>

### Exercice 2.1 - Connaissances générales <span class="fs-5 fw-lighter">(3 points)</span>

Quelle est la complexité en notation O d'un algorithme de recherche binaire dans une liste triée ?

<div class="w-100 border rounded d-block mb-3" style="height: 100px;"></div>

<!--
Réponse (1 point) : O(log N)
-->


Quelle est la complexité en notation O d'un algorithme de tri rapide ?

<div class="w-100 border rounded d-block mb-3" style="height: 100px;"></div>

<!--
Réponse (1 point) : O(N log N)
-->


Que signifie l'expression Turing-complet lorsque l'on parle d'un langage de programmation ?

<div class="w-100 border rounded d-block mb-3" style="height: 100px;"></div>

<!--
Réponse (1 point) : Ce langage de programmation est capable d'effectuer n'importe quel calcul modéliser par une machine de Turing. Autrement dit, n'importe quel algorithme peut être écrit dans ce langage.
-->

### Exercice 2.2 - Compréhension de code <span class="fs-5 fw-lighter">(2 points)</span>

Que fait le code suivant ?

```python
def f(L):
    taille = len(L)
    for i in range(taille):
        if L[i] == 42:
            print("La réponse est 42")
            return True

    return False
```

<div class="w-100 border rounded d-block mb-3" style="height: 300px;"></div>

<!--
Réponse (2 points) : 
Il s'agit d'une fonction qui prend une liste. La fonction parcourt chaque élément de la liste. Si le nombre 42 est trouvé, on affiche dans la sortie standard la chaîne de caractères "La réponse est 42", on stoppe la boucle et on renvoie True. Dans le cas contraire, la boucle continue jusqu'à son terme et on renvoie False.
-->


### Exercice 2.3 - Un peu de programmation <span class="fs-5 fw-lighter">(3 points)</span>

Ecrivez une fonction `trouve_triplets` qui prend 3 listes d'entiers en entrée. Cette fonction doit trouver tous les triplets dont la somme s'annule et renvoyer leurs indices.

Par exemple, en Python :
```python
L1 = [1, 3, 4]
L2 = [8, -1, 12, -3]
L3 = [0, 2]

resultat = trouve_triplets(L1, L2, L3)
print(resultat)
```

doit afficher :
```python
[(0, 1, 0), (0, 3, 1), (1, 3, 0)]
```

En effet :
* $\text{L1}[0] + \text{L2}[1] + \text{L3}[0] = 1 + (-1) + 0 = 0$.
* $\text{L1}[0] + \text{L2}[3] + \text{L3}[1] = 1 + (-3) + 2 = 0$.
* $\text{L1}[1] + \text{L2}[3] + \text{L3}[0] = 3 + (-3) + 0 = 0$.

Indiquez le langage de programmation que vous utilisez pour votre implémentation.

<!--
Réponse :
def trouve_triplets(L1, L2, L3):
    resultat = []
    for i in range(len(L1)):
        for j in range(len(L2)):
            for k in range(len(L3)):
                if L1[i] + L2[j] + L3[k] == 0:
                    resultat.append((i, j, k))

    return resultat
-->

<div class="w-100 border rounded d-block mb-3" style="height: 400px;"></div>

## Partie 3 - HTML/CSS <span class="fs-4 fw-lighter">(8 points)</span>

### Exercice 3.1 - Connaissances générales <span class="fs-5 fw-lighter">(3 points)</span>

Que sont HTTP et HTML ?

<div class="w-100 border rounded d-block mb-3" style="height: 100px;"></div>

<!--
Réponse (1 point) :
HTTP est un protocole d'échange de données.
HTML est un langage de markup pour décrire le contenu d'une page web.
-->


Quelles sont les relations entre HTML et XML ?

<div class="w-100 border rounded d-block mb-3" style="height: 100px;"></div>

<!--
Réponse (1 point) :
Les 2 utilisent des balises du type <div></div>.
XML est plus rigoureux que HTML concernant la fermeture des balises.
XML est un meta-langage tandis que HTML est un langage spécifique.
-->



Quelles sont les relations entre HTML et CSS ?

<div class="w-100 border rounded d-block mb-3" style="height: 100px;"></div>

<!--
Réponse (1 point) :
HTML permet de décrire le contenu d'une page web.
CSS permet de contrôler le style et l'affichage de ce contenu.
-->


### Exercice 3.2 - Compréhension de code <span class="fs-5 fw-lighter">(2 points)</span>

Que fait le code suivant ?

```html
<table class="table table-hover table-bordered table-responsive align-middle">
    <caption>Joueurs de PathFinder</caption>
    <thead class="table-dark">
        <tr class="text-center">
            <th></th>
            <th>
                Alice
            </th>
            <th>
                Bob
            </th>
            <th>
                Eve
            </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th>
                Classe
            </th>
            <td class="text-center">
                <a href="https://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.Magicien.ashx">Magicienne</a>
            </td>
            <td class="text-center">
                <a href="https://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.Roublard.ashx">Voleur</a>
            </td>
            <td class="text-center">
                <a href="https://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.Guerrier.ashx">Guerrière</a>
            </td>
        </tr>
        <tr>
            <th>
                Illustration
            </th>
            <td>
                <img src="https://www.pathfinder-fr.org/wiki/public/upload/Illustrations/PNJ/Seoni.jpg"
                     style="width: 80px;"/>
            </td>
            <td>
                <img src="https://www.pathfinder-fr.org/wiki/public/upload/Illustrations/PNJ/Barde.jpg"
                     style="width: 80px;"/>
            </td>
            <td>
                <img src="https://www.pathfinder-fr.org/wiki/public/upload/Illustrations/PNJ/Amiri.jpg"
                     style="width: 80px;"/>
            </td>
        </tr>
    </tbody>
</table>
```

<div class="w-100 border rounded d-block mb-3" style="height: 300px;"></div>

<!--
Réponse :
On affiche un tableau de 4 colonnes et 3 lignes comportant des entêtes.
La première ligne comprend les titres des colonnes.
La deuxième ligne contient des liens hypertexte vers des pages web.
La troisième ligne contient des images de largeurs égales.
Un caption est affiché sous le tableau.
Point bonus si l'apprenant reconnaît l'usage de Bootstrap.
-->


### Exercice 3.3 - Donner du style <span class="fs-5 fw-lighter">(3 points)</span>

En utilisant une liste HTML et en la stylisant avec CSS, créez le rendu suivant :

<img src="../assets/exo3.3.png" style="margin-left:0;"/>

<div class="w-100 border rounded d-block mb-3" style="height: 400px;"></div>

<!--
Réponse :
<ul>
    <li class="d-inline rounded p-2 m-1 text-white bg-danger">Rouge</li>
    <li class="d-inline rounded p-2 m-1 text-white bg-success">Vert</li>
    <li class="d-inline rounded p-2 m-1 text-white bg-primary">Bleu</li>
</ul>
-->