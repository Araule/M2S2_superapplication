#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Ce fichier python permet d'aller chercher 
les informations du chinois pour le dictionnaire

Vous pouvez appeler le fichier comme ceci:
    $ python dico_cn.py [phrase ou mot]
"""

# possibilité de rajouter dico xml ou csv dans solr
# pour 

import sys
from hanziconv import HanziConv
import jieba
import regex

def infos_tradi(tokens: list):
    pass
    
def infos_simpli(tokens: list):
    pass

if __name__ == "__main__":
    
    # on vérifie le nombre d'arguments
    if len(sys.argv) != 2:
        print("\033[91mIl faut une phrase, un mot ou un caractère en argument")
        sys.exit(1)
        
    input = sys.argv[1]

    # on vérifie que ce soit bien du chinois
    if not regex.match(r'[\p{Han}\p{Bopomofo}]+', input, regex.UNICODE):
        print("\033[91mCe n'est pas du chinois")
        sys.exit(1)
    
    # on obtient nos deux versions du chinois
    simplified_input = HanziConv.toSimplified(input)
    traditional_input = HanziConv.toTraditional(input)
    
    # on tokenise nos deux versions
    simplified_tok = [tok for tok in jieba.cut(simplified_input)]
    traditional_tok = [tok for tok in jieba.cut(traditional_input)]
    
    # on lance la recherche d'informations
    infos_tradi(traditional_tok)
    infos_simpli(simplified_input)
    