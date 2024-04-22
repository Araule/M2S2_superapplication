#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Ce script extrait les informations du fichier XML   
    JMdict et les enregistre dans un fichier CSV.
    
    Exécution : 
    $ python3 dico_jp_build.py
"""

from lxml import etree as ET
import pandas as pd

ns = {"xml": "http://www.w3.org/XML/1998/namespace"}

def extract_jmdict_info_from_xml(xml_file_path="../JMdict.xml"):
    """
    Cette fonction extrait les informations du fichier XML JMdict et renvoie les termes, les lectures,
    et les traductions françaises et anglaises sous forme de listes.

    Args:
        xml_file_path (str): Chemin d'accès au fichier XML JMdict.

    Returns:
        list: Liste des termes.
        list: Liste des lectures.
        list: Liste des traductions françaises.
        list: Liste des traductions anglaises.
    """
    # Parse le fichier XML JMdict
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    TERMS = []
    READINGS = []
    SENSES_FRE = []
    SENSES_ENG = []

    # Parcourt chaque entrée dans le fichier XML JMdict
    # for entry in root.xpath('(.//entry)[position() <= 32]'):
    for entry in root.xpath('.//entry'):
        # Extrait les termes et les lectures de l'entrée
        terms = entry.xpath('.//k_ele/keb/text()') or entry.xpath('.//r_ele/reb/text()')
        
        for term in terms:
            readings = entry.xpath('.//r_ele/reb/text()')

            # Extrait les traductions françaises et anglaises de l'entrée
            senses_fre = [sense.xpath('.//text()')[0] for sense in entry.xpath('.//sense/gloss[@xml:lang="fre"]', namespaces=ns)]
            senses_eng = [sense.xpath('.//text()')[0] for sense in entry.xpath('.//sense/gloss[not(@xml:lang)]', namespaces=ns)]

            # Ajoute les informations aux listes correspondantes
            TERMS.append(term)
            READINGS.append('/'.join(readings))
            SENSES_FRE.append('/'.join(senses_fre) if senses_fre else "NULL")
            SENSES_ENG.append('/'.join(senses_eng) if senses_eng else "NULL")

    return TERMS, READINGS, SENSES_FRE, SENSES_ENG

if __name__ == '__main__':
    t, r, sfre, seng = extract_jmdict_info_from_xml()

    # Crée un DataFrame à partir des informations extraites et l'enregistre dans un fichier CSV
    df = pd.DataFrame({'tokens': t,
                       'readings': r,
                       'eng': seng,
                       'fra': sfre})

    df.to_csv('../data/jmdict.tsv', sep='\t', index=False)
