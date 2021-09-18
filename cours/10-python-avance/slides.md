---
marp: true
title: "Algorithmique Appliquée - Python avancé"
description: "Cours d'Algorithmique Appliquée avec Python"
author: "Loïc Yvonnet"
keywords: "Algorithmique, Algorithme, Python, Introduction, Débutant"
lang: "fr"
url: "https://loic-yvonnet.github.io/algo-appliquee/10-python-avance/"
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

## Bibliothèques Python

<!--
Tout langage de programmation et toute technologie moderne est complexe et profond.
Les bibliothèques sont très importantes pour développer des logiciels au bon niveau d'abstraction.
Afin que vous puissiez être efficaces rapidement dans vos entreprises en alternance, il est important que vous connaissiez les principales bibliothèques offertes par le langage de programmation Python.
-->

---

# Plan

- Programmation modulaire
- Librairie standard
- Focus sur les fichiers
- Gestionnaire de paquets
- Discussion sur les licences

---

<!-- _class: title-section -->

# Programmation modulaire

---

## Taille d'une fonction

* Combien de **responsabilités** doit avoir une fonction ?
* 1 fonction :arrow_right: 1 responsabilité.
* En moyenne, une fonction doit faire entre **7 et 15 lignes**.
* Une fonction qui fait plus de 30 lignes doit être découpée en **plusieurs fonctions plus simples**.

<!--
Il s'agit ici d'ordres de grandeur et de bonnes pratiques.
Il ne s'agit pas d'une règle stricte.
Il faut se référer au context de travail et aux règles de codage de l'entreprise dans laquelle vous intervenez.
-->

---

### Exemples de responsabilités

* Effectuer un calcul (ex : racine carrée).
* Rechercher une valeur (ex : recherche binaire)
* Appliquer une transformation (ex : nombre textuel vers numérique).
* Afficher un résultat (ex : une matrice).

---

## Ne pas se répéter

* Lorsque l'on observe un **motif qui se répète** dans le code, il y a un problème.
* Ces répétitions sont le signe d'une **duplication de code**.
* A la place, il faut créer des fonctions et les appeler.
* Le processus de modification du code pour supprimer les duplications s'appelle la **refactorisation**.
* Il s'agit d'une bonne pratique du génie logiciel.

<!--
Par exemple, lorsque l'on a dupliqué plusieurs fois le code de la racine carrée pour calculer la racine de 16, puis pour calculer la somme d'une racine carrée et d'une racine cubique.
A la place, nous avons désormais une fonction racine carrée propre et réutilisable.
-->

---

### Notion de script modulaire

- On rassemble les fonctions de même nature dans un **script**.
- Par exemple, on peut avoir un script `racine.py` qui contient les fonctions `racine_carree` et `racine_cubique`.
- On pourrait avoir un autre script nommé `chaine_caracteres.py` qui contient des fonctions de manipulation de chaînes de caractères.

---

# Module

* Un **module** est un fichier `.py` contenant des définitions et des déclarations Python.
* Le script `racine.py` est donc un module.

---

### Module `racine.py`

| ![w:500](./assets/racine.py.jpg) | ![w:500](./assets/scripts-python.png) |
|:--------------------------------:|:-------------------------------------:|
|       Fichier `racine.py`        |        Explorateur de fichiers        |

---

## Utilisation d'un module

- On emploie le mot clé `import` pour utiliser une bibliothèque de fonctions.
- Par exemple, avec le module `racine.py` :
```python
import racine

cinq = racine.racine_carree(25)
print(cinq)

trois = racine.racine_cubique(27)
print(trois)
```

<!--
On voit ici que les fonctions sont préfixées par le nom du module.
Cela ressemble à un appel de méthode, comme quand on appelle sort sur une liste.
-->

---

### Autre exemple avec `math`

```python
import math

print(math.cos(0))
```

:arrow_down:

```
1.0
```

---

## Intérêt du préfixe

* Lorsque l'on importe un module, on doit employer `module.f()` pour appeler la fonction `f` définie dans `module.py`.
* On appelle ce préfixe une **qualification complète** (fully qualified :uk:).
* L'objectif est d'éviter la **collision de nom**.
* En effet, plusieurs modules peuvent définir une fonction `f`.

---

### Importer une fonction spécifique

```python
from racine import racine_carree

cinq = racine_carree(25)
print(cinq)
```

:arrow_down:

```
5.000000000016778
```

---

#### :warning: Les autres fonctions sont invisibles

```python
from racine import racine_carree

trois = racine_cubique(27)
print(trois)
```

:arrow_down:

```
NameError: name 'racine_cubique' is not defined
```

---

#### :warning: Le module aussi est invisible

```python
from racine import racine_carree

trois = racine.racine_cubique(27)
print(trois)
```

:arrow_down:

```
NameError: name 'racine' is not defined
```

---

### Tout importer ? :skull:

```python
from racine import *

cinq = racine_carree(25)
print(cinq)

trois = racine_cubique(27)
print(trois)
```

:arrow_down:

```
5.000000000016778
3.000000000000002
```

<!--
Il vaut mieux éviter cette approche.
La diapositive suivante explique pourquoi.
-->

---

### Inconvénients de tout importer

* On perd l'avantage de la **qualification complète**.
* On peut donc avoir des **collisions de noms**.
* Le code est également plus **difficle à comprendre** car on ne sait pas d'où viennent les fonctions utilisées.

<!--
Dans les exemples fournis, on sait d'où viennent les fonctions.
Imaginez maintenant une base de code de 1 million de lignes avec plusieurs centaines de modules.
-->

---

# Alias

```python
import racine as rcn

cinq = rcn.racine_carree(25)
print(cinq)

trois = rcn.racine_cubique(27)
print(trois)
```

:arrow_down:

```
5.000000000016778
3.000000000000002
```

<!--
Il s'agit là d'une bien meilleure alternative.
On n'a plus à tapper le nom complet du module donc le code est moins lourd.
En même temps, on ne perd pas la qualification complète des noms donc le code reste clair et propre.
-->

---

### Importer une liste d'objets

```python
from math import cos, sin, pi

print(cos(0))
print(cos(pi))
print(sin(0))
print(sin(pi))
```

:arrow_down:

```
1.0
-1.0
0.0
1.2246467991473532e-16
```

<!--
En Python, tout est objet.
-->

---

## La fonction principale (1/2)

- Lorsque l'on exécute un script en ligne de commande, l'interprêteur assigne la chaîne de caractère `"__main__"` à la variable globale `__name__`.
- Cela permet de distinguer le cas où un script est importé avec `import`, du cas où un script est exécuté indépendemment.

---

## La fonction principale (2/2)

```python
def main():
    # On peut par exemple tester le bon fonctionnement de 
    # racine_carree et racine_cubique ici.
    pass

if __name__ == "__main__":
    # Exécuté uniquement si le script est lancé en ligne de commande
    main()
```

---

<!-- _class: title-section -->

# <!--fit--> Tour d'horizon de la librairie standard Python

---

<!-- _class: title-section -->

# <!--fit--> Focus sur les fichiers

##### Ouverture, fermeture, lecture et écriture

---

<!-- _class: title-section -->

# TP : Initiation aux fichiers

---

### TP : Initiation aux fichiers

[**Lien** vers le sujet de TP](./tp-16-fichiers.html).

---

<!-- _class: title-section -->

# <!--fit--> Introduction aux paquets

##### Gestionnaire de paquets `pip`

---

<!-- _class: title-section -->

# <!--fit--> Discussion sur les licences

##### GPL, MIT, BSD, Apache, etc.

---

<!-- _class: title-section -->

# TP : Courbes et traitement d'images

---

### TP : Courbes et traitement d'images

[**Lien** vers le sujet de TP](./tp-17-courbes.html).

---

<!-- _class: title-section -->

# <!--fit--> Programmation Orientée Object

##### Optionnel (hors programme)

---

<!-- _class: title-section -->

# Devoir à la Maison 05

---

### DM : Plus de modules

[**Lien** vers le sujet de DM](./dm-05.html).
