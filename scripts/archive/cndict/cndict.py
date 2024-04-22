#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Ce fichier sert à réunier en un seul fichier tsv les 
    dictionnaires cedict et cfdict

    Le fichier python doit être appelé comme ceci:
            $ python cndict.py
            
    Dans le même dossier doit se trouver les fichiers 
    cedict.tsv et cfdict.tsv
"""

import pandas as pd

if __name__ == '__main__':
    
    # on va chercher le fichier tsv
    cfdict = pd.read_csv('cfdict.tsv', sep='\t', header=0)
    # on fait en sorte que toutes les valeurs de la colonne definitions soient de type str
    cfdict['fra'] = cfdict['fra'].astype(str)
    # on merge les ligne où les charactères et pinyin sont identiques mais les définitions différentes
    # on est obligé de le faire après avoir mis en minuscule tous les pinyins
    cfdict_merged = cfdict.groupby(['trad', 'simp', 'py'])['fra'].apply(lambda x: ''.join(x)).reset_index()
    
    cedict = pd.read_csv('cedict.tsv', sep='\t', header=0)
    cedict['eng'] = cedict['eng'].astype(str)
    cedict_merged = cedict.groupby(['trad', 'simp', 'py'])['eng'].apply(lambda x: ''.join(x)).reset_index()
    
    cndict = pd.merge(cedict_merged, cfdict_merged, on=['trad', 'simp', 'py'], how='outer')
    cndict.to_csv('cndict.tsv', sep='\t', index=False)
    
    # vérifier les quelques erreurs pour finir à la main la bdd tsv
    # au niveau des pinyins
    def filter_function(group):
        return len(group) >= 2 and group[['fra', 'eng']].isnull().any().any()

    result = cndict.groupby(['trad', 'simp']).filter(filter_function)
    result.to_csv('result.tsv', sep='\t', index=False)
