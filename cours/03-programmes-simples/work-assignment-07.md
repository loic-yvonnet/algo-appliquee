---
title: "Travail Pratique 6 - Débogage"
summary: "Travaux Pratiques : Déboguer un programme mal écrit et comportant des bugs."
category: 03-programmes-simples
permalink: "{{ category }}/tp-06-debogage.html"
url: "{{ url_prefix }}/{{ permalink }}"
layout: layouts/site.njk
---

Dans ce TP, vous allez déboguer un programme mal écrit et comportant des bugs. L'objectif va être de comprendre ce programme, de le documenter et de corriger un certain nombre de problèmes.

## Exercice 1 - Prendre connaissance du code

On vous donne le code suivant et on vous demande simplement de le faire fonctionner sans vous donner plus de précision.

Prenez connaissance de ce code, exécutez-le et mettez des points d'arrêt pour tenter de comprendre le flot d'exécution.

Rajoutez des commentaires, renommez les variables et reformattez le code.

```py
entree = """
somme = 0
for i in range(10):
    somme += i
print(somme)
"""
avant,apres,boucle1,corps="","","",""
bcl_var,bcl_indt="",4
r_debut,r_inc,r_fin=0,1,0
idx_actu=0
mot_prec,mot_actu="",""
dans_boucle1,dans_corps,dans_r,debut_l=False,False,False,True
verifie_mot_prec=False
for c in entree:
    if c not in {",",":","(",")",";","\n"," ","=","<",">","{","}","[","]","+","-","*","/","%","#","\t","\r","\"","\'"}:
        mot_actu += c
    elif mot_actu != "":
        mot_prec,mot_actu,verifie_mot_prec=mot_actu,"",True
    if c == "\n":
        idx_actu,debut_l=0,True
        if dans_boucle1:
            dans_boucle1,dans_r,dans_corps=False,False,True
    else:
        if c == " ":
            if debut_l:idx_actu+=1
        else:
            debut_l=False
            if dans_corps and idx_actu<bcl_indt+4:dans_corps=False
    if verifie_mot_prec:
        if mot_prec == "for":dans_boucle1,bcl_indt,avant,boucle1=True,idx_actu,avant[:-3],"for"
        elif dans_boucle1 and len(bcl_var)==0:bcl_var=mot_prec
        elif dans_boucle1 and mot_prec == "range":dans_r=True
        elif dans_r:r_fin=int(mot_prec)
        mot_prec,verifie_mot_prec="",False
    if dans_corps:corps+=c
    elif dans_boucle1:boucle1+=c
    elif len(boucle1)==0:avant+=c
    else:apres+=c
final_code,lines=avant,corps.split("\n")
for i in range(r_debut,r_fin,r_inc):
    for line in lines:
        if len(line)>4:final_code+=line[4:].replace(bcl_var,str(i))+"\n"
final_code+=apres
print(final_code)
```

Que se passe-t-il si vous changez l'entrée de la manière suivante ?
```py
entree = """
somme = 0
mult = 1
for i in range(10):
    somme += i
    mult *= i ** 2
print(somme)
print(mult)
"""
```

Que se passe-t-il si vous changez l'entrée de la manière suivante ?
```py
entree = """
somme = 0
mult = 1
for nb in range(10):
    somme += nb
    if somme > 3:
        mult *= nb ** 2
    else:
        mult += nb
print(somme)
print(mult)
"""
```

Qu'en déduisez-vous concernant l'intention du développeur initial de ce code ?

Rajoutez des commentaires pour expliquer l'intention de ce code.

## Exercice 2 - Problèmes sur le range

Que se passe-t-il si vous changez l'entrée de la manière suivante :
```py
entree = """
somme = 0
for i in range(3:10):
    somme += i
print(somme)
"""
```

Est-ce que cela vous paraît correct ? Existe-t-il toujours une bijection ?
Corrigez ce problème.

Que se passe-t-il si vous changez l'entrée de la manière suivante ?
```py
entree = """
somme = 0
for i in range(0:10:2):
    somme += i
print(somme)
"""
```

Corrigez également ce problème.

## Exercice 3 - Remplacements inattendus

Que se passe-t-il si vous changez l'entrée de la manière suivante ?
```py
entree = """
hit = 0
for i in range(10):
    hit += i
print(hit)
"""
```

Corrigez ce problème.

## Exercice 4 - Problèmes de contexte

Que se passe-t-il si vous changez l'entrée de la manière suivante ?
```py
entree = """
somme = 0
" for i in range(10): \\
    somme += i"
print(somme)
"""
```

Que se passe-t-il si vous changez l'entrée de la manière suivante ?
```py
entree = """
somme = 0
# for i in range(10):
    somme += i
print(somme)
"""
```

Que se passe-t-il si vous changez l'entrée de la manière suivante ?
```py
entree = """
somme = 0
for i in range(10):
    for j in range(20):
        somme += i + j
print(somme)
"""
```

Que déduisez-vous de cette implémentation par rapport aux problèmes rencontrés ?

Est-ce une solution viable ? Que feriez-vous ?

Faites une recherche sur Internet sur les mots clés suivants :
* Tokenizer ou Lexer.
* Pygments, SimpleParse, PyParsing.
* Abstract Syntax Tree (AST).
* Module ast de Python.

Quelles sont vos conclusions ?