#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Ce fichier python permet d'aller chercher 
les informations du chinois pour le dictionnaire

Vous pouvez appeler le fichier comme ceci:
    $ python dico_cn.py [phrase ou mot]
    
Ex:
    $ python dico_cn.py 我來到北京清華大學 # chinois traditionnel
    $ python dico_cn.py 我来到北京清华大学 # chinois simplifié
"""

import sys
from hanziconv import HanziConv
import jieba
import regex
import pandas as pd
import pprint


def infos(sent: str, dico: pd.core.frame.DataFrame, column: str):
    """
    Args:
        sent (str): tokens en chinois traditionnel ou simplifié
        dico (dict): le dictionnaire chinois, français, anglais
        column (str): trad ou simp en fonction des tokens donnés
    """
    # on split la phrase
    tokens = jieba.cut(sent, cut_all=False)
    results = []

    for token in tokens:
        
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

    # on vérifie que ce soit bien du chinois
    if not regex.match(r"[\p{Han}\p{Bopomofo}]+", sent, regex.UNICODE):
        print("\033[91mCe n'est pas du chinois\x1b[0m")
        sys.exit(1)

    # on vérifie si les caractères sont en chinois simplifié ou en chinois classique
    simplified_sent = HanziConv.toSimplified(sent)
    if simplified_sent == sent:
        type = 'simp'
    else:
        type = 'trad'

    # on obtient notre dictionnaire
    cndict = pd.read_csv("../data/cndict.tsv", sep="\t", header=0)
    cndict["trad"] = cndict["trad"].astype(str)
    cndict["simp"] = cndict["simp"].astype(str)
    cndict["py"] = cndict["py"].astype(str)
    cndict["fra"] = cndict["fra"].astype(str)
    cndict["eng"] = cndict["eng"].astype(str)

    return infos(sent, cndict, type)

if __name__ == "__main__":
    infos = main()
    pprint.pprint(infos)
