import sys
import requests
import regex
from pprint import pprint


def search_naver_dic(query_keyword):
    r = requests.get(f"https://koreanhanja.app/{query_keyword}")
    t = regex.sub(r"\s+"," ", r.text)
    results = regex.findall(r"<tr>.*?<\/tr>", t)
    pprint("".join(results))


def main(args=None):
    """The main routine."""
    if len(sys.argv) < 2:
        print("Usage : kdic [keyword]")
        sys.exit(0)

    query = sys.argv[1]
    try:
        search_naver_dic(query)
    except:
        print("Please check your internet connection.")


if __name__ == "__main__":
    main()