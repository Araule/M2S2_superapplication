import sys
import requests
import regex
from pprint import pprint


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

    pprint(dico)
    


def main(args=None):
    """The main routine."""
    if len(sys.argv) < 2:
        print("Usage : kdic [keyword]")
        sys.exit(0)

    query = sys.argv[1]
    try:
        build_dict(query)
    except:
        print("Please check your internet connection.")


if __name__ == "__main__":
    main()