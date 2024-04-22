import sys
import requests
import regex
from pprint import pprint

"""
Exécution : python3 dico_ko.py <token en hanja>
"""

def search_hanja_dic(query_keyword: str):
    r = requests.get(f"https://koreanhanja.app/{query_keyword}")
    t = regex.sub(r"\s+"," ", r.text)
    results = regex.findall(r"<tr>.*?<\/tr>", t)
    return results


def build_dict(query_keyword: str):
    dico={}
    r = search_hanja_dic(query_keyword)
    for entry in r:
        link = regex.sub(r".*?href=\"(.*?)\">.*", r"\1", entry)
        hanja = regex.sub(r".*?<a.*?>(.*?)<\/a>.*", r"\1", entry)
        sens = regex.sub(r".*?<\/a><\/td>", "", entry)
        s = regex.findall(r"<td.*?>.*?<\/td>", sens)
        if len(s)>1:
            lecture = regex.sub(r"<td.*?>(.*?)<\/td>", r"\1", s[0])
            a = regex.sub(r"<td.*?>(.*?)<\/td>", r"\1", s[1])
            sens = f"{lecture}, {a}"
        else:
            sens = regex.sub(r"<td.*?>(.*?)\(?\d?\d?\)?<\/td>", r"\1", s[0])
        dico.update({hanja:(link, sens.strip())})

    return dico


def main(query):
    """The main routine."""
    if len(sys.argv) < 2:
        print("Usage : kdic [keyword]")
        sys.exit(0)

    try:
        pprint(build_dict(query))
    except:
        print("Please check your internet connection.")


if __name__ == "__main__":
    main(sys.argv[1])