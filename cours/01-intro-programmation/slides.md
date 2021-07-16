---
marp: true
title: "Algorithmique Appliquée - Introduction"
description: "Cours d'Algorithmique Appliquée avec Python"
theme: uncover
paginate: true
_paginate: false
style: |
  section {
    background-image: url("https://raw.githubusercontent.com/loic-yvonnet/algo-appliquee/master/assets/bg_normal.jpg");
  }
---

![](#fff)
![bg](https://raw.githubusercontent.com/loic-yvonnet/algo-appliquee/master/assets/bg_title.jpg)


# <!--fit--> Algorithmique Appliquée

##### BTS SIO SISR

## Introduction à la programmation et à l'algorithmique

<!-- On commence les choses sérieuses ! -->

---

# Plan

* Intérêt du cours
* Discussion sur les algorithmes
* Histoire de l’algorithmique
* Définition formelle
* Architecture simplifiée d'un ordinateur
* Discussion sur les langages de programmation
* Introduction au langage Python
* Types numériques, expressions et objets en Python
* Variables et assignation

---

![](#fff)
![bg](https://raw.githubusercontent.com/loic-yvonnet/algo-appliquee/master/assets/bg_title.jpg)

# <!--fit--> Intérêt du cours

## :star: :star: :star: :star: :star:

<!-- Pourquoi venir en cours et écouter un prof quand on pourrait rester au chaud chez soi et jouer à des jeux vidéos ? -->

---

# :point_right: Intérêt de savoir programmer

Selon vous, à quoi sert de savoir programmer ?

<!--
On va commencer par une autre question :
A quoi pensez-vous que sert de savoir programmer ?
-->

---

# Quelques exemples

* Automatiser votre travail pour rentrer plus tôt chez vous le soir :alarm_clock:
* Ecrire une App révolutionnaire et devenir millionnaire :moneybag:
* Amuser vos amis avec vos propres jeux vidéos :space_invader:
* Simplifier la mise en relation de milliers de personnes :busts_in_silhouette:

<!--
Voici quelques exemples de cas où savoir programmer est utile...
-->

---

# Et l'algorithmique dans tout ça ? :astonished:

L'algorithmique est au :heart: de la programmation

<!--
Il s'agit d'une formalisation et d'un socle commun à toutes les technologies et langages de programmation.
Même s'il est possible de programmer sans une connaissance approfondie de l'algorithmique, son étude est capitale pour écrire des programmes performants et maintenables.
-->

---

# Qu'est-ce que je vais apprendre d'utile ? :neutral_face:

* Le socle de la programmation : l'**algorithmique** :computer:
* Un langage de programmation industriel : **Python** :snake:
* Les bases pour écrire un logiciel **robuste** :muscle:, **performant** :fire: et **maintenable** :+1:

---

# Euh... Attendez, j'ai choisi SISR, pas SLAM :angry:

* Ce cours fait bien parti de votre programme.
* De plus en plus d'entreprises s'organisent en mode **DevOps**.
* La capacité à **automatiser** des tâches est également capital dans votre futur métier.

<!--
Le mode de fonctionnement DevOps regroupe des experts en Opérations/Réseau avec des experts en développement logiciel : pour être efficace, ous devez comprendre les métiers de vos collaborateurs.
L'automatisation est la clé du succès de très nombreux projets car elle permet de gagner du temps, et de vérifier la qualité tout au long de l'avancement du projet.
-->

---

![](#fff)
![bg](https://raw.githubusercontent.com/loic-yvonnet/algo-appliquee/master/assets/bg_title.jpg)

# <!--fit--> Discussion sur les algorithmes

---

## :point_right: Auriez-vous des exemples d'algorithmes en tête ?

<!--
A ce stade, sans doute pas... Ou alors vous avez déjà lu des choses sur le sujet.
-->

---

## Exemple informel 1
#### Aller sur Internet :computer:

* Brancher l'ordinateur.
* Appuyer sur le bouton Power.
* Vérifier la connexion réseau.
* Cliquer sur l'icône du navigateur web.
* Entrer une URL.
* Tapper sur la touche *Entrée*.

<!--
Cet exemple illustre simplement une série d'instructions.
-->

---

## Exemple informel 2
#### Cuisine :cake:

* Prendre les ingrédients.
* Suivre les étapes de la recette.
* Mettre au four.
* Tant que ce n'est pas cuit, attendre.
* Sortir le plat du four.

<!--
Cet exemple illustre les concepts d'entrées (les ingrédients) et de sortie (le plat) d'un algorithme.
-->

---

## Exemple informel 3
#### Choisir le petit déjeuner :coffee:

* S'il reste du café:
  * Faire chauffer du café.
  * Prendre une tasse.
  * Verser le café.
* Sinon:
  * Prendre un paquet de céréales.
  * Prendre un bol.
  * Verser du lait.

<!--
Cet exemple illustre le concept de condition.
-->

---

## Exemple 4
#### Multiplication calculée avec une somme

*Mathématiques* : $x \times y = \sum_{0}^{y - 1} x$

:arrow_down:

*Python* :
```py
def multiplie(x, y):
    resultat = 0
    for _ in range(y):
        resultat += x  
    return resultat
```

<!--
Cet exemple est un petit spoiler de la suite du cours avec un vrai algorithme implémenté en Python et sa définition équivalente en mathématiques.
-->

---

## :point_right: A vous de trouver des idées

<!--
Après ces quelques exemples, les étudiants devraient pouvoir trouver quelques exemples supplémentaires.
Faire un tour de table ou demander aléatoirement à quelques étudiants.
-->

---

# Intuitions à ce stade... 

Un algorithme :
* a des **entrées** et des **sorties**,
* comporte une **suite d'instructions**,
* peut comporter des **conditions**,
* peut comporter des **répétitions** (boucles).

<!--
Aborder ces quelques exemples permet d'avoir une première intuition sur la nature exacte d'un algorithme.
-->

---


![](#fff)
![bg](https://raw.githubusercontent.com/loic-yvonnet/algo-appliquee/master/assets/bg_title.jpg)

# <!--fit--> Histoire de l'algorithmique

<!--
Avant d'approfondir la notion d'algorithme, on va parler un peu d'histoire...
-->

---

### :point_right: Selon vous, de quelle époque datent les premiers algorithmes ?

<!--
Sachant que l'informatique a vraiment commencé à prendre son essor vers les années 1980, et que les étudiants sont (probablement) des milléniums, il est probable qu'ils avancent des dates assez récentes.
C'est justement pour casser le plus rapidement possible cette vision que cette partie du cours présente une histoire rapide de l'algorithmique.
-->

---

# Babylone

* Les mathématiques Babyloniennes de l'ancienne Mésopotomie (actuellement l'Iraq) montrent les premiers algorithmes.
* Des premières tablettes d'argile Sumérienne trouvées près de Bagdad remontent à **2500 ans avant notre ère**.
* Ces algorithmes étaient utilisés pour prédire la date et le lieux de certains événements astronomiques.

<!--
Les GAFAM n'ont inventé ni la roue, ni l'eau chaude...
-->

---

# Egypte

* Les mathématiques de l'ancienne Egypte utilisaient également des algorithmes pour résoudre des problèmes arithmétiques.
* Certains papyrus, comme celui de Rhind, remontent à **1550 ans avant notre ère**. Ils cherchaient à calculer des volumes, des aires et à résoudre des problèmes géométriques... notamment en relation avec des pyramides !

---

# Grèce Antique

* On doit aux mathématiques Hellenistiques, qui remontent à **300 ans** avant notre ère, de nombreux algorithmes encore célèbres aujourd'hui.
* Deux exemples notables :
  * Le *Siève d'Eratosthenes* : permet de trouver tous les nombres premiers jusqu'à une certaine limite.
  * L'*algorithme d'Euclide* : permet de calculer le Plus Grand Commun Dénominateur (PGCD).

---

### Muhammad ibn Musa al-Khwarizmi

* Il était un mathématicien, astronome, géographe et professeur à la Maison de la Sagesse à Bagdad. Il a vécu au **9e siècle** de notre ère.
* Il était le mathématicien le plus lu au moyen-âge en Europe.
* Le mot "algorithme" vient de la **traduction du nom Al-Khwarizmi** d'abord en latin (Algorizmi) puis en ancien anglais (algorism). Ce mot avait alors une signification différente.

<!--
Il a notamment écrit un traité sur le système numéraire Hindou-Arabique qui a été traduit au 12e siècle en latin, ainsi qu'un livre sur l'algèbre.
-->

---

# Ada Loveplace

* La comtesse Ada Loveplace a vécu au milieu du **19e siècle** au Royaume-Uni.
* Elle a travaillé avec Charles Babbage sur des machines analytiques capables théoriquement d'exécuter n'importe quel algorithme.
* Ada est considérée comme pionière car elle a écrit les premiers algorithmiques dédiés à une exécution par un ordinateur.
* Un langage de programmation créé beaucoup à la fin du 20e siècle a été nommé Ada en sa mémoire.

---

# Alan Turing

* Ce mathématicien, informaticien, scientifique et philosophe a vécu au **début du 20e siècle**.
* Ce personnage est historique au-délà de la discipline de l'algorithmique puisqu'il a fortement contribué à la victoire contre les Nazis lors de la 2e guerre mondiale.
* L'une de ses contributions essentielles est la **Machine de Turing**, qui est le premier ordinateur généraliste (par rapport à des ordinateurs spécialisés commes les calculatrices).

<!--
C'est grâce à sa machine Enigma, capable de décrypter les messages des Nazis, que de nombreuses opérations ont pu être déjouées.
Pour l'anecdote, son décès tragique a inspiré le logo de l'entreprise Apple (C).
-->

---

# Donald Knuth

Ce professeur émérite en informatique de l'université de Stanford a contribué à la démocratisation de l'algorithmique au travers de ses ouvrages *The Art of Computer Programming*, sur lesquels il travaille toujours **aujourd'hui**.

---

### Anecdotes récentes

* Google s'est construit autour de l'algorithme *Map Reduce*, inventé par ses fondateurs.
* Bill Gates a indiqué que Microsoft recrute n'importe quelle personne qui comprend les ouvrages de Knuth.
* Les géants Américains (GAFAM) et Chinois (BATX) utilisent tous des algorithmes et recherchent tous les meilleurs candidats dans ce domaine.
* L'Intelligence Artificielle est simplement un ensemble d'algorithmes travaillant sur des données massives.

<!--
Quelques anecdotes récentes...
Etre bon en algorithmique, c'est la garantie d'un succès professionnel.
-->

---

![](#fff)
![bg](https://raw.githubusercontent.com/loic-yvonnet/algo-appliquee/master/assets/bg_title.jpg)

# <!--fit--> Définition formelle

---

Un algorithme est une liste **finie** d'instructions décrivant un ensemble de calculs qui, lorsqu'ils sont exécutés sur un ensemble d'entrées, va passer par une séquence d'états bien définis et finalement produire une sortie.

<!--
On insiste ici sur le fait que la liste d'instructions doit être finie. Une boucle infinie ou une récursion infinie ne constituent pas des algorithmes.
On note que cette définition n'implique pas nécessairement de déterminisme par rapport aux sorties. Un algorithme peut utiliser un générateur de nombres aléatoires et faire varier ses sorties pour des entrées constantes.
-->

---

![](#fff)
![bg](https://raw.githubusercontent.com/loic-yvonnet/algo-appliquee/master/assets/bg_title.jpg)

# <!--fit--> Architecture simplifiée d'un ordinateur

<!--
A partir de maintenant, on va s'intéresser uniquement à la classe des algorithmes qui s'exécutent sur une machine.
Nous allons donc nous intéresser au fonctionnement d'un ordinateur.
-->

---

# Un champ limité d'actions

Un ordinateur ne sait faire que 2 choses :
* Faire des calculs,
* Se souvenir du résultat de ces calculs.

<!--
Par ailleurs, un ordinateur ne sait faire que ce qu'on lui dit.
L'Intelligence Artificielle ne change rien à cela.
-->

---

# Mise en perspective

Un simple ordinateur de bureau standard sait :
* Faire beaucoup de calculs très rapidement : des **centaines de milliards de calculs par seconde**.
* Se souvenir qu'une quantité remarquable de données : 1 téraoctet (To), c'est **1 000 000 000 000 octets**. Changez l'unité en kilogrammes ou mètres...

<!--
Un ordinateur sait donc faire ces 2 choses extrèmement bien.
A tel point qu'il peut vous tromper en vous donnant l'impression d'intelligence.
Mais la seule intelligence est celle des scientifiques, ingénieurs et développeurs qui ont travaillé dessus.
-->

---

# <!--fit--> Champ encore plus limité avant

Les premières machines étaient à **programme fixe** :
* Une calculatrice avec les opérations $+$, $-$, $\times$, $\div$.
* Un calculateur de trajectoire de missiles.
* Un solveur de système d'équations linéaires.
* Etc.

Les systèmes embarqués utilisent encore ce procédé pour des raisons de coût et de performance.

<!--
Cela signifie qu'ils ne savaient résoudre qu'un unique type de problème.
Concernant les systèmes embarqués, si on doit programmer un peluche qui doit dire "Bonjour maman" lorsque l'on appuie sur son ventre, on est très limité en terme de puissance de calcul et la performance énergétique doit être maximale pour éviter de devoir changer les piles toutes les 3 minutes.
-->

---

# <!--fit--> Capacité à exécuter différents programmes

Vos machines sont dites à **programmes stockés** :
* Elles ont des composants qui stockent les programmes.
* Elles ont des composants qui lui permettent d'exécuter les instructions de ces programmes.

---

# <!--fit--> Architecture logique simplifiée d'un ordinateur

Un ordinateur comporte :
* Des **entrées** (clavier, souris, ...) et des **sorties** (écran, son, ...).
* Des **mémoires** (disque, RAM, caches, ...).
* Des **calculateurs** (CPU, GPU, ...) ayant :
  * **Unité de contrôle** (compteur de programme, ...).
  * **Unités arithmétique et logique** ($+$, $-$, ...).

<!--
@TODO : faire un diagramme à la place
-->

---

# <!--fit--> Cycle de vie simplifié d'un programme

* La séquence d'instructions du programme est chargé en mémoire.
* Un programme particulier appelé **interprêteur** exécute chaque instruction dans l'ordre :
    * Un **compteur de programme** pointe en mémoire vers la prochaine instruction à exécuter.
    * Cette instruction est envoyée à l'**unité arithmétique et logique** qui s'occupe de la résoudre.

---

# Flot de contrôle

* Dans certains cas, sur la base d'un test, l'interprêteur saute vers une autre séquence d'instructions.
* C'est ce que l'on appelle le **flot de contrôle**.
* Cela nous permet d'écrire des programmes complexes.
* Une partie de ce premier cours et du prochain est dédié à l'étude des **structures de contrôle**.

---

### Graphe de flot de contrôle

![Flot de contrôle pour le petit-déjeuner](./assets/exemple-flot.png)

---

![](#fff)
![bg](https://raw.githubusercontent.com/loic-yvonnet/algo-appliquee/master/assets/bg_title.jpg)

# <!--fit--> TP 01 - Démarrer avec Scratch

---

![bg left:40% 80%](./assets/scratch-logo.png)


* Scratch est un langage de programmation graphique à destination des plus jeunes.
* Créé par le MIT.
* Démo : [Editeur Scratch](https://scratch.mit.edu/projects/editor/).

<!--
Faire une démo live de Scratch pour présenter le fonctionnement général.
La démo live peut consister en la 1ière partie du TP avec le personnage du chat Scratch.
Ma nièce, qui a 10 ans au moment de l'écriture de ce cours, sait utiliser Scratch.
C'est un langage parfait pour apprendre la programmation.
-->

---

![bg right:40% 80%](./assets/../work-assignment-01/assets/014-apercu-execution.jpeg)

# <!--fit--> TP : Jeu Vidéo avec Scratch

* [Lien vers le sujet de TP](./tp-01-scratch.html).
* Contexte : Anjou Vélo Vintage.

---

![](#fff)
![bg](https://raw.githubusercontent.com/loic-yvonnet/algo-appliquee/master/assets/bg_title.jpg)

# <!--fit--> Discussion sur les langages de programmation

---

# Intuition

* Un langage de programmation offre une **syntaxe** pour spécifier les **instructions** que l'interprêteur doit exécuter.
* Il existe de nombreux langages de programmation.
* Scratch et Pythonen font parti.

---

# Machine de Turing

* En 1936, Alan Turing : spécification de la **Machine de Turing Universelle**.
* Avec quelques instructions simples, et une mémoire, il est possible d'écrire n'importe quel programme.
* Tout programme peut être écrit avec un jeu de 6 instructions élémentaires.

---

# Thèse de Church Turing

---

Le Problème de Stoppage (Halting Problem)
Turing complet

Puis

Paradigmes de programmation :
Langage déclaratif
Langage impératif
Autres : langage orienté objet, fonctionnel, etc.

Puis 

Sémantique
Syntaxe et grammaire
Intuition concernant la qualité


---

![](#fff)
![bg](https://raw.githubusercontent.com/loic-yvonnet/algo-appliquee/master/assets/bg_title.jpg)

# <!--fit--> Introduction au langage Python

---

![](#fff)
![bg](https://raw.githubusercontent.com/loic-yvonnet/algo-appliquee/master/assets/bg_title.jpg)

# <!--fit--> Types numériques, expressions et objets en Python

---

![](#fff)
![bg](https://raw.githubusercontent.com/loic-yvonnet/algo-appliquee/master/assets/bg_title.jpg)

# <!--fit--> Variables et assignation

---

![](#fff)
![bg](https://raw.githubusercontent.com/loic-yvonnet/algo-appliquee/master/assets/bg_title.jpg)

# <!--fit--> TP 02 - Python avec Jupyter Notebook
