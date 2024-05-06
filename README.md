# M2S2_superapplication

Ce projet a été réalisé dans le cadre du cours de Technique Web du Master de Traitement Automatique des Langues de l'Inalco. 

Il s'agit d'un dictionnaire plurilingue dans lequel vous pouvez entrer un caractère, un mot ou une phrase en chinois (classique ou simplifié) et le dictionnaire vous retournera son sens chinois, mais également japonais et coréen, avec une traduction des sens en anglais et/ou français pour une meilleure compréhension. Cela vous permettra ainsi de saisir les subtilités de l'utilisation des caractères chinois dans telle ou telle langue.

---

Pour lancer notre application, clonez ce répertoire via votre terminal.
```bash
git clone https://github.com/Araule/M2S2_superapplication.git
```
Placez-vous dans le répertoire du projet : 
```bash
cd M2S2_superapplication
```
Vous pouvez maintenant installer les bibliothèques nécessaires via le `requirements.txt`.
```bash
pip install -r requirements.txt 
```
Pour lancer l'application, tapez simplement la commande suivante :
```bash
uvicorn main:app --reload
```
Vous pourrez ensuite cliquer sur l'url indiquée sur votre terminal.

Si vous avez déployé une autre application avant la nôtre, n'hésitez pas à faire un `CTRL+MAJ+R` pour que le cache de la précédente application soit vidé et que notre application s'affiche telle qu'elle a été conçue. Merci et bonne navigation !


## Groupe
- Laura Darenne (@Araule)
- Florian Jacquot (@FlorianJacquot)
- Agathe Wallet (@AgatheWallet)
