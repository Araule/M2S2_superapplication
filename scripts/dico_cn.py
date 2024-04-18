#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Ce fichier python permet d'aller chercher 
les informations du chinois pour le dictionnaire

Vous pouvez appeler le fichier comme ceci:
    $ python dico_cn.py [phrase ou mot]
    
Ex:
    $ python dico_cn.py 我來到北京清華大學 # chinois traditionnel
    $ python dico_cn.py 我来到北京清华大学 # chinois simplifié

Ex. avec chinois simplifié

- une liste de dictionnaire 
- un dictionnaire par token avec un ou plusieurs résultats indexés 
    de 0 à n tel que dico[0][0]['eng'] = '/I; me; my/' (premier 0 = premier token, 
    deuxième 0 = première entrée du dico, 'eng' = entrée du dico de la def)
- chaque dictionnaire comporte plusieurs clés :
    - 'eng': définition anglais, noté nan s'il n'y en a pas
    - 'fr': définition français, noté nan s'il n'y en a pas
    - 'py': le pinyin, la prononciation
    - 'simp': le caractère simplifié
    - 'trad': le caractère traditionnel
    - 'characters': la clé n'existe que si le token fait plus de 1 caractère, 
            donne les définitions de chaque caractère se trouvant dans le dico
            
[
 {0: {'eng': '/I; me; my/',
      'fra': '/je/moi/',
      'py': 'wo3',
      'simp': '我',
      'trad': '我'}},

 {0: {'eng': '/to arrive; to come/',
      'fra': '/arriver/venir/',
      'py': 'lai2 dao4',
      'simp': '来到',
      'trad': '來到'},
  'characters': [{0: {'eng': '/to come/(used as a substitute for a more '
                             'specific verb)/hither (directional complement '
                             'for motion toward the speaker, as in '
                             '回來|回来[hui2lai5])/ever since (as in '
                             '自古以來|自古以来[zi4gu3 yi3lai2])/for the past (amount '
                             'of time)/(prefix) the coming ...; the next ... '
                             '(as in 來世|来世[lai2shi4])/(between two verbs) in '
                             'order to/(after a round number) '
                             'approximately/(used after 得[de2] to indicate '
                             'possibility, as in 談得來|谈得来[tan2de5lai2], or '
                             'after 不[bu4] to indicate impossibility, as in '
                             '吃不來|吃不来[chi1bu5lai2])/',
                      'fra': '/venir/arriver/prochain/suivant/environ/',
                      'py': 'lai2',
                      'simp': '来',
                      'trad': '來'}},
                 {0: {'eng': '/to reach; to arrive/to leave for; to go to/to '
                             '(a place); until (a time); up to (a point)/(verb '
                             'complement indicating arriving at a place or '
                             'reaching a point)/considerate; thoughtful; '
                             'thorough/',
                      'fra': "/jusqu'à/arriver/parvenir/atteindre/aller à/",
                      'py': 'dao4',
                      'simp': '到',
                      'trad': '到'}}]},

 {0: {'eng': "/Beijing, capital of the People's Republic of China/",
      'fra': '/Pékin/Beijing/',
      'py': 'bei3 jing1',
      'simp': '北京',
      'trad': '北京'},
  'characters': [{0: {'eng': '/north/(classical) to be defeated/',
                      'fra': '/nord/',
                      'py': 'bei3',
                      'simp': '北',
                      'trad': '北'}},
                 {0: {'eng': '/surname Jing/Jing ethnic minority/abbr. for '
                             'Beijing 北京[Bei3jing1]/capital city of a '
                             'country/big/algebraic term for a large number '
                             '(old)/artificial mound (old)/',
                      'fra': '/capitale/Pékin/Beijing/',
                      'py': 'jing1',
                      'simp': '京',
                      'trad': '京'}}]},

 {0: {'eng': '/Tsinghua University, Beijing/National Tsing Hua University, '
             'Hsinchu, Taiwan/',
      'fra': '/Université Tsinghua/',
      'py': 'qing1 hua2 da4 xue2',
      'simp': '清华大学',
      'trad': '清華大學'},
  'characters': [{0: {'eng': "/Qing (Wade-Giles: Ch'ing) dynasty of China "
                             '(1644-1911)/surname Qing/(of water etc) clear; '
                             'clean/quiet; still/pure; uncorrupted/clear; '
                             'distinct/to clear; to settle (accounts)/',
                      'fra': '/clair/pur/distinct/net/liquider/',
                      'py': 'qing1',
                      'simp': '清',
                      'trad': '清'}},
                 {0: {'eng': '/old variant of 花[hua1]/flower/',
                      'fra': 'nan',
                      'py': 'hua1',
                      'simp': '华',
                      'trad': '華'},
                  1: {'eng': '/abbr. for China/magnificent/splendid/flowery/',
                      'fra': '/meilleure '
                             'partie/brillant/magnifique/splendide/somptueux/prospère/florissant/éclat/',
                      'py': 'hua2',
                      'simp': '华',
                      'trad': '華'},
                  2: {'eng': '/Mount Hua 華山|华山[Hua4 Shan1] in Shaanxi/surname '
                             'Hua/',
                      'fra': '/(nom de famille)/Mont Hua (Shaanxi)/',
                      'py': 'hua4',
                      'simp': '华',
                      'trad': '華'}},
                 {0: {'eng': '/big; large; great/older (than another '
                             'person)/eldest (as in 大姐[da4 jie3])/greatly; '
                             'freely; fully/(dialect) father/(dialect) uncle '
                             "(father's brother)/",
                      'fra': '/grand/massif/',
                      'py': 'da4',
                      'simp': '大',
                      'trad': '大'},
                  1: {'eng': '/see 大夫[dai4 fu5]/',
                      'fra': '/docteur/médecin/',
                      'py': 'dai4',
                      'simp': '大',
                      'trad': '大'}},
                 {0: {'eng': '/to learn/to study/to imitate/science/-ology/',
                      'fra': '/étudier/apprendre/science/-ologie/',
                      'py': 'xue2',
                      'simp': '学',
                      'trad': '學'}}]}]

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
