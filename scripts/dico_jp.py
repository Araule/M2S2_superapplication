#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Ce fichier python permet d'aller chercher 
les informations du japonais pour le dictionnaire

Vous pouvez appeler le fichier comme ceci:
    $ python dico_jp.py [phrase ou mot]
    
Ex:
    $ python3 dico_jp_application.py 猫が大好きだよ！
"""

import sys
import MeCab
import regex
import pandas as pd
import pprint


def infos(sent: str, dico: pd.core.frame.DataFrame, column: str="tokens"):
    """
    Args:
        sent (str): tokens en chinois traditionnel ou simplifié
        dico (dict): le dictionnaire chinois, français, anglais
        column (str): trad ou simp en fonction des tokens donnés
    """
    # on split la phrase
    wakati = MeCab.Tagger("-Owakati")
    # tokens = wakati.parse(sent).split()
    parser = wakati.parseToNode(sent)
    lemmatized_sent = []
    
    while parser:
        features = parser.feature.split(',')
        lemma = features[7]
        lemmatized_sent.append(lemma)
        parser = parser.next
    
    results = []

    for token in lemmatized_sent:
        
        #-- d'abord, les informations sur le token
        # on va chercher les ligne correspondant au token
        dico_filtered = dico.loc[dico[column] == token].reset_index(drop=True)

        if dico_filtered.empty:  # si le dataframe est vide, on y va caractère par caractère
            for tok in token:
                dico_refiltered = dico.loc[dico[column] == tok].reset_index(drop=True)
                if not dico_refiltered.empty:
                    results.append(dico_refiltered.to_dict(orient="index"))

        else: # s'il n'est pas vide, on obtient les infos de chaque caractère également
            infos = dico_filtered.to_dict(orient="index")
            #-- puis, les infos supplémentaires sur chaque caractère s'il y en a
            if len(token) > 1:
                infos["characters"] = []
                for tok in token:
                    dico_refiltered = dico.loc[dico[column] == tok].reset_index(drop=True)
                    if not dico_refiltered.empty:
                        infos["characters"].append(dico_refiltered.to_dict(orient="index"))
                        
            results.append(infos)

    return results


def main():
    # on vérifie le nombre d'arguments
    if len(sys.argv) != 2:
        print("\033[91mIl faut une phrase, un mot ou un caractère en argument\x1b[0m")
        sys.exit(1)

    sent = sys.argv[1]

    # on vérifie que ce soit bien du japonais
    if not regex.match(r"[[\u3000-\u303f]|[\u3040-\u309f]|[\u30a0-\u30ff]|[\uff00-\uffef]|[\u4e00-\u9faf]|[\u3400-\u4dbf]]+",
        # r"[\p{Hiragana}\p{Katakana}\p{Han}" # pour les hiragana, katakana et caractères chinois
        #                     r"[\x2E80-\x2FD5]" # pour les radicaux de kanjis (caractères chinois)
        #                     r"[\xFF5F-\xFF9F]" # pour les katakana et les ponctuations (half-width)
        #                     r"[\x3000-\x303F]" # les symboles et ponctuations japonaises
        #                     r"[\x31F0-\x31FF\x3220-\x3243\x3280-\x337F]" # pour les autres caractères japonaise (miscellaneous)
        #                     r"[\xFF01-\xFF5E]]+", # pour les caractères latin (full-width)    
                        sent, regex.UNICODE):
        print("\033[91mCe n'est pas du japonais\x1b[0m")
        sys.exit(1)

    # spécifier les types de données des colonnes
    dtype_dict = {
        'tokens': str,
        'readings': str,
        'eng': str,
        'fra': str
    }
    # on obtient notre dictionnaire
    jmdict = pd.read_csv("../data/jmdict.tsv", sep="\t", header=0, dtype=dtype_dict)
    jmdict["tokens"] = jmdict["tokens"].astype(str)
    jmdict["readings"] = jmdict["readings"].astype(str)
    jmdict["eng"] = jmdict["eng"].astype(str)
    jmdict["fra"] = jmdict["fra"].astype(str)

    return infos(sent, jmdict)

if __name__ == "__main__":
    infos = main()
    pprint.pprint(infos)
