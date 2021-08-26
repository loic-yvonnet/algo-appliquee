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


<!-- On commence les choses sérieuses ! -->

---

# Plan

- Introduction à la technique "devine-et-vérifie"
- Introduction à la dichotomie
- Introduction à l'instrumentation de code
- Introduction à l'algorithme Newton Raphson
- Histoire des bugs et du debugging dans la culture anglo-saxonne
- Techniques pour déboguer manuellement un programme sur papier
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

Guess-and-Check

---

Problème des racines carrées.

---

<!-- _class: title-section -->

# <!--fit--> Introduction à la dichotomie

Bisection Search

---

Le juste prix (faire jouer les étudiants)
Puis le résoudre
Puis revenir sur les racines carrées.

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

Instrumentation à base de `print`s.
Intérêt => comprendre les problèmes.
Instrumentation avec des wallclocks.
Intérêt => amélioration des perfs + comparaison entre solutions
Mentionner rapidement que Python permet de faire de l'instrumentation de code automatique grâce à une notion avancée nommée annotation

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
