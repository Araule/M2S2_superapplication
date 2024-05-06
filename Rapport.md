# M2S2_superapplication

Lien cahier des charges et notes : https://codimd.math.cnrs.fr/fKyJ-j26QqOfg0B82SRopg?both

## Présentation du projet
Ce projet d'application a été réalisé dans le cadre du cours Techniques Web du Master de Traitement Automatique des Langues (TAL) de l'Inalco. L'idée était de déployer une application autour du TAL, dans laquelle nous pourrions mettre en avant ce que nous avons vu en cours : programmation avec FastAPI, HTML, CSS, Javascript et Jquery. Aussi, nous avons décidé de développer un dictionnaire multilingue chinois/japonais/coréen

Ces trois langues, bien qu'ayant des systèmes d'écriture et des grammaires différentes, partagent un certain nombre caractères communs, connus sous le nom de hanja en coréen et de kanji en japonais. Il existe également un vocabulaire commun, souvent emprunté au chinois, avec des lectures similaires ou identiques.

L'idée derrière une telle application est que de nombreux apprenants de ces langues rencontrent des difficultés à mémoriser les caractères et à comprendre les nuances de sens qu'ils peuvent exprimer dans chaque langue. En outre, les ressources existantes traitent généralement ces langues de manière isolée, sans mettre en évidence leurs liens et leurs similitudes, d'où cette approche plurilingue.

## Cahier des charges

### Les objectifs et le public cible

L'objectif était donc de créer une application dans laquelle l'utilisateur pourrait faire une recherche d'un caractère d'un mot ou d'une phrase en japonais, chinois ou coréen pour obtenir des informations sur le ou les mots dans toutes les langues en même temps. Nous avons finalement privilégié la recherche en chinois (simplifié ou traditionnel), en maintenant les autres langues dans les résultats de recherche. Les différents sens des caractères sont indiqué en anglais, et parfois en français puisque nous visons un public d'apprenants de ces trois langues.

Options que nous n'avons finalement pas pu développer : 
- Recherche en japonais ou en coréen : difficulté dans la prise en charge des termes qui ne s'écrivent pas en caractères chinois
- Recherche en français ou anglais : il faudrait traduire entièrement la phrase ce qui peut amener de nombreuses erreurs de traductions

### État de l'art
- Naver : pas de page multilingue, possibilité de chercher dans plusieurs langues mais 1 page/langue → pas pratique pour faire une comparaison des sens des caractères dans différentes langues [lien](https://dict.naver.com/frkodict/#/search?query=%E9%9F%93)
- Daum 사전: à destination des coréens, [lien](https://dic.daum.net/search.do?q=%E9%9F%93)
- Dictionnaire de Hanja : [lien](https://koreanhanja.app/%e9%9f%93)
- Pleco (téléphone): uniquement chinois mais très bien fait, [lien](https://www.pleco.com)
- convertisseur chinois (classique, simplifié) - japonais: [lien](http://www.jcdic.com/chinese_convert/index.php)
- peut-être un API avec dictionnaires gratuits: [lien](https://glosbe.com/)
- comment écrire le caractère en chinois, les traits: [lien](https://github.com/skishore/makemeahanzi)
- chinois-français: [hanyudic](https://github.com/guilhemmariotte/HanYuDic) et [frcndict](https://github.com/Nilhcem/frcndict-android)
- dictionnaire chinois: [lien](http://dict.cn/)
- apprendre à écrire un caractère en japonais: [lien](https://kanjialive.com/) et [lien github](https://github.com/TashiiDesign/Kanji-Search)

### Ergonomie

Nous avons choisi un design simple et efficace pour notre application. 

Nous avons décidé de nommer notre application "DWJ Dictionary", reprenant les initiales de nos 3 noms de famille. Le nom de notre application forme le logo de celle-ci.

Nous avons un menu, reprenant le logo de notre dictionnaire. Celui-ci est cliquable et renvoie sur la page d'accueil, également accessible via le `Home`. Cette page d'accueil est la page sur laquelle tout se passe : l'utilisateur fait sa recherche et les résultats s'affiche sur cette page. Il y a également une seconde page accessible via cette barre de navigation : `About` présentant brièvement l'application et les personnes qui l'ont conçu.

Le site présente un fond coloré mais qui ne distrait pas l'oeil de l'utilisateur. Il s'agit d'une estampe japonaise tirée du Recueil des traditions de jadis et de nagère, exposé au Musée Cernuschi. Le contenu de la page est dans un cadre blanc aux contours arrondis, permettant de le faire contraster avec l'image de fond tout en gardant une certaine douceur.

La police utilisée est une police fournie par Bootstrap et soutenue par tous les navigateurs. L'application s'adapte également à toute taille d'écran (ordinateur, tablette, téléphone, etc). On peut également zoomer ou dézoomer le contenu sans que cela n'impacte la mise en page ni l'expérience utilisateur (pas de scroll horizontal notamment).

### Liste des fonctionnalités

#### côté interface (formulaires, visualisations, etc) 

#### côté serveur (librairies Python à utiliser, format des données à manipuler, bases de données)

### Conception : tâches et répartition

- Laura Darenne : dictionnaire chinois, design du site, de la partie chinoise et japonaise
- Florian Jacquot : dictionnaire japonais, mise en place du loader, rédaction du tutoriel
- Agathe Wallet : dictionnaire coréen, design du site et de la partie coréen, création des avatars



## Les visuels

