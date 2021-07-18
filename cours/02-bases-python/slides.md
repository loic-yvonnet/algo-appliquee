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

  section.smaller-text p, section.smaller-text pre, section.smaller-text ul {
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

- Conditions
- Chaînes de caractères et encodage de caractères
- Entrée et sortie standard
- Boucles "Tant Que"
- Boucles "Pour"
- Discussion sur les différences entre Scratch et Python
- Style, commentaires et PEP 8

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

* Attention aux `:` et à l'**indentation** de 4 espaces.
* Attention à la casse : les mots clés `if` et `else` sont en **minuscule**.

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

# <!--fit--> Plus lisible avec les expressions Booléennes composées

```py
texte = ""
taille = 175

if taille > 200:
    texte = "très grand"
elif taille > 180:
    texte = "grand"
elif taille > 155:
    texte = "moyen"
else:
    texte = "petit"

print(texte)
```

:arrow_right: `moyen`

---

# <!--fit--> Expression conditionnelle dense

```py
taille = 175
texte = "grand" if taille > 180 else "petit"
print(texte)
```

:arrow_right: `petit`

---

<!-- _class: title-section -->

# <!--fit--> Chaînes de caractères et encodage de caractères

---

# Type `str`

* En anglais, **string** signifie **chaîne de caractères**.
* Cela n'a *rien* à voir avec certains vêtements... :bikini:
* `str` est la contraction de string.
* Exemple :

```py
taille = "petit"
```

---

# Concaténation

```py
entree = "avocat"
plat = "riz"
dessert = "chocolat"
espace = " "
repas = entree + espace + plat + espace + dessert

print(repas)
```

:arrow_right: `avocat riz chocolat`

---

# Multiplication scalaire

```py
a = "a"
trois_a = 3 * a

print(trois_a)
```

:arrow_right: `aaa`

---

# Multiplication ?

```py
a = "a"
a_voir = a * a
```

:arrow_down:

```
TypeError: can't multiply sequence by non-int of type 'str'
```

<!--
Cela ne voudrait de toutes façons rien dire.
Mieux vaut interdire une syntaxe sans sémantique.
-->

---

# Longueur

`len` est un diminutif de **length**, qui signifie longueur.

```py
chaine = "abcde"
len(chaine)
```

:arrow_right: `5`

```py
chaine = "papillon"
len(chaine)
```

:arrow_right: `8`

---

# Indexation

```py
chaine = "abcde"
chaine[0]
```

:arrow_right: `"a"`

```py
chaine = "abcde"
chaine[2]
```

:arrow_right: `"c"`

---

# Indexation négative

```py
chaine = "abcde"
chaine[-1]
```

:arrow_right: `"e"`

```py
chaine = "abcde"
chaine[-3]
```

:arrow_right: `"c"`

---

# <!--fit--> Indexation en dehors des limites

```py
chaine = "abcde"
chaine[5]
```

:arrow_down:

```
IndexError: string index out of range
```

---

# Tranche entre 2 bornes

```py
debut = 1
fin = 4
chaine = "abcde"
tranche = chaine[debut:fin]
print(tranche)
```

:arrow_right: `"bcd"`

*Note* : en anglais, on parle de **slicing**.
*Note 2* : la borne de fin est exclue.

---

# <!--fit--> Tranche à partir d'un index

```py
debut = 2
chaine = "abcdefg"
tranche = chaine[debut:]
print(tranche)
```

:arrow_right: `"cdefg"`

---

# <!--fit--> Tranche jusqu'à un index

```py
fin = 5
chaine = "abcdefg"
tranche = chaine[:fin]
print(tranche)
```

:arrow_right: `"abcde"`

---

# <!--fit--> Tranche non contiguë

```py
debut = 1
fin = 10
saut = 2
chaine = "abcdefghijklmnop"
tranche = chaine[debut:fin:saut]
print(tranche)
```

:arrow_right: `"bdfhj"`

---

# Caractères spéciaux

- On utilise le **caractère d'échappement** `\` en préfixe des caractères spéciaux dans les chaînes de caractères.
- Quelques exemples :
  - Guillements : `\"`
  - Tabulation : `\t`
  - Retour à la ligne : `\n`
  - Retour chariot : `\r`
  - Backslash : `\\`

---

# <!--fit--> Exemples de caractères spéciaux

```py
print("lapin\rLu")
```

:arrow_right: `"Lupin"`

```py
print("C:\\Users\\mikado\\Documents")
```

:arrow_right: `"C:\Users\mikado\Documents"`

```py
print("\tValeur : \"Zorro\"")
```

:arrow_right: `"	Valeur : "Zorro""`

---

# <!--fit--> Conversion vers des nombres

```py
chaine = "1234"
entier = int(chaine)
entier += 8765
print(entier)
```

:arrow_right: `9999`

```py
chaine = "3.1415"
reel = float(chaine)
reel *= 2
print(reel)
```

:arrow_right: `6.283`

---

# <!--fit--> Conversion depuis des nombres

```py
entier = 123
chaine = str(entier)
chaine *= 2
print(chaine)
```

:arrow_right: `"123123"`

---

<!-- _class: smaller-text -->

![bg right:45% 95%](./assets/USASCII_code_chart.png)

# <!--fit--> Encodage de caratères : ASCII

* **ASCII** : American Standard Code for Information Interchange.
* Encodage simple et **compact** : sur 7 bits (moins de 1 octet), on peut avoir jusqu'à $2^7 = 128$ caractères.
* Chaque caractère est représenté par un nombre entre 0 et 127.
* La **table ASCII** offre une correspondance entre les nombres et leurs caractères associés.

---

# Limites du ASCII

* こんにちは : Bonjour *(Japonais)*
* 你好吗？ Comment allez-vous ? *(Mandarin)*
* شكرا لك : Merci *(Arabe)*
* :sos: :weary: :computer: : Je ne comprends rien au cours ! *(Emoji)*

---

# Unicode

* **Unicode** : Universal Coded Character Set.
* L'objectif est de **normaliser** l'encodage de caractères, d'**inclure** un maximum de langues et autres besoins et d'**optimiser** la représentation numérique.
* L'**UTF-8** (pour Unicode Transformation Format - 8 bit) est le plus répandu.
* UTF-8 utilise entre 1 et 8 octets pour représenter jusqu'à 1 112 064 caractères.

<!--
UTF-8 ne permet pas de représenter tous les symboles de toutes les langues.
Il existe de très nombreux autres formats d'encodage.
Certains formats sont populaires pour certaines langues.
Par défaut, Python utilise UTF-8.
-->

---

# Encodage en Python

* L'encodage par défaut d'un script Python est **UTF-8**.
* On peut changer cela en ajoutant au tout début d'un fichier Python :

```py
# -*- coding: ascii -*- 
```

* Toutes les `str` d'un script Python utilisent cet encodage par défaut.

---

# <!--fit--> Changer l'encodage à la volée

```py
texte_en_utf8 = "Bonjour !"
texte_en_ascii = texte_en_utf8.encode("ascii")
print(texte_en_ascii)
```

:arrow_right: `b'Bonjour !'`

Le préfixe `b` signifie qu'il s'agit d'une chaîne binaire.

<!--
Nous reviendrons plus tard sur le type binaire.
-->

---

<!-- _class: title-section -->

# <!--fit--> Entrée et sortie standard

---

# Introduction aux I/O

* En français, on parle d'Entrées/Sorties, soit **E/S**.
* La langue anglaise prédomine en informatique.
* La traduction en anglais d'E/S est **I/O** pour Input/Output.
* On enlève en général le *slash*, ce qui donne **IO**.

---

# Les fichiers standards

* Les Systèmes d'Exploitation classiques comportent 3 fichiers standards :
  * `stdin` (index 0) : entrée texte standard.
  * `stdout` (index 1) : sortie texte standard.
  * `stderr` (index 2) : sortie d'erreur standard.

---

# Lire dans `stdin`

* `stdin` est une redirection vers le périphérique clavier.
* Une lecture dans `stdin` signifie donc que l'on va lire ce que l'utilisateur écrit.
* En Python, on utilise la fonction `input` pour lire dans `stdin` :

```py
nom = input("Votre nom : ")
```

---

# Ecrire dans `stdout`

* `stdout` est une redirection vers la console.
* Une écriture dans `stdout` va afficher le contenu dans la console.
* En Python, on utilise la fonction `print` pour écrire dans `stdout` :

```py
nom = input("Votre nom : ")
print(nom)
```

---

<!-- _class: smaller-text -->

# Ecrire dans `stderr`

* `stderr`, tout comme `stdout`, est une redirection vers la console.
* Une écriture dans `stderr` va afficher le contenu dans la console.
* En Python, lorsqu'une exception est levée, un message d'erreur est affiché dans `stderr` par défaut.
* On peut également utiliser `sys.stderr.write` :

```py
import sys
sys.stderr.write("Oh mince ! dit Shipper")
```

---

# Formattage simple

```py
age_en_texte = input("Votre age : ")
age = int(age_en_texte)
print("Vous avez", age, "ans")
```

:arrow_right: `"Vous avez 42 ans"`
*(si `age == 42`)*

---

# <!--fit--> Limites du formattage simple

```py
ht = 69.5
tva = 1/5
taxe = round(ht * tva * 100) / 100
ttc = ht + taxe
label_ht = "Prix (HT) : "
label_ttc = "Prix (TTC) : "
print(label_ht, ht, "€\n", label_ttc, ttc, "€")
```

:arrow_down:

```
Prix (HT) :  69.5 €
 Prix (TTC) :  83.4 €
```

---

# <!--fit--> Chaîne de caractères litérale formattée

```py
ht = 69.5
tva = 1/5
taxe = round(ht * tva * 100) / 100
label_ht = "Prix (HT) :"
label_ttc = "Prix (TTC) :"
print(f"{label_ht:>12} {ht:.2f}€\n{label_ttc:>12} {ht + taxe:.2f}€")
```

:arrow_down:

```
 Prix (HT) : 69.50€
Prix (TTC) : 83.40€
```

---

<!-- _class: title-section -->

# TP 03 - Initiation aux Environnements de Développement Intégrés avec pour but de manipuler des chaînes de caractères

---

![bg left:40% 60%](./assets/Visual_Studio_Code_1.35_icon.svg.png)


* **Visual Studio Code** est un Environnement de Développement Intégré.
* Edité par Microsoft en JavaScript/Electron.
* Gratuit et Open Source.
* Linux, macOS, Windows.
* Nombreuses extensions.
* [**Lien vers le site officiel**](https://code.visualstudio.com)

<!--
Extensions disponibles pour presque tous les langages de programmation.
Excellent support de Python.
Vous pourrez l'utiliser sans problème pour vos projets professionnels.
Est utilisé notamment pour l'édition de ce cours.
-->

---

![bg right:40% 90%](./assets/vscode_ide.png)

### TP : Usage d'un IDE et manipulation de chaînes

[**Lien** vers le sujet de TP](./tp-03-ide-et-strings.html).

---

<!-- _class: title-section -->

# <!--fit--> Boucles "Tant que"

---

<!-- _class: title-section -->

# <!--fit--> Boucles "Pour" et "Bornes"

---

<!-- _class: title-section -->

# TP 04 - Quelques algorithmes simples pour prendre en main les fondamentaux de l'algorithmique

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
