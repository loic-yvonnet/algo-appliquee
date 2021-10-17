---
title: "Travail Pratique 16 - Initiation aux fichiers"
summary: "Travaux Pratiques : Ecrire dans un fichier le contenu d'un Dictionary et relire ce fichier pour repopuler un Dictionary."
category: 10-python-avance
permalink: "{{ category }}/tp-16-fichiers.html"
url: "{{ url_prefix }}/{{ permalink }}"
layout: layouts/site.njk
---

Une partie essentielle de l'automatisation de tâches consiste à lire et écrire dans des fichiers.

Deux cas d'usage classiques incluent :
* La lecture de fichiers CSV produits par des collaborateurs avec Microsoft Excel afin de générer automatiquement des rapports.
* Lire les logs générées par des processus sur un réseau afin de suivre l'évolution de l'état de santé de différents services (sites web, bases de données, etc.).

Bien que la gestion de fichiers ne soit pas officiellement au programme, nous considérons que c'est essentiel pour votre travail en alternance. Vous n'aurez donc pas de question sur la gestion de fichiers lors de l'examen final.

Pour chaque exercice, vous devez créer un fichier nommé `tp16_exercice_X.py` où X est le numéro de l'exercice.

## Exercice 1 - Lire un fichier et afficher son contenu dans la console

Avec un éditeur de texte, créer un fichier nommé `lorem_ipsum.txt` avec le contenu suivant :
```
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
```

Utilisez les fonction `open`, `read`, `close` et `print` pour lire le fichier `lorem_ipsum.txt` et afficher son contenu dans la sortie standard de la console.

## Exercice 2 - Génération d'un fichier ini à partir d'un dictionnaire

Créez le dictionnaire suivant :
```py
anti_heros = {
    "prenom": "Jaime",
    "nom": "Lannister",
    "metier": "Garde Royal",
    "expression": "The things we do for love...",
    "adresse": "Casterly Rock, Lannisport",
    "age": "30",
    "matrimonial": "Célibataire"
}
```

En utilisant les fonctions `open`, `write`, et `close`, écrivez le contenu de ce dictionnaire dans un fichier nommé `anti_heros.ini`, au format `clé=valeur`.

Le résultat attendu est le suivant :
```
prenom=Jaime
nom=Lannister
metier=Garde Royal
expression=The things we do for love...
adresse=Casterly Rock, Lannisport
age=30
matrimonial=Célibataire
```

*Astuce* : Pour séparer les lignes, vous pouvez utiliser le caractère spécial `"\n"`.

*Notes* : 
* En pratique, on utiliserait plutôt `os.linesep` du paquet `os` pour représenter le séparateur de lignes, afin d'utiliser le séparateur du système d'exploitation (CRLF sur Windows et LF sur la plupart des autres systèmes).
* On part du principe que le format des fichiers lus et écrits dans ce TP est UTF-8.

## Exercice 3 - Population d'un dictionnaire à partir d'un fichier ini

En utilisant `open`, `read`, `close`, lisez le fichier `anti_heros.ini` et créez le dictionnaire `anti_heros` tel que décrit dans l'exercice 2.

Vous avez maintenant une bijection entre le dictionnaire et le fichier.

## Exercice 4 - CLI pour gérer une liste de fruits

Ecrivez un programme permettant :
* La saisie du nom d'un fruit.
* L'affichage de la liste des fruits.
* La sauvegarde de la liste des fruits dans un fichier.
* Le chargement d'une liste de fruits depuis un fichier.
