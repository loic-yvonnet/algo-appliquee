---
title: "Travail Pratique : Anjou Vélo Vintage avec Scratch 3"
summary: "Travaux Pratiques : Initiation au langage graphique Scratch 3."
category: 01-intro-programmation
permalink: "{{ category }}/tp-01-scratch.html"
url: "{{ url_prefix }}/{{ permalink }}"
layout: layouts/site.njk
---

![Scratch logo](./assets/scratch-logo.png)

[**Scratch**](https://scratch.mit.edu/projects/editor/) est un langage de programmation graphique qui permet de réaliser de petites **histoires animées** ou des **jeux vidéos simples**. Ce langage est particulièrement adapté à l'**apprentissage de la programmation**. Il a été maintes fois été utilisé avec succès pour initier de jeunes enfants au développement logiciel.

Scratch est ludique et drôle à utiliser. Cependant, de **nombreux concepts fondamentaux** à l'ingénierie logicielle se cachent derrière les couleurs chatoyantes et les animaux souriants. On retrouve des concepts comme les structures de contrôle, les variables, les boucles, ou encore les fonctions. On y aborde implicitement la **programmation impérative**, la **programmation orientée-objet**, la **programmation événementielle** et la **programmation concurrente**.

En anglais, "*starting from scratch*" signifie "commencer à partir de rien". En ce sens, Scratch se positionne comme le tout premier langage de programmation de choix quand on n'a jamais fait de développement. En revanche, Scratch n'a pas vocation à être utilisé dans un contexte professionnel, contrairement au **Python**.

Nous allons très prochaintement passer au langage Python, qui est beaucoup plus sérieux. Mais Python n'existe qu'en anglais, et sa version graphique [edublocks](https://app.edublocks.org/) est un peu moins intuitive. Par ailleurs, il existe une multitude de langages de programmation, et c'est toujours intéressant d'en connaître plusieurs.

Scratch ne sera pas un choix possible lors de l'examen final.

L'interface graphique est disponible de Scratch [en ligne](https://scratch.mit.edu/projects/editor/) et nous allons l'utiliser pour réaliser un tout premier programme.

## Tout premier programme Scratch

Si vous n'avez pas encore écrit de programme informatique, vous êtes sur le point de créer le tout premier. Commencez par aller sur [https://scratch.mit.edu/projects/editor/](https://scratch.mit.edu/projects/editor/). Vous allez arriver sur l'éditeur Scratch :

![Editeur](./work-assignment-01/distrib/000-editeur.jpeg)

L'éditeur comporte plusieurs zones :
* **Menu Principal** : permet de créer un nouveau programme, d'en charger en existant, de sauvegarder l'actuel, de changer la langue d'affichage, de revenir en arrière, etc.
* **Menu Secondaire** : permet de naviguer entre la zone de codage, la zone de gestion des graphiques (appelés costumes) et la zone de gestion des sons.
* **Blocs de Code** : Scratch fourni une liste prédéfinie de blocs de code réutilisables dans la zone de programmation.
* **Zone de Programmation** : permet d'écrire un programme Scratch pour donner du comportement au *sprite* sélectionné, en glissant-déposant des blocs de code.
* **Zone de Résultat** : permet d'exécuter le code et d'en visualiser le résultat.
* **Configuration Graphique** : permet de gérer la liste des *sprites* et des *scènes*.

Un "*sprite*" est personnage ou objet animé dans le jeu. Par exemple, le chat (qui s'appelle le "chat Scratch") est un *sprite*. Dans Super Mario Bros (C), les personnages Mario et Luigi sont des *sprites*, ainsi que les ennemis, les briques, les tuyaux, etc. Le décors en fond d'écran avec lequel on ne peut pas interagir n'est pas un *sprite* : il s'agit de la *scène*.

![Zones éditeur](./work-assignment-01/distrib/001-zones-editeur.jpeg)

Vous aller commencer par aller chercher le bloc "Quand *drapeau-vert* est cliqué" dans la catégorie Evénements.

![Glisser déposer bloc](./work-assignment-01/distrib/002-glisser-deposer-bloc.jpeg)

Vous aller ensuite lui ajouter le bloc "Avancer de" dans la catégorie Mouvements. Faites bien attention à ce que le bloc bleu colle le bloc jaune. Si 2 blocs ne sont pas collés, ils ne sont pas en relation.

![Avancer de](./work-assignment-01/distrib/003-avancer-de.jpeg)

Ce programme est très simple. Il indique que lorsque l'on clique sur le drapeau vert dans la Zone de Résultat, le sprite du chat Scratch doit d'avancer de 10 pas. On peut trouver le nom du sprite, ainsi que ses coordonnées juste en-dessous de la Zone de Résultat.

![Test drapeau vert](./work-assignment-01/distrib/004-test-drapeau-vert.jpeg)

Vous pouvez maintenant appuyer sur le drapeau vert pour commencer l'exécution. Notez que le sprite du chat se déplace légèrement vers la droite. Par ailleurs, la nouvelle coordonnée x est désormais égale à 10.

![Commencer](./work-assignment-01/distrib/005-commencer.jpeg)

Relancer plusieurs l'exécution en appuyant plusieurs fois sur le drapeau vert. Observez le déplacement progressif du chat Scratch vers la droite.

![Quelques executions](./work-assignment-01/distrib/006-quelques-executions.jpeg)

En pratique, la scène peut être considérée comme un système d'axe à 2 dimensions dont le centre O(0, 0) se situe au milieu.

![Coordonnees](./work-assignment-01/distrib/007-coordonnees.jpeg)

Vous pouvez maintenant sauvegarder ce tout premier programme sur votre ordinateur. Le format de fichier de Scratch est le sb3.

![Sauvegarder](./work-assignment-01/distrib/008-sauvegarder.jpeg)

Notez qu'il est possible de supprimer un bloc dans la Zone de Programmation en effectuant un clic-droit, puis en sélectionnant "Supprimer le bloc". Cela peut s'avérer utile en cas d'erreur.

![Supprimer bloc](./work-assignment-01/distrib/009-supprimer-bloc.jpeg)

De même, il est possible de supprimer un sprite en cliquand sur l'icône de poubelle située en haut à droite de l'icône de sprite dans la zone Configuration Graphique.

![Suppression sprite](./work-assignment-01/distrib/010-suppression-sprite.jpeg)

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

Maintenant, il vous faut un décor. Vous décidez d'utiliser le plan de Saumur en 1814, bien que ce soit relativement anachronique par rapport à l'Anjou Vélo Vintage. Vous trouvez ce plan sur le site [Saumur Jadis](https://saumur-jadis.pagesperso-orange.fr/) : [https://saumur-jadis.pagesperso-orange.fr/plans/plan1814.jpg](https://saumur-jadis.pagesperso-orange.fr/plans/plan1814.jpg).

## Programmation de base du jeu

Retournez sur dans l'[éditeur Scratch](https://scratch.mit.edu/projects/editor/). Cliquez sur Fichier > Nouveau.

![Nouveau](./work-assignment-01/distrib/011-nouveau.jpeg)

Nous n'avons pas besoin du chat Scratch. Nous pouvons donc le supprimer.

![Suppression sprite](./work-assignment-01/distrib/012-suppression-sprite.jpeg)

Voici un aperçu du résultat souhaité à la fin de ce TP. Le code est beaucoup plus complexe dans le premier programme, mais nous allons avancer pas-à-pas.

![Apercu final](./work-assignment-01/distrib/013-apercu-final.jpeg)

Bien que le résultat ne soit pas un jeu AAA comme World of Warcraft (C), il est remarquable de parvenir à finaliser un premier jeu vidéo lors de son tout premier cours d'informatique.

![Apercu execution](./work-assignment-01/distrib/014-apercu-execution.jpeg)

Nous allons commencer par téléverser les éléments graphiques du jeu. Commençons par l'arrière-plan. En bas à droite, cliquez sur "Importer un arrière-plan".

![Choisir scene](./work-assignment-01/distrib/015-choisir-scene.jpeg)

Sélectionnez ensuite plan1814.jpg que vous avez précédemment enregistrer sur votre machine.

![Choisir scene](./work-assignment-01/distrib/016-choisir-scene.jpeg)

Notre arrière-plan apparaît dans le 2e onglet.

![Plan a retravailler](./work-assignment-01/distrib/018-plan-a-retravailler.jpeg)

Il est souhaitable de nettoyer l'arrière-plan vide par défaut. Pour cela, on commence par le sélectionner.

![Choisir plan 1](./work-assignment-01/distrib/019-choisir-plan-1.jpeg)

Puis on clique sur la poubelle.

![Supprimer plan 1](./work-assignment-01/distrib/020-supprimer-plan-1.jpeg)

Comme vous pouvez l'observer dans la Zone de Résultat, le plan importé ne couvre pas toute la largeur. Pour agrandir le plan, vous devons le convertir en vectoriel. Cliquez sur le bouton "Convertir en Vecteur" en bas.

![Convertir plan en vecteur](./work-assignment-01/distrib/021-convertir-plan-en-vecteur.jpeg)

Dans la zone graphique, cliquez sur le plan.

![Selectionner plan](./work-assignment-01/distrib/022-selectionner-plan.jpeg)

En utilisant les manipulateurs, agrandissez le plan pour qu'il couvre toute la largeur de la Zone de Résultat.

![Agrandir plan](./work-assignment-01/distrib/023-agrandir-plan.jpeg)

Cliquez sur "Importer un sprite" et choisissez glamour.png.

![Importer glamour](./work-assignment-01/distrib/024-importer-glamour.jpeg)

Modifiez la taille : mettez 40 à la place de 100.

![Changer taille glamour](./work-assignment-01/distrib/025-changer-taille-glamour.jpeg)

Cliquez dans l'onglet "Costumes" en haut à gauche.

![Aller dans costumes](./work-assignment-01/distrib/026-aller-dans-costumes.jpeg)

Cliquez sur "Importer un Costume" en bas à gauche. Choisissez à nouveau glamour.png.

![Importer costume](./work-assignment-01/distrib/027-importer-costume.jpeg)

Changez le nom du costume : glamour-to-left (ou bien glamour-vers-la-gauche).

![Changer nom costume](./work-assignment-01/distrib/028-changer-nom-costume.jpeg)

Appliquez un mirroir horizontal en cliquant sur le bouton associé.

![Mirroir horizontal](./work-assignment-01/distrib/029-mirroir-horizontal.jpeg)

Choisissez le premier costume. Ensuite, changez le nom du premier costume : glamour-to-right (ou bien glamour-vers-la-droite).

![Maj nom 1er costume](./work-assignment-01/distrib/030-maj-nom-1er-costume.jpeg)

Cliquez à nouveau sur "Importer un sprite" et choisissez logo.png cette fois-ci.

![Importer logo](./work-assignment-01/distrib/031-importer-logo.jpeg)

Modifiez la taille du logo : 25

![Redimensionner logo](./work-assignment-01/distrib/032-redimensionner-logo.jpeg)

Modifiez les coordonnées du logo :
* x : -194
* y : 166

![Resultat redim logo](./work-assignment-01/distrib/033-resultat-redim-logo.jpeg)

Suivez les mêmes étapes pour importer le drapeau représentant une étape du parcours.

![Importer depart](./work-assignment-01/distrib/034-importer-depart.jpeg)

Sélectionnez le sprite glamour afin de l'activer.

![Reselectionner glamour](./work-assignment-01/distrib/035-reselectionner-glamour.jpeg)

Ajoutez le bloc "Quand *drapeau-vert* est cliqué".

![Ajouter quand drapeau vert](./work-assignment-01/distrib/036-ajouter-quand-drapeau-vert.jpeg)

Ajoutez le bloc "Glisser en à x/y" :
* En 1 seconde
* x : -190
* y : 30

Cela permet de repositionner la cycliste à son point de départ à chaque fois que l'on réexécute le jeu.

![Reinit position](./work-assignment-01/distrib/037-reinit-position.jpeg)

Ajoutez le bloc "Basculer sur le costume" et choisissez glamour-to-right (ou glamour-vers-la-droite).

Cela permet de réinitialiser l'orientation de la cycliste pour qu'elle regarde vers la droite lorsque l'on exécute le jeu.

![Reinit costume](./work-assignment-01/distrib/038-reinit-costume.jpeg)

On peut faire une première exécution en cliquant sur le drapeau vert.

![Executer programme](./work-assignment-01/distrib/039-executer-programme.jpeg)
![Quand](./work-assignment-01/distrib/040-quand.jpeg)
![Quand fleche droite](./work-assignment-01/distrib/041-quand-fleche-droite.jpeg)
![Changer costume](./work-assignment-01/distrib/042-changer-costume.jpeg)
![Mettre x a](./work-assignment-01/distrib/042-mettre-x-a.jpeg)
![Operator plus](./work-assignment-01/distrib/043-operator-plus.jpeg)
![Abscisse plus 2](./work-assignment-01/distrib/044-abscisse-plus-2.jpeg)
![Execution](./work-assignment-01/distrib/045-execution.jpeg)
![Duplication](./work-assignment-01/distrib/046-duplication.jpeg)
![Gestion gauche](./work-assignment-01/distrib/047-gestion-gauche.jpeg)
![Execution](./work-assignment-01/distrib/048-execution.jpeg)
![Rebond](./work-assignment-01/distrib/049-rebond.jpeg)
![Haut et bas](./work-assignment-01/distrib/050-haut-et-bas.jpeg)
![Creer variable](./work-assignment-01/distrib/051-creer-variable.jpeg)
![Var peut bouger](./work-assignment-01/distrib/052-var-peut-bouger.jpeg)
![Cache var](./work-assignment-01/distrib/053-cache-var.jpeg)
![Ajout mettre var](./work-assignment-01/distrib/054-ajout-mettre-var.jpeg)
![Peut pas bouger au debut](./work-assignment-01/distrib/055-peut-pas-bouger-au-debut.jpeg)
![Ajout si](./work-assignment-01/distrib/057-ajout-si.jpeg)
![Ajout condition](./work-assignment-01/distrib/058-ajout-condition.jpeg)
![Si peut bouger](./work-assignment-01/distrib/059-si-peut-bouger.jpeg)
![Mouvement ok](./work-assignment-01/distrib/060-mouvement-ok.jpeg)
![Bonjour](./work-assignment-01/distrib/061-bonjour.jpeg)
![Autres textes](./work-assignment-01/distrib/062-autres-textes.jpeg)
![Execution](./work-assignment-01/distrib/063-execution.jpeg)
![Sauvegarder](./work-assignment-01/distrib/064-sauvegarder.jpeg)
![Aller dans depart](./work-assignment-01/distrib/065-aller-dans-depart.jpeg)
![Quand drapeau vert](./work-assignment-01/distrib/066-quand-drapeau-vert.jpeg)
![Creer variable](./work-assignment-01/distrib/067-creer-variable.jpeg)
![Var nb drapeaux touches](./work-assignment-01/distrib/068-var-nb-drapeaux-touches.jpeg)
![Var total drapeaux](./work-assignment-01/distrib/069-var-total-drapeaux.jpeg)
![Cacher variables](./work-assignment-01/distrib/070-cacher-variables.jpeg)
![Init nb total drapeaux](./work-assignment-01/distrib/071-init-nb-total-drapeaux.jpeg)
![Init nb drap touches](./work-assignment-01/distrib/072-init-nb-drap-touches.jpeg)
![Repeter](./work-assignment-01/distrib/073-repeter.jpeg)
![Operateur moins](./work-assignment-01/distrib/074-operateur-moins.jpeg)
![Creer clone](./work-assignment-01/distrib/075-creer-clone.jpeg)
![Commencement clone](./work-assignment-01/distrib/076-commencement-clone.jpeg)
![Glisser](./work-assignment-01/distrib/077-glisser.jpeg)
![Rebondir](./work-assignment-01/distrib/078-rebondir.jpeg)
![Execution](./work-assignment-01/distrib/079-execution.jpeg)
![Attendre que](./work-assignment-01/distrib/080-attendre-que.jpeg)
![Attendre toucher glamour](./work-assignment-01/distrib/081-attendre-toucher-glamour.jpeg)
![Incremente drapeaux](./work-assignment-01/distrib/082-incremente-drapeaux.jpeg)
![Cacher drapeaux touches](./work-assignment-01/distrib/083-cacher-drapeaux-touches.jpeg)
![Retourner cote glamour](./work-assignment-01/distrib/084-retourner-cote-glamour.jpeg)
![Var temps total](./work-assignment-01/distrib/085-var-temps-total.jpeg)
![Reinit chrono](./work-assignment-01/distrib/086-reinit-chrono.jpeg)
![Attendre que](./work-assignment-01/distrib/087-attendre-que.jpeg)
![Drapeaux tous touches](./work-assignment-01/distrib/088-drapeaux-tous-touches.jpeg)
![Maj temps total](./work-assignment-01/distrib/089-maj-temps-total.jpeg)
![Arrondi de](./work-assignment-01/distrib/090-arrondi-de.jpeg)
![Arrondi chrono](./work-assignment-01/distrib/091-arrondi-chrono.jpeg)
![Empeche bouger](./work-assignment-01/distrib/092-empeche-bouger.jpeg)
![Bien arrivee](./work-assignment-01/distrib/093-bien-arrivee.jpeg)
![Dire](./work-assignment-01/distrib/094-dire.jpeg)
![Regrouper](./work-assignment-01/distrib/095-regrouper.jpeg)
![Regrouper 2 fois](./work-assignment-01/distrib/096-regrouper-2-fois.jpeg)
![Afficher temps](./work-assignment-01/distrib/097-afficher-temps.jpeg)
![Execution](./work-assignment-01/distrib/098-execution.jpeg)
![Sons](./work-assignment-01/distrib/099-sons.jpeg)
![Choisir son](./work-assignment-01/distrib/100-choisir-son.jpeg)
![Cheer](./work-assignment-01/distrib/101-cheer.jpeg)
![Autre son](./work-assignment-01/distrib/102-autre-son.jpeg)
![Classical piano](./work-assignment-01/distrib/103-classical-piano.jpeg)
![Retour dans code](./work-assignment-01/distrib/104-retour-dans-code.jpeg)
![Arreter sons](./work-assignment-01/distrib/105-arreter-sons.jpeg)
![Deposer jouer son](./work-assignment-01/distrib/106-deposer-jouer-son.jpeg)
![Choisir cheer](./work-assignment-01/distrib/107-choisir-cheer.jpeg)
![Nouveau drapeau vert](./work-assignment-01/distrib/108-nouveau-drapeau-vert.jpeg)
![Jouer piano](./work-assignment-01/distrib/109-jouer-piano.jpeg)
![Repeter](./work-assignment-01/distrib/110-repeter.jpeg)
![Condition repeter](./work-assignment-01/distrib/111-condition-repeter.jpeg)
![Rejouer en boucle](./work-assignment-01/distrib/112-rejouer-en-boucle.jpeg)
![Retour depart](./work-assignment-01/distrib/113-retour-depart.jpeg)
![Retour son](./work-assignment-01/distrib/114-retour-son.jpeg)
![Laugh1](./work-assignment-01/distrib/115-laugh1.jpeg)
![Code depart](./work-assignment-01/distrib/116-code-depart.jpeg)
![Jouer rires](./work-assignment-01/distrib/117-jouer-rires.jpeg)
