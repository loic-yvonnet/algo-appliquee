---
marp: true
title: "Algorithmique Appliquée - Fonctions"
description: "Cours d'Algorithmique Appliquée avec Python"
author: "Loïc Yvonnet"
keywords: "Algorithmique, Algorithme, Python, Introduction, Débutant"
lang: "fr"
url: "https://loic-yvonnet.github.io/algo-appliquee/04-fonctions/"
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

## Procédures et fonctions

<!--
Les fonctions sont fondamentales en programmation.
Il s'agit de l'unité de travail permettant la réutilisation et la programmation modulaire.
Nous allons voir dans ce cours en quoi les fonctions sont importantes et comment les définir et les appeler.
-->

---

<!-- _class: smaller-text -->

# Plan

- Procédures : définition et appel
- Arguments
- Valeurs par défaut
- Variables locales et globales
- Fonctions
- Spécifications et contrat
- Modularisation de code
- Nombre variable d'argument
- Retour de plusieurs résultats
- Un mot sur la récursivité
- Fonctions d'ordre supérieur
- Fonctions lambda
- Programmation impérative et fonctionnelle
- Un mot sur les méthodes
 
---

<!-- _class: title-section -->

# <!--fit--> Procédures : définition et appel

---

# Comment réutiliser ce code ?

```python
a0 = 16

s = a0 / 2
epsilon = 0.001

while abs(s ** 2 - a0) >= epsilon:
    P = s ** 2 - a0
    P_prime = 2 * s
    s = s - P / P_prime
```

:arrow_right: On souhaite pouvoir appeler ce code pour n'importe quelle valeur de $a_0$.

<!--
La solution naïve consiste à dire qu'il suffit de changer la valeur de a0 puis de relancer le script.
Ce n'est pas vraiment réutilisable : il faut modifier le code source à chaque fois que l'on souhaite tester une nouvelle valeur.
Vous n'avez pas besoin de changer le code source de votre calculatrice pour faire un nouveau calcul.
-->

---

# Comment combiner des algorithmes ?

```python
a0 = 16
b0 = -27
epsilon = 0.001

# Racine carrée
sa = a0 / 2
while abs(sa ** 2 - a0) >= epsilon:
    P = sa ** 2 - a0
    P_prime = 2 * sa
    sa = sa - P / P_prime

# Racine cubique
positif = True
if b0 < 0:
    positif = False
    b0 = -b0
sb = b0 / 2
while abs(sb ** 3 - b0) >= epsilon:
    P = sb ** 3 - b0
    P_prime = 3 * sb ** 2
    sb = sb - P / P_prime
if not positif:
    sb = -sb

s = sa + sb
```

<!--
Il s'agit d'une manière un peu complexe d'afficher 1.
Pour afficher la somme d'une racine carrée et d'une racine cubique, on est obligé d'implémenter 2 fois Newtown-Raphson et de copier-coller nos algorithmes.
On souhaite réutiliser nos algorithmes.
-->

---

# Réutilisabilité

- On souhaite pouvoir **réutiliser** des algorithmes.
- On souhaite pouvoir **appeler** et **paramétrer** les appels à nos algorithmes.
- On souhaite pouvoir **combiner** facilement nos algorithmes.

---

# Couches d'abstraction

![75%](./assets/couches_abstraction.png)

<!--
Si on devait recopier chaque algorithme à chaque fois qu'on doit l'appeler avec une valeur particulière, ce sera ingérable.
Pour gérer des projets complexes, on est obligé de construire des couches d'abstraction.
Chaque couche d'abstraction s'appuie sur les couches inférieures pour fournir des services de plus haut niveau.
Une couche d'abstraction abstraie une partie de la complexité.
Cela permet au final de manipuler facilement des composants qui eux-mêmes sont complexes.
Dans ce diagramme, on a une application avec une interface graphique et des APIs qui permettent de manipuler un modèle de données qui s'appuie lui-même sur une base de données, sur des fonctions mathématiques, etc.
Si les couches d'abstraction n'existaient pas, l'utilisateur final devrait lui-même manipuler les fonctions mathématiques.
Les jeux vidéos seraient potentiellement moins funs et plus éducatifs !
-->

---

# Procédure

- Une **procédure** est une suite d'instructions.
- Il est possible d'appeler plusieurs fois une procédure.

---

# Syntaxe d'une procédure

```python
def procedure():
    print("Première procédure")
```

<!--
Ici, rien n'est affiché.
On ne fait que définir une procédure.
-->

---

# Appel d'une procédure (invocation)

```python
def procedure():
    print("Première procédure")

procedure()
procedure()
procedure()
```

:arrow_down:

```
Première procédure
Première procédure
Première procédure
```

<!--
Ici, on défini une procédure, puis on l'appelle 3 fois.
Par conséquent, le message est affiché 3 fois dans la sortie standard.
-->

---

# Suite d'instructions

```python
def racine_cubique_27():
    """Affiche la racine cubique de 27."""
    b0 = 27
    epsilon = 0.001

    positif = True
    if b0 < 0:
        positif = False
        b0 = -b0
    sb = b0 / 2
    while abs(sb ** 3 - b0) >= epsilon:
        P = sb ** 3 - b0
        P_prime = 3 * sb ** 2
        sb = sb - P / P_prime
    if not positif:
        sb = -sb

    print(sb)

racine_cubique_27()
```

:arrow_down:

```
3.000000081210202
```

<!--
Evidemment, il peut y avoir plusieurs instructions dans une procédure.
Une procédure peut contenir ses propres variables locales.
Une procédure possède son propre contexte d'exécution.
-->    

---

<!-- _class: title-section -->

# Arguments

---

# Passage d'un argument

```python
def carre(x):
    print(f"{x ** 2}")

carre(2)
carre(3)
```

:arrow_down:

```
4
9
```

<!--
La valeur de la variable x passée en argument de la fonction carre est remplacée pour le nombre au niveau de l'appel de procédure.
Ainsi, pour carre(2), on a x == 2.
De même, pour carre(3), on a x == 3.
-->

---

# Argument pour le calcul de la racine cubique

```python
def racine_cubique(x):
    epsilon = 0.001

    positif = True
    if x < 0:
        positif = False
        x = -x
    s = x / 2
    while abs(s ** 3 - x) >= epsilon:
        P = s ** 3 - x
        P_prime = 3 * s ** 2
        s = s - P / P_prime
    if not positif:
        s = -s

    print(s)

racine_cubique(27)
racine_cubique(-27)
```

:arrow_down:

```
3.000000081210202
-3.000000081210202
```

<!--
On a désormais des procédures réutilisables et utiles.
-->

---

# Plusieur arguments

```python
def somme(a, b)
    resultat = a + b
    print(resultat)

somme(2, 3)
somme(3, 4)
```

:arrow_down:

```
5
7
```

<!--
On peut évidemment passer autant d'arguments que nécessaire.
-->

---

<!-- _class: title-section -->

# Valeurs par défaut

---

# Intérêt

- Une valeur par défaut pour un argument permet de **simplifier l'appel** dans les cas classiques.
- Cela donne à l'appelant **plus de possibilités** de paramétrage dans les cas particuliers.

---

# Puissance

```python
def puissance(x, exposant=2):
    print(f"{x ** exposant}")

puissance(2)
puissance(2, 3)
```

:arrow_down:

```
4
8
```

---

# Racine cubique avec $\lambda$

```python
def racine_cubique(x, epsilon=0.0000001):
    positif = True
    if x < 0:
        positif = False
        x = -x
    s = x / 2
    while abs(s ** 3 - x) >= epsilon:
        P = s ** 3 - x
        P_prime = 3 * s ** 2
        s = s - P / P_prime
    if not positif:
        s = -s

    print(s)

racine_cubique(27)
racine_cubique(27, 1)
```

:arrow_down:

```
3.000000000000002
3.0004936436555805
```

---

# Tous les arguments sont éligibles

```python
def bonjour(prenom="Amélie", nom="Poulain"):
    print(f"Bonjour {prenom} {nom}")

bonjour()
bonjour(nom="Teng")
```

:arrow_down:

```
Bonjour Amélie Poulain
Bonjour Amélie Teng
```

---

# Attention

```python
def bonjour(prenom="Amélie", nom):
    print(f"Bonjour {prenom} {nom}")
```

:arrow_down:

```
    def bonjour(prenom="Amélie", nom):
                                     ^
SyntaxError: non-default argument follows default argument
```

<!--
Un argument sans valeur par défaut ne peut pas succéder à un argument avec une valeur par défaut.
-->

---

<!-- _class: title-section -->

# <!--fit--> Variables locales et globales

##### Scope

---

# Portée des variables

```python
def f(a):
    print(a)

def g(a, b):
    f(a)
    f(b)

def h():
    a = 3
    b = a + 2
    g(b, a)

h()
```

:arrow_down:

```
5
3
```

<!--
La portée d'une variable est limitée a la procédure dans laquelle elle est définie.
Les arguments d'une procédure sont des variables de cette procédure.
Ainsi, dans le contexte de h, on appelle g(b, a), avec b == 5 et a == 3.
Dans le contexte de g, le premier argument a == 5, et le second argument b == 3.
La première fois que l'on appelle f, on affiche donc 5.
La deuxièmre fois que l'on appelle f, la variable a dans le contexte de f est a == 3.
Donc on affiche 3 la deuxième fois.
-->

---

# Variable globale

```python
a = 5

def f(a=10):
    print(a)

f()
f(a)
```

:arrow_down:

```
10
5
```

<!--
Même principe que précédemment.
La différence ici est que la variable globale a n'affecte pas le contexte de f.
-->

---

# Accès en lecture à une variable globale

```python
a = 3

def f():
    for _ in range(a):
        print(a * "*")

f()
```

:arrow_down:

```
***
***
***
```

<!--
On peut accéder en lecture seule à une variable globale dans le contexte d'une fonction.
On dit que la variable est globale car elle n'est locale à aucune procédure.
-->

---

# Accès en écriture à une variable globale

```python
a = 3

def f():
    a -= 1
    for _ in range(a):
        print(a * "*")

f()
```

:arrow_down:

```
    a -= 1
UnboundLocalError: local variable 'a' referenced before assignment
```

<!--
On ne peut pas accéder en écriture à une variable globale par défaut.
-->

---

# Mot clé `global`

```python
a = 3

def f():
    global a
    a -= 1
    for _ in range(a):
        print(a * "*")

f()
```

:arrow_down:

```
**
**
```

<!--
On doit informer explicitement que l'on souhaite réutiliser la variable a du contexte global.
-->


---

<!-- _class: title-section -->

# Fonctions

---

# Généralisation

- Une procédure est une **fonction** qui ne retourne pas de résultat.
- Une procédure est donc une fonction.
- De manière générale, on parle toujours de fonctions.

---

# Retourner un résultat

```python
def somme(a, b):
    """Renvoie la somme de a + b."""
    return a + b

resultat = somme(1, 2)
```

:arrow_down:

```
3
```

<!--
Le mot clé return permet de retourner un résultat.
On peut affecter ce résultat à une autre variable.
En pratique, vous avez déjà utilisé de nombreuses fonctions : range, int, float, input, print, etc.
-->

---

# Définition formelle (1/2)

```python
def nom_de_la_fonction(liste_de_parametres):
    corps_de_la_fonction
```

---

# Définition formelle (2/2)

- Lorsque l'on appelle (ou *invoque*) une fonction :
    - les expressions qui forment les paramètres sont évalués.
    - les paramètres formels de la fonction sont liés aux valeurs de ces expressions.
    - le point d'exécution est déplacé depuis le point d'invocation à la première instruction du corps de la fonction.
    - le corps de la fonction est exécuté :
        - jusqu'à une instruction `return`, auquel cas la valeur de la fonction devient la valeur de cette expression `return`,
        - ou alors jusqu'à ce qu'il n'y ait plus d'instruction à exécuter, auquel cas `None` est retourné.

---

# Fonction racine carrée

```python
def racine_carree(x, epsilon=0.000001):
    """Renvoie la racine carrée de x à epsilon près."""
    s = x / 2
    while abs(s ** 2 - x) >= epsilon:
        P = s ** 2 - x
        P_prime = 2 * s
        s = s - P / P_prime

    return s

resultat = racine_carree(16)
```

:arrow_down:

```
4.000000000000004
```

<!--
Plutôt que d'afficher le résultat dans la sortie standard, on préfère le renvoyer.
Cela offre plus de flexibilité et est plus évolutif.
-->

---

# Fonction racine cubique

```python
def racine_cubique(x, epsilon=0.000001):
    """Renvoie la racine cubique de x à epsilon près."""
    positif = True
    if x < 0:
        positif = False
        x = -x
    s = x / 2
    while abs(s ** 3 - x) >= epsilon:
        P = s ** 3 - x
        P_prime = 3 * s ** 2
        s = s - P / P_prime
    if not positif:
        s = -s

    return s

resultat = racine_cubique(-27)
```

:arrow_down:

```
-3.000000000000002
```

<!--
On vient de se faire une petite bibliothèque composée des fonctions somme, racine_carre, et racine_cubique.
On va donc pouvoir répondre à notre problématique initiale de simplification de notre code.
-->

---

# Retour au problème initial

```python
r2 = racine_carree(16)
r3 = racine_cubique(-27)
resultat = somme(r2, r3)
```

:arrow_down:

```
1.0000000000000022
```

<!--
Le code initial pour résoudre ce problème était beaucoup plus conséquent, comme vous pourriez le voir en revenant sur les première diapositives.
-->

---

# Plusieurs retours

```python
def converti_nombre(x):
    """Converti le nombre x textuel sous un format entier."""
    if x == "zéro":
        return 0
    elif x == "un":
        return 1
    elif x == "deux":
        return 2
    else:
        return "non défini"

resultat = converti_nombre("un")
```

:arrow_down:

```
1
```

---

<!-- _class: title-section -->

# <!--fit--> Spécifications et contrat

---

# Intérêt de la documentation des spécifications

* Vous avez étudié lors du dernier cours l'algorithme de Newtown-Raphson.
* Cet algorithme n'est pas trivial.
* De manière générale, il faut considérer qu'aucun algorithme n'est trivial.
* Il faut documenter son code.
* En particulier, il faut documenter chacune de ses fonctions.

---

# Contrat d'une fonction

* Une fonction a un **contrat**.
* Ce contrat est un ensemble de :
    * **préconditions** : contraintes sur les valeurs d'entrée.
    * **invariants** : garantie sur les valeurs d'entrée.
    * **post-conditions** : contraintes sur les valeurs de sortie.

---

# Contrat de la fonction `racine_carree`

* **Préconditions** :
    - La variable `x` est un nombre flottant positif ou nul.
    - La variable `epsilon` est un nombre flottant strictement positif.
* **Invariants** : `x` et `epsilon` sont inchangés.
* **Post-conditions** : la valeur retournée est proche de la racine carrée de `x`, à plus ou moins `epsilon`.

---

# Attention à la sur-spécification

* On pourrait également préciser que `x` et `epsilon` doivent être différents de NAN (Not A Number) et de l'infinie.
* On pourrait également préciser que `x` et `epsilon` peuvent également être des entiers.
* Certaines choses sont implicites et n'ont pas besoin d'être spécifiées.
* C'est l'expérience qui dicte ce qui est explicite et implicite.
* Il vaut mieux commencer par être trop explicite et réduire progressivement.

---

# Les docstrings

* Chaque langage de programmation a ses bonnes pratiques de documentation.
* En Python, on documente le contrat de nos fonctions en utilisant une **docstring**.
* Une **docstring** commence et termine par un triple double-guillemet sur plusieurs lignes.

```python
    """La première ligne décrit de manière concise le but de la fonction.
    
    On laisse ensuite une ligne vide avant de rentrer plus dans les détails.
    Ensuite, on documente chaque entrée, puis chaque sortie.
    """
```

---

# Exemple avec la fonction `somme`

```python
def somme(a, b):
    """Retourne la somme des arguments.

    a - entier, flottant ou chaîne de caractères.
    b - entier, flottant ou chaîne de caractères.
    Retourne la somme a + b.
    """
    return a + b
```

<!--
On peut dans certains cas se retrouver avec plus de commentaires que de code.
Il faut faire attention à bien garder les commentaires synchronisés avec l'implémentation.
-->

---

# Exemple avec la fonction `racine_carree`

```python
def racine_carree(x, epsilon=0.000001):
    """Renvoie la racine carrée de x à epsilon près.

    Calcule la racine carrée d'un nombre x positif en employant
    l'algorithme de Newtown-Raphson.
    x - nombre flottant positif ou nul.
    epsilon - nombre flottant strictement positif.
    Retourne une valeur proche de la racine carrée de x, à plus
    ou moins epsilon près.
    """
    s = x / 2
    while abs(s ** 2 - x) >= epsilon:
        P = s ** 2 - x
        P_prime = 2 * s
        s = s - P / P_prime

    return s
```

---

# Vérification des préconditions

- Il existe 2 écoles :
    * Programmation **offensive** : les préconditions sont décrites en commentaires mais non vérifiées.
        - Avantages : performance et simplificité.
        - Inconvénients : robustesse.
    * Programmation **défensive** : les préconditions sont vérifiées et on renvoie une erreur si nécessaire.
        - Avantages : robustesse.
        - Inconvénients : lenteur et complexité.

---

# Division offensive

```python
def divise(a, b):
    """Divise a par b.

    a - nombre flottant.
    b - nombre flottant non nul.
    Retourne la division a / b.
    """
    return a / b
```

---

# Division défensive

```python
def divise(a, b, epsilon=0.000001):
    """Divise a par b.

    a - nombre flottant.
    b - nombre flottant non nul.
    epsilon - valeur autour de laquelle b est considérée nul
    Retourne la division a / b.
    """
    if abs(b) < epsilon:
        return float("inf")

    return a / b
```

---

# Division défensive extrême

```python
def divise(a, b, epsilon=0.000001):
    """Divise a par b.

    a - nombre flottant.
    b - nombre flottant non nul.
    epsilon - valeur autour de laquelle b est considérée nul
    Retourne la division a / b si a et b sont corrects. Sinon,
    retourne nan ou inf.
    """
    if type(a) != float and type(a) != int:
        return float("nan")
    if type(b) != float and type(b) != int:
        return float("nan")
    if abs(b) < epsilon:
        return float("inf")

    return a / b
```

---

# Approche pragmatique

* Souvent, en Python, on privilégie l'approche offensive avec une bonne documentation.
* Dans d'autres langages de programmation, ou certains contextes industriels, d'autres approches peuvent être favorisées.
* Il faut se renseigner sur les bonnes pratiques dans votre environnement, et suivre ces bonnes pratiques.

---

# Aide (1/2)

```python
help(round)
```

:arrow_down:

```
round(number, ndigits=None)
    Round a number to a given precision in decimal digits.
    
    The return value is an integer if ndigits is omitted or None.  Otherwise
    the return value has the same type as the number.  ndigits may be negative.
```

<!--
Il s'agit de la docstring de la fonction native round.
-->

---

# Aide (2/2)

```python
help(racine_carree)
```

:arrow_down:

```
racine_carree(x, epsilon=1e-06)
    Renvoie la racine carrée de x à epsilon près.
    
    Calcule la racine carrée d'un nombre x positif en employant
    l'algorithme de Newtown-Raphson.
    x - nombre flottant positif ou nul.
    epsilon - nombre flottant strictement positif.
    Retourne une valeur proche de la racine carrée de x, à plus
    ou moins epsilon près.
```

<!--
On peut utiliser la même commande pour obtenir les docstring que l'on a défini.
-->

---

<!-- _class: title-section -->

# <!--fit--> Modularisation de code 

##### et conventions avec la fonction main

---

# Taille d'une fonction

* Combien de responsabilités doit avoir une fonction ?
* 1 fonction :arrow_right: 1 responsabilité.
* En moyenne, une fonction doit faire entre 7 et 15 lignes.
* Une fonction qui fait plus de 30 lignes doit être découpée en plusieurs fonctions plus simples.

---

# Exemples de responsabilités

- Effectuer un calcul (ex : racine carrée).
- Appliquer une transformation (ex : nombre textuel vers numérique).
- Afficher un résultat (ex : une matrice).

---

# Ne pas se répéter

- Lorsque l'on observe un **motif qui se répète** dans le code, il y a un problème.
- Ces répétitions sont le signe d'une **duplication de code**.
- A la place, il faut créer des fonctions et les appeler.
- Le processus de modification du code pour supprimer les duplications s'appelle la **refactorisation**.
- Il s'agit d'une bonne pratique du génie logiciel.

<!--
Par exemple, lorsque l'on a dupliqué plusieurs fois le code de la racine carrée pour calculer la racine de 16, puis pour calculer la somme d'une racine carrée et d'une racine cubique.
A la place, nous avons désormais une fonction racine carrée propre et réutilisable.
-->

---

# Notion de script modulaire

- On rassemble les fonctions de même nature dans un script.
- Par exemple, on peut avoir un script `racine.py` qui contient les fonctions `racine_carree` et `racine_cubique`.
- On pourrait avoir un autre script nommé `chaine_caracteres.py` qui contient des fonctions de manipulation de chaînes de caractères.

---

# Utilisation d'un script

- On emploie le mot clé `import` pour utiliser une bibliothèque de fonctions.
- Par exemple, si on a un script `racine.py`, on utilise :

```python
import racine

print(racine_carree(4))
```

---

# La fonction principale

- Lorsque l'on exécute un script en ligne de commande, l'interprêteur assigne la chaîne de caractère `"__main__"` à la variable globale `__name__`.
- Cela permet de distinguer le cas où un script est importé avec `import`, du cas où un script est exécuté indépendemment :

```python
def main():
    # On peut par exemple tester le bon fonctionnement de racine_carree et 
    # racine_cubique ici.
    # L'instruction pass veut simplement dire que la fonction ne fait rien
    # pour le moment. C'est souvent employé en cours de développement pour
    # définir l'ensemble des fonctions à implémenter.
    pass

if __name__ == "__main__":
    # Exécuté uniquement si le script est lancé en ligne de commande
    main()
```

---

<!-- _class: title-section -->

# TD : Fonctions géométriques simples

---

### TD : Fonctions géométriques simples

[**Lien** vers le sujet de TD](./td-02-fonctions-geom.html).

---

<!-- _class: title-section -->

# <!--fit--> Nombre variable d'arguments

---

Exemple avec la fonction print
Exemple avec la fonction sum
Intérêt
Syntaxe
Exemples

---

<!-- _class: title-section -->

# <!--fit--> Retour de plusieurs résultats

---

Intérêt
Syntaxe
Exemples

---

<!-- _class: title-section -->

# <!--fit--> Un mot sur la récursivité

---

GNU is Not Unix
WINE Is Not an Emulator
Fractal
Définition comme en mathématiques : f(0) = 1, f(N) = 3 * f(N-1) + 4.
Exemple simple
Attention à la stack : exemple de stack overflow
Attention à la stack => on empile tout à chaque call récursif => utilisation massive de mémoire
Conclusion : c'est beau, mais on évite en général

---

<!-- _class: title-section -->

# <!--fit--> Fonctions d'ordre supérieur

#### Fonctions en tant qu'objets

---

Intérêt = généricité && réutilisation
Tout est objet : def foo(): pass; type(foo)
Assignation d'une fonction à une variable
Réassignation d'une autre fonction à une variable
Passage d'une fonction comme argument d'une fonction
Générateur de fonction : on retourne une nouvelle fonction

---

<!-- _class: title-section -->

# Fonctions lambda

---

Origine : calcul lambda (et pas un truc quelconque...)
Intérêt : les dévs sont un peu feignants et n'aiment pas trop tapper (sauf aux jeux de baston)
Syntaxe
Exemples

---

<!-- _class: title-section -->

# <!--fit--> Programmation impérative
### :vs:
# <!--fit--> Programmation fonctionnelle 

##### Notions de pureté et d'immutabilité

---

De grands pouvoirs impliquent de grandes responsabilités : code mess && spaghetti code
Programmation impérative => variables (ou état) globales, effets de bords non maîtrisé et beau bord**
A moins d'appliquer des bonnes pratiques stricts => boiled frog && broken windows
Exemple qui marche : kernel Linux => règles très (très très) sévères
Règle d'immutabilité : les variables constantes
Règle de pureté : pas d'effet de bord (print, etc.)
Il existe des langages qui imposent ces règles et qui pronent certaines techniques héritées de la théorie des catégories, une branche des maths.

---

<!-- _class: title-section -->

# <!--fit--> Un mot sur les méthodes

#### Avec l'exemple du type str

---

Python est *orienté object*
Tout est objet
Définition On appelle méthode une fonction rattachée à un type.
Un type défini ses propriétés (données membres) && capacités (méthodes).
`str` est un type. `upper()` est une méthode de ce type.
Exemples en plus.

---

<!-- _class: title-section -->

# <!--fit--> TP : Fonctions d'ordre supérieur

---

### TP : Fonctions d'ordre supérieur

[**Lien** vers le sujet de TP](./tp-07-fonctions-sup.html).

---

<!-- _class: title-section -->

# Devoir à la Maison 02

---

### DM : Retours sur les fonctions et le débogage

[**Lien** vers le sujet de DM](./dm-02.html).
