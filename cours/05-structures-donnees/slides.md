---
marp: true
title: "Algorithmique Appliquée - Structures de données"
description: "Cours d'Algorithmique Appliquée avec Python"
author: "Loïc Yvonnet"
keywords: "Algorithmique, Algorithme, Python, Introduction, Débutant"
lang: "fr"
url: "https://loic-yvonnet.github.io/algo-appliquee/05-structures-donnees/"
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

## Structures de données fondamentales en Python

---

# Plan

- Notion de conteneur
- Notion d'opérations CRUD
- Tuples
- Ranges
- Lists
- Clonage et copie profonde
- Sets
- Dictionaries
- Technique "Pythonic": comprehensions
- Structure personnalisée

---

<!-- _class: title-section -->

# <!--fit--> Correction du travail à la maison

---

### DM : Retours sur les fonctions et le débogage

[**Lien** vers le sujet de DM](../03-programmes-simples/dm-02.html).

---

<!-- _class: title-section -->

# <!--fit--> Notion de conteneur

##### Container :uk:

---

# Types utilisés jusqu'à présent

- `int` : nombre entier.
- `float` : nombre flottant.
- `str` : chaîne de caractères.


---

# Conteneur de caractères

![bg right:45% 90%](./assets/conteneur-caracteres.png)

Une chaîne de caractères est un **conteneur de caractères**.

```python
chaine = "Bonjour"
```

---

# Conteneur d'entiers

![bg right:45% 90%](./assets/conteneur-entiers.png)

On voudrait aussi pouvoir manipuler des conteneurs d'entiers.

---

# Conteneur de flottants

![bg right:45% 90%](./assets/conteneur-flottants.png)

On voudrait aussi pouvoir manipuler des conteneurs de nombres flottants.

---

# Tableaux à 2 dimensions

![bg right:45% 90%](./assets/tableau-2-dimensions.png)

On voudrait aussi pouvoir manipuler des tableaux à 2, 3, N dimensions.

---

# Données hétérogènes

![bg right:45% 90%](./assets/heterogene.png)

On voudrait aussi pouvoir manipuler des données hétérogènes.

---

# Collections

* Les conteneurs sont également appelés **collections**.
* Leur propriété principale est d'être **itérable**.
* Cela signifie que l'on peut itérer sur chaque élément de la collection.

---

# Différents conteneurs

- Il existe différents types de conteneurs, pour répondre à différents besoins.
- Nous allons étudier les principes offerts en Python.
- Avant cela, nous allons étudier les principales opérations sur les conteneurs.

---

<!-- _class: title-section -->

# <!--fit--> Notion d'opérations CRUD 

##### **C**reate, **R**ead, **U**pdate, **D**elete :uk:

---

# Opérations de base

* **Création** : Création d'un nouveau conteneur.
* **Lecture** : Lecture de tout ou parti du contenu du conteneur.
* **Mise à Jour** :
    * Modification d'une valeur.
    * Insertion d'une valeur.
    * Suppression d'une valeur.
* **Suppression** : Suppression du conteneur.

---

# Création

```python
chaine = "nouvelle chaine"
```

---

# Lecture

```python
for i in range(len(chaine)):
    print(chaine[i])

print(type(chaine))

i = chaine.find("c")
print(i)
```

<!--
Toute opération non destructive est une lecture.
-->

---

# Mise à jour

```python
nouvelle_chaine = chaine.replace("nouvelle", "nouveau")
print(chaine)
print(nouvelle_chaine)
```

:arrow_down:

```
nouvelle chaine
nouveau chaine
```

On ne peut pas modifier une chaîne de caractères.

La mise à jour est impossible.

<!--
Cette impossibilité est une caractéristique intéressante.
Elle est voulue.
Nous allons y revenir très prochainement.
-->

---

# Suppression

```python
chaine = None
```

<!--
On ne peut pas vraiment forcer la suppression d'un objet en Python.
Il s'agit d'un langage dit "managé".
Cela signifie que la fin du cycle de vie d'un objet est géré par l'interpréteur.
En pratique, il existe un processus particulier nommé garbage collector (collecteur de déchets) dont le rôle est de libérer la mémoire des objets qui ne sont pas utilisés.
Une fois que la chaine est mise à None, les caractères ne sont plus référencés, et la mémoire associée sera donc libérée par le garbage collector à son prochain passage.
-->

---

# Immutabilité

* La **mutabilité** est la capacité à mettre à jour un objet.
* Cela signifie qu'il est possible de modifier sa valeur, d'insérer des éléments, ou d'en supprimer.
* L'**immutabilité** est donc l'impossibilité à mettre à jour un objet.

---

# `str` est immutable

```python
chaine = "oui"
chaine = "non"
```

Dans l'exemple ci-dessus, à la 2e ligne, on lie une nouvelle chaîne de caractères `"non"` à la variable `chaine`.

<!--
La chaîne "oui" reste inchangée.
Cette chaîne n'est tout simplement plus référencée par la variable chaine.
-->

---

<!-- _class: title-section -->

# Tuples

---

# Notion de tuple

* Comme les chaînes de caractères, les **tuples** sont des séquences ordonnées immutables d'éléments.
* La différence est que les éléments d'un tuple n'ont pas à être des caractères.
* Les éléments individuels peuvent être de **n'importe quel type**.
* Ils peuvent même être de **types différents**.

---

# Création

```python
tuple1 = () # le tuple vide
print(tuple1)

tuple2 = (1, "deux", 3.14)
print(tuple2)

tuple3 = tuple(range(3))
print(tuple3)
```

:arrow_down:

```
()
(1, 'deux', 3.14)
(0, 1, 2)
```

---

# Valeur répétée

```python
t = (1, 1, 1, 1, 1, 1)
print(t)
```

:arrow_down:

```
(1, 1, 1, 1, 1, 1)
```

---

# Ordre conservé

```python
t = (5, 4, 3, 2, 1, 0)
print(t)
```

:arrow_down:

```
(5, 4, 3, 2, 1, 0)
```

---

# Création d'un tuple à 1 élément

```python
t = (1,)
print(t)
```

:arrow_down:

```
(1,)
```

<!--
La syntaxe (1) est déjà réservée pour le nombre entier 1 entre paranthèses.
Il ne peut pas y avoir 2 sémantiques associées à la même syntaxe dans le même contexte.
Donc, il fallait une syntaxe différente. Cette syntaxe consiste à avoir une virgule supplémentaire à la fin.
-->

---

# Tuple imbriqué

```python
t = (1, ("deux", "trois"), 3.14)
print(t)
```

:arrow_down:

```
(1, ("deux", "trois"), 3.14)
```

---

# Itération sur un tuple (1/2)

```python
t = (1, 2, 3.14)
for i in range(len(t)):
    print(t[i])
```

:arrow_down:

```
1
2
3.14
```

---

# Itération sur un tuple (2/2)

```python
for element in (1, 2, 3.14):
    print(element)
```

:arrow_down:

```
1
2
3.14
```

---

# Slicing

```python
t = (0, 1, 2, 3, 4, 5, 6, 7)
t2 = t[1:6:2]
print(t2)
```

:arrow_down:

```
(1, 3, 5)
```

---

<!-- _class: title-section -->

# <!--fit--> Bornes et itérateurs

##### Ranges & iterables :uk:

---

# Range

```python
print(range(10))
```

:arrow_down:

```
range(0, 10)
```

<!--
La fonction range renvoie un objet range.
Cet objet n'est pas un conteneur.
Il ne renvoie donc pas directement les valeurs 0 à 9 dans cet exemple.
-->

---

# Comparaison de ranges

```python
r1 = range(10)
r2 = range(0, 10, 2)
r3 = range(0, 9, 2)

similaires = (r1 == r2)
print(similaires) # False

similaires = (r2 == r3)
print(similaires) # True
```

<!--
Dans le second cas, les mêmes valeurs sont renvoyées par les ranges.
0, 2, 4, 6, 8
-->

---

# Itérateur

* Tous les types **itérables** ont une méthode nommée `__iter__`.
* La méthode `__iter__` renvoie un **objet itérable**.
* Cet objet itérable est utilisé dans les boucles `for`.
* A chaque itération, le prochain élément de la séquence est renvoyée.
* Un `range` est itérable.

---

# Evaluation paresseuse

### Lazy evaluation :uk:

* La séquence complète d'un `range` n'est jamais construite intégralement.
* A la place, on conserve uniquement les bornes et l'élément actuel.
* On reste ainsi capable de renvoyer toujours le prochain élément.
* Cette optimisation s'appelle l'**évaluation paresseuse**.

---

# <!--fit--> Intérêt de l'évaluation paresseuse (1/2)

```python
import time

depart = time.process_time()

for i in range(1000000000):
    if i == 300:
        break

fin = time.process_time()
temps = fin - depart
print(f"{temps:.6f}s")
```

:arrow_down:

```
0.000064s
```

<!--
Il n'a pas été nécessaire de construire un ensemble d'un milliard d'éléments.
Par conséquent, l'exécution est instantannée.
-->

---

# <!--fit--> Intérêt de l'évaluation paresseuse (2/2)

```python
import time

depart = time.process_time()

for i in tuple(range(1000000000)): # tuple ajouté ici
    if i == 300:
        break

fin = time.process_time()
temps = fin - depart
print(f"{temps:.6f}s")
```

:arrow_down:

```
60.011151s
```

<!--
Simplement en rajoutant le mot clé tuple, il faut maintenant 1 minute pour exécuter ce code sur une station de travail avec un CPU i9 à 4.5GHz.
L'ajout de ce mot clé force l'interpréteur à créer un tuple contenant 1 milliard d'éléments, même si on ne regarde que les 300 premiers.
On parle ici d'évaluation gourmande (greedy evaluation), qui est l'inverse de l'évaluation paresseuse.
-->

---

# Immutable et ordonné

* Par nature, un `range` est immutable.
* Par nature, un `range` conserve son ordre initial.

---

<!-- _class: title-section -->

# Listes

---

# Notion de liste

* Comme les tuples, les **listes** sont une séquence ordonnée de valeurs, où chaque valeur peut être identifiée par un index.
* Une liste, contrairement à un tuple, est **mutable**.
* La liste, notée `list`, est très utilisée en Python.

---

# Création

```python
liste1 = [] # la liste vide
print(liste1)

liste2 = [1, "deux", 3.14]
print(liste2)

liste3 = list(range(3))
print(liste3)
```

:arrow_down:

```
[]
[1, 'deux', 3.14]
[0, 1, 2]
```

---

# Valeur répétée

```python
liste = [1, 1, 1, 1, 1, 1]
print(liste)
```

:arrow_down:

```
[1, 1, 1, 1, 1, 1]
```

---

# Ordre conservé

```python
liste = [5, 4, 3, 2, 1, 0]
print(liste)
```

:arrow_down:

```
[5, 4, 3, 2, 1, 0]
```

---

# Création d'une liste à 1 élément

```python
liste = [1]
print(liste)
```

:arrow_down:

```
[1]
```

---

# Liste imbriquée

```python
liste = [1, ["deux", "trois"], 3.14]
print(liste)
```

:arrow_down:

```
[1, ["deux", "trois"], 3.14]
```

---

# Itération d'une liste (1/2)

```python
liste = [1, 2, 3.14]
for i in range(len(liste)):
    print(liste[i])
```

:arrow_down:

```
1
2
3.14
```

---

# Itération d'une liste (2/2)

```python
for element in [1, 2, 3.14]:
    print(element)
```

:arrow_down:

```
1
2
3.14
```

---

# Slicing

```python
liste = [0, 1, 2, 3, 4, 5, 6, 7]
liste2 = liste[1:6:2]
print(liste2)
```

:arrow_down:

```
[1, 3, 5]
```

---

# Liste de tuples

```python
liste = [(1, 2), (3, 4)]
print(liste)
```

:arrow_down:

```
[(1, 2), (3, 4)]
```

---

# Tuple de listes

```python
t = ([1, 2], [3, 4])
print(liste)
```

:arrow_down:

```
([1, 2], [3, 4])
```

---

# Liste à 2 dimensions

```python
liste = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]
```

---

# Liste à 3 dimensions

```python
liste = [
    [
        [1, 0],
        [0, 1]
    ],
    [
        [1, 0],
        [0, 1]
    ]
]
```

---

# Modification d'une valeur

```python
liste = [1, 2, 3]
liste[0] = 5
print(liste)
```

:arrow_down:

```
[5, 2, 3]
```

---

# <!--fit--> Insertion d'une valeur au début

```python
liste = [1, 2, 3]
liste.insert(0, 42)
print(liste)
```

:arrow_down:

```
[42, 1, 2, 3]
```

---

# <!--fit--> Insertion d'une valeur au milieu

```python
liste = [1, 2, 3]
liste.insert(2, 42)
print(liste)
```

:arrow_down:

```
[1, 2, 42, 3]
```

---

# <!--fit--> Insertion d'une valeur à la fin

```python
liste = [1, 2, 3]
liste.append(42)
print(liste)
```

:arrow_down:

```
[1, 2, 3, 42]
```

---

# Suppression d'une valeur

```python
liste = [1, 2, 3]
liste.remove(liste[0])
print(liste)
```

:arrow_down:

```
[2, 3]
```

---

# <!--fit--> Suppression de la dernière valeur

```python
liste = [1, 2, 3]
liste.pop()
print(liste)
```

:arrow_down:

```
[1, 2]
```

---

<!-- _class: title-section -->

# TD : Implémenter les opérations matricielles les plus classiques

---

### TD : Opérations matricielles classiques

[**Lien** vers le sujet de TD](./td-03-op-matricielles.html).


---

<!-- _class: title-section -->

# <!--fit--> Clonage et copie profonde

##### Shallow and deep copy :uk:

---

# Le problème

```python
liste1 = [1, 2, 3]
liste2 = liste1

liste2.append(4)
print(liste1)
```

:arrow_down:

```
[1, 2, 3, 4]
```

<!--
Le fait de modifier la 2e liste modifie également la 1ière.
Est-ce surprenant ?
Pas vraiment, la variable liste1 est liée à la liste [1, 2, 3].
Ensuite, on lie la variable liste2 à la même liste [1, 2, 3].
Donc, les variables liste1 et liste2 référencent la même liste.
-->

---

# Impact imbriqué

```python
def f(liste):
    liste.append(4)

liste1 = [1, 2, 3]
f(liste1)
print(liste1)
```

:arrow_down:

```
[1, 2, 3, 4]
```

<!--
Il s'agit exactement du même cas que dans la diapositive précédente.
Même si le passage des variables se fait par valeur en Python, l'argument liste se voit lié à la même liste que la variable liste1.
Par conséquent, la modification de la liste dans la fonction impacte la variable liste1.
Parfois, c'est ce que l'on veut, parfois, non.
-->

---

# Egalité de listes

```python
liste1 = [1, 2, 3]
liste2 = [1, 2, 3]

egaux = (liste1 == liste2)
print(egaux)
```

:arrow_down:

```
[1, 2, 3, 4]
```

<!--
Deux listes sont égales si elles possèdent le même nombre d'éléments et si chacun d'entre eux sont égaux 2 à 2.
Cela n'aide pas à savoir si les 2 variables liste1 et liste2 référencent la même liste.
-->

---

# <!--fit--> Egalité d'objets : opérateur `is`

```python
liste1 = [1, 2, 3]
liste2 = [1, 2, 3]
liste3 = liste2

egaux = (liste1 is liste2)
print(egaux) # False

egaux = (liste2 is liste3)
print(egaux) # True
```

<!--
L'opérateur is permet de déterminer avec certitudes sur 2 variables référencent le même objet.
On sait ainsi si la modification de l'une des variables va entrainer la modification de l'autre.
-->

---

# Clonage (1/2)

```python
liste1 = [1, 2, 3]
liste2 = liste1.copy()
liste2.append(4)
print(liste1)
```

:arrow_down:

```
[1, 2, 3]
```

<!--
Dans ce cas, le clonage nous a permi de créer très facilement un clone indépendant de l'original.
Donc maintenant, lorsque l'on modifie la variable liste2, liste1 reste inchangée.
-->

---

# Clonage (2/2)

```python
liste1 = [1, 2, 3]
liste2 = liste1[:]
liste2.append(4)
print(liste1)
```

:arrow_down:

```
[1, 2, 3]
```

<!--
Il s'agit de la même technique. Seule la syntaxe change.
Il est important de comprendre cette syntaxe car elle est souvent utilisée.
On utilise l'opérateur de slicing pour renvoyer une nouvelle liste.
Cette nouvelle liste va du début à la fin de la liste actuelle, car on utilise les valeurs par défaut.
En effet, lorsque l'on ne spécifie pas la valeur avant le ":", c'est 0.
De même, lorsque l'on ne spécifie pas la valeur après le ":", c'est len(liste).
-->

---

# Limites du clonage

```python
liste1 = [[1, 2], [3, 4]]
liste2 = liste1[:]
liste2[0][0] = 5
print(liste1)
```

:arrow_down:

```
[[5, 2], [3, 4]]
```

<!--
Un clonage effectue une copie uniquement au premier niveau.
Par conséquent, les sous-listes de liste1 sont toujours référencées dans liste2.
La diapositive suivante clarifie les étapes.
-->

---

<!-- Etapes de clonage -->

![bg 80%](./assets/copie-profonde-1.png)

![bg 80%](./assets/copie-profonde-2.png)

![bg 80%](./assets/copie-profonde-3.png)

---

# Copie profonde

```python
import copy

liste1 = [[1, 2], [3, 4]]
liste2 = copy.deepcopy(liste1)
liste2[0][0] = 5
print(liste1)
```

:arrow_down:

```
[[1, 2], [3, 4]]
```

<!--
La copie profonde permet de dupliquer l'ensemble de la structure, quelque soit sa profondeur.
Ainsi, on a maintenant liste1 et liste2 qui sont liés à des structures totalement différentes.
-->

---

<!-- _class: title-section -->

# Ensembles

##### Sets :uk:

---

Notation
Mutable
Eléments uniques
Pas dans l'ordre d'insertion
Requis lorsque l'on a besoin de garantir l'unicité de chaque élément du conteneur

---

<!-- _class: title-section -->

# Dictionnaires

##### Dictionaries :uk:

---

Notation
Mutable
Dans l'ordre d'insertion depuis Python 3.8
Utilisé très souvent
Clés uniques
Parcours des éléments
Parcours des clés uniquement ou des valeurs uniquement

---

<!-- _class: title-section -->

# <!--fit--> Technique "Pythonic": comprehensions

---

@TODO : vérifier comment on dit en français!!
Exemple simple avec liste
Exemple avec liste + condition
Exemple imbriqué
Warning : ne pas faire de choses trop compliquées => les boucles classiques sont plus simples à comprendre!
Exemple avec tuple
Exemple avec set
Exemple**s** avec dico

---

<!-- _class: title-section -->

# TP : Utiliser un dictionnaire pour gérer un hôpital avec des patients, des médecins et des soins àapporter

---

### TP : Gestion d'un hôpital

[**Lien** vers le sujet de TP](./tp-08-gestion-hosto.html).

---

<!-- _class: title-section -->

# Structure personnalisée

##### Notion de classe comme Tuple avancé

---

Avec les conteneurs vus jusqu'ici, on peut aller loin
Python nous permet de définir nos propres types d'objet
Comme un tuple, mais à la place d'accéder aux élements par index t[0], t[1], t[2], on peut faire t.x, t.y, t.z par exemple.
Fondamental pour définir des abstractions de niveau supérieur et simplifier la programmation
Mot clé `class`
La fonction spéciale __init__(self, ...)
La spécification de données membres
Usage

Shortcut en Python 3.7 :
```py
from dataclasses import dataclass

@dataclass
class Point:
    x: float = 0.
    y: float = 0.
    z: float = 0.
```

<!--
Notes : on ne parle pas de POO.
On montre juste l'équivalent d'une struct C, POD (C++), POJO (Java), POCO (C#), etc.
C'est dommage que l'on ne puisse pas plus facilement faire ça en Python !
-->
