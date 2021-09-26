---
title: "Travail Dirigé 1 - Dichotomie pour Racines et Logarithmes"
summary: "Travaux Dirigés : Utilisation de la dichotomie pour calculer des racines et des logarithmes."
category: 03-programmes-simples
permalink: "{{ category }}/td-01-dichotomie.html"
url: "{{ url_prefix }}/{{ permalink }}"
layout: layouts/site.njk
---

Le jour de l'examen, vous commencerez par avoir du temps pour réfléchir et poser vos idées sur papier avant de passer sur machine. Vous devez donc pratiquer cette approche.

Au-delà de l'aspect préparation à l'examen, il s'agit d'une pratique importante qui permet de prendre du recul par rapport à des problématiques de développement logiciel. Plutôt que de tenter d'écrire directement un programme sur machine, prendre le temps de noter ses réflexions permet souvent de trouver de meilleures solutions.

Dans le cadre de ce premier TD, vous allez donc écrire vos premiers programmes Python sur papier.

## Exercice 1 - Calcul d'un racine carrée par énumération dans un espace de solutions

Ecrivez un script en Python qui calcule une racine carrée $x \approx \sqrt{N} \pm \varepsilon$ en énumérant une suite de solutions.

Le nombre $N$ est obtenu via la fonction `input` et le résultat $x$, s'il est trouvé, est affiché dans la sortie standard avec `print`. Sinon, le message d'erreur suivant est affiché : `"Erreur : la racine carrée de {N} n'a pas été trouvée"`.

L'algorithme suit les étapes suivantes :
* On lit la valeur $N$ rétournée par `input`, qui est convertie en `float`.
* On initialise $x$ à `0`.
* On initialise $\varepsilon$ à `0.01`.
* Dans une boucle :
    * Si $\left| x^2 - N \right| \leq \varepsilon$, alors la boucle s'arrête et on affiche le résultat $x$.
    * Si $x \geq N$, alors la boucle s'arrête et le message d'erreur est affiché.
    * Sinon, on incrémente $x$ de $\varepsilon ^ 2$ et on poursuit la recherche.

## Exercice 2 - Calcul d'une racine carrée en utilisant la dichotomie

Ecrivez un script qui calcule une racine carrée $x \approx \sqrt{N} \pm \varepsilon$ en utilisant la dichotomie.

Le principe consiste à réduire progressivement un interval $\left[ \inf ; \sup \right]$ de telle sorte que cet interval converge vers $\left[ \sqrt{N} - \varepsilon ; \sqrt{N} + \varepsilon \right]$. N'importe quelle valeur dans cet interval est considérée comme un $x$ valable.

De manière intuitive, l'interval va commencer à $[0 ; N]$, puis à chaque étape, on teste la valeur au milieu de cet interval. A chacune de ces étapes, soit on augmente la borne inférieure $\inf$, soit on diminue la borne supérieure $\sup$.

Par exemple, pour $N = 9$ :
* On commence sur l'interval $[0 ; 9]$ et on teste $4.5$.
* L'interval devient $[0 ; 4.5]$ et on teste donc $2.25$.
* L'interval devient $[2.25 ; 4.5]$ et on teste donc $\frac{2.25 + 4.5}{2} = 3.375$.
* L'interval devient $[2.25 ; 3.375]$ et on teste donc $\frac{2.25 + 3.375}{2} = 2.8125$.
* L'interval devient $[2.8125 ; 3.375]$ et on teste donc $\frac{2.8125 + 3.375}{2} = 3.09375$.
* L'interval devient $[2.8125 ; 3.09375]$ et on teste donc $\frac{2.8125 + 3.09375}{2} = 2.953125$.
* L'interval devient $[2.953125 ; 3.09375]$ et on teste donc $\frac{2.953125 + 3.09375}{2} = 3.0234375$.
* L'interval devient $[2.953125 ; 3.0234375]$ et on teste donc $\frac{2.953125 + 3.0234375}{2} = 2.98828125$.
* L'interval devient $[2.98828125 ; 3.0234375]$ et on teste donc $\frac{2.98828125 + 3.0234375}{2} = 3.005859375$.
* L'interval devient $[2.98828125 ; 3.005859375]$ et on teste donc $\frac{2.98828125 + 3.005859375}{2} = 2.997070312$.
* L'interval devient $[2.997070312 ; 3.005859375]$ et on teste donc $\frac{2.997070312 + 3.005859375}{2} = 3.001464843$.
* Or $3.001464843^2 = 9.008791207$, donc si $\varepsilon = 0.01$, alors on a notre résultat.

Le nombre $N$ est obtenu via la fonction `input` et le résultat $x$ est affiché dans la sortie standard.

L'algorithme suit les étapes suivantes :
* On lit la valeur $N$ rétournée par `input`.
* On initialise $\varepsilon$ à `0.01`.
* On initialise $\inf$ à `0`.
* On initialise $\sup$ à $\begin{cases}N, si N > 1 \\ 1, sinon\end{cases}$.
* On initialise $x$ à $\frac{\inf + \sup}{2}$ : on prend le milieu de l'interval.
* Dans une boucle :
    * Si $\left| x^2 - N \right| \leq \varepsilon$, alors la boucle s'arrête et on affiche le résultat $x$.
    * Sinon :
        * Si $x^2 < N$, alors la borne $\inf$ prend la valeur $x$. On est donc dans l'interval $[x ; \sup]$.
        * Sinon, la borne $\sup$ prend la valeur $x$. On est donc dans l'interval $[\inf ; x]$.
        * On met à jour $x$ en calculant à nouveau $\frac{\inf + \sup}{2}$ : on prend le milieu du nouvel interval réduit.

## Exercice 3 - Comparaison des approches

Selon vous, quelle approche de calcul de racine carrée fonctionne le mieux entre :
* une énumération dans un espace de solutions,
* l'utilisation de la dichotomie.

Pourquoi ? Veuillez justifier votre réponse avec des exemples.

## Exercice 4 - Nombre négatif

Que se passe-t-il si l'utilisateur rentre $N = -9$ ?

Que faut-il faire pour éviter cela ?

## Exercice 5 - Calcul d'un logarithme

Ecrivez un script qui calcule un logarithme $x \approx \log_2(N) \pm \varepsilon$ en utilisant la dichotomie.

Pour rappel, un logarithme en base 2 est tel que $2^x = N$. Il s'agit donc, algorithmiquement parlant, d'un problème similaire à celui du calcul d'une racine carrée (pour lequel on avait $x^2 = N$).

Par exemple, pour $N = 8$ :
* On commence sur l'interval $[0 ; 8]$ et on teste $4$.
* L'interval devient $[0 ; 4]$ et on teste donc $2$.
* L'interval devient $[2 ; 4]$ et on teste donc $3$.
* Bingo, $2^3 = 8$ et on a trouvé le résultat exact.

## Exercice 6 - Accélération du calcul de logarithme

Dans l'exercice précédent, nous avons utilisé l'interval de départ $[0 ; N]$ pour commencer la dichotomie. En pratique, il est possible de trouver très rapidement un interval de recherche beaucoup plus petit. Plus l'interval est petit, plus on diminue le nombre d'itérations nécessaires pour trouver un résultat, et plus l'exécution est rapide.

Intuitivement, la raison pour laquelle on peut trouver un meilleur interval de départ est la vitesse à laquelle la fonction puissance évolue :

 $x$  |  $2^x$
:----:|--------:
  0	  |       1
  1	  |       2
  2	  |       4
  3	  |       8
  4	  |      16
  5	  |      32
  6	  |      64
  7	  |     128
  8	  |     256
  9	  |     512
 10	  |    1024
 11   |    2048
 12   |    4096
 13   |    8192
 14   |   16384
 15   |   32768
 16   |   65536
 17   |  131072
 18   |  262144
 19   |  524288
 20   | 1048576

On peut donc commencer par rechercher le plus grand nombre entier $borne$ tel que $2^{borne} < N$.

On pourra ainsi commencer la dichotomie avec l'interval $[borne - 1 ; borne + 1]$ à la place de l'interval $[0 ; N]$.

Par exemple, si on recherche $x = \log_2(N)$ pour $N = 80000$, on peut voir dans le tableau ci-dessus que  $2^{16} = 65536$.

On pourra donc commencer la dichotomie avec l'interval $[15 ; 17]$ à la place de l'interval $[0 ; 80000]$.

Cette technique porte le nom d'**approximations successives** : on trouve d'abord l'interval $[15 ; 17]$ puis on recherche la valeur $x$ par dichotomie, soit environ $16.2877123$.

Réécrivez votre script de calcul de logarithme pour y intégrer l'optimisation initiale sur les bornes.
