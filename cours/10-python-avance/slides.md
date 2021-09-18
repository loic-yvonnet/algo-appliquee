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

- Autre exemple avec `math.cos` :
```python
from math import cos

print(cos(0))
```

---

# La fonction principale

- Lorsque l'on exécute un script en ligne de commande, l'interprêteur assigne la chaîne de caractère `"__main__"` à la variable globale `__name__`.
- Cela permet de distinguer le cas où un script est importé avec `import`, du cas où un script est exécuté indépendemment :

```python
def main():
    # On peut par exemple tester le bon fonctionnement de racine_carree et 
    # racine_cubique ici.
    pass

if __name__ == "__main__":
    # Exécuté uniquement si le script est lancé en ligne de commande
    main()
```


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
