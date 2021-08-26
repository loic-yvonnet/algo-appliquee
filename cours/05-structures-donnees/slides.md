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

##### Container

---

str = liste de caractères
On veut pouvoir manipuler des ensembles d'autres choses
=> Ce sont les conteneurs (également appelées collections)
Il existe différents types de conteneurs, pour répondre à différents besoins

---

<!-- _class: title-section -->

# <!--fit--> Notion d'opérations CRUD 

##### Create, Read, Update, Delete

---

Opérations de base
Création, Recherche/Lecture, Mise à Jour, Suppression
Insertion
Mutabilité
Recherche uniformisée quelque soit le conteneur

---

<!-- _class: title-section -->

# Tuples

---

Notation
Immutable
Contient généralement des types différents
Utilisé pour retourner plusieurs valeurs dans une fonction
Utilisé pour représenter un type customisé simple
Peut contenir plusieurs fois la même valeur
Ordre d'insertion conservé
Tuple à 1 élément (1,)
Tuple de tuples

---

<!-- _class: title-section -->

# <!--fit--> Bornes et itérateurs

##### Ranges & iterables

---

Retour sur la fonction range qui renvoie un objet range
Immutable
Peut être comparé
Peut être itéré
Léger en mémoire => lazy evaluation
Peut être utilisé partour où l'on attend un iterable d'entiers

---

<!-- _class: title-section -->

# Listes

---

Notation
Mutable
Le conteneur le plus utilisé en Python
Contient la plupart du temps des objets d'un unique type
Peut contenir des objets de types variés
Peut contenir plusieurs fois la même valeur
Ordre d'insertion conservé
Liste de listes
Liste à N dimensions
Liste de tuples
Tuple de listes

---

<!-- _class: title-section -->

# <!--fit--> TD : Implémenter les opérations matricielles les plus classiques

---

### TD : Opérations matricielles classiques

[**Lien** vers le sujet de TD](./td-03-op-matricielles.html).


---

<!-- _class: title-section -->

# <!--fit--> Clonage et copie profonde

##### Shallow and deep copy

---

Rabachage : tout est OBJET
Assignation d'une même liste à 2 variables et modification du contenu de la liste : les 2 variables sont affectées
Technique pour créer un clone : utiliser `[:]` ou `.copy()`.
Problème : les objets à l'intérieur de la liste restent les mêmes.
Technique pour créer une copie profonde : `copy.deepcopy()`.
Exemples

---

<!-- _class: title-section -->

# Ensembles

##### Sets

---

Notation
Mutable
Eléments uniques
Pas dans l'ordre d'insertion
Requis lorsque l'on a besoin de garantir l'unicité de chaque élément du conteneur

---

<!-- _class: title-section -->

# Dictionnaires

##### Dictionaries

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
