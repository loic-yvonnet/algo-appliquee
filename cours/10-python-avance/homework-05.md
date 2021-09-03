---
title: "Devoir à la Maison 5 - Plus de modules"
summary: "Devoirs à la Maison : Utilisation de MatPlotLib, Panda et de requête HTTP pour effectuer des opérations de base."
category: 10-python-avance
permalink: "{{ category }}/dm-05.html"
url: "{{ url_prefix }}/{{ permalink }}"
layout: layouts/site.njk
---

Ce 5e DM vous amène à revoir des éléments de cours vu aujourd'hui concernant les modules.

## Exercice 1 - Moteur de recherche en ligne de commande

Vous allez implémenter un utilitaire permettant d'effectuer une recherche Internet à l'aide :
* du moteur de recherche Qwant,
* du module `requests`,
* du module `inscriptis`.

A l'aide de `pip`, installez les paquets `requests` et `inscriptis` depuis un terminal.

Ensuite, créez un nouveau script Python.

A l'aide de la fonction `input`, demandez à l'utilisateur de rentrer ses termes de recherche.

Ensuite, concatenez ces termes en utilisant un `"+"` comme séparateur. La chaîne de caractères ne doit plus comporter d'espace ni de caractères spéciaux.

Par exemple, si l'utilisateur a rentré `"chat gris"`, votre chaîne de caractères doit devenir `"chat+gris"`.

Créez ensuite une variable nommée `url` telle que :
* Elle comporte le préfix `"https://www.qwant.com/?q="`,
* Puis les termes de recherches concaténés,
* Et enfin le suffix `"&t=web"`.

En poursuivant notre exemple, la variable `url` serait `"https://www.qwant.com/?q=chat+gris&t=web"`.

En utilisant le module `requests`, effectuez une requête HTTP GET sur l'`url` et récupérez la réponse en sortie.

Le code HTML de la page se trouve dans la propriété `text` de la réponse HTTP.

En utilisant le module `inscriptis`, convertissez le code HTML de la page en texte simple (à l'aide de `get_text`). Utilisez la fonction `print` pour afficher ce texte dans la sortie.

Le résultat obtenu à ce stade est déroutant : il n'y a aucun résultat de recherche ! La même recherche dans un navigateur web donne un résultat différent. La raison est simple : utiliser une API Web est un service payant de manière générale.

La question qui suit est : comment le serveur de recherche (Google, Bing, Qwant et autres) reconnait-il des requêtes faites depuis un navigateur web ? Comment faire la distinction avec des requêtes effectuées en ligne de commande ?

En pratique, une requête HTTP comporte des entêtes. L'une de ces entêtes s'appelle le User Agent, et identifie la nature de l'entité qui effectue la requête.

On peut donc se faire passer pour un navigateur web pour obtenir des résultats de recherche :
```py
firefox = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
requests.get(url, headers={"User-Agent":firefox})
```

En revanche, il ne faut pas exécuter la requête un nombre de fois trop élevé : 
* un navigateur web implémente un cache navigateur qui va minimiser le nombre de requêtes effectuées au serveur, contrairement à l'outil naïf en cours d'implémentation,
* les moteurs de recherche limitent le nombre de requêtes que l'on peut effectuer sur un laps de temps donné sans passer par leur site (en utilisant d'autres mécanimes),
* si les moteurs de recherche ne peuvent pas se rémunérer avec la publicité, il est normal qu'ils utilisent un autre modèle économique de rémunération - ici, au nombre de requêtes effectuées sur le laps de temps donné -,

Par ailleurs, il faut être conscient qu'il s'agit d'un hack et non pas d'une vraie solution viable. En effet :
* changer l'identité du User Agent n'est pas une bonne pratique sauf lorsque l'on souhaite tester des problématiques de cybersécurité,
* il ne faut pas changer l'identité du User Agent dans des solutions industrielles.


## Exercice 2 - Tableau de points

Lire un fichier CSV qui contient un tableau de points et afficher le contenu avec MatPlotLib.
Encapsuler MapPlotLib dans SimplePyGUIQt.

## Exercice 3 - Tableur

Lire un fichier CSV qui contient des données en colonnes et effectuer des opérations avec Panda.
Encapsuler des graphes Panda dans SimplePyGUIQt.