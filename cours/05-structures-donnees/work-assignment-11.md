---
title: "Travail Pratique 8 - Gestion d'un hôpital"
summary: "Travaux Pratiques : Utiliser un dictionnaire pour gérer un hôpital avec des patients, des médecins et des soins à apporter."
category: 05-structures-donnees
permalink: "{{ category }}/tp-08-gestion-hosto.html"
url: "{{ url_prefix }}/{{ permalink }}"
layout: layouts/site.njk
---

Ce TP va vous amener progressivement à construire une mini application en ligne de commande pour gérer un hôpital : les patients, les médecins et les soins à apporter.

L'objectif de ce TP est de vous familiariser avec les 2 principales structures de données en Python : les listes et les dictionnaires.

## Exercice 1 - Menu en ligne de commande

Ecrivez un script nommé `gestion_hosto.py` dans lequel la fonction __main__ affiche l'entête suivante :
```bash
Bienvenu dans Gestion Hosto 0.0.1 alpha
---------------------------------------
```

Créer une fonction `menu_principal` appelée en boucle par __main__. La fonction `menu_principal` renvoie un entier et la boucle s'arrête lorsque cet entier est égal à 0.

La fonction `menu_principal` commence par afficher le texte suivant :
```
Veuillez choisir une action parmis les choix suivants :

[ 0] - Quitter

PATIENTS
--------
[ 1] - Lister
[ 2] - Ajouter
[ 3] - Retirer
[ 4] - Rechercher
[ 5] - Afficher les soins
[ 6] - Afficher les médecins

MEDECINS
--------
[ 7] - Lister
[ 8] - Ajouter
[ 9] - Retirer
[10] - Rechercher
[11] - Assigner patient
[12] - Prodiguer un soin
```

Ensuite, la fonction `menu_principal` fait un appel à `input("Votre choix : ")`.

La fonction `menu_principal` renvoie le choix de l'utilisateur sous la forme d'un entier.

## Exercice 2 - Préparation du dictionnaire

Ecrivez une fonction `prepare_dico` qui créé et retourne le dictionnaire suivant :
```py
dico = {
    "patients": {},
    "medecins": {}
}
```

Cette fonction `prepare_dico` doit être appelée depuis __main__. Ce dictionnaire va être votre structure de données principales dans laquelle toutes les informations seront stockées.

In fine, après utilisation des différents menus, le dictionnaire pourra contenir par exemple :
```py
dico = {
    "patients": [
        {
            "id": 0,
            "prenom": "Rob",
            "nom": "Stark",
            "naissance": "Hivers 837",
            "adresse": "Winterfell",
            "telephone": "06.07.08.09.10",
            "email": "rob.stark@winterfell.ws",
            "soins": [ "pommade", "aspirine", "sangsue" ]
        },
        {
            "id": 1,
            "prenom": "Sansa",
            "nom": "Stark",
            "naissance": "Hivers 843",
            "adresse": "Winterfell",
            "telephone": "06.05.04.03.02",
            "email": "sansa.stark@winterfell.ws",
            "soins": [ "vitamines", "gelules" ]
        }
    ],
    "medecins": [
        {
            "id": 0,
            "prenom": "Tyrion",
            "nom": "Lannister",
            "naissance": "Ete 824",
            "adresse": "Lannisport",
            "telephone": "06.70.80.90.01",
            "email": "the_imp@westeros.com",
            "patients": [ 0, 1 ]
        },
        {
            "id": 1,
            "prenom": "Cercei",
            "nom": "Lannister",
            "naissance": "Ete 816",
            "adresse": "Lannisport",
            "telephone": "06.65.65.65.65",
            "email": "cercei.lannister@trust.com",
            "patients": [ 1 ]
        }
    ]
}
```

## Exercice 3 - Fonctions de gestion des sous-menus (interface utilisateur)

Rajoutez les fonctions suivantes :
* `menu_ajoute_patient()` : demande à l'utilisateur un id, prénom, nom, date de naissance, adresse, numéro de téléphone et un email puis renvoie ces informations.
* `menu_retire_patient()` : demande à l'utilisateur un id de patient puis renvoie cette information.
* `menu_recherche_patient()` : demande à l'utilisateur un prénom, un nom et une date de naissance puis renvoie ces informations.
* `menu_affiche_soins_patient()` : demande à l'utilisateur un id de patient puis renvoie cette information.
* `menu_affiche_medecins_patient()` : demande à l'utilisateur un id de patient puis renvoie cette information.
* `menu_ajoute_medecin()` : demande à l'utilisateur un id, prénom, nom, date de naissance, adresse, numéro de téléphone et un email puis renvoie ces informations.
* `menu_retire_medecin()` : demande à l'utilisateur un id de médecin et renvoie cette information.
* `menu_recherche_medecin()` : demande à l'utilisateur un prénom, un nom et une date de naissance puis renvoie ces informations.
* `menu_assigne_patient()` : demande à l'utilisateur un id de médecin et un id de patient puis renvoie ces informations.
* `menu_prodigue_soin()` : demande à l'utilisateur un id de médecin, un id de patient et une description des soins, puis renvoie ces informations.

## Exercice 4 - Préparation des fonctions de manipulation du modèle de données

Rajoutez les fonctions suivantes :
* `liste_patients(dico)` : affiche toutes les informations (sauf les soins) de tous les patients.
* `ajoute_patient(dico, id, prenom, nom, naissance, adresse, telephone, email)` : ajoute un nouveau patient, sauf si l'id est déjà utilisé, auquel cas, un message d'erreur est affiché.
* `retire_patient(dico, id)` : si l'id existe, retire le patient associé, ou affiche un message d'erreur. Attention à également retirer le patient du côté des médecins.
* `recherche_patient(dico, prenom, nom, naissance)` : recherche un patient par son prénom, nom et date de naissance. S'il est trouvé, on affiche toutes ses informations (sauf les soins).
* `affiche_soins_patient(dico, id)` : si l'id existe, affiche le prénom, le nom et la liste des soins apportés au patient. Sinon, affiche un message d'erreur.
* `affiche_medecins_patient(dico, id)` : si l'id de patient existe, affiche les ids, prénoms et noms des médecins qui s'occupent d'elle ou lui.
* `liste_medecins(dico)` : affiche toutes les informations concernant les médecins. Les patients assignés sont également affichés avec leur id, prénom et nom.
* `ajoute_medecin(dico, id, prenom, nom, naissance, adresse, telephone, email)` : ajoute un nouveau médecin, sauf si l'id est déjà utilisé, auquel cas, un message d'erreur est affiché.
* `retire_medecin(dico, id)` : si l'id existe, retire le médecin associé, ou affiche un message d'erreur.
* `recherche_medecin(dico, prenom, nom, naissance)` : recherche un médecin par son prénom, nom et date de naissance. S'il est trouvé, on affiche toutes ses informations (y compris les patients associés, dont on affiche l'id, le prénom et le nom).
* `assigne_patient(dico, id_medecin, id_patient)` : si les ids de médecin et de patient existent, et si le médecin ne traite pas déjà ce patient, ajoute l'id du patient dans la liste de ceux suivis par le médecin. Dans le cas contraire, affiche un message d'erreur.
* `prodigue_soin(dico, id_medecin, id_patient, soin)` : si les ids de médecin et de patient existent, et si le médecin suit le patient, ajoute le soin dans la liste des soins du patient. Dans le cas contraire, affiche un message d'erreur.

Faites attention à ne pas dupliquer de code. Utilisez des fonctions supplémentaires si nécessaire pour éviter les duplications inutiles.

Veillez à commenter et à aérer correctement votre code.

Faites attention à vos messages d'erreur : ils doivent être ausi précis et compréhensibles que possible.

## Exercice 5 - Glue code et tests

Rajoutez le code qui permet d'appeler les bonnes fonctions et testez votre code.
