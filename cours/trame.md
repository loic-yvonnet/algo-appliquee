---
title: Trame du Cours
summary: Trame du cours d'Algorithmique Appliquée avec Python.
url: "{{ url_prefix }}/trame.html"
layout: layouts/site.njk
---

Chaque partie correspond à une demie-journée de cours, comportant chacune en moyenne 2 activités (TD/TP).

### Avant-Propos
* Organisation du cours.
* Évaluation.

### 1. Introduction à la programmation et à l’algorithmique
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

### 2. Les bases du langage Python
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

*Travail à la maison* : Retours sur Scratch et Python.

### 3. Programmes numériques simples et techniques de débogage

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

### 4. Procédures et fonctions

* Procédures : définition et appel.
* Arguments.
* Valeurs par défaut.
* Variables locales et globales (scope).
* Fonctions.
* Spécifications et contrat.
* Modularisation de code et conventions avec la fonction main.
* **TD** : Fonctions géométriques simples.
* Nombre variable d'arguments
* Retour de plusieurs résultats.
* Un mot sur la récursivité.
* Fonctions lambda.
* Fonctions d'ordre supérieur : fonctions en tant qu'objets.
* Programmation impérative et programmation fonctionnelle : notions de pureté et d'immutabilité.
* Un mot sur les méthodes avec l'exemple du type `str`.
* **TP** : Fonctions d'ordre supérieur.

*Travail à la maison* : Retours sur les fonctions et le débogage.

### 5. Structures de données fondamentales en Python

* Correction du travail à la maison.
* Notion de conteneur (container).
* Notion d'opérations CRUD (Create, Read, Update, Delete).
* Tuples.
* Ranges.
* Lists.
* **TD** : Opérations matricielles classiques.
* Clonage et copie profonde (shallow & deep copy).
* Sets.
* Dictionaries.
* Technique "Pythonic": comprehensions.
* **TP** : Gestion d'un hôpital.
* Structure personnalisée : notion de classe comme Tuple avancé.

### 6. Résolution de problèmes classiques

* Listes chaînées.
* **TP** : Manipulation d'une liste chaînée.
* Queue et FIFO (First-In, First-Out).
* Stack et LIFO (Last-In, First-Out).
* Comparaison entre FIFO et LIFO.
* **TP** : Queues de messages simple.
* Rappels sur la théorie des ensembles : union, intersection, exclusion.
* Rappels sur le calcul matriciel avancé : diagonalisation, inversion, méthode de Gauss.

*Travail à la maison* : Ensembles et calcul matriciel.

### 7. Introduction à la complexité d’algorithme

* Correction du travail à la maison.
* Intuition sur la complexité avec un exemple simple.
* Réflexion sur la complexité temporelle et spatiale.
* Notation $O(...)$.
* Classes de complexité : constante, logarithmique, linéaire, log-linéaire, polynomiale.
* Comparaison des classes de complexité.
* **TD** : Evaluation de compléxité.
* Problèmes NP-complet : intuition et exemple.
* Limites de l'étude de complexité : architecture matérielle moderne (CPU).
* Approche pragmatique : mesures et benchmarks.
* Discussion concernant la parallélisation sur CPU et GPU
* Discussion sur la distribution de calcul dans un cluster et sur le Cloud.
* Discussion sur les machines quantiques.
* **TP** : Benchmark et complexité.

### 8. Tests, exceptions et assertions

* Gestion d'erreurs avec des codes de retour.
* Notion d'exception.
* Gestion d'exceptions et classes d'exception.
* Programmation offensive et défensive.
* Assertions.
* Invariants : préconditions et post-conditions.
* **TP** : Exceptions dans une calculatrice.
* Tests et qualité logicielle : boîte opaque et équipe QA.
* Tests en boîte transparente par les développeurs.
* Automatisation des tests.
* Tests unitaires.
* Tests pilotant le développement (Test Driven Development).
* Pyramide de tests.
* **TP** : Ecriture de tests unitaires.

*Travail à la maison* : Retour sur la complexité et les tests.

### 9. Algorithmes de recherche et de tri

* Correction du travail à la maison.
* Retour sur les classes de problèmes usuelles en algorithmique.
* Recherche en Python (opérateur `in`).
* Recherche linéaire.
* Recherche binaire (binary search).
* **TP** : Recherche dans une collection.
* Tri en Python (`sort` et `sorted`).
* Algorithme de tri naïf : Bubble Sort.
* Partition : diviser et conquérir (divide-and-conquer).
* Quick Sort.
* Merge Sort.
* **TP** : Tri de collections.

### 10. Code modulaire et « Pythonic »

* Programmation modulaire : les modules.
* Tour d'horizon de la librairie standard Python.
* Focus sur les fichiers : ouverture, fermeture, lecture et écriture.
* **TP** : Ecrire dans un fichier le contenu d'un Dictionary et relire ce fichier pour repopuler un Dictionary.
* Introduction aux paquets et au gestionnaire de paquets `pip`.
* Discussion sur les licences : GPL, MIT, BSD, Apache, etc.
* **TP** : Utiliser MatPlotLib et random pour afficher l'évolution du temps d'exécution de Bubble Sort, Quick Sort et du `sort` de Python en fonction de la taille des entrées.
* Optionnel : Discussion sur la programmation orientée object.
* Optionnel : Discussion sur les coroutines et `async`.

*Travail à la maison* :
* Utiliser requests pour faire une requête HTTP sur DuckDuckGo et afficher la réponse (au format HTML).
* Lire un fichier CSV qui contient un tableau de points et afficher le contenu avec MatPlotLib.

### 11. Introduction aux graphes

* Correction du travail à la maison.
* Discussion sur les hiérarchies : exemples en entreprises, structure produits, compétitions, etc.
* Arbre binaire : représentation.
* Arbre N-aire : représentation.
* Insertion et recherche dans un arbre binaire.
* **TP** : Parcours d'un arbre binaire (récursif et itératif avec queue) pour application d'une fonction à chaque noeud et implémentation de tests unitaires.
* Discussion concernant les problèmes impliquant des graphes : GPS, réseaux sociaux, etc.
* Introduction à la théorie des graphes : noeud, arc, cycle, digraph.
* Digraph : représentation.
* Identification d'un cycle.
* Recherche en profondeur (Depth-First Search).
* Recherche en largeur (Breadth-First Search).
* Graphe pondéré : représentation.
* Recherche de chemin critique.
* **TP** : Implémentation de DFS sur un digraph acyclique.

### 12. Conclusion

* Retours sur les points essentiels et attendus pour l'examen.
* Conseils pour l'examen.
* Questions/réponses sur l'ensemble du cours.
* Discussion concernant le travail dans une base de code réelle.
* Retour sur la qualité logicielle et l'optimisation.
* Discussion concernant la recherche opérationnelle et l'algorithmique plus avancée.