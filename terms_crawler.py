import os
import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd
import string


def terms_listup(scrape_url):
    empty_list = []
    alphabet = scrape_url.split("-")[-2]
    print(alphabet)
    # get page content response from the web using requests and beautifulsoup
    res = requests.get(scrape_url)
    soup = BeautifulSoup(res.content, "lxml")
    # print(soup)
    for item in soup.find_all("a", href=True):
        href_item = item["href"]
        # print(href_item)
        term_url = "https://www.investopedia.com/terms/" + alphabet
        if term_url in href_item:
            print(href_item)
            empty_list.append(href_item)
            vocab_url_list = empty_list
    print(vocab_url_list)
    return vocab_url_list


def all_terms_listup():
    alphabet_list = string.ascii_lowercase
    for alphabet in alphabet_list:
        index_no_int = 4769351 + alphabet_list.index(alphabet)
        index_no_str = str(index_no_int)
        terms_url = f"https://www.investopedia.com/terms-beginning-with-{alphabet}-{index_no_str}"
        print(terms_url)
    return


terms_listup("https://www.investopedia.com/terms-beginning-with-b-4769352")
