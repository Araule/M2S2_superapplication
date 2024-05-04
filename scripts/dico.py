
#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Ce fichier python permet d'aller chercher les informations 
du chinois, du japonais et du coréen pour le dictionnaire

Vous pouvez appeler le fichier comme ceci:
    $ python dico_cn.py [phrase ou mot]

Ex: j'adore lire
    $ python dico_cn.py 我來到北京 # chinois traditionnel 
    $ python dico_cn.py 我喜歡閱讀 # chinois simplifié
"""

import sys
from pprint import pprint
from hanziconv import HanziConv
import jieba
import regex
import pandas as pd
import requests

#=== partie Agathe
def search_hanja_dic(query_keyword: str):
    r = requests.get(f"https://koreanhanja.app/{query_keyword}")
    t = regex.sub(r"\s+"," ", r.text)
    results = regex.findall(r"<tr>.*?<\/tr>", t)
    return results

def ko_main(query_keyword: str):
    dico={}
    r = search_hanja_dic(query_keyword)
    for entry in r:
        # link = regex.sub(r".*?href=\"(.*?)\">.*", r"\1", entry)
        hanja = regex.sub(r".*?<a.*?>(.*?)<\/a>.*", r"\1", entry)
        sens = regex.sub(r".*?<\/a><\/td>", "", entry)
        s = regex.findall(r"<td.*?>.*?<\/td>", sens)
        if len(s)>1:
            lecture = regex.sub(r"<td.*?>(.*?)<\/td>", r"\1", s[0])
            anglais = regex.sub(r"<td.*?>(.*?)<\/td>", r"\1", s[1])
            anglais = regex.sub(r"\(.*?\)", "", anglais)
            dico_sens = {lecture.strip(): anglais.strip()}
        else:
            sens = regex.sub(r"<td.*?>(.*?)\(?\d?\d?\)?<\/td>", r"\1", s[0])
            liste_mots = sens.split(",")
            dico_sens = {}
            lecture = []
            trad = []
            for mot in liste_mots:
                if mot.isascii():
                    mot = regex.sub(r"\(.*?\)", "", mot)
                    trad.append(mot.strip())
                else:
                    lecture.append(mot.strip())
            for m, t in zip(lecture, trad):
                dico_sens.update({m:t})
                
            
            # liste_sens = [lecture, trad]
        # Si l'entrée correspond à la requête et n'est pas encore dans le dico
        if hanja == query_keyword and "main" not in dico:
            dico.update({"main":{hanja:dico_sens}})
        # S'il y a déjà une entrée de la requête dans le dico, on ajoute les sens supp à la liste
        elif hanja == query_keyword and "main" in dico :
            dico["main"][hanja].update(dico_sens)
        # Si l'entrée ne correspond pas à la requête et qu'aucune entrée ne correspondant pas à la requête est dans le dico
        elif len(query_keyword) == 1:
            if hanja != query_keyword and "others" not in dico:
                dico.update({"others":{hanja:dico_sens}})
            elif hanja != query_keyword and "others" in dico and hanja not in dico["others"]: 
                dico['others'].update({hanja:dico_sens})
            else:
                dico['others'][hanja].update(dico_sens)
        else :
            if hanja != query_keyword and "xcomponent" not in dico:
                dico.update({"xcomponent":{hanja:dico_sens}})
            elif hanja != query_keyword and "xcomponent" in dico and hanja not in dico["xcomponent"]: 
                dico['xcomponent'].update({hanja:dico_sens})
            else:
                dico['xcomponent'][hanja].update(dico_sens)
    sorted_keys = sorted(dico.keys())
    return {k: dico[k] for k in sorted_keys}


#=== partie Florian
def jp_infos(sent: str, dico: pd.core.frame.DataFrame, column: str="tokens"):
    """
    Args:
        sent (str): tokens en chinois traditionnel ou simplifié
        dico (dict): le dictionnaire chinois, français, anglais
        column (str): trad ou simp en fonction des tokens donnés
    """
    results = []

    for token in sent:

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

def jp_main(query_keyword: str):

    sent = query_keyword

    # on vérifie que ce soit bien du japonais
    if not regex.match(r"[[\u3000-\u303f]|[\u3040-\u309f]|[\u30a0-\u30ff]|[\uff00-\uffef]|[\u4e00-\u9faf]|[\u3400-\u4dbf]]+",
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
    jmdict = pd.read_csv("./scripts/data/jmdict.tsv", sep="\t", header=0, dtype=dtype_dict)
    jmdict["tokens"] = jmdict["tokens"].astype(str)
    jmdict["readings"] = jmdict["readings"].astype(str)
    jmdict["eng"] = jmdict["eng"].astype(str)
    jmdict["fra"] = jmdict["fra"].astype(str)

    return jp_infos(sent, jmdict)


#== partie Laura
def group_tokens(tokens: list, entry: str)-> dict:
    """ groupe la liste de mots par longueur de mots

    Args:
        tokens (list): liste de mots en chinois
        token (str): entrée du dictionnaire

    Returns:
        dict: dictionnaire qui trie la liste 
        par longueur de mots
    """
    token_groups = {}
    for token in tokens:
        length = len(token)
        if token == entry: # pour ne pas avoir notre entrée dans la liste
            continue
        if length not in token_groups:
            token_groups[length] = []
        token_groups[length].append(token)
    return token_groups

def infos(sent: str, dico: pd.core.frame.DataFrame, column: str) -> dict:
    """ crée le dictionnaire chinois et renvoie 
    un dictionnaire complet avec toutes les informations 
    sur le chinois, le coréen et le japonais

    Args:
        sent (str): tokens en chinois traditionnel ou simplifié
        dico (dict): le dictionnaire chinois, français, anglais
        column (str): trad ou simp en fonction des tokens donnés
    """
    # on split la phrase
    tokens = jieba.cut(sent, cut_all=False)
    results = []

    for token in tokens:
        # notre dictionnaire pour le token
        infos = {}

        # on va chercher les informations dans le dataframe
        dico_filtered = dico.loc[dico[column] == token].reset_index(drop=True)

        # si le dataframe est vide, on y va caractère par caractère
        if dico_filtered.empty:
            for tok in token:
                # on va chercher les informations dans le dataframe une nouvelle fois
                dico_refiltered = dico.loc[dico[column] == tok].reset_index(drop=True)

                # si le dataframe n'est pas vide
                if not dico_refiltered.empty:
                    #-- la partie définitions chinois
                    cn_defs = dico_refiltered.to_dict(orient="index")
                    infos["chi"] = cn_defs
                    #-- la partie 'caracters' n'existe pas
                    #-- la partie 'words'
                    words = dico[dico[column].str.contains(tok)][column].to_list()
                    if len(words) != 0 and words != [tok]:
                        infos["words"] = group_tokens(words, tok)
                    #-- la partie  définitions coréen
                    if column != "trad":
                        new_tok = dico.loc[dico[column] == tok].reset_index(drop=True)["trad"].to_list()[0]
                        infos["kor"] = ko_main(new_tok) # a renvoyé un dict
                    else:
                        infos["kor"] = ko_main(tok) # a renvoyé un dict
                    #-- la partie  définitions japonais
                    infos["jap"] = jp_main(token) # a renvoyé un dict
                    #-- on rajoute à notre liste
                    results.append(infos)

                # sinon, on renvoie un dictionnaire quasi vide avec uniquement le caractère
                else:
                    #-- on rajoute à notre liste
                    results.append(tok)

        # sinon on continue la recherche d'informations
        else:
            #-- la partie définitions de 0 à n
            cn_defs = dico_filtered.to_dict(orient="index")
            infos["chi"] = cn_defs

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
                infos["words"] = group_tokens(words, token)
            #-- la partie  définitions coréen
            if column != "trad":
                new_token = dico.loc[dico[column] == token].reset_index(drop=True)["trad"].to_list()[0]
                infos["kor"] = ko_main(new_token) # a renvoyé un dict
            else:
                infos["kor"] = ko_main(token) # a renvoyé un dict
            #-- la partie  définitions japonais
            infos["jap"] = jp_main(token) # a renvoyé un dico
            #-- on rajoute à notre liste
            results.append(infos)

    return results

def main(sent: str) -> dict:
    """ 
    Args:
        sent (str): la phrase ou le mot rentré par l'utilisateur
        dans la barre de recherche

    Returns:
        dict: un dictionnaire complet avec toutes les informations 
        sur le chinois, le coréen et le japonais
    """

    # on vérifie que ce soit bien du chinois
    if not regex.match(r"[\p{Han}\p{Bopomofo}]+", sent, regex.UNICODE):
        return [] # renvoie une liste vide

    # on vérifie si les caractères sont en chinois simplifié ou en chinois classique
    simplified_sent = HanziConv.toSimplified(sent)
    if simplified_sent == sent:
        cntype = 'simp'
    else:
        cntype = 'trad'

    # on obtient notre dictionnaire
    cndict = pd.read_csv("./scripts/data/cndict.tsv", sep="\t", header=0)
    cndict["trad"] = cndict["trad"].astype(str)
    cndict["simp"] = cndict["simp"].astype(str)
    cndict["py"] = cndict["py"].astype(str)
    cndict["fra"] = cndict["fra"].astype(str)
    cndict["eng"] = cndict["eng"].astype(str)

    return infos(sent, cndict, cntype), cntype

# if __name__ == "__main__":

#     # on vérifie le nombre d'arguments
#     if len(sys.argv) != 2:
#         print("\033[91mIl faut une phrase, un mot ou un caractère en argument\x1b[0m")
#         sys.exit(1)

#     sent = sys.argv[1]

#     pprint(main(sent))
