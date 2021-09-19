---
title: "Travail Pratique 1 - Anjou Vélo Vintage avec Scratch 3"
summary: "Travaux Pratiques : Initiation au langage graphique Scratch 3."
category: 01-intro-programmation
permalink: "{{ category }}/tp-01-scratch.html"
url: "{{ url_prefix }}/{{ permalink }}"
layout: layouts/site.njk
---

![Scratch logo](./assets/scratch-logo.png)

[**Scratch**](https://scratch.mit.edu/projects/editor/) est un langage de programmation graphique qui permet de réaliser de petites **histoires animées** ou des **jeux vidéos simples**. Ce langage est particulièrement adapté à l'**apprentissage de la programmation**. Il a été maintes fois utilisé avec succès pour initier de jeunes enfants au développement logiciel.

Scratch est ludique et drôle à utiliser. Cependant, de **nombreux concepts fondamentaux** à l'ingénierie logicielle se cachent derrière les couleurs chatoyantes et les animaux souriants. On retrouve des concepts comme les structures de contrôle, les variables, les boucles, ou encore les fonctions. On y aborde implicitement la **programmation impérative**, la **programmation orientée-objet**, la **programmation événementielle** et la **programmation concurrente**.

En anglais, "*starting from scratch*" signifie "commencer à partir de rien". En ce sens, Scratch se positionne comme le tout premier langage de programmation de choix quand on n'a jamais fait de développement. En revanche, Scratch n'a pas vocation à être utilisé dans un contexte professionnel, contrairement au **Python**.

Nous allons très prochaintement passer au langage Python, qui est beaucoup plus "*sérieux*". Mais Python n'existe qu'en anglais, et sa version graphique [edublocks](https://app.edublocks.org/) est un peu moins intuitive que Scratch. Par ailleurs, il existe une multitude de langages de programmation, et c'est toujours intéressant d'en connaître plusieurs.

Scratch ne sera pas un choix possible lors de l'examen final.

L'interface graphique de Scratch est disponible [en ligne](https://scratch.mit.edu/projects/editor/) et nous allons l'utiliser pour réaliser un tout premier programme.

## Tout premier programme Scratch

Si vous n'avez pas encore écrit de programme informatique, vous êtes sur le point de créer le tout premier. Commencez par aller sur [https://scratch.mit.edu/projects/editor/](https://scratch.mit.edu/projects/editor/). Vous allez arriver sur l'éditeur Scratch :

![Editeur](./work-assignment-01/assets/000-editeur.jpeg)

L'éditeur comporte plusieurs zones :
* **Menu Principal** : permet de créer un nouveau programme, d'en charger en existant, de sauvegarder l'actuel, de changer la langue d'affichage, de revenir en arrière, etc.
* **Menu Secondaire** : permet de naviguer entre la zone de codage, la zone de gestion des graphiques (appelés costumes) et la zone de gestion des sons.
* **Blocs de Code** : Scratch fourni une liste prédéfinie de blocs de code réutilisables dans la zone de programmation.
* **Zone de Programmation** : permet d'écrire un programme Scratch pour donner du comportement au *sprite* sélectionné, en glissant-déposant des blocs de code.
* **Zone de Résultat** : permet d'exécuter le code et d'en visualiser le résultat.
* **Configuration Graphique** : permet de gérer la liste des *sprites* et des *scènes*.

Un "*sprite*" est personnage ou objet animé dans le jeu. Par exemple, le chat (qui s'appelle le "chat Scratch") est un *sprite*. Dans Super Mario Bros (C), les personnages Mario et Luigi sont des *sprites*, ainsi que les ennemis, les briques, les tuyaux, etc. Le décor en fond d'écran avec lequel on ne peut pas interagir n'est pas un *sprite* : il s'agit de la *scène*.

![Zones éditeur](./work-assignment-01/assets/001-zones-editeur.jpeg)

Vous aller commencer par aller chercher le bloc "Quand *drapeau-vert* est cliqué" dans la catégorie Evénements.

![Glisser déposer bloc](./work-assignment-01/assets/002-glisser-deposer-bloc.jpeg)

Vous aller ensuite lui ajouter le bloc "Avancer de" dans la catégorie Mouvements. Faites bien attention à ce que le bloc bleu colle le bloc jaune. Si 2 blocs ne sont pas collés, ils ne sont pas en relation.

![Avancer de](./work-assignment-01/assets/003-avancer-de.png)

Ce programme est très simple. Il indique que lorsque l'on clique sur le drapeau vert dans la Zone de Résultat, le sprite du chat Scratch doit d'avancer de 10 pas. On peut trouver le nom du sprite, ainsi que ses coordonnées juste en-dessous de la Zone de Résultat.

![Test drapeau vert](./work-assignment-01/assets/004-test-drapeau-vert.png)

Vous pouvez maintenant appuyer sur le drapeau vert pour commencer l'exécution. Notez que le sprite du chat se déplace légèrement vers la droite. Par ailleurs, la nouvelle coordonnée x est désormais égale à 10.

![Commencer](./work-assignment-01/assets/005-commencer.png)

Relancer plusieurs l'exécution en appuyant plusieurs fois sur le drapeau vert. Observez le déplacement progressif du chat Scratch vers la droite.

![Quelques executions](./work-assignment-01/assets/006-quelques-executions.png)

En pratique, la scène peut être considérée comme un système d'axe à 2 dimensions dont le centre O(0, 0) se situe au milieu.

![Coordonnees](./work-assignment-01/assets/007-coordonnees.png)

Vous pouvez maintenant sauvegarder ce tout premier programme sur votre ordinateur. Le format de fichier de Scratch est le sb3.

![Sauvegarder](./work-assignment-01/assets/008-sauvegarder.png)

Notez qu'il est possible de supprimer un bloc dans la Zone de Programmation en effectuant un clic-droit, puis en sélectionnant "Supprimer le bloc". Cela peut s'avérer utile en cas d'erreur.

![Supprimer bloc](./work-assignment-01/assets/009-supprimer-bloc.png)

De même, il est possible de supprimer un sprite en cliquand sur l'icône de poubelle située en haut à droite de l'icône de sprite dans la zone Configuration Graphique.

![Suppression sprite](./work-assignment-01/assets/010-suppression-sprite.png)

## Présentation du projet Anjou Vélo Vintage

Tous les ans, une manifestation joyeuse et joviale réunit des cyclistes nostalgiques (ou pas) à [Saumur](https://www.ville-saumur.fr/) : [l'Anjou Vélo Vintage](https://www.anjou-velo-vintage.com/fr/). Le principe est simple : plusieurs courses cyclistes sont proposées et il est nécessaire d'avoir un vélo et de porter des vêtements "vintages" pour y participer.

L'exercice qui suit est un hommage à cette manifestation. Il est à noter que les images et logos utilisés sont la propriété exclusive de la manifestation et de ses organisateurs.

Supposons que vous travaillez pour une ESN (Entreprise de Services du Numérique). Les organisateurs ont fait appel à votre entreprise pour créer un teaser de leur événement sur la forme d'un mini jeu vidéo mettant en scène une cycliste qui doit passer par les différentes étapes de la course. Votre supérieur hiérarchique vient vous voir et vous délègue l'implémentation du jeu.

Fort de votre première expérience avec Scratch, vous décidez d'utiliser ce langage pour réaliser le mini jeu.

## Recueil graphique

La première étape consiste à réaliser une recherche de visuels, car il n'y a pas de graphiste dans votre équipe. Vous décidez d'utiliser les éléments suivants :
* Cycliste glamour que vous trouvez ici : [https://www.anjou-velo-vintage.com/images/dresscode/glamour.png](https://www.anjou-velo-vintage.com/images/dresscode/glamour.png).
* Logo de l'événement que vous trouvez ici : [https://www.anjou-velo-vintage.com/images/logo.png](https://www.anjou-velo-vintage.com/images/logo.png).
* Drapeau représentant une étape de la course que vous trouvez ici : [https://www.anjou-velo-vintage.com/images/esprit-avv/pictos/depart.png](https://www.anjou-velo-vintage.com/images/esprit-avv/pictos/depart.png).

Maintenant, il vous faut un décor. Vous décidez d'utiliser le plan de Saumur en 1814, bien que ce soit relativement anachronique par rapport à l'Anjou Vélo Vintage. Vous trouvez ce plan sur le site [Saumur Jadis](https://saumur-jadis.pagesperso-orange.fr/) : [https://saumur-jadis.pagesperso-orange.fr/plans/plan1814.jpg](https://saumur-jadis.pagesperso-orange.fr/plans/plan1814.jpg). Notez que ce plan est la propriété exclusive des administrateurs du site [Saumur Jadis](https://saumur-jadis.pagesperso-orange.fr/).

## Ajout des éléments graphiques dans Scratch

Retournez sur dans l'[éditeur Scratch](https://scratch.mit.edu/projects/editor/). Cliquez sur Fichier > Nouveau.

![Nouveau](./work-assignment-01/assets/011-nouveau.png)

Nous n'avons pas besoin du chat Scratch. Nous pouvons donc le supprimer.

![Suppression sprite](./work-assignment-01/assets/012-suppression-sprite.png)

Voici un aperçu du résultat souhaité à la fin de ce TP. Le code est beaucoup plus complexe dans le premier programme, mais nous allons avancer pas-à-pas.

![Apercu final](./work-assignment-01/assets/013-apercu-final.jpeg)

Bien que le résultat ne soit pas un jeu AAA comme World of Warcraft (C), il est remarquable de parvenir à finaliser un premier jeu vidéo lors de son tout premier cours d'informatique.

![Apercu execution](./work-assignment-01/assets/014-apercu-execution.jpeg)

Nous allons commencer par téléverser les éléments graphiques du jeu. Commençons par l'arrière-plan. En bas à droite, cliquez sur "Importer un arrière-plan".

![Choisir scene](./work-assignment-01/assets/015-choisir-scene.png)

Sélectionnez ensuite plan1814.jpg que vous avez précédemment enregistrer sur votre machine.

![Choisir scene](./work-assignment-01/assets/016-choisir-scene.png)

Notre arrière-plan apparaît dans le 2e onglet.

![Plan a retravailler](./work-assignment-01/assets/018-plan-a-retravailler.jpeg)

Il est souhaitable de nettoyer l'arrière-plan vide par défaut. Pour cela, on commence par le sélectionner.

![Choisir plan 1](./work-assignment-01/assets/019-choisir-plan-1.png)

Puis on clique sur la poubelle.

![Supprimer plan 1](./work-assignment-01/assets/020-supprimer-plan-1.png)

Comme vous pouvez l'observer dans la Zone de Résultat, le plan importé ne couvre pas toute la largeur. Pour agrandir le plan, vous devons le convertir en vectoriel. Cliquez sur le bouton "Convertir en Vecteur" en bas.

![Convertir plan en vecteur](./work-assignment-01/assets/021-convertir-plan-en-vecteur.jpeg)

Dans la zone graphique, cliquez sur le plan.

![Selectionner plan](./work-assignment-01/assets/022-selectionner-plan.jpeg)

En utilisant les manipulateurs, agrandissez le plan pour qu'il couvre toute la largeur de la Zone de Résultat.

![Agrandir plan](./work-assignment-01/assets/023-agrandir-plan.jpeg)

Cliquez sur "Importer un sprite" et choisissez glamour.png.

![Importer glamour](./work-assignment-01/assets/024-importer-glamour.png)

Modifiez la taille : mettez 40 à la place de 100.

![Changer taille glamour](./work-assignment-01/assets/025-changer-taille-glamour.jpeg)

Cliquez dans l'onglet "Costumes" en haut à gauche.

![Aller dans costumes](./work-assignment-01/assets/026-aller-dans-costumes.jpeg)

Cliquez sur "Importer un Costume" en bas à gauche. Choisissez à nouveau glamour.png.

![Importer costume](./work-assignment-01/assets/027-importer-costume.jpeg)

Changez le nom du costume : glamour-to-left (ou bien glamour-vers-la-gauche).

![Changer nom costume](./work-assignment-01/assets/028-changer-nom-costume.png)

Appliquez un mirroir horizontal en cliquant sur le bouton associé.

![Mirroir horizontal](./work-assignment-01/assets/029-mirroir-horizontal.jpeg)

Choisissez le premier costume. Ensuite, changez le nom du premier costume : glamour-to-right (ou bien glamour-vers-la-droite).

![Maj nom 1er costume](./work-assignment-01/assets/030-maj-nom-1er-costume.jpeg)

Cliquez à nouveau sur "Importer un sprite" et choisissez logo.png cette fois-ci.

![Importer logo](./work-assignment-01/assets/031-importer-logo.png)

Modifiez la taille du logo : 25

![Redimensionner logo](./work-assignment-01/assets/032-redimensionner-logo.jpeg)

Modifiez les coordonnées du logo :
* x : -194
* y : 166

![Resultat redim logo](./work-assignment-01/assets/033-resultat-redim-logo.jpeg)

Suivez les mêmes étapes pour importer le drapeau représentant une étape du parcours.

![Importer depart](./work-assignment-01/assets/034-importer-depart.jpeg)

Sélectionnez le sprite glamour afin de l'activer.

![Reselectionner glamour](./work-assignment-01/assets/035-reselectionner-glamour.png)

## Initialisation de la scène

Le code source du jeu vidéo est nettement plus complexe que celui de votre tout premier programme. Aidez-vous des couleurs et des formes des blocs pour reproduire le programme pas-à-pas.

A ce stade, il est tout-à-fait normal de ne pas encore comprendre toutes les subtilités de la programmation. Il est possible d'appréhender ce TP comme un simple puzzle ou Lego (R) : il suffit d'assembler les pièces comme indiqué pour parvenir au résultat souhaité.

Ajoutez le bloc `quand `*drapeau-vert*` est cliqué`.

![Ajouter quand drapeau vert](./work-assignment-01/assets/036-ajouter-quand-drapeau-vert.png)

Ajoutez le bloc `glisser en à x ; y` :
* En 1 seconde
* x : -190
* y : 30

Cela permet de repositionner la cycliste à son point de départ à chaque fois que l'on réexécute le jeu.

![Reinit position](./work-assignment-01/assets/037-reinit-position.png)

Ajoutez le bloc `basculer sur le costume` et choisissez glamour-to-right (ou glamour-vers-la-droite).

Cela permet de réinitialiser l'orientation de la cycliste pour qu'elle regarde vers la droite lorsque l'on exécute le jeu.

![Reinit costume](./work-assignment-01/assets/038-reinit-costume.png)

On peut faire une première exécution en cliquant sur le drapeau vert. On pourra alors observer la cycliste se déplacer en 1s vers la position initiale souhaitée.

Si vous n'observez pas de déplacement, cela signifie tout simplement qu'elle se trouve déjà à sa position initiale.

![Executer programme](./work-assignment-01/assets/039-executer-programme.jpeg)

On souhaite donner au joueur la possibilité de déplacer la cycliste. Pour ce faire, on va utiliser les flèches du clavier : les touches haut, bas, droite et gauche. Pour cela, on va réagir à des événements clavier grâce à des blocs qui représentent ces événements.

Rajoutez un bloc `quand la touche` dans la Zone de Programmation. Ce bloc ne s'imbrique pas avec le reste et doit rester indépendant dans un premier temps. On remarque au passage que les programmes Scratch se construisent comme des Lego (R). Certaines pièces sont faites pour s'assembler, et d'autres non.

## Gestion des touches clavier

![Quand](./work-assignment-01/assets/040-quand.png)

Par défaut, le bloc `quand la touche` réagit à un appuie sur la touche espace. Choisissez plutôt la flèche droite à la place.

![Quand fleche droite](./work-assignment-01/assets/041-quand-fleche-droite.png)

Quand l'utilisateur appuie sur la flèche droite de son clavier, la cycliste doit partir vers la droite. On doit donc l'orienter vers la droite.

Pour cela, connectez un bloc `changer costume` et choisissez "glamour-to-right" ou "glamour-vers-la-droite".

![Changer costume](./work-assignment-01/assets/042-changer-costume.png)

Ensuite, on souhaite que la cycliste se déplace vers la droite. Un déplacement vers la droite correspond à l'application d'un vecteur (x, 0). Autrement dit, on va incrémenter l'abscisse du sprite représentant la cycliste.

Rajoutez un bloc `mettre x à`.

![Mettre x a](./work-assignment-01/assets/042-mettre-x-a.png)

A l'intérieur du bloc `mettre x à`, glissez-déposez un bloc d'addition. Faites bien attention à le mettre à l'intérieur, comme sur la capture d'écran ci-dessous.

![Operator plus](./work-assignment-01/assets/043-operator-plus.png)

Dans le bloc d'addition, vous allez ajouter en opérande le bloc `abscisse x`. Comme son nom l'indique, cela représente l'abscisse du sprite de la cycliste à un instant donné.

Toujours dans le bloc d'addition, vous allez rentrer la valeur `2` comme seconde opérande. La séquence se lit donc de la manière suivante : "lorsque l'utilisateur appuie sur la flèche droite, change l'orientation du sprite et déplace le de 2 unités en x (donc vers la droite)".

![Abscisse plus 2](./work-assignment-01/assets/044-abscisse-plus-2.png)

Relancez l'exécution à nouveau. Appuyez sur la flèche droite du clavier et observer le personnage évoluer vers la droite.

![Execution](./work-assignment-01/assets/045-execution.jpeg)

On souhaite maintenant pouvoir déplacer notre sprite également à gauche, en bas et en haut, afin de pouvoir explorer l'ensemble de la zone de jeu. On pourrait refaire l'exercice 3 fois. Cela étant, on peut aussi dupliquer le travail réaliser et l'adapter.

Faites un clic droit sur le bloc `quand la touche` puis cliquez sur "Dupliquer".

![Duplication](./work-assignment-01/assets/046-duplication.png)

Il ne reste plus qu'à adapter les valeurs comme sur la capture d'écran ci-dessous. Faites attention au bloc de soustraction qui doit venir remplacer le bloc d'addition.

![Gestion gauche](./work-assignment-01/assets/047-gestion-gauche.png)

Relancez l'exécution pour vérifier que vous pouvez déplacer la cycliste à gauche et à droite.
Tentez notamment de la déplacer au-délà des limites de l'écran. Observez qu'elle peut parfaitement en sortir.

![Execution](./work-assignment-01/assets/048-execution.jpeg)

Dans ce jeu, on considère que sortir de l'écran n'est pas souhaitable. Vous allez donc corriger ce problème en rajoutant un bloc `rebondir si le bord est atteint`. Pensez à bien mettre ce bloc pour la gestion des 2 événements : gauche et droite.

N'hésitez à relancer l'exécution (drapeau vert) pour vérifier le comportement. Maintenant, la cycliste ne doit plus pouvoir sortir de l'écran.

![Rebond](./work-assignment-01/assets/049-rebond.png)

En vous inspirant des précédentes actions pour gérer les événements gauche et droite, ajoutez les blocs nécessaires pour aller en bas et en haut.

![Haut et bas](./work-assignment-01/assets/050-haut-et-bas.png)

## Eviter un conflit de déplacement

Pendant la première seconde de jeu, on réinitialise la position de notre cycliste. Cependant, durant ce même laps de temps, le joueur a déjà la possibilité d'appuyer sur les flèches de son clavier. Lorsque cela survient, on fait face à un conflit. En effet, d'un côté, un appuie sur une flèche provoque un déplacement relatif par rapport à la position actuelle du sprite. D'un autre côté, le sprite tente d'aller exactement en même temps à une position fixe pré-définie. Ces 2 demandes de déplacement sont en contradiction : on nomme cela un problème de concurrence.

Pour prévenir ce problème, vous allez attendre que le déplacement initial soit terminé avant de prendre en compte l'appuie sur les flèches du clavier.

Dans la zone des Blocs de Code, cliquez sur le bouton "Créez une variable".

![Creer variable](./work-assignment-01/assets/051-creer-variable.png)

Dans le menu qui s'ouvre, remplissez le champ avec la valeur "peutBouger" puis cliquez sur Ok.

![Var peut bouger](./work-assignment-01/assets/052-var-peut-bouger.png)

Toujours dans la zone des Blocs de Code, décochez la variable "peutBouger". Cela permet de ne pas l'afficher dans la Zone de Résultat.

![Cache var](./work-assignment-01/assets/053-cache-var.png)

Ajoutez le bloc `mettre ma variable à` directement sous le block `quand `*drapeau-vert*` est cliqué`. Vous pouvez jouer avec le magnétisme des blocs pour insérer un nouveau blocs entre 2 blocs déjà connectés.

![Ajout mettre var](./work-assignment-01/assets/054-ajout-mettre-var.png)

Dans la liste, vous allez choisir "peutBouger" à la place de "ma variable". Dans la zone de texte à droite, vous allez rentrer "faux". Le bloc doit donc contenir "mettre peutBouger à faux".

Rajoutez à nouveau un bloc `mettre ma variable` à la fin de la séquence. Cette fois-ci, la bloc doit contenir "mettre peutBouger à vrai".

Autrement dit, tant que le sprite de cycliste n'a pas atteint sa position initiale, la variable "peutBouger" est valué à "faux". Dès que ce déplacement initial est terminé, la variable "peutBouger" prend la valeur "vrai".

![Peut pas bouger au debut](./work-assignment-01/assets/055-peut-pas-bouger-au-debut.png)

On souhaite maintenant que les événements de gestion des flèches du clavier ne fassent rien tant que la variable "peutBouger" est égale à "faux".

Ajoutez un bloc `si` qui va encadrer tous les blocs situés sous le bloc `quand la touche flèche haut est pressée`. Aidez-vous du magnétisme des blocs.

![Ajout si](./work-assignment-01/assets/057-ajout-si.png)

A l'intérieur du bloc `si`, vous devez ajouter un bloc de `condition d'égalité`. Ce bloc comporte 2 opérandes qui doivent être égales afin que les blocs internes soient exécutés.

![Ajout condition](./work-assignment-01/assets/058-ajout-condition.png)

Toujours à l'intérieur du bloc `si`, la première opérande du bloc de `condition d'égalité` est la variable "peutBouger". La seconde opérande est le texte "vrai".

La manière de lire cette séquence de blocs est désormais : lorsque la flèche haute du clavier est pressée, si la variable peutBouger est vraie, alors déplace le sprite de cycliste vers le haut et rebondie si le bord est atteint.

![Si peut bouger](./work-assignment-01/assets/059-si-peut-bouger.png)

Reproduisez le même schéma pour les autres événements.

![Mouvement ok](./work-assignment-01/assets/060-mouvement-ok.png)

## Afficher du texte

La gestion des entrées/sorties est importante en programmation logicielle. Afin d'informer un utilisateur, on souhaite souvent afficher un texte à l'écran.

Dans le cas présent, on souhaite informer le joueur de l'objectif du jeu et de le scénariser.

Insérez un bloc `dire pendant` juste au-dessus de `mettre peutBouger à vrai`. Faites dire "Bonjour !" pendant 2 secondes.

![Bonjour](./work-assignment-01/assets/061-bonjour.png)

De la même manière, rajoutez d'autres textes à faire dire à notre cycliste avant qu'elle ne parte :
* Bonjour ! (2 secondes)
* Allons nous ballader dans le Saumurois ! (3 secondes)
* Chaque drapeau représente une étape de notre voyage... (3 secondes)
* Allons-y ! (2 secondes)
* 3... (1 seconde)
* 2... (1 seconde)
* 1... (1 seconde)
* Partez ! (1 sconde)

![Autres textes](./work-assignment-01/assets/062-autres-textes.png)

Vérifiez que tout se passe comme prévu. Vérifiez notamment que vous ne pouvez pas déplacer le sprite de la cycliste avant que cette dernière n'ait dit "Partez !" (ou quelque soit le dernier texte que vous ayez choisi de lui faire dire).

![Execution](./work-assignment-01/assets/063-execution.jpeg)

Vous avez maintenant atteint un stade où le sprite se déplace convenablement après une initialisation complète. Il est temps de sauvegarder votre travail.

![Sauvegarder](./work-assignment-01/assets/064-sauvegarder.png)

## Gestion des collisions : attraper les drapeaux

L'étape suivante consiste à multiplier les drapeaux, les positionner à des emplacements aléatoires et à permettre à votre cycliste d'attraper ces drapeaux. Le fait de réagir à l'intersection entre 2 sprites s'appelle la gestion des collisions.

Dans la zone de Configuration Graphique, cliquez sur le sprite nommé "départ" qui est représenté par un drapeau. Notez que l'icône en haut à droite de la Zone de Programmation a été mise à jour. Vous programmez maintenant le comportement du sprite départ.

![Aller dans depart](./work-assignment-01/assets/065-aller-dans-depart.png)

Ajoutez un bloc `quand `*drapeau-vert*` est cliqué`.

![Quand drapeau vert](./work-assignment-01/assets/066-quand-drapeau-vert.png)

Cliquez sur le bouton "Créer une variable".

![Creer variable](./work-assignment-01/assets/067-creer-variable.png)

Renseignez "nbDrapeauxTouches" comme nom de variable et cliquez sur Ok. Attention à ne pas utiliser d'accent, ni d'espace ni de caractère spécial : il s'agit bien de nbDrapeauxTouch**e**s, sans accent.

![Var nb drapeaux touches](./work-assignment-01/assets/068-var-nb-drapeaux-touches.png)

Créez une autre variable et appelez-la "nbTotalDrapeaux".

![Var total drapeaux](./work-assignment-01/assets/069-var-total-drapeaux.png)

Cachez ces 2 variables en les décochant.

![Cacher variables](./work-assignment-01/assets/070-cacher-variables.png)

Ajoutez un bloc `mettre ma variable à` et changez ses paramètres pour donner : mettre nbTotalDrapeaux à 6.

![Init nb total drapeaux](./work-assignment-01/assets/071-init-nb-total-drapeaux.png)

Ajoutez un bloc `mettre ma variable à` et changez ses paramètres pour donner : mettre nbDrapeauTouches à 0.

![Init nb drap touches](./work-assignment-01/assets/072-init-nb-drap-touches.png)

Ajoutez un bloc `répétez fois`.

![Repeter](./work-assignment-01/assets/073-repeter.png)

A l'intérieur du bloc `répétez fois`, ajouter un `bloc de soustraction`.

![Operateur moins](./work-assignment-01/assets/074-operateur-moins.png)

Les opérandes du `bloc de soustraction` sont :
* La variable nbTotalDrapeaux,
* 1.

A l'intérieur du bloc `répéter`, rajoutez un bloc `créer un clone de moi-même`.

Ainsi, on va créer 6 - 1 = 5 clones du sprite nommé départ. Initialement, tous ses sprites partagent la même position. Ils sont donc les uns sur les autres.

![Creer clone](./work-assignment-01/assets/075-creer-clone.png)

Rajoutez un bloc indépendant `quand je commence comme un clone`.

![Commencement clone](./work-assignment-01/assets/076-commencement-clone.png)

Ajoutez, à ce bloc indépendant, un bloc `glisser en 1 seconde à position aléatoire`.

![Glisser](./work-assignment-01/assets/077-glisser.png)

Comme pour notre cycliste, on va éviter que nos drapeaux sortent de l'écran. On va donc les faire rebondir. Ce n'est pas idéal car on peut se retrouver avec des drapeaux à l'envers, mais c'est toujours mieux que de ne pas pouvoir les voir, ne pas pouvoir les attraper et donc ne pas pouvoir finir le jeu.

Ajoutez un bloc `rebondir si le bord est atteint`.

![Rebondir](./work-assignment-01/assets/078-rebondir.png)

En exécutant à nouveau le jeu, vous devriez voir 5 drapeaux se déplacer à des positions aléatoires.

Faites les essais suivant :
* Initialisez la variable nbTotalDrapeaux à 10 : que se passe-t-il ?
* Initialisez la variable nbTotalDrapeaux à 100 : que se passe-t-il ?

![Execution](./work-assignment-01/assets/079-execution.jpeg)

Rajoutez un bloc `attendre jusqu'à ce que` sous les 2 séquences.

![Attendre que](./work-assignment-01/assets/080-attendre-que.png)

A l'intérieur des blocs `attendre jusqu'à ce que`, ajoutez un sous-bloc `touche le` et choisissez le paramètre "glamour". Cela signifie que les blocs suivants ne seront pas exécutés tant que le sprite courant (ou l'un de ses clones) ne soit touché par le sprite de votre cycliste.

![Attendre toucher glamour](./work-assignment-01/assets/081-attendre-toucher-glamour.png)

Dans les 2 cas, ajoutez un bloc `ajouter à` afin d'ajouter 1 à la variable nbDrapeauxTouches.

![Incremente drapeaux](./work-assignment-01/assets/082-incremente-drapeaux.png)

Ajoutez un bloc `cacher` pour faire disparaître les drapeaux une fois qu'ils sont touchés.

Ajoutez un bloc `montrer` au début pour le sprite original pour le montrer à nouveau après une exécution où il aurait été touché (et donc caché).

![Cacher drapeaux touches](./work-assignment-01/assets/083-cacher-drapeaux-touches.png)

Si vous réexécutez le jeu, vous verrez que les drapeaux disparaissent lorsque la cycliste les touche. Par contre, il ne se passe rien de spécial quand tous les drapeaux ont été attrapés.

## Gérer la fin du jeu

Lorsque tous les drapeaux ont été attrapés, on veut stopper le jeu et afficher des messages de récompense. On souhaite également afficher le temps mis pour attraper tous les drapeaux, afin de mettre en avant un challenge.

Retournez dans le sprite "glamour" pour ajouter plus de comportements à notre cycliste.

![Retourner cote glamour](./work-assignment-01/assets/084-retourner-cote-glamour.png)

Créez une nouvelle variable nommée tempsTotal.

![Var temps total](./work-assignment-01/assets/085-var-temps-total.png)

En bas de la séquence principale, ajoutez un bloc `réinitialiser le chronomètre`.

![Reinit chrono](./work-assignment-01/assets/086-reinit-chrono.png)

Ajoutez un bloc `attendre jusqu'à ce que`

![Attendre que](./work-assignment-01/assets/087-attendre-que.png)

A l'intérieur du bloc `attendre jusqu'à ce que`, insérez un bloc de `condition d'égalité`. Les opérandes de ce dernier bloc sont :
* nbDrapeauxTouches
* nbTotalDrapeaux

Autrement dit, les blocs suivants ne seront exécutés qu'une fois que la cycliste aura touché tous les drapeaux affichés dans la scène.

![Drapeaux tous touches](./work-assignment-01/assets/088-drapeaux-tous-touches.png)

Ajoutez un bloc `mettre ma variable à` et utilisez tempsTotal.

![Maj temps total](./work-assignment-01/assets/089-maj-temps-total.png)

Ajoutez un sous-bloc `arrondi de`.

![Arrondi de](./work-assignment-01/assets/090-arrondi-de.png)

Utilisez le bloc `chronomètre` en paramètre d'`arrondi de`.

En d'autres termes, une fois que la cycliste a touché tous les drapeaux, on regarde notre chronomètre et on inscrit sa valeur (arrondie).

![Arrondi chrono](./work-assignment-01/assets/091-arrondi-chrono.png)

Utilisez un nouveau bloc `mettre ma variable à` pour mettre la variable peutBouger à faux. En effet, une fois que le jeu est fini, on ne doit plus pouvoir bouger le personnage.

![Empeche bouger](./work-assignment-01/assets/092-empeche-bouger.png)

On va maintenant afficher des messages d'une part pour scénariser la fin du jeu et d'autre part pour rendre compte du résultat du joueur : son chrono.

Ajoutez un bloc `pensez à pendant` en rajoutant un message du type : "Trop fière d'être arrivée !".

![Bien arrivee](./work-assignment-01/assets/093-bien-arrivee.png)

Ajoutez un bloc `dire`.

![Dire](./work-assignment-01/assets/094-dire.png)

Dans le bloc `dire`, ajoutez un sous-bloc `regrouper`.

![Regrouper](./work-assignment-01/assets/095-regrouper.png)

Dans le sous-bloc `regrouper`, ajoutez un sous-sous-bloc `regrouper`. Nous avons maintenant 3 champs.

![Regrouper 2 fois](./work-assignment-01/assets/096-regrouper-2-fois.png)

Remplissez les 3 champs comme suit :
* "J'ai mis "
* Bloc variable `tempsTotal`
* " secondes !"

![Afficher temps](./work-assignment-01/assets/097-afficher-temps.png)

Vous avez maintenant un jeu complet avec une vraie gestion des collisions. N'hésitez à l'exécuter plusieurs fois et à changer quelques paramètres pour observer les différences. Vous auriez aussi intérêt à sauvegarder votre travail.

![Execution](./work-assignment-01/assets/098-execution.jpeg)

## Son

L'ajout de son à un jeu fournit une touche finale importante pour l'ambiance.

Dirigez-vous vers le 3e onglet du Menu Secondaire, intitulé Sons.

![Sons](./work-assignment-01/assets/099-sons.png)

Pour le son, vous allez utiliser directement la bibliothèque de base de Scratch.

Cliquez sur Choisir un son.

![Choisir son](./work-assignment-01/assets/100-choisir-son.png)

Cliquez sur le filtre Voix, puis sélectionnez Cheer.

![Cheer](./work-assignment-01/assets/101-cheer.png)

Ajoutez un autre son.

![Autre son](./work-assignment-01/assets/102-autre-son.png)

Cliquez sur le filtre Boucle, puis sélectionnez Classical Piano.

![Classical piano](./work-assignment-01/assets/103-classical-piano.png)

Retournez dans l'onglet Code.

![Retour dans code](./work-assignment-01/assets/104-retour-dans-code.png)

Ajoutez un bloc `arrêtez tous les sons` sous le bloc `mettre peutBouger à faux` afin de stopper la musique d'ambiance lorsque le jeu est fini.

![Arreter sons](./work-assignment-01/assets/105-arreter-sons.jpeg)

Ajoutez tout de suite après un bloc `jouer le son`.

![Deposer jouer son](./work-assignment-01/assets/106-deposer-jouer-son.jpeg)

Choisissez "Cheer".

![Choisir cheer](./work-assignment-01/assets/107-choisir-cheer.jpeg)

Rajoutez un nouveau bloc quand `*drapeau-vert*` est cliqué, indépendant de tout le reste.

![Nouveau drapeau vert](./work-assignment-01/assets/108-nouveau-drapeau-vert.png)

Ajoutez-lui un bloc `jouer le son Classical Piano jusqu'au bout`.

![Jouer piano](./work-assignment-01/assets/109-jouer-piano.png)

Connectez un bloc `répéter jusqu'à ce que`.

![Repeter](./work-assignment-01/assets/110-repeter.png)

Utilisez un bloc conditionnel pour comparer nbDrapeauxTouches et nbTotalDrapeaux. 

![Condition repeter](./work-assignment-01/assets/111-condition-repeter.png)

A l'intérieur, rajouter à nouveau un `jouer le son Classical Piano jusqu'au bout`. Cela permet de jouer en boucle le même son.

![Rejouer en boucle](./work-assignment-01/assets/112-rejouer-en-boucle.png)

Maintenant, on souhaite jouer un son particulier lorsque la cycliste attrape un drapeau.

Retournez dans le sprite nommé "départ", et qui correspond au drapeau.

![Retour depart](./work-assignment-01/assets/113-retour-depart.png)

Allez dans l'onglet Sons.

![Retour son](./work-assignment-01/assets/114-retour-son.png)

Rajoutez un son depuis la catégorie Voix et choisir Laugh1.

![Laugh1](./work-assignment-01/assets/115-laugh1.png)

Retournez dans le code.

![Code depart](./work-assignment-01/assets/116-code-depart.png)

Ajoutez les derniers blocs `jouer le son Laugh1` pour le cas nominal, et le cas des clones.

![Jouer rires](./work-assignment-01/assets/117-jouer-rires.png)

Félicitations, vous venez de réaliser votre premier jeu vidéo. Pensez à bien le sauvegarder et faites-le essayer à tous vos amis (*) !

Veuillez ne pas publier ce contenu sur Internet pour des raisons de droit d'auteur. En effet, les images sont la propriété exclusive de [Saumur Jadis](https://saumur-jadis.pagesperso-orange.fr/) et d'[Anjou Vélo Vintage](https://www.anjou-velo-vintage.com/fr/).

(*) sauf en salle de classe !