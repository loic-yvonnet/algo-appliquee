---
title: "Travail Dirigé 4 - Evaluation de compléxité"
summary: "Travaux Dirigés : Evaluer la complexité de fonctions fournies."
category: 07-complexite
permalink: "{{ category }}/td-04-eval-complexite.html"
url: "{{ url_prefix }}/{{ permalink }}"
layout: layouts/site.njk
---

Ce 4ième TD va vous ammener à évaluer la compléxité de certains algorithmes. Vous utiliserez à chaque foix la notation O, et justifierez votre réponse.

## Exercice 1 - Complexité d'une recherche dichotomique

Dans l'exercice 2 du TP n°5, vous avez implémenté une recherche dichotomique. Quelle est sa complexité ?

## Exercice 2 - Complexité d'une addition matricielle

Dans l'exercice 3 du TD n°3, vous avez implémenté une addition matricielle. Quelle est sa complexité ?

## Exercice 3 - Complexité d'une multiplication matricielle

Dans l'exercice 6.2 du TD n°3, vous avez implémenté une multiplication matricielle. Quelle est sa complexité ?

## Exercice 4 - Complexité du calcul d'une factorielle

Dans l'exercice 4 du TP n°4, vous avez implémenté une factorielle. Quelle est sa complexité ?

## Exercice 5 - Complexité de la méthode de Gauss Jordan

Dans l'exercice 4.7 DM n°3, vous avez implémenté la méthode de Gauss Jordan. Quelle est sa complexité ?

## Exercice 6 - Complexité du calcul de collision entre sphère et plan

Dans l'exercice 6 du TD n°2, vous avez implémenté un algorithme de détection de collision entre une sphère et un plan. Quelle est sa complexité ?

## Exercice 7 - Complexité de Fibonacci

Dans l'exercice 4 du DM n°2, vous avez implémenté la suite de Fibonacci de 2 manières :
* version itérative avec une boucle,
* version récursive.

Quelles sont les complexités de ces 2 versions ?

## Exercice 8 - Complexité des fonctions de gestion de liste chaînée

Dans le TP n°9, vous avez implémenté des fonctions d'insertion, de suppression et de recherche. Quelles sont leurs complexités ?

## Exercice 9 - Complexité des tours de Hanoï

Dans l'exercice 1 du TP 10, vous avez implémenté un algorithme résolvant le problème des tours de Hanoï. Quel est sa complexité ?


## Exercice 10 - Evaluation de la complexité d'un nouveau code

Quelle est la complexité du code suivant ?

```py
def donne_geometries_des_liaisons_cinematiques(produit):
    geometries = []
    for mecanisme in produit.mecanismes:
        for liaison in mecanisme.liaisons_cinematiques:
            for contrainte in liaison.contraintes_geometriques:
                for geometrie in contraintes.supports_geometriques:
                    trouvee = False
                    for geom_inserees in geometries:
                        if geom_inserees == geometrie:
                            trouvee = True
                            break
                    
                    if not trouvee:
                        geometries.append(geometrie)
        
```
