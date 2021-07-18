---
marp: true
title: "Algorithmique Appliquée - Bases du Python"
description: "Cours d'Algorithmique Appliquée avec Python"
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

  section.smaller-text p, section.smaller-text pre {
    font-size: 0.6em;
  }
---

<!-- _class: title-section -->

# <!--fit--> Algorithmique Appliquée

##### BTS SIO SISR

## Les bases du langage Python

<!-- Faisons sifler les serpents ! -->

---

# Plan

* Conditions
* Chaînes de caractères et encodage de caractères
* Entrée et sortie standard
* Boucles "Tant Que"
* Boucles "Pour"
* Discussion sur les différences entre Scratch et Python
* Style, commentaires et PEP 8

---

<!-- _class: title-section -->

# Conditions

---

# Branche

* Un algorithme doit souvent prendre des **décisions**.
* En fonction de la valeur d'une **expression Booléenne**, l'interprêteur va suivre une **branche** ou une autre.

---

# <!--fit--> Exemple de branchement

![bg left:30% 80%](./assets/condition.png)

* On peut visualiser graphiquement les branches.
* Pseudo-code équivalent :

```
Si la valeur de l'expression Test renvoie Vrai:
    Exécute le Bloc de code 1
Sinon:
    Exécute le Bloc de code 2
```

* En anglais :
  * si :arrow_right: `if`
  * sinon :arrow_right: `else`


---

# Conditions en Python

* La forme de base est la suivante :

```py
if Test:
    Bloc de code 1
else:
    Bloc de code 2
```

* Attention aux `:` et à l'indentation.
* Attention à la casse : les mots clés sont en minuscule.

---

# Le `else` est facultatif

* Une condition peut prendre tout simplement la forme :

```py
if Test:
    Bloc de code # Exécuté si Test == True
```

---

# Quelques exemples

```py
texte = ""
taille = 175

if taille > 180:
    texte = "grand"
else:
    texte = "petit"

print(texte)
```

:arrow_right: `petit`

---

# Quelques exemples

```py
texte = "petit"
taille = 175

if taille > 180:
    texte = "grand"

print(texte)
```

:arrow_right: `petit`

---

<!-- _class: smaller-text -->

# `if` imbriqués

```py
texte = ""
taille = 175

if taille > 180:
    if taille > 200:
        texte = "très grand"
    else:
        texte = "grand"
else:
    if taille > 155:
        texte = "moyen"
    else:
        texte = "petit"

print(texte)
```

:arrow_right: `moyen`

---

---

<!-- _class: title-section -->

# <!--fit--> Chaînes de caractères et encodage de caractères

---

<!-- _class: title-section -->

# <!--fit--> Entrée et sortie standard

---

<!-- _class: title-section -->

# <!--fit--> TP 03 - Initiation aux Environnement de Développement Intégrés avec pour but de manipuler des chaînes de caractères

---

<!-- _class: title-section -->

# <!--fit--> Boucles "Tant que"

---

<!-- _class: title-section -->

# <!--fit--> Boucles "Pour" et "Bornes"

---

<!-- _class: title-section -->

# <!--fit--> TP 04 - Quelques algorithmes simples pour prendre en main les fondamentaux de l'algorithmique

---

<!-- _class: title-section -->

# <!--fit--> Différences entre Python et Scratch

---

Discussion sur les différences concernant les conditions

---

Discussion sur les différences concernant les boucles

---

Comment feriez-vous pour ré-implémenter le TP 01 Anjou Vélo Vintage en Python ?

---

<!-- _class: title-section -->

# <!--fit--> Style, commentaires et PEP 8

---

<!-- _class: title-section -->

# <!--fit--> Devoir à la Maison 01
