import os
import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd
import string


def terms_listup(scrape_url):
    # get page content response from the web using requests and beautifulsoup
    res = requests.get(scrape_url)
    soup = BeautifulSoup(res.content, "lxml")
    # print(soup)
    href_data = soup.find_all("a", href=True)
    print(href_data)

    return


def all_terms_listup():
    alphabet_list = string.ascii_lowercase

    for alphabet in alphabet_list:
        index_no_int = 4769351 + alphabet_list.index(alphabet)
        index_no_str = str(index_no_int)
        terms_url = f"https://www.investopedia.com/terms-beginning-with-{alphabet}-{index_no_str}"
        print(terms_url)
    return


terms_listup("https://www.investopedia.com/terms-beginning-with-a-4769351")
