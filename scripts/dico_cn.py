
#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Ce fichier python permet d'aller chercher 
les informations du chinois pour le dictionnaire

Vous pouvez appeler le fichier comme ceci:
    $ python dico_cn.py [phrase ou mot]
    
Ex:
    $ python dico_cn.py 我來到北京 # chinois traditionnel
    $ python dico_cn.py 我来到北京 # chinois simplifié

Ex. avec chinois simplifié

- une liste de dictionnaire 
- un dictionnaire par token avec un ou plusieurs résultats indexés
    - 'n': un numéro de definition de 0 à n
    - 'characters': la clé n'existe que si le token fait plus de 1 caractère, 
        donne les définitions de chaque caractère se trouvant dans le dico
    de 0 à n tel que dico[0][0]['eng'] = '/I; me; my/'
    - 'words': la clé n'existe que s'il y a d'autres mots dans le dico contenant
        le token
    - si aucune definition n'a été trouvé à un token, même en le splitant,
    on obtient : {0: {'empty': token}}
- chaque dictionnaire comporte plusieurs clés :
    - 'eng': définition anglais, noté nan s'il n'y en a pas
    - 'fr': définition français, noté nan s'il n'y en a pas
    - 'py': le pinyin, la prononciation
    - 'simp': le caractère simplifié
    - 'trad': le caractère traditionnel
"""

import sys
from hanziconv import HanziConv
import jieba
import regex
import pandas as pd
from pprint import pprint


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
        # on va chercher les informations dans le dataframe
        dico_filtered = dico.loc[dico[column] == token].reset_index(drop=True)
        
        # si le dataframe est vide, on y va caractère par caractère
        if dico_filtered.empty:  
            for tok in token:
                # on va chercher les informations dans le dataframe une nouvelle fois
                dico_filtered = dico.loc[dico[column] == tok].reset_index(drop=True)
                
                # si le dataframe n'est pas vide
                if not dico_refiltered.empty:
                    #-- la partie définitions de 0 à n
                    infos = dico_refiltered.to_dict(orient="index")
                    #-- la partie 'caracters' n'existe pas
                    #-- la partie 'words'
                    words = dico[dico[column].str.contains(tok)][column].to_list()
                    if len(words) != 0 and words != [tok]:
                        infos["words"] = words
                    #-- on rajoute à notre liste
                    results.append(words)
                
                # sinon, on renvoie un dictionnaire quasi vide avec uniquement le caractère  
                else:
                    #-- on rajoute à notre liste
                    results.append({0: {'empty': tok}})
                    
        # sinon on continue la recherche d'informations
        else: 
            #-- la partie définitions de 0 à n
            infos = dico_filtered.to_dict(orient="index")
            #-- la partie 'caracters'
            if len(token) > 1:
                infos["characters"] = []
                for tok in token:
                    dico_refiltered = dico.loc[dico[column] == tok].reset_index(drop=True)
                    if not dico_refiltered.empty:
                        infos["characters"].append(dico_refiltered.to_dict(orient="index"))
            #-- la partie 'words'
            words = dico[dico[column].str.contains(token)][column].to_list()
            if len(words) != 0 and words != [token]:
                infos["words"] = words
            #-- on rajoute à notre liste
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
        return {}

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
    pprint(main())