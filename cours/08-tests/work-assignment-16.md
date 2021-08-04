---
title: "Travail Pratique 12 - Exceptions dans une calculatrice"
summary: "Travaux Pratiques : Utilisation d'exceptions pour gérer les cas exceptionnels d'un calculatrice (division par zéro, racine carrée négative, opérateur manquant, etc.)."
category: 08-tests
permalink: "{{ category }}/tp-12-exceptions-calculatrice.html"
url: "{{ url_prefix }}/{{ permalink }}"
layout: layouts/site.njk
---

![Calculatrice](./assets/calculatrice.png)

Dans ce TP, vous allez implémenter une **calculatrice**. Votre attention devra se porter tout particulièrement sur la gestion des erreurs :
* Division par zéro.
* Racine carrée négative.
* Opérateur manquant ou invalide.
* A vous de voir s'il y a d'autres cas.

Vous devrez utiliser **les exceptions** pour gérer les cas d'erreur.

Vous allez devoir prendre connaissance d'un programme écrit partiellement. Vous allez le compléter, le déboguer et le faire fonctionner dans tous les cas de figure.

Une calculatrice comporte une interface utilisateur. Vous allez devoir installer sur votre machine une bibliothèque de gestion d'interfaces utilisateur appelé **PySimpleGUI**. GUI signifie Graphical User Interface en anglais, c'est à dire Interface Utilisateur Graphique.

Pour installer cette dépendance, ouvrez un terminal (ou PowerShell sur Windows) et tappez les commandes suivantes :

```bash
python3.9 -m pip install -U pip
python3.9 -m pip install -U pysimplegui
python3.9 -m pip install -U PyQt5
python3.9 -m pip install -U PySimpleGUIQt
```

En fonction de votre système d'exploitation, vous pourriez avoir à modifier ces commandes. Par exemple, sur Windows, vous pouvez invoquer `python` à la place de `python3.9`.

Ensuite, [télécharger le script calculatrice.py](https://raw.githubusercontent.com/loic-yvonnet/algo-appliquee/master/cours/08-tests/assets/calculatrice.py). Ouvrez ce script dans votre IDE préféré (par exemple, Visual Studio Code).

Lisez le code, exécutez le, mettez des points d'arrêt.