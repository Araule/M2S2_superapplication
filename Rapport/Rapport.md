# M2S2_superapplication

Lien cahier des charges et notes : https://codimd.math.cnrs.fr/fKyJ-j26QqOfg0B82SRopg?both

## Présentation du projet
Ce projet d'application a été réalisé dans le cadre du cours Techniques Web du Master de Traitement Automatique des Langues (TAL) de l'Inalco. L'idée était de déployer une application autour du TAL, dans laquelle nous pourrions mettre en avant ce que nous avons vu en cours : programmation avec FastAPI, HTML, CSS, Javascript et Jquery. Aussi, nous avons décidé de développer un dictionnaire multilingue chinois/japonais/coréen

Ces trois langues, bien qu'ayant des systèmes d'écriture et des grammaires différentes, partagent un certain nombre de caractères communs, connus sous le nom de hanja en coréen et de kanji en japonais. Il existe également un vocabulaire commun, souvent emprunté au chinois, avec des lectures similaires ou identiques.

L'idée derrière une telle application est que de nombreux apprenants de ces langues rencontrent des difficultés à mémoriser les caractères et à comprendre les nuances de sens qu'ils peuvent exprimer dans chaque langue. En outre, les ressources existantes traitent généralement ces langues de manière isolée, sans mettre en évidence leurs liens et leurs similitudes, d'où cette approche plurilingue.

## Cahier des charges

### Les objectifs et le public cible

L'objectif était donc de créer une application dans laquelle l'utilisateur pourrait faire une recherche d'un caractère d'un mot ou d'une phrase en japonais, chinois ou coréen pour obtenir des informations sur le ou les mots dans toutes les langues en même temps. Nous avons finalement privilégié la recherche en chinois (simplifié ou traditionnel), en maintenant les autres langues dans les résultats de recherche. Les différents sens des caractères sont indiqués en anglais, et parfois en français puisque nous visons un public d'apprenants de ces trois langues.

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

Nous avons un menu, reprenant le logo de notre dictionnaire. Celui-ci est cliquable et renvoie sur la page d'accueil, également accessible via le `Home`. Cette page d'accueil est la page sur laquelle tout se passe : l'utilisateur fait sa recherche et les résultats s'affiche sur cette page. Il y a également une seconde page accessible via cette barre de navigation : `About` présentant brièvement l'application et les personnes qui l'ont conçues.

Le site présente un fond coloré mais qui ne distrait pas l'oeil de l'utilisateur. Il s'agit d'une estampe japonaise tirée du Recueil des traditions de jadis et de nagère, exposé au Musée Cernuschi. Le contenu de la page est dans un cadre blanc aux contours arrondis, permettant de le faire contraster avec l'image de fond tout en gardant une certaine douceur.

La police utilisée est une police fournie par Bootstrap et soutenue par tous les navigateurs. L'application s'adapte également à toute taille d'écran (ordinateur, tablette, téléphone, etc). On peut également zoomer ou dézoomer le contenu sans que cela n'impacte la mise en page ni l'expérience utilisateur (pas de scroll horizontal notamment). Le contenu complémentaire est également caché pour éviter un surplus d'informations sur la page mais sont accessibles en un clic via des accordéons.

### Liste des fonctionnalités

#### Côté interface (formulaires, visualisations, etc.)

* **Une barre de recherche** permettant de saisir un caractère, un mot ou une phrase en chinois simplifié ou traditionnel. La barre de recherche est située en haut de la page d'accueil et permet à l'utilisateur de saisir facilement sa requête. La recherche se lance automatiquement lorsque l'utilisateur appuie sur la touche "Entrée" ou clique sur l'icône de loupe.
* **Une page d'accueil** affichant les résultats de la recherche, par langue (chinois, japonais, coréen) et par type de résultat (caractère, mot). Les résultats de la recherche sont affichés sous forme de liste séparée par langue, avec pour chaque résultat son écriture dans sa langue, sa prononciation (en pinyin, hiragana ou hangul), sa traduction en français et en anglais.
* **Une page "About"** présentant l'application et les personnes qui l'ont conçue. La page "About" est accessible depuis le menu principal de l'application.
* **Un tutoriel** expliquant comment utiliser l'application et présentant les différentes fonctionnalités. Le tutoriel est accessible depuis la page d'accueil.
* **Un loader** indiquant à l'utilisateur que la recherche est en cours. Le loader est affiché à l'écran lorsque l'utilisateur effectue une recherche et disparaît lorsque les résultats sont affichés. Il permet à l'utilisateur de savoir que l'application est en train de traiter sa requête et qu'il doit patienter quelques instants.
* **Des accordéons** permettant d'afficher ou de masquer des informations complémentaires sur les résultats de la recherche (mots contenant le caractère recherché). L'utilisateur peut cliquer sur le titre de l'accordéon pour afficher ou masquer son contenu.

#### Côté serveur (librairies Python à utiliser, format des données à manipuler, bases de données)

* De la librairie Python **fastapi** :
    * utilisation de **FastAPI** pour créer l'API de l'application et gérer les requêtes HTTP entrantes et sortantes ;
    * utilisation de **Jinja2Templates** pour le rendu des templates HTML. Jinja2 est une librairie Python permettant de générer des templates HTML dynamiques. Elle a été utilisée pour générer les pages HTML de l'application en fonction des données récupérées depuis la base de données ;
    * utilisation de **StaticFiles** pour utiliser des fichiers dits statiques tels que des images, des feuilles de styles CSS et des fichier JavaScript ; 
    * utilisation de **HTMLResponse** qui permet de renvoyer une réponse HTTP avec un corps HTML.
* Utilisation de la librairie **requests** pour les requêtes HTTP vers l'API externe de `koreanhanja.app`.
* Utilisation de la librairie **Pandas** pour la manipulation des données. Elle a été utilisée pour manipuler les données récupérées depuis les base de données du chinois et du japonais pour les mettre en forme avant de les envoyer vers l'interface utilisateur.
* Utilisation de la librairie **Regex** pour la vérification de la validité des caractères chinois saisis par l'utilisateur. Regex est aussi utilisé pour extraire les informations pertinentes des résultats de la recherche de `Koreanhanja.app`.
* Utilisation de la librairie **HanziConv** pour la conversion entre les caractères chinois simplifiés et traditionnels. 
* Utilisation de la librairie **Jieba** pour la segmentation des phrases/mots en chinois entrée par l'utilisateur. 
* Utilisation de **base de données** au format tsv:
    * CFDICT: Base de données "chinois - français" [https://chine.in/mandarin/dictionnaire/CFDICT/]
    * CC-DICT: Base de données "chinois - anglais" [https://www.mdbg.net/chinese/dictionary?page=cedict]

### Conception : tâches et répartition

- Laura Darenne : dictionnaire chinois, design du site, de la partie chinoise et japonaise
- Florian Jacquot : dictionnaire japonais, mise en place du loader, rédaction du tutoriel
- Agathe Wallet : dictionnaire coréen, design du site et de la partie coréenne, création des avatars

## Les visuels

![page d'accueil](./home_1.jpg "page d'accueil")

![page de résultats](./home_2.jpg "page de résultats")

![page about](./about.jpg "page about")