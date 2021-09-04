---
marp: true
title: "Algorithmique Appliquée - Programmes simples"
description: "Cours d'Algorithmique Appliquée avec Python"
author: "Loïc Yvonnet"
keywords: "Algorithmique, Algorithme, Python, Introduction, Débutant"
lang: "fr"
url: "https://loic-yvonnet.github.io/algo-appliquee/03-programmes-simples/"
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

## Programmes numériques simples et techniques de débogage


<!--
On va commencer à réfléchir aux manières d'utiliser les outils vus précédemment pour construire des programmes simples.
On va également voir quelques techniques de programmation et de débogage.
-->

---

# Plan

- Introduction à la technique "devine-et-vérifie"
- Introduction à la dichotomie
- Introduction à l'instrumentation de code
- Introduction à l'algorithme Newton Raphson
- Histoire des bugs et du debugging
- Techniques pour déboguer manuellement
- Utilisation d'un debugger avec points d'arrêt

---

<!-- _class: title-section -->

# Correction du travail à la maison

---

### DM : Retours sur Scratch et Python

[**Lien** vers le sujet de DM](../02-bases-python/dm-01.html).

---

<!-- _class: title-section -->

# <!--fit--> Introduction à la technique "devine-et-vérifie"

##### Guess-and-Check

---

# Devine-et-vérifie

Nous souhaitons résoudre les problèmes suivants :
- Retrouver un nombre dans un interval,
- Déterminer si un nombre est premier,
- Calculer une racine carrée.

Nous allons aborder différentes techniques. La plus simple est "devine-et-vérifie".

---

# Retrouver un nombre dans un interval

```python
valeur_recherchee = int(input("Entrez un nombre entre 0 et 1 000 000 : "))

if valeur_recherchee < 0 or valeur_recherchee > 1000000:
    print("Erreur")
else:
    devine = 0
    while devine < valeur_recherchee:
        devine += 1
    print(devine)
```

<!--
On cherche simplement à retrouver le nombre rentré par l'utilisateur.
On énumère toutes les possibilité.
A chaque étape, on tente de deviner la valeur et on vérifie si c'est la bonne.
-->

---

# Nombre premier

```python
x = int(input("Entrez un nombre entier positif : "))

if x <= 2:
    print("Les nombres inférieurs ou égaux à 2 ne sont pas premiers")
else:
    diviseur = None
    for devine in range(2, x):
        if x % devine == 0:
            diviseur = devine
            break
    
    if diviseur != None:
        print(f"Le plus petit diviseur de {x} est {diviseur}.")
    else:
        print(f"{x} est un nombre premier")
```

<!--
On énumère à nouveau toutes les possibilités.
A chaque fois, on tente de deviner un diviseur possible et on vérifie le reste de la division.
Au final, si on a trouvé un diviseur, c'est que le nombre n'est pas premier.
-->

---

# Nombre premier (plus rapide)

```python
x = int(input("Entrez un nombre entier positif : "))

if x <= 2:
    print("Les nombres inférieurs ou égaux à 2 ne sont pas premiers")
elif x % 2 == 0:
    print(f"Le plus petit diviseur de {x} est 2.")
else:
    diviseur = None
    for devine in range(3, x, 2):
        if x % devine == 0:
            diviseur = devine
            break
    
    if diviseur != None:
        print(f"Le plus petit diviseur de {x} est {diviseur}.")
    else:
        print(f"{x} est un nombre premier")
```

<!--
Ce nouvel algorithme est plus complexe que le précédent pour résoudre le même problème.
Cela étant, cet algorithme est également plus efficace.
En effet, il tire parti du fait qu'un nombre sur 2 est pair, et que les nombres pairs ne sont pas premiers.
Par conséquent, cet algorithme teste 2x moins de nombres que le précédent.
C'est un compromis classique : complexité d'implémentation pour meilleure vitesse d'exécution.
-->

---

# Notion d'heuristique

On pourrait encore accélérer l'algorithme précédent avec des **heuristiques** supplémentaires.

Une heuristique est une astuce permettant de simplifier un problème.

Par exemple :
* on sait qu'un nombre dont le dernier chiffre est 5 est divisible par 5.
* on sait que si la somme des chiffres d'un nombre est divisible par 3, alors ce nombre est divisible par 3.
* on sait qu'il n'est pas nécessaire de tester les nombres supérieurs à $\sqrt{x}$.

Ainsi, on peut éliminer très rapidement les nombres divisibles par 2, 3 ou 5.

---

# Racine carrée

```python
x = int(input("Entrez un nombre entier positif : "))
devine = 0
while devine ** 2 < x:
    devine += 1

if devine ** 2 != x:
    print(f"{x} n'est pas un carré parfait")
else:
    print(f"La racine carrée de {x} est {devine}.")
```

<!--
Cet algorithme, encore du type "devine-et-vérifie" effectue une énumération exhaustive.
Cependant, elle est très limitée : on ne peut trouver que les carrés parfaits.
-->

---

# Racine carrée à petits pas

```python
x = int(input("Entrez un nombre entier positif : "))
devine = 0
pas = 0.0001
while devine ** 2 < x:
    devine += pas

erreur = abs(x - devine ** 2)
print(f"La racine carrée de {x} est {devine} à {erreur} près")
```

<!--
Cet algorithme naïf est inefficace et peu précis.
En effet, il effectue un nombre très important de tests.
Par ailleurs, la précision n'est pas garantie pour les grands nombres.
-->

---

# Limites de l'approche devine-et-vérifie

Cette approche est basée sur une **énumération exhaustive**.

Limites :
* Effectue un grand nombre de tests.
* Si le nombre recherché n'est pas énuméré, l'erreur n'est pas complètement maîtrisée.

D'autres approches existent.

---

<!-- _class: title-section -->

# <!--fit--> Introduction à la dichotomie

##### Bisection Search

---

# Le juste prix

Contexte et règles :
- Jeu télévisé des années 1990.
- Le présentateur demandait au joueur de trouver un prix entre 1 et 1000 francs.
- Le joueur propose un prix.
- Le présentateur dit si c'est supérieur, inférieur ou égal.
- Le joueur propose un nouveau prix, et le présentateur répond à nouveau.
- Le joueur a une minute pour trouver le juste prix.

<!--
Tirer au sort un édudiant et le faire jouer pour voir si elle utilise naturellement une énumération exhaustive ou une dichotomie.
Demandez ensuite aux autres étudiants ce qu'ils en pensent.
Faire éventuellement passer un autre étudiant si la première n'a pas trouvé le juste prix.
-->

---

# La dichotomie

On utilise le fait que l'espace de travail est **fini** et **totalement ordonné**.
A chaque étape, on divise l'espace de travail par 2, jusqu'à converger vers une solution satisfaisante.

--- 

# Retrouver un nombre dans un interval

```python
valeur_recherchee = int(input("Entrez un nombre entre 0 et 1 000 000 : "))

if valeur_recherchee < 0 or valeur_recherchee > 1000000:
    print("Erreur")
else:
    debut = 0
    fin = 1000000
    milieu = round((fin + debut) / 2)
    while milieu != valeur_recherchee:
        if milieu > valeur_recherchee:
            fin = milieu
        else:
            debut = milieu
        milieu = round((fin + debut) / 2)
    print(milieu)
```

<!--
L'interval est représenté par [début ; fin].
A chaque itération, on regarde si la valeur au milieu de l'interval est la bonne.
Si la valeur recherchée est plus petite que le milieu, l'interval devient [début ; milieu].
Sinon, l'interval devient [milieu ; fin].
Par conséquent, début et fin convergent rapidement vers la valeur recherchée.
-->

---

# Racine carrée

```python
x = int(input("Entrez un nombre positif : "))

debut = 0
fin = max(1, x)
milieu = (fin + debut) / 2
epsilon = 0.0001

while abs(milieu ** 2 - x) >= epsilon:
    if milieu ** 2 > x:
        fin = milieu
    else:
        debut = milieu
    milieu = (fin + debut) / 2

erreur = abs(milieu ** 2 - x)
print(f"La racine carrée de {x} est {milieu} à {erreur} près")
```

<!--
On travaille dans l'interval [0 ; x] si x > 1 ou dans [0 ; 1] si 0 < x < 1.
A chaque itération, on regarde si la valeur au milieu de l'interval est proche de la valeur souhaitée, à un epsilon près.
Si la valeur recherchée est plus petite que le milieu, l'interval devient [début ; milieu].
Sinon, l'interval devient [milieu ; fin].
Par conséquent, début et fin convergent rapidement vers la valeur recherchée.
Cet algorithme basé sur la dichotomie converge beaucoup plus rapidement que la version avec énumération exhaustive.
De plus, on contrôle mieux l'erreur grâce à un epsilon indépendant du pas d'itération.
-->

---

# Comparaison entre dichotomie et énumération exhaustive

Intuitivement, pour les 3 problèmes qui nous préoccupent :
* Retrouver un nombre dans un interval : la dichotomie gagne.
* Déterminer si un nombre est premier : l'énumération exhaustive gagne.
* Calculer une racine carrée : la dichotomie gagne.

S'il est nécessaire de tester toutes les valeurs, la dichotomie n'apporte rien.

<!--
Dans le cas des nombres premiers, il est de toutes façons nécessaires de tester toutes les valeurs.
-->

---

<!-- _class: title-section -->

# TD : Utilisation de la dichotomie pour calculer des racines et des logarithmes

---

### TD : Dichotomie pour Racines et Logarithmes

[**Lien** vers le sujet de TD](./td-01-dichotomie.html).

---

<!-- _class: title-section -->

# <!--fit--> Introduction à l'instrumentation de code

---

# Pourquoi instrumenter le code

* Nous avons vu que différents algorithmes permettent de résoudre un même problème.
* Nous avons tenté de comparer ces algorithmes en utilisant notre intuition.
* L'intuition est utile mais pas très *mathématiques*.
* On souhaite effectuer des **mesures** et **obserser l'exécution**.

---

# Instrumentation

L'instrumentation consiste à rajouter du code :
* pour observer l'exécution avec des `print`.
* pour mesurer des indicateurs comme le nombre d'itérations effectuées.
* pour comprendre les problèmes, lorsqu'il y en a.

Ces ajouts **ne modifient pas** l'algorithme instrumenté. Il s'agit **d'instruments de mesure**.

---

# Observation de valeurs en cour d'exécution

```python
x = int(input("Entrez un nombre positif : "))

debut = 0
fin = max(1, x)
milieu = (fin + debut) / 2
epsilon = 0.0001

while abs(milieu ** 2 - x) >= epsilon:
    print(milieu) # On affiche ici la valeur
    if milieu ** 2 > x:
        fin = milieu
    else:
        debut = milieu
    milieu = (fin + debut) / 2

erreur = abs(milieu ** 2 - x)
print(f"La racine carrée de {x} est {milieu} à {erreur} près")
```
<!--
Dans la version finale de l'algorithme, on souhaitera retirer cette instrumentation.
En effet, l'utilisateur final de l'algorightme ne souhaite pas voir les étapes intermédiaires.
En revanche, pour comprendre un algorithme, il est utile de l'instrumenter de cette manière.
-->

---

# Comptage du nombre d'itérations

```python
x = int(input("Entrez un nombre positif : "))

debut = 0
fin = max(1, x)
milieu = (fin + debut) / 2
epsilon = 0.0001

compteur = 0

while abs(milieu ** 2 - x) >= epsilon:
    compteur += 1 # On incrémente le compteur d'itérations
    if milieu ** 2 > x:
        fin = milieu
    else:
        debut = milieu
    milieu = (fin + debut) / 2

erreur = abs(milieu ** 2 - x)
print(f"La racine carrée de {x} est {milieu} à {erreur} près")
print(f"Nombre d'itérations : {compteur}") # on l'affiche
```

<!--
Compter le nombre d'itérations permet de comparer 2 algorithmes ayant le même objectif.
L'algorithme qui parvient au résultat en un nombre d'itérations minimum est meilleur.
-->

---

# Chronométrage de l'exécution
```python
import time

x = int(input("Entrez un nombre positif : "))

chrono_debut = time.process_time() # démarrage du chronomètre

debut = 0
fin = max(1, x)
milieu = (fin + debut) / 2
epsilon = 0.0001

while abs(milieu ** 2 - x) >= epsilon:
    if milieu ** 2 > x:
        fin = milieu
    else:
        debut = milieu
    milieu = (fin + debut) / 2

chrono_fin = time.process_time()         # arrêt du chronomètre
temps_ecoule = chrono_fin - chrono_debut # calcul du temps écoulé

erreur = abs(milieu ** 2 - x)
print(f"La racine carrée de {x} est {milieu} à {erreur} près")
print(f"Temps d'exécution : {temps_ecoule}s") # on l'affiche
```

<!--
En plus du nombre d'itérations, avoir le temps d'exécution permet également de comparer des algorithmes.
Il est à noter que cette manière de mesurer est naïve.
Il existe des approches plus robustes pour mesurer un temps d'exécution.
Néanmoins, cette technique offre un moyen rapide de se faire une idée.
-->

---

# Benchmark

* La comparaison du temps d'exécution de 2 algorithmes s'appelle un **benchmark**.
* Les processus s'exécutant sur un système d'exploitation sont en compétition pour les ressources de la machine.
* Les mesures effectuées avec `time.process_time` ne sont pas précises car elles sont impactées par les autres processus s'exécutant sur la machine.
* Si un processus gourmant en ressources (tel qu'un jeu vidéo) est exécuté en même temps, la mesure peut être fortement impactée.
* Lorsque l'on souhaite être précis, il faut que les mesures soient indépendantes des autres processus.
* Dans les prochains cours et TPs, nous verrons des méthodes plus précises.


---

<!-- _class: title-section -->

# <!--fit--> Introduction à l'algorithme Newton Raphson

---

Présentation d'une meilleure solution pour calculer des racines carrées.

---

<!-- _class: title-section -->

# TP : Comparaison d'algorithmes ayant le même objectif

---

### TP : Comparaison d'Algorithmes

[**Lien** vers le sujet de TP](./tp-05-comparaison-algo.html).

---

<!-- _class: title-section -->

# <!--fit--> Histoire des bugs et du debugging dans la culture anglo-saxonne

---

Le mythe de l'insecte dans la machine
Les vraies origines
Rappel du Halting Problem et rabachage sur la qualité logicielle

---

<!-- _class: title-section -->

# <!--fit--> Techniques pour déboguer manuellement un programme sur papier

---

Tu prends un papier, tu prends un crayon, tu dessines un tableau avec tes variables en colonnes et les itérations en ligne, pis tu regardes ce qui se passe.... Et boom => le bug saute aux yeux !

---

<!-- _class: title-section -->

# <!--fit--> Utilisation d'un debugger avec points d'arrêt

---

Démo dans VS Code des breakpoints, breakpoints conditionels, introspection de variables, etc.

---

<!-- _class: title-section -->

# TP : Déboguer un programme mal écrit et comportant des bugs

---

### TP : Débogage d'un programme mal écrit

[**Lien** vers le sujet de TP](./tp-06-debogage.html).
