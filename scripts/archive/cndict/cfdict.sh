#########################################################
#
# ce fichier permet de transformer le dictionnaire 
# au format texte cfdict.u8 en fichier tsv cfdict.tsv
#
#########################################################
echo -e "trad\tsimp\tpy\tfra";

while read line; do # pour chaque entrée

    # on print les charactères chinois
    chars=${line%%\[*};
    for char in $chars; do
        echo -n $char;
        echo -ne "\t";
    done

    # on print le pinyin
    py=${line#*\[} # supprime la partie avant le premier [
    py=${py%%]*} # Supprime la partie après le premier ]
    echo -n "${py,,}";
    echo -ne "\t";

    # print les définitions françaises
    def=${line#*/}   # Supprime la partie avant la première barre oblique
    echo -n "/";
    echo $def; # on print avec retour à la ligne

    # avec vscod
    # - transformer r en r5 dans pinyin

done < cfdict.u8