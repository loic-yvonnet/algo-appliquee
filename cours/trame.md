---
title: Trame du Cours
summary: Trame du cours d'Algorithmique Appliquée avec Python.
url: "{{ url_prefix }}/trame.html"
layout: layouts/site.njk
---

Chaque partie correspond à une demie-journée de cours, comportant chacune en moyenne 2 activités (TD/TP).

## Avant-Propos
* Organisation du cours.
* Évaluation.

## 1. Introduction à la programmation et à l’algorithmique
* Intérêt.
* Discussion sur les algorithmes.
* Une brève histoire de l’algorithmique.
* **TP** : Tutoriel pas-à-pas sur Scratch pour implémenter un jeu vidéo simple en rapport avec la ville de Saumur (manifestation Anjou vélo-vintage).
* Discussion sur les langages de programmation : compilation, interprétation et transpilation.
* Définition formelle de l’algorithmique.
* Introduction au langage Python : forces et faiblesses.
* Types numériques, expressions et objets en Python.
* Variables et assignation.
* **TP** : Utiliser Python dans Jupyter Notebook.

## 2. Les bases du langage Python
* Conditions.
* Chaînes de caractères et encodage de caractères.
* Entrée et sortie standard.
* **TP** : Utilisation d’un Environnement de Développement Intégré pour des traitements simples de chaînes de caractères.
* Boucles "Tant Que" (while).
* Boucles "Pour" (for) et "Bornes" (range).
* **TP** : Implémentation d’algorithmes mathématiques simples (ex : min, max, multiplication avec boucle d’additions, PGCD, nombre premier).
* Discussion sur les différences entre Scratch et Python.
* Retour sur le 1er TP : demander aux étudiants de l’expliquer avec leurs nouvelles connaissances.
* Discussion sur le style, les commentaires et PEP 8.

*Travail à la maison* :
* Reprendre le TP Scratch et aller plus loin : nouvelles fonctionnalités.
* Quelques exercices supplémentaires sur les chaînes de caractères.
* Quelques exercices supplémentaires sur le calcul numérique.

## 3. Programmes numériques simples et techniques de débogage

* Correction du travail à la maison.
* Introduction à la technique "devine-et-vérifie" (guess-and-check).
* Introduction à la dichotomie (bisection search).
* **TD** : Utilisation de la dichotomie pour calculer des racines et des logarithmes.
* Introduction à l'instrumentation de code.
* Introduction à l'algorithme Newton Raphson.
* **TP** : Comparaison d'algorithmes ayant le même objectif.
* Histoire des bugs et du debugging dans la culture anglo-saxonne.
* Techniques pour déboguer manuellement un programme sur papier.
* Utilisation d'un debugger avec points d'arrêt.
* **TP** : Déboguer un programme mal écrit et comportant des bugs.

## 4. Procédures et fonctions

* Procédures : définition et appel.
* Arguments.
* Valeurs par défaut.
* Variables locales et globales (scope).
* Fonctions.
* Spécifications et contrat.
* Modularisation de code et conventions avec la fonction main.
* **TD** : Ecrire des fonctions de calcul de périmètre, aire et volume selon les spécifications fournies.
* Nombre variable d'arguments
* Retour de plusieurs résultats.
* Un mot sur la récursivité.
* Fonctions lambda.
* Fonctions d'ordre supérieur : fonctions en tant qu'objets.
* Programmation impérative et programmation fonctionnelle : notions de pureté et d'immutabilité.
* Un mot sur les méthodes avec l'exemple du type `str`.
* **TP** : Ecrire une fonction générique résolvant une dichotomie entre 2 bornes grâce à une fonction d'évaluation.

*Travail à la maison* :
* Identifier et corriger les problèmes dans des programmes buggés et/ou mal écrits.
* Tri d'une chaîne de caractères avec un alphabet réduit.
* Dérivée d'un polynôme de degré N avec fonction variadique.
* Implémenter l'agorithme Fibonacci avec une boucle, et l'implémenter de manière récursive.

## 5. Structures de données fondamentales en Python

* Correction du travail à la maison.
* Tuples.
* Ranges.
* Lists.
* **TD** : Implémenter les opérations matricielles les plus classiques (addition, multiplication scalaire, calcul de déterminant, multiplication matricielle).
* Clonage et copie profonde (shallow & deep copy).
* Sets.
* Dictionaries.
* Technique "Pythonic": comprehensions.
* **TP** : Utiliser un dictionnaire pour gérer un hôpital avec des patients, des médecins et des soins à apporter.
* Structure personnalisée : notion de classe comme Tuple avancé.

## 6. Résolution de problèmes classiques

* Listes chaînées.
* CRUD (Create, Read, Update, Delete).
* **TP** : Manipulation d'une liste chaînée (création, insertion, suppression, recherche).
* Queue et FIFO (First-In, First-Out).
* Stack et LIFO (Last-In, First-Out).
* Comparaison entre FIFO et LIFO.
* **TP** : Production/consommateur avec une queue de messages simple.
* Rappels sur la théorie des ensembles : union, intersection, exclusion.
* Rappels sur le calcul matriciel avancé : diagonalisation, inversion, méthode de Gauss.

*Travail à la maison*:
* Echauffement : implémenter $\sum_{i=1}^{n} f(i)$ et $\prod_{i=1}^{n} f(i)$.
* Implémenter des fonctions de gestion d'ensemble avec des Sets (union, intersection, exclusion).
* Implémenter des fonctions de calcul matriciel avancées (diagonalisation, inversion, méthode de Gauss).

## 7. Introduction à la complexité d’algorithme

## 8. Tests, exceptions et assertions

## 9. Algorithmes de recherche et de tri

## 10. Code modulaire et « Pythonic »

## 11. Introduction aux graphes

## 12. Conclusion

