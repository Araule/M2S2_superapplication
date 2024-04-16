#########################################################
#
# ce fichier permet de transformer le dictionnaire 
# au format texte cedict_ts.u8 en fichier tsv cedict.tsv
#
#########################################################
echo -e "trad\tsimp\tpy\teng";

while read line; do # pour chaque entrée

    # on print les charactères chinois
    chars=${line%%\[*};
    for char in $chars; do
        echo -n $char;
        echo -ne "\t";
    done

    # on print le pinyin
    py=${line#*\[} # supprime la partie avant le premier [
    py=${py%%\]*} # Supprime la partie après le premier ]
    echo -n "${py,,}";
    echo -ne "\t";

    # print les définitions anglaises
    def=${line#*/}   # Supprime la partie avant la première barre oblique
    echo -n "/";
    echo $def; # retour à la ligne

    # avec vscode :
    # - enlever les tiret

done < cedict.u8