# Évaluation du site de Alice, Kenza, Liza et Shami

## Attractivité (UI) /5
**3/5** : Le design du site est un peu simple (fond blanc, pas de footer). Le logo est chouette et recherché, mais il n'est pas assez visible/gros. L'expérience utilisateur est intuitive et simple.

## Robustesse /5
**3.5/5** : Une fois que l'application est installée, tout fonctionne. Cependant, l'installation de l'application a posé problème (nous n'avons pu l'installer correctement que sur 1 machine sur 3 et le `requirements.txt` a dû être modifié pour se faire). De plus, il faut installer de nombreuses bibliothèques Python avec des problèmes de compatibilité entre elles.

## Qualités pragmatiques : clarté, efficacité, structuration, contrôle /5
**4.5/5** : Le site est facile et simple d'utilisation. Il y a juste un petit bémol → les boutons de copie des traductions manquent d'interactivité : on ne voit pas si on a bien cliqué dessus (pas de changement de la souris à la main ni d'information "texte copié"). De même, le logo cliquable ne renvoie à rien (#).

## Utilisabilité par les cibles de l'application ? /5
**4.5/5** : Le site répond bien à son objectif initial. Tout étant sur une seule page, l'utilisateur ne peut que aller au bout de la tâche. Il manquerait juste une indication de la langue source détectée par les différentes API (test sur le tuwari qui a donné des traductions alors qu'aucun traducteur automatique n'existe pour cette langue).

# Total : 15.5/20

## Observations faites lors du test
### Installation de l'application
- Trop de packages dans le fichier requirement
- Problème de compatibilité avec `fastapi==0.111.0` et `googletrans==3.0.0`

### Lancement de l'application
+ Fichier `start.sh` qui facilite le lancement de l'application
- Téléchargement lourd des packages pour la première utilisation de l'application

### Esthétique du site
- Logo chouette et recherché
- Le site est simple, pas forcément accrocheur
- Petit bouton `commencer` très appréciable
- S'adapte plutôt bien à la taille de l'écran

### Utilisation du site
- Petit problème d'interactivité : la souris ne change pas quand on clique sur l'un des boutons (copier par exemple), on ne sait donc pas si l'action a fonctionné
- Ordi d'Agathe: lorsqu'on modifie une traduction et qu'on appuie sur la petite étoile, la traduction ne se met pas dans "mes traductions" (problème de cache ?); `GoogleTrans` ne fonctionne pas du tout (alors que tout a été installé et que l'application a été lancé avec `start.sh`)
- Ordi d'Agathe (`update`) : après avoir essayé de réinstaller dans un nouvel environnement virtuel, plus rien ne fonctionne...
- Ordi de Florian: tout marche correctement
- Ce serait bien d'avoir un module pour savoir si la langue d'origine a bien été détectée
- Peu de clics nécessaires
- Très simple d'utilisation et instinctif
- Le logo renvoie simplement sur la page en cours (#)
